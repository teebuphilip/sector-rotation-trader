# Heartland Harvest

**Idea ID:** `heartland-harvest`
**Source:** anthropic / claude-3-haiku-20240307
**Frequency:** weekly

## Thesis
Crop progress data can signal shifting sentiment around agricultural commodity prices and farm-related stocks. Agriculture is a key materials/industrials sector input.

## Universe
- XLB

## Data Sources
- USDA weekly crop progress reports through html_table adapter

## Signal Logic
If current week's crop progress is more than 5% ahead of the 5-year average

## Entry / Exit
Entry: If current week's crop progress is more than 5% ahead of the 5-year average Exit: After 2 trading weeks or once crop progress falls back to the 5-year average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USDA weekly crop progress reports through html_table adapter via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Crop progress reports are a regular weekly release, and deviations from historical norms often occur seasonally.

## Required Keys
- None
