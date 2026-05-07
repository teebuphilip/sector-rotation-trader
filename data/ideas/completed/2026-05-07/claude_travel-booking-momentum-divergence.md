# Travel Booking Momentum Divergence

**Idea ID:** `travel-booking-momentum-divergence`
**Family:** `travel_mobility`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When last-minute travel search interest exceeds early-booking interest by >20%, it signals price-sensitive consumer behavior and margin compression in hospitality and airlines. Last-minute booking spikes indicate weak demand visibility and pricing power erosion in leisure and hospitality.

## Universe
- XLY

## Data Sources
- Google Trends weekly search volume for 'last minute hotel deals' and 'flight price alerts'

## Signal Logic
When last-minute travel searches exceed advance-booking searches by 20% over 2-week window

## Entry / Exit
Entry: When last-minute travel searches exceed advance-booking searches by 20% over 2-week window Exit: After 8 trading days or when booking pattern normalizes

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search volume for 'last minute hotel deals' and 'flight price alerts' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Travel search seasonality creates regular booking pattern divergences; occurs 2-3 times per month.

## Required Keys
- None
