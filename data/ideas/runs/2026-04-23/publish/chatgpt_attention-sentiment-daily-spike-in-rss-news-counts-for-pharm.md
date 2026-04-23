# Attention Sentiment Daily Spike In Rss News Counts For Pharmaceutical Price Hike Triggers Bearish Xlv

**Idea ID:** `attention-sentiment-daily-spike-in-rss-news-counts-for-pharm`
**Family:** `attention_sentiment`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden news surges on drug price hikes increase regulatory risk and negative sentiment for healthcare sector. News-driven regulatory fears pressure healthcare stocks.

## Universe
- XLV

## Data Sources
- RSS news feed counts for 'pharmaceutical price hike'

## Signal Logic
Enter short XLV when daily RSS counts for 'pharmaceutical price hike' exceed 3x 7-day average

## Entry / Exit
Entry: Enter short XLV when daily RSS counts for 'pharmaceutical price hike' exceed 3x 7-day average Exit: Exit after 5 trading days or when counts fall below 1.5x average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news feed counts for 'pharmaceutical price hike' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Healthcare news cycles regularly generate short-term spikes in drug pricing stories.

## Required Keys
- None
