import os
from datetime import date

import pandas as pd

from crazy.algos.base import CrazyAlgoBase
from crazy.blocked import record_blocked


class JobPostingAccelerationAlgo(CrazyAlgoBase):
    algo_id = "job-posting-acceleration"
    name = "Job Posting Acceleration"
    rebalance_frequency = "monthly"
    supports_historical_seed = False

    # 3-month rate of change thresholds on job openings
    ROC_BULL = 0.02    # rising job postings → expansion
    ROC_BEAR = -0.02   # falling job postings → contraction

    def universe(self):
        return ["XLY", "XLK", "XLF", "XLP", "XLU", "XLV"]

    def compute_signal(self, as_of, state, historical=False):
        api_key = os.getenv("FRED_API_KEY")
        if not api_key:
            record_blocked(self.algo_id, self.name, ["FRED_API_KEY"], "Missing FRED_API_KEY")
            return "HOLD"

        try:
            from fredapi import Fred
            fred = Fred(api_key=api_key)
            jolts = fred.get_series("JTSJOL")
        except Exception:
            return "HOLD"

        if jolts is None or len(jolts) < 6:
            return "HOLD"

        df = pd.DataFrame({"jolts": jolts}).dropna()
        df["roc_3m"] = df["jolts"].pct_change(3)
        df = df.dropna()
        if df.empty:
            return "HOLD"

        latest = df.iloc[-1]
        roc = latest["roc_3m"]

        meta = self.meta(state)
        meta["jolts_level"] = int(latest["jolts"])
        meta["roc_3m"] = round(float(roc), 4)

        if roc > self.ROC_BULL:
            meta["signal_label"] = "EXPANSION"
            meta["signal_key"] = "EXPANSION"
            return "EXPANSION"
        if roc < self.ROC_BEAR:
            meta["signal_label"] = "CONTRACTION"
            meta["signal_key"] = "CONTRACTION"
            return "CONTRACTION"

        meta["signal_label"] = "HOLD"
        meta["signal_key"] = "HOLD"
        return "HOLD"

    def target_allocations(self, signal, state, as_of):
        if signal == "EXPANSION":
            return {"XLY": 0.35, "XLK": 0.35, "XLF": 0.30}
        if signal == "CONTRACTION":
            return {"XLP": 0.40, "XLU": 0.30, "XLV": 0.30}
        return None
