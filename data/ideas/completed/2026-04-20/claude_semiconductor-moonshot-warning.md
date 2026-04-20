# Semiconductor Moonshot Warning

**Idea ID:** `semiconductor-moonshot-warning`
**Source:** anthropic / claude-3-haiku-20240307
**Frequency:** daily

## Thesis
Semiconductors often experience large daily price jumps, which can signal speculative froth and increased risk of a pullback. Semiconductors are a high-beta technology sector that leads the market up and down.

## Universe
- XLK

## Data Sources
- Yahoo Finance daily prices for SOXX and SPY through price_only adapter

## Signal Logic
If SOXX closes up more than 4% for the day

## Entry / Exit
Entry: If SOXX closes up more than 4% for the day Exit: After 3 trading days or once SOXX underperforms SPY by 2%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily prices for SOXX and SPY through price_only adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Semiconductor stocks often exhibit volatile intraday price swings, especially on high-profile earnings or news.

## Required Keys
- None
