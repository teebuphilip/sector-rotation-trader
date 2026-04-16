from datetime import date, timedelta
import pandas as pd
from crazy.algos.base import CrazyAlgoBase
from crazy.blocked import record_blocked
from crazy.utils import cached_fetch
from config import CRAZY_CACHE_DIR

class RedditGamingThreadSpikeAlgo(CrazyAlgoBase):
    algo_id = "reddit-gaming-thread-spike"
    name = "Reddit Gaming Thread Spike"
    rebalance_frequency = "daily"
    supports_historical_seed = False

    def universe(self):
        return ["ATVI", "EA", "NVDA", "TTWO", "MSFT"]

    def compute_signal(self, as_of: date, state: dict, historical: bool = False):
        reddit_api_key = self.get_required_key("redditApiKey")
        if not reddit_api_key:
            record_blocked(self.algo_id, self.name, ["redditApiKey"], "Missing redditApiKey")
            return "HOLD"

        min_post_volume = self.get_required_key("minPostVolume")
        min_comment_volume = self.get_required_key("minCommentVolume")
        post_percent_increase = self.get_required_key("postPercentIncrease")
        comment_percent_increase = self.get_required_key("commentPercentIncrease")
        post_moving_average = self.get_required_key("postMovingAverage")
        comment_moving_average = self.get_required_key("commentMovingAverage")

        subreddit_data = self.fetch_reddit_data(as_of)
        if subreddit_data is None:
            return "HOLD"

        post_volume = subreddit_data["num_posts"].sum()
        comment_volume = subreddit_data["num_comments"].sum()

        post_ma = subreddit_data["num_posts"].rolling(post_moving_average).mean().iloc[-1]
        comment_ma = subreddit_data["num_comments"].rolling(comment_moving_average).mean().iloc[-1]

        post_percent_change = (post_volume - post_ma) / post_ma * 100
        comment_percent_change = (comment_volume - comment_ma) / comment_ma * 100

        if post_percent_change >= post_percent_increase and post_volume >= min_post_volume:
            return "RISK_ON"
        elif comment_percent_change >= comment_percent_increase and comment_volume >= min_comment_volume:
            return "RISK_ON"
        else:
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

    def fetch_reddit_data(self, as_of: date):
        reddit_api_key = self.get_required_key("redditApiKey")
        subreddit_urls = [
            "r/gaming/new",
            "r/pcgaming/new",
            "r/games/new"
        ]
        fields = [
            "num_comments",
            "num_crossposts",
            "num_reports",
            "num_awards",
            "created_utc"
        ]
        rate_limit = {
            "maxRequests": 60,
            "windowMs": 60000
        }

        data = []
        for url in subreddit_urls:
            url_data = cached_fetch(
                f"{CRAZY_CACHE_DIR}/reddit_{url.replace('/', '_')}_{as_of.isoformat()}.json",
                lambda: self.fetch_reddit_api_data(url, fields, reddit_api_key, rate_limit),
                ttl=timedelta(days=1)
            )
            if url_data is None:
                return None
            data.append(url_data)

        df = pd.concat(data, ignore_index=True)
        df["created_date"] = pd.to_datetime(df["created_utc"], unit="s").dt.date
        df["num_posts"] = 1
        return df.groupby("created_date")[fields + ["num_posts"]].sum().reset_index()

    def fetch_reddit_api_data(self, url, fields, api_key, rate_limit):
        # Implement Reddit API call with rate limiting
        pass