from datetime import datetime, timedelta
from typing import Any, Dict, List

import pandas as pd
from crazy.algos.base import CrazyAlgoBase
from crazy.blocked import record_blocked
from crazy.utils import cached_fetch

REDDIT_API_RETRIES = 3
YAHOO_FINANCE_FALLBACK_DAYS = 5

class RedditGamingThreadSpikeAlgo(CrazyAlgoBase):
    def __init__(self):
        self.subreddits = ["r/gaming", "r/pcgaming", "r/games"]
        self.tickers = ["ATVI", "EA", "NVDA", "TTWO", "MSFT"]
        self.gaming_hardware_stocks = ["NVDA"]
        self.gaming_publisher_stocks = ["ATVI", "EA", "TTWO", "MSFT"]
        self.post_exit_cooldown = 7

    def universe(self) -> List[str]:
        return self.tickers

    def compute_signal(self, as_of: datetime, state: Dict[str, Any], historical: bool = False) -> str:
        try:
            reddit_data = self._fetch_reddit_data(as_of)
            if reddit_data is None:
                return "HOLD/{}"

            total_posts_plus_comments = reddit_data["total_posts_plus_comments"].sum()
            avg_posts_plus_comments = reddit_data["total_posts_plus_comments"].rolling(7).mean().iloc[-1]
            pct_change = (total_posts_plus_comments - avg_posts_plus_comments) / avg_posts_plus_comments

            if pct_change > 0.5 and total_posts_plus_comments > 100:
                return "signal_trigger"
            else:
                return "HOLD/{}"
        except Exception as e:
            record_blocked(self.id, str(e))
            return "HOLD/{}"

    def target_allocations(self, signal: str, state: Dict[str, Any], as_of: datetime) -> Dict[str, float] | None:
        if signal == "signal_trigger":
            allocations = {
                ticker: 0.05 for ticker in self.gaming_hardware_stocks + self.gaming_publisher_stocks
            }
            return allocations
        else:
            return None

    def _fetch_reddit_data(self, as_of: datetime) -> pd.DataFrame | None:
        data = {}
        for subreddit in self.subreddits:
            key = f"{subreddit}_total_posts_plus_comments"
            data[key] = self._fetch_reddit_activity(subreddit, as_of)
            if data[key] is None:
                return None

        return pd.DataFrame(data)

    def _fetch_reddit_activity(self, subreddit: str, as_of: datetime) -> int | None:
        for _ in range(REDDIT_API_RETRIES):
            try:
                return cached_fetch(
                    f"reddit_activity_{subreddit}_{as_of.date()}",
                    lambda: self._fetch_reddit_activity_impl(subreddit, as_of),
                    "CRAZY_CACHE_DIR",
                )
            except Exception as e:
                record_blocked(self.id, str(e))
        return None

    def _fetch_reddit_activity_impl(self, subreddit: str, as_of: datetime) -> int:
        # Fetch Reddit data and compute total posts + comments
        # Implement the logic to fetch data from the Reddit API and process it
        # Return the total posts + comments count for the given subreddit and date
        raise NotImplementedError()