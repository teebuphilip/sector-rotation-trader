#!/usr/bin/env python3
"""
Generate public-facing content from a deep validation report JSON.

No strategy metrics are recomputed here. The report JSON is the source of
truth; this script only formats validated facts into short text files.
"""
from __future__ import annotations

import argparse
import json
from datetime import date, datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REPORT = ROOT / "reports" / "deep_validation" / "latest.json"
DEFAULT_OUT = ROOT / "content"


def _load(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text())


def _pct(value: Optional[float], scale: float = 1.0) -> str:
    if value is None:
        return "n/a"
    return f"{value * scale:+.2f}%"


def _rank_change(value: Any) -> str:
    if value is None:
        return "new/no prior"
    try:
        n = int(value)
    except Exception:
        return "n/a"
    if n > 0:
        return f"up {n}"
    if n < 0:
        return f"down {abs(n)}"
    return "unchanged"


def _safe_name(row: Dict[str, Any]) -> str:
    return str(row.get("name") or row.get("algo_id") or "unknown")


def _daily_post(report: Dict[str, Any]) -> str:
    d = report["report_date"]
    force = report.get("force_rank", {})
    rolling = report.get("rolling_30d", {})
    state = report.get("system_state", {})
    facts = report.get("content_facts", {})
    lines: List[str] = []

    lines.append(f"Daily Signal Board - {d}")
    lines.append("")
    lines.append("Force rank is full-window/since-seed. Rolling 30D is recent momentum.")
    lines.append("")
    lines.append("Top force-ranked signals:")
    for r in (force.get("top_10") or [])[:5]:
        lines.append(f"{r.get('rank_return')}. {_safe_name(r)} {_pct(r.get('ytd_pct'))} alpha {_pct(r.get('alpha_pct'))} ({_rank_change(r.get('rank_change'))})")

    lines.append("")
    lines.append("Top rolling 30D signals:")
    for i, r in enumerate((rolling.get("top_10") or [])[:5], 1):
        lines.append(f"{i}. {_safe_name(r)} {_pct(r.get('ret_30d'), 100)} vs SPY {_pct(r.get('spy_delta_30d'), 100)}")

    divs = facts.get("notable_divergences") or []
    if divs:
        lines.append("")
        lines.append("Notable divergence:")
        for drow in divs[:3]:
            lines.append(f"- {_safe_name(drow)}: force #{drow.get('force_rank')}, rolling 30D #{drow.get('rolling_30d_rank')}")

    lines.append("")
    lines.append("System:")
    lines.append(f"- {state.get('total_force_ranked', 0)} force-ranked algos")
    lines.append(f"- {state.get('beating_spy_force_rank', 0)} beating SPY on force rank")
    lines.append(f"- {state.get('signals_generated', 0)} current signals across {state.get('tickers_covered', 0)} tickers")
    return "\n".join(lines) + "\n"


def _signal_of_day(report: Dict[str, Any]) -> str:
    d = report["report_date"]
    signal = (report.get("content_facts") or {}).get("signal_of_day") or {}
    if not signal:
        return f"Signal of the Day - {d}\n\nNo signal selected.\n"

    lines = [f"Signal of the Day - {d}", "", str(signal.get("name", "unknown")), ""]
    lines.append(str(signal.get("reason", "Selected by validation report.")))
    if signal.get("ret_30d") is not None:
        lines.append(f"30D return: {_pct(signal.get('ret_30d'), 100)}")
    if signal.get("spy_delta_30d") is not None:
        lines.append(f"30D vs SPY: {_pct(signal.get('spy_delta_30d'), 100)}")
    if signal.get("force_rank"):
        lines.append(f"Force rank: #{signal.get('force_rank')}")
    if signal.get("caveat"):
        lines.append("")
        lines.append(f"Caveat: {signal.get('caveat')}. Rolling momentum is not the same as full-window validation.")
    return "\n".join(lines) + "\n"


def _failure_report(report: Dict[str, Any]) -> str:
    d = report["report_date"]
    failure = (report.get("content_facts") or {}).get("failure_of_day") or {}
    bottom = (report.get("force_rank") or {}).get("bottom_5") or []
    lines = [f"Failure Report - {d}", ""]

    if failure:
        lines.append(f"Failure of the day: {failure.get('name')}")
        lines.append(f"Reason: {failure.get('reason')}")
        lines.append(f"Force rank: #{failure.get('rank_return')}")
        lines.append(f"Return: {_pct(failure.get('ytd_pct'))}")
        lines.append(f"Alpha vs SPY: {_pct(failure.get('alpha_pct'))}")
        lines.append(f"Status: {failure.get('status', 'FAILING')}")
    else:
        lines.append("No failure selected by validation report.")

    if bottom:
        lines.append("")
        lines.append("Bottom force-ranked signals:")
        for r in bottom:
            lines.append(f"- #{r.get('rank_return')} {_safe_name(r)} {_pct(r.get('ytd_pct'))} alpha {_pct(r.get('alpha_pct'))}")
    return "\n".join(lines) + "\n"


def _call_of_day(report: Dict[str, Any]) -> str:
    d = report["report_date"]
    call = (report.get("content_facts") or {}).get("call_of_day") or {}
    sectors = (report.get("sector_consensus") or {}).get("sectors_ranked") or []
    lines = [f"Call of the Day - {d}", ""]
    if call:
        lines.append(f"{call.get('sector')} - {call.get('stance')}")
        if call.get("sector_name"):
            lines.append(str(call.get("sector_name")))
        lines.append(f"Composite: {call.get('composite')}")
        lines.append(f"Bullish: {call.get('bullish_pct')}%")
        lines.append(f"Reason: {call.get('reason')}")
    else:
        lines.append("No sector call selected by validation report.")

    if sectors:
        lines.append("")
        lines.append("Top sector context:")
        for row in sectors[:3]:
            lines.append(f"- {row.get('etf')} {row.get('sector')}: {row.get('composite')} {row.get('composite_label')}")
    return "\n".join(lines) + "\n"


def _weekly_summary(report: Dict[str, Any]) -> str:
    # V1 is current-report based. It intentionally does not aggregate unless a
    # future weekly report builder provides authoritative weekly facts.
    d = report["report_date"]
    try:
        iso = date.fromisoformat(d).isocalendar()
        week_id = f"{iso.year}-W{iso.week:02d}"
    except Exception:
        week_id = datetime.utcnow().strftime("%G-W%V")
    state = report.get("system_state", {})
    rolling = (report.get("rolling_30d") or {}).get("top_10") or []
    force_bottom = (report.get("force_rank") or {}).get("bottom_5") or []

    lines = [f"Weekly Summary - {week_id}", ""]
    lines.append("Current report snapshot. Weekly aggregation is not enabled yet.")
    lines.append("")
    lines.append("Top recent signals:")
    for i, r in enumerate(rolling[:5], 1):
        lines.append(f"{i}. {_safe_name(r)} {_pct(r.get('ret_30d'), 100)}")
    lines.append("")
    lines.append("Weakest force-ranked signals:")
    for r in force_bottom:
        lines.append(f"- #{r.get('rank_return')} {_safe_name(r)} {_pct(r.get('ytd_pct'))}")
    lines.append("")
    lines.append("System health:")
    lines.append(f"- {state.get('total_force_ranked', 0)} force-ranked algos")
    lines.append(f"- {state.get('beating_spy_force_rank', 0)} beating SPY on force rank")
    lines.append(f"- {state.get('signals_generated', 0)} generated signals")
    return "\n".join(lines) + "\n"


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    print(f"[content] wrote {path.relative_to(ROOT)}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", default=str(DEFAULT_REPORT), help="Deep validation report JSON")
    parser.add_argument("--out-dir", default=str(DEFAULT_OUT))
    args = parser.parse_args()

    report_path = Path(args.report)
    report = _load(report_path)
    report_date = report.get("report_date") or date.today().isoformat()
    out = Path(args.out_dir)

    try:
        iso = date.fromisoformat(report_date).isocalendar()
        week_id = f"{iso.year}-W{iso.week:02d}"
    except Exception:
        week_id = datetime.utcnow().strftime("%G-W%V")

    _write(out / "daily" / f"{report_date}.txt", _daily_post(report))
    _write(out / "signal_of_day" / f"{report_date}.txt", _signal_of_day(report))
    _write(out / "failures" / f"{report_date}.txt", _failure_report(report))
    _write(out / "call_of_day" / f"{report_date}.txt", _call_of_day(report))
    _write(out / "weekly" / f"{week_id}.txt", _weekly_summary(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
