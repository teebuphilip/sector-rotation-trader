from datetime import date, timedelta
from typing import Literal
import os
import pandas as pd
from crazy.algos.base import CrazyAlgoBase
from crazy.blocked import record_blocked
from crazy.utils import cached_fetch
from crazy.config import CRAZY_CACHE_DIR
from scanner import safe_download

class RedditGamingThreadSpike(CrazyAlgoBase):
    algo_id = "reddit-gaming-thread-spike"
    name = "Reddit Gaming Thread Spike"
    rebalance_frequency = "daily"
    supports_historical_seed = False

    def universe(self):
        return ["ATVI", "EA", "NVDA"]

    def compute_signal(self, as_of: date, state: dict, historical: bool = False) -> Literal["RISK_ON", "HOLD"]:
        reddit_api_key = os.getenv("REDDIT_API_KEY")
        if not reddit_api_key:
            record_blocked(self.algo_id, self.name, ["REDDIT_API_KEY"], "Missing REDDIT_API_KEY")
            return "HOLD"

        cache_path = f"{CRAZY_CACHE_DIR}/reddit_activity_{as_of.strftime('%Y%m%d')}.json"
        activity_data = cached_fetch(
            cache_path,
            ttl_hours=1,
            fetch_fn=lambda: self._fetch_reddit_activity(as_of, reddit_api_key),
        )

        if activity_data is None:
            return "HOLD"

        ma7 = activity_data["total_activity"].rolling(7).mean()
        spike_threshold = 1.5
        min_baseline = 100

        if (
            activity_data["total_activity"].iloc[-1] >= min_baseline
            and activity_data["total_activity"].iloc[-1] >= spike_threshold * ma7.iloc[-1]
        ):
            return "RISK_ON"
        else:
            return "HOLD"

    def target_allocations(self, signal: Literal["RISK_ON", "HOLD"], state: dict, as_of: date) -> dict | None:
        if signal == "RISK_ON":
            return {
                "ATVI": 0.05,
                "EA": 0.05,
                "NVDA": 0.05,
            }
        return None

    def _fetch_reddit_activity(self, as_of: date, reddit_api_key: str) -> pd.DataFrame:
        subreddits = ["r/gaming", "r/pcgaming", "r/games"]
        activity_data = []
        total_activity = 0
        for subreddit in subreddits:
            url = f"https://api.pushshift.io/reddit/submission/search/?subreddit={subreddit}&after={as_of - timedelta(days=7)}&before={as_of + timedelta(days=1)}&sort=asc&sort_type=created_utc"
            response = safe_download(url, headers={"Authorization": f"Bearer {reddit_api_key}"})
            data = response.json()
            post_count = len(data["data"])
            comment_count = 0  # Comments need to be fetched separately
            activity_data.append({"subreddit": subreddit, "post_count": post_count, "comment_count": comment_count})
            total_activity += post_count + comment_count

        df = pd.DataFrame(activity_data)
        df["total_activity"] = total_activity
        return df

REGISTRY_CHANGE = """
from .reddit_gaming_thread_spike import RedditGamingThreadSpike

CRAZY_ALGOS = [
    RedditGamingThreadSpike,
]
"""

BLOCKED_ALGO_ENTRY = {
    "date": "2026-04-08",
    "algo_id": "reddit-gaming-thread-spike",
    "name": "Reddit Gaming Thread Spike",
    "required_keys": ["REDDIT_API_KEY"]
}