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
      "data_fields": [
        "post_count",
        "comment_count",
        "sentiment_score"
      ],
      "data_quality_filters": [
        "exclude_deleted_posts",
        "exclude_low_quality_posts"
      ]
    },
    "yahoo_finance": {
      "tickers": [
        "ATVI",
        "EA",
        "NVDA",
        "TTWO",
        "MSFT"
      ],
      "data_fields": [
        "adjusted_close",
        "volume"
      ],
      "frequency": "daily"
    }
  },
  "signal_logic": {
    "metric": "total_posts_and_comments",
    "trigger": {
      "condition": "percentage_increase",
      "threshold": 50,
      "window": {
        "type": "rolling",
        "length": 7,
        "exclude_current_day": true
      }
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
          "metric": "adjusted_close"
        },
        {
          "type": "after_trading_days",
          "length": 5
        }
      ],
      "priority": "whichever_comes_first"
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
      "Use Reddit API to pull daily post and comment counts from target subreddits, along with sentiment scores",
      "Filter out deleted and low-quality posts",
      "Compute rolling averages and percentage changes for post/comment metrics",
      "Integrate with adjusted close price and volume data from Yahoo Finance to manage entry/exit",
      "Implement fallback handling for missing or delayed data",
      "Backtest on historical Reddit and price data"
    ]
  },
  "required_keys": []
}
```