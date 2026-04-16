Here is a critique of the provided algo spec JSON, highlighting missing thresholds, ambiguous data sources, missing edge cases, and suggested fixes:

- **Missing Thresholds / Parameters:**
  - The **trigger threshold** is set as a 50% increase over 7 days, but:
    - No **minimum baseline volume** is specified (e.g., avoid triggering on very low absolute counts where 50% increase is noise).
    - No **maximum threshold** or upper bound to avoid extreme outliers.
  - The **exit conditions** are ambiguous:
    - "below_7day_moving_average" — unclear which metric this applies to (price? volume? signal metric?).
    - No threshold or tolerance for "below" (e.g., how much below the moving average triggers exit).
  - No **stop-loss** or risk management thresholds beyond time-based exit and moving average.
  - No **signal cooldown** or refractory period to prevent repeated triggers from the same spike.

- **Ambiguous Data Sources / Definitions:**
  - Reddit data:
    - "api_endpoints" list subreddit names, but no details on which API endpoints or data fields are used (e.g., new posts, comments, timestamps).
    - No specification on how "total_posts_plus_comments" is computed (e.g., are comments nested? Are deleted posts/comments excluded?).
    - No mention of timezone or timestamp normalization.
  - Yahoo Finance:
    - "price_data": true — no detail on which price (close, open, adjusted close) or frequency (daily, intraday).
  - Universe:
    - Stocks listed include MSFT, which is a broad tech company, not purely gaming-focused — rationale for inclusion is unclear.
  - Instruments in entry:
    - "gaming_hardware_stocks" and "gaming_publisher_stocks" are not explicitly mapped to ticker symbols or universe subsets.

- **Missing Edge Cases / Considerations:**
  - Handling **API rate limits** or partial data outages is mentioned as a risk but no mitigation strategy is specified.
  - No handling of **weekends/holidays** in Reddit data or trading days in price data.
  - No treatment of **spam or bot-generated posts/comments** which could cause false spikes.
  - No mention of **normalization for subreddit size differences** (e.g., r/gaming vs r/pcgaming have different baseline activity).
  - No handling of **multiple simultaneous signals** (e.g., spikes in multiple subreddits or multiple stocks).
  - No **validation or filtering** of posts/comments by relevance or sentiment (all posts/comments are treated equally).
  - No **latency or delay** consideration between Reddit signal and price reaction.
  - No **backtesting evaluation metrics** or success criteria defined.

---

### Suggested Fixes / Improvements

- **Add explicit thresholds and parameters:**
  - Define a **minimum baseline volume** threshold for posts+comments to avoid noise triggers.
  - Clarify the metric for exit condition (e.g., "price closing below 7-day moving average of closing prices by X%").
  - Add optional **stop-loss** or max drawdown limits.
  - Define a **signal cooldown period** (e.g., no new entry within N days of last trigger).

- **Clarify data sources and processing:**
  - Specify exact Reddit API endpoints and data fields used.
  - Define how posts and comments are counted (e.g., exclude deleted, spam).
  - Normalize counts by subreddit size or historical averages.
  - Specify Yahoo Finance price type (close, adjusted close) and frequency.
  - Map "gaming_hardware_stocks" and "gaming_publisher_stocks" to specific tickers or universe subsets.
  - Justify inclusion of MSFT or remove if out of scope.

- **Handle edge cases and risks:**
  - Implement retry/backoff logic for API limits and outages.
  - Account for non-trading days and align Reddit data timestamps accordingly.
  - Add spam/bot detection or filtering heuristics.
  - Consider weighting posts/comments by sentiment or engagement.
  - Define behavior for multiple simultaneous signals.
  - Include latency assumptions and potential delays in signal effectiveness.
  - Define backtesting metrics (e.g., hit rate, average return, drawdown).

- **Documentation and completeness:**
  - Populate `required_keys` with essential config keys.
  - Add examples or sample data for clarity.
  - Provide clear definitions for all terms used (e.g., "total_posts_plus_comments").

By addressing these points, the algo spec will be more robust, unambiguous, and implementable.