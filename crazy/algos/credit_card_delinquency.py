import os
from datetime import date

import pandas as pd

from crazy.algos.base import CrazyAlgoBase
from crazy.blocked import record_blocked


class CreditCardDelinquencyAlgo(CrazyAlgoBase):
    algo_id = "credit-card-delinquency"
    name = "Credit Card Delinquency"
    rebalance_frequency = "quarterly"
    supports_historical_seed = False

    # Change thresholds on delinquency rate (quarterly series)
    DELTA_STRESS = 0.20    # rising delinquency → consumer stress → defensive
    DELTA_HEALTHY = -0.20  # falling delinquency → healthy consumer → offensive

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
            dq = fred.get_series("DRCCLACBS")
        except Exception:
            return "HOLD"

        if dq is None or len(dq) < 4:
            return "HOLD"

        df = pd.DataFrame({"dq_rate": dq}).dropna()
        # Quarterly data — use 1-period diff (= quarter-over-quarter change)
        df["delta_1q"] = df["dq_rate"].diff(1)
        df = df.dropna()
        if df.empty:
            return "HOLD"

        latest = df.iloc[-1]
        delta = latest["delta_1q"]

        meta = self.meta(state)
        meta["dq_rate"] = round(float(latest["dq_rate"]), 2)
        meta["delta_1q"] = round(float(delta), 2)

        if delta < self.DELTA_HEALTHY:
            meta["signal_label"] = "HEALTHY"
            meta["signal_key"] = "HEALTHY"
            return "HEALTHY"
        if delta > self.DELTA_STRESS:
            meta["signal_label"] = "STRESS"
            meta["signal_key"] = "STRESS"
            return "STRESS"

        meta["signal_label"] = "HOLD"
        meta["signal_key"] = "HOLD"
        return "HOLD"

    def target_allocations(self, signal, state, as_of):
        if signal == "HEALTHY":
            return {"XLY": 0.40, "XLK": 0.30, "XLF": 0.30}
        if signal == "STRESS":
            return {"XLP": 0.40, "XLU": 0.30, "XLV": 0.30}
        return None
