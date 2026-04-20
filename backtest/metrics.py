from __future__ import annotations

import math
from typing import Any

import pandas as pd


def _max_drawdown(equity: pd.Series) -> float:
    if equity.empty:
        return 0.0
    peak = equity.cummax()
    dd = equity / peak - 1.0
    return float(dd.min())


def _sharpe(equity: pd.Series) -> float:
    if len(equity) < 3:
        return 0.0
    returns = equity.pct_change().dropna()
    std = returns.std()
    if std == 0 or pd.isna(std):
        return 0.0
    excess = returns.mean() - (0.045 / 252)
    return float(excess / std * math.sqrt(252))


def compute_metrics(equity_curve: pd.DataFrame, trades: list[dict[str, Any]], spy_curve: pd.DataFrame) -> dict[str, Any]:
    if equity_curve.empty or "equity" not in equity_curve.columns:
        return {
            "status": "INSUFFICIENT_DATA",
            "total_return_pct": 0.0,
            "spy_return_pct": 0.0,
            "alpha_vs_spy_pct": 0.0,
            "max_drawdown_pct": 0.0,
            "spy_max_drawdown_pct": 0.0,
            "sharpe": 0.0,
            "trade_count": 0,
            "win_rate_pct": 0.0,
            "turnover": 0.0,
        }

    eq = pd.to_numeric(equity_curve["equity"], errors="coerce").dropna()
    total_return = float(eq.iloc[-1] / eq.iloc[0] - 1.0) if len(eq) >= 2 and eq.iloc[0] > 0 else 0.0

    spy = pd.to_numeric(spy_curve.get("equity", pd.Series(dtype=float)), errors="coerce").dropna()
    spy_return = float(spy.iloc[-1] / spy.iloc[0] - 1.0) if len(spy) >= 2 and spy.iloc[0] > 0 else 0.0

    sells = [t for t in trades if t.get("action") == "SELL"]
    wins = [t for t in sells if float(t.get("pnl", 0) or 0) > 0]
    total_trade_value = sum(float(t.get("notional", 0) or 0) for t in trades)
    start_equity = float(eq.iloc[0]) if len(eq) else 100_000.0

    return {
        "total_return_pct": round(total_return * 100, 2),
        "spy_return_pct": round(spy_return * 100, 2),
        "alpha_vs_spy_pct": round((total_return - spy_return) * 100, 2),
        "max_drawdown_pct": round(_max_drawdown(eq) * 100, 2),
        "spy_max_drawdown_pct": round(_max_drawdown(spy) * 100, 2),
        "sharpe": round(_sharpe(eq), 2),
        "spy_sharpe": round(_sharpe(spy), 2),
        "trade_count": len(trades),
        "sell_count": len(sells),
        "win_rate_pct": round((len(wins) / len(sells) * 100), 2) if sells else 0.0,
        "turnover": round(total_trade_value / start_equity, 4) if start_equity > 0 else 0.0,
    }


def label(metrics: dict[str, Any]) -> str:
    trades = int(metrics.get("trade_count") or 0)
    if trades < 3:
        return "INSUFFICIENT_ACTIVITY"
    alpha = float(metrics.get("alpha_vs_spy_pct") or 0.0)
    ret = float(metrics.get("total_return_pct") or 0.0)
    dd = float(metrics.get("max_drawdown_pct") or 0.0)
    spy_dd = float(metrics.get("spy_max_drawdown_pct") or 0.0)
    if ret < 0:
        return "BACKTEST_FAIL"
    if alpha > 0 and dd >= (spy_dd - 10.0):
        return "BACKTEST_PASS"
    if ret > 0:
        return "BACKTEST_WEAK"
    return "BACKTEST_FAIL"
