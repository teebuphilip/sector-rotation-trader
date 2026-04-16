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
        return ["ATVI", "EA", "NVDA", "TTWO", "MSFT"]

    def _fetch_reddit_activity(self, subreddits, days_back):
        cache_key = f"reddit_activity_{','.join(subreddits)}_{days_back}"
        cache_path = os.path.join(CRAZY_CACHE_DIR, f"{cache_key}.json")

        def _fetch():
            return fetch_reddit_activity(subreddits=subreddits, days_back=days_back)

        data = cached_fetch(cache_path, ttl_hours=1, fetch_fn=_fetch)
        return pd.DataFrame(data) if data else pd.DataFrame()

    def compute_signal(self, as_of: date, state: dict, historical: bool = False):
        subreddits = ["r/gaming", "r/pcgaming", "r/Games"]
        df = self._fetch_reddit_activity(subreddits, days_back=7)
        if df.empty:
            record_blocked(self.algo_id, self.name, ["reddit_activity"], "Missing Reddit activity data")
            return "HOLD"

        df["total"] = df["posts"] + df["comments"]
        df["ma7_posts"] = df["posts"].rolling(7).mean()
        df["ma7_comments"] = df["comments"].rolling(7).mean()

        latest = df.iloc[-1]
        if (
            ((latest["posts"] - df["ma7_posts"].iloc[-1]) / df["ma7_posts"].iloc[-1]) > 0.5
            or ((latest["comments"] - df["ma7_comments"].iloc[-1]) / df["ma7_comments"].iloc[-1]) > 0.5
        ) and latest["total"] > 1000:
            return "RISK_ON"
        return "HOLD"

    def target_allocations(self, signal: str, state: dict, as_of: date):
        if signal == "RISK_ON":
            return {
                "ATVI": 0.2,
                "EA": 0.2,
                "NVDA": 0.2,
                "TTWO": 0.2,
                "MSFT": 0.2,
            }
        return None

# Register the algo
from crazy.algos.registry import register_algo
register_algo(RedditGamingThreadSpike)