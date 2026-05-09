# Copper Price Momentum Mean Reversion Industrial Cycle

**Idea ID:** `copper-price-momentum-mean-reversion-industrial-cycle`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Copper is a leading cyclical indicator. Sharp 3–5 day rallies above the 50-day moving average often reverse within a week as overextension unwinds, creating mean reversion trades. Copper strength signals manufacturing demand and infrastructure investment; materials and industrials benefit.

## Universe
- XLB

## Data Sources
- Yahoo Finance daily prices for CU (Copper Futures ETF) or commodity copper index through price_only adapter

## Signal Logic
If copper price rallies 4%+ in 3 trading days and closes above 50-day MA by 2%+

## Entry / Exit
Entry: If copper price rallies 4%+ in 3 trading days and closes above 50-day MA by 2%+ Exit: After 6 trading days or if price falls back below 50-day MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily prices for CU (Copper Futures ETF) or commodity copper index through price_only adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Copper rallies 4%+ in 3 days occur 1–2 times per month on cyclical swings and Fed commentary.

## Required Keys
- None
