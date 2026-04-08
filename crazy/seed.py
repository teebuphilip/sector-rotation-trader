from datetime import date, timedelta
import os

import pandas as pd

from config import SEED_DAYS
from scanner import safe_download
from portfolio import load_state_from, save_state_to, save_trade_log_to, snapshot, total_equity, open_position, close_position
from crazy.algos import get_crazy_algos
from crazy.config import CRAZY_STATE_DIR, CRAZY_LOG_DIR


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
        if state["cash"] >= amount:
            open_position(state, ticker, price, amount, using_margin=False)


def seed_all():
    end_date = date.today() - timedelta(days=1)
    start_date = end_date - timedelta(days=SEED_DAYS)
    trading_days = pd.bdate_range(start=start_date, end=end_date)

    algos = get_crazy_algos()
    all_tickers = sorted({t for algo in algos for t in algo.universe()})

    prices_raw = safe_download(all_tickers, period="2y")
    if prices_raw.empty:
        print("✖ Failed to download price data for seeding.")
        return

    prices_df = prices_raw["Close"] if "Close" in prices_raw.columns else prices_raw

    for algo in algos:
        state_path = os.path.join(CRAZY_STATE_DIR, f"{algo.algo_id}.json")
        trade_log_path = os.path.join(CRAZY_LOG_DIR, algo.algo_id, "trades.json")

        state = load_state_from(state_path)
        state["cash"] = 100_000
        state["positions"] = {}
        state["trade_log"] = []
        state["daily_snapshots"] = []
        state["borrowed"] = 0.0
        state["accrued_interest"] = 0.0
        state["sim_start"] = start_date.isoformat()
        state.setdefault("meta", {})

        if not algo.supports_historical_seed:
            for dt in trading_days:
                snapshot(state, {}, algo.name)
            save_state_to(state, state_path)
            save_trade_log_to(state, trade_log_path)
            print(f"Seeded {algo.name} with flat cash history (no historical data).")
            continue

        for dt in trading_days:
            current_prices = {}
            for t in algo.universe():
                if t in prices_df.columns:
                    s = prices_df[t].loc[prices_df.index <= dt].dropna()
                    if len(s):
                        current_prices[t] = float(s.iloc[-1])

            signal = algo.compute_signal(dt.date(), state, historical=True)
            target = algo.target_allocations(signal, state, dt.date())
            if target is not None and current_prices:
                if algo.should_rebalance(dt.date(), state, signal):
                    rebalance_to_target(state, target, current_prices)

            snapshot(state, current_prices, algo.name)

        save_state_to(state, state_path)
        save_trade_log_to(state, trade_log_path)
        print(f"Seeded {algo.name} with historical simulation.")


if __name__ == "__main__":
    seed_all()
