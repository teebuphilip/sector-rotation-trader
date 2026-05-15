# Earthquake Swarm Construction Material Demand Surge

**Idea ID:** `earthquake-swarm-construction-material-demand-surge`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Multi-day earthquake swarms (>5 events in 48 hrs, magnitude 3.5+) in urban areas signal impending rebuilding demand and construction/materials activity. Post-earthquake reconstruction drives cement, steel, and materials demand.

## Universe
- XLB

## Data Sources
- USGS earthquake activity API for daily counts and magnitude by region

## Signal Logic
If daily earthquake count in a metro region >5 in 48 hours with avg magnitude >3.5

## Entry / Exit
Entry: If daily earthquake count in a metro region >5 in 48 hours with avg magnitude >3.5 Exit: Exit 10 trading days later or if swarm subsides for 5+ days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS earthquake activity API for daily counts and magnitude by region via api (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Seismic swarms occur 2–4 times per month globally; US-based swarms fire 1–2 times per month.

## Required Keys
- None
