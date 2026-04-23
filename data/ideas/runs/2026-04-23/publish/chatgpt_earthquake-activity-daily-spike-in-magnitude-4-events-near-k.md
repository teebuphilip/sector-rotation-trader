# Earthquake Activity Daily Spike In Magnitude 4 Events Near Key Ports Signals Bearish Xli

**Idea ID:** `earthquake-activity-daily-spike-in-magnitude-4-events-near-k`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden increased earthquake activity near major port hubs disrupts logistics and industrial activity. Port disruptions reduce industrial throughput and supply chain efficiency.

## Universe
- XLI

## Data Sources
- USGS earthquake activity

## Signal Logic
Enter short XLI if daily count of magnitude 4+ earthquakes near ports doubles prior 7-day average

## Entry / Exit
Entry: Enter short XLI if daily count of magnitude 4+ earthquakes near ports doubles prior 7-day average Exit: Exit after 5 trading days or when counts return below 1.2x average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS earthquake activity via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seismic activity near ports regularly produces short-term spikes.

## Required Keys
- None
