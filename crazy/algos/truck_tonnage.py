import os
from datetime import date

import pandas as pd

from crazy.algos.base import CrazyAlgoBase
from crazy.blocked import record_blocked


class TruckTonnageAlgo(CrazyAlgoBase):
    algo_id = "truck-tonnage"
    name = "Truck Tonnage Index"
    rebalance_frequency = "monthly"
    supports_historical_seed = False

    TONNAGE_ACCEL_BULL = 0.01
    TONNAGE_ACCEL_BEAR = -0.01
    RAIL_CONFIRM = 0.0

    def universe(self):
        return ["XLI", "XLB", "XLE", "XLP", "XLU", "XLV"]

    def compute_signal(self, as_of, state, historical=False):
        api_key = os.getenv("FRED_API_KEY")
        if not api_key:
            record_blocked(self.algo_id, self.name, ["FRED_API_KEY"], "Missing FRED_API_KEY")
            return "HOLD"

        try:
            from fredapi import Fred
            fred = Fred(api_key=api_key)
            tonnage = fred.get_series("TSIFRGHT")
            rail = fred.get_series("RAILFRTCARLOADSD11")
        except Exception:
            return "HOLD"

        df = pd.DataFrame({"tonnage": tonnage, "rail": rail}).dropna()
        if len(df) < 6:
            return "HOLD"

        df["tonnage_3m_chg"] = df["tonnage"].pct_change(3)
        df["tonnage_accel"] = df["tonnage_3m_chg"].diff()
        df["rail_3m_chg"] = df["rail"].pct_change(3)
        df = df.dropna()
        if df.empty:
            return "HOLD"

        latest = df.iloc[-1]
        tonnage_accel = latest["tonnage_accel"]
        rail_chg = latest["rail_3m_chg"]

        meta = self.meta(state)
        meta["tonnage_accel"] = round(float(tonnage_accel), 4)
        meta["rail_3m_chg"] = round(float(rail_chg), 4)

        if tonnage_accel > self.TONNAGE_ACCEL_BULL and rail_chg > self.RAIL_CONFIRM:
            meta["signal_label"] = "EXPANSION"
            meta["signal_key"] = "EXPANSION"
            return "EXPANSION"
        if tonnage_accel < self.TONNAGE_ACCEL_BEAR and rail_chg < self.RAIL_CONFIRM:
            meta["signal_label"] = "CONTRACTION"
            meta["signal_key"] = "CONTRACTION"
            return "CONTRACTION"

        meta["signal_label"] = "HOLD"
        meta["signal_key"] = "HOLD"
        return "HOLD"

    def target_allocations(self, signal, state, as_of):
        if signal == "EXPANSION":
            return {"XLI": 0.40, "XLB": 0.30, "XLE": 0.30}
        if signal == "CONTRACTION":
            return {"XLP": 0.40, "XLU": 0.30, "XLV": 0.30}
        return None
