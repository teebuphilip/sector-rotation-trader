# Unemployment Initial Claims Mean Reversion Pop

**Idea ID:** `unemployment-initial-claims-mean-reversion-pop`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When initial claims spike 20%+ above their 4-week moving average, they revert within 2-4 weeks; early reversions often precede a bullish labor repricing. Labor market normalization from shock spikes reduces recession fears and supports financial sector re-risking and credit demand.

## Universe
- XLF

## Data Sources
- FRED series ICSA (initial jobless claims weekly) through fred_series adapter

## Signal Logic
If ICSA exceeds 4-week MA by 20% or more, enter long on Thursday open

## Entry / Exit
Entry: If ICSA exceeds 4-week MA by 20% or more, enter long on Thursday open Exit: Exit after 14 trading days or if ICSA falls below 4-week MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series ICSA (initial jobless claims weekly) through fred_series adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Claims data is volatile; 20% spikes above MA occur 3-4 times per year and reverse predictably within 14-21 days.

## Required Keys
- None
