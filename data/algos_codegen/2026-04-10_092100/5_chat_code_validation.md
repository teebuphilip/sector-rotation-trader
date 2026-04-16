- In `_fetch_reddit_data`, the subreddits are passed as `["r/gaming", "r/pcgaming", "r/Games"]` but spec expects `["gaming", "pcgaming", "Games"]` (no "r/" prefix).
- The `compute_signal` method uses a 7-day EMA but does not handle the zero moving average edge case by enforcing a minimum threshold of 10 posts+comments.
- The signal triggers if combined activity rises more than 50% compared to 7-day EMA and baseline is at least 100 posts+comments — this is implemented correctly.
- The exit logic ("Sell when activity falls below 80% of the 7-day EMA or after 5 trading days") is missing entirely.
- Position sizing does not match spec:
  - Spec requires 5% total allocation per signal, max 2% per individual stock, max 20% total exposure with proportional reduction if exceeded.
  - Code allocates 20% per stock (0.2), totaling 100%, which violates spec.
- The code does not handle edge cases:
  - Missing data: partly handled by blocking and returning HOLD.
  - Zero moving average threshold: missing.
  - Overlapping signals within 5 trading days: missing.
  - Max exposure reached proportional reduction: missing.
  - Non-trading days exclusion from 5-day exit rule: missing.
- The `adapter_contracts` allowed kwargs (`subreddits`, `days_back`, `cache_key`) are not fully respected: `cache_key` is not passed to `fetch_reddit_activity`.
- The `target_allocations` method returns `None` on HOLD instead of an empty dict or zero allocations (minor).

Summary:  
- Subreddit names include "r/" prefix incorrectly.  
- Exit logic missing.  
- Position sizing allocation incorrect (20% per stock vs 5% total, max 2% per stock).  
- Edge cases mostly unhandled.  
- `cache_key` not passed to adapter call.  

Therefore, the code does **not** fully match the spec.