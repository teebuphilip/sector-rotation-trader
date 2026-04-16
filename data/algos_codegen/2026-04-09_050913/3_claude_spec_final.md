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
      "data_collection": {
        "exclude_deleted_posts_comments": true,
        "handle_crossposts_reposts": "deduplicate",
        "timezone_normalization": "UTC"
      }
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
      "weighting": {
        "posts": 1,
        "comments": 1
      }
    },
    "trigger": {
      "condition": {
        "daily_percentage_increase": {
          "operator": ">=",
          "threshold": 50
        },
        "minimum_volume": 100
      },
      "reference": "7-day_moving_average"
    }
  },
  "entry_exit": {
    "entry": {
      "condition": "signal_trigger",
      "instruments": [
        "ATVI",
        "EA",
        "NVDA",
        "TTWO",
        "MSFT"
      ]
    },
    "exit": {
      "condition": [
        {
          "activity_falls_below_7day_average": {
            "operator": "<",
            "threshold": 95
          }
        },
        {
          "trading_days_passed": 5
        }
      ],
      "priority": "whichever_comes_first"
    }
  },
  "position_sizing": {
    "allocation_per_signal": 0.05,
    "max_total_exposure": 0.2,
    "multiple_signal_handling": "prorate_allocations"
  },
  "risks": [
    "false_positives_from_viral_posts",
    "short-lived_spikes_with_no_price_follow-through",
    "api_rate_limits_or_data_outages",
    "sector-wide_selloffs_overriding_signal"
  ],
  "implementation_notes": {
    "reddit_data_collection": {
      "use_reddit_api_to_pull_daily_post_and_comment_counts": true,
      "comments_included": "created_on_day"
    },
    "data_processing": [
      "compute_rolling_averages",
      "calculate_percentage_changes"
    ],
    "integration": {
      "yahoo_finance_for_price_data": true
    },
    "backtest": {
      "minimum_period": "5_years",
      "performance_metrics": [
        "sharpe_ratio",
        "max_drawdown"
      ]
    },
    "noise_filtering": {
      "cap_max_daily_increase": 100,
      "require_sustained_increase": 3
    }
  },
  "required_keys": []
}
```