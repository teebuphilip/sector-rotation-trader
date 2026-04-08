from datetime import date


class CrazyAlgoBase:
    algo_id = "base"
    name = "Base"
    rebalance_frequency = "daily"  # daily | weekly | monthly
    supports_historical_seed = False

    def universe(self):
        return []

    def meta(self, state: dict) -> dict:
        state.setdefault("meta", {})
        state["meta"].setdefault(self.algo_id, {})
        return state["meta"][self.algo_id]

    def compute_signal(self, as_of: date, state: dict, historical: bool = False):
        return "HOLD"

    def target_allocations(self, signal: str, state: dict, as_of: date):
        return None

    def should_rebalance(self, as_of: date, state: dict, signal: str) -> bool:
        meta = self.meta(state)
        last_signal = meta.get("last_signal")
        if last_signal != signal:
            return True

        if self.rebalance_frequency == "weekly":
            return as_of.weekday() == 0
        if self.rebalance_frequency == "monthly":
            return as_of.day == 1
        return False
