# Earthquake Swarm Near Oil Refinery Cluster Signal

**Idea ID:** `earthquake-swarm-near-oil-refinery-cluster-signal`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When a cluster of 5+ small earthquakes (magnitude 3.0-4.5) occurs within 50 km of a major US refinery zone in a single week, it signals potential refinery operational stress or community concern; downstream energy prices rise and energy stocks underperform. Seismic activity near refineries creates operational risk perception and potential supply disruption fears.

## Universe
- XLE

## Data Sources
- USGS earthquake activity daily data via earthquake_activity adapter, filtered for Texas Gulf Coast and Southern California refinery zones

## Signal Logic
If 5+ earthquakes magnitude 3.0-4.5 occur within 50 km of major refinery cluster in a single week, AND XLE volume exceeds 20-day average by 25%

## Entry / Exit
Entry: If 5+ earthquakes magnitude 3.0-4.5 occur within 50 km of major refinery cluster in a single week, AND XLE volume exceeds 20-day average by 25% Exit: After 4 weeks or when earthquake activity returns to background rates (1-2 events per week in zone)

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS earthquake activity daily data via earthquake_activity adapter, filtered for Texas Gulf Coast and Southern California refinery zones via api (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Earthquake swarms near refinery zones occur 1-2 times per quarter; seismic activity is persistent and measurable.

## Required Keys
- None
