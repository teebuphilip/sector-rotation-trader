from datetime import date, timedelta
import os
from typing import List, Optional

import pandas as pd

from config import SEED_DAYS
from scanner import safe_download
from portfolio import load_state_from, save_state_to, save_trade_log_to, snapshot, total_equity, open_position, close_position
from normal.algos import get_normal_algos


def is_month_end(d: date) -> bool:
    return (pd.Timestamp(d) + pd.tseries.offsets.BMonthEnd(0)).date() == d


def rebalance_to_target(state: dict, target: dict, prices: dict, as_of=None):
    for ticker in list(state["positions"].keys()):
        price = prices.get(ticker)
        if price is None:
            continue
        close_position(state, ticker, price, reason="rebalance", as_of=as_of)

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
            open_position(state, ticker, price, amount, using_margin=False, as_of=as_of)


def seed_algos(algos):
    if not algos:
        return
    end_date = date.today() - timedelta(days=1)
    start_date = end_date - timedelta(days=SEED_DAYS)
    trading_days = pd.bdate_range(start=start_date, end=end_date)

    all_tickers = sorted({t for algo in algos for t in algo.universe()})

    prices_raw = safe_download(all_tickers, period="2y")
    if prices_raw.empty:
        print("✖ Failed to download price data for seeding.")
        return

    prices_df = prices_raw["Close"] if "Close" in prices_raw.columns else prices_raw
    available_tickers = set(prices_df.columns)

    for algo in algos:
        state_path = os.path.join("data/normal/state", f"{algo.algo_id}.json")
        trade_log_path = os.path.join("docs/normal", algo.algo_id, "trades.json")

        state = load_state_from(state_path)
        state["cash"] = 100_000
        state["positions"] = {}
        state["trade_log"] = []
        state["daily_snapshots"] = []
        state["borrowed"] = 0.0
        state["accrued_interest"] = 0.0
        state["sim_start"] = start_date.isoformat()
        state.setdefault("meta", {})

        algo_tickers = [t for t in algo.universe() if t in available_tickers]
        if not algo_tickers:
            for dt in trading_days:
                snapshot(state, {}, algo.name, as_of=dt.date())
            save_state_to(state, state_path)
            save_trade_log_to(state, trade_log_path)
            missing = [t for t in algo.universe() if t not in available_tickers]
            print(f"Seeded {algo.name} with flat cash history (no available price data). Missing: {missing}")
            continue

        for dt in trading_days:
            current_prices = {}
            for t in algo_tickers:
                if t in prices_df.columns:
                    s = prices_df[t].loc[prices_df.index <= dt].dropna()
                    if len(s):
                        current_prices[t] = float(s.iloc[-1])

            eom = is_month_end(dt.date())
            if algo.should_rebalance(dt.date(), eom):
                if hasattr(algo, "__dict__"):
                    algo.__dict__["_state_ref"] = state
                target = algo.compute_target(prices_df.loc[:dt], dt.date())
                if target is not None:
                    rebalance_to_target(state, target, current_prices, as_of=dt.date())

            snapshot(state, current_prices, algo.name, as_of=dt.date())

        save_state_to(state, state_path)
        save_trade_log_to(state, trade_log_path)
        print(f"Seeded {algo.name}.")


def _normalize_key(value: str) -> str:
    return value.strip().lower().replace("_", "-")


def _filter_algos(algos, algo_ids: Optional[List[str]]):
    if not algo_ids:
        return algos
    wanted = {_normalize_key(a) for a in algo_ids}
    filtered = []
    for algo in algos:
        keys = {
            _normalize_key(algo.algo_id),
            _normalize_key(algo.name),
            _normalize_key(algo.__class__.__name__),
        }
        if keys & wanted:
            filtered.append(algo)
    return filtered


def seed_all(algo_ids: Optional[List[str]] = None):
    algos = _filter_algos(get_normal_algos(), algo_ids)
    if not algos:
        print("✖ No matching normal algos found to seed.")
        return
    seed_algos(algos)


if __name__ == "__main__":
    seed_all()
