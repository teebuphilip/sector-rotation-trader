import os

import pandas as pd

from crazy.adapters.fred_series import fetch_fred_series
from crazy.algos.base import CrazyAlgoBase
from crazy.blocked import record_blocked


class FreightRailCarloadsAlgo(CrazyAlgoBase):
    algo_id = "freight-rail-carloads"
    name = "Freight Rail Carloads"
    rebalance_frequency = "monthly"
    supports_historical_seed = False

    SERIES_ID = "RAILFRTCARLOADSD11"
    BULL_13W = 0.02
    BEAR_13W = -0.02

    def universe(self):
        return ["XLI", "XLB", "XLE", "XLP", "XLU", "XLV"]

    def compute_signal(self, as_of, state, historical=False):
        api_key = os.getenv("FRED_API_KEY")
        if not api_key:
            record_blocked(self.algo_id, self.name, ["FRED_API_KEY"], "Missing FRED_API_KEY")
            return "HOLD"

        df = fetch_fred_series(self.SERIES_ID, api_key)
        if df.empty or len(df) < 20:
            return "HOLD"

        df = df.sort_values("date").copy()
        df["chg_13w"] = df["value"].pct_change(13)
        df = df.dropna()
        if df.empty:
            return "HOLD"

        latest = df.iloc[-1]
        chg = float(latest["chg_13w"])
        meta = self.meta(state)
        meta["series_id"] = self.SERIES_ID
        meta["rail_13w_chg"] = round(chg, 4)

        if chg > self.BULL_13W:
            meta["signal_label"] = "INDUSTRIAL_SHIFT"
            meta["signal_key"] = "INDUSTRIAL_SHIFT"
            return "INDUSTRIAL_SHIFT"
        if chg < self.BEAR_13W:
            meta["signal_label"] = "CONSUMER_DEFENSIVE_SHIFT"
            meta["signal_key"] = "CONSUMER_DEFENSIVE_SHIFT"
            return "CONSUMER_DEFENSIVE_SHIFT"

        meta["signal_label"] = "HOLD"
        meta["signal_key"] = "HOLD"
        return "HOLD"

    def target_allocations(self, signal, state, as_of):
        if signal == "INDUSTRIAL_SHIFT":
            return {"XLI": 0.45, "XLB": 0.35, "XLE": 0.20}
        if signal == "CONSUMER_DEFENSIVE_SHIFT":
            return {"XLP": 0.40, "XLU": 0.30, "XLV": 0.30}
        return None
