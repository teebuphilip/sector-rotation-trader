# Weekly Unusual Jump In Earthquake Activity In Industrial Hubs

**Idea ID:** `weekly-unusual-jump-in-earthquake-activity-in-industrial-hub`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Unexpected increase in earthquake activity near industrial hubs may disrupt supply chains and production. Industrial sector vulnerable to physical disruptions in key manufacturing regions.

## Universe
- XLI

## Data Sources
- USGS weekly earthquake count near key industrial areas

## Signal Logic
Enter short XLI when weekly earthquake count near hubs exceeds 3x prior 4-week average

## Entry / Exit
Entry: Enter short XLI when weekly earthquake count near hubs exceeds 3x prior 4-week average Exit: Exit after 3 weeks or when activity returns to normal

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS weekly earthquake count near key industrial areas via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Earthquake activity clusters occur episodically, causing supply chain jitters.

## Required Keys
- None
