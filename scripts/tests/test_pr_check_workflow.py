"""Regression tests for read-only PR checks and strict language selection."""
from pathlib import Path
import os
import unittest
from unittest.mock import patch

import yaml

ROOT = Path(__file__).resolve().parents[2]


class WorkflowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = (ROOT / ".github/workflows/pr-check.yml").read_text(encoding="utf-8")
        # BaseLoader keeps the YAML 1.2 `on` key as a string.
        cls.workflow = yaml.load(cls.text, Loader=yaml.BaseLoader)

    def test_read_only_every_job(self):
        self.assertEqual(self.workflow["permissions"], {"contents": "read"})
        self.assertEqual(set(self.workflow["jobs"]), {"structure", "build", "content"})
        for job in self.workflow["jobs"].values():
            self.assertEqual(job["permissions"], {"contents": "read"})
            checkout = next(s for s in job["steps"] if s.get("uses", "").startswith("actions/checkout@"))
            self.assertEqual(checkout["with"]["persist-credentials"], "false")
            self.assertEqual(checkout["with"]["fetch-depth"], "0")
        for forbidden in ("secrets.", "github.token", "GITHUB_TOKEN", "suggest_ids.py", "pull_request_target", ": write"):
            self.assertNotIn(forbidden, self.text)

    def test_paths_and_versions(self):
        trigger = self.workflow["on"]["pull_request"]
        self.assertEqual(trigger["branches"], ["master"])
        for path in ("docs/**", "scripts/**", ".translation-cache.json", "requirements*.txt",
                     ".githooks/**", "**/AGENTS.md", ".agents/**", ".claude/**", ".github/workflows/pr-check.yml"):
            self.assertIn(path, trigger["paths"])
        for job in self.workflow["jobs"].values():
            for step in job["steps"]:
                if "uses" in step:
                    self.assertIn(step["uses"], ["actions/checkout@v6", "actions/setup-python@v6",
                                                 "actions/setup-java@v6", "actions/cache@v6"])
        self.assertEqual(self.workflow["env"]["CODESPELL_VERSION"], "2.4.1")
        self.assertEqual(self.workflow["env"]["LANGUAGETOOL_VERSION"], "6.6")

    def test_structure_uses_read_only_entrypoint(self):
        steps = self.workflow["jobs"]["structure"]["steps"]
        self.assertEqual(steps[-1]["run"], "python scripts/precommit.py --base origin/master")
        self.assertNotIn("--fix", self.text)

    def test_grammar_optional_but_content_failure_blocks(self):
        steps = self.workflow["jobs"]["content"]["steps"]
        for name in ("Download LanguageTool", "Start LanguageTool server"):
            step = next(s for s in steps if s["name"] == name)
            self.assertEqual(step["continue-on-error"], "true")
        content = steps[-1]
        self.assertNotIn("continue-on-error", content)
        self.assertIn("scripts/pr_check.py --base origin/master", content["run"])
        self.assertIn('--languagetool "${{ steps.languagetool.outputs.url }}"', content["run"])

    def test_strict_build_changed_languages_and_script_fallback(self):
        run = self.workflow["jobs"]["build"]["steps"][-1]["run"]
        code = run.split("python - <<'PY'\n", 1)[1].rsplit("\nPY", 1)[0]
        for changed, expected in [(b"docs/de/docs/page.md\0docs/fr/docs/\xe4\xb8\xad.md\0", ["de", "fr"]),
                                  (b"", ["en"]),
                                  (b"docs/README.md\0", ["en"])]:
            with patch("subprocess.check_output", return_value=changed) as diff, \
                    patch("subprocess.run") as build, \
                    patch.object(Path, "is_file", autospec=True, side_effect=lambda p: p.parts[-2] in ("de", "fr", "en")), \
                    patch.dict(os.environ, {"RUNNER_TEMP": "temporary"}):
                exec(compile(code, "workflow-build", "exec"), {})
                self.assertIn("-z", diff.call_args.args[0])
                commands = [call.args[0] for call in build.call_args_list]
                self.assertEqual([c[3] for c in commands], [f"docs/{lang}/mkdocs.yml" for lang in expected])
                for call in build.call_args_list:
                    self.assertIn("--strict", call.args[0])
                    self.assertTrue(call.kwargs["check"])


if __name__ == "__main__":
    unittest.main()
