# Weekly Google Trends Surge In Hotel Booking Cancellations Signals Bearish Travel Sector

**Idea ID:** `weekly-google-trends-surge-in-hotel-booking-cancellations-si`
**Family:** `travel_mobility`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Spikes in cancellations searches reflect rising travel uncertainty and reduced demand. Reduced hotel bookings depress travel and leisure industry revenue.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest

## Signal Logic
Enter short XLY when weekly search volume for 'hotel booking cancellations' rises 40% above 12-week average

## Entry / Exit
Entry: Enter short XLY when weekly search volume for 'hotel booking cancellations' rises 40% above 12-week average Exit: Exit after 5 weeks or when volume falls below 12-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Travel disruptions cause recurring weekly spikes in cancellation interest.

## Required Keys
- None
