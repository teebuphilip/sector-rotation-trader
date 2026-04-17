import os

import pandas as pd

from crazy.adapters.fred_series import fetch_fred_series
from crazy.algos.base import CrazyAlgoBase
from crazy.blocked import record_blocked


class YieldCurveRegimeAlgo(CrazyAlgoBase):
    algo_id = "yield-curve-regime"
    name = "Yield Curve Regime"
    rebalance_frequency = "monthly"
    supports_historical_seed = False

    SERIES_ID = "T10Y2Y"
    STEEPENING_3M = 0.25
    INVERSION_LEVEL = 0.0

    def universe(self):
        return ["XLF", "XLI", "XLY", "XLP", "XLU", "XLV"]

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
        meta["curve_level"] = round(level, 3)
        meta["curve_delta_63d"] = round(delta, 3)

        if level < self.INVERSION_LEVEL:
            meta["signal_label"] = "INVERTED_DEFENSIVE"
            meta["signal_key"] = "INVERTED_DEFENSIVE"
            return "INVERTED_DEFENSIVE"
        if delta > self.STEEPENING_3M:
            meta["signal_label"] = "STEEPENING_RISK_ON"
            meta["signal_key"] = "STEEPENING_RISK_ON"
            return "STEEPENING_RISK_ON"

        meta["signal_label"] = "HOLD"
        meta["signal_key"] = "HOLD"
        return "HOLD"

    def target_allocations(self, signal, state, as_of):
        if signal == "STEEPENING_RISK_ON":
            return {"XLF": 0.45, "XLI": 0.30, "XLY": 0.25}
        if signal == "INVERTED_DEFENSIVE":
            return {"XLP": 0.40, "XLU": 0.30, "XLV": 0.30}
        return None
