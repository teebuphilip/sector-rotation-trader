# Weekly Google Trends Surge In Pest Control Searches

**Idea ID:** `weekly-google-trends-surge-in-pest-control-searches`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Spikes in pest control searches correlate with seasonal property stress and localized economic downturn; homeowners prioritize pest mitigation when neighborhood conditions deteriorate or rental markets tighten. Rising pest control urgency signals deteriorating property conditions and neighborhood quality, pressuring real estate valuations and sentiment.

## Universe
- XLRE

## Data Sources
- Google Trends weekly search volume for 'pest control near me' and 'termite inspection' through google_trends adapter

## Signal Logic
When weekly Google Trends search volume for pest control queries rises 35% or more above the 8-week rolling average

## Entry / Exit
Entry: When weekly Google Trends search volume for pest control queries rises 35% or more above the 8-week rolling average Exit: After 10 trading days or when search volume falls back to within 15% of rolling average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search volume for 'pest control near me' and 'termite inspection' through google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seasonal pest activity and neighborhood stress cycles generate regular search spikes; threshold is tight enough to fire 2–4 times per quarter.

## Required Keys
- None
