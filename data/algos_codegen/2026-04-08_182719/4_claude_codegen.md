Here's the implementation of the "reddit-gaming-thread-spike" algo in the sector-rotation-trader repo:

```python
# crazy/algos/reddit_gaming_thread_spike.py

import pandas as pd
from datetime import datetime, timedelta
from typing import List
from crazy.utils.cache import cached_fetch
from crazy.utils.data_sources import RedditAPI, YahooFinanceAPI
from crazy.algos.algo_base import AlgoBase

ALGO_ID = "reddit-gaming-thread-spike"
ALGO_NAME = "Reddit Gaming Thread Spike"
UNIVERSE = ["ATVI", "EA", "NVDA", "TTWO", "MSFT"]
SUBREDDITS = ["r/gaming", "r/pcgaming", "r/games"]
ACTIVITY_THRESHOLD = 1000
ACTIVITY_INCREASE_THRESHOLD = 50

class RedditGamingThreadSpikeAlgo(AlgoBase):
    algo_id = ALGO_ID
    name = ALGO_NAME
    universe = lambda self: UNIVERSE
    rebalance_frequency = "daily"

    def compute_signal(self, context):
        # Fetch Reddit data
        reddit_data = self._fetch_reddit_data()
        total_posts_and_comments = reddit_data["total_posts_and_comments"].iloc[-1]
        ma_7d = reddit_data["total_posts_and_comments"].rolling(7).mean().iloc[-1]
        daily_pct_change = (total_posts_and_comments - ma_7d) / ma_7d * 100

        # Trigger signal if activity spike meets criteria
        signal_triggered = (daily_pct_change > ACTIVITY_INCREASE_THRESHOLD) and (total_posts_and_comments > ACTIVITY_THRESHOLD)

        return {"signal_triggered": signal_triggered}

    def target_allocations(self, context):
        if context["signal_triggered"]:
            return {asset: 0.05 for asset in UNIVERSE}
        else:
            return {asset: 0.0 for asset in UNIVERSE}

    def _fetch_reddit_data(self):
        # Use cached_fetch to fetch Reddit data and save to CRAZY_CACHE_DIR
        today = datetime.now().date()
        start_date = today - timedelta(days=7)
        reddit_data = cached_fetch(
            f"reddit_gaming_thread_spike_{start_date}_{today}",
            lambda: self._get_reddit_activity_data(start_date, today),
            expires_after=timedelta(days=1)
        )
        return reddit_data

    def _get_reddit_activity_data(self, start_date: datetime, end_date: datetime) -> pd.DataFrame:
        reddit_api = RedditAPI()
        data = []
        for subreddit in SUBREDDITS:
            subreddit_data = reddit_api.get_post_and_comment_counts(subreddit, start_date, end_date)
            data.append(subreddit_data)
        df = pd.concat(data, ignore_index=True)
        df["total_posts_and_comments"] = df["posts"] + df["comments"]
        df = df.groupby("date")["total_posts_and_comments"].sum().reset_index()
        return df
```

Registry change:
```python
# crazy/algos/registry.py
from crazy.algos.reddit_gaming_thread_spike import RedditGamingThreadSpikeAlgo

ALGOS = [
    RedditGamingThreadSpikeAlgo,
    # Other algos...
]
```

The algo is blocked due to the requirement of the Reddit API, so we need to add it to the `data/blocked/algos.jsonl` file:

```json
{"date":"2023-04-24","algo_id":"reddit-gaming-thread-spike","name":"Reddit Gaming Thread Spike","required_keys":["reddit"]}
```

This implementation follows the provided scaffold and constraints:

1. The algo file `crazy/algos/reddit_gaming_thread_spike.py` contains the full code for the new algo.
2. The minimal registry change is added to `crazy/algos/registry.py`.