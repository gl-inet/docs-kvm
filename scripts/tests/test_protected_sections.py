"""Offline tests of the HEAD/index legal-text protection API."""
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import i18n_check as checker


class ProtectedSectionsTests(unittest.TestCase):
    rel = "user_guide/gl-rm1/index.md"
    before = (
        "# Gerät {#device}\n\nIntroduction.\n\n"
        "## Sicherheit {#safety-information}\nApproved.\n\n"
        "### Details {#details}\nSubsection text.\n\n"
        "## Setup {#setup}\nInstructions.\n"
    )
    standalone = (
        "---\ntitle: Sicherheit\n---\n\n"
        "# Sicherheit {#safety-information}\nApproved.\n\n"
        "## Details {#details}\nSubsection text.\n"
    )

    def check(self, before, after, rel=None, lang="de"):
        # No source-page lookup, file reads or allowlist should be necessary.
        with patch.object(Path, "read_bytes", side_effect=AssertionError("file read")), \
             patch.object(checker, "load_allowlist", side_effect=AssertionError("allowlist")):
            return checker.check_protected_text(lang, rel or self.rel, before, after)

    def assert_protected(self, before, after, rel=None):
        issues = self.check(before, after, rel)
        self.assertTrue(issues)
        self.assertTrue(all(issue.check == "protected-section" for issue in issues))
        self.assertEqual(issues[0].lang, "de")
        self.assertEqual(issues[0].page, rel or self.rel)
        self.assertEqual(issues[0].section, "safety-information")
        self.assertIsNotNone(issues[0].line)
        return issues

    def test_unchanged(self):
        self.assertEqual(self.check(self.before, self.before), [])
        self.assertEqual(self.check(self.standalone, self.standalone), [])

    def test_modified_section(self):
        issues = self.assert_protected(self.before, self.before.replace("Approved.", "Changed."))
        self.assertEqual(issues[0].line, 5)

    def test_deleted_section_and_page(self):
        self.assert_protected(self.before, "# Gerät {#device}\n## Setup {#setup}\n")
        self.assert_protected(self.before, None)

    def test_removed_or_renamed_id(self):
        for replacement in ("", "{#renamed}"):
            with self.subTest(replacement=replacement):
                self.assert_protected(self.before, self.before.replace("{#safety-information}", replacement))

    def test_subsection_text_and_heading_are_protected(self):
        for old, new in (("Subsection text.", "Changed."),
                         ("### Details", "#### Details"),
                         ("{#details}", "{#other}")):
            with self.subTest(old=old):
                self.assert_protected(self.before, self.before.replace(old, new))

    def test_normalization(self):
        embedded = self.before.replace("### Details", "#### Details")
        for before in (embedded, self.standalone):
            after = before.replace("## Sicherheit", "### Sicherheit") if before == embedded else before.replace("# Sicherheit", "### Sicherheit")
            after = "\r\n".join(line + "  " for line in after.splitlines()) + "\r\n"
            self.assertEqual(self.check(before, after), [])

    def test_standalone_edit_delete_and_id_changes(self):
        rel = "user_guide/gl-rm1/safety_information.md"
        for after in (None, "", self.standalone.replace("Approved.", "Changed."),
                      self.standalone.replace("{#safety-information}", ""),
                      self.standalone.replace("{#safety-information}", "{#renamed}"),
                      self.standalone.replace("title: Sicherheit", "title: Changed"),
                      self.standalone + "\n## Extra {#extra}\nNew text.\n"):
            with self.subTest(after=after):
                self.assert_protected(self.standalone, after, rel)

    def test_fenced_fake_headings(self):
        for fence in ("```", "~~~~"):
            with self.subTest(fence=fence):
                text = "# Page {#page}\n" + fence + "markdown\n## Fake {#safety-information}\nExample.\n" + fence + "\n"
                self.assertEqual(self.check(text, text.replace("Example.", "Changed.")), [])
                # Fake sibling headings must not terminate the protected section.
                text = self.before.replace("Approved.", "Approved.\n" + fence + "\n## Fake {#fake}\n" + fence)
                self.assert_protected(text, text.replace("Subsection text.", "Changed."))

    def test_nonlegal_edits_and_new_legal_text(self):
        self.assertEqual(self.check(self.before, self.before.replace("Instructions.", "Updated.")), [])
        self.assertEqual(self.check(None, self.standalone), [])
        self.assertEqual(self.check(None, None), [])
        self.assertEqual(self.check("# Page {#page}\n", self.before), [])
        self.assertEqual(self.check(self.before, None, lang="en"), [])
        self.assertEqual(self.check("# Page {#page}\n", None), [])

    def test_declaration_of_conformity(self):
        before = self.before.replace("safety-information", "declaration-of-conformity")
        issues = self.check(before, before.replace("Approved.", "Changed."))
        self.assertEqual(issues[0].section, "declaration-of-conformity")


if __name__ == "__main__":
    unittest.main()
