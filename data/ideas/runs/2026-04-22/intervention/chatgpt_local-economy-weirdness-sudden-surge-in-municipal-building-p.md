# Local Economy Weirdness Sudden Surge In Municipal Building Permits Signals Real Estate Rebound

**Idea ID:** `local-economy-weirdness-sudden-surge-in-municipal-building-p`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A jump in building permits indicates increased construction activity, often leading to real estate sector strength. Real estate benefits from construction activity acceleration.

## Universe
- XLRE

## Data Sources
- FRED API: Building Permits (monthly)

## Signal Logic
Enter long XLRE if weekly rate of building permits rises by more than 20% compared to 4-week average

## Entry / Exit
Entry: Enter long XLRE if weekly rate of building permits rises by more than 20% compared to 4-week average Exit: Exit after 8 weeks or if permits decline below 10% above baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED API: Building Permits (monthly) via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Building permit data is regularly reported and reacts to seasonal and policy changes.

## Required Keys
- None
