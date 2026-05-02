# Jobless Claims Shock Reversal Trade

**Idea ID:** `jobless-claims-shock-reversal-trade`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When initial jobless claims spike above 2-standard-deviations of the 8-week rolling mean, a mean-reversion bounce typically follows within 2-3 weeks as temporary layoffs resolve. Claims shock reversals signal labor market stabilization, boosting consumer discretionary spending confidence.

## Universe
- XLY

## Data Sources
- FRED series ICSA (initial jobless claims weekly)

## Signal Logic
When weekly initial claims exceed (8-week rolling mean + 2*stdev) AND prior week was not already elevated

## Entry / Exit
Entry: When weekly initial claims exceed (8-week rolling mean + 2*stdev) AND prior week was not already elevated Exit: After claims return to rolling mean or 12 trading days elapse

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series ICSA (initial jobless claims weekly) via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Weekly claims data is volatile; seasonal layoffs and temporary shocks occur 3-5 times per year, triggering mean-reversion signals.

## Required Keys
- None
