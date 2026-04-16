```json
{
  "pattern": "D",
  "sliced_spec": {
    "id": "reddit-gaming-thread-spike",
    "source": "reddit_and_yahoo_finance",
    "frequency": "daily",
    "universe": [
      "ATVI",
      "EA",
      "NVDA",
      "TTWO",
      "MSFT"
    ],
    "data_sources": {
      "reddit": {
        "subreddits": [
          "r/gaming",
          "r/pcgaming",
          "r/games"
        ],
        "data_cleaning": {
          "filter_bots": true,
          "filter_spam": true,
          "only_new_posts_comments": true
        }
      },
      "yahoo_finance": {
        "fields": [
          "adjusted_close"
        ]
      }
    },
    "signal_logic": {
      "metric": {
        "posts": "new_posts_count",
        "comments": "new_comments_count"
      },
      "trigger": {
        "condition": "percentage_increase",
        "threshold": {
          "posts": 50,
          "comments": 50
        },
        "window": 7,
        "baseline": "7_day_rolling_average"
      }
    },
    "entry_exit": {
      "entry": {
        "condition": "on_spike_detection",
        "instruments": [
          "gaming_hardware_stocks",
          "gaming_publisher_stocks"
        ]
      },
      "exit": {
        "condition": [
          {
            "metric": "adjusted_close",
            "threshold": "below_7day_moving_average"
          },
          {
            "time_condition": "after_5_trading_days"
          }
        ],
        "order": "whichever_comes_first"
      }
    },
    "position_sizing": {
      "allocation_per_signal": 0.05,
      "max_total_exposure": 0.2
    }
  }
}
```