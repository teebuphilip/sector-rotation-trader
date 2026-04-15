#!/usr/bin/env python3
"""
Build a standalone deep validation report for the content engine.

This is intentionally outside the tactical run. It reads already-produced
artifacts and writes a human report plus a machine JSON version:
  reports/deep_validation/YYYY-MM-DD.md
  reports/deep_validation/YYYY-MM-DD.json
  reports/deep_validation/latest.md
  reports/deep_validation/latest.json

Inputs are treated as authoritative; this script explains and joins them, it
does not rerun strategies or recompute trading metrics.
"""
from __future__ import annotations

import argparse
import csv
import json
import shutil
from datetime import date, datetime
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

ROOT = Path(__file__).resolve().parents[1]
RANK_CSV = ROOT / "data" / "rank_history.csv"
ROLLING_JSON = ROOT / "docs" / "leaderboards" / "rolling_30d.json"
SIGNALS_JSON = ROOT / "docs" / "signals" / "index.json"
OUT_DIR = ROOT / "reports" / "deep_validation"


def _load_json(path: Path) -> Optional[Dict[str, Any]]:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text())
    except Exception:
        return None


def _float(value: Any, default: float = 0.0) -> float:
    try:
        if value is None or value == "":
            return default
        return float(value)
    except Exception:
        return default


def _int(value: Any, default: int = 0) -> int:
    try:
        if value is None or value == "":
            return default
        return int(float(value))
    except Exception:
        return default


def _pct(value: Optional[float], scale: float = 1.0) -> str:
    if value is None:
        return "n/a"
    return f"{value * scale:+.2f}%"


def _read_rank_rows() -> List[Dict[str, str]]:
    if not RANK_CSV.exists():
        return []
    with RANK_CSV.open("r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _select_rank_date(rows: List[Dict[str, str]], requested: Optional[str]) -> str:
    dates = sorted({r.get("date", "") for r in rows if r.get("date")})
    if requested:
        return requested
    if dates:
        return dates[-1]
    return date.today().isoformat()


def _force_rows(rows: List[Dict[str, str]], report_date: str) -> List[Dict[str, Any]]:
    selected = [r for r in rows if r.get("date") == report_date]
    out = []
    for r in selected:
        out.append({
            "date": r.get("date", report_date),
            "rank_return": _int(r.get("rank_return")),
            "rank_alpha": _int(r.get("rank_alpha")),
            "algo_id": r.get("algo_id", ""),
            "algo_type": r.get("algo_type", ""),
            "name": r.get("name") or r.get("algo_id", ""),
            "ytd_pct": _float(r.get("ytd_pct")),
            "spy_pct": _float(r.get("spy_pct")),
            "alpha_pct": _float(r.get("alpha_pct")),
            "equity": _float(r.get("equity")),
            "beat_spy": str(r.get("beat_spy", "")).lower() == "true",
            "days_running": _int(r.get("days_running")),
        })
    return sorted(out, key=lambda r: r["rank_return"] or 999999)


def _previous_rank_map(rows: List[Dict[str, str]], report_date: str) -> Dict[str, int]:
    dates = sorted({r.get("date", "") for r in rows if r.get("date") and r.get("date") < report_date})
    if not dates:
        return {}
    prior_date = dates[-1]
    return {
        r.get("algo_id", ""): _int(r.get("rank_return"))
        for r in rows
        if r.get("date") == prior_date and r.get("algo_id")
    }


def _with_rank_changes(force: List[Dict[str, Any]], prior: Dict[str, int]) -> None:
    for r in force:
        old = prior.get(r["algo_id"])
        if old:
            # Positive means moved up, negative means fell.
            r["rank_change"] = old - r["rank_return"]
            r["previous_rank_return"] = old
        else:
            r["rank_change"] = None
            r["previous_rank_return"] = None


def _rolling_entries() -> Tuple[List[Dict[str, Any]], Optional[float], Optional[str]]:
    raw = _load_json(ROLLING_JSON) or {}
    entries = []
    for idx, e in enumerate(raw.get("entries", []) or [], 1):
        row = dict(e)
        category = str(e.get("category") or "")
        row["algo_type"] = "crazy" if category == "crazy" else "normal"
        row["rolling_30d_rank"] = idx
        row["ret_30d"] = e.get("ret_30d")
        row["spy_delta_30d"] = None
        spy = raw.get("spy_ret_30d")
        if e.get("ret_30d") is not None and spy is not None:
            row["spy_delta_30d"] = float(e["ret_30d"]) - float(spy)
        entries.append(row)
    return entries, raw.get("spy_ret_30d"), raw.get("as_of")


def _sector_consensus(signals: Dict[str, Any]) -> Dict[str, Any]:
    summary = signals.get("sector_summary", {}) or {}
    sectors = []
    for etf, data in summary.items():
        row = dict(data)
        row["etf"] = etf
        row["bullish_pct"] = _int(row.get("bullish_pct"))
        sectors.append(row)
    sectors.sort(key=lambda s: (s.get("bullish_pct", 0), s.get("etf", "")), reverse=True)
    return {
        "generated": signals.get("generated"),
        "signal_count": signals.get("signal_count", 0),
        "total_algos": signals.get("total_algos", 0),
        "ticker_count": signals.get("ticker_count", 0),
        "top_bullish_etfs": signals.get("top_bullish_etfs", []) or [],
        "top_bearish_etfs": signals.get("top_bearish_etfs", []) or [],
        "sector_summary": summary,
        "sectors_ranked": sectors,
    }


def _join_by_algo(force: List[Dict[str, Any]], rolling: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    rolling_by_key = {
        (r.get("algo_id"), r.get("algo_type")): r
        for r in rolling
        if r.get("algo_id")
    }
    rows = []
    for f in force:
        row = dict(f)
        r = rolling_by_key.get((f["algo_id"], f.get("algo_type")), {})
        row.update({
            "rolling_30d_rank": r.get("rolling_30d_rank"),
            "ret_30d": r.get("ret_30d"),
            "spy_delta_30d": r.get("spy_delta_30d"),
            "sharpe_30d": r.get("sharpe_30d"),
            "max_dd_30d": r.get("max_dd_30d"),
        })
        rows.append(row)
    return rows


def _divergences(joined: List[Dict[str, Any]], limit: int = 5) -> List[Dict[str, Any]]:
    candidates = []
    for r in joined:
        force_rank = r.get("rank_return")
        rolling_rank = r.get("rolling_30d_rank")
        if not force_rank or not rolling_rank:
            continue
        gap = int(force_rank) - int(rolling_rank)
        if abs(gap) < 10:
            continue
        if gap > 0:
            explanation = "Strong recent 30D rank despite weaker full-window force rank."
        else:
            explanation = "Strong full-window force rank but weaker recent 30D rank."
        candidates.append({
            "algo_id": r.get("algo_id"),
            "name": r.get("name"),
            "force_rank": force_rank,
            "rolling_30d_rank": rolling_rank,
            "rank_gap": gap,
            "ret_30d": r.get("ret_30d"),
            "ytd_pct": r.get("ytd_pct"),
            "explanation": explanation,
        })
    return sorted(candidates, key=lambda x: abs(x["rank_gap"]), reverse=True)[:limit]


def _biggest_movers(force: List[Dict[str, Any]], limit: int = 5) -> Dict[str, List[Dict[str, Any]]]:
    known = [r for r in force if r.get("rank_change") is not None]
    up = sorted([r for r in known if r["rank_change"] > 0], key=lambda r: r["rank_change"], reverse=True)[:limit]
    down = sorted([r for r in known if r["rank_change"] < 0], key=lambda r: r["rank_change"])[:limit]
    def slim(rows: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
        return [{
            "algo_id": r.get("algo_id"),
            "name": r.get("name"),
            "rank_return": r.get("rank_return"),
            "previous_rank_return": r.get("previous_rank_return"),
            "rank_change": r.get("rank_change"),
            "ytd_pct": r.get("ytd_pct"),
            "alpha_pct": r.get("alpha_pct"),
        } for r in rows]
    return {"up": slim(up), "down": slim(down)}


def _content_facts(force: List[Dict[str, Any]], rolling: List[Dict[str, Any]], sectors: Dict[str, Any], joined: List[Dict[str, Any]]) -> Dict[str, Any]:
    top_rolling = rolling[0] if rolling else None
    top_force = force[0] if force else None
    divs = _divergences(joined)
    force_by_key = {(r["algo_id"], r.get("algo_type")): r for r in force}

    signal = None
    if top_rolling:
        f = force_by_key.get((top_rolling.get("algo_id"), top_rolling.get("algo_type")), {})
        signal = {
            "algo_id": top_rolling.get("algo_id"),
            "name": top_rolling.get("name"),
            "reason": "Ranked #1 on rolling 30D leaderboard",
            "rank": top_rolling.get("rolling_30d_rank", 1),
            "rank_type": "rolling_30d",
            "ret_30d": top_rolling.get("ret_30d"),
            "spy_delta_30d": top_rolling.get("spy_delta_30d"),
            "force_rank": f.get("rank_return"),
            "caveat": f"Force rank #{f.get('rank_return')}" if f.get("rank_return") else None,
        }
    elif top_force:
        signal = {
            "algo_id": top_force.get("algo_id"),
            "name": top_force.get("name"),
            "reason": "Ranked #1 on force rank",
            "rank": top_force.get("rank_return"),
            "rank_type": "force_rank",
            "ret_30d": None,
            "spy_delta_30d": None,
            "force_rank": top_force.get("rank_return"),
            "caveat": None,
        }

    ranked_sectors = sectors.get("sectors_ranked", [])
    top_sector = ranked_sectors[0] if ranked_sectors else None
    call = None
    if top_sector:
        call = {
            "sector": top_sector.get("etf"),
            "sector_name": top_sector.get("sector"),
            "stance": top_sector.get("composite_label"),
            "composite": top_sector.get("composite"),
            "bullish_pct": top_sector.get("bullish_pct"),
            "reason": "Highest bullish percentage in precomputed sector consensus",
        }

    failures = [r for r in force[-5:] if not r.get("beat_spy")]
    failure = None
    if failures:
        worst = force[-1]
        failure = {
            "algo_id": worst.get("algo_id"),
            "name": worst.get("name"),
            "reason": "Lowest full-window force rank",
            "rank_return": worst.get("rank_return"),
            "ytd_pct": worst.get("ytd_pct"),
            "alpha_pct": worst.get("alpha_pct"),
            "status": "FAILING",
        }

    return {
        "signal_of_day": signal,
        "call_of_day": call,
        "failure_of_day": failure,
        "notable_divergences": divs,
    }


def _build_report(report_date: str) -> Dict[str, Any]:
    rank_rows = _read_rank_rows()
    force = _force_rows(rank_rows, report_date)
    prior = _previous_rank_map(rank_rows, report_date)
    _with_rank_changes(force, prior)

    rolling, spy_30d, rolling_as_of = _rolling_entries()
    signals = _load_json(SIGNALS_JSON) or {}
    sectors = _sector_consensus(signals)
    joined = _join_by_algo(force, rolling)
    movers = _biggest_movers(force)
    facts = _content_facts(force, rolling, sectors, joined)

    beating = sum(1 for r in force if r.get("beat_spy"))
    rolling_beating_spy = 0
    if spy_30d is not None:
        rolling_beating_spy = sum(1 for r in rolling if r.get("ret_30d") is not None and r["ret_30d"] > spy_30d)

    return {
        "report_date": report_date,
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "definitions": {
            "force_rank": "Full-window/since-seed rank from data/rank_history.csv. Use for long-term trust, promotion, demotion, and kill review.",
            "rolling_30d": "Recent trailing 30-day return rank from docs/leaderboards/rolling_30d.json. Use for tactical spotlight and recent momentum.",
            "sector_consensus": "Precomputed sector verdicts from docs/signals/index.json. Use for current directional sector context.",
        },
        "system_state": {
            "total_force_ranked": len(force),
            "beating_spy_force_rank": beating,
            "rolling_30d_algos": len(rolling),
            "rolling_30d_beating_spy": rolling_beating_spy,
            "signals_generated": sectors.get("signal_count", 0),
            "tickers_covered": sectors.get("ticker_count", 0),
            "sectors_computed": len(sectors.get("sector_summary", {})),
        },
        "force_rank": {
            "definition": "Full-window/since-seed rank; not the same as recent 30D performance.",
            "top_10": force[:10],
            "bottom_5": force[-5:],
            "biggest_movers": movers,
        },
        "rolling_30d": {
            "definition": "Trailing 30-day return rank; useful for recent momentum and tactical spotlight.",
            "as_of": rolling_as_of,
            "spy_ret_30d": spy_30d,
            "top_10": rolling[:10],
            "bottom_5": rolling[-5:],
        },
        "sector_consensus": sectors,
        "events": {
            "promoted": [],
            "killed": [],
            "flagged_for_review": facts.get("notable_divergences", []),
        },
        "content_facts": facts,
    }


def _md_row_force(r: Dict[str, Any]) -> str:
    ch = r.get("rank_change")
    ch_s = "n/a" if ch is None else f"{ch:+d}"
    return f"| {r.get('rank_return')} | {r.get('name')} | {r.get('algo_type')} | {_pct(r.get('ytd_pct'))} | {_pct(r.get('alpha_pct'))} | {ch_s} |"


def _md_row_rolling(i: int, r: Dict[str, Any]) -> str:
    return f"| {i} | {r.get('name')} | {r.get('category')} | {_pct(r.get('ret_30d'), 100)} | {_pct(r.get('spy_delta_30d'), 100)} |"


def _write_md(report: Dict[str, Any], path: Path) -> None:
    lines = []
    lines.append(f"# Deep Validation Report - {report['report_date']}")
    lines.append("")
    lines.append("## Definitions")
    for key, text in report["definitions"].items():
        lines.append(f"- {key}: {text}")
    lines.append("")

    s = report["system_state"]
    lines.append("## System State")
    lines.append(f"- Force-ranked algos: {s['total_force_ranked']}")
    lines.append(f"- Force-ranked beating SPY: {s['beating_spy_force_rank']} of {s['total_force_ranked']}")
    lines.append(f"- Rolling 30D algos: {s['rolling_30d_algos']}")
    lines.append(f"- Rolling 30D beating SPY: {s['rolling_30d_beating_spy']} of {s['rolling_30d_algos']}")
    lines.append(f"- Signals generated: {s['signals_generated']}")
    lines.append(f"- Tickers covered: {s['tickers_covered']}")
    lines.append(f"- Sectors computed: {s['sectors_computed']}")
    lines.append("")

    lines.append("## Force Rank")
    lines.append(report["force_rank"]["definition"])
    lines.append("")
    lines.append("### Top 10")
    lines.append("| Rank | Algo | Type | Return | Alpha vs SPY | Rank Change |")
    lines.append("| --- | --- | --- | --- | --- | --- |")
    for r in report["force_rank"]["top_10"]:
        lines.append(_md_row_force(r))
    lines.append("")
    lines.append("### Bottom 5")
    lines.append("| Rank | Algo | Type | Return | Alpha vs SPY | Rank Change |")
    lines.append("| --- | --- | --- | --- | --- | --- |")
    for r in report["force_rank"]["bottom_5"]:
        lines.append(_md_row_force(r))
    lines.append("")

    lines.append("## Rolling 30D")
    lines.append(report["rolling_30d"]["definition"])
    lines.append(f"SPY 30D: {_pct(report['rolling_30d'].get('spy_ret_30d'), 100)}")
    lines.append("")
    lines.append("| Rank | Algo | Category | 30D Return | 30D vs SPY |")
    lines.append("| --- | --- | --- | --- | --- |")
    for i, r in enumerate(report["rolling_30d"]["top_10"], 1):
        lines.append(_md_row_rolling(i, r))
    lines.append("")

    lines.append("## Sector Consensus")
    sc = report["sector_consensus"]
    lines.append(f"- Top Bullish: {', '.join(sc.get('top_bullish_etfs') or []) or 'none'}")
    lines.append(f"- Top Bearish: {', '.join(sc.get('top_bearish_etfs') or []) or 'none'}")
    lines.append("")
    lines.append("| ETF | Sector | Composite | Label | Bullish % |")
    lines.append("| --- | --- | --- | --- | --- |")
    for row in sc.get("sectors_ranked", []):
        lines.append(f"| {row.get('etf')} | {row.get('sector')} | {row.get('composite')} | {row.get('composite_label')} | {row.get('bullish_pct')}% |")
    lines.append("")

    lines.append("## Content Facts")
    facts = report["content_facts"]
    signal = facts.get("signal_of_day") or {}
    call = facts.get("call_of_day") or {}
    failure = facts.get("failure_of_day") or {}
    lines.append(f"- Signal of day: {signal.get('name', 'none')} ({signal.get('reason', '')})")
    lines.append(f"- Call of day: {call.get('sector', 'none')} {call.get('stance', '')} ({call.get('reason', '')})")
    lines.append(f"- Failure of day: {failure.get('name', 'none')} ({failure.get('reason', '')})")
    lines.append("")
    lines.append("## Notable Divergences")
    divs = facts.get("notable_divergences", [])
    if not divs:
        lines.append("- none")
    for d in divs:
        lines.append(f"- {d.get('name')}: force rank #{d.get('force_rank')}, rolling 30D rank #{d.get('rolling_30d_rank')}. {d.get('explanation')}")
    lines.append("")

    path.write_text("\n".join(lines) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", help="Report date. Defaults to latest date in rank_history.csv.")
    parser.add_argument("--out-dir", default=str(OUT_DIR))
    args = parser.parse_args()

    rows = _read_rank_rows()
    report_date = _select_rank_date(rows, args.date)
    report = _build_report(report_date)

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / f"{report_date}.json"
    md_path = out_dir / f"{report_date}.md"
    json_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    _write_md(report, md_path)
    shutil.copyfile(json_path, out_dir / "latest.json")
    shutil.copyfile(md_path, out_dir / "latest.md")

    print(f"[report] wrote {json_path.relative_to(ROOT)}")
    print(f"[report] wrote {md_path.relative_to(ROOT)}")
    print(f"[report] wrote {Path(args.out_dir).relative_to(ROOT) / 'latest.json'}")
    print(f"[report] wrote {Path(args.out_dir).relative_to(ROOT) / 'latest.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
