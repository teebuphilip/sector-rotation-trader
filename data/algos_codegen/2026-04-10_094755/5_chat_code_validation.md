- **Position sizing mismatch**:  
  - Spec states maximum position size per stock is 2% (0.02) and max total exposure is 20% (0.2).  
  - Code sets 2% per stock but does not enforce or mention max total exposure of 20%.  
  - Spec's `"allocation_per_signal": 0.05` (5%) conflicts with entry description and code uses 2% per stock, which matches entry description but not the `"allocation_per_signal"` field.

- **Entry description vs position sizing field conflict**:  
  - Spec entry description says max 2% per stock, code uses 2% per stock (OK).  
  - Spec position_sizing.allocation_per_signal is 0.05 (5%), which is not reflected in code.

- **Exit logic missing**:  
  - Spec exit: Sell when activity falls below 80% of 7-day moving average or after 5 trading days, whichever comes first.  
  - Code does not implement any exit logic.

- **Signal logic partial**:  
  - Spec trigger: combined daily posts+comments rise more than 50% compared to 7-day moving average AND 7-day moving average > 100.  
  - Code checks `latest["total"] > 1.5 * latest["ma7"]` and `latest["ma7"] > 100` which matches spec. OK.

- **Adapter usage**:  
  - Code uses `fetch_reddit_activity` with allowed kwargs `subreddits` and `days_back`. OK.

- **Data source subreddits**:  
  - Code uses subreddits exactly as in spec. OK.

- **Timezone**:  
  - Spec mentions timezone UTC, code does not explicitly handle timezone but likely assumed. No direct mismatch.

Summary:  
- Missing exit logic implementation.  
- Position sizing max total exposure (0.2) not enforced or mentioned.  
- Position sizing allocation_per_signal (0.05) in spec conflicts with entry description and code (which uses 0.02 per stock). Code follows entry description but not the allocation_per_signal field.

# Final verdict:

- Missing exit logic implementation.  
- Position sizing max total exposure (0.2) not enforced.  
- Spec's allocation_per_signal (0.05) conflicts with entry description and code (0.02 per stock). Code matches entry description, not allocation_per_signal field.