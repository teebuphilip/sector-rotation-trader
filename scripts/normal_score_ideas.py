#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path

REQUIRED_KEYS = [
    "idea_id",
    "title",
    "thesis",
    "data_sources",
    "signal_logic",
    "entry_exit",
    "position_sizing",
    "universe",
    "frequency",
    "risks",
    "implementation_notes",
    "required_keys",
]


def _today_iso() -> str:
    return dt.date.today().isoformat()


def _load_jsonl(path: Path) -> list[dict]:
    items = []
    if not path.exists():
        return items
    for line in path.read_text().splitlines():
        s = line.strip()
        if not s:
            continue
        items.append(json.loads(s))
    return items


def _score(idea: dict) -> int:
    present = 0
    for k in REQUIRED_KEYS:
        v = idea.get(k)
        if isinstance(v, list):
            if len(v) > 0 or k == "required_keys":
                present += 1
        elif isinstance(v, str):
            if v.strip():
                present += 1
        elif v is not None:
            present += 1
    base = int(present / len(REQUIRED_KEYS) * 100)
    if not isinstance(idea.get("required_keys"), list):
        base = max(0, base - 10)
    return base


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=_today_iso())
    args = parser.parse_args()

    run_dir = Path("data") / "normal_ideas" / "runs" / args.date
    raw_dir = run_dir / "raw"

    results = []
    for src in ["chatgpt", "claude"]:
        path = raw_dir / f"{src}_{args.date}.jsonl"
        ideas = _load_jsonl(path)
        for idea in ideas:
            results.append({
                "source": src,
                "idea_id": idea.get("idea_id"),
                "title": idea.get("title"),
                "score": _score(idea),
            })

    out_path = run_dir / "score.json"
    out_path.write_text(json.dumps(results, indent=2))
    print(f"✅ Wrote {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
