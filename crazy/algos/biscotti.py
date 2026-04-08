from datetime import date

import pandas as pd

from config import SECTOR_ETFS
from scanner import safe_download
from .base import CrazyAlgoBase


class BiscottiAlgo(CrazyAlgoBase):
    algo_id = "biscotti"
    name = "Algo Biscotti (Unconditional Loyalty)"
    rebalance_frequency = "monthly_eom"
    supports_historical_seed = True

    def universe(self):
        return list(SECTOR_ETFS)

    def _is_month_end(self, as_of: date) -> bool:
        return (pd.Timestamp(as_of) + pd.tseries.offsets.BMonthEnd(0)).date() == as_of

    def should_rebalance(self, as_of: date, state: dict, signal: str) -> bool:
        return self._is_month_end(as_of)

    def compute_signal(self, as_of: date, state: dict, historical: bool = False):
        raw = safe_download(SECTOR_ETFS, period="3mo")
        if raw.empty:
            return "HOLD"
        prices = raw["Close"] if "Close" in raw.columns else raw
        prices = prices.dropna(how="all")
        if len(prices) < 31:
            return "HOLD"

        returns = prices.pct_change(30).iloc[-1].dropna()
        if returns.empty:
            return "HOLD"

        worst = returns.sort_values().index[0]
        meta = self.meta(state)
        meta["target_sector"] = worst
        meta["signal_label"] = f"BUY:{worst}"
        meta["signal_key"] = worst
        return "BISCOTTI"

    def target_allocations(self, signal: str, state: dict, as_of: date):
        if signal != "BISCOTTI":
            return None
        meta = self.meta(state)
        sector = meta.get("target_sector")
        if not sector:
            return None
        return {sector: 1.0}
