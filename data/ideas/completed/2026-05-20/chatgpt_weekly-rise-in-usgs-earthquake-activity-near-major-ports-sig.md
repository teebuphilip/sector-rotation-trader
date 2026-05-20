# Weekly Rise In Usgs Earthquake Activity Near Major Ports Signals Potential Freight Disruptions

**Idea ID:** `weekly-rise-in-usgs-earthquake-activity-near-major-ports-sig`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increased seismic activity near key ports can disrupt freight logistics and shipping throughput. Logistics and industrial sectors are vulnerable to port shutdowns from earthquake damage.

## Universe
- XLI

## Data Sources
- USGS earthquake activity

## Signal Logic
If weekly earthquake counts within 100km of top 5 US ports increase by 50% WoW

## Entry / Exit
Entry: If weekly earthquake counts within 100km of top 5 US ports increase by 50% WoW Exit: After 2 weeks or when counts revert to baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS earthquake activity via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Seismic activity near ports fluctuates regularly enough to produce multiple signals annually.

## Required Keys
- None
