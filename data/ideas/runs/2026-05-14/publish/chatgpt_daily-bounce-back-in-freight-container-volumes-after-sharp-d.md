# Daily Bounce Back In Freight Container Volumes After Sharp Decline Signals Industrial Sector Recovery

**Idea ID:** `daily-bounce-back-in-freight-container-volumes-after-sharp-d`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
A rapid recovery in container volumes after a sudden drop signals resumption of supply chains and industrial activity. Improving freight flows indicate better industrial production and economic activity.

## Universe
- XLI

## Data Sources
- port_container_volume daily volumes

## Signal Logic
If daily container volume rises by more than 3% after a 5% drop over prior 3 days

## Entry / Exit
Entry: If daily container volume rises by more than 3% after a 5% drop over prior 3 days Exit: After 7 trading days or if volume falls below prior 7-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use port_container_volume daily volumes via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Container volume rebounds occur frequently after short disruptions.

## Required Keys
- None
