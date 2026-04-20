from __future__ import annotations

import json
from dataclasses import asdict
from datetime import datetime
from pathlib import Path
from typing import Iterable

import pandas as pd

from backtest.engine import BacktestResult


def _safe_metrics(metrics: dict) -> dict:
    return metrics or {}


def write_result(result: BacktestResult, root: Path, run_date: str) -> dict:
    algo_dir = root / result.algo_id
    algo_dir.mkdir(parents=True, exist_ok=True)

    if not result.equity_curve.empty:
        result.equity_curve.to_csv(algo_dir / "equity_curve.csv", index=False)
    else:
        (algo_dir / "equity_curve.csv").write_text("date,equity\n", encoding="utf-8")

    pd.DataFrame(result.trades).to_csv(algo_dir / "trades.csv", index=False)

    payload = {
        "algo_id": result.algo_id,
        "name": result.name,
        "family": result.family,
        "status": result.status,
        "reason": result.reason,
        "metrics": _safe_metrics(result.metrics),
        "run_date": run_date,
    }
    (algo_dir / "metrics.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    (algo_dir / "summary.md").write_text(_summary_md(payload), encoding="utf-8")
    return payload


def _summary_md(payload: dict) -> str:
    m = payload.get("metrics") or {}
    lines = [
        f"# Backtest: {payload['name']}",
        "",
        f"- Algo ID: `{payload['algo_id']}`",
        f"- Family: `{payload['family']}`",
        f"- Status: `{payload['status']}`",
        f"- Reason: {payload['reason']}",
        "",
        "## Metrics",
        "",
    ]
    if not m:
        lines.append("No metrics because this algo was not V1-backtestable.")
    else:
        for key in ["total_return_pct", "spy_return_pct", "alpha_vs_spy_pct", "max_drawdown_pct", "spy_max_drawdown_pct", "sharpe", "trade_count", "win_rate_pct", "turnover"]:
            lines.append(f"- {key}: {m.get(key)}")
    lines.extend([
        "",
        "## Method",
        "",
        "V1 professional backtest: signal after close, execution next trading day open, 5 bps default slippage, long/cash only, compared with SPY buy-and-hold. Not investment advice.",
    ])
    return "\n".join(lines) + "\n"


def write_master(results: Iterable[dict], root: Path, run_date: str, start: str, end: str, slippage_bps: float) -> None:
    rows = list(results)
    root.mkdir(parents=True, exist_ok=True)
    counts = {}
    for r in rows:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    summary = {
        "run_date": run_date,
        "start": start,
        "end": end,
        "slippage_bps": slippage_bps,
        "generated_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "counts": counts,
        "results": rows,
    }
    (root / "latest.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    (root / f"{run_date}.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    (root / "latest.md").write_text(_master_md(summary), encoding="utf-8")
    (root / f"{run_date}.md").write_text(_master_md(summary), encoding="utf-8")


def _master_md(summary: dict) -> str:
    lines = [
        "# Professional Backtest V1",
        "",
        f"- Run date: {summary['run_date']}",
        f"- Window: {summary['start']} to {summary['end']}",
        f"- Slippage: {summary['slippage_bps']} bps per trade",
        "- Method: signal after close, execute next trading day open, long/cash only, SPY benchmark.",
        "",
        "## Counts",
        "",
    ]
    for key, value in sorted(summary["counts"].items()):
        lines.append(f"- {key}: {value}")
    lines.extend(["", "## Results", "", "| Algo | Family | Status | Alpha vs SPY | Trades | Reason |", "| --- | --- | --- | ---: | ---: | --- |"])
    for r in summary["results"]:
        m = r.get("metrics") or {}
        lines.append(
            f"| {r['name']} | {r['family']} | {r['status']} | "
            f"{m.get('alpha_vs_spy_pct', '')} | {m.get('trade_count', '')} | {r['reason']} |"
        )
    lines.extend(["", "This is experimental research, not investment advice. Past performance does not predict future results."])
    return "\n".join(lines) + "\n"
