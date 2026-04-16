- **Reddit data_fields mismatch**: Spec requires `["post_count", "comment_count", "sentiment_score"]` but code requests only `["post_count", "comment_count"]` (missing `sentiment_score`).
- **Signal logic window mismatch**: Spec requires a rolling 7-day window excluding the current day for percentage increase calculation; code uses a 7-day rolling mean including the current day and compares latest total to 1.5x the mean (not a percentage increase over prior 7 days excluding current).
- **Entry condition mismatch**: Spec triggers entry on a 50%+ percentage increase in total posts and comments over prior 7 days (excluding current day); code triggers on latest total > 1.5 * 7-day rolling mean (including current day), which is similar but not exactly the same logic.
- **Exit condition missing**: Spec defines exit conditions based on adjusted_close price below 7-day average or after 5 trading days, whichever comes first; code has no exit logic implemented.
- **Position sizing mismatch**: Spec allocates 5% per signal with max total exposure 20%; code allocates 20% per ticker (total 100%), exceeding max_total_exposure.
- **Data source for price data missing**: Spec requires integration with Yahoo Finance adjusted_close and volume data; code does not fetch or use any price data.
- **Sentiment score usage missing**: Spec includes sentiment_score as a data field and implies it is part of the signal; code fetches no sentiment_score and does not use it.
- **Implementation notes on fallback and backtesting missing**: Code does not show fallback handling for missing/delayed data or backtesting steps.

Summary: The code partially implements the spec but misses key elements around sentiment data, exact signal logic, exit conditions, position sizing, and price data integration.