1. The full code for the new algo file:

```python
import datetime
import logging
from typing import List

import pandas as pd
from crazy.utils.cache import cached_fetch
from crazy.utils.data import get_reddit_data, get_yahoo_finance_data
from crazy.utils.signals import percentage_increase

logger = logging.getLogger(__name__)

ALGO_ID = "reddit-gaming-thread-spike"
ALGO_NAME = "Reddit Gaming Thread Spike"

SUBREDDITS = ["r/gaming", "r/pcgaming", "r/games"]
TICKERS = ["ATVI", "EA", "NVDA", "TTWO", "MSFT"]
TIMEZONE = "UTC"
DAILY_CUTOFF = "00:00"

METRIC_NAME = "total_posts_plus_comments"
METRIC_DESCRIPTION = "Sum of all new posts and comments (including replies) across target subreddits, excluding deleted content"

TRIGGER_CONDITION = "percentage_increase"
TRIGGER_THRESHOLD = 50
TRIGGER_BASELINE = "previous_7day_average"
TRIGGER_MINIMUM_VOLUME = 100

ENTRY_CONDITION = "signal_trigger"
ENTRY_INSTRUMENTS = ["ATVI", "EA", "NVDA"]

EXIT_CONDITIONS = [
    {"name": "below_7day_average", "threshold": 0.95},
    {"name": "after_5_trading_days"}
]
EXIT_WHICHEVER = "comes_first"

ALLOCATION_PER_SIGNAL = 0.05
MAX_TOTAL_EXPOSURE = 0.20


class RedditGamingThreadSpikeAlgo:
    algo_id = ALGO_ID
    name = ALGO_NAME

    def universe(self) -> List[str]:
        return TICKERS

    def compute_signal(self) -> pd.DataFrame:
        reddit_data = self._get_reddit_data()
        yahoo_data = self._get_yahoo_finance_data()

        signal = self._calculate_signal(reddit_data)
        signal = self._merge_with_prices(signal, yahoo_data)
        return signal

    def target_allocations(self, signal: pd.DataFrame) -> pd.DataFrame:
        signal = signal.copy()
        signal["target_weight"] = 0.0
        signal.loc[signal["signal_triggered"], "target_weight"] = ALLOCATION_PER_SIGNAL
        signal["max_total_exposure"] = MAX_TOTAL_EXPOSURE
        return signal

    def rebalance_frequency(self) -> str:
        return "daily"

    def _get_reddit_data(self) -> pd.DataFrame:
        data = get_reddit_data(
            subreddits=SUBREDDITS,
            timezone=TIMEZONE,
            daily_cutoff=DAILY_CUTOFF,
            cache_dir=CRAZY_CACHE_DIR,
        )
        return data

    def _get_yahoo_finance_data(self) -> pd.DataFrame:
        data = get_yahoo_finance_data(
            tickers=TICKERS,
            cache_dir=CRAZY_CACHE_DIR,
        )
        return data

    def _calculate_signal(self, reddit_data: pd.DataFrame) -> pd.DataFrame:
        signal = reddit_data.groupby("date")[["posts", "comments"]].sum().reset_index()
        signal["total_posts_plus_comments"] = signal["posts"] + signal["comments"]
        signal["signal_triggered"] = percentage_increase(
            signal["total_posts_plus_comments"],
            baseline=TRIGGER_BASELINE,
            threshold=TRIGGER_THRESHOLD,
            minimum_volume=TRIGGER_MINIMUM_VOLUME,
        )
        return signal

    def _merge_with_prices(self, signal: pd.DataFrame, yahoo_data: pd.DataFrame) -> pd.DataFrame:
        signal = signal.merge(yahoo_data, on="date", how="left")
        signal = signal.fillna(method="ffill")
        return signal
```

2. The minimal registry change:

```python
from crazy.algos.registry import register_algo
from crazy.algos.crazy.reddit_gaming_thread_spike import RedditGamingThreadSpikeAlgo

register_algo(RedditGamingThreadSpikeAlgo)
```

3. Since the algo requires Reddit and Yahoo Finance API keys, it needs to be added to the blocked algos list:

```json
{"date":"2023-04-26","algo_id":"reddit-gaming-thread-spike","name":"Reddit Gaming Thread Spike","required_keys":["reddit.subreddits","reddit.timezone","reddit.daily_cutoff","yahoo_finance.tickers"]}
```