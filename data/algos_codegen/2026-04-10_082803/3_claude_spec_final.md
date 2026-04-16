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
    "TTWO"
  ],
  "data_sources": {
    "reddit": {
      "api_endpoints": [
        "https://api.pushshift.io/reddit/submission/search?subreddit=gaming&after=7d&size=1000",
        "https://api.pushshift.io/reddit/comment/search?subreddit=gaming&after=7d&size=1000",
        "https://api.pushshift.io/reddit/submission/search?subreddit=pcgaming&after=7d&size=1000",
        "https://api.pushshift.io/reddit/comment/search?subreddit=pcgaming&after=7d&size=1000",
        "https://api.pushshift.io/reddit/submission/search?subreddit=games&after=7d&size=1000",
        "https://api.pushshift.io/reddit/comment/search?subreddit=games&after=7d&size=1000"
      ],
      "data_fields": {
        "posts": ["id", "created_utc", "score"],
        "comments": ["id", "created_utc", "score"]
      },
      "normalization": {
        "method": "subreddit_size_adjusted",
        "baseline_period": "30d"
      }
    },
    "yahoo_finance": {
      "price_data": {
        "metric": "adjusted_close",
        "frequency": "daily"
      }
    }
  },
  "signal_logic": {
    "metric": "normalized_total_posts_plus_comments",
    "trigger_condition": {
      "type": "percentage_increase",
      "threshold": {
        "min_baseline": 1000,
        "min_pct_increase": 50,
        "max_pct_increase": 500,
        "time_window": 7
      }
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
        {
          "type": "price_below_moving_average",
          "metric": "adjusted_close",
          "window": 7,
          "tolerance": 0.05
        },
        {
          "type": "time_based",
          "duration": 5
        }
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
      "Pull daily counts of posts and comments from target subreddits using Pushshift.io API",
      "Compute rolling averages and percentage changes, normalize by subreddit size",
      "Filter out deleted/removed posts and comments"
    ],
    "integration_with_yahoo_finance": [
      "Integrate with adjusted closing price data from Yahoo Finance to manage entry/exit"
    ],
    "backtesting": [
      "Backtest on historical Reddit and Yahoo Finance data for the last 3 years"
    ],
    "production_deployment": [
      "Implement retry/backoff logic for API rate limits",
      "Monitor for data gaps or outages and have fallback procedures",
      "Periodically review signal performance and adjust parameters as needed"
    ]
  },
  "required_keys": [
    "reddit.api_endpoints",
    "reddit.data_fields",
    "reddit.normalization",
    "yahoo_finance.price_data",
    "signal_logic.trigger_condition",
    "entry_exit.exit.condition"
  ]
}
```