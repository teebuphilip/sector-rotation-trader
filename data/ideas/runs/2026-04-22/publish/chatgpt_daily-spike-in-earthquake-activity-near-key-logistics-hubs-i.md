# Daily Spike In Earthquake Activity Near Key Logistics Hubs Indicating Potential Disruption

**Idea ID:** `daily-spike-in-earthquake-activity-near-key-logistics-hubs-i`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Short-term surge in local earthquake activity may disrupt freight and logistics flows. Logistics disruptions harm industrial and transportation sectors.

## Universe
- XLI

## Data Sources
- USGS daily earthquake activity near major port hubs

## Signal Logic
If daily earthquake count near hub doubles 7-day average

## Entry / Exit
Entry: If daily earthquake count near hub doubles 7-day average Exit: After 5 trading days or activity returns to normal

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS daily earthquake activity near major port hubs via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Earthquake activity can cluster and cause temporary logistics shocks.

## Required Keys
- None
