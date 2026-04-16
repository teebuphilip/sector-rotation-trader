Here's the implementation of the "reddit-gaming-thread-spike" algo in the sector-rotation-trader repo:

1. The new algo file: `crazy/algos/reddit_gaming_thread_spike.py`

```python
import datetime
import logging
from typing import List, Dict

import pandas as pd
from sector_rotation_trader.data.reddit import RedditData
from sector_rotation_trader.data.yahoo_finance import YahooFinanceData
from sector_rotation_trader.utils.cache import cached_fetch

logger = logging.getLogger(__name__)

ALGO_ID = "reddit-gaming-thread-spike"
ALGO_NAME = "Reddit Gaming Thread Spike"


class RedditGamingThreadSpikeAlgo:
    def __init__(self, config: Dict):
        self.config = config
        self.reddit = RedditData(config["reddit"])
        self.yahoo = YahooFinanceData(config["yahoo_finance"])

    def algo_id(self) -> str:
        return ALGO_ID

    def name(self) -> str:
        return ALGO_NAME

    def universe(self) -> List[str]:
        return self.config["yahoo_finance"]["tickers"]

    def compute_signal(self) -> pd.DataFrame:
        reddit_data = self._get_reddit_data()
        yahoo_data = self._get_yahoo_data()
        combined_data = self._combine_data(reddit_data, yahoo_data)
        signal = self._calculate_signal(combined_data)
        return signal

    def target_allocations(self, signal: pd.DataFrame) -> Dict[str, float]:
        signal_threshold = self.config["signal_logic"]["trigger"]["threshold"]
        signal_above_threshold = signal[signal["signal"] >= signal_threshold]
        total_exposure = self.config["position_sizing"]["max_total_exposure"]
        max_per_ticker = self.config["position_sizing"]["max_per_ticker"]
        allocations = {}
        for ticker in signal_above_threshold.index:
            allocation = min(self.config["position_sizing"]["allocation_per_signal"], max_per_ticker, total_exposure / len(signal_above_threshold))
            allocations[ticker] = allocation
        return allocations

    def rebalance_frequency(self) -> str:
        return self.config["frequency"]

    def _get_reddit_data(self) -> pd.DataFrame:
        subreddits = self.config["reddit"]["subreddits"]
        min_activity_threshold = self.config["reddit"]["min_activity_threshold"]
        return self.reddit.get_subreddit_activity(subreddits, min_activity_threshold)

    def _get_yahoo_data(self) -> pd.DataFrame:
        tickers = self.config["yahoo_finance"]["tickers"]
        fields = self.config["yahoo_finance"]["fields"]
        return self.yahoo.get_data(tickers, fields)

    def _combine_data(self, reddit_data: pd.DataFrame, yahoo_data: pd.DataFrame) -> pd.DataFrame:
        return pd.merge(reddit_data, yahoo_data, left_index=True, right_index=True, how="inner")

    def _calculate_signal(self, data: pd.DataFrame) -> pd.DataFrame:
        metric = self.config["signal_logic"]["metric"]
        weighting = self.config["signal_logic"]["metric_details"]["weighting"]
        filtering = self.config["signal_logic"]["metric_details"]["filtering"]

        data["total_posts_and_comments"] = (data["posts"] * weighting["posts"]) + (data["comments"] * weighting["comments"])
        data["baseline_total"] = data["total_posts_and_comments"].rolling(self.config["signal_logic"]["trigger"]["baseline_period"]).mean()
        data["percentage_change"] = (data["total_posts_and_comments"] - data["baseline_total"]) / data["baseline_total"] * 100
        data["signal"] = 0
        data.loc[data["percentage_change"] >= self.config["signal_logic"]["trigger"]["threshold"], "signal"] = 1

        if filtering["spam"]:
            data.loc[data["is_spam"], "signal"] = 0
        if filtering