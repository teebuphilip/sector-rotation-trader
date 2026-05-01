# Price Momentum Reversion In Defensive Sectors After Tech Crash

**Idea ID:** `price-momentum-reversion-in-defensive-sectors-after-tech-cra`
**Family:** `attention_sentiment`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When XLK underperforms XLV by >4% over 5 consecutive trading days, it often signals fear-driven rotation into defensive healthcare; subsequent mean reversion favors tech outperformance. Extreme defensive rotations are often overdone; tech rebounds as rotation exhausts.

## Universe
- XLK

## Data Sources
- Yahoo Finance daily closing prices for XLK (tech) and XLV (healthcare) through price_only adapter, computing 5-day rolling returns

## Signal Logic
If 5-day cumulative return for XLK < XLV by >4%, long XLK relative to XLV

## Entry / Exit
Entry: If 5-day cumulative return for XLK < XLV by >4%, long XLK relative to XLV Exit: After 6 trading days or if relative performance reverses >2%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily closing prices for XLK (tech) and XLV (healthcare) through price_only adapter, computing 5-day rolling returns via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Daily volatility and sector rotation create 4%+ relative moves weekly; signal fires multiple times per month.

## Required Keys
- None
