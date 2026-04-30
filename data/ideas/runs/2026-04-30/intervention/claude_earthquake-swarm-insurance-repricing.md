# Earthquake Swarm Insurance Repricing

**Idea ID:** `earthquake-swarm-insurance-repricing`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Cluster of 5+ magnitude 3.0+ earthquakes in a single week in a populated region triggers investor concern about insurable losses and re-insurance repricing. Seismic activity clusters raise loss reserve expectations and insurance premium pressure, impacting financial sector profitability.

## Universe
- XLF

## Data Sources
- USGS earthquake activity API for magnitude 3.0+ events by region through earthquake_activity adapter

## Signal Logic
If 5+ magnitude 3.0+ earthquakes occur within 7 days in California, Pacific Northwest, or Midwest, short XLF

## Entry / Exit
Entry: If 5+ magnitude 3.0+ earthquakes occur within 7 days in California, Pacific Northwest, or Midwest, short XLF Exit: After 6 trading days or once 7-day earthquake count drops below 2

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS earthquake activity API for magnitude 3.0+ events by region through earthquake_activity adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seismic swarms occur 8-12 times annually across active US zones; 5-event threshold fires at least once per quarter.

## Required Keys
- None
