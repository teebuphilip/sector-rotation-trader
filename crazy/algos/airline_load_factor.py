from crazy.adapters.bts_airline_load_factor import fetch_bts_airline_load_factor
from crazy.algos.base import CrazyAlgoBase


class AirlineLoadFactorAlgo(CrazyAlgoBase):
    algo_id = "airline-load-factor"
    name = "Airline Load Factor Proxy"
    rebalance_frequency = "monthly"
    supports_historical_seed = False

    BULL_3M = 0.02
    BEAR_3M = -0.02

    def universe(self):
        return ["XLY", "XLI", "XLF", "XLK", "XLP", "XLU", "XLV"]

    def compute_signal(self, as_of, state, historical=False):
        df = fetch_bts_airline_load_factor()
        if df.empty or len(df) < 6:
            return "HOLD"

        df = df.sort_values("date").copy()
        recent = float(df["value"].tail(3).mean())
        prior = float(df["value"].iloc[-6:-3].mean())
        if prior <= 0:
            return "HOLD"

        if recent > 1.0 or prior > 1.0:
            change = (recent / prior) - 1.0
            change_key = "airline_traffic_3m_chg"
        else:
            change = recent - prior
            change_key = "load_factor_3m_delta"
        meta = self.meta(state)
        meta["adapter"] = "bts_airline_load_factor"
        meta[change_key] = round(change, 4)

        if change > self.BULL_3M:
            meta["signal_label"] = "TRAVEL_DEMAND_EXPANSION"
            meta["signal_key"] = "TRAVEL_DEMAND_EXPANSION"
            return "TRAVEL_DEMAND_EXPANSION"
        if change < self.BEAR_3M:
            meta["signal_label"] = "TRAVEL_DEMAND_SLOWDOWN"
            meta["signal_key"] = "TRAVEL_DEMAND_SLOWDOWN"
            return "TRAVEL_DEMAND_SLOWDOWN"

        meta["signal_label"] = "HOLD"
        meta["signal_key"] = "HOLD"
        return "HOLD"

    def target_allocations(self, signal, state, as_of):
        if signal == "TRAVEL_DEMAND_EXPANSION":
            return {"XLY": 0.35, "XLI": 0.30, "XLF": 0.20, "XLK": 0.15}
        if signal == "TRAVEL_DEMAND_SLOWDOWN":
            return {"XLP": 0.45, "XLU": 0.35, "XLV": 0.20}
        return None
