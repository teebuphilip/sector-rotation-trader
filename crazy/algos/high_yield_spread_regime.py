import os

import pandas as pd

from crazy.adapters.fred_series import fetch_fred_series
from crazy.algos.base import CrazyAlgoBase
from crazy.blocked import record_blocked


class HighYieldSpreadRegimeAlgo(CrazyAlgoBase):
    algo_id = "high-yield-spread-regime"
    name = "High Yield Spread Regime"
    rebalance_frequency = "monthly"
    supports_historical_seed = False

    SERIES_ID = "BAMLH0A0HYM2"
    TIGHTENING_3M = -0.40
    WIDENING_3M = 0.40

    def universe(self):
        return ["XLF", "XLY", "XLI", "XLP", "XLU", "XLV"]

    def compute_signal(self, as_of, state, historical=False):
        api_key = os.getenv("FRED_API_KEY")
        if not api_key:
            record_blocked(self.algo_id, self.name, ["FRED_API_KEY"], "Missing FRED_API_KEY")
            return "HOLD"

        df = fetch_fred_series(self.SERIES_ID, api_key)
        if df.empty or len(df) < 90:
            return "HOLD"

        df = df.sort_values("date").copy()
        df["delta_63d"] = df["value"].diff(63)
        df = df.dropna()
        if df.empty:
            return "HOLD"

        latest = df.iloc[-1]
        level = float(latest["value"])
        delta = float(latest["delta_63d"])
        meta = self.meta(state)
        meta["series_id"] = self.SERIES_ID
        meta["spread_level"] = round(level, 3)
        meta["spread_delta_63d"] = round(delta, 3)

        if delta < self.TIGHTENING_3M:
            meta["signal_label"] = "CREDIT_RISK_ON"
            meta["signal_key"] = "CREDIT_RISK_ON"
            return "CREDIT_RISK_ON"
        if delta > self.WIDENING_3M:
            meta["signal_label"] = "CREDIT_STRESS"
            meta["signal_key"] = "CREDIT_STRESS"
            return "CREDIT_STRESS"

        meta["signal_label"] = "HOLD"
        meta["signal_key"] = "HOLD"
        return "HOLD"

    def target_allocations(self, signal, state, as_of):
        if signal == "CREDIT_RISK_ON":
            return {"XLF": 0.40, "XLY": 0.35, "XLI": 0.25}
        if signal == "CREDIT_STRESS":
            return {"XLP": 0.40, "XLU": 0.30, "XLV": 0.30}
        return None
