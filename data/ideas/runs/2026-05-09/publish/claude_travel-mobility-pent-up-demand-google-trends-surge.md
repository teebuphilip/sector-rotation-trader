# Travel Mobility Pent-up Demand Google Trends Surge

**Idea ID:** `travel-mobility-pent-up-demand-google-trends-surge`
**Family:** `travel_mobility`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Sharp spikes in travel booking searches indicate sudden pent-up demand release, often following lockdowns, price drops, or seasonal transitions. Correlates with airline and hospitality stock strength. Travel and leisure are discretionary; search spikes signal consumer confidence and spending willingness.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest for 'vacation packages', 'flight deals', and 'hotel bookings' through google_trends adapter

## Signal Logic
If combined travel search index exceeds 65th percentile of 13-week rolling window

## Entry / Exit
Entry: If combined travel search index exceeds 65th percentile of 13-week rolling window Exit: After 12 trading days or if index falls to below 40th percentile for 2 consecutive weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'vacation packages', 'flight deals', and 'hotel bookings' through google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Travel searches spike seasonally (holidays, spring break, summer) and after price drops; threshold fires 2–3 times per month.

## Required Keys
- None
