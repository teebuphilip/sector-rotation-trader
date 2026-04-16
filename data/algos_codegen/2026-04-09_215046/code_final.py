from datetime import date
import os
import pandas as pd
from crazy.algos.base import CrazyAlgoBase
from crazy.utils import cached_fetch
from crazy.config import CRAZY_CACHE_DIR
from crazy.blocked import record_blocked
from crazy.adapters.reddit_activity import RedditActivityAdapter

class RedditGamingThreadSpike(CrazyAlgoBase):
    algo_id = "reddit-gaming-thread-spike"
    name = "Reddit Gaming Thread Spike"
    rebalance_frequency = "daily"
    supports_historical_seed = False

    def universe(self):
        return ["ATVI", "EA", "NVDA", "TTWO", "MSFT"]

    def _fetch_reddit_data(self):
        cache_path = os.path.join(CRAZY_CACHE_DIR, "reddit_gaming_data.json")
        reddit_api_key = os.getenv("REDDIT_API_KEY")
        if not reddit_api_key:
            record_blocked(self.algo_id, self.name, ["REDDIT_API_KEY"], "Missing REDDIT_API_KEY")
            return pd.DataFrame()

        adapter = RedditActivityAdapter(
            subreddits=["r/gaming", "r/pcgaming", "r/games"],
            data_fields=["post_count", "comment_count", "sentiment_score"],
            data_quality_filters=["exclude_deleted_posts", "exclude_low_quality_posts"],
            api_key=reddit_api_key
        )

        data = cached_fetch(cache_path, ttl_hours=1, fetch_fn=adapter.fetch)
        return pd.DataFrame(data) if data else pd.DataFrame()

    def compute_signal(self, as_of: date, state: dict, historical: bool = False):
        df = self._fetch_reddit_data()
        if df.empty:
            return "HOLD"

        df["total_posts_and_comments"] = df["post_count"] + df["comment_count"]
        df["ma7"] = df["total_posts_and_comments"].rolling(7, min_periods=7).mean()
        latest = df.iloc[-1]

        if latest["total_posts_and_comments"] > 1.5 * df["ma7"].iloc[-7:].mean():
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

# Register the algo
from crazy.algos.registry import register_algo
register_algo(RedditGamingThreadSpike)