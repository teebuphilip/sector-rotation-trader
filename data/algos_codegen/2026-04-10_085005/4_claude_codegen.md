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

    def _fetch_reddit_data(self):
        cache_path = os.path.join(CRAZY_CACHE_DIR, "reddit_activity.json")

        def _fetch():
            return fetch_reddit_activity(
                subreddits=["r/gaming", "r/pcgaming", "r/nvidia"],
                activity_types=["posts", "comments"],
                timezone="UTC",
                missing_data_handling="skip_day"
            )

        data = cached_fetch(cache_path, ttl_hours=1, fetch_fn=_fetch)
        return pd.DataFrame(data) if data else pd.DataFrame()

    def compute_signal(self, as_of: date, state: dict, historical: bool = False):
        df = self._fetch_reddit_data()
        if df.empty:
            return "HOLD"

        df["total"] = df["posts"] + df["comments"]
        df["exp_ma_7d"] = df["total"].ewm(span=7, adjust=False).mean()

        latest = df.iloc[-1]
        if (latest["total"] - latest["exp_ma_7d"]) / latest["exp_ma_7d"] > 0.5 and latest["exp_ma_7d"] > 100:
            return "RISK_ON"
        return "HOLD"

    def target_allocations(self, signal: str, state: dict, as_of: date):
        if signal == "RISK_ON":
            return {
                "ATVI": 0.2,
                "EA": 0.2,
                "NVDA": 0.2,
                "TTWO": 0.2,
                "MSFT": 0.2
            }
        return None

# Register the algo
from crazy.algos.registry import register_algo
register_algo(RedditGamingThreadSpike)