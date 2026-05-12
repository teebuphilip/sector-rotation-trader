# Weekly Spike In Freight Container Volumes At East Coast Ports Signals Industrial Sector Strength

**Idea ID:** `weekly-spike-in-freight-container-volumes-at-east-coast-port`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A sudden increase in container volumes indicates rising import/export activity feeding industrial production and supply chain demand. Industrial companies benefit from increased goods movement and supply chain activity.

## Universe
- XLI

## Data Sources
- Port container volume weekly data for East Coast major ports

## Signal Logic
Enter long XLI when weekly East Coast container volume rises 10%+ over 3-week moving average

## Entry / Exit
Entry: Enter long XLI when weekly East Coast container volume rises 10%+ over 3-week moving average Exit: Exit after 5 weeks or if volume drops below 3-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Port container volume weekly data for East Coast major ports via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Port volume data has weekly seasonality and frequent volume surges tied to shipping cycles.

## Required Keys
- None
