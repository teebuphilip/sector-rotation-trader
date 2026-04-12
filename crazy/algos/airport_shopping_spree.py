from datetime import date
import pandas as pd
from crazy.algos.base import CrazyAlgoBase
from crazy.adapters.tsa_table import fetch_tsa_table


class AirportShoppingSpreeAlgo(CrazyAlgoBase):
    algo_id = "airport-shopping-spree"
    name = "Airport Shopping Spree"
    rebalance_frequency = "daily"
    supports_historical_seed = True

    def universe(self):
        return ["TICKER1", "TICKER2", "TICKER3"]

    def compute_signal(self, as_of: date, state: dict, historical: bool = False):
        # === SIGNAL_LOGIC_START ===
        return "HOLD"
# === SIGNAL_LOGIC_END ===

    def target_allocations(self, signal: str, state: dict, as_of: date):
        # === ALLOCATION_LOGIC_START ===
        if signal == "RISK_ON":
            return {}
        if signal == "RISK_OFF":
            return {}
        return {}
# === ALLOCATION_LOGIC_END ===