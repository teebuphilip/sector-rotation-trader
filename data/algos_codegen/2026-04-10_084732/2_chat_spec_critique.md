- **Missing Thresholds / Parameters:**
  - No explicit threshold for "falls below the 7-day moving average" on exit; is it any drop below or a specific percentage drop?
  - No minimum activity level or volume threshold to avoid noise from low-activity subreddits.
  - No threshold or rule for handling multiple simultaneous spikes (e.g., if multiple universe stocks spike same day).
  - No threshold for maximum position size per individual stock within the 5% allocation (e.g., if multiple stocks spike simultaneously).

- **Ambiguous Data Sources:**
  - `"reddit": {}` is empty; no details on which subreddits are monitored (only "target subreddits" mentioned in signal logic).
  - No specification if data includes posts, comments, or both separately or combined (signal logic says combined but data source is vague).
  - No mention of data latency or update time for Reddit data (important for daily frequency).

- **Missing Edge Cases:**
  - What if the 7-day moving average is zero or near zero (e.g., new subreddit or very low activity), causing division by zero or huge spikes?
  - No handling of weekends or holidays when Reddit activity or market trading is closed.
  - No rule for what happens if the stock price gaps significantly on entry or exit days.
  - No handling of partial fills or liquidity constraints for position sizing.
  - No rule for overlapping signals if a new spike occurs before the 5-day exit window ends.

- **Other Fixes / Clarifications:**
  - Clarify whether the 50% spike is relative to the combined posts+comments count or weighted by subreddit or stock relevance.
  - Define how the "combined activity" is aggregated across subreddits and mapped to individual stocks.
  - Specify if the 5 trading days exit window resets if a new spike is detected.
  - Clarify if "daily" frequency means calendar days or trading days.
  - Add risk management rules for max drawdown or stop loss per position.

**Summary of fixes:**
- Add explicit numeric thresholds for exit triggers and minimum activity.
- Specify exact subreddits and data fields used.
- Handle zero or near-zero moving averages.
- Define behavior for multiple simultaneous signals and overlapping positions.
- Clarify data update timing and frequency definitions.
- Add risk and liquidity management rules.