# Daily Spike In Rss News Counts For Cybersecurity Breach Impacts Communication Sector

**Idea ID:** `daily-spike-in-rss-news-counts-for-cybersecurity-breach-impa`
**Family:** `attention_sentiment`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden surge in cybersecurity breach news increases negative sentiment for communication stocks reliant on data security. Communication sector is sensitive to cyber risks impacting consumer trust.

## Universe
- XLC

## Data Sources
- RSS news feed counts

## Signal Logic
Enter short XLC when daily RSS count for 'cybersecurity breach' rises 40%+ from prior day

## Entry / Exit
Entry: Enter short XLC when daily RSS count for 'cybersecurity breach' rises 40%+ from prior day Exit: Exit after 5 trading days or when counts revert below 20% increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news feed counts via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Cyber breach news spikes repeatedly due to ongoing threat landscape.

## Required Keys
- None
