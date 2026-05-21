# Hotel Occupancy Rate Collapse Travel Demand Crash

**Idea ID:** `hotel-occupancy-rate-collapse-travel-demand-crash`
**Family:** `travel_mobility`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Hotel occupancy falls >8% week-over-week or drops below seasonal baseline, signaling consumer travel pullback. Hotel weakness signals discretionary spending collapse and reduced leisure travel; multiplier effect on restaurants, casinos, airlines.

## Universe
- XLY

## Data Sources
- FRED series HOUST (Total Housing Starts) as proxy for hospitality construction; supplemented by weekly hotel occupancy RSS feeds via html_table adapter

## Signal Logic
If hotel occupancy or booking pace falls >8% from prior week or falls 10% below 52-week average

## Entry / Exit
Entry: If hotel occupancy or booking pace falls >8% from prior week or falls 10% below 52-week average Exit: After 10 trading days or on rebound >5% from entry

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series HOUST (Total Housing Starts) as proxy for hospitality construction; supplemented by weekly hotel occupancy RSS feeds via html_table adapter via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seasonal and event-driven volatility in travel demand triggers 3-4 material downside moves per quarter.

## Required Keys
- None
