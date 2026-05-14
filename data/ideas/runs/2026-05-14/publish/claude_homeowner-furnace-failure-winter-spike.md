# Homeowner Furnace Failure Winter Spike

**Idea ID:** `homeowner-furnace-failure-winter-spike`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Sharp seasonal spikes in furnace/heating repair searches occur during temperature drops, signaling consumer cash outflow stress and urgent home maintenance demand. Industrial/HVAC contractors and home services benefit from repair demand spike; signals consumer willingness to spend on essential maintenance.

## Universe
- XLI

## Data Sources
- Google Trends weekly search volume for 'furnace repair' and 'heating system maintenance'

## Signal Logic
If weekly Google Trends volume for 'furnace repair' rises >40% above 12-week moving average AND temperature drops below 40°F in major metro areas

## Entry / Exit
Entry: If weekly Google Trends volume for 'furnace repair' rises >40% above 12-week moving average AND temperature drops below 40°F in major metro areas Exit: After 14 calendar days or when search volume returns to baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search volume for 'furnace repair' and 'heating system maintenance' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Winter heating season (Nov–Mar) reliably produces furnace search spikes tied to temperature drops; fires multiple times per season.

## Required Keys
- None
