from datetime import date
import os
import pandas as pd
from crazy.algos.base import CrazyAlgoBase
from crazy.utils import cached_fetch
from crazy.config import CRAZY_CACHE_DIR
from crazy.adapters.reddit_activity import fetch_reddit_activity

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

        data = fetch_reddit_activity(subreddits=subreddits, days_back=days_back)
        return pd.DataFrame(data) if data else pd.DataFrame()

    def compute_signal(self, as_of: date, state: dict, historical: bool = False):
        subreddits = ["gaming", "pcgaming", "nvidia", "callofduty", "battlefield"]
        df = self._fetch_reddit_activity(subreddits, days_back=7)
        if df.empty:
            return "HOLD"

        df["total"] = df["posts"] + df["comments"]
        df["ma7"] = df["total"].rolling(7).mean()

        latest = df.iloc[-1]
        if latest["total"] > 1.5 * latest["ma7"] and latest["ma7"] > 100:
            return "RISK_ON"
        return "HOLD"

    def target_allocations(self, signal: str, state: dict, as_of: date):
        if signal == "RISK_ON":
            return {t: 0.02 for t in self.universe()}
        return None