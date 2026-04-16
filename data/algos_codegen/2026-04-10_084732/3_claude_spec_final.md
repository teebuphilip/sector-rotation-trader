{
  "adapters": [
    "reddit_activity"
  ],
  "sliced_spec": {
    "id": "reddit-gaming-thread-spike",
    "name": "Reddit Gaming Thread Spike",
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
    "position_sizing": {
      "allocation_per_signal": "5% of portfolio",
      "max_total_exposure": "20% of portfolio",
      "max_individual_stock_exposure": "3% of portfolio"
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
    },
    "edge_cases": {
      "zero_moving_average": "If the 7-day moving average is zero or near zero, use a minimum activity threshold of 100 combined posts and comments to trigger the signal.",
      "weekends_holidays": "No positions will be opened or closed on weekends or market holidays.",
      "price_gaps": "If the stock price gaps significantly (more than 5%) on entry or exit, the position will be closed at the opening price on the next trading day.",
      "partial_fills": "Position sizing will be adjusted based on the actual fill price and quantity.",
      "overlapping_signals": "If a new spike is detected before the 5-day exit window ends for an existing position, the exit timer will be reset to 5 trading days from the new signal date."
    },
    "risk_management": {
      "max_drawdown": "10% per position",
      "stop_loss": "7% per position"
    }
  }
}