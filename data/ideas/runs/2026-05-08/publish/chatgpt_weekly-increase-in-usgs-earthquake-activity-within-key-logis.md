# Weekly Increase In Usgs Earthquake Activity Within Key Logistics Hubs Signals Potential Freight Delays

**Idea ID:** `weekly-increase-in-usgs-earthquake-activity-within-key-logis`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising earthquake activity near major freight hubs can disrupt transport and supply chains temporarily. Supply chain disruption pressures industrial sector earnings.

## Universe
- XLI

## Data Sources
- USGS earthquake activity weekly counts

## Signal Logic
If weekly earthquake count in key logistics regions rises 50% above 4-week average

## Entry / Exit
Entry: If weekly earthquake count in key logistics regions rises 50% above 4-week average Exit: When earthquake activity falls below 20% above 4-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS earthquake activity weekly counts via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Seismic activity fluctuates and occasionally clusters in regions critical for logistics.

## Required Keys
- None
