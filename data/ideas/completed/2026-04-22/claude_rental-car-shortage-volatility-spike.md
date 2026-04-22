# Rental Car Shortage Volatility Spike

**Idea ID:** `rental-car-shortage-volatility-spike`
**Family:** `travel_mobility`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Spikes in rental car availability/pricing searches correlate with tight vehicle supply, rising leisure travel demand, or fleet disruptions—both inflationary and demand signals. High rental car search volume suggests strong leisure travel demand; signals consumer confidence and discretionary spending willingness.

## Universe
- XLY

## Data Sources
- Google Trends weekly search volume for 'rental car prices' and 'car rental shortage' through google_trends adapter

## Signal Logic
When 'rental car prices' OR 'car rental shortage' search volume exceeds 70th percentile of 26-week rolling baseline

## Entry / Exit
Entry: When 'rental car prices' OR 'car rental shortage' search volume exceeds 70th percentile of 26-week rolling baseline Exit: After 7 trading days or when search volume normalizes below 55th percentile

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search volume for 'rental car prices' and 'car rental shortage' through google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seasonal travel demand, holiday planning, and summer leisure travel create recurring rental car search spikes every 3–4 weeks.

## Required Keys
- None
