#!/usr/bin/env python3
"""
Fail if public static pages still expose raw "Loading..." placeholders.

Interactive pages may still use a hidden loading state in JavaScript. This check
targets visible static placeholders that make the public site look abandoned when
data fetches fail.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
IGNORED = {
    ROOT / "docs" / "signals" / "lookup.html",
}
VISIBLE_LOADING_RE = re.compile(r">\s*Loading(?:\.\.\.)?[^<]*<", re.IGNORECASE)


def main() -> int:
    failures = []
    for path in sorted((ROOT / "docs").rglob("*.html")):
        if path in IGNORED:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for match in VISIBLE_LOADING_RE.finditer(text):
            snippet = " ".join(match.group(0).strip("<>").split())
            failures.append(f"{path.relative_to(ROOT)} -> {snippet}")

    if failures:
        print("Visible loading placeholders found:")
        for item in failures:
            print(f"- {item}")
        return 1

    print("No visible public Loading placeholders found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
