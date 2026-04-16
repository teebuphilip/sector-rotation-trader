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
        "api_endpoints": {
          "posts": [
            "/r/gaming/new",
            "/r/pcgaming/new",
            "/r/games/new"
          ],
          "comments": [
            "/r/gaming/comments",
            "/r/pcgaming/comments",
            "/r/games/comments"
          ]
        }
      }
    },
    "signal_logic": {
      "parameters": {
        "activity_threshold": 0.5,
        "moving_average_window": 7,
        "minimum_activity_threshold": 1000
      }
    },
    "entry_exit": {
      "entry": {
        "condition": "on day of spike detection"
      },
      "exit": {
        "condition": "when activity falls below the 7-day moving average by more than 10% for 2 consecutive trading days or after 5 trading days, whichever comes first"
      }
    }
  }
}
```