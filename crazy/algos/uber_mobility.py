import os
import warnings
from datetime import date

import pandas as pd

from crazy.algos.base import CrazyAlgoBase


class UberMobilityAlgo(CrazyAlgoBase):
    algo_id = "uber-mobility"
    name = "Uber Mobility Index"
    rebalance_frequency = "weekly"
    supports_historical_seed = False

    # 4-week rate of change thresholds on combined uber+lyft search interest
    ROC_BULL = 0.10    # 10% rise in 4 weeks → mobility expanding
    ROC_BEAR = -0.10   # 10% drop in 4 weeks → mobility contracting

    def universe(self):
        return ["XLY", "XLK", "XLF", "XLP", "XLU", "XLV"]

    def compute_signal(self, as_of, state, historical=False):
        try:
            from pytrends.request import TrendReq
            pytrends = TrendReq(hl="en-US", tz=360)
            pytrends.build_payload(["uber", "lyft"], timeframe="today 3-m", geo="US")
            with warnings.catch_warnings():
                warnings.filterwarnings("ignore", category=FutureWarning, module="pytrends")
                df = pytrends.interest_over_time()
        except Exception:
            return "HOLD"

        if df is None or df.empty:
            return "HOLD"

        # Drop isPartial column if present
        if "isPartial" in df.columns:
            df = df.drop(columns=["isPartial"])

        # Combined mobility index
        df["mobility"] = df["uber"] + df["lyft"]

        if len(df) < 5:
            return "HOLD"

        # 4-week rate of change
        df["roc_4w"] = df["mobility"].pct_change(4)
        df = df.dropna()
        if df.empty:
            return "HOLD"

        latest = df.iloc[-1]
        roc = latest["roc_4w"]
        mobility = latest["mobility"]

        meta = self.meta(state)
        meta["mobility_index"] = int(mobility)
        meta["roc_4w"] = round(float(roc), 4)
        meta["uber_interest"] = int(latest["uber"])
        meta["lyft_interest"] = int(latest["lyft"])

        if roc > self.ROC_BULL:
            meta["signal_label"] = "RISK_ON"
            meta["signal_key"] = "RISK_ON"
            return "RISK_ON"
        if roc < self.ROC_BEAR:
            meta["signal_label"] = "RISK_OFF"
            meta["signal_key"] = "RISK_OFF"
            return "RISK_OFF"

        meta["signal_label"] = "HOLD"
        meta["signal_key"] = "HOLD"
        return "HOLD"

    def target_allocations(self, signal, state, as_of):
        if signal == "RISK_ON":
            # Rising mobility → consumer discretionary, tech, financials
            return {"XLY": 0.40, "XLK": 0.35, "XLF": 0.25}
        if signal == "RISK_OFF":
            # Falling mobility → staples, utilities, healthcare
            return {"XLP": 0.40, "XLU": 0.30, "XLV": 0.30}
        return None
