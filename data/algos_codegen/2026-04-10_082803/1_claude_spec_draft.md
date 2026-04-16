```json
{
  "id": "reddit-gaming-thread-spike",
  "source": "openai / gpt-4.1-mini",
  "frequency": "daily",
  "thesis": "Sudden spikes in activity within specific gaming-related subreddits often precede increased interest and sales for gaming companies or hardware suppliers. By tracking the surge in new posts and comments in popular gaming subreddits, one can anticipate short-term momentum in gaming stocks. This signal leverages social sentiment shifts before they appear in traditional financial news.",
  "universe": [
    "ATVI",
    "EA",
    "NVDA",
    "TTWO",
    "MSFT"
  ],
  "data_sources": {
    "reddit": {
      "api_endpoints": [
        "r/gaming",
        "r/pcgaming",
        "r/games"
      ]
    },
    "yahoo_finance": {
      "price_data": true
    }
  },
  "signal_logic": {
    "metric": "total_posts_plus_comments",
    "trigger_condition": {
      "type": "percentage_increase",
      "threshold": 50,
      "time_window": 7
    }
  },
  "entry_exit": {
    "entry": {
      "condition": "on_signal_trigger",
      "instruments": [
        "gaming_hardware_stocks",
        "gaming_publisher_stocks"
      ]
    },
    "exit": {
      "condition": [
        "below_7day_moving_average",
        "after_5_trading_days"
      ],
      "whichever_comes_first": true
    }
  },
  "position_sizing": {
    "allocation_per_signal": 0.05,
    "max_total_exposure": 0.2
  },
  "risks": [
    "False positives from viral posts unrelated to business fundamentals",
    "Short-lived spikes with no price follow-through",
    "API rate limits or data outages",
    "Sector-wide selloffs overriding signal"
  ],
  "implementation_notes": {
    "reddit_data_processing": [
      "Pull daily counts of posts and comments from target subreddits",
      "Compute rolling averages and percentage changes"
    ],
    "integration_with_yahoo_finance": [
      "Integrate with price data from Yahoo Finance to manage entry/exit"
    ],
    "backtesting": [
      "Backtest on historical Reddit data if available"
    ]
  },
  "required_keys": []
}
```