import os

import pandas as pd

from crazy.adapters.fred_series import fetch_fred_series
from crazy.algos.base import CrazyAlgoBase
from crazy.blocked import record_blocked


class CopperMomentumAlgo(CrazyAlgoBase):
    algo_id = "copper-momentum"
    name = "Copper Momentum"
    rebalance_frequency = "monthly"
    supports_historical_seed = False

    SERIES_ID = "PCOPPUSDM"
    BULL_3M = 0.06
    BEAR_3M = -0.06

    def universe(self):
        return ["XLB", "XLI", "XLE", "XLP", "XLU", "XLV"]

    def compute_signal(self, as_of, state, historical=False):
        api_key = os.getenv("FRED_API_KEY")
        if not api_key:
            record_blocked(self.algo_id, self.name, ["FRED_API_KEY"], "Missing FRED_API_KEY")
            return "HOLD"

        df = fetch_fred_series(self.SERIES_ID, api_key)
        if df.empty or len(df) < 8:
            return "HOLD"

        df = df.sort_values("date").copy()
        df["chg_3m"] = df["value"].pct_change(3)
        df = df.dropna()
        if df.empty:
            return "HOLD"

        latest = df.iloc[-1]
        chg = float(latest["chg_3m"])
        meta = self.meta(state)
        meta["series_id"] = self.SERIES_ID
        meta["copper_3m_chg"] = round(chg, 4)

        if chg > self.BULL_3M:
            meta["signal_label"] = "GLOBAL_GROWTH"
            meta["signal_key"] = "GLOBAL_GROWTH"
            return "GLOBAL_GROWTH"
        if chg < self.BEAR_3M:
            meta["signal_label"] = "GROWTH_SCARE"
            meta["signal_key"] = "GROWTH_SCARE"
            return "GROWTH_SCARE"

        meta["signal_label"] = "HOLD"
        meta["signal_key"] = "HOLD"
        return "HOLD"

    def target_allocations(self, signal, state, as_of):
        if signal == "GLOBAL_GROWTH":
            return {"XLB": 0.45, "XLI": 0.35, "XLE": 0.20}
        if signal == "GROWTH_SCARE":
            return {"XLP": 0.40, "XLU": 0.30, "XLV": 0.30}
        return None
