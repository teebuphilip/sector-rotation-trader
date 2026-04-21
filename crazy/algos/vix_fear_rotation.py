import os

import pandas as pd

from crazy.adapters.fred_series import fetch_fred_series
from crazy.algos.base import CrazyAlgoBase
from crazy.blocked import record_blocked


class VixFearRotationAlgo(CrazyAlgoBase):
    algo_id = "vix-fear-rotation"
    name = "VIX Fear Rotation"
    family = "attention_sentiment"
    rebalance_frequency = "daily"
    supports_historical_seed = True

    SERIES_ID = "VIXCLS"
    FEAR_THRESHOLD = 25.0
    CALM_THRESHOLD = 18.0

    def universe(self):
        return ["XLP", "XLU", "XLV", "XLK", "XLY", "XLF"]

    def compute_signal(self, as_of, state, historical=False):
        api_key = os.getenv("FRED_API_KEY")
        if not api_key:
            record_blocked(self.algo_id, self.name, ["FRED_API_KEY"], "Missing FRED_API_KEY")
            return "HOLD"

        df = fetch_fred_series(self.SERIES_ID, api_key)
        if df.empty:
            return "HOLD"

        df = df.sort_values("date").copy()
        df["date"] = pd.to_datetime(df["date"])
        df = df[df["date"] <= pd.Timestamp(as_of)]
        if df.empty:
            return "HOLD"

        latest_vix = float(df.iloc[-1]["value"])
        meta = self.meta(state)
        meta["vix"] = round(latest_vix, 2)

        if latest_vix >= self.FEAR_THRESHOLD:
            meta["signal_label"] = "HIGH_FEAR"
            return "HIGH_FEAR"
        if latest_vix <= self.CALM_THRESHOLD:
            meta["signal_label"] = "LOW_FEAR"
            return "LOW_FEAR"

        meta["signal_label"] = "HOLD"
        return "HOLD"

    def target_allocations(self, signal, state, as_of):
        if signal == "HIGH_FEAR":
            return {"XLP": 0.40, "XLU": 0.35, "XLV": 0.25}
        if signal == "LOW_FEAR":
            return {"XLK": 0.40, "XLY": 0.35, "XLF": 0.25}
        return None
