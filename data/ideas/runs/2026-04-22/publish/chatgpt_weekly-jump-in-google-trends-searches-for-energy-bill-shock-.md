# Weekly Jump In Google Trends Searches For Energy Bill Shock Indicating Consumer Stress

**Idea ID:** `weekly-jump-in-google-trends-searches-for-energy-bill-shock-`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising search interest signals consumer anxiety over rising energy costs. Higher energy bills reduce consumer disposable income affecting staples.

## Universe
- XLP

## Data Sources
- Google Trends weekly search interest for 'energy bill shock'

## Signal Logic
If weekly search interest increases 25% over prior 2 weeks

## Entry / Exit
Entry: If weekly search interest increases 25% over prior 2 weeks Exit: After 4 weeks or if interest falls below 10% gain

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'energy bill shock' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Energy cost concerns are common and spike with seasonal price moves.

## Required Keys
- None
