#!/usr/bin/env python3
"""Report and update translation-cache deltas for GL.iNet KVM docs."""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import subprocess
import sys
import time
from dataclasses import dataclass
from typing import Iterable


DEFAULT_CACHE_FILE = ".translation-cache.json"
DEFAULT_EN_ROOT = "docs/en"
DEFAULT_MODEL = "gpt-5-codex"
DEFAULT_TEXT_EXTENSIONS = (
    ".md",
    ".yml",
    ".yaml",
    ".html",
    ".css",
    ".js",
    ".svg",
    ".txt",
    ".json",
)
DEFAULT_EXCLUDE_DIRS = {".git", "__pycache__", "site"}
ENGLISH_ONLY_FILENAMES = {
    "fcc_ic_compliance_statements.md",
    "regulatory_statement.md",
}


@dataclass(frozen=True)
class SourceStatus:
    path: str
    current_hash: str
    cached_hash: str
    status: str
    missing_targets: list[str]
    english_only: bool


def repo_path(path: pathlib.Path) -> str:
    return path.as_posix()


def parse_csv(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def read_json(path: pathlib.Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: pathlib.Path, data: dict) -> None:
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def source_hash(path: pathlib.Path, text_extensions: set[str]) -> str:
    suffix = path.suffix.lower()
    if suffix in text_extensions:
        text = path.read_text(encoding="utf-8-sig")
        normalized = text.replace("\r\n", "\n").replace("\r", "\n")
        return hashlib.sha256(normalized.encode("utf-8")).hexdigest()
    return hashlib.sha256(path.read_bytes()).hexdigest()


def is_english_only(source_path: str) -> bool:
    return pathlib.PurePosixPath(source_path).name in ENGLISH_ONLY_FILENAMES


def target_path_for_lang(source_path: str, lang: str) -> pathlib.Path:
    if source_path.startswith("docs/en/docs/"):
        return pathlib.Path(source_path.replace("docs/en/docs/", f"docs/{lang}/docs/", 1))
    if source_path.startswith("docs/en/"):
        return pathlib.Path(source_path.replace("docs/en/", f"docs/{lang}/", 1))
    raise ValueError(f"Unexpected English source path: {source_path}")


def detect_langs() -> list[str]:
    docs_root = pathlib.Path("docs")
    langs: list[str] = []
    if not docs_root.exists():
        return langs
    for path in sorted(docs_root.iterdir()):
        if path.is_dir() and path.name != "en" and (path / "mkdocs.yml").exists():
            langs.append(path.name)
    return langs


def run_git(args: list[str]) -> tuple[int, str]:
    try:
        proc = subprocess.run(
            ["git", *args],
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
    except FileNotFoundError:
        return 127, "git not found"
    return proc.returncode, proc.stdout.strip()


def collect_preflight() -> dict[str, object]:
    branch_code, branch = run_git(["branch", "--show-current"])
    status_code, status = run_git(["status", "--short"])
    upstream_code, upstream = run_git(["rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}"])
    ahead = None
    behind = None
    if upstream_code == 0 and upstream:
        divergence_code, divergence = run_git(["rev-list", "--left-right", "--count", f"HEAD...{upstream}"])
        if divergence_code == 0 and divergence:
            parts = divergence.split()
            if len(parts) == 2:
                ahead = int(parts[0])
                behind = int(parts[1])

    status_lines = status.splitlines() if status_code == 0 and status else []
    warnings: list[str] = []
    if status_lines:
        warnings.append("working tree is not clean")
    if behind:
        warnings.append(f"branch is behind {upstream} by {behind} commit(s)")

    return {
        "branch": branch if branch_code == 0 else "",
        "upstream": upstream if upstream_code == 0 else "",
        "ahead": ahead,
        "behind": behind,
        "status": status_lines,
        "warnings": warnings,
    }


def iter_source_files(en_root: pathlib.Path, exclude_dirs: set[str]) -> Iterable[pathlib.Path]:
    if not en_root.exists():
        raise FileNotFoundError(f"English source root not found: {en_root}")
    for path in sorted(en_root.rglob("*")):
        if not path.is_file():
            continue
        if any(part in exclude_dirs for part in path.parts):
            continue
        yield path


def analyze_sources(
    source_files: Iterable[pathlib.Path],
    cache: dict,
    langs: list[str],
    text_extensions: set[str],
) -> list[SourceStatus]:
    statuses: list[SourceStatus] = []
    for path in source_files:
        source_rel = repo_path(path)
        cache_entry = cache.get(source_rel, {})
        cached_hash = cache_entry.get("source_hash", "") if isinstance(cache_entry, dict) else ""
        current_hash = source_hash(path, text_extensions)
        if not cached_hash:
            status = "cache-missing"
        elif cached_hash != current_hash:
            status = "hash-mismatch"
        else:
            status = "synced"

        english_only = is_english_only(source_rel)
        missing_targets: list[str] = []
        if not english_only:
            missing_targets = [
                lang for lang in langs if not target_path_for_lang(source_rel, lang).exists()
            ]
            if missing_targets and status == "synced":
                status = "target-missing"

        statuses.append(
            SourceStatus(
                path=source_rel,
                current_hash=current_hash,
                cached_hash=cached_hash,
                status=status,
                missing_targets=missing_targets,
                english_only=english_only,
            )
        )
    return statuses


def stale_cache_keys(cache: dict) -> list[str]:
    stale: list[str] = []
    for key in sorted(cache):
        if key.startswith("docs/en/") and not pathlib.Path(key).exists():
            stale.append(key)
    return stale


def print_section(title: str, rows: list[str]) -> None:
    print(f"\n{title} ({len(rows)})")
    if not rows:
        print("  none")
        return
    for row in rows:
        print(f"  {row}")


def build_report(preflight: dict[str, object], statuses: list[SourceStatus], stale: list[str]) -> dict:
    return {
        "preflight": preflight,
        "cache_missing": [item.path for item in statuses if item.status == "cache-missing"],
        "hash_mismatch": [item.path for item in statuses if item.status == "hash-mismatch"],
        "target_missing": [
            {"path": item.path, "missing_targets": item.missing_targets}
            for item in statuses
            if item.missing_targets
        ],
        "english_only": [item.path for item in statuses if item.english_only],
        "stale_cache_keys": stale,
    }


def print_report(report: dict) -> None:
    preflight = report["preflight"]
    print("Preflight")
    print(f"  branch: {preflight.get('branch') or '(unknown)'}")
    print(f"  upstream: {preflight.get('upstream') or '(none)'}")
    ahead = preflight.get("ahead")
    behind = preflight.get("behind")
    if ahead is None or behind is None:
        print("  divergence: (not checked)")
    else:
        print(f"  divergence: ahead {ahead}, behind {behind}")
    warnings = preflight.get("warnings") or []
    if warnings:
        print("  warnings:")
        for warning in warnings:
            print(f"    {warning}")
    status_lines = preflight.get("status") or []
    if status_lines:
        print("  working tree:")
        for line in status_lines:
            print(f"    {line}")
    else:
        print("  working tree: clean")

    print_section("Cache missing", report["cache_missing"])
    print_section("Hash mismatch", report["hash_mismatch"])
    print_section(
        "Target missing",
        [
            f"{item['path']} -> missing {','.join(item['missing_targets'])}"
            for item in report["target_missing"]
        ],
    )
    print_section("English-only source files", report["english_only"])
    print_section("Stale cache keys", report["stale_cache_keys"])


def build_updated_cache(
    source_files: Iterable[pathlib.Path],
    cache: dict,
    target_langs: list[str],
    text_extensions: set[str],
    model: str,
    updated_at: int,
) -> dict:
    entries: dict[str, dict] = {}
    for path in source_files:
        source_rel = repo_path(path)
        current_hash = source_hash(path, text_extensions)
        targets: dict[str, dict] = {}
        cache_entry = cache.get(source_rel, {})
        cached_hash = ""
        if isinstance(cache_entry, dict) and isinstance(cache_entry.get("targets"), dict):
            targets.update(cache_entry["targets"])
        if isinstance(cache_entry, dict):
            cached_hash = cache_entry.get("source_hash", "")

        if not is_english_only(source_rel):
            for lang in target_langs:
                if target_path_for_lang(source_rel, lang).exists():
                    target_missing = lang not in targets
                    source_changed = cached_hash != current_hash
                    if target_missing or source_changed:
                        targets[lang] = {
                            "model": model,
                            "updated_at": updated_at,
                        }

        entries[source_rel] = {
            "source_hash": current_hash,
            "targets": targets,
        }

    updated: dict[str, dict] = {}
    for key in cache:
        if key in entries:
            updated[key] = entries.pop(key)
    for key in sorted(entries):
        updated[key] = entries[key]
    return updated


def add_common_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--cache-file", default=DEFAULT_CACHE_FILE)
    parser.add_argument("--en-root", default=DEFAULT_EN_ROOT)
    parser.add_argument(
        "--text-extensions",
        default=",".join(DEFAULT_TEXT_EXTENSIONS),
        help="Comma-separated extensions hashed as LF-normalized UTF-8 text.",
    )
    parser.add_argument(
        "--exclude-dirs",
        default=",".join(sorted(DEFAULT_EXCLUDE_DIRS)),
        help="Comma-separated directory names to skip under the English root.",
    )


def command_list(args: argparse.Namespace) -> int:
    langs = parse_csv(args.langs) if args.langs else detect_langs()
    text_extensions = {
        ext if ext.startswith(".") else f".{ext}" for ext in parse_csv(args.text_extensions)
    }
    exclude_dirs = set(parse_csv(args.exclude_dirs))
    cache = read_json(pathlib.Path(args.cache_file))
    statuses = analyze_sources(
        iter_source_files(pathlib.Path(args.en_root), exclude_dirs),
        cache,
        langs,
        text_extensions,
    )
    report = build_report(collect_preflight(), statuses, stale_cache_keys(cache))
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print_report(report)

    has_delta = any(
        report[key]
        for key in ("cache_missing", "hash_mismatch", "target_missing", "stale_cache_keys")
    )
    return 1 if args.fail_on_delta and has_delta else 0


def command_update(args: argparse.Namespace) -> int:
    target_langs = parse_csv(args.target) if args.target else detect_langs()
    if not target_langs:
        print("No target languages found. Pass --target de or add localized mkdocs.yml files.", file=sys.stderr)
        return 2

    text_extensions = {
        ext if ext.startswith(".") else f".{ext}" for ext in parse_csv(args.text_extensions)
    }
    exclude_dirs = set(parse_csv(args.exclude_dirs))
    cache_file = pathlib.Path(args.cache_file)
    cache = read_json(cache_file)
    source_files = list(iter_source_files(pathlib.Path(args.en_root), exclude_dirs))
    updated = build_updated_cache(
        source_files,
        cache,
        target_langs,
        text_extensions,
        args.model,
        int(args.updated_at or time.time()),
    )
    write_json(cache_file, updated)
    print(f"Updated {cache_file} with {len(updated)} English source entries.")
    print(f"Targets: {', '.join(target_langs)}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    list_parser = subparsers.add_parser("list", help="Report cache/hash/target deltas.")
    add_common_args(list_parser)
    list_parser.add_argument("--langs", default="", help="Comma-separated target languages. Defaults to detected docs/* roots.")
    list_parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")
    list_parser.add_argument("--fail-on-delta", action="store_true", help="Exit 1 when any delta is found.")
    list_parser.set_defaults(func=command_list)

    update_parser = subparsers.add_parser("update", help="Refresh source hashes and target metadata in the cache.")
    add_common_args(update_parser)
    update_parser.add_argument("--target", default="", help="Comma-separated target languages. Defaults to detected docs/* roots.")
    update_parser.add_argument("--model", default=DEFAULT_MODEL)
    update_parser.add_argument("--updated-at", type=int, default=0, help="Unix timestamp override.")
    update_parser.set_defaults(func=command_update)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
