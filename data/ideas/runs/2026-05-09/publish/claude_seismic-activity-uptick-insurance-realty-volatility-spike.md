# Seismic Activity Uptick Insurance Realty Volatility Spike

**Idea ID:** `seismic-activity-uptick-insurance-realty-volatility-spike`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Clusters of seismic events in major metro regions (CA, WA, OK) trigger insurance claim anticipation and property revaluation concerns. Real estate and insurance stocks respond to perceived risk. Earthquake clusters depress property values and increase insurance costs; REIT valuations compress.

## Universe
- XLRE

## Data Sources
- USGS Earthquake Hazards Program API daily earthquake counts (magnitude 3.0+) by region through earthquake_activity adapter

## Signal Logic
If weekly count of magnitude 3.0+ earthquakes in CA+WA+OK exceeds 52-week 75th percentile (typical: 3+ events)

## Entry / Exit
Entry: If weekly count of magnitude 3.0+ earthquakes in CA+WA+OK exceeds 52-week 75th percentile (typical: 3+ events) Exit: After 10 trading days or if weekly earthquake count returns to median for 2 consecutive weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS Earthquake Hazards Program API daily earthquake counts (magnitude 3.0+) by region through earthquake_activity adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Seismic clusters occur unpredictably but reliably; threshold fires 1–2 times per quarter.

## Required Keys
- None
