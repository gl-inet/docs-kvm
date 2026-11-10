"""Offline content checks; no network calls or installed codespell required."""
import contextlib
import io
import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch, Mock
import urllib.error

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import pr_check as pc

PAGE = "docs/en/docs/page.md"


class DiffTests(unittest.TestCase):
    def test_committed_unicode_rename_and_special_paths(self):
        with tempfile.TemporaryDirectory() as temp, patch.object(pc, "REPO_ROOT", Path(temp)):
            root = Path(temp)
            def git(*args):
                return subprocess.run(["git", *args], cwd=root, check=True,
                                      stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            git("init")
            git("config", "user.name", "Test")
            git("config", "user.email", "test@example.invalid")
            old = "docs/en/docs/old.md"
            # Tabs/quotes/Unicode are legal filenames on both CI and Windows.
            new = "docs/en/docs/中文 page.md"
            (root / old).parent.mkdir(parents=True)
            (root / old).write_text("# Old {#old}\n" + "unchanged\n" * 20, encoding="utf-8")
            git("add", ".")
            git("commit", "-m", "base")
            git("branch", "base")
            (root / old).rename(root / new)
            (root / new).write_text("# New {#new}\n" + "unchanged\n" * 20 + "added\n", encoding="utf-8")
            added = "docs/en/docs/日本語 space.md"
            (root / added).write_text("new prose\n", encoding="utf-8")
            git("add", ".")
            git("commit", "-m", "change")
            (root / new).write_text("uncommitted content", encoding="utf-8")
            self.assertIn((old, new), pc.changed_paths("base"))
            self.assertEqual(pc.added_lines("base"), {new: {1, 22}, added: {1}})
            self.assertEqual(pc.page_lines(new)[0], "# New {#new}")
            findings = pc.check_heading_ids("base")
            self.assertEqual([(f.path, f.check) for f in findings], [(new, "heading-id")])

    def test_rename_and_recreated_old_path_do_not_mix_hunks(self):
        with tempfile.TemporaryDirectory() as temp, patch.object(pc, "REPO_ROOT", Path(temp)):
            root = Path(temp)
            def git(*args):
                return subprocess.run(["git", *args], cwd=root, check=True,
                                      stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            git("init")
            git("config", "user.name", "Test")
            git("config", "user.email", "test@example.invalid")
            old, new = "docs/en/docs/old.md", "docs/en/docs/new.md"
            (root / old).parent.mkdir(parents=True)
            text = "# Page {#page}\n" + "unchanged\n" * 30
            (root / old).write_text(text, encoding="utf-8")
            git("add", ".")
            git("commit", "-m", "base")
            git("branch", "base")
            (root / old).rename(root / new)
            (root / new).write_text(text + "added\n", encoding="utf-8")
            (root / old).write_text("different\n" * 4, encoding="utf-8")
            git("add", ".")
            git("commit", "-m", "rename plus replacement")
            # Rename detection can vary when the source path still exists;
            # isolate the reported rename mapping and exercise real blob diffs.
            with patch.object(pc, "changed_paths", return_value=[(old, new), (old, old)]):
                self.assertEqual(pc.added_lines("base")[new], {32})

    def test_nul_records_preserve_tabs_quotes_newlines(self):
        name = 'docs/en/docs/中文\t"quote"\npage.md'
        with patch.object(pc, "git", return_value=f"R100\0old.md\0{name}\0M\0other.md\0") as git:
            self.assertEqual(pc.changed_paths("base"), [("old.md", name), ("other.md", "other.md")])
            self.assertIn("-z", git.call_args.args)


class ContentTests(unittest.TestCase):
    def test_fences_metadata_and_tables(self):
        lines = ["---", "title: teh", "---", "prose", "    ````python", "teh",
                 "    ```", "still code", "    ```` trailing", "still code", "    ````",
                 "~~~", "![bad](https://example.invalid/a)", "~~~", "|---|---|", "last"]
        self.assertEqual(list(pc.prose_lines(lines)), [(4, "prose"), (16, "last")])

    def test_spelling_only_added_english_prose(self):
        lines = ["old teh", "```", "teh", "```", "new teh"]
        output = Mock(returncode=65, stdout="5: teh ==> the\n", stderr="")
        with patch.object(pc, "page_lines", return_value=lines), patch.object(pc.subprocess, "run", return_value=output) as run:
            findings = pc.check_spelling({PAGE: {3, 5}, "docs/de/docs/page.md": {1}})
            self.assertEqual([(f.level, f.line) for f in findings], [("error", 5)])
            self.assertEqual(run.call_count, 1)
            self.assertEqual(run.call_args.kwargs["input"], "\n\n\n\nnew teh")

    @unittest.skipUnless(importlib.util.find_spec("codespell_lib"), "optional codespell dependency not installed")
    def test_real_codespell_stdin_format_and_line_numbers(self):
        lines = ["old teh", "~~~", "teh", "~~~", "new teh"]
        with patch.object(pc, "page_lines", return_value=lines):
            findings = pc.check_spelling({PAGE: {3, 5}})
        self.assertEqual([(f.level, f.line) for f in findings], [("error", 5)])
        self.assertIn('"teh"', findings[0].message)

    @unittest.skipUnless(importlib.util.find_spec("codespell_lib"), "optional codespell dependency not installed")
    def test_spelling_ignores_inline_code_and_attributes_not_prose(self):
        lines = ['Use `teh` and ``teh `literal` teh`` {#teh} <span title="teh">text</span>.',
                 "This is teh typo."]
        with patch.object(pc, "page_lines", return_value=lines):
            findings = pc.check_spelling({PAGE: {1, 2}})
        self.assertEqual([(f.level, f.line) for f in findings], [("error", 2)])

    def test_codespell_failure_is_error(self):
        with patch.object(pc, "page_lines", return_value=["text"]), patch.object(pc.subprocess, "run", side_effect=OSError("missing")):
            self.assertEqual(pc.check_spelling({PAGE: {1}})[0].level, "error")

    def test_images_missing_vs_unavailable_and_deduplication(self):
        lines = ["![a](https://example.invalid/a)", "![b](https://example.invalid/b)",
                 "![a](https://example.invalid/a)", "![c](https://example.invalid/c)",
                 "```", "![ignored](https://example.invalid/d)", "```"]
        statuses = {"a": 404, "b": 410, "c": 503}
        with patch.object(pc, "page_lines", return_value=lines), patch.object(pc, "url_status", side_effect=lambda url: statuses[url[-1]]) as status:
            findings = pc.check_images({"docs/de/docs/p.md": set(range(1, 8))})
            self.assertEqual([f.level for f in findings], ["error", "error", "error", "warning"])
            self.assertEqual(status.call_count, 3)

    def test_head_falls_back_to_get(self):
        response = Mock(status=200)
        response.__enter__ = Mock(return_value=response)
        response.__exit__ = Mock(return_value=False)
        with patch.object(pc.urllib.request, "urlopen", side_effect=[
                urllib.error.HTTPError("https://example.invalid", 405, "", {}, None), response]) as request:
            self.assertEqual(pc.url_status("https://example.invalid"), 200)
            self.assertEqual([c.args[0].method for c in request.call_args_list], ["HEAD", "GET"])

    def test_head_404_is_confirmed_by_get_before_error(self):
        response = Mock(status=200)
        response.__enter__ = Mock(return_value=response)
        response.__exit__ = Mock(return_value=False)
        for status in (404, 410):
            with patch.object(pc.urllib.request, "urlopen", side_effect=[
                    urllib.error.HTTPError("https://example.invalid", status, "", {}, None), response]) as request:
                self.assertEqual(pc.url_status("https://example.invalid"), 200)
                self.assertEqual([c.args[0].method for c in request.call_args_list], ["HEAD", "GET"])

    def test_grammar_only_warning_with_original_line_numbers(self):
        match = {"offset": 0, "message": "Grammar", "replacements": [{"value": "fix"}], "rule": {"id": "TEST"}}
        with patch.object(pc, "page_lines", return_value=["```", "code", "```", "This are wrong."]), patch.object(pc, "languagetool", return_value=[match]) as tool:
            findings = pc.check_grammar({PAGE: {2, 4}}, "http://localhost")
            self.assertEqual((findings[0].line, findings[0].level), (4, "warning"))
            self.assertNotIn("code", tool.call_args.args[1])
        with patch.object(pc, "page_lines", return_value=["text"]), patch.object(pc, "languagetool", side_effect=TimeoutError()):
            self.assertEqual(pc.check_grammar({PAGE: {1}}, "http://localhost")[0].level, "warning")

    def test_alt_and_copied_links(self):
        lines = ["# One {#one}", "[Official Website](https://example.invalid)",
                 "# Two {#two}", "[Official Website](https://example.invalid)",
                 "![screen2](https://example.invalid/screen1.png)"]
        with patch.object(pc, "page_lines", return_value=lines):
            self.assertEqual(pc.check_alt_text({PAGE: {5}})[0].level, "warning")
            self.assertEqual(pc.check_copied_links({PAGE: {4}})[0].line, 4)

    def test_main_errors_fail_warnings_do_not(self):
        for level, expected in [("warning", 0), ("error", 1)]:
            with contextlib.ExitStack() as stack:
                stack.enter_context(patch.object(pc, "added_lines", return_value={}))
                for name in ("check_images", "check_heading_ids", "check_alt_text", "check_copied_links"):
                    stack.enter_context(patch.object(pc, name, return_value=[]))
                stack.enter_context(patch.object(pc, "check_spelling", return_value=[pc.Finding(level, "test", PAGE, 1, "message")]))
                stack.enter_context(contextlib.redirect_stdout(io.StringIO()))
                self.assertEqual(pc.main(["--base", "base"]), expected)


if __name__ == "__main__":
    unittest.main()
