# News Sentiment Rotation Fade Trade

**Idea ID:** `news-sentiment-rotation-fade-trade`
**Family:** `attention_sentiment`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When combined recession + earnings miss mentions spike to 90th percentile, sentiment capitulation is near; market contrarian reversal opportunity follows within 3–5 days. Extreme negative sentiment clustering often marks washout phase; consumer discretionary rebounds as capitulation exhausts.

## Universe
- XLY

## Data Sources
- RSS feed (Bloomberg/Reuters/CNBC) daily article count mentioning 'recession' AND 'earnings miss' through rss_count adapter

## Signal Logic
When combined daily RSS count (recession + earnings miss) exceeds 85th percentile of 52-week rolling distribution

## Entry / Exit
Entry: When combined daily RSS count (recession + earnings miss) exceeds 85th percentile of 52-week rolling distribution Exit: After 4 trading days or when RSS count reverts to 50th percentile

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS feed (Bloomberg/Reuters/CNBC) daily article count mentioning 'recession' AND 'earnings miss' through rss_count adapter via scrape (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Earnings seasons and recession narratives cycle; 2–3 sentiment spikes per month during earnings windows and Fed announcement clusters.

## Required Keys
- None
