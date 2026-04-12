from datetime import date
import pandas as pd
from crazy.algos.base import CrazyAlgoBase
from crazy.adapters.reddit_activity import fetch_reddit_activity


class RedditSubredditMentionSpikeAlgo(CrazyAlgoBase):
    algo_id = "reddit-subreddit-mention-spike"
    name = "Reddit Subreddit Mention Spike"
    rebalance_frequency = "daily"
    supports_historical_seed = False

    def universe(self):
        return ["TSLA", "AAPL", "GME", "AMC", "NVDA", "MSFT", "AMD"]

    def compute_signal(self, as_of: date, state: dict, historical: bool = False):
        # === SIGNAL_LOGIC_START ===
        try:
            data = fetch_reddit_activity(subreddits=["r/gaming", "r/pcgaming", "r/games"], days_back=14)
            df = data if isinstance(data, pd.DataFrame) else pd.DataFrame()
            if df.empty:
                return "HOLD"
            df["total"] = df["posts"] + df["comments"]
            df = df.sort_values("date").reset_index(drop=True)
            if len(df) < 8:
                return "HOLD"
            latest = df.iloc[-1]
            ma7 = df["total"].iloc[-8:-1].mean()
            if ma7 == 0 or pd.isna(ma7):
                return "HOLD"
            position = self.position()
            if position and position.get("entry_date"):
                days_held = (latest["date"] - position["entry_date"]).days
                if latest["total"] < ma7 or days_held >= 5:
                    return "RISK_OFF"
                return "HOLD"
            if latest["total"] > 1.5 * ma7:
                return "RISK_ON"
            return "HOLD"
        except Exception:
            return "HOLD"
# === SIGNAL_LOGIC_END ===

    def target_allocations(self, signal: str, state: dict, as_of: date):
        # === ALLOCATION_LOGIC_START ===
        if signal == "RISK_ON":
            targets = [t for t in self.universe() if t in {"ATVI", "EA", "NVDA"}]
            if not targets:
                return {}
            weight = 0.05
            allocation = {t: weight for t in targets}
            total_alloc = sum(allocation.values())
            if total_alloc > 0.20:
                scale = 0.20 / total_alloc
                allocation = {k: v * scale for k, v in allocation.items()}
            return allocation
        if signal == "RISK_OFF":
            return {}
        return {}
# === ALLOCATION_LOGIC_END ===