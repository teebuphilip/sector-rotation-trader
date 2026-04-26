# Small Package Delivery Rss Volume Surge

**Idea ID:** `small-package-delivery-rss-volume-surge`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Sustained RSS mention spikes for delivery delays signal capacity constraints, labor shortages, or seasonal volume compression in parcel logistics, pressuring shipping and retail margins. Delivery delays reduce consumer satisfaction, compress retail margins, and signal e-commerce logistics stress.

## Universe
- XLY

## Data Sources
- RSS feed count for 'UPS delivery delay', 'FedEx package delay', 'Amazon logistics slowdown' via rss_count adapter

## Signal Logic
If daily RSS count for delivery delay articles exceeds 15 for 3 consecutive days, short XLY

## Entry / Exit
Entry: If daily RSS count for delivery delay articles exceeds 15 for 3 consecutive days, short XLY Exit: After 4 weeks or if daily RSS count falls below 8 for 5 consecutive days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS feed count for 'UPS delivery delay', 'FedEx package delay', 'Amazon logistics slowdown' via rss_count adapter via scrape (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Holiday shopping, seasonal weather events, and labor staffing issues trigger delivery delay articles regularly; RSS spikes occur every few weeks during peak seasons.

## Required Keys
- None
