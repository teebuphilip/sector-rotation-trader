from datetime import date

import pandas as pd

from crazy.algos.base import CrazyAlgoBase


class PatentFilingVelocityAlgo(CrazyAlgoBase):
    algo_id = "patent-filing-velocity"
    name = "Patent Filing Velocity"
    rebalance_frequency = "monthly"
    supports_historical_seed = False

    # Quarter-over-quarter growth thresholds for patent filings (G06 computing class)
    EXPANSION_THRESHOLD = 0.05   # >5% QoQ growth = R&D expansion = XLK
    CONTRACTION_THRESHOLD = -0.05  # <-5% QoQ decline = pullback = defensive

    def universe(self):
        return ["XLK", "XLI", "XLV", "XLP", "XLU"]

    def compute_signal(self, as_of, state, historical=False):
        from crazy.adapters.uspto_bulk import fetch_uspto_patent_counts
        df = fetch_uspto_patent_counts(months_back=18)
        if df.empty or len(df) < 2:
            return "HOLD"

        df = df.sort_values("date")
        latest = df.iloc[-1]
        prior = df.iloc[-2]

        if prior["patent_count"] == 0:
            return "HOLD"

        qoq = (latest["patent_count"] - prior["patent_count"]) / prior["patent_count"]

        meta = self.meta(state)
        meta["patent_count_latest"] = int(latest["patent_count"])
        meta["patent_count_prior"] = int(prior["patent_count"])
        meta["qoq_growth"] = round(float(qoq), 4)
        meta["latest_quarter"] = str(latest["date"].date())

        if qoq > self.EXPANSION_THRESHOLD:
            meta["signal_label"] = "EXPANSION"
            return "EXPANSION"
        if qoq < self.CONTRACTION_THRESHOLD:
            meta["signal_label"] = "CONTRACTION"
            return "CONTRACTION"

        meta["signal_label"] = "HOLD"
        return "HOLD"

    def target_allocations(self, signal, state, as_of):
        if signal == "EXPANSION":
            return {"XLK": 0.50, "XLI": 0.30, "XLV": 0.20}
        if signal == "CONTRACTION":
            return {"XLP": 0.40, "XLU": 0.35, "XLV": 0.25}
        return None
