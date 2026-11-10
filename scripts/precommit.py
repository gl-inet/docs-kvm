#!/usr/bin/env python3
"""Checks run by .githooks/pre-commit on the files staged for a commit.

Enable the hook once per clone:
  git config core.hooksPath .githooks

The hook first adds MkDocs-generated IDs to English headings that have no
explicit ID and stages the fix. Pages with unstaged changes are left untouched.
Existing explicit IDs are never rewritten.

For staged pages, the hook reports:
- heading ID and anchor problems (scripts/anchors.py); broken anchor links are
  reported for every page of the touched languages;
- for localized pages: structure and text problems (scripts/i18n_check.py),
  and approved legal sections or pages removed or changed between HEAD and
  the staged version (including deleted and renamed pages);
- for mkdocs.yml or added, renamed or deleted pages: orphan pages and redirect
  problems.

English-only commits do not require translations to be updated in the same
commit. English heading and anchor errors still block the commit.

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


def git(*args: str) -> str:
    return subprocess.run(
        ["git", *args], check=True, capture_output=True, text=True, encoding="utf-8",
    ).stdout


def staged_changes() -> list[tuple[str, str | None, str | None]]:
    """Return (status, old path, new path), preserving rename sources and Unicode paths."""
    fields = iter(git("diff", "--cached", "--name-status", "--find-renames", "-z").split("\0")[:-1])
    changes = []
    for status in fields:
        path = next(fields)
        kind = status[0]
        if kind == "R":
            changes.append((kind, path, next(fields)))
        else:
            changes.append((kind, None if kind == "A" else path, None if kind == "D" else path))
    return changes


def staged_files(changes: list[tuple[str, str | None, str | None]]) -> list[tuple[str, str]]:
    """Expand rename sources into deletions for the existing page/file checks."""
    files = []
    for status, old, new in changes:
        files.append((status, new or old))
        if status == "R":
            files.append(("D", old))
    return files


def add_missing_ids(files: list[tuple[str, str]]) -> None:
    """Only edit fully staged regular English pages; never stage unrelated work."""
    unstaged = set(git("diff", "--name-only", "-z").split("\0"))
    for status, path in files:
        if status == "D" or not path.startswith("docs/en/docs/") or not path.endswith(".md"):
            continue
        if path in unstaged or pathlib.Path(path).is_symlink():
            print(f"pre-commit: {path} has unstaged changes or is not a regular page; add heading IDs by hand")
            continue
        page = anchors.load_page(anchors.SOURCE_LANG, anchors.REPO_ROOT / path)
        if page.render_mismatch:
            continue
        missing = [h for h in page.headings if h.explicit_id is None and h.rendered_id]
        for heading in missing:
            anchors.set_heading_id(page, heading, heading.rendered_id)
        if missing:
            anchors.write_page(page)
            git("add", "--", path)
            print(f"pre-commit: added heading IDs to {path}: {', '.join(h.rendered_id for h in missing)}")


def revision_text(revision: str, path: str) -> str:
    # These paths came from git diff, so missing blobs indicate a real Git error.
    return git("show", f"{revision}:{path}")


def checked_pages(lang: str, files: list[tuple[str, str]]) -> dict[str, anchors.Page]:
    """Use staged text for touched pages, so unstaged fixes cannot hide heading errors."""
    pages = anchors.load_lang(lang)
    prefix = f"docs/{lang}/docs/"
    for status, path in files:
        if not path.startswith(prefix) or not path.endswith(".md"):
            continue
        rel = path[len(prefix):]
        if status == "D":
            pages.pop(rel, None)
        else:
            pages[rel] = anchors.load_page(lang, anchors.REPO_ROOT / path, revision_text("", path))
    return pages


def protected_errors(changes: list[tuple[str, str | None, str | None]]) -> list[str]:
    """Compare HEAD with the index, not the working tree, including whole-page deletions."""
    errors = []
    for _, old, new in changes:
        match = PATH_RE.match(old or "")
        if not match or match.group("lang") not in set(LANGS) - {anchors.SOURCE_LANG}:
            continue
        lang, rest = match.group("lang"), match.group("rest")
        if not rest.startswith("docs/") or not rest.endswith(".md"):
            continue
        before = revision_text("HEAD", old)
        after = revision_text("", new) if new and new.startswith(f"docs/{lang}/docs/") and new.endswith(".md") else None
        errors.extend(str(issue) for issue in i18n_check.check_protected_text(lang, rest[len("docs/"):], before, after))
    return errors


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    changes = staged_changes()
    files = staged_files(changes)
    add_missing_ids(files)
    errors = protected_errors(changes)
    pages: dict[str, set[str]] = {}  # lang -> staged pages relative to docs/<lang>/docs
    file_check_langs: set[str] = set()
    for status, path in files:
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
    if not pages and not file_check_langs and not errors:
        return 0

    en_pages = checked_pages(anchors.SOURCE_LANG, files)
    for lang in sorted(pages):
        report = anchors.Report()
        lang_pages = en_pages if lang == anchors.SOURCE_LANG else checked_pages(lang, files)
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
