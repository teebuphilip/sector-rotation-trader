import os
from datetime import date

import pandas as pd

from crazy.algos.base import CrazyAlgoBase
from crazy.blocked import record_blocked


class YelpClosureVelocityAlgo(CrazyAlgoBase):
    algo_id = "yelp-closure-velocity"
    name = "Yelp Closure Velocity"
    rebalance_frequency = "weekly"
    supports_historical_seed = False

    # Closure rate thresholds (fraction of sampled businesses permanently closed)
    STRESS_THRESHOLD = 0.15    # >15% closure rate = consumer stress = defensive
    RECOVERY_THRESHOLD = 0.08  # <8% closure rate = expansion = offensive

    def universe(self):
        return ["XLY", "XLK", "XLF", "XLP", "XLU", "XLV"]

    def compute_signal(self, as_of, state, historical=False):
        api_key = os.getenv("YELP_API_KEY")
        if not api_key:
            record_blocked(self.algo_id, self.name, ["YELP_API_KEY"], "Missing YELP_API_KEY")
            return "HOLD"

        from crazy.adapters.yelp_fusion import fetch_yelp_closure_rate
        df = fetch_yelp_closure_rate()
        if df.empty:
            return "HOLD"

        closure_rate = float(df.iloc[-1]["closure_rate"])
        meta = self.meta(state)
        meta["closure_rate"] = closure_rate
        meta["closed_count"] = int(df.iloc[-1]["closed_count"])
        meta["total_count"] = int(df.iloc[-1]["total_count"])

        # Track week-over-week change using stored prior rate
        prior_rate = meta.get("prior_closure_rate")
        if prior_rate is not None:
            delta = closure_rate - float(prior_rate)
            meta["closure_rate_delta"] = round(delta, 4)
        else:
            delta = 0.0
            meta["closure_rate_delta"] = None

        meta["prior_closure_rate"] = closure_rate

        # Signal logic: absolute level + direction
        if closure_rate > self.STRESS_THRESHOLD:
            meta["signal_label"] = "STRESS"
            return "STRESS"
        if closure_rate < self.RECOVERY_THRESHOLD:
            meta["signal_label"] = "EXPANSION"
            return "EXPANSION"

        meta["signal_label"] = "HOLD"
        return "HOLD"

    def target_allocations(self, signal, state, as_of):
        if signal == "EXPANSION":
            return {"XLY": 0.40, "XLK": 0.35, "XLF": 0.25}
        if signal == "STRESS":
            return {"XLP": 0.40, "XLU": 0.30, "XLV": 0.30}
        return None
