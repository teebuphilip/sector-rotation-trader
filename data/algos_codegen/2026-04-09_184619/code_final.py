from datetime import date, timedelta
import os
import pandas as pd
from crazy.algos.base import CrazyAlgoBase
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

    def _fetch_reddit_data(self, as_of: date):
        cache_path = os.path.join(CRAZY_CACHE_DIR, f"reddit_data_{as_of.strftime('%Y%m%d')}.json")

        def _fetch():
            reddit_api_key = os.getenv("REDDIT_API_KEY")
            if not reddit_api_key:
                record_blocked(self.algo_id, self.name, ["REDDIT_API_KEY"], "Missing REDDIT_API_KEY")
                return []

            # Fetch Reddit data using the API key
            # Return a list of dicts with "date", "posts", "comments" fields
            return []

        return cached_fetch(cache_path, ttl_hours=1, fetch_fn=_fetch)

    def compute_signal(self, as_of: date, state: dict, historical: bool = False):
        reddit_data = self._fetch_reddit_data(as_of)
        if not reddit_data:
            return "HOLD"

        combined_posts_comments = sum(item["posts"] + item["comments"] for item in reddit_data)
        avg_posts_comments = combined_posts_comments / len(reddit_data)
        window_start = as_of - timedelta(days=7)
        window_data = [item for item in reddit_data if item["date"] >= window_start]
        window_combined = sum(item["posts"] + item["comments"] for item in window_data)
        window_avg = window_combined / len(window_data)

        if window_avg > 1.5 * avg_posts_comments:
            return "RISK_ON"
        return "HOLD"

    def target_allocations(self, signal: str, state: dict, as_of: date):
        if signal == "RISK_ON":
            return {"ATVI": 0.4, "EA": 0.3, "NVDA": 0.3}
        return None