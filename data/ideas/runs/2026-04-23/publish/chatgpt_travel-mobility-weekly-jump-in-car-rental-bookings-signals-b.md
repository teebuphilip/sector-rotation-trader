# Travel Mobility Weekly Jump In Car Rental Bookings Signals Bullish Xly

**Idea ID:** `travel-mobility-weekly-jump-in-car-rental-bookings-signals-b`
**Family:** `travel_mobility`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising car rental bookings precede increased travel and discretionary spending, driving XLY gains. Travel-related consumption growth boosts consumer discretionary stocks.

## Universe
- XLY

## Data Sources
- Car rental company weekly booking data

## Signal Logic
Enter long XLY when weekly bookings increase 15%+ over prior 3 weeks

## Entry / Exit
Entry: Enter long XLY when weekly bookings increase 15%+ over prior 3 weeks Exit: Exit after 4 weeks or when bookings drop below 5% increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Car rental company weekly booking data via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Weekly travel data often experiences spikes around holidays and seasonal travel.

## Required Keys
- None
