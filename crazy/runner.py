import argparse
from datetime import date
import os

from scanner import safe_download
from portfolio import (
    load_state_from, save_state_to, save_trade_log_to,
    open_position, close_position, snapshot, total_equity, compute_analytics
)
from dashboard import generate_dashboard
from crazy.algos import get_crazy_algos
from crazy.config import CRAZY_STATE_DIR, CRAZY_DASHBOARD_DIR, CRAZY_LOG_DIR
from crazy.combined_dashboard import generate_combined_dashboard
from crazy.ledger import write_crazy_ledger
from crazy.seed import seed_algos
import subprocess


def ensure_state(state: dict):
    state.setdefault("meta", {})
    return state


def rebalance_to_target(state: dict, target: dict, prices: dict):
    # Full rebalance: sell everything, then rebuild
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

    algos = get_crazy_algos()
    summaries = []
    if not dry_run:
        to_seed = []
        for algo in algos:
            state_path = os.path.join(CRAZY_STATE_DIR, f"{algo.algo_id}.json")
            if not os.path.exists(state_path):
                to_seed.append(algo)
        if to_seed:
            names = ", ".join(a.name for a in to_seed)
            print(f"Seeding new crazy algos: {names}")
            seed_algos(to_seed)

    for algo in algos:
        state_path = os.path.join(CRAZY_STATE_DIR, f"{algo.algo_id}.json")
        trade_log_path = os.path.join(CRAZY_LOG_DIR, algo.algo_id, "trades.json")
        dashboard_path = os.path.join(CRAZY_DASHBOARD_DIR, algo.algo_id, "index.html")

        state = ensure_state(load_state_from(state_path))

        tickers = algo.universe()
        prices = {}
        if tickers:
            raw = safe_download(tickers, period="1y")
            if not raw.empty:
                prices_df = raw["Close"] if "Close" in raw.columns else raw
                for t in prices_df.columns:
                    s = prices_df[t].dropna()
                    if len(s):
                        prices[t] = float(s.iloc[-1])

        signal = algo.compute_signal(as_of, state, historical=False)
        meta = algo.meta(state)
        signal_key = meta.get("signal_key", signal)
        signal_label = meta.get("signal_label", signal)
        target = algo.target_allocations(signal, state, as_of)

        if target is not None and prices:
            if algo.should_rebalance(as_of, state, signal_key):
                rebalance_to_target(state, target, prices)

        meta["name"] = algo.name
        meta["last_signal"] = signal_key
        meta["last_run"] = as_of.isoformat()

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
                title=f"Crazy Algo | {algo.name}",
            )

        equity = state["daily_snapshots"][-1]["equity"] if state["daily_snapshots"] else state["cash"]
        summaries.append({
            "algo_id": algo.algo_id,
            "name": algo.name,
            "equity": equity,
            "net_pnl": equity - 100_000,
            "sharpe": analytics.get("sharpe", 0.0),
            "max_drawdown_pct": analytics.get("max_drawdown_pct", 0.0),
            "last_signal": signal_label,
        })

    if not dry_run:
        generate_combined_dashboard(summaries)
        write_crazy_ledger()
        subprocess.run(["python", "scripts/rolling_30d_leaderboard.py"], check=False)
        subprocess.run(["python", "scripts/update_algos_index.py"], check=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    run_all(dry_run=args.dry_run)
