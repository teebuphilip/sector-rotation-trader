#!/usr/bin/env python3
"""
quality_check.py
----------------
Manual quality check report. Inspects all algo state files, compares to SPY,
flags anything weird. Writes markdown to docs/quality_checks/.

Usage:
  python scripts/quality_check.py              # prints to stdout + writes markdown
  python scripts/quality_check.py --stdout     # prints only, no file written
"""
from __future__ import annotations

import argparse
import json
import os
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _load_json(path):
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text())
    except Exception:
        return None


def _get_spy_ytd():
    try:
        import yfinance as yf
        spy = yf.download("SPY", start="2026-01-01", progress=False)
        if spy.empty:
            return None, None, None, None
        first = float(spy["Close"].iloc[0].iloc[0]) if hasattr(spy["Close"].iloc[0], 'iloc') else float(spy["Close"].iloc[0])
        last = float(spy["Close"].iloc[-1].iloc[0]) if hasattr(spy["Close"].iloc[-1], 'iloc') else float(spy["Close"].iloc[-1])
        high = float(spy["Close"].max().iloc[0]) if hasattr(spy["Close"].max(), 'iloc') else float(spy["Close"].max())
        low = float(spy["Close"].min().iloc[0]) if hasattr(spy["Close"].min(), 'iloc') else float(spy["Close"].min())
        ytd_pct = ((last / first) - 1) * 100
        return ytd_pct, last, high, low
    except Exception as e:
        return None, None, None, None


def _algo_summary(state_path, algo_type):
    s = _load_json(state_path)
    if s is None:
        return None
    snaps = s.get("daily_snapshots", [])
    trades = s.get("trade_log", [])
    positions = s.get("positions", {})
    last_snap = snaps[-1] if snaps else {}
    equity = last_snap.get("equity", 0)
    last_date = last_snap.get("date", "?")
    signal = last_snap.get("signal", "HOLD")
    ytd_pct = ((equity / 100000) - 1) * 100

    return {
        "algo_id": state_path.stem,
        "type": algo_type,
        "equity": equity,
        "ytd_pct": ytd_pct,
        "last_date": last_date,
        "signal": signal,
        "num_trades": len(trades),
        "num_snapshots": len(snaps),
        "num_positions": len(positions) if isinstance(positions, dict) else 0,
        "sector": last_snap.get("sector", ""),
    }


def build_report():
    lines = []
    warnings = []
    today = datetime.utcnow().strftime("%Y-%m-%d")

    lines.append("# Quality Check — {}".format(today))
    lines.append("")

    # ── SPY Benchmark ─────────────────────────────────────────────
    spy_ytd, spy_price, spy_high, spy_low = _get_spy_ytd()
    lines.append("## SPY Benchmark")
    if spy_ytd is not None:
        lines.append("- Current Price: ${:,.2f}".format(spy_price))
        lines.append("- YTD Return: {:+.2f}%".format(spy_ytd))
        lines.append("- YTD High: ${:,.2f}".format(spy_high))
        lines.append("- YTD Low: ${:,.2f}".format(spy_low))
        drawdown = ((spy_low / spy_high) - 1) * 100
        lines.append("- Max Drawdown: {:.2f}%".format(drawdown))
    else:
        lines.append("- Could not fetch SPY data")
        warnings.append("WARN: Could not fetch SPY benchmark data")
    lines.append("")

    # ── Baseline NRWise ───────────────────────────────────────────
    lines.append("## Baseline (NRWise)")
    base = _load_json(ROOT / "state.json")
    if base:
        snaps = base.get("daily_snapshots", [])
        last = snaps[-1] if snaps else {}
        eq = last.get("equity", 0)
        ytd = ((eq / 100000) - 1) * 100
        lines.append("- Equity: ${:,.2f} ({:+.2f}%)".format(eq, ytd))
        lines.append("- Sector: {}".format(last.get("sector", "—")))
        lines.append("- Last Snapshot: {}".format(last.get("date", "?")))
        lines.append("- Snapshots: {}".format(len(snaps)))
        lines.append("- Trades: {}".format(len(base.get("trade_log", []))))
        lines.append("- Positions: {}".format(len(base.get("positions", {}))))
        if spy_ytd is not None:
            lines.append("- Alpha vs SPY: {:+.2f}%".format(ytd - spy_ytd))
    else:
        lines.append("- state.json MISSING")
        warnings.append("CRITICAL: state.json missing")
    lines.append("")

    # ── Collect all algos ─────────────────────────────────────────
    all_algos = []

    normal_dir = ROOT / "data" / "normal" / "state"
    if normal_dir.exists():
        for fp in sorted(normal_dir.glob("*.json")):
            info = _algo_summary(fp, "normal")
            if info:
                all_algos.append(info)

    crazy_dir = ROOT / "data" / "crazy" / "state"
    if crazy_dir.exists():
        for fp in sorted(crazy_dir.glob("*.json")):
            info = _algo_summary(fp, "crazy")
            if info:
                all_algos.append(info)

    # ── Normal Algos ──────────────────────────────────────────────
    lines.append("## Normal Algos")
    normals = [a for a in all_algos if a["type"] == "normal"]
    hdr = "  {:<20s}  {:>12s}  {:>8s}  {:>8s}  {:>6s}  {:>10s}  {:>10s}".format(
        "Algo", "Equity", "YTD", "Alpha", "Trades", "Signal", "Last Run")
    sep = "  " + "-" * len(hdr.strip())
    lines.append(hdr)
    lines.append(sep)
    for a in sorted(normals, key=lambda x: x["ytd_pct"], reverse=True):
        alpha = (a["ytd_pct"] - spy_ytd) if spy_ytd is not None else 0
        lines.append("  {:<20s}  {:>12s}  {:>7.2f}%  {:>7.2f}%  {:>6d}  {:>10s}  {:>10s}".format(
            a["algo_id"], "${:,.2f}".format(a["equity"]), a["ytd_pct"], alpha,
            a["num_trades"], a["signal"], a["last_date"]))
    lines.append("")

    # ── Crazy Algos ───────────────────────────────────────────────
    crazies = [a for a in all_algos if a["type"] == "crazy"]
    active = [a for a in crazies if a["num_trades"] > 0 or a["equity"] != 100000]
    idle = [a for a in crazies if a["num_trades"] == 0 and a["equity"] == 100000]

    lines.append("## Crazy Algos — Active ({}/{})".format(len(active), len(crazies)))
    if active:
        lines.append(hdr)
        lines.append(sep)
        for a in sorted(active, key=lambda x: x["ytd_pct"], reverse=True):
            alpha = (a["ytd_pct"] - spy_ytd) if spy_ytd is not None else 0
            lines.append("  {:<20s}  {:>12s}  {:>7.2f}%  {:>7.2f}%  {:>6d}  {:>10s}  {:>10s}".format(
                a["algo_id"], "${:,.2f}".format(a["equity"]), a["ytd_pct"], alpha,
                a["num_trades"], a["signal"], a["last_date"]))
    else:
        lines.append("  No crazy algos have traded yet.")
    lines.append("")

    lines.append("## Crazy Algos — Idle ({}/{})".format(len(idle), len(crazies)))
    lines.append("  These algos are running but have no recorded trades in the current state history.")
    lines.append("  That is not a crash; it means the trigger has not fired yet, the adapter returned no usable signal, or the strategy is still waiting for live evidence.")
    lines.append("")
    for i in range(0, len(idle), 4):
        chunk = idle[i:i+4]
        lines.append("  " + "  ".join("{:<35s}".format(a["algo_id"]) for a in chunk))
    lines.append("")

    # ── Blocked Algos ─────────────────────────────────────────────
    lines.append("## Blocked Algos")
    blocked_file = ROOT / "data" / "blocked" / "algos.jsonl"
    blocked = []
    if blocked_file.exists():
        seen = {}
        for line in blocked_file.read_text().splitlines():
            s = line.strip()
            if not s:
                continue
            try:
                obj = json.loads(s)
                seen[obj.get("algo_id", "")] = obj
            except Exception:
                pass
        blocked = list(seen.values())

    if blocked:
        by_key = {}
        for entry in blocked:
            for k in entry.get("keys", ["unknown"]):
                by_key.setdefault(k, []).append(entry.get("name", entry.get("algo_id", "?")))
        for key in sorted(by_key.keys()):
            algos = by_key[key]
            lines.append("- **{}** ({} algos): {}".format(key, len(algos), ", ".join(sorted(algos))))
    else:
        lines.append("None")
    lines.append("")

    # ── Weird Stuff ───────────────────────────────────────────────
    lines.append("## Flags & Warnings")

    # Check for stale algos (last run not today or yesterday)
    for a in all_algos:
        try:
            last_dt = datetime.strptime(a["last_date"], "%Y-%m-%d").date()
            today_dt = datetime.utcnow().date()
            days_ago = (today_dt - last_dt).days
            # weekends: if today is Sunday/Monday, allow 2-3 days
            if days_ago > 3:
                w = "STALE: {} last ran {} ({} days ago)".format(a["algo_id"], a["last_date"], days_ago)
                warnings.append(w)
        except Exception:
            warnings.append("BAD DATE: {} has last_date='{}'".format(a["algo_id"], a["last_date"]))

    # Negative equity
    for a in all_algos:
        if a["equity"] <= 0:
            warnings.append("CRITICAL: {} has zero/negative equity: ${:,.2f}".format(a["algo_id"], a["equity"]))

    # Big drawdown (> 15%)
    for a in all_algos:
        if a["ytd_pct"] < -15:
            warnings.append("BIG LOSS: {} is down {:.2f}% YTD".format(a["algo_id"], a["ytd_pct"]))

    # Big gain (> 30%) — might be a bug
    for a in all_algos:
        if a["ytd_pct"] > 30:
            warnings.append("SUSPICIOUSLY HIGH: {} is up {:.2f}% YTD — verify not a bug".format(a["algo_id"], a["ytd_pct"]))

    # Snapshot count mismatch between normals
    if normals:
        snap_counts = set(a["num_snapshots"] for a in normals)
        if len(snap_counts) > 1:
            warnings.append("SNAPSHOT MISMATCH: normal algos have different snapshot counts: {}".format(
                {a["algo_id"]: a["num_snapshots"] for a in normals}))

    # Any algo with positions but signal is HOLD
    for a in all_algos:
        if a["num_positions"] > 0 and a["signal"] == "HOLD":
            warnings.append("POSITIONS WITH HOLD: {} has {} positions but signal is HOLD".format(
                a["algo_id"], a["num_positions"]))

    # Algos with many trades but underwater
    for a in all_algos:
        if a["num_trades"] > 20 and a["ytd_pct"] < -5:
            warnings.append("CHURNING: {} has {} trades but is down {:.2f}% — overtrading?".format(
                a["algo_id"], a["num_trades"], a["ytd_pct"]))

    # Summary stats
    if spy_ytd is not None:
        beating = sum(1 for a in all_algos if a["ytd_pct"] > spy_ytd)
        genuinely_beating = sum(1 for a in all_algos if a["ytd_pct"] > spy_ytd and a["num_trades"] > 0)
        lines.append("- Total algos: {}".format(len(all_algos)))
        lines.append("- Beating SPY: {}/{} (but only {} have actually traded)".format(
            beating, len(all_algos), genuinely_beating))
        best = max(all_algos, key=lambda x: x["ytd_pct"])
        worst = min(all_algos, key=lambda x: x["ytd_pct"])
        lines.append("- Best: {} at {:+.2f}%".format(best["algo_id"], best["ytd_pct"]))
        lines.append("- Worst: {} at {:+.2f}%".format(worst["algo_id"], worst["ytd_pct"]))

    if warnings:
        lines.append("")
        for w in warnings:
            lines.append("- {}".format(w))
    else:
        lines.append("- ALL CLEAR — nothing weird detected")

    lines.append("")
    lines.append("---")
    lines.append("_Generated by `scripts/quality_check.py` at {}_".format(
        datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")))

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--stdout", action="store_true", help="Print only, don't write file")
    args = parser.parse_args()

    report = build_report()
    print(report)

    if not args.stdout:
        today = datetime.utcnow().strftime("%Y-%m-%d")
        out_dir = ROOT / "docs" / "quality_checks"
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / "quality_check_{}.md".format(today)
        out_path.write_text(report, encoding="utf-8")
        print("\nWritten to {}".format(out_path))


if __name__ == "__main__":
    main()
