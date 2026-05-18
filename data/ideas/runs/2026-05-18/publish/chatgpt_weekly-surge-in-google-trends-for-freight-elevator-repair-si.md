# Weekly Surge In Google Trends For Freight Elevator Repair Signals Industrial Sector Demand

**Idea ID:** `weekly-surge-in-google-trends-for-freight-elevator-repair-si`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A sudden increase in freight elevator repair searches suggests rising industrial facility maintenance needs, often preceding increased industrial activity. Industrial sector benefits from increased infrastructure upkeep and industrial facility utilization.

## Universe
- XLI

## Data Sources
- Google Trends weekly search interest for 'freight elevator repair'

## Signal Logic
If weekly Google Trends for 'freight elevator repair' rises by more than 20% compared to prior 4-week average

## Entry / Exit
Entry: If weekly Google Trends for 'freight elevator repair' rises by more than 20% compared to prior 4-week average Exit: Exit after 3 weeks or when trend falls below 10% increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'freight elevator repair' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Maintenance issues in industrial infrastructure spike multiple times annually due to seasonal wear.

## Required Keys
- None
