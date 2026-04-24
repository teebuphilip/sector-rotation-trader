# Daily Spike In Rss News Counts Mentioning Politician Insider Buying Tech Stock Signals Bullish Xlk

**Idea ID:** `daily-spike-in-rss-news-counts-mentioning-politician-insider`
**Family:** `political_insider_filing`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Surges in news about political insiders buying tech shares often precede short-term bullish tech rallies. Insider buying by politicians is perceived as confidence in the tech sector's outlook.

## Universe
- XLK

## Data Sources
- RSS news feed counts

## Signal Logic
If daily RSS count for 'politician insider buying tech stock' exceeds 3x 20-day average

## Entry / Exit
Entry: If daily RSS count for 'politician insider buying tech stock' exceeds 3x 20-day average Exit: Exit after 7 trading days or when RSS count drops below 1.5x average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news feed counts via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Political insider activity news spikes cluster around earnings and legislative sessions.

## Required Keys
- None
