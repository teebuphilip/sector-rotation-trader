from datetime import date, timedelta
import os
from typing import Dict

from crazy.algos.base import CrazyAlgoBase
from crazy.blocked import record_blocked
from crazy.utils import cached_fetch
from crazy.config import CRAZY_CACHE_DIR
from scanner import safe_download
import pandas as pd
import numpy as np

class RedditGamingThreadSpikeAlgo(CrazyAlgoBase):
    algo_id = "reddit-gaming-thread-spike"
    name = "Reddit Gaming Thread Spike"
    rebalance_frequency = "daily"
    supports_historical_seed = False

    def universe(self):
        return ["ATVI", "EA", "NVDA", "TTWO", "MSFT"]

    def compute_signal(self, as_of: date, state: dict, historical: bool = False):
        reddit_api_key = os.getenv("REDDIT_API_KEY")
        if not reddit_api_key:
            record_blocked(self.algo_id, self.name, ["REDDIT_API_KEY"], "Missing REDDIT_API_KEY")
            return "HOLD"

        try:
            data = self.get_reddit_data(as_of)
        except Exception as e:
            record_blocked(self.algo_id, self.name, ["REDDIT_API"], f"Error fetching Reddit data: {e}")
            return "HOLD"

        if data is None:
            return "HOLD"

        total_activity = data["total_posts_plus_comments"]
        avg_activity = data["7day_avg_total_activity"]

        if total_activity >= 1.5 * avg_activity and total_activity >= 100:
            return "RISK_ON"
        else:
            return "HOLD"

    def target_allocations(self, signal: str, state: dict, as_of: date):
        if signal == "RISK_ON":
            return {"ATVI": 0.2, "EA": 0.2, "NVDA": 0.2, "TTWO": 0.2, "MSFT": 0.2}
        return None

    @cached_fetch(cache_dir=CRAZY_CACHE_DIR)
    def get_reddit_data(self, as_of: date) -> Dict[str, float]:
        reddit_api_key = os.getenv("REDDIT_API_KEY")
        if not reddit_api_key:
            return None

        subreddits = ["r/gaming", "r/pcgaming", "r/games"]
        total_posts = 0
        total_comments = 0

        for subreddit in subreddits:
            url = f"https://api.pushshift.io/reddit/submission/search/?subreddit={subreddit}&after={as_of - timedelta(days=7)}&before={as_of + timedelta(days=1)}&size=1000"
            posts = safe_download(url)
            total_posts += len(posts)

            url = f"https://api.pushshift.io/reddit/comment/search/?subreddit={subreddit}&after={as_of - timedelta(days=7)}&before={as_of + timedelta(days=1)}&size=1000"
            comments = safe_download(url)
            total_comments += len(comments)

        total_activity = total_posts + total_comments
        avg_activity = total_activity / 7

        return {
            "total_posts_plus_comments": total_activity,
            "7day_avg_total_activity": avg_activity
        }