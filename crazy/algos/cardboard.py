import os
from datetime import date

import pandas as pd

from .base import CrazyAlgoBase
from crazy.blocked import record_blocked


class CardboardAlgo(CrazyAlgoBase):
    algo_id = "cardboard"
    name = "Cardboard Box Index"
    rebalance_frequency = "monthly"
    supports_historical_seed = False

    BOX_ACCEL_BULL = 0.02
    BOX_ACCEL_BEAR = -0.015
    IP_CONFIRM = 0.0

    def universe(self):
        return ["XLB", "XLI", "XLE", "XLP", "XLU", "XLV"]

    def compute_signal(self, as_of: date, state: dict, historical: bool = False):
        api_key = os.getenv("FRED_API_KEY")
        if not api_key:
            record_blocked(self.algo_id, self.name, ["FRED_API_KEY"], "Missing FRED_API_KEY")
            return "HOLD"

        from fredapi import Fred
        fred = Fred(api_key=api_key)
        box_ppi = fred.get_series("PCU3221213221213")
        mfg_ip = fred.get_series("IPMAN")
        df = pd.DataFrame({"box_ppi": box_ppi, "mfg_ip": mfg_ip}).dropna()
        df["box_ppi_3m_chg"] = df["box_ppi"].pct_change(3)
        df["box_ppi_accel"] = df["box_ppi_3m_chg"].diff()
        df["ip_3m_chg"] = df["mfg_ip"].pct_change(3)
        df = df.dropna()
        if df.empty:
            return "HOLD"

        latest = df.iloc[-1]
        box_accel = latest["box_ppi_accel"]
        ip_chg = latest["ip_3m_chg"]

        if box_accel > self.BOX_ACCEL_BULL and ip_chg > self.IP_CONFIRM:
            return "EXPANSION"
        if box_accel < self.BOX_ACCEL_BEAR and ip_chg < self.IP_CONFIRM:
            return "CONTRACTION"
        return "HOLD"

    def target_allocations(self, signal: str, state: dict, as_of: date):
        if signal == "EXPANSION":
            return {"XLB": 0.35, "XLI": 0.35, "XLE": 0.30}
        if signal == "CONTRACTION":
            return {"XLP": 0.50, "XLU": 0.25, "XLV": 0.25}
        return None
