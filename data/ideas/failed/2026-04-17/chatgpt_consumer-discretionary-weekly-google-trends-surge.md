# Consumer Discretionary Weekly Google Trends Surge

**Idea ID:** `consumer-discretionary-weekly-google-trends-surge`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Sharp weekly upticks in shopping-related searches often precede increased consumer discretionary spending. Rising consumer interest in deals signals potential revenue growth for discretionary retailers.

## Universe
- XLY

## Data Sources
- Google Trends weekly data for 'shopping' and 'discount' keywords mapped to XLY

## Signal Logic
If weekly search interest for 'shopping' increases 15% week-over-week

## Entry / Exit
Entry: If weekly search interest for 'shopping' increases 15% week-over-week Exit: After 3 weeks or when search interest reverts below 5% increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly data for 'shopping' and 'discount' keywords mapped to XLY via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Consumer search trends fluctuate seasonally and can spike multiple times monthly.

## Required Keys
- None
