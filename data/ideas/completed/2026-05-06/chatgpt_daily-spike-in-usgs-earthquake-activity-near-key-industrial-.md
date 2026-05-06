# Daily Spike In Usgs Earthquake Activity Near Key Industrial Hubs

**Idea ID:** `daily-spike-in-usgs-earthquake-activity-near-key-industrial-`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
A sudden rise in earthquake activity near industrial hubs can disrupt supply chains and production temporarily. Industrial sector faces operational disruptions and cost overruns from natural events.

## Universe
- XLI

## Data Sources
- USGS earthquake activity daily reports

## Signal Logic
If daily earthquake count near industrial hubs rises by 50% vs 7-day average

## Entry / Exit
Entry: If daily earthquake count near industrial hubs rises by 50% vs 7-day average Exit: After 5 trading days or when activity normalizes

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS earthquake activity daily reports via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Earthquake activity is constant and occasionally clusters near key areas impacting industry.

## Required Keys
- None
