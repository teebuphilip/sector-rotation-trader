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
      ],
      "data_definition": {
        "posts_and_comments": {
          "description": "Sum of new posts and comments, excluding deleted/removed content",
          "time_zone": "UTC",
          "collection_time": "00:00 UTC"
        }
      }
    },
    "yahoo_finance": {
      "fields": [
        "adjusted_close"
      ]
    }
  },
  "signal_logic": {
    "description": "Calculate the daily percentage increase in total posts plus comments in target subreddits. Signal triggers when combined activity rises more than 50% compared to the 7-day moving average, and the minimum daily activity exceeds 1000 posts+comments.",
    "steps": [
      {
        "action": "calculate_daily_post_and_comment_count",
        "target_subreddits": [
          "r/gaming",
          "r/pcgaming",
          "r/games"
        ]
      },
      {
        "action": "calculate_7_day_moving_average",
        "metric": "total_posts_and_comments"
      },
      {
        "action": "calculate_daily_percentage_change",
        "metric": "total_posts_and_comments"
      },
      {
        "action": "trigger_signal",
        "condition": "daily_percentage_change > 50 AND total_posts_and_comments > 1000"
      }
    ]
  },
  "entry_exit": {
    "entry": {
      "action": "buy",
      "target_assets": [
        "ATVI",
        "EA",
        "NVDA"
      ],
      "trigger": "signal_trigger"
    },
    "exit": {
      "action": "sell",
      "condition": [
        "activity_falls_below_7_day_average_by_10_percent",
        "5_trading_days_passed"
      ]
    },
    "cooldown": {
      "days": 3,
      "condition": "activity_remains_above_7_day_average_by_20_percent"
    }
  },
  "position_sizing": {
    "allocation_per_signal": 0.05,
    "max_total_exposure": 0.2
  },
  "risks": [
    "False positives from viral posts unrelated to business fundamentals",
    "Short-lived spikes with no price follow-through",
    "API rate limits or data outages leading to incomplete data",
    "Sector-wide selloffs overriding signal",
    "Overfitting to social media noise",
    "Delays in Reddit data availability or moderation affecting counts"
  ],
  "implementation_notes": {
    "description": "Use Reddit API to pull daily counts of posts and comments from target subreddits. Compute rolling averages and percentage changes. Integrate with adjusted close price data from Yahoo Finance to manage entry/exit. Backtest on historical Reddit data, simulating missing data and API outages.",
    "required_keys": []
  }
}
```