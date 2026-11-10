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
- for localized files with a matching English source: a staged per-language
  translation-cache record matching both the staged source and target hashes;
- for mkdocs.yml or added, renamed or deleted pages: orphan pages and redirect
  problems.

English-only commits do not require translations to be updated in the same
commit. English heading and anchor errors still block the commit.

For PR checks, pass ``--base origin/master`` to check the committed
merge-base...HEAD diff without auto-fixing IDs or changing the index. All
associated documentation, redirects and allowlist are read from HEAD, not
from staged or unstaged work. Approved legal text is compared with the merge
base. The local hook keeps its existing index-based behavior.

Bypass the local hook in an emergency with ``git commit --no-verify``.
"""

from __future__ import annotations

import argparse
from contextlib import contextmanager
import io
import json
import pathlib
import re
import subprocess
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import anchors  # noqa: E402
import i18n_check  # noqa: E402
import translation_delta  # noqa: E402

LANGS = anchors.LANGS
PATH_RE = re.compile(r"^docs/(?P<lang>[a-z]{2})/(?P<rest>.+)$")


def git(*args: str) -> str:
    return subprocess.run(
        ["git", *args], check=True, capture_output=True, text=True, encoding="utf-8",
    ).stdout


def staged_changes(base: str | None = None) -> list[tuple[str, str | None, str | None]]:
    """Return index changes, or committed base...HEAD changes, with rename sources."""
    revisions = [f"{base}...HEAD"] if base else ["--cached"]
    fields = iter(git("diff", *revisions, "--name-status", "--find-renames", "-z").split("\0")[:-1])
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


@contextmanager
def committed_docs(revision: str):
    """Read all documentation from a disposable snapshot, never the worktree/index.

    Extract only regular docs files and the allowlist. Reject links rather than
    following repository-controlled symlinks, and never execute snapshot files.
    The caller continues to run the already imported checkers.
    """
    roots = anchors.REPO_ROOT, anchors.DOCS_ROOT, i18n_check.DOCS_ROOT, i18n_check.ALLOWLIST_PATH
    with tempfile.TemporaryDirectory(prefix="kvm-pr-check-") as directory:
        root = pathlib.Path(directory)
        entries = []
        for entry in git("ls-tree", "-r", "-z", revision, "--", "docs/", "scripts/i18n_allowlist.yml").split("\0"):
            if not entry:
                continue
            metadata, name = entry.split("\t", 1)
            mode, kind, oid = metadata.split()
            path = pathlib.PurePosixPath(name)
            if path.is_absolute() or ".." in path.parts or "\\" in name:
                raise ValueError(f"unsafe documentation path: {name}")
            if kind != "blob" or mode not in ("100644", "100755"):
                raise ValueError(f"documentation must be a regular file: {name}")
            entries.append((path, oid))
        # Read raw blobs rather than git archive: export-ignore/export-subst
        # attributes must not change what the submitted tree actually contains.
        objects = subprocess.run(
            ["git", "cat-file", "--batch"],
            input="".join(f"{oid}\n" for _, oid in entries).encode("ascii"),
            check=True, capture_output=True,
        ).stdout
        stream = io.BytesIO(objects)
        for path, oid in entries:
            actual_oid, kind, size = stream.readline().decode("ascii").strip().split()
            if actual_oid != oid or kind != "blob":
                raise ValueError(f"cannot read documentation blob: {path}")
            destination = root.joinpath(*path.parts)
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(stream.read(int(size)))
            if stream.read(1) != b"\n":
                raise ValueError(f"invalid documentation blob: {path}")
        try:
            anchors.REPO_ROOT = root
            anchors.DOCS_ROOT = i18n_check.DOCS_ROOT = root / "docs"
            i18n_check.ALLOWLIST_PATH = root / "scripts/i18n_allowlist.yml"
            yield
        finally:
            (anchors.REPO_ROOT, anchors.DOCS_ROOT,
             i18n_check.DOCS_ROOT, i18n_check.ALLOWLIST_PATH) = roots


def checked_pages(lang: str, files: list[tuple[str, str]], revision: str = "") -> dict[str, anchors.Page]:
    """Use submitted text for touched pages, so unstaged fixes cannot hide errors."""
    pages = anchors.load_lang(lang)
    prefix = f"docs/{lang}/docs/"
    for status, path in files:
        if not path.startswith(prefix) or not path.endswith(".md"):
            continue
        rel = path[len(prefix):]
        if status == "D":
            pages.pop(rel, None)
        else:
            pages[rel] = anchors.load_page(lang, anchors.REPO_ROOT / path, revision_text(revision, path))
    return pages


def protected_errors(changes: list[tuple[str, str | None, str | None]],
                     before_revision: str = "HEAD", revision: str = "") -> list[str]:
    """Compare submitted revisions, including whole-page deletions and renames."""
    errors = []
    for _, old, new in changes:
        match = PATH_RE.match(old or "")
        if not match or match.group("lang") not in set(LANGS) - {anchors.SOURCE_LANG}:
            continue
        lang, rest = match.group("lang"), match.group("rest")
        if not rest.startswith("docs/") or not rest.endswith(".md"):
            continue
        before = revision_text(before_revision, old)
        after = revision_text(revision, new) if new and new.startswith(f"docs/{lang}/docs/") and new.endswith(".md") else None
        errors.extend(str(issue) for issue in i18n_check.check_protected_text(lang, rest[len("docs/"):], before, after))
    return errors


def cache_errors(files: list[tuple[str, str]], base: str | None = None) -> list[str]:
    """Require independent records for translations, using the index or PR HEAD.

    Other languages and English-only commits may remain pending. Existing
    legacy shared hashes are not evidence of an independently marked sync.
    """
    revision = "HEAD" if base else ""
    snapshot = "committed" if base else "staged"
    indexed = set((git("ls-tree", "-r", "--name-only", "-z", revision) if base
                   else git("ls-files", "-z")).split("\0"))
    candidates = []
    for status, path in files:
        match = PATH_RE.match(path)
        if status == "D" or not match or match.group("lang") not in translation_delta.DEFAULT_LANGS:
            continue
        lang, rest = match.group("lang"), match.group("rest")
        source = f"docs/en/{rest}"
        if source in indexed and not translation_delta.is_english_only(source):
            candidates.append((lang, source, path))
    cache_staged = any(path == translation_delta.CACHE_FILE for _, path in files)
    if not candidates and not cache_staged:
        return []
    try:
        raw = translation_delta.git_bytes(["show", f"{revision}:{translation_delta.CACHE_FILE}"])
        if raw[0]:
            raise ValueError(f"{snapshot} .translation-cache.json is missing")
        cache = json.loads(raw[1].decode("utf-8-sig"))
        if not isinstance(cache, dict):
            raise ValueError("cache root must be an object")
    except (ValueError, UnicodeError) as error:
        return [f"{translation_delta.CACHE_FILE}: invalid {snapshot} translation cache: {error}; "
                "restore the cache or run translation_delta.py mark and stage the cache"]

    errors = []
    for lang, source, path in candidates:
        entry = cache.get(source)
        targets = entry.get("targets") if isinstance(entry, dict) else None
        record = targets.get(lang) if isinstance(targets, dict) else None
        if not isinstance(record, dict) or "source_hash" in entry:
            errors.append(f"{path}: missing per-language cache baseline; run "
                          "python scripts/translation_delta.py migrate if using a legacy cache, then "
                          f"python scripts/translation_delta.py mark {source} --lang {lang} "
                          f"and stage {translation_delta.CACHE_FILE}")
            continue
        source_code, source_bytes = translation_delta.git_bytes(["show", f"{revision}:{source}"])
        target_code, target_bytes = translation_delta.git_bytes(["show", f"{revision}:{path}"])
        if source_code or target_code:
            errors.append(f"{path}: cannot read {snapshot} translation/source for cache validation")
            continue
        try:
            source_hash = translation_delta.hash_bytes(pathlib.Path(source), source_bytes)
            target_hash = translation_delta.hash_bytes(pathlib.Path(path), target_bytes)
        except UnicodeError as error:
            errors.append(f"{path}: invalid UTF-8 {snapshot} text: {error}")
            continue
        if record.get("source_hash") != source_hash or record.get("target_hash") != target_hash:
            errors.append(
                f"{path}: translation cache does not match {snapshot} source/target; run "
                f"python scripts/translation_delta.py mark {source} --lang {lang} "
                f"after validation and stage both {path} and {translation_delta.CACHE_FILE}"
            )
    return errors


def check_changes(base: str | None = None) -> int:
    changes = staged_changes(base)
    files = staged_files(changes)
    if not base:
        add_missing_ids(files)
    revision = "HEAD" if base else ""
    before = git("merge-base", base, "HEAD").strip() if base else "HEAD"
    errors = protected_errors(changes, before, revision)
    errors.extend(cache_errors(files, base))
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

    en_pages = checked_pages(anchors.SOURCE_LANG, files, revision)
    for lang in sorted(pages):
        report = anchors.Report()
        lang_pages = en_pages if lang == anchors.SOURCE_LANG else checked_pages(lang, files, revision)
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
        advice = "Fix and commit the changes before retrying." if base else "Fix them, or bypass with git commit --no-verify."
        print(f"pre-commit: {len(errors)} error(s). {advice}")
        return 1
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", help="check committed BASE...HEAD without editing files or the index")
    args = parser.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    try:
        if args.base:
            with committed_docs("HEAD"):
                return check_changes(args.base)
        return check_changes()
    except (subprocess.CalledProcessError, ValueError, UnicodeError, OSError) as error:
        print(f"ERROR pre-commit: unable to check submitted documentation: {error}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
