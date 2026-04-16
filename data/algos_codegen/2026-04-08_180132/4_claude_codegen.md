Here's the implementation of the "reddit-gaming-thread-spike" algo in the `crazy/algos/reddit_gaming_thread_spike.py` file:

```python
import numpy as np
from datetime import datetime, timedelta
from typing import List, Dict
from crazy.utils.cache import cached_fetch
from crazy.utils.data import get_yahoo_data
from crazy.utils.time import get_trading_days

ALGO_ID = "reddit-gaming-thread-spike"
ALGO_NAME = "Reddit Gaming Thread Spike"
UNIVERSE = ["ATVI", "EA", "NVDA", "TTWO", "MSFT"]
SUBREDDITS = ["r/gaming", "r/pcgaming", "r/games"]
COOLDOWN_DAYS = 3
SIGNAL_THRESHOLD = 0.5
ACTIVITY_THRESHOLD = 1000

class RedditGamingThreadSpikeAlgo:
    def __init__(self):
        self.algo_id = ALGO_ID
        self.name = ALGO_NAME
        self.universe = UNIVERSE
        self.cooldown_days = COOLDOWN_DAYS
        self.signal_threshold = SIGNAL_THRESHOLD
        self.activity_threshold = ACTIVITY_THRESHOLD

    def compute_signal(self, date: datetime) -> Dict[str, float]:
        signal = {}
        for ticker in self.universe:
            signal[ticker] = 0.0

        reddit_data = self._get_reddit_data(date)
        if reddit_data is None:
            return signal

        total_activity = reddit_data["total_posts_and_comments"]
        avg_activity = reddit_data["avg_posts_and_comments"]
        signal_value = (total_activity - avg_activity) / avg_activity

        if signal_value > self.signal_threshold and total_activity > self.activity_threshold:
            for ticker in self.universe:
                signal[ticker] = 1.0

        return signal

    def target_allocations(self, date: datetime, current_positions: Dict[str, float]) -> Dict[str, float]:
        signal = self.compute_signal(date)
        allocations = {ticker: 0.05 * signal[ticker] for ticker in self.universe}
        total_allocation = sum(allocations.values())
        if total_allocation > 0.2:
            for ticker, alloc in allocations.items():
                allocations[ticker] = alloc / total_allocation * 0.2
        return allocations

    def rebalance_frequency(self) -> str:
        return "daily"

    def _get_reddit_data(self, date: datetime) -> Dict[str, float]:
        data = {}
        for subreddit in SUBREDDITS:
            url = f"https://api.pushshift.io/reddit/submission/search/?subreddit={subreddit}&after={date.strftime('%Y-%m-%d')}&before={(date + timedelta(days=1)).strftime('%Y-%m-%d')}&size=1000"
            posts = cached_fetch(url, f"reddit_{subreddit}_{date.strftime('%Y-%m-%d')}")
            data[subreddit] = len(posts)

        total_posts_and_comments = sum(data.values())

        # Calculate 7-day moving average
        trading_days = get_trading_days(date - timedelta(days=6), date)
        avg_posts_and_comments = 0
        for i in range(7):
            reddit_data = self._get_reddit_data(date - timedelta(days=i))
            if reddit_data is not None:
                avg_posts_and_comments += sum(reddit_data.values())
        avg_posts_and_comments /= len(trading_days)

        return {"total_posts_and_comments": total_posts_and_comments, "avg_posts_and_comments": avg_posts_and_comments}
```

And the minimal registry change in `crazy/algos/registry.py`:

```python
from crazy.algos.reddit_gaming_thread_spike import RedditGamingThreadSpikeAlgo

CRAZY_ALGOS = {
    "reddit-gaming-thread-spike": Re