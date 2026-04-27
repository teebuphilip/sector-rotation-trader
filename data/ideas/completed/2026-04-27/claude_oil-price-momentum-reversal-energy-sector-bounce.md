# Oil Price Momentum Reversal Energy Sector Bounce

**Idea ID:** `oil-price-momentum-reversal-energy-sector-bounce`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When crude oil closes down 3+ days straight but bounces 2%+ on the 4th day and XLE lags, mean reversion pressure builds; XLE outperforms over next 5 days. Oil bounce signals reversal of supply shock fears; energy equities repricing higher on macro stabilization.

## Universe
- XLE

## Data Sources
- Yahoo Finance crude oil (CL=F) and XLE daily prices via price_only adapter

## Signal Logic
If crude down 3+ consecutive days, then up 2%+ next day, go long XLE.

## Entry / Exit
Entry: If crude down 3+ consecutive days, then up 2%+ next day, go long XLE. Exit: After 5 trading days or if crude falls 1.5%+.

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance crude oil (CL=F) and XLE daily prices via price_only adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Oil intraday and multi-day swings are frequent; 3-day losing streaks followed by bounces occur multiple times per month.

## Required Keys
- None
