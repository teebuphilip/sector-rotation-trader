# Weekly Rise In Google Trends For Cyberattack With Corresponding Xlc Underperformance

**Idea ID:** `weekly-rise-in-google-trends-for-cyberattack-with-correspond`
**Family:** `attention_sentiment`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising cyberattack concern often causes investor caution in communications and tech infrastructure sectors. Heightened cyber risk awareness can pressure communications sector stocks.

## Universe
- XLC

## Data Sources
- Google Trends weekly for 'cyberattack' and Yahoo Finance weekly XLC prices

## Signal Logic
Short XLC when 'cyberattack' searches increase >20% week-over-week and XLC underperforms SPY

## Entry / Exit
Entry: Short XLC when 'cyberattack' searches increase >20% week-over-week and XLC underperforms SPY Exit: Cover after 3 weeks or when search interest declines

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly for 'cyberattack' and Yahoo Finance weekly XLC prices via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Cybersecurity concerns frequently trend weekly on news cycles.

## Required Keys
- None
