# Daily Spike In Google Trends For Hotel Cancellation Signals Travel Sector Stress

**Idea ID:** `daily-spike-in-google-trends-for-hotel-cancellation-signals-`
**Family:** `travel_mobility`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
An increase in hotel cancellation searches indicates travel disruptions and consumer hesitation, pressuring travel-related stocks. Travel and leisure companies suffer reduced bookings and revenue during cancellation surges.

## Universe
- XLY

## Data Sources
- Google Trends daily search interest

## Signal Logic
Enter short XLY when daily 'hotel cancellation' searches spike above 3 std deviations of 30-day mean

## Entry / Exit
Entry: Enter short XLY when daily 'hotel cancellation' searches spike above 3 std deviations of 30-day mean Exit: Exit after 5 days or once searches normalize below 1.5 std deviations

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Travel disruptions often cause sharp daily spikes in cancellation-related searches.

## Required Keys
- None
