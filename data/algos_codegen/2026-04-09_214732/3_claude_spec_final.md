```json
{
  "id": "reddit-gaming-thread-spike",
  "source": "reddit_api, yahoo_finance",
  "frequency": "daily",
  "thesis": "Sudden spikes in activity within specific gaming-related subreddits often precede increased interest and sales for gaming companies or hardware suppliers. By tracking the surge in new posts and comments in popular gaming subreddits, one can anticipate short-term momentum in gaming stocks. This signal leverages social sentiment shifts before they appear in traditional financial news.",
  "universe": [
    {
      "ticker": "ATVI",
      "category": "gaming_publisher_stocks"
    },
    {
      "ticker": "EA",
      "category": "gaming_publisher_stocks" 
    },
    {
      "ticker": "NVDA",
      "category": "gaming_hardware_stocks"
    },
    {
      "ticker": "TTWO",
      "category": "gaming_publisher_stocks"
    },
    {
      "ticker": "MSFT",
      "category": "gaming_publisher_stocks"
    }
  ],
  "data_sources": {
    "reddit_api": {
      "subreddits": [
        "r/gaming",
        "r/pcgaming",
        "r/games"
      ],
      "data_collection": {
        "new_posts": true,
        "new_comments": true,
        "deleted_posts_comments": false,
        "time_zone": "UTC"
      }
    },
    "yahoo_finance": {
      "price_data": {
        "fields": ["open", "high", "low", "close", "adjusted_close", "volume"],
        "adjusted": true
      }
    }
  },
  "signal_logic": {
    "metric": "total_new_posts_plus_comments",
    "trigger": {
      "condition": "daily_percentage_increase_gt_50_percent_of_7day_moving_average",
      "formula": "(daily_total - 7day_moving_average) / 7day_moving_average > 0.5"
    }
  },
  "entry_exit": {
    "entry": {
      "condition": "on_day_of_spike_detection",
      "instruments": [
        "gaming_hardware_stocks",
        "gaming_publisher_stocks"
      ]
    },
    "exit": {
      "condition": "activity_falls_below_7day_moving_average_for_3_consecutive_days_or_5_trading_days"
    }
  },
  "position_sizing": {
    "allocation_per_signal": 0.05,
    "max_total_exposure": 0.2,
    "weighting": "equal"
  },
  "risks": [
    "false_positives_from_viral_posts",
    "short_lived_spikes_with_no_price_follow_through",
    "api_rate_limits_or_data_outages",
    "sector_wide_selloffs_overriding_signal"
  ],
  "implementation_notes": {
    "reddit_api_usage": {
      "pull_daily_counts_of_new_posts_and_comments": true,
      "handle_api_rate_limits": {
        "pause_trading": true,
        "use_cached_data": true
      },
      "handle_zero_activity_days": {
        "skip_signal_generation": true
      }
    },
    "computations": [
      "compute_rolling_averages",
      "compute_percentage_changes"
    ],
    "integration": [
      "integrate_with_yahoo_finance_price_data",
      "manage_entry_and_exit"
    ],
    "backtesting": {
      "data_period": "2018-01-01 to 2022-12-31",
      "performance_metrics": [
        "annualized_return",
        "max_drawdown",
        "sharpe_ratio"
      ]
    }
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