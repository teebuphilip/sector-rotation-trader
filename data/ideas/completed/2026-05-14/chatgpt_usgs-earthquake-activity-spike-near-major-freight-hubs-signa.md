# Usgs Earthquake Activity Spike Near Major Freight Hubs Signals Temporary Freight Disruption

**Idea ID:** `usgs-earthquake-activity-spike-near-major-freight-hubs-signa`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
A sudden increase in earthquake tremors near major freight hubs can disrupt logistics and shipping routes, impacting industrial production. Freight disruptions impair industrial supply chains and manufacturing output, pressuring industrial stocks.

## Universe
- XLI

## Data Sources
- USGS earthquake activity

## Signal Logic
If number of earthquakes with magnitude >3.0 near top 5 US freight hubs increases by 50% over 3 days

## Entry / Exit
Entry: If number of earthquakes with magnitude >3.0 near top 5 US freight hubs increases by 50% over 3 days Exit: After 7 trading days or when earthquake activity normalizes to baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS earthquake activity via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Seismic activity near freight hubs occasionally clusters, creating short-term disruptions detectable in USGS data.

## Required Keys
- None
