#!/usr/bin/env python3
"""
refresh_reddit_drafts.py

Reads live leaderboard data and fills in {variable} placeholders in the
Reddit launch post templates. Writes dated copies to drafts/reddit_launch/YYYY-MM-DD/.

Run any time to get current-number versions of all 5 posts.

Usage:
    python scripts/refresh_reddit_drafts.py
    python scripts/refresh_reddit_drafts.py --date 2026-05-15
"""

from __future__ import annotations

import argparse
import json
import math
from datetime import date
from pathlib import Path

LEADERBOARD = Path("docs/data/public/leaderboard.json")
TEMPLATES_DIR = Path("drafts/reddit_launch")
TEMPLATES = [
    "algotrading.md",
    "investing.md",
    "stocks.md",
    "quant.md",
    "security_analysis.md",
]


def _fmt_pct(val, sign=True):
    if val is None:
        return "n/a"
    s = f"{val:+.2f}" if sign else f"{val:.2f}"
    return s.lstrip("+") if not sign else s


def _build_vars(leaderboard):
    algos = leaderboard.get("algos", [])

    total = len(algos)
    beating = [a for a in algos if a.get("beat_spy")]
    losing = total - len(beating)

    sorted_algos = sorted(algos, key=lambda x: x.get("ytd_pct") or 0, reverse=True)
    top1 = sorted_algos[0] if sorted_algos else {}
    top2 = sorted_algos[1] if len(sorted_algos) > 1 else {}
    worst = sorted_algos[-1] if sorted_algos else {}

    biscotti = next((a for a in algos if a.get("algo_id") == "biscotti"), {})

    # rolling 30D rank for biscotti: approximate from sorted ret_30d_pct
    sorted_30d = sorted(algos, key=lambda x: x.get("ret_30d_pct") or 0, reverse=True)
    biscotti_rolling_rank = next(
        (i + 1 for i, a in enumerate(sorted_30d) if a.get("algo_id") == "biscotti"), "?"
    )

    # force rank: approximate from sorted ytd_pct (proxy for force rank position)
    biscotti_force_rank = next(
        (i + 1 for i, a in enumerate(sorted_algos) if a.get("algo_id") == "biscotti"), "?"
    )

    # days running: use mode of days_running across main algos
    days_vals = [a.get("days_running") for a in algos if a.get("days_running")]
    days_running = max(days_vals) if days_vals else 0
    weeks_running = math.ceil(days_running / 7)

    # sector consensus: top sector from public data if available
    public_sectors = Path("docs/data/public/daily.json")
    top_sector_name = "Technology"
    top_sector_etf = "XLK"
    top_sector_bullish_pct = "41"
    if public_sectors.exists():
        try:
            pd = json.loads(public_sectors.read_text())
            sectors = pd.get("sector_consensus", {}).get("sectors_ranked") or []
            if sectors:
                top_sector_name = sectors[0].get("sector", "Technology")
                top_sector_etf = sectors[0].get("etf", "XLK")
                top_sector_bullish_pct = str(sectors[0].get("bullish_pct", 41))
        except Exception:
            pass

    def name_short(algo):
        n = algo.get("name") or algo.get("algo_id") or "Unknown"
        # strip the parenthetical nickname to keep it clean
        return n.split(" (")[0].strip() if " (" in n else n

    return {
        "{total_algos}": str(total),
        "{total_algos_minus_10}": str(max(0, total - 10)),
        "{beating_spy}": str(len(beating)),
        "{losing_count}": str(losing),
        "{days_running}": str(days_running),
        "{weeks_running}": str(weeks_running),
        "{top1_name}": name_short(top1),
        "{top1_return}": _fmt_pct(top1.get("ytd_pct"), sign=False),
        "{top1_alpha}": _fmt_pct(top1.get("alpha_pct"), sign=False),
        "{top2_name}": name_short(top2),
        "{top2_return}": _fmt_pct(top2.get("ytd_pct"), sign=False),
        "{top2_alpha}": _fmt_pct(top2.get("alpha_pct"), sign=False),
        "{biscotti_rolling_rank}": str(biscotti_rolling_rank),
        "{biscotti_force_rank}": str(biscotti_force_rank),
        "{biscotti_30d_return}": _fmt_pct(biscotti.get("ret_30d_pct"), sign=False),
        "{worst_name}": name_short(worst),
        "{worst_return}": _fmt_pct(worst.get("ytd_pct"), sign=False),
        "{worst_alpha}": _fmt_pct(worst.get("alpha_pct"), sign=False),
        "{top_sector_name}": top_sector_name,
        "{top_sector_etf}": top_sector_etf,
        "{top_sector_bullish_pct}": top_sector_bullish_pct,
    }


def refresh(run_date):
    if not LEADERBOARD.exists():
        print(f"ERROR: {LEADERBOARD} not found")
        return

    leaderboard = json.loads(LEADERBOARD.read_text())
    variables = _build_vars(leaderboard)

    out_dir = TEMPLATES_DIR / run_date
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Variables as of {run_date}:")
    for k, v in variables.items():
        print(f"  {k} = {v}")
    print()

    for filename in TEMPLATES:
        template_path = TEMPLATES_DIR / filename
        if not template_path.exists():
            print(f"  [skip] template not found: {template_path}")
            continue

        text = template_path.read_text()

        # strip the template header comment lines before writing output
        lines = text.splitlines()
        content_lines = [l for l in lines if not l.startswith("# Run:") and not l.startswith("# Output")]
        text = "\n".join(content_lines)

        for placeholder, value in variables.items():
            text = text.replace(placeholder, value)

        out_path = out_dir / filename
        out_path.write_text(text)
        print(f"  wrote {out_path}")

    print(f"\nDone. Edit drafts in {out_dir} before posting.")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=None, help="YYYY-MM-DD (default: today)")
    args = parser.parse_args()

    run_date = args.date or date.today().isoformat()
    refresh(run_date)


if __name__ == "__main__":
    main()
