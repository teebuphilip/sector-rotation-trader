- **Signal logic mismatch**:  
  - Spec trigger condition requires a **daily percentage increase >= 50%** compared to the 7-day moving average, with a minimum volume of 100.  
  - Code checks if `total_activity >= 1.5 * avg_activity` (equivalent to 50% increase) and `total_activity >= 100`, but `total_activity` is the sum over 7 days, not the daily count.  
  - The code incorrectly sums posts/comments over 7 days and then divides by 7 to get avg_activity, but uses total 7-day activity as the "daily" activity for comparison. The spec requires daily counts compared to 7-day moving average of daily counts.

- **Data collection window mismatch**:  
  - Spec requires daily counts of posts and comments (with timezone normalization to UTC), excluding deleted posts/comments, and deduplicating crossposts/reposts.  
  - Code fetches posts/comments from `as_of - 7 days` to `as_of + 1 day` (8 days total) and sums all posts/comments in that window as total activity. It does not fetch or compute daily counts, nor does it exclude deleted posts/comments or deduplicate crossposts/reposts.

- **Entry/exit logic mismatch**:  
  - Spec entry condition is based on signal trigger; exit condition is either activity falls below 95% of 7-day average or 5 trading days passed, whichever comes first.  
  - Code only implements signal generation and target allocation; no exit logic or tracking of days passed or activity falling below threshold is implemented.

- **Position sizing mismatch**:  
  - Spec allocates 5% per signal with max total exposure 20%, prorating if multiple signals.  
  - Code allocates 20% to each ticker (total 100%) when signal is "RISK_ON", ignoring spec sizing and max exposure constraints.

- **Noise filtering missing**:  
  - Spec requires capping max daily increase at 100% and requiring sustained increase for 3 days.  
  - Code does not implement any noise filtering or sustained increase checks.

- **Data source usage mismatch**:  
  - Spec states to use Reddit API with exclusion of deleted posts/comments and deduplication, and Yahoo Finance for price data integration.  
  - Code uses Pushshift API (not Reddit API), does not exclude deleted content or deduplicate, and does not integrate Yahoo Finance data.

- **Comments inclusion mismatch**:  
  - Spec requires counting comments created on the day only.  
  - Code fetches comments over 7 days and sums total comments, not daily counts.

- **Implementation notes mismatch**:  
  - Spec requires computing rolling averages and percentage changes; code only computes a simple average over 7 days without rolling or percentage change calculations.

- **Signal output mismatch**:  
  - Spec does not specify signal strings; code returns "RISK_ON" or "HOLD". This may be acceptable but is not explicitly stated.

**Summary**: The code does not correctly implement the spec's data collection, signal logic, entry/exit rules, position sizing, noise filtering, or data source requirements.

# Final verdict: **Mismatches found as above.**