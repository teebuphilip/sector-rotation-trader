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
      "entry": {
        "description": "Buy gaming hardware or publisher stocks (e.g., ATVI, EA, NVDA) on day of spike detection, with a maximum position size of 2% per stock."
      },
      "exit": {
        "description": "Sell when activity falls below 80% of the 7-day moving average or after 5 trading days, whichever comes first."
      }
    },
    "signal_logic": {
      "trigger": {
        "description": "Signal triggers when the combined daily posts plus comments in the following subreddits: r/gaming, r/pcgaming, r/nvidia, r/callofduty, r/battlefield rise more than 50% compared to the 7-day moving average, and the 7-day moving average is greater than 100 posts+comments.",
        "metric": "daily percentage increase in total posts plus comments",
        "threshold": 0.5,
        "comparison_period_days": 7,
        "minimum_baseline_activity": 100
      }
    },
    "position_sizing": {
      "allocation_per_signal": 0.05,
      "max_total_exposure": 0.2
    },
    "data_sources": {
      "reddit": {
        "subreddits": [
          "gaming",
          "pcgaming",
          "nvidia",
          "callofduty",
          "battlefield"
        ],
        "timezone": "UTC"
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
    }
  }
}
```