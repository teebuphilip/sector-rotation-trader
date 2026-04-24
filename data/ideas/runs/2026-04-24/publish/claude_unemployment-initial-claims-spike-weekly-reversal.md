# Unemployment Initial Claims Spike Weekly Reversal

**Idea ID:** `unemployment-initial-claims-spike-weekly-reversal`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Weekly initial jobless claims spike above 4-week moving average by >15%, then revert within 2 weeks as employers pause hiring freezes temporarily. Consumer discretionary outperforms when labor volatility subsides and hiring uncertainty clears.

## Universe
- XLY

## Data Sources
- FRED series ICSA (Initial Claims weekly) via fred_series adapter

## Signal Logic
If ICSA > (4-week MA × 1.15) and prior week was normal, enter long XLY

## Entry / Exit
Entry: If ICSA > (4-week MA × 1.15) and prior week was normal, enter long XLY Exit: Exit after 7 trading days or when ICSA falls back below 1.05× 4-week MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series ICSA (Initial Claims weekly) via fred_series adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Initial claims data is published weekly and spikes/reversions occur multiple times per quarter in response to seasonal adjustments and policy changes.

## Required Keys
- None
