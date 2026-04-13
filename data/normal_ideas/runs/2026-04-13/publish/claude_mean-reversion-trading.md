# Mean Reversion Trading

**Idea ID:** `mean-reversion-trading`
**Source:** anthropic / claude-3-haiku-20240307
**Frequency:** daily

## Thesis
Asset prices tend to revert to their long-term mean over time. By identifying assets trading above or below their historical average, we can exploit this mean reversion phenomenon to generate profits.

## Universe
- SPY
- QQQ
- GLD
- TLT

## Data Sources
- yfinance
- FRED

## Signal Logic
Calculate the Z-score of an asset's current price relative to its 200-day moving average. If the Z-score is greater than +1 (overbought), generate a sell signal. If the Z-score is less than -1 (oversold), generate a buy signal.

## Entry / Exit
Buy when the Z-score is less than -1, sell when the Z-score is greater than +1.

## Position Sizing
Equal-weight all positions in the portfolio.

## Risks
The model may underperform during periods of sustained market trends, as mean reversion may not occur as expected. It is also susceptible to whipsaws and false signals.

## Implementation Notes
1. Calculate the 200-day moving average for each asset. 2. Calculate the Z-score of the current price relative to the 200-day MA. 3. Generate buy/sell signals based on the Z-score thresholds. 4. Rebalance the portfolio accordingly.

## Required Keys
- None
