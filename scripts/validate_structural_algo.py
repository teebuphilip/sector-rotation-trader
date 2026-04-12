#!/usr/bin/env python3
"""
Validate structural correctness of an algo file.
"""
from __future__ import annotations

import argparse
from pathlib import Path


FORBIDDEN = [
    "requests.get(",
    "requests.post(",
    "safe_download(",
    "register_algo",
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    parser.add_argument("--adapter", required=True, help="Adapter name (e.g. reddit_activity)")
    args = parser.parse_args()

    path = Path(args.file)
    if not path.exists():
        raise SystemExit(f"File not found: {path}")

    text = path.read_text(encoding="utf-8")
    errors = []

    for item in FORBIDDEN:
        if item in text:
            errors.append(f"forbidden: {item}")

    adapter_import = f"from crazy.adapters.{args.adapter} import "
    if adapter_import not in text:
        errors.append("missing adapter import")

    if "def compute_signal" not in text or "def target_allocations" not in text:
        errors.append("missing required methods")

    if errors:
        print("FAIL")
        for e in errors:
            print(f"- {e}")
        return 2

    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
