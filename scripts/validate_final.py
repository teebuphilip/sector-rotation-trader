#!/usr/bin/env python3
"""
Deterministic final validation to ensure output is safe to seed.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


FORBIDDEN = [
    "requests.get(",
    "requests.post(",
    "safe_download(",
    "register_algo",
]


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _has_marker(text: str, marker: str) -> bool:
    return marker in text


def _extract_between(text: str, start: str, end: str) -> str:
    if start not in text or end not in text:
        return ""
    return text.split(start, 1)[1].split(end, 1)[0]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    parser.add_argument("--spec", required=True)
    args = parser.parse_args()

    path = Path(args.file)
    spec = _read_json(Path(args.spec))
    text = _read(path)
    errors = []

    try:
        compile(text, str(path), "exec")
    except SyntaxError as exc:
        errors.append(f"syntax_error:{exc.msg} at line {exc.lineno}")

    for item in FORBIDDEN:
        if item in text:
            errors.append(f"forbidden:{item}")

    # Exact markers present and on their own lines
    markers = [
        "# === SIGNAL_LOGIC_START ===",
        "# === SIGNAL_LOGIC_END ===",
        "# === ALLOCATION_LOGIC_START ===",
        "# === ALLOCATION_LOGIC_END ===",
    ]
    for m in markers:
        if not _has_marker(text, m):
            errors.append(f"missing_marker:{m}")
        if f"{m}:" in text:
            errors.append(f"malformed_marker:{m}")

    # Adapter import
    adapters = spec.get("adapters") or []
    if adapters:
        adapter = adapters[0]
        adapter_import = f"from crazy.adapters.{adapter} import "
        if adapter_import not in text:
            errors.append("missing_adapter_import")

    # Signal/alloc structure
    if "def compute_signal" not in text:
        errors.append("missing_compute_signal")
    if "def target_allocations" not in text:
        errors.append("missing_target_allocations")

    signal_block = _extract_between(text, "# === SIGNAL_LOGIC_START ===", "# === SIGNAL_LOGIC_END ===")
    alloc_block = _extract_between(text, "# === ALLOCATION_LOGIC_START ===", "# === ALLOCATION_LOGIC_END ===")

    # No markdown fences
    if "```" in signal_block or "```" in alloc_block:
        errors.append("markdown_fences_present")

    # Allocation must return {} for HOLD path
    if "HOLD" in text and "return {}" not in alloc_block:
        errors.append("hold_returns_none")

    # Exit logic mention if spec says exit
    sliced_spec = spec.get("sliced_spec") or {}
    exit_spec = (sliced_spec.get("entry_exit") or {}).get("exit", "")
    if exit_spec:
        if "RISK_OFF" not in signal_block:
            errors.append("missing_risk_off_exit")

    # Allocation sizing hints: check for 0.05 and 0.20
    if "0.05" not in alloc_block and "5%" not in alloc_block:
        errors.append("missing_allocation_per_signal_5pct")
    if "0.20" not in alloc_block and "20%" not in alloc_block:
        errors.append("missing_max_total_exposure_20pct")

    if errors:
        print("FAIL")
        for e in errors:
            print(f"- {e}")
        return 2

    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
