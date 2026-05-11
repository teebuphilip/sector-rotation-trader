# Luxury Discretionary Google Trends Collapse Signal

**Idea ID:** `luxury-discretionary-google-trends-collapse-signal`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When luxury goods search interest drops 40%+ below 12-week average, wealthy consumer demand is evaporating, signaling discretionary squeeze and consumer confidence fade. Luxury weakness is leading indicator of consumer stress; high-margin discretionary retailers face demand cliff.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest for 'luxury handbag prices' + 'designer watch sales' via google_trends adapter

## Signal Logic
If luxury search index falls to <60% of 12-week average

## Entry / Exit
Entry: If luxury search index falls to <60% of 12-week average Exit: After 8 trading days or if index rebounds to >75% of baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'luxury handbag prices' + 'designer watch sales' via google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Luxury search volatility is seasonal; downside spikes 2-3x yearly during economic slowdowns and credit tightening cycles.

## Required Keys
- None
