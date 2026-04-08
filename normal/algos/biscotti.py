from datetime import date

import pandas as pd

from config import SECTOR_ETFS
from .base import NormalAlgoBase


class BiscottiAlgo(NormalAlgoBase):
    algo_id = "biscotti"
    name = "Algo Biscotti (Unconditional Loyalty)"
    rebalance_frequency = "monthly_eom"

    def universe(self):
        return list(SECTOR_ETFS)

    def compute_target(self, prices: pd.DataFrame, as_of: date):
        if prices.empty:
            return {}
        window = prices[list(SECTOR_ETFS)].dropna(how="all")
        if len(window) < 31:
            return {}
        last = window.iloc[-1]
        first = window.iloc[-31]
        returns = (last / first) - 1
        returns = returns.dropna()
        if returns.empty:
            return {}
        worst = returns.sort_values().index[0]
        return {worst: 1.0}
