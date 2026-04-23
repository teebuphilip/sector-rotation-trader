# Attention Sentiment Spike Daily Surge In News Rss Counts Mentioning Cyberattack Triggers Bullish Xlc

**Idea ID:** `attention-sentiment-spike-daily-surge-in-news-rss-counts-men`
**Family:** `attention_sentiment`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden spikes in cyberattack news drive demand for communication security and cloud services. Heightened cyberattack awareness tends to buoy cybersecurity-related communications firms.

## Universe
- XLC

## Data Sources
- RSS news feed counts for 'cyberattack' keyword

## Signal Logic
Enter long XLC if daily RSS count for 'cyberattack' doubles 2-day moving average

## Entry / Exit
Entry: Enter long XLC if daily RSS count for 'cyberattack' doubles 2-day moving average Exit: Exit after 7 trading days or when RSS counts return below 1.2x moving average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news feed counts for 'cyberattack' keyword via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Cyberattack news surges happen frequently due to ongoing cybersecurity threats.

## Required Keys
- None
