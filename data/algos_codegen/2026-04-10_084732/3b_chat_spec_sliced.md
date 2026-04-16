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
      "exit": "Sell when activity falls below 80% of the 7-day moving average or after 5 trading days, whichever comes first."
    },
    "signal_logic": {
      "trigger": "Calculate the daily percentage increase in total posts plus comments in the r/gaming, r/pcgaming, and r/nvidia subreddits. Signal triggers when combined activity rises more than 50% compared to the 7-day moving average."
    },
    "data_sources": {
      "reddit": {
        "subreddits": [
          "r/gaming",
          "r/pcgaming",
          "r/nvidia"
        ],
        "data_fields": [
          "posts",
          "comments"
        ],
        "update_frequency": "daily"
      }
    }
  }
}
```