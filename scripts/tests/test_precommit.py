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

    def run_hook(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            result = precommit.main()
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

    def test_empty_index_does_nothing(self):
        self.assertEqual((0, ""), self.run_hook())


if __name__ == "__main__":
    unittest.main()
