# Weekly Surge In Google Trends Searches For Truck Driver Strike Signals Imminent Logistics Disruption

**Idea ID:** `weekly-surge-in-google-trends-searches-for-truck-driver-stri`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increased interest in truck driver strikes often precedes actual labor actions disrupting freight transport. Labor disputes in trucking raise costs and delay supply chains in industrial sectors.

## Universe
- XLI

## Data Sources
- Google Trends weekly search interest

## Signal Logic
If weekly searches for 'truck driver strike' rise 20% above 4-week average

## Entry / Exit
Entry: If weekly searches for 'truck driver strike' rise 20% above 4-week average Exit: When searches decline below 10% above 4-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Labor unrest topics frequently trend weekly before actual strikes or contract negotiations.

## Required Keys
- None
