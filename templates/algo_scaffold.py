"""
Algo scaffold template.
Copy this file and implement the TODOs for a new algo.
"""
from datetime import date
import pandas as pd

from crazy.algos.base import CrazyAlgoBase
# For normal algos, inherit from normal.algos.base.NormalAlgoBase instead.


class AlgoTemplate(CrazyAlgoBase):
    algo_id = "template"
    name = "Template Algo"
    rebalance_frequency = "daily"  # daily | weekly | monthly
    supports_historical_seed = False  # True if you can backfill signals

    def universe(self):
        # TODO: return list of tickers / ETFs
        return []

    def compute_signal(self, as_of: date, state: dict, historical: bool = False):
        """
        Return a signal string, e.g. "RISK_ON", "RISK_OFF", "HOLD".
        Use `state` for persistence (meta/cache).
        """
        # TODO: implement signal logic
        return "HOLD"

    def target_allocations(self, signal: str, state: dict, as_of: date):
        """
        Return dict of target weights, e.g. {"XLY": 0.4, "XLK": 0.3, "XLI": 0.3}
        Return None to do nothing, or {} for cash.
        """
        # TODO: map signal -> target weights
        if signal == "RISK_ON":
            return {}
        if signal == "RISK_OFF":
            return {}
        return None

    def should_rebalance(self, as_of: date, state: dict, signal: str) -> bool:
        # Optional override; default is in base class.
        return super().should_rebalance(as_of, state, signal)
