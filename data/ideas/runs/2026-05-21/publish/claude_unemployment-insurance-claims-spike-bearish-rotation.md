# Unemployment Insurance Claims Spike Bearish Rotation

**Idea ID:** `unemployment-insurance-claims-spike-bearish-rotation`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Weekly jobless claims spike above 4-week moving average signals labor market deterioration, triggering defensive rotation out of cyclicals. Consumer discretionary is most sensitive to employment stress; claims spikes precede consumer pullback.

## Universe
- XLY

## Data Sources
- FRED series ICSA (Initial Claims) weekly via fred_series adapter

## Signal Logic
When ICSA exceeds its 4-week MA by >8% and closes above prior week

## Entry / Exit
Entry: When ICSA exceeds its 4-week MA by >8% and closes above prior week Exit: After 3 weeks or when ICSA falls below 4-week MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series ICSA (Initial Claims) weekly via fred_series adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Claims data is volatile and seasonal; threshold breaches occur 2-4 times per quarter on average.

## Required Keys
- None
