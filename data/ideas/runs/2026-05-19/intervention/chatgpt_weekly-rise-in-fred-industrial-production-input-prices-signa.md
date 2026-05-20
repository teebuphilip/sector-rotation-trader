# Weekly Rise In Fred Industrial Production Input Prices Signals Rising Input Cost Pressure

**Idea ID:** `weekly-rise-in-fred-industrial-production-input-prices-signa`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increasing input prices for industry drive margin pressure and cost-push inflation concerns. Rising input costs compress industrial sector profitability.

## Universe
- XLI

## Data Sources
- FRED API series for industrial input prices

## Signal Logic
Enter short XLI when weekly input price index rises by more than 1% week-over-week

## Entry / Exit
Entry: Enter short XLI when weekly input price index rises by more than 1% week-over-week Exit: Exit after 3 weeks or when weekly growth drops below 0.3%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED API series for industrial input prices via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Input price indices update regularly with measurable week-over-week changes.

## Required Keys
- None
