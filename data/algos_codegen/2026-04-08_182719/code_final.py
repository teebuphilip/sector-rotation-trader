# crazy/algos/reddit_gaming_thread_spike.py

import pandas as pd
from datetime import datetime, timedelta
from typing import List
from crazy.utils.cache import cached_fetch
from crazy.utils.data_sources import RedditAPI, YahooFinanceAPI
from crazy.algos.algo_base import AlgoBase

ALGO_ID = "reddit-gaming-thread-spike"
ALGO_NAME = "Reddit Gaming Thread Spike"
ENTRY_TARGETS = ["ATVI", "EA", "NVDA"]
SUBREDDITS = ["r/gaming", "r/pcgaming", "r/games"]
ACTIVITY_THRESHOLD = 1000
ACTIVITY_INCREASE_THRESHOLD = 50
MAX_TOTAL_EXPOSURE = 0.2
STOP_LOSS = -0.1
TAKE_PROFIT = 0.2

class RedditGamingThreadSpikeAlgo(AlgoBase):
    algo_id = ALGO_ID
    name = ALGO_NAME
    universe = lambda self: ENTRY_TARGETS
    rebalance_frequency = "daily"

    def compute_signal(self, context):
        # Fetch Reddit data
        reddit_data = self._fetch_reddit_data()
        total_posts_and_comments = reddit_data["total_posts_and_comments"].iloc[-1]
        ma_7d = reddit_data["total_posts_and_comments"].rolling(7).mean().iloc[-1]
        daily_pct_change = (total_posts_and_comments - ma_7d) / ma_7d * 100

        # Trigger signal if activity spike meets criteria
        signal_triggered = (daily_pct_change > ACTIVITY_INCREASE_THRESHOLD) and (total_posts_and_comments > ACTIVITY_THRESHOLD)

        return {"signal_triggered": signal_triggered, "signal_value": daily_pct_change}

    def target_allocations(self, context):
        if context["signal_triggered"]:
            total_exposure = sum(context["portfolio"]["positions"].values())
            if total_exposure + MAX_TOTAL_EXPOSURE <= MAX_TOTAL_EXPOSURE:
                return {asset: MAX_TOTAL_EXPOSURE / len(ENTRY_TARGETS) for asset in ENTRY_TARGETS}
            else:
                scaling_factor = (MAX_TOTAL_EXPOSURE - total_exposure) / len(ENTRY_TARGETS)
                return {asset: scaling_factor for asset in ENTRY_TARGETS}
        else:
            return {asset: 0.0 for asset in ENTRY_TARGETS}

    def exit_conditions(self, context):
        # Exit if activity falls below 90% of 7-day average or 5 trading days have passed
        reddit_data = self._fetch_reddit_data()
        total_posts_and_comments = reddit_data["total_posts_and_comments"].iloc[-1]
        ma_7d = reddit_data["total_posts_and_comments"].rolling(7).mean().iloc[-1]
        if total_posts_and_comments < 0.9 * ma_7d or len(context["portfolio"]["positions"]) >= 5:
            return True
        else:
            return False

    def risk_management(self, context):
        # Apply stop loss and take profit
        for asset, position in context["portfolio"]["positions"].items():
            current_price = self.get_current_price(asset)
            if current_price < position["entry_price"] * (1 + STOP_LOSS):
                return {"action": "sell", "asset": asset}
            elif current_price > position["entry_price"] * (1 + TAKE_PROFIT):
                return {"action": "sell", "asset": asset}
        return None

    def _fetch_reddit_data(self):
        # Use cached_fetch to fetch Reddit data and save to CRAZY_CACHE_DIR
        today = datetime.now(tz=datetime.utcnow().tzinfo).date()
        start_date = today - timedelta(days=7)
        reddit_data = cached_fetch(
            f"reddit_gaming_thread_spike_{start_date}_{today}",