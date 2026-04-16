- **Missing Thresholds:**
  - No explicit threshold for "activity falls below the 7-day moving average" in exit condition (e.g., by what % below the average should exit trigger?).
  - No minimum volume or minimum baseline activity threshold to avoid triggering on very low activity days.
  - No threshold or criteria for maximum position size per individual stock within the 5% allocation.

- **Ambiguous Data Sources:**
  - `reddit` data source is empty; no specification of which subreddits to monitor (only "target subreddits" mentioned in signal logic but not defined).
  - No clarity on how posts and comments are aggregated (e.g., are deleted posts/comments excluded?).
  - No mention of timezone or timestamp normalization for daily aggregation.

- **Missing Edge Cases:**
  - Handling of missing or incomplete data days (e.g., Reddit API downtime or data gaps).
  - What if the 7-day moving average is zero or near zero (division by zero risk in percentage increase calculation)?
  - Handling of overlapping signals if multiple spikes occur within 5 trading days.
  - What if the portfolio cannot allocate full 5% due to max_total_exposure limit already reached?
  - No guidance on partial exits or scaling out of positions.
  - No handling of non-trading days or holidays affecting the 5 trading days exit rule.

- **Other Fixes:**
  - Clarify if "daily" frequency means calendar days or trading days.
  - Specify whether the 7-day moving average is simple or exponential.
  - Define how to handle multiple stocks in the universe if only some show spikes.
  - Add validation for input parameters and data sanity checks.

**Summary of fixes:**
- Define exact subreddits to monitor in `data_sources.reddit`.
- Specify numeric thresholds for exit trigger (e.g., % below 7-day MA).
- Add minimum baseline activity threshold to avoid noise.
- Clarify aggregation method and data cleaning rules.
- Handle zero or near-zero moving average cases.
- Define behavior on missing data or API failures.
- Specify timezone and date normalization.
- Clarify position sizing rules when max exposure is reached.
- Define handling of overlapping signals and multiple spikes.
- Clarify calendar vs trading day frequency and holiday handling.
- Specify moving average type (SMA vs EMA).
- Add edge case handling for partial fills or scaling out.