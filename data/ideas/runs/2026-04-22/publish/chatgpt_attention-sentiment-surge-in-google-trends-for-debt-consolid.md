# Attention Sentiment Surge In Google Trends For Debt Consolidation Searches

**Idea ID:** `attention-sentiment-surge-in-google-trends-for-debt-consolid`
**Family:** `attention_sentiment`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Spike in debt consolidation interest signals rising consumer financial stress, bearish for discretionary spending. Higher consumer debt stress often reduces discretionary consumption and sector performance.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest for 'debt consolidation'

## Signal Logic
Enter short XLY if debt consolidation searches increase >20% WoW for 2 consecutive weeks

## Entry / Exit
Entry: Enter short XLY if debt consolidation searches increase >20% WoW for 2 consecutive weeks Exit: Exit after search interest normalizes below 10% WoW increase or after 6 weeks

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
- Trigger Sensitivity: high
- Why It Should Fire Soon: Debt-related search spikes appear repeatedly during consumer stress cycles.

## Required Keys
- None
