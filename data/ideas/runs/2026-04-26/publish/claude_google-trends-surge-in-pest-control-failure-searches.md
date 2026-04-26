# Google Trends Surge In Pest Control Failure Searches

**Idea ID:** `google-trends-surge-in-pest-control-failure-searches`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Spikes in pest control search interest signal housing stock deterioration, seasonal humidity/warmth events, or urban sanitation breakdown—all leading indicators of local property stress and rental market weakness. Pest control search surges correlate with deferred maintenance, rental unit degradation, and downward property value pressure.

## Universe
- XLRE

## Data Sources
- Google Trends weekly interest for 'cockroach infestation', 'bed bug removal', 'rat exterminator' in major metros via google_trends adapter

## Signal Logic
If weekly search index for any major metro exceeds 150% of 52-week median, short XLRE

## Entry / Exit
Entry: If weekly search index for any major metro exceeds 150% of 52-week median, short XLRE Exit: After 4 weeks or if search index falls back below 110% of median

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly interest for 'cockroach infestation', 'bed bug removal', 'rat exterminator' in major metros via google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seasonal temperature swings and humidity cycles trigger pest searches monthly; urban deterioration and seasonal transitions ensure regular threshold breaches.

## Required Keys
- None
