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
      "subreddits": [
        "r/gaming",
        "r/pcgaming",
        "r/games"
      ]
    },
    "yahoo_finance": {
      "fields": [
        "price"
      ]
    }
  },
  "signal_logic": {
    "metric": "total_posts_plus_comments",
    "trigger": {
      "condition": "percentage_increase",
      "threshold": 50,
      "window": 7
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
        "below_7day_moving_average",
        "after_5_trading_days"
      ],
      "order": "whichever_comes_first"
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
    "steps": [
      "Use Reddit API to pull daily counts of posts and comments from target subreddits",
      "Compute rolling averages and percentage changes",
      "Integrate with price data from Yahoo Finance to manage entry/exit",
      "Backtest on historical Reddit data if available"
    ]
  },
  "required_keys": []
}
```