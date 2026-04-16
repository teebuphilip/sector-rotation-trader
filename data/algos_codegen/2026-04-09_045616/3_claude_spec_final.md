{
  "name": "reddit-gaming-thread-spike",
  "source": "openai / gpt-4.1-mini",
  "frequency": "daily",
  "thesis": "Sudden spikes in activity within specific gaming-related subreddits often precede increased interest and sales for gaming companies or hardware suppliers. By tracking the surge in new posts and comments in popular gaming subreddits, one can anticipate short-term momentum in gaming stocks. This signal leverages social sentiment shifts before they appear in traditional financial news.",
  "universe": [
    "ATVI",
    "EA",
    "NVDA",
    "TTWO"
  ],
  "dataSources": {
    "reddit": {
      "api": {
        "endpoints": [
          "r/gaming/new",
          "r/pcgaming/new",
          "r/games/new"
        ],
        "fields": [
          "num_comments",
          "num_crossposts",
          "num_reports",
          "num_awards",
          "score"
        ]
      }
    },
    "priceData": {
      "source": "Yahoo Finance",
      "fields": [
        "close",
        "adjusted_close",
        "volume"
      ],
      "timing": "daily_close"
    }
  },
  "signalLogic": {
    "description": "Calculate the daily percentage increase in total new posts and unique comments in target subreddits. Signal triggers when combined activity rises more than 50% compared to the 7-day moving average, and the absolute daily volume exceeds 1,000 posts and comments.",
    "thresholds": {
      "activityIncrease": 0.5,
      "movingAverage": 7,
      "minAbsoluteVolume": 1000
    }
  },
  "entryExit": {
    "entry": {
      "condition": "on day of spike detection",
      "assets": [
        "ATVI",
        "EA",
        "NVDA",
        "TTWO"
      ]
    },
    "exit": {
      "condition": "when percentage change in total posts and comments falls below the 7-day moving average or after 10 trading days, whichever comes first"
    }
  },
  "positionSizing": {
    "allocation": 0.05,
    "maxExposure": 0.2
  },
  "risks": [
    "False positives from viral posts unrelated to business fundamentals",
    "Short-lived spikes with no price follow-through",
    "API rate limits or data outages",
    "Sector-wide selloffs overriding signal",
    "Bot-generated posts and comments skewing activity data"
  ],
  "implementation": {
    "description": "Use Reddit API to pull daily counts of new posts and unique comments from target subreddits. Compute rolling averages and percentage changes. Integrate with price data from Yahoo Finance to manage entry/exit. Backtest on historical Reddit and price data, evaluating metrics such as hit rate, average return, and maximum drawdown. Implement error handling for missing data, weekends, and API failures.",
    "backtestMetrics": [
      "hit_rate",
      "avg_return",
      "max_drawdown"
    ]
  },
  "requiredKeys": []
}