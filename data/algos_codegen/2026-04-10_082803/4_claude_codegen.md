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
    supports_historical_seed = True

    def universe(self):
        return ["ATVI", "EA", "NVDA", "TTWO"]

    def _fetch_reddit_data(self):
        cache_path = os.path.join(CRAZY_CACHE_DIR, "reddit_gaming_data.json")

        def _fetch():
            data = []
            for endpoint in [
                "https://api.pushshift.io/reddit/submission/search?subreddit=gaming&after=7d&size=1000",
                "https://api.pushshift.io/reddit/comment/search?subreddit=gaming&after=7d&size=1000",
                "https://api.pushshift.io/reddit/submission/search?subreddit=pcgaming&after=7d&size=1000",
                "https://api.pushshift.io/reddit/comment/search?subreddit=pcgaming&after=7d&size=1000",
                "https://api.pushshift.io/reddit/submission/search?subreddit=games&after=7d&size=1000",
                "https://api.pushshift.io/reddit/comment/search?subreddit=games&after=7d&size=1000"
            ]:
                response = safe_download(endpoint)
                data.extend(response["data"])
            return data

        data = cached_fetch(cache_path, ttl_hours=1, fetch_fn=_fetch)
        df = pd.DataFrame(data)
        df["created_utc"] = pd.to_datetime(df["created_utc"], unit="s")
        df["date"] = df["created_utc"].dt.date
        return df

    def _fetch_prices(self):
        prices = {}
        for ticker in self.universe():
            prices[ticker] = safe_download(f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1=-631123200&period2=32503680000&interval=1d&events=adjusted")
        return prices

    def compute_signal(self, as_of: date, state: dict, historical: bool = False):
        reddit_data = self._fetch_reddit_data()
        prices = self._fetch_prices()

        if reddit_data.empty or any(df.empty for df in prices.values()):
            return "HOLD"

        reddit_data = reddit_data[reddit_data["date"] <= as_of]
        if len(reddit_data) < 8:
            return "HOLD"

        reddit_data["score_sum"] = reddit_data["score"].sum()
        reddit_data["ma7"] = reddit_data["score_sum"].rolling(7).mean()
        latest = reddit_data.iloc[-1]
        if latest["score_sum"] > 1.5 * latest["ma7"]:
            return "RISK_ON"
        return "HOLD"

    def target_allocations(self, signal: str, state: dict, as_of: date):
        if signal == "RISK_ON":
            return {ticker: 0.25 for ticker in self.universe()}
        return None