"""Index-only translation cache checks in real, disposable Git repositories."""
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
import precommit
import translation_delta as delta


class PrecommitCacheTests(unittest.TestCase):
    source = "docs/en/docs/page.md"
    target = "docs/de/docs/page.md"
    cache_path = ".translation-cache.json"
    english = b"# English {#page}\n\nOriginal.\n"
    german = b"# Deutsch {#page}\n\nOriginal.\n"
    translated = b"# Deutsch {#page}\n\nGeaendert.\n"

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        old = Path.cwd()
        self.root = Path(self.temp.name).resolve()
        os.chdir(self.root)
        self.addCleanup(os.chdir, old)
        self.git("init", "-q")
        self.git("config", "core.autocrlf", "false")
        self.git("config", "core.hooksPath", ".disabled-hooks")
        self.put(self.source, self.english)
        self.put(self.target, self.german)
        self.cache = self.record(self.source, self.target, self.english, self.german)
        self.save_cache(self.cache)
        self.git("add", ".")
        # Create a fixture HEAD without running git commit or any hooks.
        tree = self.git("write-tree").strip()
        commit = (f"tree {tree}\nauthor Test <test@example.invalid> 0 +0000\n"
                  "committer Test <test@example.invalid> 0 +0000\n\nfixture\n")
        oid = subprocess.check_output(
            ["git", "hash-object", "-t", "commit", "-w", "--stdin"],
            input=commit.encode("ascii"),
        ).decode("ascii").strip()
        self.git("update-ref", "HEAD", oid)
        for name, value in (("REPO_ROOT", self.root), ("DOCS_ROOT", self.root / "docs")):
            patcher = patch.object(anchors, name, value)
            patcher.start()
            self.addCleanup(patcher.stop)

    def git(self, *args):
        return subprocess.check_output(
            ["git", *args], stderr=subprocess.STDOUT,
        ).decode("utf-8")

    def put(self, path, data):
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data if isinstance(data, bytes) else data.encode("utf-8"))

    def save_cache(self, cache, stage=True):
        self.put(self.cache_path, json.dumps(cache, ensure_ascii=False))
        if stage:
            self.git("add", "--", self.cache_path)

    def record(self, source, target, english, translated):
        lang = target.split("/")[1]
        return {source: {"targets": {lang: {
            "source_hash": delta.hash_bytes(Path(source), english),
            "target_hash": delta.hash_bytes(Path(target), translated),
        }}}}

    def errors(self):
        errors = precommit.cache_errors(precommit.staged_files(precommit.staged_changes()))
        self.assertIsInstance(errors, list)
        self.assertTrue(all(isinstance(error, str) for error in errors))
        return errors

    def stage_translation(self):
        self.put(self.target, self.translated)
        self.git("add", "--", self.target)

    def test_added_and_modified_assets_need_matching_records(self):
        assets = (
            "docs/page.md", "mkdocs.yml", "overrides/main.html",
            "docs/stylesheets/custom.css", "docs/images/icon.svg",
            "docs/data/readme.txt", "docs/data/config.json", "docs/images/image.png",
        )
        for rest in assets:
            for added in (True, False):
                with self.subTest(rest=rest, added=added):
                    self.git("reset", "--hard", "HEAD")
                    self.git("clean", "-fdq")
                    source, target = "docs/en/" + rest, "docs/fr/" + rest
                    binary = rest.endswith(".png")
                    english = b"\x89PNG\r\n\x1a\n\x00\xff" if binary else b"English\n"
                    before = b"\x89PNG\x00\xfe" if binary else b"Ancien\n"
                    after = before + (b"\x00\xfd" if binary else b"Nouveau\n")
                    self.put(source, english)
                    self.git("add", "--", source)
                    if not added:
                        # Reuse the fixture HEAD creation approach for an M status.
                        self.put(target, before)
                        self.git("add", "--", target)
                        tree = self.git("write-tree").strip()
                        raw = (f"tree {tree}\nauthor Test <test@example.invalid> 0 +0000\n"
                               "committer Test <test@example.invalid> 0 +0000\n\nasset baseline\n")
                        oid = subprocess.check_output(
                            ["git", "hash-object", "-t", "commit", "-w", "--stdin"],
                            input=raw.encode("ascii"),
                        ).decode("ascii").strip()
                        self.git("update-ref", "HEAD", oid)
                    self.put(target, after)
                    self.git("add", "--", target)
                    self.save_cache({})
                    self.assertTrue(self.errors(), "missing cache record must block")
                    self.save_cache(self.record(source, target, english, after))
                    self.assertEqual([], self.errors())

    def test_missing_and_invalid_per_language_hashes_block(self):
        self.stage_translation()
        valid = self.record(self.source, self.target, self.english, self.translated)
        variants = [{}, {self.source: {}}, {self.source: {"targets": {}}}]
        for field in ("source_hash", "target_hash"):
            for value in (None, "", "wrong"):
                cache = json.loads(json.dumps(valid))
                record = cache[self.source]["targets"]["de"]
                if value is None:
                    record.pop(field)
                else:
                    record[field] = value
                variants.append(cache)
        for cache in variants:
            with self.subTest(cache=cache):
                self.save_cache(cache)
                self.assertTrue(self.errors())

    def test_legacy_shared_source_hash_is_not_a_per_language_baseline(self):
        self.stage_translation()
        cache = self.record(self.source, self.target, self.english, self.translated)
        entry = cache[self.source]
        entry["source_hash"] = entry["targets"]["de"].pop("source_hash")
        self.save_cache(cache)
        self.assertTrue(self.errors())

    def test_unstaged_cache_fix_cannot_hide_stale_index_cache(self):
        self.stage_translation()
        self.save_cache(self.record(self.source, self.target, self.english, self.translated), stage=False)
        self.assertTrue(self.errors())

    def test_index_cache_not_unstaged_cache_is_authoritative(self):
        self.stage_translation()
        self.save_cache(self.record(self.source, self.target, self.english, self.translated))
        self.put(self.cache_path, "invalid working-tree JSON")
        self.assertEqual([], self.errors())

    def test_partial_target_staging_uses_index_hash(self):
        self.stage_translation()
        self.put(self.target, self.translated + b"Unstaged text.\n")
        self.save_cache(self.record(self.source, self.target, self.english, self.translated))
        self.assertEqual([], self.errors())
        self.save_cache(self.record(self.source, self.target, self.english, Path(self.target).read_bytes()))
        self.assertTrue(self.errors())

    def test_unstaged_english_hash_cannot_substitute_for_index_hash(self):
        self.stage_translation()
        working = self.english + b"Unstaged English.\n"
        self.put(self.source, working)
        self.save_cache(self.record(self.source, self.target, working, self.translated))
        self.assertTrue(self.errors())
        self.save_cache(self.record(self.source, self.target, self.english, self.translated))
        self.assertEqual([], self.errors())

    def test_new_staged_english_requires_its_own_hash(self):
        self.stage_translation()
        changed = self.english + b"Staged English.\n"
        self.put(self.source, changed)
        self.git("add", "--", self.source)
        self.save_cache(self.record(self.source, self.target, self.english, self.translated))
        self.assertTrue(self.errors())
        self.save_cache(self.record(self.source, self.target, changed, self.translated))
        self.assertEqual([], self.errors())

    def test_text_bom_crlf_and_cr_are_normalized(self):
        self.put(self.source, b"\xef\xbb\xbf" + self.english.replace(b"\n", b"\r\n"))
        self.put(self.target, b"\xef\xbb\xbf" + self.translated.replace(b"\n", b"\r"))
        self.git("add", "--", self.source, self.target)
        self.save_cache(self.record(self.source, self.target, self.english, self.translated))
        self.assertEqual([], self.errors())

    def test_binary_hashes_do_not_normalize_line_endings_or_bom(self):
        source, target = "docs/en/docs/image.png", "docs/de/docs/image.png"
        raw = b"\xef\xbb\xbfPNG\r\n\x00\xff"
        self.put(source, raw)
        self.put(target, raw)
        self.git("add", "--", source, target)
        self.save_cache(self.record(source, target, raw, raw))
        self.assertEqual([], self.errors())
        for field in ("source_hash", "target_hash"):
            cache = self.record(source, target, raw, raw)
            cache[source]["targets"]["de"][field] = delta.hash_bytes(Path(source), b"PNG\n\x00\xff")
            self.save_cache(cache)
            self.assertTrue(self.errors())

    def test_english_only_changes_allow_translation_backlog(self):
        self.put(self.source, self.english + b"New English.\n")
        self.git("add", "--", self.source)
        self.assertEqual([], self.errors())

    def test_no_relevant_changes_ignore_invalid_unstaged_cache(self):
        self.put(self.cache_path, "not JSON")
        self.put("README.txt", "unrelated")
        self.git("add", "--", "README.txt")
        self.assertEqual([], self.errors())

    def test_staged_cache_must_be_a_json_object_even_without_targets(self):
        for data in ("{invalid", "[]", "null", '"string"', "42"):
            with self.subTest(data=data):
                self.put(self.cache_path, data)
                self.git("add", "--", self.cache_path)
                self.assertTrue(self.errors())

    def test_cache_only_does_not_validate_other_languages_or_whole_repo(self):
        self.cache[self.source]["targets"]["fr"] = {"source_hash": "stale"}
        self.cache[self.source]["targets"]["de"]["target_hash"] = "stale"
        self.save_cache(self.cache)
        self.assertEqual([], self.errors())

    def test_changed_language_does_not_require_other_languages_to_match(self):
        self.stage_translation()
        cache = self.record(self.source, self.target, self.english, self.translated)
        cache[self.source]["targets"]["fr"] = {"source_hash": "stale"}
        self.save_cache(cache)
        self.assertEqual([], self.errors())

    def test_independent_legal_and_missing_source_are_skipped(self):
        for rest in ("docs/safety_information.md", "docs/local-only.md"):
            self.put("docs/de/" + rest, "Localized only\n")
            self.git("add", "--", "docs/de/" + rest)
        # A working-tree source must not count as an index counterpart.
        self.put("docs/en/docs/local-only.md", "Unstaged source\n")
        self.assertEqual([], self.errors())

    def test_english_only_regulatory_filenames_are_skipped(self):
        for name in ("regulatory_statement.md", "fcc_ic_compliance_statements.md"):
            for lang in ("en", "de"):
                path = f"docs/{lang}/docs/{name}"
                self.put(path, "Regulatory\n")
                self.git("add", "--", path)
        self.assertEqual([], self.errors())

    def test_deleted_target_is_skipped(self):
        self.git("rm", "--", self.target)
        self.save_cache({})
        self.assertEqual([], self.errors())


if __name__ == "__main__":
    unittest.main()
