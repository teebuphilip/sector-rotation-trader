# Industrial Sector Weekly Container Port Volume Drop

**Idea ID:** `industrial-sector-weekly-container-port-volume-drop`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Significant weekly declines in container throughput correlate with short-term industrial stock weakness. Lower port volumes indicate supply chain slowdowns affecting industrial output.

## Universe
- XLI

## Data Sources
- Port container volume weekly data from major US ports mapped to XLI

## Signal Logic
If weekly container volume drops >10% week-over-week

## Entry / Exit
Entry: If weekly container volume drops >10% week-over-week Exit: After 3 weeks or 5% price recovery

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Port container volume weekly data from major US ports mapped to XLI via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Port volume fluctuates with economic cycles and shipping disruptions.

## Required Keys
- None
