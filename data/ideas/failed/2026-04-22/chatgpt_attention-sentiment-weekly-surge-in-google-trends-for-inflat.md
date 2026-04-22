# Attention Sentiment Weekly Surge In Google Trends For Inflation Hedge Searches Indicates Rising Macro Concern

**Idea ID:** `attention-sentiment-weekly-surge-in-google-trends-for-inflat`
**Family:** `attention_sentiment`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increasing search interest signals growing market concern about inflation, often leading to commodity sector rallies. Materials sector benefits from inflation hedge demand.

## Universe
- XLB

## Data Sources
- Google Trends weekly search interest for 'inflation hedge'

## Signal Logic
Enter long XLB if weekly 'inflation hedge' searches rise >20% above 6-week baseline

## Entry / Exit
Entry: Enter long XLB if weekly 'inflation hedge' searches rise >20% above 6-week baseline Exit: Exit after 5 weeks or if interest drops below 10% above baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'inflation hedge' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Inflation concern search interest fluctuates regularly with economic data and policy news.

## Required Keys
- None
