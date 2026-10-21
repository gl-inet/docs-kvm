#!/usr/bin/env python3
"""Checks run by .githooks/pre-commit on the files staged for a commit.

Enable the hook once per clone:
  git config core.hooksPath .githooks

For staged pages, the hook reports:
- heading ID and anchor problems (scripts/anchors.py); broken anchor links are
  reported for every page of the touched languages;
- for localized pages: structure and text problems (scripts/i18n_check.py);
- for mkdocs.yml or added, renamed or deleted pages: orphan pages and redirect
  problems.

English-only commits are not blocked because translations are usually
synced in a later commit.

Bypass in an emergency with ``git commit --no-verify``.
"""

from __future__ import annotations

import pathlib
import re
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import anchors  # noqa: E402
import i18n_check  # noqa: E402

LANGS = anchors.LANGS
PATH_RE = re.compile(r"^docs/(?P<lang>[a-z]{2})/(?P<rest>.+)$")


def staged_files() -> list[tuple[str, str]]:
    """Return (status, path) for staged changes; renames give the new path."""
    output = subprocess.run(
        ["git", "diff", "--cached", "--name-status", "--find-renames"],
        check=True, capture_output=True, text=True, encoding="utf-8",
    ).stdout
    files = []
    for line in output.splitlines():
        parts = line.split("\t")
        files.append((parts[0][0], parts[-1]))
        if parts[0][0] == "R":
            files.append(("D", parts[1]))
    return files


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    errors: list[str] = []
    pages: dict[str, set[str]] = {}  # lang -> staged pages relative to docs/<lang>/docs
    file_check_langs: set[str] = set()
    for status, path in staged_files():
        match = PATH_RE.match(path)
        if not match or match.group("lang") not in LANGS:
            continue
        lang, rest = match.group("lang"), match.group("rest")
        if rest == "mkdocs.yml" or (rest.startswith("docs/") and rest.endswith(".md") and status in "ADR"):
            file_check_langs.add(lang)
        if status == "D":
            continue
        if rest.startswith("docs/") and rest.endswith(".md"):
            pages.setdefault(lang, set()).add(rest[len("docs/"):])
    if not pages and not file_check_langs:
        return 0

    en_pages = anchors.load_lang(anchors.SOURCE_LANG)
    for lang in sorted(pages):
        report = anchors.Report()
        lang_pages = en_pages if lang == anchors.SOURCE_LANG else anchors.load_lang(lang)
        anchors.check_lang(lang, lang_pages, en_pages, report)
        for error in report.errors:
            rel = error.split(":", 1)[0].split("/", 1)[1]
            # Missing English IDs in pages nobody touched are translation backlog.
            if rel in pages[lang] or "broken anchor link" in error:
                errors.append(f"[anchors] {error}")

    for lang in sorted(file_check_langs):
        errors.extend(str(issue) for issue in i18n_check.check_language_files(lang))

    for lang in sorted(set(pages) - {anchors.SOURCE_LANG}):
        for rel in sorted(pages[lang]):
            if (anchors.DOCS_ROOT / anchors.SOURCE_LANG / "docs" / rel).exists():
                errors.extend(str(issue) for issue in i18n_check.check_page(lang, rel))

    errors = list(dict.fromkeys(errors))
    for error in errors:
        print(f"ERROR {error}")
    if errors:
        print(f"pre-commit: {len(errors)} error(s). Fix them, or bypass with git commit --no-verify.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
