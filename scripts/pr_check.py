#!/usr/bin/env python3
"""Check added documentation prose: spelling/images fail; grammar is report-only.

Structure checks run separately with scripts/precommit.py --base origin/master.
Only committed HEAD content is read. No files are changed by these checks.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from bisect import bisect_right
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import anchors
import i18n_check

REPO_ROOT = anchors.REPO_ROOT
PAGE_RE = re.compile(r"^docs/(?P<lang>[a-z]{2})/docs/.+\.md$")
HUNK_RE = re.compile(r"^@@ -\S+ \+(\d+)(?:,(\d+))? @@")
CODESPELL_RE = re.compile(r"^(?P<line>\d+): (?P<word>.+?) ==> (?P<fix>.+)$")
CODESPELL_IGNORE = Path(__file__).resolve().parent / "codespell_ignore.txt"
IMAGE_ALT_RE = re.compile(r"!\[([^\]\s]*\d[^\]\s]*)\]\(\s*<?([^)\s>]+)")
OFFICIAL_LINK_RE = re.compile(r"\[Official Website\]\((https?://[^)\s]+)\)", re.I)
GRAMMAR_SUBS = (
    (re.compile(r"\{[#.:][^}\n]*\}|\{\s*\w+=[^}\n]*\}"), ""),
    (re.compile(r"!\[[^\]]*\]\([^)]*\)"), ""),
    (re.compile(r"\[([^\]]*)\]\([^)]*\)"), r"\1"),
    (re.compile(r"`[^`\n]+`"), "X"),
    (re.compile(r"<[^>]+>"), " "),
    (re.compile(r"https?://\S+"), "example.com"),
    (re.compile(r"\*\*|__|(?<![\w*])\*(?=\S)|(?<=\S)\*(?![\w*])"), ""),
    (re.compile(r"^[ \t]*(?:#{1,6}[ \t]+|(?:!!!|\?\?\?\+?|===\+?)[ \t]*\w*[ \t]*|[-*+][ \t]+|\d+\.[ \t]+)"), ""),
    (re.compile(r"^[ \t]*>[ \t]?"), ""),
)
GRAMMAR_DISABLED_RULES = (
    "MORFOLOGIK_RULE_EN_US", "UPPERCASE_SENTENCE_START", "PUNCTUATION_PARAGRAPH_END",
    "WHITESPACE_RULE", "COMMA_PARENTHESIS_WHITESPACE", "EN_UNPAIRED_BRACKETS",
    "EN_UNPAIRED_QUOTES", "DASH_RULE", "ARROWS", "COMMA_COMPOUND_SENTENCE",
)
GRAMMAR_DISABLED_CATEGORIES = ("TYPOGRAPHY", "CASING", "STYLE", "REDUNDANCY", "PLAIN_ENGLISH")
GRAMMAR_CHUNK = 15000


@dataclass
class Finding:
    level: str
    check: str
    path: str
    line: int
    message: str


def git(*args: str) -> str:
    return subprocess.run(["git", *args], check=True, capture_output=True,
                          text=True, encoding="utf-8", cwd=REPO_ROOT).stdout


def changed_paths(base: str, prefix: str = "docs/") -> list[tuple[str, str]]:
    """NUL records preserve Unicode, tabs, spaces and quoted filenames."""
    fields = git("diff", f"{base}...HEAD", "--name-status", "-z", "--find-renames",
                 "--diff-filter=AMR", "--", prefix).split("\0")
    result = []
    index = 0
    while index < len(fields) and fields[index]:
        status, old = fields[index:index + 2]
        index += 2
        new = old
        if status.startswith("R"):
            new = fields[index]
            index += 1
        result.append((old, new))
    return result


def added_lines(base: str) -> dict[str, set[int]]:
    result = {}
    merge_base = git("merge-base", base, "HEAD").strip()
    for old, path in changed_paths(base):
        if not PAGE_RE.match(path):
            continue
        # A rename may coexist with a new file at its old path. Compare the
        # two blobs directly so the recreated file's hunks cannot leak in.
        revisions = ([f"{merge_base}:{old}", f"HEAD:{path}"] if old != path
                     else [f"{base}...HEAD", "--", path])
        diff = git("diff", "--unified=0", "--no-color", "--no-ext-diff",
                   "--no-textconv", *revisions)
        numbers = set()
        for line in diff.splitlines():
            if hunk := HUNK_RE.match(line):
                start, count = int(hunk[1]), int(hunk[2] or 1)
                numbers.update(range(start, start + count))
        if numbers:
            result[path] = numbers
    return result


def page_lines(path: str) -> list[str]:
    return git("show", f"HEAD:{path}").splitlines()


def prose_lines(lines: list[str]):
    """Skip front matter, fences (including nested admonitions), and table rules."""
    fence = None
    for index in range(anchors.front_matter_end(lines), len(lines)):
        raw = lines[index]
        match = anchors.FENCE_RE.match(raw)
        if fence is not None:
            if (match and match[1][0] == fence[0] and len(match[1]) >= len(fence)
                    and not raw[match.end():].strip()):
                fence = None
            continue
        if match:
            fence = match[1]
            continue
        if not raw.strip() or i18n_check.TABLE_RULE_RE.match(raw):
            continue
        yield index + 1, raw


def spelling_text(raw: str) -> str:
    """Mask literal code and Markdown/HTML attributes, retaining prose and lines."""
    text = re.sub(r"(`+)(?!`)(.*?)\1(?!`)", " ", raw)
    text = re.sub(r"\{[#.:][^}\n]*\}|\{\s*\w+=[^}\n]*\}", " ", text)
    return re.sub(r"<[^>]+>", " ", text)


def check_spelling(pages: dict[str, set[int]]) -> list[Finding]:
    findings = []
    for path, numbers in pages.items():
        if not path.startswith("docs/en/"):
            continue
        # Preserve original line numbers, but do not spellcheck code or metadata.
        lines = page_lines(path)
        allowed = dict(prose_lines(lines))
        text = "\n".join(spelling_text(raw) if number in numbers and number in allowed else ""
                         for number, raw in enumerate(lines, 1))
        command = [sys.executable, "-m", "codespell_lib", "--stdin-single-line", "--disable-colors",
                   "--uri-ignore-words-list", "*",
                   "--ignore-words", str(CODESPELL_IGNORE), "-"]
        try:
            output = subprocess.run(command, input=text, capture_output=True, text=True,
                                    encoding="utf-8", cwd=REPO_ROOT)
        except OSError as error:
            findings.append(Finding("error", "spelling", path, 1, f"codespell did not run: {error}"))
            continue
        if output.returncode not in (0, 65):
            print(output.stderr, file=sys.stderr)
            findings.append(Finding("error", "spelling", path, 1, "codespell did not run; see the log"))
            continue
        for line in output.stdout.splitlines():
            if match := CODESPELL_RE.match(line):
                number = int(match["line"])
                if number in numbers and number in allowed:
                    findings.append(Finding("error", "spelling", path, number,
                        f'"{match["word"]}" may be a typo; did you mean: {match["fix"]}? '
                        'If correct, add it to scripts/codespell_ignore.txt.'))
    return findings


def url_status(url: str) -> int | str:
    for method in ("HEAD", "GET"):
        request = urllib.request.Request(url, method=method, headers={"User-Agent": "documentation-pr-check"})
        try:
            with urllib.request.urlopen(request, timeout=20) as response:
                return response.status
        except urllib.error.HTTPError as error:
            if method == "HEAD" and error.code in (403, 404, 405, 410):
                continue
            return error.code
        except (urllib.error.URLError, TimeoutError, OSError) as error:
            return str(getattr(error, "reason", error))
    return "no response"


def check_images(pages: dict[str, set[int]]) -> list[Finding]:
    uses = []
    for path, numbers in pages.items():
        for number, raw in prose_lines(page_lines(path)):
            if number in numbers:
                for regex in i18n_check.IMAGE_RES:
                    uses.extend((path, number, url) for url in regex.findall(raw)
                                if url.startswith(("http://", "https://")))
    urls = sorted({url for _, _, url in uses})
    with ThreadPoolExecutor(max_workers=16) as pool:
        statuses = dict(zip(urls, pool.map(url_status, urls)))
    findings = []
    for path, number, url in uses:
        status = statuses[url]
        if status in (404, 410):
            findings.append(Finding("error", "images", path, number, f"image not found (HTTP {status}): {url}"))
        elif status != 200:
            findings.append(Finding("warning", "images", path, number, f"image could not be checked ({status}): {url}"))
    return findings


def grammar_text(raw: str) -> str:
    text = raw
    for regex, replacement in GRAMMAR_SUBS:
        text = regex.sub(replacement, text)
    if raw.lstrip().startswith("|"):
        text = "\n\n".join(cell.strip() for cell in text.strip().strip("|").split("|"))
    return re.sub(r"[ \t]+", " ", text).strip()


def languagetool(url: str, text: str) -> list[dict]:
    data = urllib.parse.urlencode({"text": text, "language": "en-US",
        "disabledRules": ",".join(GRAMMAR_DISABLED_RULES),
        "disabledCategories": ",".join(GRAMMAR_DISABLED_CATEGORIES)}).encode()
    request = urllib.request.Request(f"{url.rstrip('/')}/v2/check", data=data,
                                    headers={"User-Agent": "documentation-pr-check"})
    with urllib.request.urlopen(request, timeout=120) as response:
        return json.load(response)["matches"]


def check_grammar(pages: dict[str, set[int]], url: str) -> list[Finding]:
    findings = []
    for path, numbers in pages.items():
        if not path.startswith("docs/en/"):
            continue
        chunks = []
        text, starts, line_numbers = "", [], []
        for number, raw in prose_lines(page_lines(path)):
            if number not in numbers or not (prose := grammar_text(raw)):
                continue
            if text and len(text) + len(prose) > GRAMMAR_CHUNK:
                chunks.append((text, starts, line_numbers))
                text, starts, line_numbers = "", [], []
            starts.append(len(text))
            line_numbers.append(number)
            text += prose + "\n\n"
        if text:
            chunks.append((text, starts, line_numbers))
        for text, starts, line_numbers in chunks:
            try:
                matches = languagetool(url, text)
            except (urllib.error.URLError, TimeoutError, OSError, ValueError) as error:
                findings.append(Finding("warning", "grammar", path, line_numbers[0], f"grammar check failed: {error}"))
                continue
            for match in matches:
                position = bisect_right(starts, match["offset"]) - 1
                suggestions = ", ".join(r["value"] for r in match.get("replacements", [])[:3])
                findings.append(Finding("warning", "grammar", path, line_numbers[position],
                    f'{match["message"]} -> {suggestions} [{match["rule"]["id"]}]'))
    return findings


def check_alt_text(pages: dict[str, set[int]]) -> list[Finding]:
    def letters(name):
        return re.sub(r"[\d_.-]", "", name.lower())
    findings = []
    for path, numbers in pages.items():
        for number, raw in prose_lines(page_lines(path)):
            if number not in numbers:
                continue
            for alt, url in IMAGE_ALT_RE.findall(raw):
                stem = url.rsplit("/", 1)[-1].rsplit(".", 1)[0]
                if (re.sub(r"[_.-]", "", alt.lower()) != re.sub(r"[_.-]", "", stem.lower())
                        and letters(alt) == letters(stem)):
                    findings.append(Finding("warning", "alt-text", path, number,
                                            f'alt text "{alt}" does not match the image file "{stem}"'))
    return findings


def check_copied_links(pages: dict[str, set[int]]) -> list[Finding]:
    findings = []
    for path, numbers in pages.items():
        if not path.startswith("docs/en/"):
            continue
        lines = page_lines(path)
        starts = [h.index + 1 for h in anchors.parse_headings([f"{text}\n" for text in lines])]
        uses = {}
        for number, raw in prose_lines(lines):
            for url in OFFICIAL_LINK_RE.findall(raw):
                section = starts[bisect_right(starts, number) - 1] if starts and starts[0] <= number else 0
                uses.setdefault(url, []).append((section, number))
        for url, places in uses.items():
            if len({section for section, _ in places}) > 1:
                for _, number in places:
                    if number in numbers:
                        findings.append(Finding("warning", "copied-link", path, number,
                            f"this Official Website link is used under another heading; check this section: {url}"))
    return findings


def explicit_ids(lines: list[str]) -> set[str]:
    return {h.explicit_id for h in anchors.parse_headings(lines) if h.explicit_id}


def check_heading_ids(base: str) -> list[Finding]:
    merge_base = git("merge-base", base, "HEAD").strip()
    findings = []
    for old, new in changed_paths(base, "docs/en/docs/"):
        if not PAGE_RE.match(new):
            continue
        # Added pages have no prior IDs.
        try:
            before = explicit_ids(git("show", f"{merge_base}:{old}").splitlines(keepends=True))
        except subprocess.CalledProcessError:
            continue
        removed = sorted(before - explicit_ids([f"{text}\n" for text in page_lines(new)]))
        if removed:
            findings.append(Finding("warning", "heading-id", new, 1,
                f"heading IDs removed: {', '.join(removed)}. Update matching localized IDs "
                "and in-repository anchor links and redirects."))
    return findings


def escape(value: str, property_value: bool = False) -> str:
    value = value.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
    return value.replace(":", "%3A").replace(",", "%2C") if property_value else value


def report(findings: list[Finding]) -> None:
    for f in findings:
        if os.environ.get("GITHUB_ACTIONS") == "true":
            print(f"::{f.level} file={escape(f.path, True)},line={f.line},title={escape(f.check, True)}::{escape(f.message)}")
        else:
            print(f"{f.level.upper()} [{f.check}] {f.path}:{f.line}: {f.message}")
    if summary := os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(summary, "a", encoding="utf-8") as out:
            out.write("## Documentation content checks\n\n")
            if not findings:
                out.write("No problems found on the changed lines.\n")
            else:
                out.write("| Level | Check | Location | Message |\n|---|---|---|---|\n")
                for f in findings:
                    message = f.message.replace("|", "\\|").replace("\n", " ")
                    out.write(f"| {f.level} | {f.check} | `{f.path}:{f.line}` | {message} |\n")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", required=True)
    parser.add_argument("--languagetool", metavar="URL")
    args = parser.parse_args(argv)
    pages = added_lines(args.base)
    findings = check_spelling(pages) + check_images(pages)
    if args.languagetool:
        findings += check_grammar(pages, args.languagetool)
    else:
        print("grammar: skipped, no --languagetool server given")
    findings += check_heading_ids(args.base) + check_alt_text(pages) + check_copied_links(pages)
    findings.sort(key=lambda f: (f.path, f.line, f.check))
    report(findings)
    errors = sum(f.level == "error" for f in findings)
    print(f"{len(pages)} changed page(s): {errors} error(s), {len(findings) - errors} warning(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
