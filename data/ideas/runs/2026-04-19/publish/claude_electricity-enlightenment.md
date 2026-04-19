# Electricity Enlightenment

**Idea ID:** `electricity-enlightenment`
**Source:** anthropic / claude-3-haiku-20240307
**Frequency:** weekly

## Thesis
Shifts in national electricity demand can signal changes in underlying economic activity and industrial production. Electricity demand is a key indicator for industrials and utilities.

## Universe
- XLI

## Data Sources
- EIA weekly electricity demand data through eia_electricity adapter

## Signal Logic
If weekly electricity demand increases more than 2% above the prior 4-week average

## Entry / Exit
Entry: If weekly electricity demand increases more than 2% above the prior 4-week average Exit: After 2 trading weeks or once demand falls back to the prior 4-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use EIA weekly electricity demand data through eia_electricity adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Electricity demand exhibits regular seasonal patterns, and deviations from typical ranges often occur.

## Required Keys
- None
