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
          "description": "Total number of posts and comments, with deleted content excluded. Posts and comments are weighted equally.",
          "timezone": "UTC"
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
    "description": "Calculate the daily percentage increase in total posts plus comments in target subreddits. Signal triggers when combined activity rises more than 50% compared to the 7-day moving average, with a minimum activity threshold of 1000 posts and comments.",
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
      "trigger": [
        "activity_falls_below_90%_of_7day_average",
        "5_trading_days_passed"
      ]
    }
  },
  "position_sizing": {
    "allocation_per_signal": 0.05,
    "max_total_exposure": 0.2,
    "scaling_logic": {
      "description": "If max total exposure is reached, scale down allocation per signal proportionally to stay within limit.",
      "steps": [
        {
          "action": "calculate_total_current_exposure",
          "metric": "total_portfolio_value"
        },
        {
          "action": "scale_allocation_per_signal",
          "condition": "total_current_exposure > max_total_exposure",
          "scale_factor": "max_total_exposure / total_current_exposure"
        }
      ]
    }
  },
  "risk_management": {
    "stop_loss": {
      "trigger": "price_drops_more_than_10%_from_entry"
    },
    "take_profit": {
      "trigger": "price_increases_more_than_20%_from_entry"
    }
  },
  "risks": [
    "False positives from viral posts unrelated to business fundamentals",
    "Short-lived spikes with no price follow-through",
    "API rate limits or data outages",
    "Sector-wide selloffs overriding signal"
  ],
  "implementation_notes": {
    "description": "Use Reddit API to pull daily counts of posts and comments from target subred