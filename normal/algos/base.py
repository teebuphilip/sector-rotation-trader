from datetime import date


class NormalAlgoBase:
    algo_id = "base"
    name = "Base"
    rebalance_frequency = "monthly_eom"  # daily | monthly_eom | weekly

    def universe(self):
        return []

    def meta(self, state: dict) -> dict:
        state.setdefault("meta", {})
        state["meta"].setdefault(self.algo_id, {})
        return state["meta"][self.algo_id]

    def should_rebalance(self, as_of: date, is_eom: bool) -> bool:
        if self.rebalance_frequency == "daily":
            return True
        if self.rebalance_frequency == "weekly":
            return as_of.weekday() == 0
        if self.rebalance_frequency == "monthly_eom":
            return is_eom
        return False

    def compute_target(self, prices, as_of: date):
        return {}
