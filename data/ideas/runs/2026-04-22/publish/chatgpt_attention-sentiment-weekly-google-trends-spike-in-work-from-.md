# Attention Sentiment Weekly Google Trends Spike In Work From Home Job Searches

**Idea ID:** `attention-sentiment-weekly-google-trends-spike-in-work-from-`
**Family:** `attention_sentiment`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising interest in WFH jobs signals labor market shift and potential tech sector volatility. Tech sector benefits from increased remote work trends and associated tech demand.

## Universe
- XLK

## Data Sources
- Google Trends weekly search interest for 'work from home jobs'

## Signal Logic
Enter long XLK if WFH job searches rise >15% WoW for 2 weeks

## Entry / Exit
Entry: Enter long XLK if WFH job searches rise >15% WoW for 2 weeks Exit: Exit after searches drop below 10% WoW increase or after 5 weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'work from home jobs' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: WFH job interest fluctuates frequently as labor market conditions evolve.

## Required Keys
- None
