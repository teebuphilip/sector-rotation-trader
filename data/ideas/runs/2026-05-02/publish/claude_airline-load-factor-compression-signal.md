# Airline Load Factor Compression Signal

**Idea ID:** `airline-load-factor-compression-signal`
**Family:** `travel_mobility`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When monthly load factor drops >2% from prior month, airlines cut capacity, reducing fuel demand and signaling travel demand weakness—bearish for airlines and energy. Lower airline load factors reduce jet fuel consumption and signal reduced consumer travel spending.

## Universe
- XLE

## Data Sources
- BTS Airline Load Factor monthly average (via html_table scrape)

## Signal Logic
If latest month's load factor is >2 percentage points below prior month AND below 12-month rolling average

## Entry / Exit
Entry: If latest month's load factor is >2 percentage points below prior month AND below 12-month rolling average Exit: After 15 trading days or when load factor recovers toward 12-month mean

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use BTS Airline Load Factor monthly average (via html_table scrape) via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Seasonal capacity adjustments occur quarterly; holiday travel shifts and recession fears trigger load factor compressions 3-4 times per year.

## Required Keys
- None
