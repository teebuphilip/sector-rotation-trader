from datetime import date
import os
import pandas as pd
from crazy.algos.base import CrazyAlgoBase
from crazy.utils import cached_fetch
from crazy.config import CRAZY_CACHE_DIR
from crazy.blocked import record_blocked
from crazy.adapters.reddit_activity import fetch_reddit_activity

class RedditGamingThreadSpike(CrazyAlgoBase):
    algo_id = "reddit-gaming-thread-spike"
    name = "Reddit Gaming Thread Spike"
    rebalance_frequency = "daily"
    supports_historical_seed = False

    def universe(self):
        return ["ATVI", "EA", "NVDA", "TTWO", "MSFT"]

    @cached_fetch(os.path.join(CRAZY_CACHE_DIR, "reddit_activity.json"), ttl_hours=1)
    def _fetch_reddit_activity(self, as_of: date):
        reddit_api_key = os.getenv("REDDIT_API_KEY")
        if not reddit_api_key:
            record_blocked(self.algo_id, self.name, ["REDDIT_API_KEY"], "Missing REDDIT_API_KEY")
            return pd.DataFrame()

        data = fetch_reddit_activity(
            subreddits=["r/gaming", "r/pcgaming", "r/games"],
            post_and_comment_count_method="sum",
            timestamp_normalization="UTC",
            as_of=as_of
        )
        return pd.DataFrame(data)

    def compute_signal(self, as_of: date, state: dict, historical: bool = False):
        df = self._fetch_reddit_activity(as_of)
        if df.empty:
            return "HOLD"

        df = df[df["date"] <= pd.Timestamp(as_of)]
        if len(df) < 7:
            return "HOLD"

        df["ma7"] = df["value"].rolling(7).mean()
        latest = df.iloc[-1]
        if latest["value"] > 1.5 * latest["ma7"] and latest["value"] > 1000:
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