# Weekly Acceleration In Google Trends For Flight Delay Searches

**Idea ID:** `weekly-acceleration-in-google-trends-for-flight-delay-search`
**Family:** `travel_mobility`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising flight delay searches signal travel disruptions that may pressure airline and travel-related stocks. Consumer discretionary travel exposure suffers from mobility disruptions and consumer frustration.

## Universe
- XLY

## Data Sources
- Google Trends weekly data for 'flight delay' keyword

## Signal Logic
Enter short XLY when weekly flight delay search interest rises >15% WoW

## Entry / Exit
Entry: Enter short XLY when weekly flight delay search interest rises >15% WoW Exit: Exit after 3 weeks or when search interest declines below 5% WoW

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly data for 'flight delay' keyword via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Flight delay searches spike regularly around holiday seasons and weather events.

## Required Keys
- None
