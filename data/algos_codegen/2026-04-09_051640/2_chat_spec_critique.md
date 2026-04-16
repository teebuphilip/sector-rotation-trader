Here is a critique of the provided algo spec JSON with identified issues and recommended fixes:

### Missing Thresholds / Parameters
- **Ambiguous threshold units:**  
  The `"threshold": 1.5` under `signal_logic.trigger_condition` is unclear whether it means a 50% increase (1.5x) or 150% increase. The description says "more than 50%," so clarify threshold as `0.5` or explicitly state multiplier is 1.5x baseline.

- **No threshold for exit condition `"activity_below_ma7"`:**  
  The exit condition mentions `"activity_below_ma7"` but does not specify how much below (e.g., any drop below MA7, or a specific percentage drop). This should be quantified.

- **No thresholds for position sizing risk management:**  
  No stop-loss or max drawdown limits are defined to protect capital if the signal fails.

### Ambiguous / Missing Data Sources
- **No sentiment data included:**  
  The thesis mentions "social sentiment shifts," but only volume (posts + comments) is tracked. Sentiment analysis (positive/negative tone) could improve signal quality.

- **No data source for subreddit activity timestamps:**  
  The spec assumes daily aggregation but does not specify how to handle timezone differences or partial day data.

- **Yahoo Finance data limited to `"price"` only:**  
  No volume, volatility, or other market data fields are included, which could help refine entry/exit decisions.

- **No historical Reddit data source for backtesting:**  
  The implementation notes mention backtesting but do not specify where or how to obtain historical Reddit data.

### Missing Edge Cases / Handling
- **Handling zero or very low baseline activity:**  
  If the 7-day moving average is near zero (e.g., very low subreddit activity), a small absolute increase could trigger a large percentage spike. Need a minimum baseline threshold to avoid false triggers.

- **Handling days with missing or incomplete Reddit data:**  
  No mention of how to handle API outages, rate limits, or missing data days in calculations.

- **Overlap of multiple signals on same day:**  
  If multiple spikes occur within short periods, how to handle re-entry or position scaling?

- **No handling of weekends or holidays:**  
  Reddit activity and market trading days differ; no mention of aligning these or skipping non-trading days.

- **No mention of how to handle partial data days (e.g., early market close or Reddit API delays).**

### Other Ambiguities / Improvements
- **Inconsistent universe between entry and universe:**  
  Universe includes 5 tickers, but entry only trades 3. Clarify rationale or align lists.

- **No explicit time zone or timestamp format specified for data pulls.**

- **No mention of signal decay or weighting recent days more heavily in moving average.**

- **No explicit mention of how to combine posts and comments (equal weight?).**

- **No mention of how to handle subreddit additions/removals over time.**

---

### Summary of Fixes

- Clarify threshold units for `trigger_condition.threshold` (e.g., 0.5 for 50% increase or multiplier 1.5x).
- Define numeric threshold for exit condition `"activity_below_ma7"` (e.g., drop below 90% of MA7).
- Add minimum baseline activity threshold to avoid false triggers on near-zero volumes.
- Include sentiment analysis data source or clarify why only volume is used.
- Specify handling of missing/incomplete Reddit data and API rate limits in signal logic.
- Add handling for weekends, holidays, and partial data days aligning Reddit and market data.
- Clarify how posts and comments are combined (equal weighting or weighted).
- Specify time zone and timestamp formats for data pulls.
- Add stop-loss or max drawdown thresholds in position sizing or risk management.
- Align universe and entry instruments or explain differences.
- Specify source or method for obtaining historical Reddit data for backtesting.
- Define rules for multiple signals in short timeframes (e.g., cooldown period).
- Consider adding additional Yahoo Finance fields (volume, volatility) for better exit logic.
- Add implementation notes on data validation and error handling.

Implementing these fixes will improve clarity, robustness, and practical usability of the algo spec.