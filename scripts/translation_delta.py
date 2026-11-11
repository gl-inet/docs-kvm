#!/usr/bin/env python3
"""Report KVM translation deltas per language; mark, diff, migrate or prune.

Text hashes normalize UTF-8 BOM and CRLF/CR to LF; binary hashes use raw bytes.
Only existing legacy target records inherit a shared source hash. Migration never
asserts that an unrecorded translation is synced. Run from the repository root.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import re
import subprocess
import sys
import time
from dataclasses import dataclass, field
from typing import Iterable

DEFAULT_LANGS = ("de", "es", "fr", "it", "ja", "nl", "pl", "sv")
DEFAULT_TEXT_EXTENSIONS = (".md", ".yml", ".yaml", ".html", ".css", ".js", ".svg", ".txt", ".json")
DEFAULT_EXCLUDE_DIRS = {".git", "__pycache__", "site"}
CACHE_FILE = DEFAULT_CACHE_FILE = ".translation-cache.json"
DEFAULT_EN_ROOT = "docs/en"
ENGLISH_ONLY_FILENAMES = {"regulatory_statement.md", "fcc_ic_compliance_statements.md"}
NO_TARGET_CHANGE_MODEL = "reviewed-no-target-change"
PROTECTED_IDS = {"safety-information", "declaration-of-conformity"}
HEADING = re.compile(r"^(#{1,6})\s+.*?\{#([^}]+)\}\s*$")


def repo_path(path: pathlib.Path) -> str:
    return path.as_posix()


def parse_csv(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def read_json(path: pathlib.Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8-sig")) if path.exists() else {}


def write_json(path: pathlib.Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def normalized(data: bytes) -> str:
    return data.decode("utf-8-sig").replace("\r\n", "\n").replace("\r", "\n")


def hash_bytes(path: pathlib.Path, data: bytes, text_extensions=None) -> str:
    extensions = set(DEFAULT_TEXT_EXTENSIONS) if text_extensions is None else text_extensions
    if path.suffix.lower() in extensions:
        data = normalized(data).encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def source_hash(path: pathlib.Path, text_extensions=None) -> str:
    return hash_bytes(path, path.read_bytes(), text_extensions)


def target_hash(path: pathlib.Path) -> str:
    return source_hash(path)


def is_english_only(source: str) -> bool:
    return pathlib.PurePosixPath(source).name in ENGLISH_ONLY_FILENAMES


def target_path_for_lang(source: str, lang: str) -> pathlib.Path:
    path = pathlib.PurePosixPath(source)
    if not source.startswith("docs/en/") or any(p in ("..", ".") for p in path.parts) or "\\" in source:
        raise ValueError(f"Unexpected English source path: {source}")
    if lang not in DEFAULT_LANGS:
        raise ValueError(f"Unknown language: {lang}")
    return pathlib.Path("docs", lang, *path.parts[2:])


def git_bytes(args: list[str], data: bytes | None = None) -> tuple[int, bytes]:
    try:
        proc = subprocess.run(["git", *args], input=data, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return proc.returncode, proc.stdout
    except FileNotFoundError:
        return 127, b""


def run_git(args: list[str]) -> tuple[int, str]:
    code, output = git_bytes(args)
    return code, output.decode("utf-8", errors="replace").strip()


def collect_preflight() -> dict:
    _, branch = run_git(["branch", "--show-current"])
    _, status = run_git(["status", "--short"])
    code, upstream = run_git(["rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}"])
    ahead = behind = None
    if code == 0:
        code, counts = run_git(["rev-list", "--left-right", "--count", f"HEAD...{upstream}"])
        if code == 0 and len(counts.split()) == 2:
            ahead, behind = map(int, counts.split())
    warnings = ["working tree is not clean"] if status else []
    if behind:
        warnings.append(f"branch is behind {upstream} by {behind} commit(s)")
    return dict(branch=branch, upstream=upstream, ahead=ahead, behind=behind, status=status.splitlines(), warnings=warnings)


def iter_source_files(en_root: pathlib.Path, exclude_dirs=DEFAULT_EXCLUDE_DIRS) -> Iterable[pathlib.Path]:
    if not en_root.is_dir():
        raise FileNotFoundError(f"English source root not found: {en_root}")
    for path in sorted(en_root.rglob("*")):
        if path.is_file() and not any(p in exclude_dirs for p in path.parts):
            yield path


def target_record(cache: dict, source: str, lang: str) -> dict:
    entry = cache.get(source, {})
    if not isinstance(entry, dict):
        return {}
    targets = entry.get("targets") or {}
    # Absence is not evidence of an existing translated baseline.
    if lang not in targets or not isinstance(targets[lang], dict):
        return {}
    record = dict(targets[lang])
    if "source_hash" not in record and entry.get("source_hash"):
        record["source_hash"] = entry["source_hash"]
    return record


@dataclass
class SourceStatus:
    path: str
    current_hash: str
    cache_missing: list[str] = field(default_factory=list)
    hash_mismatch: list[str] = field(default_factory=list)
    missing_targets: list[str] = field(default_factory=list)
    english_only: bool = False


def analyze_sources(source_files, cache, langs, text_extensions=None) -> list[SourceStatus]:
    statuses = []
    for path in source_files:
        source = repo_path(path)
        status = SourceStatus(source, source_hash(path, text_extensions), english_only=is_english_only(source))
        if not status.english_only:
            for lang in langs:
                cached = target_record(cache, source, lang).get("source_hash")
                if not target_path_for_lang(source, lang).is_file():
                    status.missing_targets.append(lang)
                elif not cached:
                    status.cache_missing.append(lang)
                elif cached != status.current_hash:
                    status.hash_mismatch.append(lang)
        statuses.append(status)
    return statuses


def stale_cache_keys(cache: dict) -> list[str]:
    return sorted(k for k in cache if k.startswith("docs/en/") and not is_english_only(k) and not pathlib.Path(k).exists())


def build_report(preflight, statuses, stale) -> dict:
    report = {"preflight": preflight}
    for key, attr, languages in (("cache_missing", "cache_missing", "langs"), ("hash_mismatch", "hash_mismatch", "langs"), ("target_missing", "missing_targets", "missing_targets")):
        report[key] = [{"path": s.path, languages: getattr(s, attr)} for s in statuses if getattr(s, attr)]
    report["english_only"] = [s.path for s in statuses if s.english_only]
    report["stale_cache_keys"] = stale
    return report


def cmd_report(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache-file", default=CACHE_FILE)
    parser.add_argument("--en-root", default=DEFAULT_EN_ROOT)
    parser.add_argument("--langs", default=",".join(DEFAULT_LANGS))
    parser.add_argument("--text-extensions", "--extensions", default=",".join(DEFAULT_TEXT_EXTENSIONS))
    parser.add_argument("--exclude-dirs", default=",".join(sorted(DEFAULT_EXCLUDE_DIRS)))
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--fail-on-delta", action="store_true")
    args = parser.parse_args(argv)
    langs = parse_csv(args.langs)
    if set(langs) - set(DEFAULT_LANGS):
        parser.error("unsupported target language")
    cache = read_json(pathlib.Path(args.cache_file))
    extensions = {e if e.startswith(".") else "." + e for e in parse_csv(args.text_extensions)}
    statuses = analyze_sources(iter_source_files(pathlib.Path(args.en_root), set(parse_csv(args.exclude_dirs))), cache, langs, extensions)
    report = build_report(collect_preflight(), statuses, stale_cache_keys(cache))
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print("Preflight")
        for key, value in report["preflight"].items():
            print(f"  {key}: {value}")
        for key, rows in report.items():
            if key != "preflight":
                print(f"\n{key} ({len(rows)})")
                for row in rows:
                    print(f"  {row}")
    return int(args.fail_on_delta and any(report[k] for k in ("cache_missing", "hash_mismatch", "target_missing", "stale_cache_keys")))


def source_arg(value: str, *, absent=False) -> str:
    try:
        rel = pathlib.Path(value).resolve().relative_to(pathlib.Path.cwd().resolve()).as_posix()
    except ValueError:
        raise ValueError(f"{value}: pass a path inside the repository")
    target_path_for_lang(rel, "de")
    if is_english_only(rel):
        raise ValueError(f"{rel}: English-only regulatory source is not actionable")
    if not absent and not pathlib.Path(rel).is_file():
        raise ValueError(f"{rel}: file not found")
    return rel


def protected_parts(text: str, stable_ids: set[str]) -> tuple[list[str], list[tuple[str, int, str, str]]]:
    """Own trusted check, independent of the workflow guard and i18n allowlists."""
    lines = text.splitlines(keepends=True)
    headings = [(i, len(m[1]), m[2]) for i, line in enumerate(lines) if (m := HEADING.match(line.rstrip("\r\n")))]
    sections, placements = [], []
    for pos, (index, level, ident) in enumerate(headings):
        if ident not in PROTECTED_IDS:
            continue
        end = next((j for j in range(index + 1, len(lines)) if (m := re.match(r"^(#{1,6})\s+", lines[j])) and len(m[1]) <= level), len(lines))
        sections.append("".join(lines[index:end]))
        ordinal = sum(h[2] not in PROTECTED_IDS for h in headings[:pos])
        before = next((h[2] for h in reversed(headings[:pos]) if h[2] in stable_ids), "")
        after = next((h[2] for h in headings[pos + 1:] if h[2] in stable_ids), "")
        placements.append((ident, ordinal, before, after))
    return sections, placements


def legal_errors(target: pathlib.Path, after: str) -> list[str]:
    if target.suffix.lower() not in DEFAULT_TEXT_EXTENSIONS:
        return []
    code, raw = git_bytes(["show", f"HEAD:{target.as_posix()}"])
    if code:
        # Distinguish a new file from an unavailable HEAD/repository; fail closed.
        if run_git(["rev-parse", "--verify", "HEAD"])[0]:
            return ["Cannot verify approved legal wording: HEAD unavailable"]
        if run_git(["cat-file", "-e", f"HEAD:{target.as_posix()}"])[0] == 0:
            return ["Cannot read approved legal baseline"]
        before = ""
    else:
        before = normalized(raw)
    errors = []
    if target.suffix == ".md":
        # Keep this trusted check independent of the workflow guard. Normal title
        # updates may rename neighboring IDs without moving approved legal text.
        old_ids = {m[2] for line in before.splitlines() if (m := HEADING.match(line))}
        new_ids = {m[2] for line in after.splitlines() if (m := HEADING.match(line))}
        stable_ids = (old_ids & new_ids) - PROTECTED_IDS
        if protected_parts(before, stable_ids) != protected_parts(after, stable_ids):
            errors.append("Approved legal wording or placement changed since HEAD")
    for stem in ("regulatory_statement", "fcc_ic_compliance_statements"):
        pattern = rf"(?<![A-Za-z0-9_-]){stem}(?=$|[^A-Za-z0-9_-])"
        if len(re.findall(pattern, after)) > len(re.findall(pattern, before)):
            errors.append("Added an English-only regulatory reference")
    return errors


def check_target(source: str, lang: str, file_checks: dict) -> list[str]:
    target = target_path_for_lang(source, lang)
    errors = legal_errors(target, normalized(target.read_bytes())) if target.suffix.lower() in DEFAULT_TEXT_EXTENSIONS else []
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    import i18n_check
    if source.startswith("docs/en/docs/") and source.endswith(".md"):
        errors.extend(map(str, i18n_check.check_page(lang, source[len("docs/en/docs/"):])))
    elif source == "docs/en/mkdocs.yml":
        if lang not in file_checks:
            file_checks[lang] = i18n_check.check_language_files(lang)
        errors.extend(map(str, file_checks[lang]))
    return errors


def find_source_blob(source: str, expected: str) -> str | None:
    """Return a reachable committed blob with the exact normalized hash.

    Never strip content, approximate terminal newlines, or create dangling blobs.
    Deleted files and arbitrarily old baselines are included in history searches.
    """
    code, commits = run_git(["rev-list", "HEAD", "--", source])
    if code:
        return None
    seen = set()
    for commit in commits.split():
        code, blob = run_git(["rev-parse", f"{commit}:{source}"])
        if code or blob in seen:
            continue
        seen.add(blob)
        code, raw = git_bytes(["cat-file", "blob", blob])
        if not code:
            try:
                if hash_bytes(pathlib.Path(source), raw) == expected:
                    return blob
            except UnicodeDecodeError:
                continue
    return None


def upgrade_entry(source: str, entry: dict, blob_memo: dict | None = None) -> tuple[int, int]:
    """Conservative legacy conversion, preserving all existing per-lang metadata."""
    if "source_hash" not in entry:
        return 0, 0
    legacy = entry.pop("source_hash")
    missing = 0
    if blob_memo is None:
        blob_memo = {}
    for lang, record in (entry.get("targets") or {}).items():
        if not isinstance(record, dict) or "source_hash" in record:
            continue
        record["source_hash"] = legacy
        key = (source, legacy)
        if key not in blob_memo:
            blob_memo[key] = find_source_blob(source, legacy) if legacy else None
        blob = blob_memo[key]
        if blob:
            record.setdefault("source_blob", blob)
        else:
            missing += 1
        path = pathlib.Path(source)
        target = target_path_for_lang(source, lang)
        # A changed/uncommitted localized file is not a known baseline. Do not
        # seed a target hash unless both current versions are recorded in HEAD.
        if path.is_file() and target.is_file() and source_hash(path) == legacy:
            code, raw = git_bytes(["show", f"HEAD:{target.as_posix()}"])
            if not code and hash_bytes(target, raw) == target_hash(target):
                record.setdefault("target_hash", target_hash(target))
    return 1, missing


def cmd_migrate(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Convert existing legacy target records; never invent missing languages.")
    parser.add_argument("--cache-file", default=CACHE_FILE)
    args = parser.parse_args(argv)
    path = pathlib.Path(args.cache_file)
    cache = read_json(path)
    converted = unknown = 0
    for source, entry in cache.items():
        if source.startswith("docs/en/") and isinstance(entry, dict):
            count, missing = upgrade_entry(source, entry)
            converted += count
            unknown += missing
    if converted:
        write_json(path, cache)
    print(f"converted {converted} entries; {unknown} language records without a reachable English snapshot")
    return 0


def cmd_mark(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Mark only validated, explicitly synchronized translations.")
    parser.add_argument("sources", nargs="+")
    parser.add_argument("--lang", nargs="+", required=True)
    parser.add_argument("--no-target-change", action="store_true")
    parser.add_argument("--model", default="manual-sync")
    parser.add_argument("--cache-file", default=CACHE_FILE)
    args = parser.parse_args(argv)
    langs = list(DEFAULT_LANGS) if args.lang == ["all"] else args.lang
    if set(langs) - set(DEFAULT_LANGS) or (args.no_target_change and args.lang == ["all"]):
        parser.error("use supported explicit languages for --no-target-change; otherwise --lang all is allowed")
    sources = list(dict.fromkeys(source_arg(s) for s in args.sources))
    path = pathlib.Path(args.cache_file)
    cache = read_json(path)
    checks = {}
    marked = failed = 0
    for source in sources:
        current = source_hash(pathlib.Path(source))
        blob = find_source_blob(source, current)
        for lang in dict.fromkeys(langs):
            target = target_path_for_lang(source, lang)
            errors = list(check_target(source, lang, checks)) if target.is_file() else [f"Missing target: {target}"]
            record = target_record(cache, source, lang)
            new_hash = target_hash(target) if target.is_file() else None
            changed = record.get("source_hash") != current
            baseline = record.get("target_hash")
            if changed and not args.no_target_change:
                if baseline is None:
                    code, raw = git_bytes(["show", f"HEAD:{target.as_posix()}"])
                    if not code:
                        baseline = hash_bytes(target, raw)
                if baseline == new_hash:
                    errors.append("English changed but target did not; translate it or explicitly pass --no-target-change")
            if errors:
                print(f"FAIL {lang}: {source}: " + "; ".join(errors))
                failed += 1
                continue
            if not changed and record.get("target_hash") == new_hash:
                print(f"OK {lang}: {source} (already synced, unchanged)")
                continue
            entry = cache.setdefault(source, {})
            upgrade_entry(source, entry)
            new_record = dict(record)
            new_record.update(source_hash=current, target_hash=new_hash, model=NO_TARGET_CHANGE_MODEL if args.no_target_change else args.model, updated_at=int(time.time()))
            new_record.pop("source_blob", None)
            if blob:
                new_record["source_blob"] = blob
            else:
                print(f"NOTE {source}: uncommitted English version; no reachable snapshot, diff will request a whole-file review")
            entry.setdefault("targets", {})[lang] = new_record
            marked += 1
            print(f"OK {lang}: {source}")
    if marked:
        write_json(path, cache)
    print(f"marked {marked}, failed {failed}")
    return int(bool(failed))


def cmd_diff(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Show English changes since one language was synchronized.")
    parser.add_argument("source")
    parser.add_argument("--lang", required=True, choices=DEFAULT_LANGS)
    parser.add_argument("--cache-file", default=CACHE_FILE)
    args = parser.parse_args(argv)
    source = source_arg(args.source, absent=True)
    record = target_record(read_json(pathlib.Path(args.cache_file)), source, args.lang)
    blob = record.get("source_blob")
    if not blob or not re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", blob) or run_git(["cat-file", "-e", f"{blob}^{{blob}}"])[0]:
        print(f"No stored English version for {args.lang}; review the whole file: {source}")
        return 1
    code, old = git_bytes(["cat-file", "blob", blob])
    if code:
        return 1
    import difflib
    path = pathlib.Path(source)
    new = path.read_bytes() if path.is_file() else b""
    if path.is_file() and hash_bytes(path, old) == hash_bytes(path, new):
        print(f"{source} has not changed since {args.lang} was synced.")
    elif path.suffix.lower() in DEFAULT_TEXT_EXTENSIONS:
        print("".join(difflib.unified_diff(normalized(old).splitlines(keepends=True), normalized(new).splitlines(keepends=True), fromfile=f"{source} ({args.lang} baseline)", tofile=source)), end="")
    else:
        print(f"Binary source changed: {source}" + (" (deleted)" if not path.exists() else ""))
    return 0


def cmd_prune(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Remove stale cache entries only after all localized targets are absent and legal checks pass.")
    parser.add_argument("sources", nargs="*")
    parser.add_argument("--cache-file", default=CACHE_FILE)
    args = parser.parse_args(argv)
    path = pathlib.Path(args.cache_file)
    cache = read_json(path)
    sources = [source_arg(s, absent=True) for s in args.sources] if args.sources else stale_cache_keys(cache)
    errors = []
    for source in sources:
        source_arg(source, absent=True)
        if pathlib.Path(source).exists() or source not in cache:
            errors.append(f"{source}: not a stale cache entry")
        for lang in DEFAULT_LANGS:
            target = target_path_for_lang(source, lang)
            if target.exists():
                errors.append(f"{source}: localized target still exists: {target}")
            errors.extend(legal_errors(target, ""))
    if errors:
        print("Prune refused: " + "; ".join(errors))
        return 1
    for source in sources:
        del cache[source]
    if sources:
        write_json(path, cache)
    print(f"pruned {len(sources)} entries")
    return 0


def main() -> int:
    argv = sys.argv[1:]
    if argv and argv[0] == "update":
        print("Bulk update is disabled: use mark <en-file> --lang <lang> after validating the translation; use prune for deleted sources.", file=sys.stderr)
        return 2
    commands = {"mark": cmd_mark, "diff": cmd_diff, "migrate": cmd_migrate, "prune": cmd_prune, "report": cmd_report, "list": cmd_report}
    try:
        return commands[argv[0]](argv[1:]) if argv and argv[0] in commands else cmd_report(argv)
    except (ValueError, OSError) as error:
        print(str(error), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
