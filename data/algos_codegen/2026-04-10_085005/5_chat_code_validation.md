- **Position sizing mismatch**:  
  Spec states "5% per stock" with "max_total_exposure" 20%, but code allocates 20% per stock (total 100%).  
- **Entry logic mismatch**:  
  Spec entry says "Buy gaming hardware or publisher stocks (e.g., ATVI, EA, NVDA)" — implying only those 3 stocks, but code buys all 5 stocks in universe.  
- **Exit logic missing**:  
  Spec exit condition ("Sell when activity falls below 95% of 7-day EMA or after 5 trading days") is not implemented in code.  
- **Adapters list missing in code**:  
  Spec lists adapter "reddit_activity" but code does not explicitly declare or register adapters (may be acceptable depending on framework).  
- **Signal logic condition matches spec**:  
  Code correctly implements the trigger condition as per spec.  
- **Data sources parameters match spec**:  
  Subreddits, activity types, timezone, and missing data handling match spec.  

Summary: The main mismatches are in position sizing, entry universe, and missing exit logic.