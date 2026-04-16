{
  "version": "1.0",
  "spec": {
    "id": "reddit-gaming-thread-spike",
    "name": "Reddit Gaming Thread Spike",
    "frequency": "daily",
    "universe": [
      "ATVI",
      "EA",
      "NVDA",
      "TTWO",
      "MSFT"
    ],
    "entry_exit": {
      "entry": "Buy gaming hardware or publisher stocks (e.g., ATVI, EA, NVDA) on day of spike detection.",
      "exit": "Sell when activity falls below 80% of the 7-day exponential moving average or after 5 trading days, whichever comes first."
    },
    "signal_logic": {
      "trigger": "Calculate the daily percentage increase in total posts plus comments in r/gaming, r/pcgaming, and r/Games. Signal triggers when combined activity rises more than 50% compared to the 7-day exponential moving average, and the baseline 7-day average activity is at least 100 posts+comments."
    },
    "position_sizing": {
      "allocation_per_signal": "5% of portfolio, with no more than 2% per individual stock",
      "max_total_exposure": "20% of portfolio"
    },
    "data_sources": {
      "reddit": {
        "subreddits": [
          "gaming",
          "pcgaming",
          "Games"
        ]
      }
    },
    "adapter_contracts": {
      "reddit_activity": {
        "func": "fetch_reddit_activity",
        "allowed_kwargs": [
          "subreddits",
          "days_back",
          "cache_key"
        ],
        "returns": [
          "date",
          "posts",
          "comments"
        ]
      }
    },
    "edge_cases": {
      "missing_data": "Skip signal generation for days with incomplete or missing Reddit data.",
      "zero_moving_average": "Avoid division by zero by setting a minimum threshold of 10 posts+comments for the 7-day moving average.",
      "overlapping_signals": "If multiple spikes occur within 5 trading days, only the first signal will be acted upon.",
      "max_exposure_reached": "If the 5% allocation would exceed the 20% max total exposure, reduce the allocation proportionally across all stocks to stay within the limit.",
      "non_trading_days": "Exclude non-trading days (weekends, holidays) from the 5 trading day exit rule."
    }
  }
}