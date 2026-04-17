import os

from crazy.adapters.eia_electricity import fetch_eia_electricity
from crazy.algos.base import CrazyAlgoBase
from crazy.blocked import record_blocked


class ElectricityConsumptionAlgo(CrazyAlgoBase):
    algo_id = "electricity-consumption"
    name = "Electricity Consumption"
    rebalance_frequency = "weekly"
    supports_historical_seed = False

    BULL_4W = 0.015
    BEAR_4W = -0.015

    def universe(self):
        return ["XLI", "XLB", "XLU", "XLP", "XLV"]

    def compute_signal(self, as_of, state, historical=False):
        api_key = os.getenv("EIA_API_KEY")
        if not api_key:
            record_blocked(self.algo_id, self.name, ["EIA_API_KEY"], "Missing EIA_API_KEY")
            return "HOLD"

        df = fetch_eia_electricity(api_key=api_key, respondent="US48", days_back=120)
        if df.empty or len(df) < 56:
            return "HOLD"

        df = df.sort_values("date").copy()
        recent = float(df["value"].tail(28).mean())
        prior = float(df["value"].iloc[-56:-28].mean())
        if prior <= 0:
            return "HOLD"

        change = (recent / prior) - 1.0
        meta = self.meta(state)
        meta["adapter"] = "eia_electricity"
        meta["respondent"] = "US48"
        meta["electricity_4w_chg"] = round(change, 4)

        if change > self.BULL_4W:
            meta["signal_label"] = "INDUSTRIAL_POWER_DEMAND"
            meta["signal_key"] = "INDUSTRIAL_POWER_DEMAND"
            return "INDUSTRIAL_POWER_DEMAND"
        if change < self.BEAR_4W:
            meta["signal_label"] = "POWER_DEMAND_SLOWDOWN"
            meta["signal_key"] = "POWER_DEMAND_SLOWDOWN"
            return "POWER_DEMAND_SLOWDOWN"

        meta["signal_label"] = "HOLD"
        meta["signal_key"] = "HOLD"
        return "HOLD"

    def target_allocations(self, signal, state, as_of):
        if signal == "INDUSTRIAL_POWER_DEMAND":
            return {"XLI": 0.45, "XLB": 0.35, "XLU": 0.20}
        if signal == "POWER_DEMAND_SLOWDOWN":
            return {"XLP": 0.40, "XLU": 0.35, "XLV": 0.25}
        return None
