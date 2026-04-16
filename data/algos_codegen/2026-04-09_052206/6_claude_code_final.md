from datetime import date, timedelta
import os
import pandas as pd
from crazy.algos.base import CrazyAlgoBase
from crazy.blocked import record_blocked
from crazy.utils import cached_fetch
from crazy.config import CRAZY_CACHE_DIR
from scanner import safe_download

class RedditGamingThreadSpike(CrazyAlgoBase):
    algo_id = "reddit-gaming-thread-spike"
    name = "Reddit Gaming Thread Spike"
    rebalance_frequency = "daily"
    supports_historical_seed = False

    def universe(self):
        return ["ATVI", "EA", "NVDA", "TTWO", "MSFT"]

    def compute_signal(self, as_of: date, state: dict, historical: bool = False):
        cache_path = os.path.join(CRAZY_CACHE_DIR, "reddit_activity.json")
        data = cached_fetch(cache_path, ttl_hours=1, fetch_fn=self._fetch_reddit_data)
        if not data:
            record_blocked(self.algo_id, self.name, [], "Failed to fetch Reddit data")
            return "HOLD"

        df = pd.DataFrame(data)
        df["total_activity"] = df["num_comments"] + 1  # Assuming 1 post per comment
        df = df.groupby(pd.to_datetime(df["created_utc"], unit="s").dt.date)["total_activity"].sum().reset_index()
        ma = df["total_activity"].rolling(self.signalLogic["thresholds"]["movingAverage"]).mean()
        pct_change = (df["total_activity"].iloc[-1] - ma.iloc[-1]) / ma.iloc[-1] * 100

        if pct_change > self.signalLogic["thresholds"]["percentIncrease"] and df["total_activity"].iloc[-1] > self.signalLogic["thresholds"]["minBaselineActivity"]:
            return "RISK_ON"
        else:
            return "HOLD"

    def target_allocations(self, signal: str, state: dict, as_of: date):
        if signal == "RISK_ON":
            return {"ATVI": 0.2, "EA": 0.2, "NVDA": 0.1, "TTWO": 0.1, "MSFT": 0.1}
        return None

    def _fetch_reddit_data(self):
        data = []
        for endpoint in [
            "https://www.reddit.com/r/gaming/new.json",
            "https://www.reddit.com/r/pcgaming/new.json",
            "https://www.reddit.com/r/games/new.json"
        ]:
            resp = safe_download(endpoint)
            if resp.status_code == 200:
                for post in resp.json()["data"]["children"]:
                    data.append({
                        "title": post["data"]["title"],
                        "num_comments": post["data"]["num_comments"],
                        "created_utc": post["data"]["created_utc"]
                    })
        return data

REGISTRY_CHANGE = [
    RedditGamingThreadSpike
]