import os
from datetime import date

import pandas as pd

from crazy.algos.base import CrazyAlgoBase
from crazy.blocked import record_blocked


class BankruptcyFilingRateAlgo(CrazyAlgoBase):
    algo_id = "bankruptcy-filing-rate"
    name = "Bankruptcy Filing Rate"
    rebalance_frequency = "monthly"
    supports_historical_seed = False

    # 3-month change thresholds on business bankruptcy filings
    DELTA_STRESS = 0.05     # rising bankruptcies → stress → defensive
    DELTA_RECOVERY = -0.05  # falling bankruptcies → recovery → offensive

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
            bk = fred.get_series("BUSTHCONS")
        except Exception:
            return "HOLD"

        if bk is None or len(bk) < 6:
            return "HOLD"

        df = pd.DataFrame({"bk": bk}).dropna()
        df["roc_3m"] = df["bk"].pct_change(3)
        df = df.dropna()
        if df.empty:
            return "HOLD"

        latest = df.iloc[-1]
        roc = latest["roc_3m"]

        meta = self.meta(state)
        meta["bankruptcy_level"] = int(latest["bk"])
        meta["roc_3m"] = round(float(roc), 4)

        if roc < self.DELTA_RECOVERY:
            meta["signal_label"] = "RECOVERY"
            meta["signal_key"] = "RECOVERY"
            return "RECOVERY"
        if roc > self.DELTA_STRESS:
            meta["signal_label"] = "STRESS"
            meta["signal_key"] = "STRESS"
            return "STRESS"

        meta["signal_label"] = "HOLD"
        meta["signal_key"] = "HOLD"
        return "HOLD"

    def target_allocations(self, signal, state, as_of):
        if signal == "RECOVERY":
            return {"XLY": 0.35, "XLK": 0.35, "XLF": 0.30}
        if signal == "STRESS":
            return {"XLP": 0.40, "XLU": 0.30, "XLV": 0.30}
        return None
