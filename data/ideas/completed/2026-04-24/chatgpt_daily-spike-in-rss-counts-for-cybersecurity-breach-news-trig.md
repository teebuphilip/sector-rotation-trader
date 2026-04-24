# Daily Spike In Rss Counts For Cybersecurity Breach News Triggers Bearish Xlk

**Idea ID:** `daily-spike-in-rss-counts-for-cybersecurity-breach-news-trig`
**Family:** `attention_sentiment`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Increased cyber breach news often causes technology sector volatility and short-term selling pressure. Cybersecurity events increase risk perception and can hit tech stock prices temporarily.

## Universe
- XLK

## Data Sources
- RSS news feed counts

## Signal Logic
If daily RSS count for 'cybersecurity breach' exceeds 4x 20-day average

## Entry / Exit
Entry: If daily RSS count for 'cybersecurity breach' exceeds 4x 20-day average Exit: Exit after 5 trading days or RSS count below 2x average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news feed counts via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 16
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Cyber incidents cluster often with multiple daily news spikes.

## Required Keys
- None
