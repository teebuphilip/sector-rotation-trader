# Earthquake Swarm Activity Spike

**Idea ID:** `earthquake-swarm-activity-spike`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Elevated earthquake frequency in seismically active regions (CA, WA, OK) signals geological stress and triggers property insurance and structural repair demand surges. Earthquake swarms drive construction, engineering services, and property repair demand; signals short-term industrial/materials activity boost.

## Universe
- XLI

## Data Sources
- USGS earthquake activity feed (daily: count of magnitude 3.0+ earthquakes per week by region)

## Signal Logic
If weekly 3.0+ magnitude earthquake count in CA/WA/OK exceeds 8-week moving average by >150%

## Entry / Exit
Entry: If weekly 3.0+ magnitude earthquake count in CA/WA/OK exceeds 8-week moving average by >150% Exit: After 20 trading days or when weekly count returns to baseline moving average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS earthquake activity feed (daily: count of magnitude 3.0+ earthquakes per week by region) via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seismic activity clusters occur regularly in fault zones; swarms lasting 2–4 weeks are common and trigger repair demand within days.

## Required Keys
- None
