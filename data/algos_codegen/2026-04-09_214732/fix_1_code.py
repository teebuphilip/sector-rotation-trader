from crazy.adapters.reddit_activity import fetch_reddit_activity
from datetime import date
import os
import pandas as pd
from crazy.algos.base import CrazyAlgoBase
from crazy.utils import cached_fetch
from crazy.config import CRAZY_CACHE_DIR
from crazy.blocked import record_blocked
from scanner import safe_download

class RedditGamingThreadSpike(CrazyAlgoBase):
    algo_id = "reddit-gaming-thread-spike"
    name = "Reddit Gaming Thread Spike"
    rebalance_frequency = "daily"
    supports_historical_seed = False

    def universe(self):
        return ["ATVI", "EA", "NVDA", "TTWO", "MSFT"]

    def _fetch_reddit_activity(self):
        cache_path = os.path.join(CRAZY_CACHE_DIR, "reddit_activity.json")

        def _fetch():
            return fetch_reddit_activity(["r/gaming", "r/pcgaming", "r/games"], ["new_posts", "new_comments"], False, "UTC")

        data = cached_fetch(cache_path, ttl_hours=1, fetch_fn=_fetch)
        return pd.DataFrame(data) if data else pd.DataFrame()

    def compute_signal(self, as_of: date, state: dict, historical: bool = False):
        reddit_df = self._fetch_reddit_activity()
        if reddit_df.empty:
            record_blocked(self.algo_id, self.name, ["reddit_api"], "Missing Reddit API data")
            return "HOLD"

        reddit_df = reddit_df[reddit_df["date"] <= pd.Timestamp(as_of)]
        if len(reddit_df) < 8:
            return "HOLD"

        reddit_df["total_new_posts_plus_comments"] = reddit_df["new_posts"] + reddit_df["new_comments"]
        reddit_df["7day_moving_average"] = reddit_df["total_new_posts_plus_comments"].rolling(7).mean()
        latest = reddit_df.iloc[-1]

        if (latest["total_new_posts_plus_comments"] - latest["7day_moving_average"]) / latest["7day_moving_average"] > 0.5:
            return "RISK_ON"
        return "HOLD"

    def target_allocations(self, signal: str, state: dict, as_of: date):
        if signal == "RISK_ON":
            return {
                "ATVI": 0.05,
                "EA": 0.05,
                "NVDA": 0.05,
                "TTWO": 0.05,
                "MSFT": 0.05
            }
        return None