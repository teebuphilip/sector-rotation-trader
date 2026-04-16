- **Missing Thresholds / Parameters:**
  - The exit condition "activity falls below the 7-day moving average" is ambiguous without a numeric threshold (e.g., does it trigger on any drop below the average or a certain % drop?).
  - No minimum volume or minimum baseline activity threshold to avoid false positives from very low activity days.
  - No threshold or criteria for what constitutes "target subreddits" in the data request or signal logic.
  - No threshold or limit on maximum position size per individual stock within the 5% allocation per signal.

- **Ambiguous Data Sources:**
  - `data_sources.reddit` is empty; no specification of which subreddits to monitor or how they map to the universe stocks.
  - The "combined daily posts plus comments in target subreddits" is not explicitly linked to the universe stocks (e.g., which subreddits correspond to which stocks?).
  - The adapter contract allows `subreddits` as a parameter but no subreddits are specified anywhere in the spec.
  - No mention of timezone or date alignment between Reddit activity data and market trading days.

- **Missing Edge Cases:**
  - Handling of missing or incomplete Reddit data for certain days (e.g., API downtime or data gaps).
  - What if the 7-day moving average is zero or near zero, causing division or percentage increase calculations to be unstable?
  - Handling multiple signals triggering on the same day for multiple stocks—how to allocate position sizing if max exposure is reached?
  - No logic for overlapping signals or re-entry after exit within a short timeframe.
  - No handling of weekends or holidays when Reddit activity might differ and markets are closed.
  - No consideration of outlier spikes or data anomalies (e.g., spam or bot activity inflating counts).

- **Additional Suggestions:**
  - Specify exact subreddits to monitor or provide a mapping from universe stocks to relevant subreddits.
  - Clarify if the 50% spike threshold applies to each stock individually or combined across all universe stocks.
  - Define how to handle partial fills or liquidity constraints if multiple signals trigger simultaneously.
  - Add a cooldown or minimum holding period before re-entry after exit to avoid whipsaw trades.
  - Include validation or sanity checks on input data (e.g., minimum data points for moving average calculation).