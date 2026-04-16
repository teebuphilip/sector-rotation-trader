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
          "https://www.reddit.com/r/gaming/new.json",
          "https://www.reddit.com/r/pcgaming/new.json",
          "https://www.reddit.com/r/games/new.json"
        ],
        "fields": [
          "title",
          "num_comments",
          "created_utc"
        ]
      }
    },
    "priceData": {
      "source": "Yahoo Finance",
      "fields": [
        "close",
        "volume"
      ],
      "frequency": "daily"
    }
  },
  "signalLogic": {
    "description": "Calculate the daily percentage increase in total new posts plus comments in target subreddits. Signal triggers when combined activity rises more than 50% compared to the 7-day moving average, and the baseline activity is above a minimum threshold of 100 new posts plus comments.",
    "thresholds": {
      "percentIncrease": 50,
      "movingAverage": 7,
      "minBaselineActivity": 100
    }
  },
  "entryExit": {
    "entry": {
      "condition": "on day of spike detection",
      "assets": [
        "ATVI",
        "EA",
        "NVDA"
      ]
    },
    "exit": {
      "condition": "when activity falls below 80% of the 7-day moving average or after 5 trading days, whichever comes first"
    }
  },
  "positionSizing": {
    "allocation": 5,
    "maxExposure": 20
  },
  "risks": [
    "False positives from viral posts unrelated to business fundamentals",
    "Short-lived spikes with no price follow-through",
    "API rate limits or data outages",
    "Sector-wide selloffs overriding signal"
  ],
  "implementation": {
    "description": "Use Reddit API to pull daily counts of new posts and comments from target subreddits. Compute rolling averages and percentage changes. Integrate with daily close and volume data from Yahoo Finance to manage entry/exit. Backtest on historical Reddit and price data to validate the strategy."
  },
  "requiredKeys": []
}