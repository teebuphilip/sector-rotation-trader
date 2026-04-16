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
        "filters": {
          "post_types": [
            "submission",
            "comment"
          ],
          "exclude_deleted_removed": true,
          "spam_filtering": true
        },
        "normalization": {
          "timezone": "UTC",
          "weekends_holidays": "exclude"
        }
      }
    },
    "signal_logic": {
      "metric": "total_posts_and_comments",
      "trigger": {
        "condition": "percentage_increase",
        "threshold": {
          "value": 50,
          "window": 7,
          "apply_to": "combined_posts_comments"
        }
      }
    },
    "entry_exit": {
      "entry": {
        "condition": "signal_trigger",
        "instruments": [
          "ATVI",
          "EA",
          "NVDA"
        ]
      },
      "exit": {
        "condition": [
          {
            "type": "below_moving_average",
            "window": 10,
            "average_type": "simple"
          },
          {
            "type": "after_trading_days",
            "value": 5
          }
        ]
      }
    }
  }
}
```