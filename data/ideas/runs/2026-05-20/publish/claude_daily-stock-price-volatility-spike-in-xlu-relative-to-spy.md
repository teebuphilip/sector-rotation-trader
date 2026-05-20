# Daily Stock Price Volatility Spike In Xlu Relative To Spy

**Idea ID:** `daily-stock-price-volatility-spike-in-xlu-relative-to-spy`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Utilities volatility spikes when energy cost shocks or grid stress events create input price uncertainty; relative volatility surge precedes defensive sector rotation. Utilities volatility spikes often reverse as defensive money rotates into the sector; mean reversion opportunity.

## Universe
- XLU

## Data Sources
- Yahoo Finance daily prices for XLU (utilities ETF) and SPY via price_only adapter

## Signal Logic
When 5-day rolling volatility (realized standard deviation) of XLU exceeds that of SPY by 1.5x or more

## Entry / Exit
Entry: When 5-day rolling volatility (realized standard deviation) of XLU exceeds that of SPY by 1.5x or more Exit: After 8 trading days or once XLU volatility falls back to within 1.1x of SPY volatility

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily prices for XLU (utilities ETF) and SPY via price_only adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Utilities experience weekly volatility shocks; 1.5x threshold fires regularly during macro uncertainty or energy market turbulence.

## Required Keys
- None
