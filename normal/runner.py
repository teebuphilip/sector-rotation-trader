import argparse
from datetime import date
from pathlib import Path
import json
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
from normal.seed import seed_algos
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
    if not dry_run:
        to_seed = []
        for algo in algos:
            state_path = os.path.join("data/normal/state", f"{algo.algo_id}.json")
            if not os.path.exists(state_path):
                to_seed.append(algo)
        if to_seed:
            names = ", ".join(a.name for a in to_seed)
            print(f"Seeding new normal algos: {names}")
            seed_algos(to_seed)
            _log_new_algos("normal", to_seed, as_of)

    all_tickers = sorted({t for algo in algos for t in algo.universe()})
    prices = {}
    prices_df = pd.DataFrame()
    spy_prices = None
    if all_tickers:
        raw = safe_download(all_tickers, period="2y")
        if not raw.empty:
            prices_df = raw["Close"] if "Close" in raw.columns else raw
            for t in prices_df.columns:
                s = prices_df[t].dropna()
                if len(s):
                    prices[t] = float(s.iloc[-1])
    spy_raw = safe_download(["SPY"], period="2y")
    if not spy_raw.empty:
        spy_prices = spy_raw["Close"] if "Close" in spy_raw.columns else spy_raw

    for algo in algos:
        state_path = os.path.join("data/normal/state", f"{algo.algo_id}.json")
        trade_log_path = os.path.join("docs/normal", algo.algo_id, "trades.json")
        dashboard_path = os.path.join("docs/normal", algo.algo_id, "index.html")

        state = load_state_from(state_path)
        state.setdefault("meta", {})

        target = None
        rebalanced = False
        if not prices_df.empty and algo.should_rebalance(as_of, eom):
            if hasattr(algo, "__dict__"):
                algo.__dict__["_state_ref"] = state
            target = algo.compute_target(prices_df, as_of)
            if target is not None:
                rebalance_to_target(state, target, prices)
                rebalanced = True

        prev_meta = state["meta"].get(algo.algo_id, {}) or {}
        new_meta = {
            "name": algo.name,
            "last_run": as_of.isoformat(),
            "last_signal": prev_meta.get("last_signal", "CASH"),
        }
        if rebalanced:
            new_meta["last_signal"] = ",".join(sorted(target.keys())) if target else "CASH"
        state["meta"][algo.algo_id] = new_meta

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
                spy_prices=spy_prices,
                output_path=dashboard_path,
                strategy_label="Strategy",
                strategy_value=algo.name,
                title="StockArithm",
            )

    if not dry_run:
        write_normal_ledger()
        _run_post_script("scripts/rolling_30d_leaderboard.py")
        _run_post_script("scripts/update_algos_index.py")
        _run_post_script("scripts/build_product_index.py")


def _run_post_script(script: str):
    """Run a post-pipeline helper script. Logs failures loudly but does
    not abort the run — an index/leaderboard failure should not kill
    a trading pipeline that already committed state."""
    result = subprocess.run(
        ["python", script],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"[WARN] {script} exited {result.returncode}")
        if result.stdout:
            print(f"[WARN] {script} stdout:\n{result.stdout}")
        if result.stderr:
            print(f"[WARN] {script} stderr:\n{result.stderr}")
    else:
        if result.stdout:
            print(result.stdout, end="")


def _log_new_algos(category: str, algos: list, as_of: date):
    if not algos:
        return
    log_dir = Path("data/algos")
    log_dir.mkdir(parents=True, exist_ok=True)
    path = log_dir / "new_algos.jsonl"
    with path.open("a", encoding="utf-8") as f:
        for algo in algos:
            f.write(json.dumps({
                "date": as_of.isoformat(),
                "category": category,
                "algo_id": algo.algo_id,
                "name": algo.name,
            }) + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    run_all(dry_run=args.dry_run)
