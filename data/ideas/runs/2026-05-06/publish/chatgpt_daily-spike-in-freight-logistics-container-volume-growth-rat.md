# Daily Spike In Freight Logistics Container Volume Growth Rate

**Idea ID:** `daily-spike-in-freight-logistics-container-volume-growth-rat`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden daily increases in container volume growth rate often precede industrial production ramp-ups and supply chain acceleration. Industrial sector stocks benefit from increased freight activity and supply chain momentum.

## Universe
- XLI

## Data Sources
- Port container volume daily updates

## Signal Logic
If daily container volume growth exceeds 3% compared to previous 3-day average

## Entry / Exit
Entry: If daily container volume growth exceeds 3% compared to previous 3-day average Exit: After 7 trading days or when growth falls below 1%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Port container volume daily updates via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Daily freight volume data often fluctuates with port activity and supply chain cycles.

## Required Keys
- None
