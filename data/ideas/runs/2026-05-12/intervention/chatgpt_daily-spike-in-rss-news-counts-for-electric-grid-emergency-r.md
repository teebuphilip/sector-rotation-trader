# Daily Spike In Rss News Counts For Electric Grid Emergency Repairs Signals Utility Sector Volatility

**Idea ID:** `daily-spike-in-rss-news-counts-for-electric-grid-emergency-r`
**Family:** `attention_sentiment`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
News surges about grid emergencies often precede utility sector price swings due to repair costs and regulatory scrutiny. Utility stocks often face short-term pressure from emergency repair cost concerns.

## Universe
- XLU

## Data Sources
- RSS feed counts for electric grid emergency and repair news

## Signal Logic
Enter short XLU when daily RSS counts for grid emergency news rise 50%+ above 7-day average

## Entry / Exit
Entry: Enter short XLU when daily RSS counts for grid emergency news rise 50%+ above 7-day average Exit: Exit after 7 days or when news counts normalize

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS feed counts for electric grid emergency and repair news via scrape (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Grid emergency news spikes multiple times annually tied to weather and infrastructure failures.

## Required Keys
- None
