# Unemployment Claims Spike Jobless Fear Burst

**Idea ID:** `unemployment-claims-spike-jobless-fear-burst`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Week-over-week jump in jobless claims exceeding seasonal adjustment by 15% or more signals labor market stress and consumer anxiety. Jobless claims spikes correlate with consumer pullback on discretionary spending and equity de-risking.

## Universe
- XLY

## Data Sources
- FRED initial jobless claims (ICSA) daily/weekly release

## Signal Logic
If weekly jobless claims spike >15% above prior week and exceed 52-week median by 20%

## Entry / Exit
Entry: If weekly jobless claims spike >15% above prior week and exceed 52-week median by 20% Exit: Exit after 2 weeks or when claims revert to median

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED initial jobless claims (ICSA) daily/weekly release via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Jobless claims volatility is weekly and frequent; threshold fires 6–10 times per year during normal volatility.

## Required Keys
- None
