- **Universe mismatch in signal triggering:**  
  Spec entry action triggers only on ["ATVI", "EA", "NVDA"], but code applies signal and allocates to all universe tickers ["ATVI", "EA", "NVDA", "TTWO", "MSFT"].

- **Signal logic - percentage change calculation:**  
  Spec requires daily percentage increase compared to 7-day moving average:  
  `(today - 7-day avg) / 7-day avg` > 50%  
  Code computes `(total_activity - avg_activity) / avg_activity` which is correct.

- **Signal logic - minimum daily activity threshold:**  
  Spec requires total posts+comments > 1000, code matches this.

- **Signal logic - data aggregation:**  
  Spec requires sum of posts and comments (excluding deleted/removed) from three subreddits.  
  Code fetches only submissions (posts) via Pushshift API endpoint `/submission/search/`, no comments fetched.  
  **Mismatch:** Comments are missing from data aggregation.

- **Data fetching - API endpoint:**  
  Spec states to use Reddit API (official), code uses Pushshift API (third-party).  
  This is an implementation detail, possibly acceptable, but worth noting.

- **7-day moving average calculation:**  
  Code calls `_get_reddit_data` recursively for last 7 days, but `_get_reddit_data` returns a dict with keys `total_posts_and_comments` and `avg_posts_and_comments`.  
  In the loop:  
  ```python
  avg_posts_and_comments += sum(reddit_data.values())
  ```  
  `reddit_data.values()` includes both total and avg, so summing them is incorrect.  
  It should sum only total posts and comments for each day.  
  **Mismatch:** 7-day average calculation incorrectly sums both total and avg values.

- **7-day moving average denominator:**  
  Code divides by `len(trading_days)` which is the number of trading days in the 7-day window.  
  Spec does not specify trading days, but daily data in UTC.  
  Using trading days may exclude some days, causing inconsistency.  
  **Minor mismatch:** Spec expects daily data, code uses trading days count for averaging.

- **Entry/Exit logic:**  
  Code only implements `compute_signal` and `target_allocations` (entry).  
  Spec requires exit conditions:  
  - activity falls below 7-day average by 10%  
  - 5 trading days passed  
  And cooldown logic (3 days cooldown if activity remains above 7-day average by 20%).  
  Code does not implement exit or cooldown logic.  
  **Mismatch:** Exit and cooldown logic missing.

- **Position sizing:**  
  Spec: allocation per signal 0.05, max total exposure 0.2.  
  Code applies 0.05 per ticker, then rescales if total > 0.2.  
  Matches spec.

- **Signal frequency:**  
  Spec: daily  
  Code: `rebalance_frequency` returns "daily"  
  Matches spec.

- **Time zone:**  
  Spec requires UTC time zone and collection at 00:00 UTC.  
  Code uses date with no explicit timezone handling, but date formatting is in `%Y-%m-%d` which is date only.  
  No explicit timezone handling or collection time enforcement.  
  **Minor mismatch:** No explicit UTC enforcement.

- **Data filtering:**  
  Spec excludes deleted/removed content.  
  Code counts length of posts returned by Pushshift, no filtering for deleted/removed posts/comments.  
  **Mismatch:** No filtering for deleted/removed content.

- **Comments data:**  
  Spec requires sum of posts and comments.  
  Code fetches only posts (submissions).  
  **Mismatch:** Comments missing.

- **Registry code incomplete:**  
  Provided registry snippet is truncated and incomplete.  
  **Minor mismatch:** incomplete registry code.

---

### Summary of mismatches:

- Universe for signal triggering and allocation includes all 5 tickers, but spec entry triggers only on 3 tickers (ATVI, EA, NVDA).  
- Comments data missing; code fetches only posts, spec requires posts + comments.  
- 7-day moving average calculation incorrectly sums total and average values together.  
- 7-day moving average denominator uses trading days count, spec expects daily data.  
- Exit and cooldown logic not implemented.  
- No filtering of deleted/removed posts/comments.  
- No explicit UTC timezone handling or collection time enforcement.  
- Registry code incomplete.

If these are addressed, code would match spec.