Here is a critique of the provided algo spec JSON with identified issues and recommended fixes:

### Missing Thresholds / Parameters
- **Ambiguous threshold for "percentage_increase" trigger**  
  - The spec states `"threshold": 50` but does not clarify if this is a 50% increase relative to the previous day, previous 7-day average, or some other baseline.  
  - **Fix:** Specify baseline for percentage increase calculation (e.g., compared to previous 7-day average or previous day).

- **No threshold for "below_7day_average" exit condition**  
  - The exit condition triggers when the signal is "below_7day_average" but no threshold or tolerance is defined (e.g., does it trigger immediately when below average by any amount, or only after a sustained drop?).  
  - **Fix:** Define threshold or persistence criteria for exit (e.g., below 7-day average for 2 consecutive days).

- **No thresholds or conditions for position sizing limits**  
  - `"allocation_per_signal": 5` and `"max_total_exposure": 20` are given but no unit or context (percent of portfolio? dollars?).  
  - **Fix:** Clarify units (e.g., 5% of portfolio per signal, max 20% total exposure).

### Ambiguous Data Sources / Metrics
- **"total_posts_plus_comments" metric is vague**  
  - Does this metric count unique posts and comments combined? Are comments nested or only top-level? Are deleted posts/comments filtered out?  
  - **Fix:** Define exact counting methodology (e.g., count all posts and comments including replies, exclude deleted content).

- **No mention of time zone or timestamp alignment for Reddit data**  
  - Daily counts depend on consistent time zones; unclear how daily windows are defined.  
  - **Fix:** Specify time zone and cutoff time for daily aggregation.

- **No data source or method for sentiment analysis despite thesis mentioning "social sentiment shifts"**  
  - The spec only tracks volume (posts + comments), but thesis references sentiment shifts.  
  - **Fix:** Either remove sentiment reference or add sentiment analysis data source and logic.

### Missing Edge Cases / Handling
- **No handling of low volume or sparse data periods**  
  - What if subreddit activity is very low or zero? Percentage increase could be misleading or undefined (division by zero).  
  - **Fix:** Add minimum volume thresholds or smoothing to avoid false triggers on low base activity.

- **No handling of overlapping signals or multiple subreddit spikes**  
  - If spikes occur in multiple subreddits simultaneously, how are signals aggregated or weighted?  
  - **Fix:** Define aggregation logic or priority rules for multiple subreddit signals.

- **No handling of ticker-to-subreddit mapping**  
  - The universe includes MSFT, but MSFT is not included in entry instruments. Also, no rationale or mapping between subreddits and tickers is provided.  
  - **Fix:** Clarify how subreddits relate to tickers and why some tickers are excluded from entry.

- **No handling of market holidays or missing price data**  
  - Exit condition includes "after_5_trading_days" but no mention of how to handle non-trading days or missing price data.  
  - **Fix:** Specify how to count trading days and handle missing data.

- **No risk mitigation for API rate limits or data outages beyond listing as a risk**  
  - No fallback or retry logic described.  
  - **Fix:** Add implementation notes on error handling and data quality checks.

### Additional Suggestions
- **Add "required_keys" or mandatory config parameters**  
  - Currently empty; useful to enforce presence of critical config fields.

- **Clarify "frequency": "daily"**  
  - Does this mean signal is generated once per day after market close? Specify timing.

- **Backtest details are minimal**  
  - No mention of performance metrics, lookback period, or validation approach.  
  - **Fix:** Expand backtest methodology.

---

### Summary of Fixes
- Specify baseline for percentage increase calculation (e.g., vs prior 7-day average).  
- Define threshold or persistence for "below_7day_average" exit condition.  
- Clarify units for position sizing parameters (percent of portfolio, dollars, etc.).  
- Define exact counting method for "total_posts_plus_comments" metric.  
- Specify time zone and daily aggregation cutoff for Reddit data.  
- Add sentiment analysis data source or remove sentiment references.  
- Add minimum volume thresholds to avoid false triggers on low activity.  
- Define aggregation or prioritization logic for multiple subreddit signals.  
- Clarify ticker-to-subreddit mapping and rationale for entry instrument selection.  
- Specify handling of market holidays and missing price data for exit timing.  
- Add error handling and fallback strategies for API rate limits and data outages.  
- Populate "required_keys" with mandatory config fields.  
- Clarify timing of daily signal generation relative to market hours.  
- Expand backtest methodology with metrics and validation details.