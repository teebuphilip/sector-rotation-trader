# Fred Unemployment Rate Surprise Downside

**Idea ID:** `fred-unemployment-rate-surprise-downside`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When actual unemployment releases beat consensus expectations by more than 0.2%, it signals stronger labor demand and consumer cash flow, driving discretionary spending optimism. Better-than-expected jobs data lowers recession fears and supports consumer confidence, directly benefiting discretionary retailers and services.

## Universe
- XLY

## Data Sources
- FRED series UNRATE (U.S. unemployment rate) weekly; compare to consensus forecast and prior month

## Signal Logic
If reported UNRATE is ≥0.2% lower than consensus forecast and prior month reading

## Entry / Exit
Entry: If reported UNRATE is ≥0.2% lower than consensus forecast and prior month reading Exit: Exit after 7 trading days or if next week's jobless claims spike above 5-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series UNRATE (U.S. unemployment rate) weekly; compare to consensus forecast and prior month via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Monthly employment reports provide weekly trigger windows; surprise beats happen 3–4 times per year.

## Required Keys
- None
