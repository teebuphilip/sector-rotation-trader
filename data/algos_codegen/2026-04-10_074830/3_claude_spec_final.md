```json
{
  "id": "reddit-gaming-thread-spike",
  "source": "reddit_and_yahoo_finance",
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
      "data_cleaning": {
        "filter_bots": true,
        "filter_spam": true,
        "only_new_posts_comments": true
      }
    },
    "yahoo_finance": {
      "fields": [
        "adjusted_close"
      ]
    }
  },
  "signal_logic": {
    "metric": {
      "posts": "new_posts_count",
      "comments": "new_comments_count"
    },
    "trigger": {
      "condition": "percentage_increase",
      "threshold": {
        "posts": 50,
        "comments": 50
      },
      "window": 7,
      "baseline": "7_day_rolling_average"
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
        {
          "metric": "adjusted_close",
          "threshold": "below_7day_moving_average"
        },
        {
          "time_condition": "after_5_trading_days"
        }
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
      "Use Reddit API to pull daily counts of new posts and new comments from target subreddits",
      "Compute rolling averages and percentage changes",
      "Integrate with adjusted close price data from Yahoo Finance to manage entry/exit",
      "Backtest on historical Reddit and Yahoo Finance data"
    ]
  },
  "required_keys": [
    "id",
    "source",
    "frequency",
    "thesis",
    "universe",
    "data_sources",
    "signal_logic",
    "entry_exit",
    "position_sizing",
    "risks",
    "implementation_notes"
  ]
}
```