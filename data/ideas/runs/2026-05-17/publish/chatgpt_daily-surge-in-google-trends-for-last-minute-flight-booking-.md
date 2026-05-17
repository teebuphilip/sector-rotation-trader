# Daily Surge In Google Trends For Last Minute Flight Booking Signals Travel Rebound

**Idea ID:** `daily-surge-in-google-trends-for-last-minute-flight-booking-`
**Family:** `travel_mobility`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
A sudden increase in last-minute flight searches indicates quick recovery or surge in travel demand. Consumer discretionary travel-related sectors benefit from higher booking activity.

## Universe
- XLY

## Data Sources
- Google Trends daily search interest for 'last minute flight booking'

## Signal Logic
Enter long XLY if daily Google Trends for 'last minute flight booking' increases 30%+ over 5-day moving average

## Entry / Exit
Entry: Enter long XLY if daily Google Trends for 'last minute flight booking' increases 30%+ over 5-day moving average Exit: Exit after 10 trading days or if trend drops below 15% increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest for 'last minute flight booking' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Travel demand fluctuates rapidly with events and holidays causing frequent search spikes.

## Required Keys
- None
