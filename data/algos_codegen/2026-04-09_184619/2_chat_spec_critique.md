- **Missing Thresholds / Ambiguities:**
  - The `signal_logic.trigger.threshold` is set to 50 (percent increase) over a 7-day window, but it is unclear if this applies to combined posts + comments or separately. Clarify if the metric is aggregated or if spikes in posts vs comments are weighted differently.
  - No threshold or definition for what constitutes "below_moving_average" in the exit condition. Specify the moving average type (e.g., 10-day SMA, 20-day EMA) and exact threshold for exit.
  - The exit condition includes "after_5_trading_days" but the `window` is 7 — clarify if the 7-day window applies to moving average calculation or exit timing.
  - Position sizing: `allocation_per_signal` is 5 (percent?), but no unit specified. Clarify if this is % of portfolio or fixed units.
  - No threshold or filter on minimum volume or liquidity of stocks to avoid illiquid trades.

- **Ambiguous Data Sources:**
  - Reddit data source only specifies subreddits but no mention of filtering by post/comment type (e.g., excluding deleted or removed content).
  - No specification on how to handle bot/spam posts or comments that could skew counts.
  - No mention of timezone or timestamp normalization for daily counts.
  - Yahoo Finance data source is generic; no details on which price fields are used (close, adjusted close, volume).

- **Missing Edge Cases:**
  - Handling of zero or very low baseline activity in subreddits (e.g., if previous 7-day average is near zero, a small absolute increase could trigger a huge percentage spike).
  - No handling of weekends/holidays when Reddit activity or market trading is lower or absent.
  - No mention of how to handle missing data days or API outages.
  - No logic for overlapping signals or conflicting signals across multiple subreddits.
  - No stop-loss or risk management beyond exit conditions.
  - No handling of multiple simultaneous signals exceeding max total exposure (how to prioritize or scale down positions).

- **Other Suggestions:**
  - Add sentiment analysis or keyword filtering to reduce false positives from viral but irrelevant posts.
  - Specify backtesting period and data availability for Reddit historical data.
  - Clarify how to handle corporate actions (splits, dividends) in price data integration.
  - Define how to aggregate signals across the universe (e.g., if spike in r/gaming relates to ATVI but not MSFT, how to assign weights).

---

### Summary of Fixes

- Define exact metric calculation: combined posts+comments or separate; how to handle low baseline values.
- Specify moving average type and parameters for exit condition.
- Clarify timing windows for exit conditions and signal triggers.
- Specify units for position sizing and max exposure.
- Add filters for spam/bot content and data quality checks on Reddit data.
- Normalize timestamps and handle non-trading days.
- Add handling for missing data and API outages.
- Define logic for multiple simultaneous signals and exposure scaling.
- Include sentiment or keyword filters to reduce false positives.
- Clarify price data fields and corporate action adjustments.
- Add stop-loss or additional risk management rules.
- Specify backtesting data availability and methodology.