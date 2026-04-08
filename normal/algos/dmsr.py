from datetime import date

import pandas as pd

from config import SECTOR_ETFS
from .base import NormalAlgoBase


class DMSRAlgo(NormalAlgoBase):
    algo_id = "dmsr"
    name = "Antonacci Dual Momentum Sector Rotation"
    rebalance_frequency = "monthly_eom"

    def universe(self):
        return list(SECTOR_ETFS) + ["SPY", "AGG"]

    def compute_target(self, prices: pd.DataFrame, as_of: date):
        monthly = prices.resample("M").last().dropna(how="all")
        if len(monthly) < 13:
            return {}

        spy = monthly["SPY"].dropna()
        if len(spy) < 13:
            return {}
        spy_12m = spy.iloc[-1] / spy.iloc[-13] - 1
        if spy_12m < 0:
            return {"AGG": 1.0}

        sectors = monthly[SECTOR_ETFS].dropna(how="all")
        returns_12m = sectors.iloc[-1] / sectors.iloc[-13] - 1
        top4 = returns_12m.sort_values(ascending=False).head(4).index.tolist()
        weight = 1.0 / len(top4)
        return {t: weight for t in top4}
