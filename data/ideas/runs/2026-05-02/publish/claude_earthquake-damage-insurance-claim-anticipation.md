# Earthquake Damage Insurance Claim Anticipation

**Idea ID:** `earthquake-damage-insurance-claim-anticipation`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Significant earthquake clusters (>3 events magnitude 4.0+ within 7 days in same region) trigger insurance loss recognition and reconstruction demand—benefiting financials and industrials. Immediate insurance claim spikes hurt financial sector valuations; property & casualty insurers face margin pressure.

## Universe
- XLF

## Data Sources
- USGS Earthquake Activity API (daily magnitude >4.0 events in insurable regions)

## Signal Logic
If 7-day rolling count of magnitude 4.0+ earthquakes in CA/OR/WA exceeds 3 events

## Entry / Exit
Entry: If 7-day rolling count of magnitude 4.0+ earthquakes in CA/OR/WA exceeds 3 events Exit: After 15 trading days or when seismic activity normalizes to <1 event per week

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS Earthquake Activity API (daily magnitude >4.0 events in insurable regions) via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Earthquake clusters occur regularly along US fault lines; 2-3 trading opportunities per quarter in seismically active states.

## Required Keys
- None
