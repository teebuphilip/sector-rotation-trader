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
      ],
      "timestamp_format": "iso8601",
      "timezone": "UTC"
    },
    "yahoo_finance": {
      "fields": [
        "price",
        "volume",
        "volatility"
      ]
    }
  },
  "signal_logic": {
    "description": "Calculate the daily percentage increase in total posts plus comments in target subreddits. Signal triggers when combined activity rises more than 50% (1.5x) compared to the 7-day moving average, with a minimum baseline of 100 total posts+comments.",
    "trigger_condition": {
      "metric": "post_and_comment_volume",
      "threshold": 1.5,
      "timeframe": 7,
      "min_baseline": 100
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
        "activity_below_90_percent_of_ma7",
        "hold_for_5_days"
      ],
      "timeframe": 5
    }
  },
  "position_sizing": {
    "allocation_per_signal": 0.05,
    "max_total_exposure": 0.2,
    "stop_loss": 0.1,
    "max_drawdown": 0.2
  },
  "risks": [
    "False positives from viral posts unrelated to business fundamentals",
    "Short-lived spikes with no price follow-through",
    "API rate limits or data outages",
    "Sector-wide selloffs overriding signal"
  ],
  "implementation_notes": {
    "description": "Use Reddit API to pull daily counts of posts and comments from target subreddits. Compute rolling averages and percentage changes. Integrate with price, volume, and volatility data from Yahoo Finance to manage entry/exit. Backtest on historical Reddit data from Pushshift.io. Handle missing data, API rate limits, and weekends/holidays appropriately.",
    "required_keys": []
  }
}
```