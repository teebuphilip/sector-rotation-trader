# Weekly Surge In Localeconomyweirdness Spike In City Building Permits For Small Retail Kiosks

**Idea ID:** `weekly-surge-in-localeconomyweirdness-spike-in-city-building`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increased permits for small retail kiosks signal localized consumer spending shifts and potential retail expansion. Retail sector benefits from growth in small-scale retail development.

## Universe
- XLY

## Data Sources
- City building permit public tables for small retail kiosks

## Signal Logic
Entry when weekly permits increase by more than 20% compared to 4-week average

## Entry / Exit
Entry: Entry when weekly permits increase by more than 20% compared to 4-week average Exit: Exit after 5 weeks or if permits fall below 10% increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use City building permit public tables for small retail kiosks via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Building permit data is updated weekly with clear seasonal trends.

## Required Keys
- None
