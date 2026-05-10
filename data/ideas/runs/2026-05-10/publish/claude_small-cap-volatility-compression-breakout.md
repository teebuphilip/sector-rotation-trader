# Small Cap Volatility Compression Breakout

**Idea ID:** `small-cap-volatility-compression-breakout`
**Family:** `attention_sentiment`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When IWM 30-day realized volatility falls below 12% while IWM lags SPY by >2% cumulatively over 15 days, subsequent mean reversion often triggers sharp small-cap rallies. Small-cap outperformance correlates with risk-on rotation and consumer discretionary strength.

## Universe
- XLY

## Data Sources
- Yahoo Finance daily price data for IWM (Russell 2000) and SPY, 30-day realized volatility, price_only adapter

## Signal Logic
If IWM 30-day realized vol <12% AND IWM underperforms SPY by >2% over prior 15 days AND IWM closes above 5-day MA, enter long

## Entry / Exit
Entry: If IWM 30-day realized vol <12% AND IWM underperforms SPY by >2% over prior 15 days AND IWM closes above 5-day MA, enter long Exit: Exit after 8 trading days or once IWM outperforms SPY by >1.5% over 3 days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily price data for IWM (Russell 2000) and SPY, 30-day realized volatility, price_only adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Small-cap volatility compression + underperformance occurs 3–4 times per quarter, especially after Fed pauses or risk sentiment shifts.

## Required Keys
- None
