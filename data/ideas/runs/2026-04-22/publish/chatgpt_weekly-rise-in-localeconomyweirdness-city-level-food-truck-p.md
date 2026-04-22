# Weekly Rise In Localeconomyweirdness City-level Food Truck Permit Applications Surge

**Idea ID:** `weekly-rise-in-localeconomyweirdness-city-level-food-truck-p`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A surge in food truck permits signals localized consumer spending shifts and potential retail disruption. Growth in alternative food service options may boost overall consumer discretionary sales.

## Universe
- XLY

## Data Sources
- City government food truck permit application public tables

## Signal Logic
Entry when weekly permit applications increase by 25% compared to 4-week average

## Entry / Exit
Entry: Entry when weekly permit applications increase by 25% compared to 4-week average Exit: Exit after 6 weeks or when permit applications revert below 10% increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use City government food truck permit application public tables via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Food truck permit data is updated regularly with notable weekly changes.

## Required Keys
- None
