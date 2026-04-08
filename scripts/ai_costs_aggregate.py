#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path


def _read_costs(path: Path) -> list[dict]:
    if not path.exists():
        return []
    rows = []
    with path.open("r", encoding="utf-8", errors="replace") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows


def main() -> int:
    logs_dir = Path("logs")
    out_path = logs_dir / "ai_costs_aggregated.csv"

    sources = [
        logs_dir / "ai_costs_chatgpt_ideas.csv",
        logs_dir / "ai_costs_claude_ideas.csv",
        logs_dir / "ai_costs_chatgpt_normal.csv",
        logs_dir / "ai_costs_claude_normal.csv",
    ]

    rows = []
    for src in sources:
        rows.extend(_read_costs(src))

    if not rows:
        return 0

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", newline="") as f:
        fieldnames = ["date", "time", "provider", "model", "input_tokens", "output_tokens", "cost_usd"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
