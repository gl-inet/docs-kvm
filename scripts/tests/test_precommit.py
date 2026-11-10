"""Pre-commit regression tests in isolated Git repositories."""
import contextlib
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import anchors
import i18n_check
import precommit
import translation_delta


class PrecommitTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.old = Path.cwd()
        self.root = Path(self.temp.name).resolve()
        os.chdir(self.root)
        self.git("init", "-q")
        self.git("config", "user.email", "test@example.invalid")
        self.git("config", "user.name", "Test")
        self.git("config", "core.autocrlf", "false")
        self.git("config", "core.hooksPath", ".disabled-hooks")
        self.source = "docs/en/docs/page.md"
        self.target = "docs/de/docs/page.md"
        self.legal = "docs/de/docs/safety_information.md"
        self.put(self.source, "# English {#page}\n\nOriginal.\n")
        self.put(self.target, "# Deutsch {#page}\n\nText.\n\n## Sicherheit {#safety-information}\nApproved wording.\n")
        self.put(self.legal, "# Sicherheit {#safety-information}\n\nApproved standalone wording.\n")
        for lang in ("en", "de"):
            self.put(f"docs/{lang}/mkdocs.yml", "plugins: []\n")
        self.update_cache()
        self.git("add", ".")
        self.git("commit", "-qm", "fixture")
        self.patches = [
            patch.object(anchors, "REPO_ROOT", self.root),
            patch.object(anchors, "DOCS_ROOT", self.root / "docs"),
            patch.object(i18n_check, "DOCS_ROOT", self.root / "docs"),
            patch.object(i18n_check, "ALLOWLIST_PATH", self.root / "allowlist.yml"),
        ]
        for item in self.patches:
            item.start()

    def tearDown(self):
        for item in reversed(self.patches):
            item.stop()
        os.chdir(self.old)
        self.temp.cleanup()

    def git(self, *args):
        return subprocess.check_output(["git", *args], stderr=subprocess.STDOUT).decode("utf-8")

    def put(self, path, text):
        target = Path(path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(text.encode("utf-8"))

    def update_cache(self):
        cache = {self.source: {"targets": {"de": {
            "source_hash": translation_delta.source_hash(Path(self.source)),
            "target_hash": translation_delta.target_hash(Path(self.target)),
        }}}}
        self.put(translation_delta.CACHE_FILE, json.dumps(cache))
        self.git("add", translation_delta.CACHE_FILE)

    def run_hook(self, *args):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            result = precommit.main(list(args))
        return result, output.getvalue()

    def test_auto_add_ids_and_stage_without_changing_rendered_urls(self):
        text = '# English {#page}\r\n\r\n## New *heading* {.extra}\r\n\r\n## New *heading*\r\n\r\n```md\r\n# Not a heading\r\n```\r\n'
        self.put(self.source, text)
        page = anchors.load_page("en", self.root / self.source)
        ids_before = page.rendered_ids
        self.git("add", self.source)
        code, output = self.run_hook()
        self.assertEqual(0, code, output)
        after = Path(self.source).read_bytes()
        self.assertIn(b"{#new-heading .extra}\r\n", after)
        self.assertIn(b"{#new-heading_1}\r\n", after)
        self.assertIn(b"# Not a heading\r\n", after)
        self.assertEqual(ids_before, anchors.load_page("en", self.root / self.source).rendered_ids)
        self.assertEqual(after.decode(), self.git("show", ":" + self.source))
        self.assertEqual("", self.git("diff", "--name-only"))
        self.assertEqual(0, self.run_hook()[0])

    def test_partial_stage_never_edits_or_stages_work_in_progress(self):
        staged = "# English {#page}\n\n## New heading\n"
        self.put(self.source, staged)
        self.git("add", self.source)
        working = staged + "\nUnstaged paragraph.\n"
        self.put(self.source, working)
        code, output = self.run_hook()
        self.assertEqual(1, code, output)
        self.assertIn("unstaged changes", output)
        self.assertEqual(staged, self.git("show", ":" + self.source))
        self.assertEqual(working, Path(self.source).read_text())

    def test_unstaged_id_fix_cannot_hide_missing_staged_id(self):
        staged = "# English {#page}\n\n## New heading\n"
        self.put(self.source, staged)
        self.git("add", self.source)
        working = staged.replace("## New heading", "## New heading {#new-heading}")
        self.put(self.source, working)
        code, output = self.run_hook()
        self.assertEqual(1, code, output)
        self.assertIn("heading has no explicit ID", output)
        self.assertEqual(staged, self.git("show", ":" + self.source))
        self.assertEqual(working, Path(self.source).read_text())

    def test_closing_atx_hashes_do_not_become_visible_text(self):
        text = "# English {#page}\n\n## New heading ##\n"
        self.put(self.source, text)
        before = anchors.render_ids(text.splitlines(keepends=True))
        import markdown
        html_before = markdown.markdown(text, extensions=anchors.MD_EXTENSIONS,
                                        extension_configs=anchors.MD_EXTENSION_CONFIGS)
        self.git("add", self.source)
        code, output = self.run_hook()
        self.assertEqual(0, code, output)
        after = Path(self.source).read_text()
        html_after = markdown.markdown(after, extensions=anchors.MD_EXTENSIONS,
                                       extension_configs=anchors.MD_EXTENSION_CONFIGS)
        self.assertEqual(html_before, html_after)
        self.assertEqual(before.ids, anchors.render_ids(after.splitlines(keepends=True)).ids)
        self.assertIn("## New heading {#new-heading}", after)

    def test_preserve_existing_id_even_when_title_changes(self):
        text = "# Different title {#page}\n"
        self.put(self.source, text)
        self.git("add", self.source)
        self.assertEqual(0, self.run_hook()[0])
        self.assertEqual(text, Path(self.source).read_text())

    def test_render_mismatch_is_not_auto_fixed(self):
        self.put(self.source, "# English {#page}\n\nSetext heading\n==============\n\n## New heading\n")
        self.git("add", self.source)
        before = Path(self.source).read_bytes()
        code, _ = self.run_hook()
        self.assertEqual(1, code)
        self.assertEqual(before, Path(self.source).read_bytes())

    def test_new_english_unicode_filename(self):
        path = "docs/en/docs/überblick.md"
        self.put(path, "# Overview\n")
        self.git("add", path)
        self.assertEqual(0, self.run_hook()[0])
        self.assertIn("{#overview}", self.git("show", ":" + path))

    def test_staged_legal_edit_is_blocked_despite_unstaged_restoration(self):
        approved = Path(self.target).read_text()
        self.put(self.target, approved.replace("Approved wording", "Changed wording"))
        self.git("add", self.target)
        self.put(self.target, approved)
        code, output = self.run_hook()
        self.assertEqual(1, code, output)
        self.assertIn("[protected-section]", output)

    def test_unstaged_legal_edit_does_not_block_staged_nonlegal_edit(self):
        approved = Path(self.target).read_text()
        staged = approved.replace("Text.", "Anderer Text.")
        self.put(self.target, staged)
        self.git("add", self.target)
        self.update_cache()
        self.put(self.target, staged.replace("Approved wording", "Unstaged wording"))
        code, output = self.run_hook()
        self.assertEqual(0, code, output)

    def test_standalone_legal_edit_and_delete_without_english_counterpart(self):
        self.put(self.legal, "# Sicherheit {#safety-information}\nChanged.\n")
        self.git("add", self.legal)
        code, output = self.run_hook()
        self.assertEqual(1, code, output)
        self.assertIn("[protected-section]", output)
        self.git("rm", "-f", self.legal)
        code, output = self.run_hook()
        self.assertEqual(1, code, output)
        self.assertIn("[protected-section]", output)

    def test_legal_page_rename_preserves_content_but_does_not_hide_edits(self):
        new = "docs/de/docs/sicherheit.md"
        self.git("mv", self.legal, new)
        self.assertEqual(0, self.run_hook()[0])
        self.put(new, Path(new).read_text().replace("Approved standalone", "Edited standalone"))
        self.git("add", new)
        code, output = self.run_hook()
        self.assertEqual(1, code, output)
        self.assertIn("[protected-section]", output)

    def test_legal_page_moved_out_of_language_is_removal(self):
        self.git("mv", self.legal, "safety_information.md")
        code, output = self.run_hook()
        self.assertEqual(1, code, output)
        self.assertIn("[protected-section]", output)

    def test_legal_checks_cannot_be_allowlisted(self):
        self.put("allowlist.yml", "- lang: de\n  page: safety_information.md\n  check: protected-section\n  reason: Test bypass\n")
        self.put(self.legal, "# Sicherheit {#safety-information}\nChanged.\n")
        self.git("add", self.legal)
        code, output = self.run_hook()
        self.assertEqual(1, code, output)
        self.assertIn("[protected-section]", output)

    def test_changed_translation_requires_matching_staged_cache(self):
        approved = Path(self.target).read_text()
        self.put(self.target, approved.replace("Text.", "Anderer Text."))
        self.git("add", self.target)
        code, output = self.run_hook()
        self.assertEqual(1, code, output)
        self.assertIn("translation cache does not match staged source/target", output)
        self.assertIn("translation_delta.py mark", output)
        self.update_cache()
        code, output = self.run_hook()
        self.assertEqual(0, code, output)

    def test_invalid_cache_only_commit_is_blocked(self):
        self.put(translation_delta.CACHE_FILE, "not valid JSON")
        self.git("add", translation_delta.CACHE_FILE)
        code, output = self.run_hook()
        self.assertEqual(1, code, output)
        self.assertIn("invalid staged translation cache", output)

    def test_pr_mode_reports_missing_ids_without_editing_or_staging(self):
        base = self.git("rev-parse", "HEAD").strip()
        committed = "# English {#page}\n\n## Missing ID\n"
        self.put(self.source, committed)
        self.git("add", self.source)
        self.git("commit", "-qm", "missing ID")
        # Even staged and unstaged repairs must not mask the committed error.
        self.put(self.source, committed.replace("## Missing ID", "## Missing ID {#missing-id}"))
        self.git("add", self.source)
        self.put(self.source, Path(self.source).read_text() + "\nWork in progress.\n")
        before = self.git("status", "--porcelain=v1"), Path(self.source).read_bytes(), self.git("write-tree")
        code, output = self.run_hook("--base", base)
        self.assertEqual(1, code, output)
        self.assertIn("heading has no explicit ID", output)
        self.assertNotIn("added heading IDs", output)
        self.assertNotIn("--no-verify", output)
        self.assertEqual(before, (self.git("status", "--porcelain=v1"), Path(self.source).read_bytes(), self.git("write-tree")))

    def test_pr_mode_checks_committed_translation_cache_not_index_repairs(self):
        base = self.git("rev-parse", "HEAD").strip()
        self.put(self.target, Path(self.target).read_text().replace("Text.", "Anderer Text."))
        self.git("add", self.target)
        self.git("commit", "-qm", "translation without record")
        self.update_cache()
        code, output = self.run_hook("--base", base)
        self.assertEqual(1, code, output)
        self.assertIn("does not match committed source/target", output)

    def test_pr_mode_ignores_uncommitted_source_target_and_cache_errors(self):
        base = self.git("rev-parse", "HEAD").strip()
        self.put(self.target, Path(self.target).read_text().replace("Text.", "Anderer Text."))
        self.update_cache()
        self.git("add", self.target)
        self.git("commit", "-qm", "reviewed translation")
        for path in (self.source, self.target):
            self.put(path, "# Uncommitted heading without ID\n")
        self.put(translation_delta.CACHE_FILE, "not JSON")
        self.git("add", ".")
        code, output = self.run_hook("--base", base)
        self.assertEqual(0, code, output)

    def test_pr_mode_reads_related_anchor_pages_from_head(self):
        base = self.git("rev-parse", "HEAD").strip()
        self.put(self.source, "# English {#page}\n\n[Other](other.md#other)\n")
        self.put("docs/en/docs/other.md", "# Other {#other}\n")
        self.git("add", ".")
        self.git("commit", "-qm", "linked page")
        self.put("docs/en/docs/other.md", "# Uncommitted {#different}\n")
        code, output = self.run_hook("--base", base)
        self.assertEqual(0, code, output)

    def test_pr_mode_uses_committed_redirects_not_working_tree(self):
        base = self.git("rev-parse", "HEAD").strip()
        self.put("docs/en/mkdocs.yml", "plugins:\n  - redirects:\n      redirect_maps:\n        old.md: page.md\n")
        self.git("add", ".")
        self.git("commit", "-qm", "redirect")
        self.put("docs/en/mkdocs.yml", "plugins:\n  - redirects:\n      redirect_maps:\n        old.md: missing.md\n")
        code, output = self.run_hook("--base", base)
        self.assertEqual(0, code, output)

    def test_pr_mode_english_only_allows_pending_translations(self):
        base = self.git("rev-parse", "HEAD").strip()
        self.put(self.source, Path(self.source).read_text() + "\nNew English paragraph.\n")
        self.git("add", self.source)
        self.git("commit", "-qm", "English only")
        code, output = self.run_hook("--base", base)
        self.assertEqual(0, code, output)

    def test_pr_mode_blocks_committed_legal_delete_despite_restored_worktree(self):
        base = self.git("rev-parse", "HEAD").strip()
        approved = Path(self.legal).read_text()
        self.git("rm", self.legal)
        self.git("commit", "-qm", "delete legal")
        self.put(self.legal, approved)
        code, output = self.run_hook("--base", base)
        self.assertEqual(1, code, output)
        self.assertIn("[protected-section]", output)

    def test_pr_mode_preserves_rename_sources_including_unicode(self):
        base = self.git("rev-parse", "HEAD").strip()
        new = "docs/de/docs/sicherheitsüberblick.md"
        self.git("mv", self.legal, new)
        self.git("commit", "-qm", "rename legal")
        code, output = self.run_hook("--base", base)
        self.assertEqual(0, code, output)
        self.put(new, Path(new).read_text().replace("Approved standalone", "Changed standalone"))
        self.git("add", new)
        self.git("commit", "-qm", "edit legal")
        code, output = self.run_hook("--base", base)
        self.assertEqual(1, code, output)
        self.assertIn("[protected-section]", output)

    def test_pr_mode_uses_merge_base_for_legal_comparison(self):
        original = self.git("rev-parse", "HEAD").strip()
        self.put(self.legal, "# Sicherheit {#safety-information}\n\nDifferent on base branch.\n")
        self.git("add", self.legal)
        self.git("commit", "-qm", "base branch legal update")
        base = self.git("rev-parse", "HEAD").strip()
        self.git("checkout", "-q", "--detach", original)
        self.put(self.target, Path(self.target).read_text().replace("Text.", "Anderer Text."))
        self.update_cache()
        self.git("add", self.target)
        self.git("commit", "-qm", "PR branch update")
        code, output = self.run_hook("--base", base)
        self.assertEqual(0, code, output)

    def test_pr_mode_invalid_ref_fails_instead_of_succeeding(self):
        code, output = self.run_hook("--base", "refs/heads/not-a-real-base")
        self.assertEqual(1, code, output)
        self.assertIn("unable to check submitted documentation", output)

    def test_pr_mode_invalid_committed_cache_cannot_be_hidden_by_repair(self):
        base = self.git("rev-parse", "HEAD").strip()
        self.put(translation_delta.CACHE_FILE, "not JSON")
        self.git("add", translation_delta.CACHE_FILE)
        self.git("commit", "-qm", "invalid record")
        self.update_cache()
        code, output = self.run_hook("--base", base)
        self.assertEqual(1, code, output)
        self.assertIn("invalid committed translation cache", output)

    def test_pr_mode_committed_binary_assets_use_head_hashes(self):
        base = self.git("rev-parse", "HEAD").strip()
        source, target = "docs/en/docs/picture.png", "docs/de/docs/picture.png"
        raw = b"\x89PNG\r\n\x00\xff"
        for path in (source, target):
            Path(path).write_bytes(raw)
        cache = {source: {"targets": {"de": {
            "source_hash": translation_delta.hash_bytes(Path(source), raw),
            "target_hash": translation_delta.hash_bytes(Path(target), raw),
        }}}}
        self.put(translation_delta.CACHE_FILE, json.dumps(cache))
        self.git("add", ".")
        self.git("commit", "-qm", "binary translation")
        Path(target).write_bytes(b"uncommitted corruption")
        code, output = self.run_hook("--base", base)
        self.assertEqual(0, code, output)

    def test_pr_mode_rejects_documentation_symlinks_without_following_them(self):
        base = self.git("rev-parse", "HEAD").strip()
        oid = subprocess.check_output(["git", "hash-object", "-w", "--stdin"],
                                      input=b"../../../../outside.md").decode().strip()
        self.git("update-index", "--add", "--cacheinfo", "120000", oid, "docs/en/docs/link.md")
        self.git("commit", "-qm", "symlink")
        code, output = self.run_hook("--base", base)
        self.assertEqual(1, code, output)
        self.assertIn("documentation must be a regular file", output)

    def test_pr_snapshot_is_not_filtered_by_export_attributes(self):
        self.put(".gitattributes", "docs/en/docs/page.md export-ignore\n")
        self.git("add", ".gitattributes")
        self.git("commit", "-qm", "export attribute")
        with precommit.committed_docs("HEAD"):
            self.assertEqual(self.git("show", "HEAD:" + self.source),
                             (anchors.REPO_ROOT / self.source).read_text())

    def test_pr_mode_restores_checker_roots(self):
        roots = anchors.REPO_ROOT, anchors.DOCS_ROOT, i18n_check.DOCS_ROOT, i18n_check.ALLOWLIST_PATH
        self.assertEqual((0, ""), self.run_hook("--base", "HEAD"))
        self.assertEqual(roots, (anchors.REPO_ROOT, anchors.DOCS_ROOT, i18n_check.DOCS_ROOT, i18n_check.ALLOWLIST_PATH))

    def test_empty_index_does_nothing(self):
        self.assertEqual((0, ""), self.run_hook())


if __name__ == "__main__":
    unittest.main()
