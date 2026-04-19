# Real Estate Sector Weekly Google Trends Home Buying Surge

**Idea ID:** `real-estate-sector-weekly-google-trends-home-buying-surge`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Sharp rises in home-buying related searches often precede increased real estate market activity. Higher search interest signals potential rise in housing demand and prices.

## Universe
- XLRE

## Data Sources
- Google Trends weekly 'house for sale' and 'mortgage rates' search interest mapped to XLRE

## Signal Logic
If weekly combined search interest for 'house for sale' and 'mortgage rates' rises >15% week-over-week

## Entry / Exit
Entry: If weekly combined search interest for 'house for sale' and 'mortgage rates' rises >15% week-over-week Exit: After 4 weeks or interest normalizes

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly 'house for sale' and 'mortgage rates' search interest mapped to XLRE via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Homebuying interest fluctuates seasonally and can spike multiple times yearly.

## Required Keys
- None
