from datetime import date

import pandas as pd

from config import SECTOR_ETFS
from .base import NormalAlgoBase


class FaberMomentumAlgo(NormalAlgoBase):
    algo_id = "faber"
    name = "Faber Momentum Rotation"
    rebalance_frequency = "monthly_eom"

    def universe(self):
        return list(SECTOR_ETFS) + ["SPY"]

    def compute_target(self, prices: pd.DataFrame, as_of: date):
        monthly = prices.resample("ME").last().dropna(how="all")
        if len(monthly) < 12:
            return {}

        spy = monthly["SPY"].dropna()
        if len(spy) < 10:
            return {}
        spy_sma10 = spy.rolling(10).mean().iloc[-1]
        if spy.iloc[-1] < spy_sma10:
            return {}

        sectors = monthly[SECTOR_ETFS].dropna(how="all")
        if len(sectors) < 4:
            return {}

        returns_3m = sectors.iloc[-1] / sectors.iloc[-4] - 1
        top3 = returns_3m.sort_values(ascending=False).head(3).index.tolist()
        weight = 1.0 / len(top3)
        return {t: weight for t in top3}
