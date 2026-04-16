```json
{
  "pattern": "D",
  "sliced_spec": {
    "id": "reddit-gaming-thread-spike",
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
      "exit": "Sell when activity falls below 95% of the 7-day exponential moving average or after 5 trading days, whichever comes first."
    },
    "signal_logic": {
      "trigger": {
        "description": "Signal triggers when combined daily posts plus comments in r/gaming, r/pcgaming, and r/nvidia rise more than 50% compared to the 7-day exponential moving average, and the 7-day average is greater than 100 total activities.",
        "condition": "((today_total_activity - exp_moving_average_7d) / exp_moving_average_7d) > 0.5 && exp_moving_average_7d > 100"
      }
    },
    "data_sources": {
      "reddit": {
        "subreddits": [
          "r/gaming",
          "r/pcgaming",
          "r/nvidia"
        ],
        "activity_type": [
          "posts",
          "comments"
        ],
        "aggregation": "sum",
        "timezone": "UTC",
        "missing_data_handling": "skip_day"
      }
    }
  }
}
```