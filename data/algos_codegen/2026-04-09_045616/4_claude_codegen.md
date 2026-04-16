Here's the implementation of the `reddit-gaming-thread-spike` algo in the `crazy/algos` directory:

```python
import pandas as pd
from datetime import datetime, timedelta
from typing import List, Dict
from crazy.algos.base import CrazyAlgoBase
from crazy.utils import cached_fetch
from crazy.blocked import record_blocked

SUBREDDIT_NAMES = ["gaming", "pcgaming", "games"]
TICKERS = ["ATVI", "EA", "NVDA", "TTWO"]
ACTIVITY_INCREASE_THRESHOLD = 0.5
MOVING_AVG_WINDOW = 7
MIN_ABSOLUTE_VOLUME = 1000
POSITION_ALLOCATION = 0.05
MAX_EXPOSURE = 0.2
ENTRY_DURATION = 10  # trading days

class RedditGamingThreadSpikeAlgo(CrazyAlgoBase):
    def __init__(self):
        self.reddit_data = {}
        self.price_data = {}

    def universe(self) -> List[str]:
        return TICKERS

    def compute_signal(self, as_of: datetime, state: Dict, historical: bool = False) -> str:
        try:
            reddit_data = self.fetch_reddit_data(as_of)
            price_data = self.fetch_price_data(as_of)
        except Exception as e:
            record_blocked(self.algo_id, self.name, ["reddit", "yahoo_finance"])
            return "HOLD/{}"

        total_activity = sum(reddit_data.values())
        avg_activity = reddit_data.rolling(MOVING_AVG_WINDOW).mean().iloc[-1]
        activity_increase = (total_activity - avg_activity) / avg_activity

        if activity_increase > ACTIVITY_INCREASE_THRESHOLD and total_activity > MIN_ABSOLUTE_VOLUME:
            return "BUY/{}"
        else:
            return "HOLD/{}"

    def target_allocations(self, signal: str, state: Dict, as_of: datetime) -> Dict[str, float] | None:
        if signal.startswith("BUY"):
            return {ticker: POSITION_ALLOCATION for ticker in TICKERS}
        elif signal.startswith("HOLD"):
            return None

    def fetch_reddit_data(self, as_of: datetime) -> Dict[str, float]:
        if as_of.date() not in self.reddit_data:
            data = {}
            for subreddit in SUBREDDIT_NAMES:
                url = f"https://api.pushshift.io/reddit/submission/search/?subreddit={subreddit}&after={as_of - timedelta(days=1)}&before={as_of}&size=1000"
                submissions = cached_fetch(url, CRAZY_CACHE_DIR)
                data[subreddit] = len(submissions)
            self.reddit_data[as_of.date()] = data
        return self.reddit_data[as_of.date()]

    def fetch_price_data(self, as_of: datetime) -> pd.DataFrame:
        if as_of.date() not in self.price_data:
            data = []
            for ticker in TICKERS:
                url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={as_of - timedelta(days=30)}&period2={as_of}&interval=1d&events=history&includeAdjustedClose=true"
                df = cached_fetch(url, CRAZY_CACHE_DIR)
                df = df.set_index("Date")
                data.append(df)
            self.price_data[as_of.date()] = pd.concat(data, axis=1, keys=TICKERS)
        return self.price_data[as_of.date()]
```

And the corresponding registry change in `crazy/algos/registry.py`:

```python
from .reddit_gaming_thread_spike import RedditGamingThreadSpikeAlgo

CRAZY_ALGOS = {
    "reddit-gaming-thread-spike": RedditGamingThreadSpikeAlgo,
}
```

Since the algo requires the Reddit API and Yahoo Finance API, which are not available in the repo, the algo is marked as blocked by adding the following line to `data/blocked/algos.jsonl`:

```json
{"date":"2023-04-08","algo_id":"reddit-gaming-thread-spike","name":"reddit-gaming-thread-spike","required_keys":["reddit","yahoo_finance"]}
```

This sets `supports_historical_seed = False` for the algo, as it cannot be run without the required API keys.