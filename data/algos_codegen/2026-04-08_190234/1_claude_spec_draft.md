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
      ]
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
    "metric": "total_posts_plus_comments",
    "trigger": {
      "condition": "daily_percentage_increase > 50%",
      "window": "7-day_moving_average"
    }
  },
  "entry_exit": {
    "entry": {
      "condition": "signal_trigger",
      "instruments": [
        "gaming_hardware_stocks",
        "gaming_publisher_stocks"
      ]
    },
    "exit": {
      "condition": [
        "activity_falls_below_7day_average",
        "5_trading_days_elapsed"
      ],
      "whichever": "comes_first"
    }
  },
  "position_sizing": {
    "allocation_per_signal": "5%",
    "max_total_exposure": "20%"
  },
  "risks": [
    "false_positives_from_viral_posts",
    "short-lived_spikes_with_no_price_follow-through",
    "api_rate_limits_or_data_outages",
    "sector-wide_selloffs_overriding_signal"
  ],
  "implementation_notes": {
    "reddit_data_collection": "use_reddit_api_to_pull_daily_post_and_comment_counts",
    "data_processing": [
      "compute_rolling_averages",
      "calculate_percentage_changes"
    ],
    "integration": "integrate_with_yahoo_finance_for_price_data_to_manage_entry_and_exit",
    "backtest": "backtest_on_historical_reddit_data_if_available"
  },
  "required_keys": []
}
```