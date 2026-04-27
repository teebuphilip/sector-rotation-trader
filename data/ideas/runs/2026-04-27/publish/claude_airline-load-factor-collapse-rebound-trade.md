# Airline Load Factor Collapse Rebound Trade

**Idea ID:** `airline-load-factor-collapse-rebound-trade`
**Family:** `travel_mobility`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When airline load factors drop 3+ percentage points week-over-week (signaling demand shock), they historically bounce back 2+ points within 2 weeks as airlines cut capacity and demand stabilizes. Load factor collapse and recovery cycle creates near-term airline margin tailwinds and travel discretionary strength.

## Universe
- XLY

## Data Sources
- BTS airline load factor weekly data via html_table scrape

## Signal Logic
If weekly load factor drops 3+ pts vs prior week and is below 52-week median, long XLY.

## Entry / Exit
Entry: If weekly load factor drops 3+ pts vs prior week and is below 52-week median, long XLY. Exit: After 10 trading days or if load factor rises 2+ pts.

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use BTS airline load factor weekly data via html_table scrape via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Airline capacity and demand cycles produce load factor swings monthly; recovery bounces are reliable within 2-week windows.

## Required Keys
- None
