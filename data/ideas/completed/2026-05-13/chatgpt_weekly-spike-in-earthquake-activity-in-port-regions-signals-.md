# Weekly Spike In Earthquake Activity In Port Regions Signals Potential Freight Logistics Disruption

**Idea ID:** `weekly-spike-in-earthquake-activity-in-port-regions-signals-`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increased seismic activity near major ports often precedes supply chain disruptions impacting freight logistics and industrial sectors. Port disruptions reduce throughput and increase costs for industrial companies.

## Universe
- XLI

## Data Sources
- USGS earthquake activity

## Signal Logic
If weekly USGS earthquake count near major ports rises 50% week-over-week

## Entry / Exit
Entry: If weekly USGS earthquake count near major ports rises 50% week-over-week Exit: After 3 weeks or when activity returns to baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS earthquake activity via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Seismic activity near ports fluctuates regularly with geological patterns.

## Required Keys
- None
