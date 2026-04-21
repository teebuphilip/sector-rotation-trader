# Materials Sector Weekly Volatility Contraction Breakout

**Idea ID:** `materials-sector-weekly-volatility-contraction-breakout`
**Family:** ``
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
When weekly realized volatility contracts below 50% of its 20-week average, a breakout in price often follows. Volatility compression usually precedes directional moves in materials stocks.

## Universe
- XLB

## Data Sources
- Yahoo Finance weekly realized volatility for XLB

## Signal Logic
Enter long XLB when weekly realized volatility <50% of 20-week average and price closes higher that week

## Entry / Exit
Entry: Enter long XLB when weekly realized volatility <50% of 20-week average and price closes higher that week Exit: Exit after 5 weeks or if price falls 4%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance weekly realized volatility for XLB via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Volatility contractions and subsequent breakouts occur regularly in materials markets.

## Required Keys
- None
