# Ev Charger Network Density Jump

**Idea ID:** `ev-charger-network-density-jump`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Rapid expansion in public EV charger installations signals infrastructure investment and regional EV adoption acceleration, boosting tech and utilities stocks. EV charger expansion drives software/IoT infrastructure demand and signals strong regional clean energy investment; bullish for tech providers.

## Universe
- XLK

## Data Sources
- OpenChargeMap EV charger count by state/region (weekly scrape of public API data)

## Signal Logic
If weekly EV charger count rises >20% above 12-week moving average in a region with >500 existing chargers

## Entry / Exit
Entry: If weekly EV charger count rises >20% above 12-week moving average in a region with >500 existing chargers Exit: After 16 trading days or when monthly addition rate returns to baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap EV charger count by state/region (weekly scrape of public API data) via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Government EV subsidies and corporate commitments drive quarterly charger deployment waves; infrastructure grants create regular spike cycles.

## Required Keys
- None
