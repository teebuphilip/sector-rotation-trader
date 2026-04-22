# Unemployment Claim Anticipation Hedge

**Idea ID:** `unemployment-claim-anticipation-hedge`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When initial jobless claims spike above 2-week moving average by >10%, it signals near-term labor market stress and often precedes equity volatility. Claims spikes pressure financial sector credit quality and loan loss provisions; weakness in financial stocks often leads broader selloffs.

## Universe
- XLF

## Data Sources
- FRED series ICSA (Initial Claims, weekly) through fred_series adapter

## Signal Logic
When ICSA exceeds its 2-week SMA by ≥10% and closes above prior week's high

## Entry / Exit
Entry: When ICSA exceeds its 2-week SMA by ≥10% and closes above prior week's high Exit: After 5 trading days or when ICSA reverts below 1.05× 2-week SMA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series ICSA (Initial Claims, weekly) through fred_series adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Weekly claims data ensures signal recurrence; seasonal layoffs and economic cycles produce 2–3 spike events per month on average.

## Required Keys
- None
