import os
from datetime import date

import pandas as pd

from .base import CrazyAlgoBase
from crazy.blocked import record_blocked


class LiquorAlgo(CrazyAlgoBase):
    algo_id = "liquor"
    name = "Liquor Store Leading Indicator"
    rebalance_frequency = "monthly"
    supports_historical_seed = False

    def universe(self):
        return ["XLY", "XLK", "XLF", "XLP", "XLU", "XLV"]

    def compute_signal(self, as_of: date, state: dict, historical: bool = False):
        api_key = os.getenv("FRED_API_KEY")
        if not api_key:
            record_blocked(self.algo_id, self.name, ["FRED_API_KEY"], "Missing FRED_API_KEY")
            return "HOLD"

        try:
            from fredapi import Fred
            fred = Fred(api_key=api_key)
            total_sales = fred.get_series("MRTSSM4453USN")
        except Exception:
            return "HOLD"
        df = pd.DataFrame({"sales": total_sales}).dropna()
        if len(df) < 4:
            return "HOLD"
        sales_chg = df["sales"].pct_change(3).iloc[-1]

        if sales_chg > 0.02:
            return "RISK_ON"
        if sales_chg < -0.02:
            return "RISK_OFF"
        return "NEUTRAL"

    def target_allocations(self, signal: str, state: dict, as_of: date):
        if signal == "RISK_ON":
            return {"XLY": 0.50, "XLK": 0.30, "XLF": 0.20}
        if signal == "RISK_OFF":
            return {"XLP": 0.50, "XLU": 0.30, "XLV": 0.20}
        return None
