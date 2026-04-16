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
      "timezone": "UTC",
      "daily_cutoff": "00:00"
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
    "metric": {
      "name": "total_posts_plus_comments",
      "description": "Sum of all new posts and comments (including replies) across target subreddits, excluding deleted content"
    },
    "trigger": {
      "condition": "percentage_increase",
      "threshold": 50,
      "baseline": "previous_7day_average",
      "minimum_volume": 100
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
          "name": "below_7day_average",
          "threshold": 0.95
        },
        {
          "name": "after_5_trading_days"
        }
      ],
      "whichever": "comes_first"
    }
  },
  "position_sizing": {
    "allocation_per_signal": 0.05,
    "max_total_exposure": 0.20
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
      "Compute rolling averages and percentage changes",
      "Filter out deleted posts and comments"
    ],
    "integration": [
      "Integrate with price data from Yahoo Finance to manage entry/exit",
      "Handle missing price data and non-trading days for exit timing"
    ],
    "backtest": [
      "Backtest on historical Reddit data for the past 3 years",
      "Evaluate performance metrics such as annualized return, Sharpe ratio, and maximum drawdown",
      "Conduct out-of-sample validation on the most recent 1 year of data"
    ],
    "error_handling": [
      "Implement retry logic and fallback data sources to mitigate API rate limits and outages",
      "Monitor data quality and trigger alerts for anomalies or missing data"
    ]
  },
  "required_keys": [
    "reddit.subreddits",
    "reddit.timezone",
    "reddit.daily_cutoff",
    "yahoo_finance.tickers",
    "signal_logic.metric.name",
    "signal_logic.metric.description",
    "signal_logic.trigger.condition",
    "signal_logic.trigger.threshold",
    "signal_logic.trigger.baseline",
    "signal_logic.trigger.minimum_volume",
    "entry_exit.entry.condition",
    "entry_exit.entry.instruments",
    "entry_exit.exit.condition",
    "entry_exit.exit.whichever",
    "position_sizing.allocation_per_signal",
    "position_sizing.max_total_exposure"
  ]
}
```