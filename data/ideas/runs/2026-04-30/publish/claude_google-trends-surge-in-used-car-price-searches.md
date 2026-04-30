# Google Trends Surge In Used Car Price Searches

**Idea ID:** `google-trends-surge-in-used-car-price-searches`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Spike in searches for used car pricing signals consumer anxiety about vehicle affordability and resale values, often preceding used car market weakness. Used car price stress ripples into auto retail, financing, and discretionary consumer spending on vehicles and related services.

## Universe
- XLY

## Data Sources
- Google Trends weekly search volume for 'used car prices' and 'car price drop' through google_trends adapter

## Signal Logic
If Google Trends search volume for 'used car prices' rises 40% week-over-week and stays above 60-week median

## Entry / Exit
Entry: If Google Trends search volume for 'used car prices' rises 40% week-over-week and stays above 60-week median Exit: After 8 trading days or if search volume normalizes to 50-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search volume for 'used car prices' and 'car price drop' through google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Consumer automotive searches spike monthly during rate hikes, supply shocks, and seasonal transitions; threshold is loose enough to trigger 3-4 times per quarter.

## Required Keys
- None
