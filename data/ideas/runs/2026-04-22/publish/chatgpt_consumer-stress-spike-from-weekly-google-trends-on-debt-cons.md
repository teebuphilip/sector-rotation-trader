# Consumer Stress Spike From Weekly Google Trends On Debt Consolidation Searches

**Idea ID:** `consumer-stress-spike-from-weekly-google-trends-on-debt-cons`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A sudden rise in debt consolidation interest signals rising consumer financial stress, often preceding reduced discretionary spending. Consumer discretionary sector suffers when consumers increase debt management concerns.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest for 'debt consolidation'

## Signal Logic
Enter short XLY if weekly search interest rises more than 15% compared to prior 4-week average

## Entry / Exit
Entry: Enter short XLY if weekly search interest rises more than 15% compared to prior 4-week average Exit: Exit after 3 weeks or if interest falls below 10% above 4-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'debt consolidation' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Weekly Google Trends data often shows spikes in consumer stress terms several times a year.

## Required Keys
- None
