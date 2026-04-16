from datetime import date
import os
import pandas as pd
from crazy.algos.base import CrazyAlgoBase
from crazy.utils import cached_fetch
from crazy.config import CRAZY_CACHE_DIR
from crazy.adapters.reddit_activity import fetch_reddit_activity
from crazy.adapters.yahoo_finance import safe_download

class RedditGamingThreadSpike(CrazyAlgoBase):
    algo_id = "reddit-gaming-thread-spike"
    name = "Reddit Gaming Thread Spike"
    rebalance_frequency = "daily"
    supports_historical_seed = False

    def universe(self):
        return ["ATVI", "EA", "NVDA", "TTWO", "MSFT"]

    def _fetch_reddit_data(self):
        cache_path = os.path.join(CRAZY_CACHE_DIR, "reddit_gaming_data.json")

        def _fetch():
            subreddits = ["r/gaming", "r/pcgaming", "r/games"]
            data = fetch_reddit_activity(subreddits, filter_bots=True, filter_spam=True, only_new=True)
            return data

        data = cached_fetch(cache_path, ttl_hours=1, fetch_fn=_fetch)
        return pd.DataFrame(data) if data else pd.DataFrame()

    def _fetch_yahoo_data(self):
        cache_path = os.path.join(CRAZY_CACHE_DIR, "yahoo_gaming_prices.json")

        def _fetch():
            tickers = self.universe()
            prices = safe_download(tickers, ["adjusted_close"])
            return prices

        data = cached_fetch(cache_path, ttl_hours=1, fetch_fn=_fetch)
        return data if data is not None else pd.DataFrame()

    def compute_signal(self, as_of: date, state: dict, historical: bool = False):
        reddit_df = self._fetch_reddit_data()
        yahoo_df = self._fetch_yahoo_data()

        if reddit_df.empty or yahoo_df.empty:
            return "HOLD"

        reddit_df = reddit_df[reddit_df["date"] <= pd.Timestamp(as_of)]
        yahoo_df = yahoo_df[yahoo_df.index <= pd.Timestamp(as_of)]

        if len(reddit_df) < 7 or len(yahoo_df) < 7:
            return "HOLD"

        reddit_df["posts_ma7"] = reddit_df["new_posts_count"].rolling(7).mean()
        reddit_df["comments_ma7"] = reddit_df["new_comments_count"].rolling(7).mean()

        latest = reddit_df.iloc[-1]
        if (latest["new_posts_count"] >= 1.5 * latest["posts_ma7"] and
            latest["new_comments_count"] >= 1.5 * latest["comments_ma7"]):
            return "RISK_ON"

        return "HOLD"

    def target_allocations(self, signal: str, state: dict, as_of: date):
        if signal == "RISK_ON":
            return {ticker: 0.05 for ticker in self.universe()}
        return None