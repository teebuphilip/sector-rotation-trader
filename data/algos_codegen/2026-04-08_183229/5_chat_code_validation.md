- The code uses `TRIGGER_BASELINE = "previous_7day_average"` as a string parameter passed to `percentage_increase()`. The spec expects the baseline to be the previous 7-day average, but it is unclear if the `percentage_increase` function accepts a string `"previous_7day_average"` or expects an actual numeric baseline series. The code does not show computing the rolling 7-day average explicitly before passing it as baseline, which may be a mismatch.

- The code's `_calculate_signal` method sums posts and comments but does not explicitly filter out deleted posts/comments as required by the spec ("excluding deleted content"). It depends on `get_reddit_data` to have done this filtering, but this is not shown or asserted.

- The exit conditions in the spec include two conditions with "whichever comes first":  
  1) below 0.95 * 7-day average  
  2) after 5 trading days  
  The code does not implement any exit logic or mention handling these exit conditions.

- The code's `target_allocations` method sets `target_weight` to 0.05 for rows where `"signal_triggered"` is True but does not enforce the `max_total_exposure` of 0.20 across positions. It just adds a column `"max_total_exposure"` with the value 0.20 but does not implement any logic to cap total exposure.

- The code does not show any handling of missing price data or non-trading days for exit timing, which is mentioned in the spec under integration notes.

- The code does not show any retry logic, fallback data sources, or monitoring for API rate limits or data anomalies as per the spec's error handling notes.

- The code does not show any backtesting or out-of-sample validation logic as required by the spec.

Summary:

- Missing explicit rolling 7-day average baseline calculation for trigger condition  
- No explicit filtering of deleted posts/comments shown  
- No implementation of exit conditions logic  
- No enforcement of max total exposure limit  
- No handling of missing price data or non-trading days for exit timing  
- No error handling for API limits or data quality monitoring  
- No backtest or validation code

If the code relies on external utilities to handle some of these (e.g., filtering deleted content in `get_reddit_data`, baseline calculation inside `percentage_increase`), it should be explicitly confirmed or documented.

Otherwise, these are mismatches with the spec.

---

**Final bullet list of mismatches:**

- No explicit calculation of previous 7-day average baseline before calling `percentage_increase`; baseline passed as string instead of numeric series.  
- No explicit filtering of deleted posts/comments in Reddit data processing.  
- Exit conditions (`below_7day_average` threshold and `after_5_trading_days`) are not implemented or handled.  
- Max total exposure (0.20) is not enforced in position sizing logic.  
- Missing handling of missing price data and non-trading days for exit timing.  
- No retry logic or fallback data sources for API rate limits or outages.  
- No monitoring or alerting for data quality anomalies.  
- No backtesting or out-of-sample validation code present.