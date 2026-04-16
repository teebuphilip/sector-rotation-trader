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
      "reddit": {
        "subreddits": [
          "r/gaming",
          "r/pcgaming",
          "r/games"
        ],
        "data_fields": [
          "post_count",
          "comment_count"
        ],
        "data_quality_filters": [
          "exclude_deleted_posts",
          "exclude_low_quality_posts"
        ]
      }
    },
    "signal_logic": {
      "metric": "total_posts_and_comments",
      "trigger": {
        "condition": "percentage_increase",
        "threshold": 50,
        "window": {
          "type": "rolling",
          "length": 7,
          "exclude_current_day": true
        }
      }
    },
    "entry_exit": {
      "entry": {
        "condition": "signal_trigger"
      },
      "exit": {
        "condition": [
          {
            "type": "after_trading_days",
            "length": 5
          }
        ]
      }
    }
  }
}
```