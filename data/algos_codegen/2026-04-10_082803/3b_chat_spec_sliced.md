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
      "TTWO"
    ],
    "data_sources": {
      "reddit": {
        "api_endpoints": [
          "https://api.pushshift.io/reddit/submission/search?subreddit=gaming&after=7d&size=1000",
          "https://api.pushshift.io/reddit/comment/search?subreddit=gaming&after=7d&size=1000",
          "https://api.pushshift.io/reddit/submission/search?subreddit=pcgaming&after=7d&size=1000",
          "https://api.pushshift.io/reddit/comment/search?subreddit=pcgaming&after=7d&size=1000",
          "https://api.pushshift.io/reddit/submission/search?subreddit=games&after=7d&size=1000",
          "https://api.pushshift.io/reddit/comment/search?subreddit=games&after=7d&size=1000"
        ],
        "data_fields": {
          "posts": [
            "id",
            "created_utc",
            "score"
          ],
          "comments": [
            "id",
            "created_utc",
            "score"
          ]
        },
        "normalization": {
          "method": "subreddit_size_adjusted",
          "baseline_period": "30d"
        }
      },
      "yahoo_finance": {
        "price_data": {
          "metric": "adjusted_close",
          "frequency": "daily"
        }
      }
    },
    "signal_logic": {
      "trigger_condition": {
        "type": "percentage_increase",
        "threshold": {
          "min_baseline": 1000,
          "min_pct_increase": 50,
          "max_pct_increase": 500,
          "time_window": 7
        }
      }
    },
    "entry_exit": {
      "exit": {
        "condition": [
          {
            "type": "price_below_moving_average",
            "metric": "adjusted_close",
            "window": 7,
            "tolerance": 0.05
          },
          {
            "type": "time_based",
            "duration": 5
          }
        ],
        "whichever_comes_first": true
      }
    }
  }
}
```