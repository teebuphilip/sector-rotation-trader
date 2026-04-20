from __future__ import annotations

import importlib
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any
from unittest.mock import patch

import pandas as pd

from backtest.classifier import BacktestClassification, classify_algo
from backtest.metrics import compute_metrics, label as label_metrics
from backtest.price_data import PriceData, download_price_data, price_adapter_frame
from config import SECTOR_ETFS

STARTING_CASH = 100_000.0


@dataclass
class BacktestResult:
    algo_id: str
    name: str
    family: str
    status: str
    reason: str
    metrics: dict[str, Any]
    trades: list[dict[str, Any]]
    equity_curve: pd.DataFrame
    spy_curve: pd.DataFrame


def default_state(start: date) -> dict[str, Any]:
    return {
        "cash": STARTING_CASH,
        "positions": {},
        "trade_log": [],
        "daily_snapshots": [],
        "meta": {},
        "sim_start": start.isoformat(),
        "last_run": None,
    }


def _prices_on(df: pd.DataFrame, ts: pd.Timestamp, tickers: list[str]) -> dict[str, float]:
    if df.empty or ts not in df.index:
        return {}
    row = df.loc[ts]
    prices: dict[str, float] = {}
    for t in tickers:
        key = t.upper()
        if key in row.index and pd.notna(row[key]):
            prices[key] = float(row[key])
    return prices


def _equity(state: dict[str, Any], prices: dict[str, float]) -> float:
    pos_value = 0.0
    for ticker, pos in state["positions"].items():
        px = prices.get(ticker, pos["entry_price"])
        pos_value += pos["shares"] * px
    return float(state["cash"] + pos_value)


def _snapshot(state: dict[str, Any], ts: pd.Timestamp, prices: dict[str, float]) -> None:
    state["daily_snapshots"].append({
        "date": ts.date().isoformat(),
        "cash": round(float(state["cash"]), 2),
        "equity": round(_equity(state, prices), 2),
        "positions": dict(state["positions"]),
        "num_positions": len(state["positions"]),
    })
    state["last_run"] = ts.date().isoformat()


def _close_position(state: dict[str, Any], ticker: str, price: float, ts: pd.Timestamp, slippage_bps: float) -> None:
    if ticker not in state["positions"]:
        return
    pos = state["positions"][ticker]
    exec_price = price * (1.0 - slippage_bps / 10000.0)
    gross = pos["shares"] * exec_price
    pnl = gross - pos["cost"]
    state["cash"] += gross
    state["trade_log"].append({
        "date": ts.date().isoformat(),
        "action": "SELL",
        "ticker": ticker,
        "shares": round(pos["shares"], 4),
        "price": round(exec_price, 4),
        "notional": round(gross, 2),
        "pnl": round(pnl, 2),
        "entry_date": pos["entry_date"],
        "reason": "rebalance",
    })
    del state["positions"][ticker]


def _open_position(state: dict[str, Any], ticker: str, amount: float, price: float, ts: pd.Timestamp, slippage_bps: float) -> None:
    if amount <= 0:
        return
    exec_price = price * (1.0 + slippage_bps / 10000.0)
    spend = min(amount, state["cash"])
    if spend <= 0 or exec_price <= 0:
        return
    shares = spend / exec_price
    state["cash"] -= spend
    state["positions"][ticker] = {
        "shares": shares,
        "entry_price": exec_price,
        "entry_date": ts.date().isoformat(),
        "cost": spend,
    }
    state["trade_log"].append({
        "date": ts.date().isoformat(),
        "action": "BUY",
        "ticker": ticker,
        "shares": round(shares, 4),
        "price": round(exec_price, 4),
        "notional": round(spend, 2),
    })


def _rebalance_to_target(state: dict[str, Any], target: dict[str, float], prices: dict[str, float], ts: pd.Timestamp, slippage_bps: float) -> bool:
    normalized = {str(k).upper(): float(v) for k, v in (target or {}).items() if float(v) > 0}
    if any(float(v) < 0 for v in (target or {}).values()):
        raise ValueError("negative target allocation is unsupported in V1")

    changed = False
    for ticker in list(state["positions"].keys()):
        if ticker in prices:
            _close_position(state, ticker, prices[ticker], ts, slippage_bps)
            changed = True

    if not normalized:
        return changed

    equity = _equity(state, prices)
    total_weight = min(sum(normalized.values()), 1.0)
    if total_weight <= 0:
        return changed
    scale = min(1.0, 1.0 / sum(normalized.values())) if sum(normalized.values()) > 1 else 1.0
    for ticker, weight in normalized.items():
        if ticker not in prices:
            continue
        amount = equity * weight * scale
        _open_position(state, ticker, amount, prices[ticker], ts, slippage_bps)
        changed = True
    return changed


def _is_month_end(ts: pd.Timestamp, all_dates: list[pd.Timestamp]) -> bool:
    future = [d for d in all_dates if d > ts and d.month == ts.month]
    return not future


def _spy_curve(price_data: PriceData, dates: list[pd.Timestamp]) -> pd.DataFrame:
    if price_data.open.empty or price_data.close.empty or "SPY" not in price_data.open.columns or not dates:
        return pd.DataFrame(columns=["date", "equity"])
    first = dates[0]
    start_px = float(price_data.open.loc[first, "SPY"])
    if start_px <= 0:
        return pd.DataFrame(columns=["date", "equity"])
    shares = STARTING_CASH / start_px
    rows = []
    for ts in dates:
        if ts in price_data.close.index and pd.notna(price_data.close.loc[ts, "SPY"]):
            rows.append({"date": ts.date().isoformat(), "equity": shares * float(price_data.close.loc[ts, "SPY"])})
    return pd.DataFrame(rows)


def _patch_price_only(algo, price_data: PriceData):
    def fake_fetch_prices(tickers: list, period: str = "2y") -> pd.DataFrame:
        return price_adapter_frame(price_data.close, tickers)

    patches = [patch("crazy.adapters.price_only.fetch_prices", fake_fetch_prices)]
    module = importlib.import_module(algo.__class__.__module__)
    if hasattr(module, "fetch_prices"):
        patches.append(patch(f"{algo.__class__.__module__}.fetch_prices", fake_fetch_prices))
    return patches


def _run_with_patches(patches, fn):
    if not patches:
        return fn()
    first, *rest = patches
    with first:
        return _run_with_patches(rest, fn)


def run_backtest(algo, family: str, start: str, end: str, slippage_bps: float = 5.0) -> BacktestResult:
    classification = classify_algo(algo, family)
    if not classification.backtestable:
        return BacktestResult(
            algo_id=algo.algo_id,
            name=algo.name,
            family=family,
            status=classification.status,
            reason=classification.reason,
            metrics={},
            trades=[],
            equity_curve=pd.DataFrame(columns=["date", "equity"]),
            spy_curve=pd.DataFrame(columns=["date", "equity"]),
        )

    universe = [str(t).upper() for t in algo.universe()]
    tickers = sorted(set(universe) | {"SPY"})
    price_data = download_price_data(tickers, start=start, end=end)
    dates = [d for d in price_data.close.index if pd.Timestamp(start) <= d <= pd.Timestamp(end)]
    if len(dates) < 40:
        return BacktestResult(algo.algo_id, algo.name, family, "INSUFFICIENT_DATA", "Not enough price history", {}, [], pd.DataFrame(), pd.DataFrame())

    state = default_state(dates[0].date())
    patches = _patch_price_only(algo, price_data) if family == "crazy" else []

    def simulate() -> BacktestResult:
        pending_target = None
        pending_signal = None
        for idx, ts in enumerate(dates):
            open_prices = _prices_on(price_data.open, ts, universe)
            close_prices = _prices_on(price_data.close, ts, universe)

            if pending_target is not None and open_prices:
                try:
                    _rebalance_to_target(state, pending_target, open_prices, ts, slippage_bps)
                except ValueError as exc:
                    return BacktestResult(algo.algo_id, algo.name, family, "UNSUPPORTED_SHORT", str(exc), {}, [], pd.DataFrame(), pd.DataFrame())
                meta = state.setdefault("meta", {}).setdefault(algo.algo_id, {})
                meta["last_signal"] = pending_signal or "TARGET"
                pending_target = None
                pending_signal = None

            _snapshot(state, ts, close_prices)

            if idx >= len(dates) - 1:
                continue

            as_of = ts.date()
            target = None
            signal_key = None
            if family == "normal":
                eom = _is_month_end(ts, dates)
                if algo.should_rebalance(as_of, eom):
                    close_slice = price_data.close.loc[:ts, tickers].dropna(how="all")
                    if hasattr(algo, "__dict__"):
                        algo.__dict__["_state_ref"] = state
                    target = algo.compute_target(close_slice, as_of)
                    signal_key = ",".join(sorted(target.keys())) if target else "CASH"
            else:
                signal = algo.compute_signal(as_of, state, historical=True)
                meta = algo.meta(state)
                signal_key = meta.get("signal_key") or meta.get("signal_label") or signal
                if algo.should_rebalance(as_of, state, signal_key):
                    target = algo.target_allocations(signal, state, as_of)

            if target is not None:
                pending_target = target
                pending_signal = signal_key

        equity_curve = pd.DataFrame(state["daily_snapshots"])[["date", "equity"]]
        trades = state["trade_log"]
        spy = _spy_curve(price_data, dates)
        metrics = compute_metrics(equity_curve, trades, spy)
        status = label_metrics(metrics)
        return BacktestResult(algo.algo_id, algo.name, family, status, "Backtest completed", metrics, trades, equity_curve, spy)

    return _run_with_patches(patches, simulate)
