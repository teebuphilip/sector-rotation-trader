# Airline Fuel Surcharge Announcement Spike

**Idea ID:** `airline-fuel-surcharge-announcement-spike`
**Family:** `travel_mobility`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Spikes in airline surcharge announcements signal crude oil pressure and margin compression in carriers, triggering flight capacity cuts and reduced travel demand—bearish for discretionary travel and hospitality. Fuel surcharge announcements signal rising operational costs, capacity constraint, and reduced pricing power—reducing leisure travel demand.

## Universe
- XLY

## Data Sources
- RSS feed count for 'airline fuel surcharge', 'airline ticket price increase fuel', 'carrier surcharge announcement' via rss_count adapter

## Signal Logic
If daily RSS count for surcharge announcements exceeds 8 for 2 consecutive days, short XLY

## Entry / Exit
Entry: If daily RSS count for surcharge announcements exceeds 8 for 2 consecutive days, short XLY Exit: After 2 weeks or if daily count falls below 4 for 7 consecutive days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS feed count for 'airline fuel surcharge', 'airline ticket price increase fuel', 'carrier surcharge announcement' via rss_count adapter via scrape (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Oil price volatility and quarterly fare review cycles trigger surcharge announcement waves multiple times per year; seasonal travel demand spikes force pricing announcement clusters.

## Required Keys
- None
