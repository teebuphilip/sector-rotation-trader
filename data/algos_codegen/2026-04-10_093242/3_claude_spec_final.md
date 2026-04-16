{
  "version": "1.0",
  "spec": {
    "id": "reddit-gaming-thread-spike",
    "name": "Reddit Gaming Thread Spike",
    "frequency": "daily",
    "universe": [
      "ATVI",
      "EA",
      "NVDA",
      "TTWO",
      "MSFT"
    ],
    "entry_exit": {
      "entry": "Buy gaming hardware or publisher stocks (e.g., ATVI, EA, NVDA) on day of spike detection.",
      "exit": "Sell when activity falls below the 7-day moving average or after 5 trading days, whichever comes first."
    },
    "signal_logic": {
      "trigger": {
        "description": "Calculate the daily percentage increase in total posts and comments separately in the r/gaming, r/pcgaming, and r/Games subreddits. Signal triggers when either posts or comments rise more than 50% compared to the 7-day moving average, and the total daily activity exceeds a minimum threshold of 1000 posts and comments.",
        "condition": "(((today_posts - moving_average_posts_7d) / moving_average_posts_7d) > 0.5 or ((today_comments - moving_average_comments_7d) / moving_average_comments_7d) > 0.5) and (today_posts + today_comments) > 1000"
      }
    },
    "position_sizing": {
      "per_signal_allocation": "5%",
      "max_total_exposure": "20%"
    },
    "data_sources": {
      "reddit": {
        "subreddits": [
          "r/gaming",
          "r/pcgaming",
          "r/Games"
        ],
        "timezone": "UTC",
        "filter_deleted": true,
        "filter_bots": true
      }
    },
    "adapter_contracts": {
      "reddit_activity": {
        "func": "fetch_reddit_activity",
        "allowed_kwargs": [
          "subreddits",
          "days_back",
          "cache_key"
        ],
        "returns": [
          "date",
          "posts",
          "comments"
        ],
        "error_handling": {
          "missing_data": "skip_day",
          "api_failure": "skip_day"
        }
      }
    }
  }
}