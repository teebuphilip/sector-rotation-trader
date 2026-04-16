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
    "data_sources": {
      "reddit_api": {
        "subreddits": [
          "r/gaming",
          "r/pcgaming",
          "r/games"
        ],
        "post_and_comment_count": {
          "method": "sum"
        },
        "timestamp_normalization": "UTC"
      }
    },
    "signal_logic": {
      "trigger": {
        "condition": "combined_posts_and_comments_increase",
        "threshold": {
          "type": "percentage",
          "value": 50,
          "window": 7
        },
        "minimum_activity": 1000
      }
    },
    "entry_exit": {
      "entry": {
        "condition": "signal_trigger",
        "instruments": [
          "gaming_hardware_stocks",
          "gaming_publisher_stocks"
        ]
      },
      "exit": {
        "condition": [
          "activity_falls_below_moving_average",
          "holding_period_exceeds_5_days"
        ],
        "activity_threshold": {
          "type": "percentage",
          "value": -10,
          "window": 7
        }
      }
    }
  }
}
```