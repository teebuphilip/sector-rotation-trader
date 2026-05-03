# Earthquake Aftershock Insurance Claims Spike

**Idea ID:** `earthquake-aftershock-insurance-claims-spike`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Clusters of moderate earthquakes in populated regions trigger immediate insurance claim filings and property damage estimates, creating short-term sector rotation into insurance and repair stocks. Insurance and reinsurance companies see claim volume spikes; financial sector benefits from short-term repricing of risk premiums.

## Universe
- XLF

## Data Sources
- USGS earthquake API daily magnitude 4.0+ events by region with historical comparison

## Signal Logic
If 3+ magnitude 4.0+ earthquakes occur within 7 days in same region (e.g., California, Pacific Northwest)

## Entry / Exit
Entry: If 3+ magnitude 4.0+ earthquakes occur within 7 days in same region (e.g., California, Pacific Northwest) Exit: Exit after 8 trading days or if no additional earthquakes occur in next 5 days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS earthquake API daily magnitude 4.0+ events by region with historical comparison via api (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seismic activity is unpredictable but frequent enough that multi-event clusters occur several times per year in active zones.

## Required Keys
- None
