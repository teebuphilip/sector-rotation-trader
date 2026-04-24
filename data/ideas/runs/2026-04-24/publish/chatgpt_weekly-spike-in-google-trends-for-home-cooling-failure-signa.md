# Weekly Spike In Google Trends For Home Cooling Failure Signals Bearish Xlu

**Idea ID:** `weekly-spike-in-google-trends-for-home-cooling-failure-signa`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Surges in searches about home cooling failures indicate stress on utilities and potential power supply issues. Electric utilities face operational pressure and potential outages when cooling systems fail broadly.

## Universe
- XLU

## Data Sources
- Google Trends weekly search interest

## Signal Logic
If weekly search volume for 'home cooling failure' rises 30% above 8-week average

## Entry / Exit
Entry: If weekly search volume for 'home cooling failure' rises 30% above 8-week average Exit: Exit after 4 weeks or when volume drops below 10% increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Cooling system issues spike in summer months and heat waves causing utility strain.

## Required Keys
- None
