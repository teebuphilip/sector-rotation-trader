import os
from datetime import date

import pandas as pd

from crazy.algos.base import CrazyAlgoBase
from crazy.blocked import record_blocked


class ConsumerSentimentAlgo(CrazyAlgoBase):
    algo_id = "consumer-sentiment"
    name = "Consumer Sentiment"
    rebalance_frequency = "monthly"
    supports_historical_seed = False

    # 3-month change thresholds on U Michigan consumer sentiment
    DELTA_BULL = 2.0    # rising sentiment → consumer confidence → offensive
    DELTA_BEAR = -2.0   # falling sentiment → fear → defensive

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
            umcsent = fred.get_series("UMCSENT")
        except Exception:
            return "HOLD"

        if umcsent is None or len(umcsent) < 6:
            return "HOLD"

        df = pd.DataFrame({"sentiment": umcsent}).dropna()
        df["delta_3m"] = df["sentiment"].diff(3)
        df = df.dropna()
        if df.empty:
            return "HOLD"

        latest = df.iloc[-1]
        delta = latest["delta_3m"]

        meta = self.meta(state)
        meta["sentiment_level"] = round(float(latest["sentiment"]), 1)
        meta["delta_3m"] = round(float(delta), 2)

        if delta > self.DELTA_BULL:
            meta["signal_label"] = "BULLISH"
            meta["signal_key"] = "BULLISH"
            return "BULLISH"
        if delta < self.DELTA_BEAR:
            meta["signal_label"] = "BEARISH"
            meta["signal_key"] = "BEARISH"
            return "BEARISH"

        meta["signal_label"] = "HOLD"
        meta["signal_key"] = "HOLD"
        return "HOLD"

    def target_allocations(self, signal, state, as_of):
        if signal == "BULLISH":
            return {"XLY": 0.40, "XLK": 0.35, "XLF": 0.25}
        if signal == "BEARISH":
            return {"XLP": 0.40, "XLU": 0.30, "XLV": 0.30}
        return None
