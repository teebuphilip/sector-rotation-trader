# Earthquake Swarm Insurance Demand Spike

**Idea ID:** `earthquake-swarm-insurance-demand-spike`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Clusters of seismic activity in populated areas trigger insurance claim inquiry spikes and reinforce re-insurance pricing pressure, shifting capital to insurers and risk management firms. Earthquake swarms increase insurance underwriting activity, loss reserve adjustments, and reinsurance demand.

## Universe
- XLF

## Data Sources
- USGS Earthquake Activity API daily magnitude 3.0+ events by region

## Signal Logic
When a region records 5+ magnitude 3.0+ earthquakes within 7 days

## Entry / Exit
Entry: When a region records 5+ magnitude 3.0+ earthquakes within 7 days Exit: After 8 trading days or when seismic activity drops to <2 events per week

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS Earthquake Activity API daily magnitude 3.0+ events by region via api (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seismic clusters occur regularly; US averages 1-2 significant swarms per month in active zones.

## Required Keys
- None
