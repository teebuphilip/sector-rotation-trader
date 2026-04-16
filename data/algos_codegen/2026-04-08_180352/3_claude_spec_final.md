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
      "min_activity_threshold": 100
    },
    "yahoo_finance": {
      "tickers": [
        "ATVI",
        "EA",
        "NVDA",
        "TTWO",
        "MSFT"
      ],
      "fields": ["close", "volume"]
    }
  },
  "signal_logic": {
    "metric": "total_posts_and_comments",
    "metric_details": {
      "weighting": {
        "posts": 1,
        "comments": 0.5
      },
      "filtering": {
        "spam": true,
        "deleted": true
      }
    },
    "trigger": {
      "condition": "percentage_increase",
      "baseline_period": 14,
      "threshold": 50
    }
  },
  "entry_exit": {
    "entry": {
      "condition": "signal_trigger"
    },
    "exit": {
      "condition": [
        {
          "type": "below_7day_average",
          "threshold": 0.95
        },
        {
          "type": "after_5_trading_days"
        }
      ],
      "priority": "whichever_comes_first"
    }
  },
  "position_sizing": {
    "allocation_per_signal": 5,
    "max_total_exposure": 20,
    "max_per_ticker": 10
  },
  "risks": [
    "False positives from viral posts unrelated to business fundamentals",
    "Short-lived spikes with no price follow-through",
    "API rate limits or data outages",
    "Sector-wide selloffs overriding signal"
  ],
  "implementation_notes": {
    "reddit_data_collection": {
      "use_reddit_api": true,
      "timezone_normalization": true,
      "fallback_logic": true
    },
    "data_processing": {
      "compute_rolling_averages": true,
      "calculate_percentage_changes": true
    },
    "integration": {
      "combine_reddit_yahoo_data": true,
      "manage_entry_exit_logic": true
    },
    "backtesting": {
      "use_historical_reddit_data": true
    }
  },
  "required_keys": [
    "reddit.subreddits",
    "reddit.min_activity_threshold",
    "yahoo_finance.tickers",
    "yahoo_finance.fields",
    "signal_logic.metric_details.weighting",
    "signal_logic.metric_details.filtering",
    "signal_logic.trigger.baseline_period",
    "signal_logic.trigger.threshold",
    "entry_exit.exit.condition[0].threshold",
    "position_sizing.allocation_per_signal",
    "position_sizing.max_total_exposure",
    "position_sizing.max_per_ticker"
  ]
}
```