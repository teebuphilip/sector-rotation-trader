# Ev Charger Network Expansion Sprint Demand Surge

**Idea ID:** `ev-charger-network-expansion-sprint-demand-surge`
**Family:** `travel_mobility`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
New EV charging stations added at >15% monthly growth rate after policy incentive announcements, driving bullish sentiment in EV and auto stocks. EV infrastructure expansion signals robust consumer adoption and OEM capex confidence.

## Universe
- XLY

## Data Sources
- OpenChargeMap daily charger counts by region via openchargemap adapter

## Signal Logic
If monthly charger count growth > 15% YoY and daily count increases 3 days in a row, long XLY

## Entry / Exit
Entry: If monthly charger count growth > 15% YoY and daily count increases 3 days in a row, long XLY Exit: Exit after 12 trading days or if growth rate falls below 8%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap daily charger counts by region via openchargemap adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Infrastructure build-outs are announced quarterly; monthly surges align with federal/state incentive rollouts, which occur multiple times per year.

## Required Keys
- None
