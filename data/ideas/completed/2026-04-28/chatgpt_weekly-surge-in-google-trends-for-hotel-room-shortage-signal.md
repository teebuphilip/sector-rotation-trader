# Weekly Surge In Google Trends For Hotel Room Shortage Signals Travel Sector Tightness

**Idea ID:** `weekly-surge-in-google-trends-for-hotel-room-shortage-signal`
**Family:** `travel_mobility`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Search spikes for hotel room shortages indicate strong travel demand and pricing power for lodging. Consumer discretionary benefits from higher travel and lodging revenues.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest

## Signal Logic
Enter long XLY if weekly Google Trends for 'hotel room shortage' rises 25% week-over-week

## Entry / Exit
Entry: Enter long XLY if weekly Google Trends for 'hotel room shortage' rises 25% week-over-week Exit: Exit after 4 weeks or if interest drops by 15% week-over-week

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Hotel availability concerns surge seasonally with travel demand fluctuations.

## Required Keys
- None
