# Fred Unemployment Insurance Claims Weekly Print Beats Expectations Triggers Defensive Rotation

**Idea ID:** `fred-unemployment-insurance-claims-weekly-print-beats-expect`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When weekly initial jobless claims exceed consensus forecast by >5% (using 4-week smoothed trend), markets reprices labor risk; defensive sectors outperform 3-5 days. Claims beats signal economic softening and consumer income pressure; discretionary spending faces headwinds.

## Universe
- XLY

## Data Sources
- FRED series ICSA (Initial Claims) weekly through fred_series adapter

## Signal Logic
When weekly ICSA print >5% above 8-week moving average and >110% of prior year same week

## Entry / Exit
Entry: When weekly ICSA print >5% above 8-week moving average and >110% of prior year same week Exit: When ICSA normalizes back within 2% of 8-week average or after 10 trading days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series ICSA (Initial Claims) weekly through fred_series adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Labor market volatility produces claims surprises multiple times per quarter; seasonal patterns are well-established.

## Required Keys
- None
