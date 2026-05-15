# Stock Buyback Momentum Reversion Signal

**Idea ID:** `stock-buyback-momentum-reversion-signal`
**Family:** `attention_sentiment`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Multi-day surge in relative trading volume on mega-cap tech/growth stocks often coincides with corporate buyback windows; pullback signals mean reversion. Buyback-driven rallies are mechanical; when volume normalizes, momentum fades and reverses.

## Universe
- XLK

## Data Sources
- Yahoo Finance daily volume and price for XLK, XLY, XLC relative to SPY

## Signal Logic
If XLK or XLC volume exceeds 30-day median by 40% for 2 consecutive days AND price up >1%, short on day 3

## Entry / Exit
Entry: If XLK or XLC volume exceeds 30-day median by 40% for 2 consecutive days AND price up >1%, short on day 3 Exit: Exit after 5 trading days or if price rallies another 2%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily volume and price for XLK, XLY, XLC relative to SPY via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Corporate buyback windows occur quarterly; volume spikes happen 2–3 times per month during window periods.

## Required Keys
- None
