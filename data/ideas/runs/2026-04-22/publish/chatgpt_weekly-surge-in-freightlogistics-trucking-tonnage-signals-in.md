# Weekly Surge In Freightlogistics Trucking Tonnage Signals Industrial Demand Rebound

**Idea ID:** `weekly-surge-in-freightlogistics-trucking-tonnage-signals-in`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
An increase in trucking tonnage indicates rising industrial and consumer goods movement signaling economic strength. Industrial sector benefits from higher freight activity.

## Universe
- XLI

## Data Sources
- Freight trucking tonnage weekly data

## Signal Logic
Entry when weekly tonnage rises more than 10% versus prior 3-week average

## Entry / Exit
Entry: Entry when weekly tonnage rises more than 10% versus prior 3-week average Exit: Exit when tonnage drops below 5% increase or after 5 weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Freight trucking tonnage weekly data via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Trucking tonnage data shows regular weekly fluctuations tied to demand.

## Required Keys
- None
