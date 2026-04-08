from datetime import date

import pandas as pd

from .base import NormalAlgoBase


class SimpleMonthlyAlgo(NormalAlgoBase):
    algo_id = "simple_monthly"
    name = "Quantified Simple Monthly Rotation"
    rebalance_frequency = "monthly_eom"

    def universe(self):
        return ["SPY", "EEM", "TLT"]

    def compute_target(self, prices: pd.DataFrame, as_of: date):
        monthly = prices.resample("M").last().dropna(how="all")
        if len(monthly) < 2:
            return {}

        last = monthly.iloc[-1]
        prev = monthly.iloc[-2]
        returns_1m = (last / prev) - 1
        top = returns_1m.sort_values(ascending=False).head(1).index.tolist()
        return {top[0]: 1.0} if top else {}
