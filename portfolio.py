"""
portfolio.py — Portfolio state management: cash, margin, positions, P&L
"""
import json
import os
from datetime import date, datetime
from config import (
    STARTING_CASH, MAX_POSITION_SIZE, MAX_BORROW,
    BORROW_RATE_ANNUAL, STATE_FILE, LOG_FILE
)

DAILY_BORROW_RATE = BORROW_RATE_ANNUAL / 365.0


def _today():
    return date.today().isoformat()


def load_state() -> dict:
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            return json.load(f)
    return _default_state()


def save_state(state: dict):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2, default=str)


def _default_state() -> dict:
    return {
        "cash":            STARTING_CASH,
        "borrowed":        0.0,
        "accrued_interest":0.0,
        "positions":       {},   # ticker -> {shares, entry_price, entry_date, consec_below_ma, cost}
        "trade_log":       [],
        "daily_snapshots": [],
        "sim_start":       _today(),
        "last_run":        None,
    }


def available_cash(state: dict) -> float:
    return state["cash"]


def can_borrow(state: dict, amount: float) -> bool:
    return (state["borrowed"] + amount) <= MAX_BORROW


def total_equity(state: dict, current_prices: dict) -> float:
    """Cash + market value of all positions - borrowed."""
    pos_value = sum(
        pos["shares"] * current_prices.get(ticker, pos["entry_price"])
        for ticker, pos in state["positions"].items()
    )
    return state["cash"] + pos_value - state["borrowed"] - state["accrued_interest"]


def open_position(state: dict, ticker: str, price: float, amount: float, using_margin: bool = False):
    """Buy $amount worth of ticker at price."""
    shares = amount / price
    cost   = amount

    if using_margin:
        state["borrowed"] += cost
    else:
        state["cash"] -= cost

    state["positions"][ticker] = {
        "shares":         shares,
        "entry_price":    price,
        "entry_date":     _today(),
        "cost":           cost,
        "using_margin":   using_margin,
        "consec_below_ma":0,
    }

    state["trade_log"].append({
        "date":          _today(),
        "action":        "BUY",
        "ticker":        ticker,
        "shares":        round(shares, 4),
        "price":         round(price, 4),
        "cost":          round(cost, 2),
        "margin":        using_margin,
    })


def close_position(state: dict, ticker: str, price: float, reason: str = "exit_signal"):
    """Sell position at price, settle cash/margin."""
    if ticker not in state["positions"]:
        return

    pos      = state["positions"][ticker]
    proceeds = pos["shares"] * price
    cost     = pos["cost"]
    pnl      = proceeds - cost

    if pos["using_margin"]:
        # Pay back principal from proceeds
        repay          = min(pos["cost"], proceeds)
        state["borrowed"] = max(0, state["borrowed"] - repay)
        state["cash"]  += max(0, proceeds - repay)
    else:
        state["cash"]  += proceeds

    state["trade_log"].append({
        "date":          _today(),
        "action":        "SELL",
        "ticker":        ticker,
        "shares":        round(pos["shares"], 4),
        "price":         round(price, 4),
        "proceeds":      round(proceeds, 2),
        "pnl":           round(pnl, 2),
        "pnl_pct":       round((pnl / cost) * 100, 2),
        "entry_date":    pos["entry_date"],
        "reason":        reason,
    })

    del state["positions"][ticker]


def accrue_interest(state: dict):
    """Daily margin interest accrual."""
    if state["borrowed"] > 0:
        daily_interest          = state["borrowed"] * DAILY_BORROW_RATE
        state["accrued_interest"] += daily_interest


def snapshot(state: dict, current_prices: dict, sector: str):
    """Record daily portfolio snapshot."""
    pos_details = {}
    for ticker, pos in state["positions"].items():
        px = current_prices.get(ticker, pos["entry_price"])
        pos_details[ticker] = {
            "shares":      round(pos["shares"], 4),
            "entry_price": round(pos["entry_price"], 4),
            "current_price": round(px, 4),
            "market_value":  round(pos["shares"] * px, 2),
            "unrealized_pnl": round((px - pos["entry_price"]) * pos["shares"], 2),
            "entry_date":  pos["entry_date"],
            "margin":      pos["using_margin"],
        }

    equity = total_equity(state, current_prices)

    state["daily_snapshots"].append({
        "date":      _today(),
        "cash":      round(state["cash"], 2),
        "borrowed":  round(state["borrowed"], 2),
        "interest":  round(state["accrued_interest"], 2),
        "equity":    round(equity, 2),
        "positions": pos_details,
        "sector":    sector,
        "num_positions": len(state["positions"]),
    })

    state["last_run"] = _today()


def save_trade_log(state: dict):
    """Write trade log to docs/trades.json for dashboard."""
    os.makedirs("docs", exist_ok=True)
    with open(LOG_FILE, "w") as f:
        json.dump({
            "trade_log":       state["trade_log"],
            "daily_snapshots": state["daily_snapshots"],
            "sim_start":       state["sim_start"],
        }, f, indent=2, default=str)
