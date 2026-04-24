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
import csv
import json
import math
import re
from datetime import date
from pathlib import Path

LEADERBOARD = Path("docs/data/public/leaderboard.json")
DAILY = Path("docs/data/public/daily.json")
RANK_HISTORY = Path("data/rank_history.csv")
ROLLING_30D = Path("docs/leaderboards/rolling_30d.json")
OVERRIDES_DIR = Path("drafts/reddit_launch/overrides")
TEMPLATES_DIR = Path("drafts/reddit_launch")
TEMPLATES = [
    "algotrading.md",
    "investing.md",
    "stocks.md",
    "quant.md",
    "security_analysis.md",
]
STALE_PHRASES = [
    "A month of data is a starting point, not a verdict.",
    "late-cycle, risk-off positioning read",
]


def _fmt_pct(val, sign=True):
    if val is None:
        return "n/a"
    s = f"{val:+.2f}" if sign else f"{val:.2f}"
    return s.lstrip("+") if not sign else s


def _name_short(algo):
    n = algo.get("name") or algo.get("algo_id") or "Unknown"
    return n.split(" (")[0].strip() if " (" in n else n


def _pick_algo(algos, algo_id, algo_type=None):
    matches = [a for a in algos if a.get("algo_id") == algo_id]
    if algo_type:
        typed = [a for a in matches if a.get("algo_type") == algo_type]
        if typed:
            return typed[0]
    return matches[0] if matches else {}


def _load_rank_history():
    if not RANK_HISTORY.exists():
        return []
    rows = []
    with RANK_HISTORY.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    if not rows:
        return []
    latest_date = max(r.get("date", "") for r in rows)
    return [r for r in rows if r.get("date") == latest_date]


def _load_rolling_30d():
    if not ROLLING_30D.exists():
        return {}
    try:
        return json.loads(ROLLING_30D.read_text())
    except Exception:
        return {}


def _load_overrides(run_date):
    override_path = OVERRIDES_DIR / f"{run_date}.json"
    if not override_path.exists():
        return {}
    try:
        return json.loads(override_path.read_text())
    except Exception:
        return {}


def _validate_output(text, filename):
    unresolved = sorted(set(re.findall(r"\{[^}]+\}", text)))
    if unresolved:
        raise ValueError(f"{filename}: unresolved placeholders remain: {', '.join(unresolved)}")
    for phrase in STALE_PHRASES:
        if phrase in text:
            raise ValueError(f"{filename}: stale phrase still present: {phrase}")


def _build_vars(leaderboard):
    algos = leaderboard.get("algos", [])

    total = len(algos)
    beating = [a for a in algos if a.get("beat_spy")]
    losing = total - len(beating)

    sorted_algos = sorted(algos, key=lambda x: x.get("ytd_pct") or 0, reverse=True)
    top1 = sorted_algos[0] if sorted_algos else {}
    top2 = sorted_algos[1] if len(sorted_algos) > 1 else {}
    worst = sorted_algos[-1] if sorted_algos else {}

    biscotti = _pick_algo(algos, "biscotti", algo_type="normal")

    rank_rows = _load_rank_history()
    rank_by_key = {(row.get("algo_id", ""), row.get("algo_type", "")): row for row in rank_rows}
    rolling = _load_rolling_30d()
    rolling_entries = rolling.get("entries") or []
    rolling_beating_spy = 0
    spy_ret_30d = rolling.get("spy_ret_30d")
    if spy_ret_30d is not None:
        rolling_beating_spy = sum(1 for entry in rolling_entries if (entry.get("ret_30d") or 0) > spy_ret_30d)

    biscotti_force_rank = rank_by_key.get(("biscotti", "normal"), {}).get("rank_return", "?")
    biscotti_rolling_rank = next(
        (
            i + 1
            for i, entry in enumerate(rolling_entries)
            if entry.get("algo_id") == "biscotti" and entry.get("category") == "standard"
        ),
        "?",
    )
    top_rolling = rolling_entries[0] if rolling_entries else {}

    days_vals = [a.get("days_running") for a in algos if a.get("days_running")]
    days_running = max(days_vals) if days_vals else 0
    weeks_running = math.ceil(days_running / 7)

    # sector consensus: top sector from public data if available
    top_sector_name = "Technology"
    top_sector_etf = "XLK"
    top_sector_bullish_pct = "41"
    if DAILY.exists():
        try:
            pd = json.loads(DAILY.read_text())
            sectors = list((pd.get("sector_summary") or {}).values())
            sectors.sort(key=lambda item: item.get("bullish_pct", 0), reverse=True)
            if sectors:
                top_sector_name = sectors[0].get("sector", "Technology")
                top_sector_etf = sectors[0].get("etf", "XLK")
                top_sector_bullish_pct = str(sectors[0].get("bullish_pct", 41))
        except Exception:
            pass

    return {
        "{algotrading_title}": f"I've been running {total} alternative-data signals against SPY for {days_running} days. {len(beating)} are beating it. Here's the full picture.",
        "{security_macro_note}": f"{top_sector_name} ({top_sector_etf}) leads current bullish share at {top_sector_bullish_pct}%. I update the actual macro read by hand before posting so I do not overstate what the nightly data says.",
        "{total_algos}": str(total),
        "{total_algos_minus_10}": str(max(0, total - 10)),
        "{beating_spy}": str(len(beating)),
        "{losing_count}": str(losing),
        "{days_running}": str(days_running),
        "{weeks_running}": str(weeks_running),
        "{top1_name}": _name_short(top1),
        "{top1_return}": _fmt_pct(top1.get("ytd_pct"), sign=False),
        "{top1_alpha}": _fmt_pct(top1.get("alpha_pct"), sign=False),
        "{top2_name}": _name_short(top2),
        "{top2_return}": _fmt_pct(top2.get("ytd_pct"), sign=False),
        "{top2_alpha}": _fmt_pct(top2.get("alpha_pct"), sign=False),
        "{biscotti_rolling_rank}": str(biscotti_rolling_rank),
        "{biscotti_force_rank}": str(biscotti_force_rank),
        "{biscotti_30d_return}": _fmt_pct(biscotti.get("ret_30d_pct"), sign=False),
        "{worst_name}": _name_short(worst),
        "{worst_return}": _fmt_pct(worst.get("ytd_pct"), sign=False),
        "{worst_alpha}": _fmt_pct(worst.get("alpha_pct"), sign=False),
        "{rolling_30d_beating_spy}": str(rolling_beating_spy),
        "{top_rolling_name}": _name_short(top_rolling),
        "{top_rolling_return}": _fmt_pct((top_rolling.get("ret_30d") or 0) * 100, sign=False) if top_rolling else "n/a",
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
    variables.update({f"{{{k}}}": str(v) for k, v in _load_overrides(run_date).items()})

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
        _validate_output(text, filename)

        out_path = out_dir / filename
        out_path.write_text(text, encoding="utf-8")
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
