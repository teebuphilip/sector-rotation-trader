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
      "tickers": [
        "ATVI",
        "EA",
        "NVDA",
        "TTWO",
        "MSFT"
      ]
    }
  },
  "signal_logic": {
    "description": "Calculate the daily percentage increase in total posts plus comments in target subreddits. Signal triggers when combined activity rises more than 50% compared to the 7-day moving average.",
    "parameters": {
      "activity_threshold": 0.5,
      "moving_average_window": 7
    }
  },
  "entry_exit": {
    "entry": {
      "condition": "on day of spike detection",
      "assets": [
        "gaming hardware stocks",
        "publisher stocks"
      ]
    },
    "exit": {
      "condition": "when activity falls below the 7-day moving average or after 5 trading days, whichever comes first"
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
    "description": "Use Reddit API to pull daily counts of posts and comments from target subreddits. Compute rolling averages and percentage changes. Integrate with price data from Yahoo Finance to manage entry/exit. Backtest on historical Reddit data if available.",
    "required_keys": []
  }
}
```