# Retail Roulette

**Idea ID:** `retail-roulette`
**Source:** anthropic / claude-3-haiku-20240307
**Frequency:** daily

## Thesis
Retail stocks exhibit high volatility and frequent swings in investor sentiment, often leading to sharp drawdowns and bounces. Retail is a key discretionary consumer spending proxy.

## Universe
- XLY

## Data Sources
- Yahoo Finance daily prices for XRT and SPY through price_only adapter

## Signal Logic
If XRT closes down more than 2% from its 10-day high

## Entry / Exit
Entry: If XRT closes down more than 2% from its 10-day high Exit: After 5 trading days or once XRT recovers to within 1% of its 10-day high

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily prices for XRT and SPY through price_only adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Retail stocks often experience volatile 2%+ daily moves, especially in the current economic environment.

## Required Keys
- None
