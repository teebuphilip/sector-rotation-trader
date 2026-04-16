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
      "filters": {
        "post_types": ["submission", "comment"],
        "exclude_deleted_removed": true,
        "spam_filtering": true
      },
      "normalization": {
        "timezone": "UTC",
        "weekends_holidays": "exclude"
      }
    },
    "yahoo_finance": {
      "tickers": [
        "ATVI",
        "EA",
        "NVDA",
        "TTWO",
        "MSFT"
      ],
      "fields": ["adjusted_close", "volume"],
      "corporate_actions": "adjusted"
    }
  },
  "signal_logic": {
    "metric": "total_posts_and_comments",
    "trigger": {
      "condition": "percentage_increase",
      "threshold": {
        "value": 50,
        "window": 7,
        "apply_to": "combined_posts_comments"
      }
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
          "type": "below_moving_average",
          "window": 10,
          "average_type": "simple"
        },
        {
          "type": "after_trading_days",
          "value": 5
        }
      ]
    }
  },
  "position_sizing": {
    "allocation_per_signal": 0.05,
    "max_total_exposure": 0.2,
    "liquidity_filter": {
      "min_volume": 100000
    }
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
      "Filter out spam/bot content",
      "Handle missing data days"
    ],
    "price_data_integration": [
      "Integrate with adjusted close and volume data from Yahoo Finance",
      "Adjust for corporate actions (splits, dividends)"
    ],
    "backtesting": [
      "Backtest on historical Reddit data from 2018-2022",
      "Test sensitivity to different moving average parameters and liquidity filters"
    ]
  },
  "required_keys": []
}
```