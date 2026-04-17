import os

import pandas as pd

from crazy.adapters.fred_series import fetch_fred_series
from crazy.algos.base import CrazyAlgoBase
from crazy.blocked import record_blocked


class MortgageRateHousingProxyAlgo(CrazyAlgoBase):
    algo_id = "mortgage-rate-housing-proxy"
    name = "Mortgage Rate Housing Proxy"
    rebalance_frequency = "monthly"
    supports_historical_seed = False

    SERIES_ID = "MORTGAGE30US"
    RATE_DROP_BULL = -0.25
    RATE_RISE_BEAR = 0.25

    def universe(self):
        return ["XLRE", "XLF", "XLB", "XLP", "XLU", "XLV"]

    def compute_signal(self, as_of, state, historical=False):
        api_key = os.getenv("FRED_API_KEY")
        if not api_key:
            record_blocked(self.algo_id, self.name, ["FRED_API_KEY"], "Missing FRED_API_KEY")
            return "HOLD"

        df = fetch_fred_series(self.SERIES_ID, api_key)
        if df.empty or len(df) < 12:
            return "HOLD"

        df = df.sort_values("date").copy()
        df["delta_8w"] = df["value"].diff(8)
        df = df.dropna()
        if df.empty:
            return "HOLD"

        latest = df.iloc[-1]
        delta = float(latest["delta_8w"])
        meta = self.meta(state)
        meta["series_id"] = self.SERIES_ID
        meta["mortgage_rate"] = round(float(latest["value"]), 3)
        meta["rate_delta_8w"] = round(delta, 3)

        if delta < self.RATE_DROP_BULL:
            meta["signal_label"] = "HOUSING_TAILWIND"
            meta["signal_key"] = "HOUSING_TAILWIND"
            return "HOUSING_TAILWIND"
        if delta > self.RATE_RISE_BEAR:
            meta["signal_label"] = "HOUSING_HEADWIND"
            meta["signal_key"] = "HOUSING_HEADWIND"
            return "HOUSING_HEADWIND"

        meta["signal_label"] = "HOLD"
        meta["signal_key"] = "HOLD"
        return "HOLD"

    def target_allocations(self, signal, state, as_of):
        if signal == "HOUSING_TAILWIND":
            return {"XLRE": 0.40, "XLF": 0.30, "XLB": 0.30}
        if signal == "HOUSING_HEADWIND":
            return {"XLP": 0.40, "XLU": 0.30, "XLV": 0.30}
        return None
