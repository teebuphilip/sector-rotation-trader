import os
from datetime import date

import pandas as pd

from crazy.algos.base import CrazyAlgoBase
from crazy.blocked import record_blocked


class SmallBusinessFormationAlgo(CrazyAlgoBase):
    algo_id = "small-business-formation"
    name = "Small Business Formation"
    rebalance_frequency = "monthly"
    supports_historical_seed = False

    # 3-month change thresholds on small business optimism index
    DELTA_BULL = 1.0    # rising optimism → expansion
    DELTA_BEAR = -1.0   # falling optimism → defensive

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
            nfib = fred.get_series("SBUSV")
        except Exception:
            return "HOLD"

        if nfib is None or len(nfib) < 6:
            return "HOLD"

        df = pd.DataFrame({"nfib": nfib}).dropna()
        df["delta_3m"] = df["nfib"].diff(3)
        df = df.dropna()
        if df.empty:
            return "HOLD"

        latest = df.iloc[-1]
        delta = latest["delta_3m"]

        meta = self.meta(state)
        meta["nfib_level"] = round(float(latest["nfib"]), 1)
        meta["delta_3m"] = round(float(delta), 2)

        if delta > self.DELTA_BULL:
            meta["signal_label"] = "EXPANSION"
            meta["signal_key"] = "EXPANSION"
            return "EXPANSION"
        if delta < self.DELTA_BEAR:
            meta["signal_label"] = "CONTRACTION"
            meta["signal_key"] = "CONTRACTION"
            return "CONTRACTION"

        meta["signal_label"] = "HOLD"
        meta["signal_key"] = "HOLD"
        return "HOLD"

    def target_allocations(self, signal, state, as_of):
        if signal == "EXPANSION":
            return {"XLY": 0.40, "XLF": 0.35, "XLK": 0.25}
        if signal == "CONTRACTION":
            return {"XLP": 0.40, "XLU": 0.30, "XLV": 0.30}
        return None
