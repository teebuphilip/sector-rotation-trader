# Volatility Expansion Xlv Defensive Safe Haven Rotation

**Idea ID:** `volatility-expansion-xlv-defensive-safe-haven-rotation`
**Family:** `attention_sentiment`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
VIX spikes >30% from prior day close while XLV outperforms SPY by >1% same day, confirming flight-to-safety into healthcare. VIX spikes trigger defensive rotation; healthcare is low-beta hedge; outperformance is sticky for 5-10 days post-shock.

## Universe
- XLV

## Data Sources
- Yahoo Finance daily VIX and XLV (Healthcare ETF) price and returns via price_only adapter

## Signal Logic
If VIX rises >30% day-over-day AND XLV outperforms SPY by >1% same day

## Entry / Exit
Entry: If VIX rises >30% day-over-day AND XLV outperforms SPY by >1% same day Exit: After 7 trading days or when VIX falls below 20-day MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily VIX and XLV (Healthcare ETF) price and returns via price_only adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Market shocks occur monthly; 30% VIX spikes happen 8-12 times annually and reliably trigger defensive rotation for 1-2 weeks.

## Required Keys
- None
