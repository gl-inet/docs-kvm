"""Integration tests using real, isolated Git repositories (no docs checkout mutations)."""
import contextlib
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / "translation_delta.py"
spec = importlib.util.spec_from_file_location("translation_delta_under_test", SCRIPT)
delta = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = delta
spec.loader.exec_module(delta)


class TranslationDeltaTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.old = Path.cwd()
        os.chdir(self.temp.name)
        self.git("init", "-q")
        self.git("config", "user.email", "test@example.invalid")
        self.git("config", "user.name", "Test")
        self.git("config", "core.autocrlf", "false")
        self.source = "docs/en/docs/page.md"
        self.target = "docs/de/docs/page.md"
        self.put(self.source, b"# English {#page}\n\nOriginal.  \n\n\n")
        self.put(self.target, b"# Deutsch {#page}\n\nUrsprung.\n")
        self.commit()
        self.legacy_hash = delta.source_hash(Path(self.source))

    def tearDown(self):
        os.chdir(self.old)
        self.temp.cleanup()

    def git(self, *args):
        return subprocess.check_output(["git", *args], stderr=subprocess.STDOUT).decode().strip()

    def put(self, path, data):
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        Path(path).write_bytes(data)

    def commit(self):
        self.git("add", ".")
        self.git("commit", "-qm", "fixture")

    def cache(self, entry=None):
        data = {self.source: entry or {"source_hash": self.legacy_hash, "targets": {"de": {"model": "old", "updated_at": 42}}}}
        delta.write_json(Path(delta.CACHE_FILE), data)
        return data

    def read_cache(self):
        return delta.read_json(Path(delta.CACHE_FILE))

    def run_cmd(self, function, argv):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = function(argv)
        return code, out.getvalue()

    def test_text_binary_and_full_scan(self):
        for ext in delta.DEFAULT_TEXT_EXTENSIONS:
            lf = Path("docs/en/asset" + ext)
            self.put(lf, b"x\n\n")
            expected = delta.source_hash(lf)
            self.put(lf, b"\xef\xbb\xbfx\r\n\r\n")
            self.assertEqual(expected, delta.source_hash(lf))
        self.put("docs/en/image.png", b"\xff\x00\r\n")
        self.put("docs/en/docs/downloads/index.md", b"Downloads\n")
        self.assertIn(Path("docs/en/image.png"), list(delta.iter_source_files(Path("docs/en"))))
        self.assertIn(Path("docs/en/docs/downloads/index.md"), list(delta.iter_source_files(Path("docs/en"))))
        self.assertNotEqual(delta.hash_bytes(Path("a.png"), b"\r\n"), delta.hash_bytes(Path("a.png"), b"\n"))
        self.assertNotIn("uk", delta.DEFAULT_LANGS)
        self.assertEqual(8, len(delta.DEFAULT_LANGS))

    def test_missing_languages_remain_missing_and_migration_idempotent(self):
        self.cache()
        self.assertEqual({}, delta.target_record(self.read_cache(), self.source, "ja"))
        self.run_cmd(delta.cmd_migrate, [])
        entry = self.read_cache()[self.source]
        self.assertEqual({"de"}, set(entry["targets"]))
        record = entry["targets"]["de"]
        self.assertEqual("old", record["model"])
        self.assertEqual(42, record["updated_at"])
        self.assertEqual(self.legacy_hash, record["source_hash"])
        self.assertEqual(self.git("rev-parse", "HEAD:" + self.source), record["source_blob"])
        self.assertIn("target_hash", record)
        before = Path(delta.CACHE_FILE).read_bytes()
        self.run_cmd(delta.cmd_migrate, [])
        self.assertEqual(before, Path(delta.CACHE_FILE).read_bytes())

    def test_history_exact_whitespace_mismatch_and_existing_record(self):
        independent = {"source_hash": "independent", "source_blob": "keep", "target_hash": "keep-target", "updated_at": 7}
        self.cache({"source_hash": self.legacy_hash, "targets": {"de": {"model": "old", "updated_at": 42}, "ja": independent}})
        blob = self.git("rev-parse", "HEAD:" + self.source)
        self.put(self.source, b"# English {#page}\n\nNew.\n")
        self.commit()
        self.run_cmd(delta.cmd_migrate, [])
        records = self.read_cache()[self.source]["targets"]
        self.assertEqual(blob, records["de"]["source_blob"])
        self.assertNotIn("target_hash", records["de"])
        self.assertEqual(independent, records["ja"])
        code, text = self.run_cmd(delta.cmd_diff, [self.source, "--lang", "de"])
        self.assertEqual(0, code)
        self.assertIn("-Original.  ", text)
        self.assertIn("+New.", text)
        self.assertNotEqual(blob, delta.find_source_blob(self.source, delta.hash_bytes(Path(self.source), b"# English {#page}\n\nOriginal.  \n")))

    def test_pending_pairs_unchanged_by_migration(self):
        self.cache()
        self.put("docs/ja/docs/page.md", b"Existing but unrecorded Japanese\n")
        self.put(self.source, b"New English\n")
        files = [Path(self.source)]
        before = delta.build_report({}, delta.analyze_sources(files, self.read_cache(), ["de", "ja"]), [])
        self.run_cmd(delta.cmd_migrate, [])
        after = delta.build_report({}, delta.analyze_sources(files, self.read_cache(), ["de", "ja"]), [])
        self.assertEqual(before, after)
        self.assertEqual([{"path": self.source, "langs": ["ja"]}], after["cache_missing"])
        self.assertEqual([{"path": self.source, "langs": ["de"]}], after["hash_mismatch"])

    def test_diff_noop_lf_crlf(self):
        self.cache()
        self.run_cmd(delta.cmd_migrate, [])
        raw = Path(self.source).read_bytes()
        self.put(self.source, raw.replace(b"\n", b"\r\n"))
        code, output = self.run_cmd(delta.cmd_diff, [self.source, "--lang", "de"])
        self.assertEqual(0, code)
        self.assertIn("has not changed", output)

    def test_deleted_legacy_and_unknown_blob(self):
        self.cache()
        blob = self.git("rev-parse", "HEAD:" + self.source)
        Path(self.source).unlink()
        self.commit()
        self.run_cmd(delta.cmd_migrate, [])
        self.assertEqual(blob, self.read_cache()[self.source]["targets"]["de"]["source_blob"])
        self.cache({"source_hash": "unknown", "targets": {"de": {"updated_at": 4}}})
        self.run_cmd(delta.cmd_migrate, [])
        record = self.read_cache()[self.source]["targets"]["de"]
        self.assertNotIn("source_blob", record)
        self.assertNotIn("target_hash", record)

    def test_changed_localized_file_not_seeded_as_baseline(self):
        self.cache()
        self.put(self.target, b"Edited but not reviewed\n")
        self.run_cmd(delta.cmd_migrate, [])
        self.assertNotIn("target_hash", self.read_cache()[self.source]["targets"]["de"])

    def test_mark_one_language_does_not_clear_other_delta(self):
        self.cache({"source_hash": self.legacy_hash, "targets": {"de": {"model": "old"}, "ja": {"model": "old-ja"}}})
        self.put("docs/ja/docs/page.md", b"Japanese\n")
        self.put(self.source, b"# English {#page}\n\nChanged.\n")
        self.put(self.target, b"# Deutsch {#page}\n\nGeaendert.\n")
        with patch.object(delta, "check_target", return_value=[]):
            code, text = self.run_cmd(delta.cmd_mark, [self.source, "--lang", "de"])
        self.assertEqual(0, code)
        cache = self.read_cache()
        self.assertEqual(self.legacy_hash, cache[self.source]["targets"]["ja"]["source_hash"])
        self.assertNotIn("source_blob", cache[self.source]["targets"]["de"])
        self.assertIn("uncommitted", text)
        status = delta.analyze_sources([Path(self.source)], cache, ["de", "ja"])[0]
        self.assertEqual(["ja"], status.hash_mismatch)

    def test_failed_mark_and_noop_never_advance_cache(self):
        self.cache()
        with patch.object(delta, "check_target", return_value=[]):
            self.run_cmd(delta.cmd_mark, [self.source, "--lang", "de"])
            before = Path(delta.CACHE_FILE).read_bytes()
            self.run_cmd(delta.cmd_mark, [self.source, "--lang", "de"])
            self.assertEqual(before, Path(delta.CACHE_FILE).read_bytes())
            self.put(self.source, b"Changed English\n")
            code, _ = self.run_cmd(delta.cmd_mark, [self.source, "--lang", "de"])
            self.assertEqual(1, code)
            self.assertEqual(before, Path(delta.CACHE_FILE).read_bytes())
            code, _ = self.run_cmd(delta.cmd_mark, [self.source, "--lang", "de", "--no-target-change"])
            self.assertEqual(0, code)
        before = Path(delta.CACHE_FILE).read_bytes()
        with patch.object(delta, "check_target", return_value=["invalid structure"]):
            code, _ = self.run_cmd(delta.cmd_mark, [self.source, "--lang", "de"])
        self.assertEqual(1, code)
        self.assertEqual(before, Path(delta.CACHE_FILE).read_bytes())

    def test_legal_preservation_and_prune(self):
        approved = b"# Deutsch {#page}\n\nText\n\n## Sicherheit {#safety-information}\nApproved wording.\n"
        self.put(self.target, approved)
        self.commit()
        self.assertEqual([], delta.legal_errors(Path(self.target), approved.decode()))
        self.assertTrue(delta.legal_errors(Path(self.target), approved.decode().replace("Approved", "Changed")))
        self.assertTrue(delta.legal_errors(Path(self.target), ""))
        self.cache()
        Path(self.source).unlink()
        before = Path(delta.CACHE_FILE).read_bytes()
        self.assertEqual(1, self.run_cmd(delta.cmd_prune, [])[0])
        Path(self.target).unlink()
        self.assertEqual(1, self.run_cmd(delta.cmd_prune, [])[0])
        self.assertEqual(before, Path(delta.CACHE_FILE).read_bytes())

    def test_prune_safe_deletion_and_regulatory_excluded(self):
        self.cache()
        Path(self.source).unlink()
        self.assertEqual(1, self.run_cmd(delta.cmd_prune, [])[0])
        Path(self.target).unlink()
        self.assertEqual(0, self.run_cmd(delta.cmd_prune, [])[0])
        self.assertEqual({}, self.read_cache())
        regulatory = Path("docs/en/docs/regulatory_statement.md")
        self.put(regulatory, b"Legal\n")
        statuses = delta.analyze_sources([regulatory], {}, list(delta.DEFAULT_LANGS))
        report = delta.build_report({}, statuses, [])
        for key in ("cache_missing", "hash_mismatch", "target_missing"):
            self.assertEqual([], report[key])
        with self.assertRaises(ValueError):
            delta.source_arg(str(regulatory))

    def test_crlf_committed_blob_and_binary_migration(self):
        self.put(self.source, b"# English {#page}\r\n\r\nChanged.  \r\n\r\n")
        self.commit()
        expected = delta.source_hash(Path(self.source))
        self.assertEqual(self.git("rev-parse", "HEAD:" + self.source), delta.find_source_blob(self.source, expected))
        binary = "docs/en/picture.png"
        self.put(binary, b"\x89\xff\x00\r\n")
        self.put("docs/de/picture.png", b"\x89\xff\x00\r\n")
        self.commit()
        cache = {binary: {"source_hash": delta.source_hash(Path(binary)), "targets": {"de": {"model": "binary"}}}}
        delta.write_json(Path(delta.CACHE_FILE), cache)
        self.run_cmd(delta.cmd_migrate, [])
        record = self.read_cache()[binary]["targets"]["de"]
        self.assertEqual(self.git("rev-parse", "HEAD:" + binary), record["source_blob"])
        self.assertIn("target_hash", record)

    def test_snapshot_portable_in_fresh_clone_not_sibling_branch(self):
        original_blob = self.git("rev-parse", "HEAD:" + self.source)
        original_hash = self.legacy_hash
        branch = self.git("branch", "--show-current")
        self.git("checkout", "-qb", "unrelated")
        self.put(self.source, b"Only on sibling branch.  \n\n")
        self.commit()
        sibling_hash = delta.source_hash(Path(self.source))
        self.git("checkout", "-q", branch)
        self.assertIsNone(delta.find_source_blob(self.source, sibling_hash))
        self.assertEqual(original_blob, delta.find_source_blob(self.source, original_hash))
        source_repo = Path.cwd()
        with tempfile.TemporaryDirectory() as destination:
            subprocess.check_call(["git", "clone", "--quiet", "--no-local", "--single-branch", "--branch", branch, str(source_repo), destination])
            try:
                os.chdir(destination)
                self.assertEqual(original_blob, delta.find_source_blob(self.source, original_hash))
                self.assertIsNone(delta.find_source_blob(self.source, sibling_hash))
                self.assertEqual(0, delta.run_git(["cat-file", "-e", original_blob + "^{blob}"])[0])
            finally:
                os.chdir(source_repo)

    def test_check_target_uses_kvm_signature_and_own_legal_guard(self):
        import types
        checker = types.SimpleNamespace(check_page=lambda lang, rel: [], check_language_files=lambda lang: [])
        with patch.dict(sys.modules, {"i18n_check": checker}):
            self.assertEqual([], delta.check_target(self.source, "de", {}))
            self.put(self.target, b"# Deutsch {#page}\n## Safety {#safety-information}\nNew legal text\n")
            self.assertTrue(delta.check_target(self.source, "de", {}))


if __name__ == "__main__":
    unittest.main()
