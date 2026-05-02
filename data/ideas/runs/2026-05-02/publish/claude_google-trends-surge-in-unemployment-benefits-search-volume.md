# Google Trends Surge In Unemployment Benefits Search Volume

**Idea ID:** `google-trends-surge-in-unemployment-benefits-search-volume`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Sharp week-over-week spikes in unemployment benefits search volume (>40% increase) precede negative consumer sentiment and spending cuts, signaling economic stress. Consumer discretionary spending declines as households anticipate or experience job loss.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest for 'unemployment benefits' and 'how to apply for unemployment'

## Signal Logic
If weekly search volume index exceeds prior 4-week average by >40% AND prior week was not already elevated

## Entry / Exit
Entry: If weekly search volume index exceeds prior 4-week average by >40% AND prior week was not already elevated Exit: After 10 trading days or when search volume returns to 4-week baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'unemployment benefits' and 'how to apply for unemployment' via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Google Trends search spikes correlate with labor market weakness; seasonal layoffs and recession fears trigger 3-4 signals per year.

## Required Keys
- None
