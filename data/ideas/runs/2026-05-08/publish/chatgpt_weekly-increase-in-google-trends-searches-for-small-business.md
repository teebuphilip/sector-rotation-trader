# Weekly Increase In Google Trends Searches For Small Business Loan Default Signals Rising Credit Stress

**Idea ID:** `weekly-increase-in-google-trends-searches-for-small-business`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
More searches on loan defaults suggest financial stress among small businesses, possibly foreshadowing economic weakness. Rising defaults impact financial sector asset quality and credit availability.

## Universe
- XLF

## Data Sources
- Google Trends weekly search interest

## Signal Logic
If weekly searches increase at least 15% above prior 4-week average

## Entry / Exit
Entry: If weekly searches increase at least 15% above prior 4-week average Exit: When searches decline below 10% above prior 4-week average

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
- Why It Should Fire Soon: Credit stress indicators fluctuate with economic cycles and often rise sharply in downturns.

## Required Keys
- None
