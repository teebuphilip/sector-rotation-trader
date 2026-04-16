from datetime import date, timedelta
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

    def _fetch_reddit_activity(self, as_of: date):
        cache_path = os.path.join(CRAZY_CACHE_DIR, f"reddit_activity_{as_of.strftime('%Y%m%d')}.json")

        def _fetch():
            activity = {}
            for subreddit in ["/r/gaming/new", "/r/pcgaming/new", "/r/games/new"]:
                activity[subreddit] = safe_download(f"https://www.reddit.com{subreddit}", max_retries=3).json()["data"]["children"]
            for subreddit in ["/r/gaming/comments", "/r/pcgaming/comments", "/r/games/comments"]:
                activity[subreddit] = safe_download(f"https://www.reddit.com{subreddit}", max_retries=3).json()["data"]["children"]
            return activity

        return cached_fetch(cache_path, ttl_hours=1, fetch_fn=_fetch)

    def compute_signal(self, as_of: date, state: dict, historical: bool = False):
        activity = self._fetch_reddit_activity(as_of)
        if not activity:
            return "HOLD"

        total_activity = 0
        for subreddit, posts in activity.items():
            total_activity += len(posts)

        start_date = as_of - timedelta(days=7)
        activity_history = []
        while start_date <= as_of:
            daily_activity = self._fetch_reddit_activity(start_date)
            if daily_activity:
                daily_total = 0
                for subreddit, posts in daily_activity.items():
                    daily_total += len(posts)
                activity_history.append(daily_total)
            start_date += timedelta(days=1)

        if len(activity_history) < 7:
            return "HOLD"

        ma7 = sum(activity_history[-7:]) / 7
        if total_activity > ma7 * 1.5 and total_activity > 1000:
            return "RISK_ON"
        return "HOLD"

    def target_allocations(self, signal: str, state: dict, as_of: date):
        if signal == "RISK_ON":
            return {ticker: 0.2 for ticker in self.universe()}
        return None