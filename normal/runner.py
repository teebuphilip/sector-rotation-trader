import argparse
from datetime import date
import os

import pandas as pd

from scanner import safe_download
from portfolio import (
    load_state_from, save_state_to, save_trade_log_to,
    open_position, close_position, snapshot, total_equity, compute_analytics
)
from dashboard import generate_dashboard
from normal.algos import get_normal_algos
from normal.ledger import write_normal_ledger
import subprocess


def is_month_end(d: date) -> bool:
    return (pd.Timestamp(d) + pd.tseries.offsets.BMonthEnd(0)).date() == d


def rebalance_to_target(state: dict, target: dict, prices: dict):
    for ticker in list(state["positions"].keys()):
        price = prices.get(ticker)
        if price is None:
            continue
        close_position(state, ticker, price, reason="rebalance")

    equity = total_equity(state, prices)
    for ticker, weight in target.items():
        if weight <= 0:
            continue
        price = prices.get(ticker)
        if price is None or price <= 0:
            continue
        amount = equity * weight
        if amount <= 0:
            continue
        if state["cash"] >= amount:
            open_position(state, ticker, price, amount, using_margin=False)


def run_all(dry_run: bool = False, as_of: date = None):
    as_of = as_of or date.today()
    eom = is_month_end(as_of)

    algos = get_normal_algos()

    all_tickers = sorted({t for algo in algos for t in algo.universe()})
    prices = {}
    prices_df = pd.DataFrame()
    if all_tickers:
        raw = safe_download(all_tickers, period="2y")
        if not raw.empty:
            prices_df = raw["Close"] if "Close" in raw.columns else raw
            for t in prices_df.columns:
                s = prices_df[t].dropna()
                if len(s):
                    prices[t] = float(s.iloc[-1])

    for algo in algos:
        state_path = os.path.join("data/normal/state", f"{algo.algo_id}.json")
        trade_log_path = os.path.join("docs/normal", algo.algo_id, "trades.json")
        dashboard_path = os.path.join("docs/normal", algo.algo_id, "index.html")

        state = load_state_from(state_path)
        state.setdefault("meta", {})

        target = {}
        if not prices_df.empty and algo.should_rebalance(as_of, eom):
            if hasattr(algo, "__dict__"):
                algo.__dict__["_state_ref"] = state
            target = algo.compute_target(prices_df, as_of)
            if target is not None:
                rebalance_to_target(state, target, prices)

        state["meta"][algo.algo_id] = {
            "name": algo.name,
            "last_run": as_of.isoformat(),
            "last_signal": ",".join(sorted(target.keys())) if target else "CASH",
        }

        snapshot(state, prices, algo.name)

        if not dry_run:
            save_state_to(state, state_path)
            save_trade_log_to(state, trade_log_path)

        analytics = compute_analytics(state)
        if not dry_run:
            generate_dashboard(
                state,
                prices,
                algo.name,
                analytics=analytics,
                output_path=dashboard_path,
                strategy_label="Strategy",
                strategy_value=algo.name,
                title=f"Normal Algo | {algo.name}",
            )

    if not dry_run:
        write_normal_ledger()
        subprocess.run(["python", "scripts/rolling_30d_leaderboard.py"], check=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    run_all(dry_run=args.dry_run)
