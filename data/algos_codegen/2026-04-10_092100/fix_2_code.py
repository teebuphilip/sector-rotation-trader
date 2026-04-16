from datetime import date, timedelta
import os
import pandas as pd
from crazy.algos.base import CrazyAlgoBase
from crazy.utils import cached_fetch
from crazy.config import CRAZY_CACHE_DIR
from crazy.blocked import record_blocked
from crazy.adapters.reddit_activity import fetch_reddit_activity

class RedditGamingThreadSpike(CrazyAlgoBase):
    algo_id = "reddit-gaming-thread-spike"
    name = "Reddit Gaming Thread Spike"
    rebalance_frequency = "daily"
    supports_historical_seed = True

    def universe(self):
        return ["ATVI", "EA", "NVDA", "TTWO", "MSFT"]

    def _fetch_reddit_data(self, days_back: int):
        cache_key = f"reddit_activity_{days_back}"
        cache_path = os.path.join(CRAZY_CACHE_DIR, f"{cache_key}.json")

        data = fetch_reddit_activity(
            subreddits=["gaming", "pcgaming", "Games"],
            days_back=days_back,
            cache_key=cache_key
        )
        return pd.DataFrame(data) if data else pd.DataFrame()

    def compute_signal(self, as_of: date, state: dict, historical: bool = False):
        df = self._fetch_reddit_data(days_back=7)
        if df.empty:
            record_blocked(self.algo_id, self.name, ["reddit_activity"], "Missing Reddit data")
            return "HOLD"

        df["total"] = df["posts"] + df["comments"]
        df["ma7"] = df["total"].ewm(span=7, adjust=False).mean()

        latest = df.iloc[-1]
        if latest["total"] > 1.5 * latest["ma7"] and latest["ma7"] >= 100:
            return "RISK_ON"
        return "HOLD"

    def target_allocations(self, signal: str, state: dict, as_of: date):
        if signal == "RISK_ON":
            total_allocation = 0.05
            max_per_stock = 0.02
            max_total_exposure = 0.2
            allocations = {}
            for stock in self.universe():
                allocation = min(max_per_stock, total_allocation / len(self.universe()))
                if sum(allocations.values()) + allocation > max_total_exposure:
                    allocation = max_total_exposure - sum(allocations.values())
                allocations[stock] = allocation
            return allocations
        return {}