{
  "name": "reddit-gaming-thread-spike",
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
          "created_utc"
        ],
        "rateLimit": {
          "maxRequests": 60,
          "windowMs": 60000
        }
      }
    },
    "priceData": {
      "source": "Yahoo Finance API",
      "frequency": "daily",
      "adjustedPrices": true
    }
  },
  "signalLogic": {
    "description": "Calculate the daily percentage increase in total new posts and new comments in target subreddits. Signal triggers when either posts or comments rise more than 50% compared to the 7-day moving average, with a minimum absolute volume threshold of 1000 posts or 5000 comments.",
    "thresholds": {
      "postPercentIncrease": 50,
      "commentPercentIncrease": 50,
      "postMovingAverage": 7,
      "commentMovingAverage": 7,
      "minPostVolume": 1000,
      "minCommentVolume": 5000
    }
  },
  "entryExit": {
    "entry": {
      "condition": "on day of spike detection",
      "assets": [
        "ATVI",
        "EA",
        "NVDA",
        "TTWO",
        "MSFT"
      ]
    },
    "exit": {
      "condition": "when either posts or comments fall below their respective 7-day moving averages for 2 consecutive trading days, or after 5 trading days, whichever comes first"
    },
    "reEntry": {
      "condition": "if a new spike is detected at least 3 trading days after the previous exit"
    }
  },
  "positionSizing": {
    "allocation": 5,
    "maxExposure": 20,
    "maxPositionPerAsset": 10
  },
  "risks": [
    "False positives from viral posts unrelated to business fundamentals",
    "Short-lived spikes with no price follow-through",
    "API rate limits or data outages",
    "Sector-wide selloffs overriding signal",
    "Distortion from bot activity or deleted content on Reddit"
  ],
  "implementation": {
    "description": "Use Reddit API to pull daily counts of new posts and new comments from target subreddits. Compute rolling averages and percentage changes, applying minimum volume thresholds. Integrate with adjusted price data from Yahoo Finance API to manage entry/exit and re-entry. Implement error handling for missing data and outlier detection to smooth viral spikes. Backtest on historical Reddit and price data.",
    "timeZone": "UTC"
  },
  "requiredKeys": [
    "redditApiKey",
    "yahooFinanceApiKey",
    "minPostVolume",
    "minCommentVolume",
    "postPercentIncrease",
    "commentPercentIncrease",
    "postMovingAverage",
    "commentMovingAverage",
    "maxPositionPerAsset"
  ]
}