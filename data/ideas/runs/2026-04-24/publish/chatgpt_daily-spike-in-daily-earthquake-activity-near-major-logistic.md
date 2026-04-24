# Daily Spike In Daily Earthquake Activity Near Major Logistics Hubs Signals Bearish Xli

**Idea ID:** `daily-spike-in-daily-earthquake-activity-near-major-logistic`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden increases in seismic activity near logistics hubs can disrupt supply chains and industrial operations. Increased earthquake activity threatens industrial infrastructure causing operational uncertainty.

## Universe
- XLI

## Data Sources
- USGS earthquake activity

## Signal Logic
If daily earthquake event count near major hubs rises 2x above 30-day average

## Entry / Exit
Entry: If daily earthquake event count near major hubs rises 2x above 30-day average Exit: Exit after 5 trading days or when daily count returns below 1.2x average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS earthquake activity via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Seismic clusters near hubs occasionally spike, causing temporary operational concerns.

## Required Keys
- None
