# Volatility Spike Follow-Through

**Idea ID:** `volatility-spike-follow-through`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden large spikes in implied volatility often indicate upcoming sharp moves in the underlying asset's price. By identifying when implied volatility surges beyond recent norms and then observing the following day's price direction, we can capture momentum trades that exploit volatility-driven breakouts or breakdowns.

## Universe
- SPY
- AAPL
- TSLA
- MSFT
- AMZN
- NVDA
- GOOG
- META
- NFLX
- AMD

## Data Sources
- Yahoo Finance (for options implied volatility and price data)
- CBOE website (for VIX and related volatility indices)

## Signal Logic
Identify stocks where the implied volatility percentile (over the last 30 days) jumps above 80% compared to the previous day, with at least a 15% increase in IV. On the following trading day, if the stock price moves at least 1.5% in the direction of the IV spike (positive or negative), trigger entry.

## Entry / Exit
Entry: Buy if IV spikes and next-day price moves up >=1.5%; short if price moves down >=1.5%. Exit: Close position after 3 trading days or if price retraces 1% against the position.

## Position Sizing
Allocate 2% of portfolio capital per position to limit risk from volatility whipsaws.

## Risks
False signals during earnings or news events; IV spikes can be driven by option demand unrelated to directional moves; rapid reversals causing stop-loss hits; liquidity constraints in options data.

## Implementation Notes
Fetch daily implied volatility data from Yahoo Finance options chains; calculate 30-day IV percentiles and daily changes; monitor price moves next day; implement logic to enter/exit trades and track stops; backtest over last 6 months to validate thresholds.

## Required Keys
- None
