# Weekly Surge In Freight Container Volume At Port Of Long Beach Signals Industrial Sector Strength

**Idea ID:** `weekly-surge-in-freight-container-volume-at-port-of-long-bea`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increasing container throughput reflects rising industrial production and goods movement. Higher freight activity correlates with stronger industrial sector fundamentals.

## Universe
- XLI

## Data Sources
- Port container volume data for Port of Long Beach

## Signal Logic
Enter long XLI if weekly container volume rises above 15% over prior 4-week average

## Entry / Exit
Entry: Enter long XLI if weekly container volume rises above 15% over prior 4-week average Exit: Exit after 4 weeks or if volume drops below 5% above baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Port container volume data for Port of Long Beach via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Port throughput fluctuates weekly with shipping cycles and trade demand.

## Required Keys
- None
