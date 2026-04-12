#!/usr/bin/env python3
"""
Deterministic algo spec completeness check.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List


REQUIRED = [
    "id",
    "name",
    "frequency",
    "universe",
    "data_sources",
    "signal_logic",
    "entry_exit",
    "position_sizing",
]


def _read_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _missing_fields(spec: Dict[str, Any]) -> List[str]:
    missing = []
    for key in REQUIRED:
        if key not in spec or spec[key] in (None, "", [], {}):
            missing.append(key)
    if "entry_exit" in spec:
        if "entry" not in spec["entry_exit"]:
            missing.append("entry_exit.entry")
        if "exit" not in spec["entry_exit"]:
            missing.append("entry_exit.exit")
    if "signal_logic" in spec and "trigger" not in spec["signal_logic"]:
        missing.append("signal_logic.trigger")
    return missing


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--spec", required=True)
    args = parser.parse_args()

    spec_path = Path(args.spec)
    if not spec_path.exists():
        raise SystemExit(f"Spec not found: {spec_path}")

    spec = _read_json(spec_path)
    missing = _missing_fields(spec)
    if missing:
        print("FAIL")
        print(json.dumps({"missing": missing}, indent=2))
        return 2
    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
