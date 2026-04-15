#!/usr/bin/env python3
"""
evening_email.py
----------------
Evening tactical summary email. Runs after daily_run.yml completes.
Covers: trades, equity, force rankings, validation results, signal status.

Usage:
  python scripts/evening_email.py
"""
from __future__ import annotations

import csv
import json
import os
import subprocess
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _load_json(path: Path):
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text())
    except Exception:
        return None


def _stale(last_run: str) -> bool:
    try:
        from datetime import timedelta
        dt = datetime.fromisoformat(last_run)
        return (datetime.utcnow().date() - dt.date()) > timedelta(days=2)
    except Exception:
        return True


def build_report() -> str:
    lines = []
    now = datetime.utcnow().strftime("%Y-%m-%d")
    run_date = os.getenv("AFH_RUN_DATE") or now

    lines.append("Evening Trading Report — {}".format(run_date))
    lines.append("=" * 50)

    # ── 1. Baseline NRWise ─────────────────────────────────────────
    lines.append("")
    lines.append("BASELINE (NRWise Acceleration):")
    base_state = _load_json(ROOT / "state.json")
    if base_state:
        snaps = base_state.get("daily_snapshots", [])
        if snaps:
            latest = snaps[-1]
            lines.append("  Equity:  ${:,.2f}".format(latest.get("equity", 0)))
            lines.append("  Sector:  {}".format(latest.get("sector", "—")))
            lines.append("  Date:    {}".format(latest.get("date", "?")))
        trades_today = [t for t in base_state.get("trade_log", [])
                        if t.get("date") == run_date]
        buys = [t for t in trades_today if t.get("action") == "BUY"]
        sells = [t for t in trades_today if t.get("action") == "SELL"]
        lines.append("  Trades today: {} BUY, {} SELL".format(len(buys), len(sells)))
        for t in trades_today:
            lines.append("    {} {} @ ${:.2f}".format(
                t.get("action"), t.get("ticker"), t.get("price", 0)))
    else:
        lines.append("  state.json missing")

    # ── 2. Algo Run Status ─────────────────────────────────────────
    lines.append("")
    lines.append("ALGO RUN STATUS:")
    for label, state_dir in [
        ("Normal", ROOT / "data" / "normal" / "state"),
        ("Crazy", ROOT / "data" / "crazy" / "state"),
    ]:
        if not state_dir.exists():
            lines.append("  {}: directory missing".format(label))
            continue

        states = sorted(state_dir.glob("*.json"))
        ok_count = 0
        stale_list = []
        for fp in states:
            state = _load_json(fp)
            if not state:
                stale_list.append(fp.stem)
                continue
            snaps = state.get("daily_snapshots", [])
            if snaps and snaps[-1].get("date") == run_date:
                ok_count += 1
            else:
                stale_list.append(fp.stem)

        lines.append("  {}: {}/{} ran today".format(label, ok_count, len(states)))
        if stale_list:
            for s in stale_list[:5]:
                lines.append("    STALE: {}".format(s))
            if len(stale_list) > 5:
                lines.append("    ...+{} more stale".format(len(stale_list) - 5))

    # ── 3. Force Rankings ──────────────────────────────────────────
    lines.append("")
    rank_csv = ROOT / "data" / "rank_history.csv"
    if rank_csv.exists():
        with rank_csv.open("r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            today_rows = [r for r in reader
                          if r.get("date") == run_date and r.get("algo_type") == "crazy"]

        if today_rows:
            by_return = sorted(today_rows,
                               key=lambda r: float(r.get("ytd_pct", 0)),
                               reverse=True)
            beating = sum(1 for r in by_return
                          if r.get("beat_spy", "").lower() == "true")

            lines.append("CRAZY FORCE RANKINGS ({} algos):".format(len(by_return)))
            lines.append("  Beating SPY: {}/{}".format(beating, len(by_return)))
            lines.append("")
            lines.append("  Top 10 by Return:")
            for i, r in enumerate(by_return[:10], 1):
                name = r.get("name", r.get("algo_id", "?"))
                ytd = float(r.get("ytd_pct", 0))
                alpha = float(r.get("alpha_pct", 0))
                flag = "BEAT" if r.get("beat_spy", "").lower() == "true" else "LAG"
                lines.append("    {:2d}. {:40s}  {:+7.2f}%  alpha:{:+6.2f}%  [{}]".format(
                    i, name, ytd, alpha, flag))

            lines.append("")
            lines.append("  Top 5 by Alpha vs SPY:")
            by_alpha = sorted(today_rows,
                              key=lambda r: float(r.get("alpha_pct", 0)),
                              reverse=True)
            for i, r in enumerate(by_alpha[:5], 1):
                name = r.get("name", r.get("algo_id", "?"))
                ytd = float(r.get("ytd_pct", 0))
                alpha = float(r.get("alpha_pct", 0))
                lines.append("    {:2d}. {:40s}  {:+7.2f}%  alpha:{:+6.2f}%".format(
                    i, name, ytd, alpha))

            lines.append("")
            lines.append("  Bottom 5:")
            for r in by_return[-5:]:
                name = r.get("name", r.get("algo_id", "?"))
                ytd = float(r.get("ytd_pct", 0))
                alpha = float(r.get("alpha_pct", 0))
                rank = r.get("rank_return", "?")
                lines.append("    #{:>3s}  {:40s}  {:+7.2f}%  alpha:{:+6.2f}%".format(
                    rank, name, ytd, alpha))
        else:
            lines.append("FORCE RANKINGS: no rows for today")
    else:
        lines.append("FORCE RANKINGS: rank_history.csv missing")

    # ── 4. Precompute Signals Status ───────────────────────────────
    lines.append("")
    signals_dir = ROOT / "docs" / "signals"
    index_path = signals_dir / "index.json"
    if index_path.exists():
        idx = _load_json(index_path)
        if idx:
            gen = idx.get("generated", "?")
            ticker_count = idx.get("ticker_count", "?")
            signal_count = idx.get("signal_count", "?")
            top_bull = ", ".join(idx.get("top_bullish_etfs", []))
            top_bear = ", ".join(idx.get("top_bearish_etfs", []))
            lines.append("PRECOMPUTE SIGNALS:")
            lines.append("  Generated:    {}".format(gen))
            lines.append("  Signals:      {}".format(signal_count))
            lines.append("  Tickers:      {}".format(ticker_count))
            lines.append("  Top Bullish:  {}".format(top_bull or "none"))
            lines.append("  Top Bearish:  {}".format(top_bear or "none"))
            if gen != run_date:
                lines.append("  *** STALE — generated {} but today is {} ***".format(gen, run_date))

            # Sector breakdown
            sectors = idx.get("sector_summary", {})
            if sectors:
                lines.append("  Sector Heatmap:")
                for etf, s in sectors.items():
                    lines.append("    {:5s} {:25s} {:12s} {}".format(
                        etf,
                        s.get("sector", ""),
                        s.get("composite", ""),
                        s.get("composite_label", ""),
                    ))
        else:
            lines.append("PRECOMPUTE SIGNALS: index.json unreadable")
    else:
        lines.append("PRECOMPUTE SIGNALS: not yet generated")

    # ── 5. Validation Results ──────────────────────────────────────
    lines.append("")
    lines.append("VALIDATION:")
    cache_path = ROOT / "data" / ".validation_cache" / "snapshot_counts.json"
    if cache_path.exists():
        counts = _load_json(cache_path)
        if isinstance(counts, dict):
            lines.append("  Snapshot cache: {} algos tracked".format(len(counts)))
        else:
            lines.append("  Snapshot cache: present but unreadable")
    else:
        lines.append("  Snapshot cache: not yet established")

    # Try to run surface validation inline for the email
    try:
        result = subprocess.run(
            ["python", str(ROOT / "scripts" / "validate_nightly.py")],
            capture_output=True, text=True, timeout=60, cwd=str(ROOT),
        )
        exit_code = result.returncode
        if exit_code == 0:
            lines.append("  Surface: ALL CLEAR")
        elif exit_code == 1:
            lines.append("  Surface: WARNINGS")
        else:
            lines.append("  Surface: FAILURES (exit code {})".format(exit_code))

        # Extract just the summary lines from output
        for line in result.stdout.splitlines():
            stripped = line.strip()
            if stripped.startswith("FAIL:") or stripped.startswith("WARN:"):
                lines.append("    {}".format(stripped))
            elif stripped.startswith("STATUS:"):
                lines.append("  {}".format(stripped))
    except Exception as e:
        lines.append("  Surface: could not run ({})".format(e))

    # ── 6. Rolling 30D Leaderboard ─────────────────────────────────
    lines.append("")
    lb_json = ROOT / "docs" / "leaderboards" / "rolling_30d.json"
    if lb_json.exists():
        lb = _load_json(lb_json)
        if lb:
            spy_ret = lb.get("spy_ret_30d")
            entries = lb.get("entries", [])
            lines.append("ROLLING 30D LEADERBOARD:")
            if spy_ret is not None:
                lines.append("  SPY 30D: {:+.2%}".format(spy_ret))
            lines.append("  Algos:   {}".format(len(entries)))
            for i, e in enumerate(entries[:5], 1):
                r = e.get("ret_30d")
                ret_str = "{:+.2%}".format(r) if r is not None else "n/a"
                lines.append("    {:2d}. {:40s}  {}".format(
                    i, e.get("name", "?"), ret_str))
        else:
            lines.append("ROLLING 30D LEADERBOARD: unreadable")
    else:
        lines.append("ROLLING 30D LEADERBOARD: not yet generated")

    # ── 7. Blocked Algos (missing API keys) ───────────────────────
    lines.append("")
    blocked_file = ROOT / "data" / "blocked" / "algos.jsonl"
    if blocked_file.exists():
        from collections import Counter
        seen_algos = {}
        for line in blocked_file.read_text().splitlines():
            s = line.strip()
            if not s:
                continue
            try:
                obj = json.loads(s)
            except Exception:
                continue
            aid = obj.get("algo_id", "")
            seen_algos[aid] = obj

        unique_blocked = list(seen_algos.values())
        if unique_blocked:
            # Collect all unique missing keys
            all_keys = set()
            for entry in unique_blocked:
                for k in entry.get("keys", []):
                    all_keys.add(k)

            lines.append("BLOCKED ALGOS ({} unique, {} missing keys):".format(
                len(unique_blocked), len(all_keys)))

            # List missing keys
            lines.append("  Missing keys: {}".format(", ".join(sorted(all_keys))))

            # Group by key
            by_key = {}
            for entry in unique_blocked:
                for k in entry.get("keys", ["unknown"]):
                    by_key.setdefault(k, []).append(
                        entry.get("name", entry.get("algo_id", "?")))
            for key in sorted(by_key.keys()):
                algos = by_key[key]
                lines.append("  {} ({}):".format(key, len(algos)))
                for name in sorted(algos):
                    lines.append("    - {}".format(name))
        else:
            lines.append("BLOCKED ALGOS: none")
    else:
        lines.append("BLOCKED ALGOS: none")

    return "\n".join(lines)


def main():
    print(build_report())


if __name__ == "__main__":
    main()
