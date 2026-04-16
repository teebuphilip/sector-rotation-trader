from datetime import date
import os
import pandas as pd
from crazy.algos.base import CrazyAlgoBase
from crazy.adapters.reddit_activity import fetch_reddit_activity
from crazy.utils import cached_fetch
from crazy.config import CRAZY_CACHE_DIR
from crazy.blocked import record_blocked

class RedditGamingThreadSpike(CrazyAlgoBase):
    algo_id = "reddit-gaming-thread-spike"
    name = "Reddit Gaming Thread Spike"
    rebalance_frequency = "daily"
    supports_historical_seed = False

    def universe(self):
        return ["ATVI", "EA", "NVDA"]

    def _fetch_reddit_data(self):
        cache_path = os.path.join(CRAZY_CACHE_DIR, "reddit_activity.json")

        def _fetch():
            return fetch_reddit_activity(subreddits=["r/gaming", "r/pcgaming", "r/nvidia"], days_back=7)

        data = cached_fetch(cache_path, ttl_hours=1, fetch_fn=_fetch)
        return pd.DataFrame(data) if data else pd.DataFrame()

    def compute_signal(self, as_of: date, state: dict, historical: bool = False):
        df = self._fetch_reddit_data()
        if df.empty:
            record_blocked(self.algo_id, self.name, ["reddit_activity"], "Missing Reddit activity data")
            return "HOLD"

        df["total"] = df["posts"] + df["comments"]
        df["ma7"] = df["total"].rolling(7).mean()
        latest = df.iloc[-1]

        if latest["total"] > 1.5 * latest["ma7"] and latest["total"] >= 100:
            return "RISK_ON"
        return "HOLD"

    def target_allocations(self, signal: str, state: dict, as_of: date):
        if signal == "RISK_ON":
            return {
                "ATVI": 0.05,
                "EA": 0.05,
                "NVDA": 0.05
            }
        return None

# Register the algo
from crazy.algos.registry import register_algo
register_algo(RedditGamingThreadSpike)