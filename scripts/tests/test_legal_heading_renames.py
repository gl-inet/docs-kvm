"""Both trusted legal checks allow title-ID sync, but reject actual legal changes."""
from pathlib import Path
import sys
import types
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import translation_guard as guard
import test_translation_delta as fixtures

delta = fixtures.delta


class LegalHeadingRenameTests(unittest.TestCase):
    # Reuse isolated Git fixtures without inheriting their unrelated test cases.
    setUp = fixtures.TranslationDeltaTests.setUp
    tearDown = fixtures.TranslationDeltaTests.tearDown
    git = fixtures.TranslationDeltaTests.git
    put = fixtures.TranslationDeltaTests.put
    commit = fixtures.TranslationDeltaTests.commit
    cache = fixtures.TranslationDeltaTests.cache
    read_cache = fixtures.TranslationDeltaTests.read_cache
    run_cmd = fixtures.TranslationDeltaTests.run_cmd

    def baseline(self, ident):
        legal = f"## Legal {{#{ident}}}\nApproved wording.\n\n"
        before = "# Old title {#old-title}\n\n" + legal + "## Setup {#setup}\nInstructions.\n"
        self.put(self.target, before.encode())
        self.commit()
        return before, legal

    def check_both(self, after, accepted):
        self.put(self.target, after.encode())
        self.git("add", self.target)
        errors = delta.legal_errors(Path(self.target), after)
        if accepted:
            self.assertEqual(errors, [])
            self.assertEqual(guard.check_patch(), [self.target])
        else:
            self.assertIn("Approved legal wording or placement changed since HEAD", errors)
            with self.assertRaisesRegex(ValueError, "approved legal"):
                guard.check_patch()

    def test_one_or_all_neighbor_ids_can_be_renamed(self):
        for ident in sorted(guard.PROTECTED_IDS):
            before, _ = self.baseline(ident)
            renamed = before.replace("Old title {#old-title}", "New title {#new-title}")
            for after in (renamed, before.replace("Setup {#setup}", "Installation {#installation}"),
                          renamed.replace("Setup {#setup}", "Installation {#installation}")):
                with self.subTest(ident=ident, after=after):
                    self.check_both(after, True)

    def test_legal_wording_heading_and_deletion_stay_protected(self):
        for ident in sorted(guard.PROTECTED_IDS):
            before, legal = self.baseline(ident)
            for after in (before.replace("Approved", "Altered"),
                          before.replace("## Legal", "## Changed legal"),
                          before.replace("## Legal", "### Legal"),
                          before.replace(legal, "")):
                with self.subTest(ident=ident, after=after):
                    self.check_both(after, False)

    def test_cross_heading_moves_and_neighbor_renames_are_rejected(self):
        for ident in sorted(guard.PROTECTED_IDS):
            before, legal = self.baseline(ident)
            after = before.replace(legal, "") + "\n" + legal
            for moved in (after, after.replace("old-title", "new-title")):
                with self.subTest(ident=ident, after=moved):
                    self.check_both(moved, False)

    def test_neighbor_swap_with_same_ordinal_is_rejected(self):
        for ident in sorted(guard.PROTECTED_IDS):
            before, _ = self.baseline(ident)
            after = before.replace("old-title", "temporary").replace("setup", "old-title").replace("temporary", "setup")
            with self.subTest(ident=ident):
                self.check_both(after, False)

    def test_new_heading_before_legal_section_is_conservatively_rejected(self):
        before, legal = self.baseline("safety-information")
        self.check_both(before.replace(legal, "## Extra {#extra}\nNew.\n\n" + legal), False)

    def test_mark_accepts_neighbor_id_sync_without_changing_legal_text(self):
        before, _ = self.baseline("safety-information")
        self.cache()
        self.put(self.source, b"# New title {#new-title}\n\nUpdated English.\n")
        self.put(self.target, before.replace("Old title {#old-title}", "New title {#new-title}").encode())
        # Isolate structural/text diagnostics, but run the real check_target and
        # HEAD-based legal check so this covers mark's previously blocked path.
        checker = types.SimpleNamespace(check_page=lambda lang, rel: [])
        with patch.dict(sys.modules, {"i18n_check": checker}):
            code, output = self.run_cmd(delta.cmd_mark, [self.source, "--lang", "de"])
        self.assertEqual(code, 0, output)
        record = self.read_cache()[self.source]["targets"]["de"]
        self.assertEqual(record["source_hash"], delta.source_hash(Path(self.source)))
        self.assertEqual(record["target_hash"], delta.target_hash(Path(self.target)))

    def test_mark_rejects_actual_move_and_preserves_cache_bytes(self):
        before, legal = self.baseline("declaration-of-conformity")
        self.cache()
        cache_before = Path(delta.CACHE_FILE).read_bytes()
        self.put(self.source, b"# New title {#new-title}\n\nUpdated English.\n")
        self.put(self.target, (before.replace(legal, "") + "\n" + legal).encode())
        checker = types.SimpleNamespace(check_page=lambda lang, rel: [])
        with patch.dict(sys.modules, {"i18n_check": checker}):
            code, output = self.run_cmd(delta.cmd_mark, [self.source, "--lang", "de"])
        self.assertEqual(code, 1, output)
        self.assertIn("Approved legal wording or placement changed", output)
        self.assertEqual(Path(delta.CACHE_FILE).read_bytes(), cache_before)


if __name__ == "__main__":
    unittest.main()
