import os

import pandas as pd

from crazy.adapters.fred_series import fetch_fred_series
from crazy.algos.base import CrazyAlgoBase
from crazy.blocked import record_blocked


class VixTermStructureAlgo(CrazyAlgoBase):
    """
    VIX/VXV ratio signal. VXV is the CBOE 3-month vol index.
    Ratio > 1 (backwardation) = near-term fear spike = defensive.
    Ratio < 0.88 (steep contango) = calm/complacent = risk-on.
    """
    algo_id = "vix-term-structure"
    name = "VIX Term Structure"
    family = "attention_sentiment"
    rebalance_frequency = "daily"
    supports_historical_seed = True

    BACKWARDATION_THRESHOLD = 1.0
    CONTANGO_THRESHOLD = 0.88

    def universe(self):
        return ["XLP", "XLU", "XLV", "XLK", "XLY", "XLF"]

    def compute_signal(self, as_of, state, historical=False):
        api_key = os.getenv("FRED_API_KEY")
        if not api_key:
            record_blocked(self.algo_id, self.name, ["FRED_API_KEY"], "Missing FRED_API_KEY")
            return "HOLD"

        vix_df = fetch_fred_series("VIXCLS", api_key)
        vxv_df = fetch_fred_series("VXVCLS", api_key)

        if vix_df.empty or vxv_df.empty:
            return "HOLD"

        for df in (vix_df, vxv_df):
            df["date"] = pd.to_datetime(df["date"])

        as_of_ts = pd.Timestamp(as_of)
        vix_df = vix_df[vix_df["date"] <= as_of_ts].sort_values("date")
        vxv_df = vxv_df[vxv_df["date"] <= as_of_ts].sort_values("date")

        if vix_df.empty or vxv_df.empty:
            return "HOLD"

        vix = float(vix_df.iloc[-1]["value"])
        vxv = float(vxv_df.iloc[-1]["value"])

        if vxv == 0:
            return "HOLD"

        ratio = vix / vxv
        meta = self.meta(state)
        meta["vix"] = round(vix, 2)
        meta["vxv"] = round(vxv, 2)
        meta["ratio"] = round(ratio, 4)

        if ratio >= self.BACKWARDATION_THRESHOLD:
            meta["signal_label"] = "BACKWARDATION"
            return "BACKWARDATION"
        if ratio <= self.CONTANGO_THRESHOLD:
            meta["signal_label"] = "STEEP_CONTANGO"
            return "STEEP_CONTANGO"

        meta["signal_label"] = "HOLD"
        return "HOLD"

    def target_allocations(self, signal, state, as_of):
        if signal == "BACKWARDATION":
            return {"XLP": 0.40, "XLU": 0.35, "XLV": 0.25}
        if signal == "STEEP_CONTANGO":
            return {"XLK": 0.40, "XLY": 0.35, "XLF": 0.25}
        return None
