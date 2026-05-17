# Weekly Rise In Earthquake Activity Near Major Manufacturing Hubs Signals Industrial Risk

**Idea ID:** `weekly-rise-in-earthquake-activity-near-major-manufacturing-`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A spike in seismic activity near key industrial clusters increases risk perception for manufacturing disruption. Industrial sector stocks are vulnerable to natural disaster-related production interruptions.

## Universe
- XLI

## Data Sources
- USGS weekly earthquake activity counts near major manufacturing regions

## Signal Logic
Enter short XLI if weekly earthquake count near hubs rises 50%+ WoW

## Entry / Exit
Entry: Enter short XLI if weekly earthquake count near hubs rises 50%+ WoW Exit: Exit after 2 weeks or when counts normalize

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS weekly earthquake activity counts near major manufacturing regions via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Seismic events cluster regionally and can spike repeatedly in short periods.

## Required Keys
- None
