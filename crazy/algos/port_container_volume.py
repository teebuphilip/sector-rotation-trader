from crazy.adapters.port_container_volume import fetch_port_container_volume
from crazy.algos.base import CrazyAlgoBase


class PortContainerVolumeAlgo(CrazyAlgoBase):
    algo_id = "port-container-volume"
    name = "Port Container Volume"
    rebalance_frequency = "monthly"
    supports_historical_seed = False

    BULL_3M = 0.03
    BEAR_3M = -0.03

    def universe(self):
        return ["XLI", "XLB", "XLY", "XLP", "XLU"]

    def compute_signal(self, as_of, state, historical=False):
        df = fetch_port_container_volume()
        if df.empty or len(df) < 6:
            return "HOLD"

        df = df.sort_values("date").copy()
        recent = float(df["value"].tail(3).mean())
        prior = float(df["value"].iloc[-6:-3].mean())
        if prior <= 0:
            return "HOLD"

        change = (recent / prior) - 1.0
        meta = self.meta(state)
        meta["adapter"] = "port_container_volume"
        meta["port_teu_3m_chg"] = round(change, 4)

        if change > self.BULL_3M:
            meta["signal_label"] = "SUPPLY_CHAIN_EXPANSION"
            meta["signal_key"] = "SUPPLY_CHAIN_EXPANSION"
            return "SUPPLY_CHAIN_EXPANSION"
        if change < self.BEAR_3M:
            meta["signal_label"] = "SUPPLY_CHAIN_SLOWDOWN"
            meta["signal_key"] = "SUPPLY_CHAIN_SLOWDOWN"
            return "SUPPLY_CHAIN_SLOWDOWN"

        meta["signal_label"] = "HOLD"
        meta["signal_key"] = "HOLD"
        return "HOLD"

    def target_allocations(self, signal, state, as_of):
        if signal == "SUPPLY_CHAIN_EXPANSION":
            return {"XLI": 0.45, "XLB": 0.35, "XLY": 0.20}
        if signal == "SUPPLY_CHAIN_SLOWDOWN":
            return {"XLP": 0.45, "XLU": 0.35, "XLI": 0.20}
        return None
