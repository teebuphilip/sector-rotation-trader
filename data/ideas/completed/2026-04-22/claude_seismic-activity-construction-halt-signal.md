# Seismic Activity Construction Halt Signal

**Idea ID:** `seismic-activity-construction-halt-signal`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Clusters of moderate earthquakes (M4.5+) in major construction zones halt projects, disrupt supply chains, and create insurance/liability spikes in affected regions. Building materials demand falls during seismic event construction halts; project delays inflate materials inventory and reduce near-term demand.

## Universe
- XLB

## Data Sources
- USGS earthquake activity (magnitude ≥4.5) by region through earthquake_activity adapter

## Signal Logic
When 2+ earthquakes M≥4.5 occur within same tectonic region within 48 hours

## Entry / Exit
Entry: When 2+ earthquakes M≥4.5 occur within same tectonic region within 48 hours Exit: After 7 trading days or when seismic activity subsides (<1 event per week in region)

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS earthquake activity (magnitude ≥4.5) by region through earthquake_activity adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Earthquake clusters are non-uniform but frequent; California/Japan/Chile produce 2–4 M4.5+ clusters per month on average.

## Required Keys
- None
