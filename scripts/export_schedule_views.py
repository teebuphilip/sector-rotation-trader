#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLAN_PATH = ROOT / "stockarithm_execution_plan.csv"
OUT_DIR = ROOT / "reports" / "morning_status"
MASTER_SCHEDULE_PATH = OUT_DIR / "master_schedule.csv"
CONTENT_SCHEDULE_PATH = OUT_DIR / "content_schedule.csv"

CONTENT_TAGS = {
    "marketing",
    "content",
    "reddit",
    "email",
    "mailerlite",
    "launch",
    "copy",
    "voice",
    "branding",
    "social",
}

CONTENT_KEYWORDS = (
    "reddit",
    "email",
    "mailerlite",
    "landing",
    "hero",
    "launch",
    "content",
    "copy",
    "biscotti",
    "waitlist",
    "domain",
)


def _is_content_row(row: list[str]) -> bool:
    joined = " ".join(row[:2]).lower()
    tags = set()
    if len(row) > 6:
        tags = {tag.strip().lower() for tag in row[6].split(",") if tag.strip()}
    if tags & CONTENT_TAGS:
        return True
    return any(keyword in joined for keyword in CONTENT_KEYWORDS)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    with PLAN_PATH.open(newline="") as handle:
        rows = [row for row in csv.reader(handle) if row]

    with MASTER_SCHEDULE_PATH.open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerows(rows)

    content_rows = [row for row in rows if _is_content_row(row)]
    with CONTENT_SCHEDULE_PATH.open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerows(content_rows)

    print(f"Wrote {MASTER_SCHEDULE_PATH}")
    print(f"Wrote {CONTENT_SCHEDULE_PATH} ({len(content_rows)} rows)")


if __name__ == "__main__":
    main()
