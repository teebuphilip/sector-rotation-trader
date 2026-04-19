# Xlc Weekly Google Trends Surge In 5g Rollout

**Idea ID:** `xlc-weekly-google-trends-surge-in-5g-rollout`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising interest in 5G deployment correlates with communication sector ETF strength. Increased tech infrastructure interest boosts communication services stocks.

## Universe
- XLC

## Data Sources
- Google Trends weekly data for '5G rollout' search term

## Signal Logic
Enter long if weekly search interest in '5G rollout' increases by 25%+ vs prior week

## Entry / Exit
Entry: Enter long if weekly search interest in '5G rollout' increases by 25%+ vs prior week Exit: Exit after 4 weeks or if search interest declines 2 weeks consecutively

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly data for '5G rollout' search term via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: 5G related search interest fluctuates regularly as new rollouts happen.

## Required Keys
- None
