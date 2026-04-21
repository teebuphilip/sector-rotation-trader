"""
portfolio.py — Portfolio state management: cash, margin, positions, P&L
"""
import json
import os
import sys
from datetime import date, datetime
from config import (
    STARTING_CASH, MAX_POSITION_SIZE, MAX_BORROW,
    BORROW_RATE_ANNUAL, STATE_FILE, LOG_FILE,
    APPLY_FEES, COMMISSION_PER_TRADE, SEC_FEE_RATE, TAF_FEE_PER_SHARE,
    APPLY_TAXES, TAX_RATE_SHORT, TAX_RATE_LONG, TAX_LONG_TERM_DAYS
)

DAILY_BORROW_RATE = BORROW_RATE_ANNUAL / 365.0


def _today():
    return date.today().isoformat()


def _as_of_iso(as_of):
    """Normalize an as_of value to an ISO date string, defaulting to today."""
    if as_of is None:
        return _today()
    if isinstance(as_of, str):
        return as_of
    if hasattr(as_of, "isoformat"):
        # date or datetime
        return as_of.isoformat() if isinstance(as_of, date) else as_of.date().isoformat()
    return str(as_of)


def load_state() -> dict:
    return load_state_from(STATE_FILE)


def save_state(state: dict):
    save_state_to(state, STATE_FILE)


def load_state_from(path: str) -> dict:
    if os.path.exists(path):
        try:
            with open(path) as f:
                state = json.load(f)
            state.setdefault("fees_paid", 0.0)
            state.setdefault("taxes_paid", 0.0)
            state.setdefault("meta", {})
            return state
        except (json.JSONDecodeError, ValueError) as exc:
            print(f"  ✖ CRITICAL: {path} is corrupted ({exc}) — starting from default state.", file=sys.stderr)
    return _default_state()


def save_state_to(state: dict, path: str):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w") as f:
        json.dump(state, f, indent=2, default=str)


def _default_state() -> dict:
    return {
        "cash":            STARTING_CASH,
        "borrowed":        0.0,
        "accrued_interest":0.0,
        "fees_paid":       0.0,
        "taxes_paid":      0.0,
        "positions":       {},   # ticker -> {shares, entry_price, entry_date, consec_below_ma, cost}
        "trade_log":       [],
        "daily_snapshots": [],
        "sim_start":       _today(),
        "last_run":        None,
    }


def available_cash(state: dict) -> float:
    return max(0.0, state["cash"] - state["accrued_interest"])


def can_borrow(state: dict, amount: float) -> bool:
    return (state["borrowed"] + amount) <= MAX_BORROW


def total_equity(state: dict, current_prices: dict) -> float:
    """Cash + market value of all positions - borrowed."""
    pos_value = sum(
        pos["shares"] * current_prices.get(ticker, pos["entry_price"])
        for ticker, pos in state["positions"].items()
    )
    return state["cash"] + pos_value - state["borrowed"] - state["accrued_interest"]


def open_position(state: dict, ticker: str, price: float, amount: float, using_margin: bool = False, as_of=None):
    """Buy $amount worth of ticker at price."""
    # Reserve commission out of cash before sizing — otherwise a full-equity
    # target would overdraft cash by the commission amount.
    commission = COMMISSION_PER_TRADE if (APPLY_FEES and COMMISSION_PER_TRADE > 0) else 0.0
    if not using_margin and commission > 0:
        max_spend = state["cash"] - commission
        if max_spend <= 0:
            return
        if amount > max_spend:
            amount = max_spend

    if price <= 0:
        print(f"  ✖ CRITICAL: invalid price {price} for {ticker} — skipping open_position.", file=sys.stderr)
        return
    shares = amount / price
    cost   = amount

    if using_margin:
        state["borrowed"] += cost
    else:
        state["cash"] -= cost

    fees = 0.0
    if commission > 0:
        fees += commission
        state["cash"] -= commission
        state["fees_paid"] += commission

    as_of_iso = _as_of_iso(as_of)
    state["positions"][ticker] = {
        "shares":         shares,
        "entry_price":    price,
        "entry_date":     as_of_iso,
        "cost":           cost,
        "using_margin":   using_margin,
        "consec_below_ma":0,
    }

    state["trade_log"].append({
        "date":          as_of_iso,
        "action":        "BUY",
        "ticker":        ticker,
        "shares":        round(shares, 4),
        "price":         round(price, 4),
        "cost":          round(cost, 2),
        "margin":        using_margin,
        "fees":          round(fees, 2),
    })


def close_position(state: dict, ticker: str, price: float, reason: str = "exit_signal", as_of=None):
    """Sell position at price, settle cash/margin."""
    if ticker not in state["positions"]:
        return

    pos      = state["positions"][ticker]
    gross_proceeds = pos["shares"] * price
    cost     = pos["cost"]

    fees = 0.0
    if APPLY_FEES:
        if COMMISSION_PER_TRADE > 0:
            fees += COMMISSION_PER_TRADE
        if SEC_FEE_RATE > 0:
            fees += gross_proceeds * SEC_FEE_RATE
        if TAF_FEE_PER_SHARE > 0:
            fees += pos["shares"] * TAF_FEE_PER_SHARE

    proceeds = gross_proceeds - fees
    pnl      = proceeds - cost

    as_of_iso = _as_of_iso(as_of)
    try:
        as_of_dt = date.fromisoformat(as_of_iso)
    except Exception:
        as_of_dt = date.today()

    tax = 0.0
    if APPLY_TAXES and pnl > 0:
        try:
            entry_dt = datetime.fromisoformat(pos["entry_date"])
            hold_days = (as_of_dt - entry_dt.date()).days
        except Exception:
            hold_days = 0
        rate = TAX_RATE_LONG if hold_days >= TAX_LONG_TERM_DAYS else TAX_RATE_SHORT
        tax = pnl * rate

    if pos["using_margin"]:
        # When multiple margin positions close on the same day, allocate interest
        # against the opening borrowed/interest snapshot for that close batch so
        # settlement does not depend on close order.
        meta = state.setdefault("meta", {})
        batch = meta.get("margin_interest_batch")
        if not isinstance(batch, dict) or batch.get("date") != as_of_iso:
            batch = {
                "date": as_of_iso,
                "borrowed_base": float(state.get("borrowed", 0.0) or 0.0),
                "interest_base": float(state.get("accrued_interest", 0.0) or 0.0),
                "allocated": 0.0,
            }
            meta["margin_interest_batch"] = batch

        if batch.get("borrowed_base", 0.0) > 0 and batch.get("interest_base", 0.0) > 0 and state["accrued_interest"] > 0:
            ratio = min(float(pos["cost"]) / float(batch["borrowed_base"]), 1.0)
            target_share = float(batch["interest_base"]) * ratio
            remaining_batch_interest = max(0.0, float(batch["interest_base"]) - float(batch["allocated"]))
            interest_share = min(float(state["accrued_interest"]), remaining_batch_interest, target_share)
            proceeds -= interest_share
            state["accrued_interest"] = max(0.0, state["accrued_interest"] - interest_share)
            batch["allocated"] = float(batch.get("allocated", 0.0)) + interest_share

        # Repay borrowed principal fully — shortfall comes from cash
        principal = pos["cost"]
        if proceeds >= principal:
            state["borrowed"] = max(0, state["borrowed"] - principal)
            state["cash"] += proceeds - principal
        else:
            state["borrowed"] = max(0, state["borrowed"] - principal)
            shortfall = principal - proceeds
            state["cash"] -= shortfall  # loss hits cash
    else:
        state["cash"] += proceeds

    if fees > 0:
        state["fees_paid"] += fees

    if tax > 0:
        state["taxes_paid"] += tax
        state["cash"] -= tax
        pnl -= tax

    state["trade_log"].append({
        "date":          as_of_iso,
        "action":        "SELL",
        "ticker":        ticker,
        "shares":        round(pos["shares"], 4),
        "price":         round(price, 4),
        "proceeds":      round(proceeds, 2),
        "fees":          round(fees, 2),
        "tax":           round(tax, 2),
        "pnl":           round(pnl, 2),
        "pnl_pct":       round((pnl / cost) * 100, 2),
        "entry_date":    pos["entry_date"],
        "reason":        reason,
    })

    del state["positions"][ticker]

    batch = state.setdefault("meta", {}).get("margin_interest_batch")
    if isinstance(batch, dict):
        margin_positions_left = any(p.get("using_margin") for p in state["positions"].values())
        if batch.get("date") != as_of_iso or not margin_positions_left or state.get("borrowed", 0.0) <= 0:
            state["meta"].pop("margin_interest_batch", None)


def accrue_interest(state: dict):
    """Daily margin interest accrual."""
    if state["borrowed"] > 0:
        daily_interest          = state["borrowed"] * DAILY_BORROW_RATE
        state["accrued_interest"] += daily_interest


def snapshot(state: dict, current_prices: dict, sector: str, as_of=None):
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

    as_of_iso = _as_of_iso(as_of)
    state["daily_snapshots"].append({
        "date":      as_of_iso,
        "cash":      round(state["cash"], 2),
        "borrowed":  round(state["borrowed"], 2),
        "interest":  round(state["accrued_interest"], 2),
        "equity":    round(equity, 2),
        "positions": pos_details,
        "sector":    sector,
        "num_positions": len(state["positions"]),
    })

    state["last_run"] = as_of_iso


def compute_analytics(state: dict) -> dict:
    """Compute risk metrics from daily snapshots."""
    snaps = state.get("daily_snapshots", [])
    equities = [s["equity"] for s in snaps]

    if len(equities) < 2:
        return {"sharpe": 0.0, "max_drawdown_pct": 0.0, "avg_win": 0.0, "avg_loss": 0.0}

    # Daily returns
    returns = [(equities[i] - equities[i-1]) / equities[i-1]
               for i in range(1, len(equities)) if equities[i-1] > 0]

    # Sharpe (annualized, rf=4.5%)
    import numpy as np
    if returns and np.std(returns) > 0:
        excess = np.mean(returns) - (0.045 / 252)
        sharpe = float(excess / np.std(returns) * np.sqrt(252))
    else:
        sharpe = 0.0

    # Max drawdown
    peak = equities[0]
    max_dd = 0.0
    for eq in equities:
        if eq > peak:
            peak = eq
        dd = (eq - peak) / peak if peak > 0 else 0
        if dd < max_dd:
            max_dd = dd

    # Avg win / avg loss
    sells = [t for t in state["trade_log"] if t["action"] == "SELL"]
    wins  = [t["pnl"] for t in sells if t.get("pnl", 0) > 0]
    losses = [t["pnl"] for t in sells if t.get("pnl", 0) < 0]
    avg_win  = float(np.mean(wins)) if wins else 0.0
    avg_loss = float(np.mean(losses)) if losses else 0.0

    # Drawdown series for chart
    dd_series = []
    peak = equities[0]
    for i, eq in enumerate(equities):
        if eq > peak:
            peak = eq
        dd_pct = ((eq - peak) / peak * 100) if peak > 0 else 0
        dd_series.append(round(dd_pct, 2))

    return {
        "sharpe": round(sharpe, 2),
        "max_drawdown_pct": round(max_dd * 100, 2),
        "avg_win": round(avg_win, 2),
        "avg_loss": round(avg_loss, 2),
        "drawdown_series": dd_series,
    }


def save_trade_log(state: dict):
    save_trade_log_to(state, LOG_FILE)


def save_trade_log_to(state: dict, path: str):
    """Write trade log to a JSON file for dashboards."""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w") as f:
        json.dump({
            "trade_log":       state["trade_log"],
            "daily_snapshots": state["daily_snapshots"],
            "sim_start":       state["sim_start"],
        }, f, indent=2, default=str)
