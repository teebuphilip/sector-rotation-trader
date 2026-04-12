#!/usr/bin/env python3
"""
Rebuild data/algos_registry_crazy.txt from crazy/algos/*.py
"""
from __future__ import annotations

from pathlib import Path


def class_name_from_file(path: Path) -> str:
    stem = path.stem
    words = stem.split("_")
    return "".join(w.title() for w in words) + "Algo"


def main() -> int:
    base = Path("crazy/algos")
    out = Path("data/algos_registry_crazy.txt")
    out.parent.mkdir(parents=True, exist_ok=True)

    entries = []
    for p in sorted(base.glob("*.py")):
        if p.name in {"__init__.py", "registry.py"}:
            continue
        entries.append(f"{p.stem}:{class_name_from_file(p)}")

    out.write_text("\n".join(entries) + "\n", encoding="utf-8")
    print(f"Wrote {len(entries)} entries to {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
