# Airline Seat Upgrade Price Surge

**Idea ID:** `airline-seat-upgrade-price-surge`
**Family:** `travel_mobility`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Rising seat upgrade and ancillary fees indicate strong airline pricing power and full cabins, signaling elevated leisure/business travel demand. Strong airline ancillary revenue signals robust discretionary spending and high travel demand; consumer sentiment on travel is bullish.

## Universe
- XLY

## Data Sources
- BTS average ancillary revenue per passenger (weekly via HTML table scrape from airline earnings data proxies)

## Signal Logic
If weekly average ancillary revenue per passenger rises >8% above 8-week moving average AND load factor >82%

## Entry / Exit
Entry: If weekly average ancillary revenue per passenger rises >8% above 8-week moving average AND load factor >82% Exit: After 12 trading days or when ancillary revenue retreats below entry level

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use BTS average ancillary revenue per passenger (weekly via HTML table scrape from airline earnings data proxies) via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seasonal travel peaks (spring break, summer, holidays) reliably push ancillary revenue spikes; high-frequency data ensures multiple triggers per quarter.

## Required Keys
- None
