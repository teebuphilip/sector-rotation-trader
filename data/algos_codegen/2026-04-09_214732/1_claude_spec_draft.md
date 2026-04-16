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
    "reddit_api": [
      "r/gaming",
      "r/pcgaming",
      "r/games"
    ],
    "yahoo_finance": {
      "price_data": true
    }
  },
  "signal_logic": {
    "metric": "total_posts_plus_comments",
    "trigger": {
      "condition": "daily_percentage_increase_gt_50_of_7day_moving_average"
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
      "condition": "activity_falls_below_7day_moving_average_or_5_trading_days"
    }
  },
  "position_sizing": {
    "allocation_per_signal": 0.05,
    "max_total_exposure": 0.2
  },
  "risks": [
    "false_positives_from_viral_posts",
    "short_lived_spikes_with_no_price_follow_through",
    "api_rate_limits_or_data_outages",
    "sector_wide_selloffs_overriding_signal"
  ],
  "implementation_notes": {
    "reddit_api_usage": "pull_daily_counts_of_posts_and_comments",
    "computations": [
      "compute_rolling_averages",
      "compute_percentage_changes"
    ],
    "integration": [
      "integrate_with_yahoo_finance_price_data",
      "manage_entry_and_exit"
    ],
    "backtesting": "backtest_on_historical_reddit_data"
  },
  "required_keys": []
}
```