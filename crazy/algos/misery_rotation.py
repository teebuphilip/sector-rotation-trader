import os
from datetime import date

import pandas as pd

from crazy.algos.base import CrazyAlgoBase
from crazy.blocked import record_blocked


class MiseryRotationAlgo(CrazyAlgoBase):
    algo_id = "misery-rotation"
    name = "Misery Rotation"
    rebalance_frequency = "monthly"
    supports_historical_seed = False

    # Misery Index = unemployment + YoY inflation
    # Thresholds on 3-month change in the misery index
    MISERY_DELTA_BULL = -0.3   # falling misery → offensive
    MISERY_DELTA_BEAR = 0.3    # rising misery → defensive

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
            unrate = fred.get_series("UNRATE")
            cpi = fred.get_series("CPIAUCSL")
        except Exception:
            return "HOLD"

        if unrate is None or cpi is None or len(unrate) < 15 or len(cpi) < 15:
            return "HOLD"

        # Build misery index: unemployment rate + YoY CPI inflation rate
        df = pd.DataFrame({"unrate": unrate, "cpi": cpi}).dropna()
        if len(df) < 13:
            return "HOLD"

        df["cpi_yoy"] = df["cpi"].pct_change(12) * 100  # annualized %
        df = df.dropna()
        if len(df) < 4:
            return "HOLD"

        df["misery"] = df["unrate"] + df["cpi_yoy"]
        df["misery_delta_3m"] = df["misery"].diff(3)
        df = df.dropna()
        if df.empty:
            return "HOLD"

        latest = df.iloc[-1]
        misery = latest["misery"]
        delta = latest["misery_delta_3m"]

        meta = self.meta(state)
        meta["misery_index"] = round(float(misery), 2)
        meta["misery_delta_3m"] = round(float(delta), 2)
        meta["unrate"] = round(float(latest["unrate"]), 2)
        meta["cpi_yoy"] = round(float(latest["cpi_yoy"]), 2)

        if delta < self.MISERY_DELTA_BULL:
            meta["signal_label"] = "OFFENSIVE"
            meta["signal_key"] = "OFFENSIVE"
            return "OFFENSIVE"
        if delta > self.MISERY_DELTA_BEAR:
            meta["signal_label"] = "DEFENSIVE"
            meta["signal_key"] = "DEFENSIVE"
            return "DEFENSIVE"

        meta["signal_label"] = "HOLD"
        meta["signal_key"] = "HOLD"
        return "HOLD"

    def target_allocations(self, signal, state, as_of):
        if signal == "OFFENSIVE":
            # Falling misery → consumer discretionary, tech, financials
            return {"XLY": 0.40, "XLK": 0.35, "XLF": 0.25}
        if signal == "DEFENSIVE":
            # Rising misery → staples, utilities, healthcare
            return {"XLP": 0.40, "XLU": 0.30, "XLV": 0.30}
        return None
