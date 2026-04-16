```json
{
  "pattern": "D",
  "sliced_spec": {
    "id": "reddit-gaming-thread-spike",
    "source": "reddit_api, yahoo_finance",
    "frequency": "daily",
    "universe": [
      {
        "ticker": "ATVI",
        "category": "gaming_publisher_stocks"
      },
      {
        "ticker": "EA",
        "category": "gaming_publisher_stocks"
      },
      {
        "ticker": "NVDA",
        "category": "gaming_hardware_stocks"
      },
      {
        "ticker": "TTWO",
        "category": "gaming_publisher_stocks"
      },
      {
        "ticker": "MSFT",
        "category": "gaming_publisher_stocks"
      }
    ],
    "data_sources": {
      "reddit_api": {
        "subreddits": [
          "r/gaming",
          "r/pcgaming",
          "r/games"
        ],
        "data_collection": {
          "new_posts": true,
          "new_comments": true,
          "time_zone": "UTC"
        }
      }
    },
    "signal_logic": {
      "metric": "total_new_posts_plus_comments",
      "trigger": {
        "condition": "daily_percentage_increase_gt_50_percent_of_7day_moving_average",
        "formula": "(daily_total - 7day_moving_average) / 7day_moving_average > 0.5"
      }
    },
    "entry_exit": {
      "entry": {
        "condition": "on_day_of_spike_detection",
        "instruments": [
          "gaming_hardware_stocks",
          "gaming_publisher_stocks"
        ]
      },
      "exit": {
        "condition": "activity_falls_below_7day_moving_average_for_3_consecutive_days_or_5_trading_days"
      }
    }
  }
}
```