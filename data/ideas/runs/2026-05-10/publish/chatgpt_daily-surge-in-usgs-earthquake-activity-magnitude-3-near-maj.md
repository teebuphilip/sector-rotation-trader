# Daily Surge In Usgs Earthquake Activity Magnitude 3 Near Major Ports Signals Freight Logistics Disruption Risk

**Idea ID:** `daily-surge-in-usgs-earthquake-activity-magnitude-3-near-maj`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Increased seismic activity near ports can disrupt freight logistics flows, impacting industrial supply chains. Port disruptions cause delays and cost increases for industrial companies.

## Universe
- XLI

## Data Sources
- USGS earthquake daily activity near ports via earthquake_activity adapter

## Signal Logic
If daily count of earthquakes magnitude >3 near major ports exceeds 2

## Entry / Exit
Entry: If daily count of earthquakes magnitude >3 near major ports exceeds 2 Exit: Once count returns to zero

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS earthquake daily activity near ports via earthquake_activity adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Seismic events near ports occur irregularly but often enough to generate recent signals.

## Required Keys
- None
