# Small-cap Growth Momentum Rotation

**Idea ID:** `small-cap-growth-momentum-rotation`
**Family:** `attention_sentiment`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When IWM (small-cap) 5-day momentum outpaces QQQ (large-cap growth) by 2% or more, it signals a rotation into lower-liquidity names—often driven by retail attention shifts visible in option flow and social media chatter. Small-cap rotation favors consumer discretionary and beaten-down cyclical names.

## Universe
- XLY

## Data Sources
- Yahoo Finance daily prices for IWM (Russell 2000) and QQQ via price_only adapter

## Signal Logic
If IWM 5-day return minus QQQ 5-day return exceeds +2% AND IWM volume is 15%+ above 20-day average

## Entry / Exit
Entry: If IWM 5-day return minus QQQ 5-day return exceeds +2% AND IWM volume is 15%+ above 20-day average Exit: After 6 trading days or if relative momentum reverses (IWM underperforms by 1% or more)

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily prices for IWM (Russell 2000) and QQQ via price_only adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Small-cap momentum surges occur 2-3 times per month in typical market conditions.

## Required Keys
- None
