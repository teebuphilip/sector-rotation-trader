- The spec requires tracking **new posts and new comments** counts, but the code only sums `num_comments` and counts posts as `num_posts = 1` per post, which is correct. However, the spec fields include `num_comments`, but the code does not explicitly verify that comments counted are only from new posts or new comments separately. The code sums `num_comments` per post, which is acceptable.

- The spec requires calculating the **7-day moving average** and comparing the current day’s total posts and comments to that average. The code calculates rolling means on the same day’s data (`subreddit_data`), which only contains one day (as it groups by `created_date` for the `as_of` date). Rolling mean on a single day’s data is invalid and will return NaN or the same value. The code does not fetch or use historical data for the moving average calculation, violating the spec.

- The spec requires the signal to trigger when **either posts or comments rise more than 50% compared to the 7-day moving average**, with minimum absolute volume thresholds. The code implements this logic correctly in `compute_signal`, but since the moving average is incorrectly computed (only on one day’s data), the logic is flawed.

- The spec requires **exit condition**: when posts or comments fall below their respective 7-day moving averages for 2 consecutive trading days, or after 5 trading days, whichever comes first. The code does not implement any exit logic or track consecutive days or days since entry.

- The spec requires **re-entry condition**: if a new spike is detected at least 3 trading days after the previous exit. The code does not implement any re-entry logic.

- The spec requires **position sizing**: allocation 5% per asset, max exposure 20%, max position per asset 10%. The code allocates 20% per asset (0.2), which sums to 100% total, violating the spec’s max exposure (20%) and max position per asset (10%).

- The spec requires **dataSources** including Reddit API with specified fields and rate limits, and Yahoo Finance API for price data. The code fetches Reddit data but does not integrate or use Yahoo Finance price data for entry/exit or re-entry logic.

- The spec requires **error handling for missing data and outlier detection**. The code handles missing Reddit data by returning "HOLD" but does not implement outlier detection or smoothing viral spikes.

- The spec requires **timeZone: UTC**. The code converts `created_utc` timestamps to dates but does not explicitly mention or enforce UTC timezone handling.

Summary:

- Moving average calculation is incorrect (only one day’s data used).
- Exit and re-entry logic missing.
- Position sizing allocations do not match spec (20% per asset vs 5% per asset max 10%).
- No integration with Yahoo Finance price data.
- No outlier detection or smoothing.
- Timezone handling not explicit.

**Mismatches:**

- Moving average calculation uses only current day data, not 7-day historical data.
- Exit condition logic (2 consecutive days below MA or 5 days max) not implemented.
- Re-entry condition logic (3 days after exit) not implemented.
- Position sizing allocations exceed spec limits (allocates 20% per asset instead of max 10%).
- No use of Yahoo Finance price data for entry/exit decisions.
- No outlier detection or viral spike smoothing.
- Timezone handling (UTC) not explicitly enforced.

If you want me to list these as bullet points, here they are.