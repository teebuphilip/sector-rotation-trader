# Weekly Rise In Google Trends For Airline Strikes With Bearish Xly Travel Leisure Impact

**Idea ID:** `weekly-rise-in-google-trends-for-airline-strikes-with-bearis`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increased interest in airline labor disruptions often signals near-term travel demand weakness. Travel and leisure stocks are sensitive to airline labor disruptions.

## Universe
- XLY

## Data Sources
- Google Trends weekly for 'airline strikes' and Yahoo Finance weekly XLY prices

## Signal Logic
Short XLY when 'airline strikes' searches rise >15% week-over-week and XLY underperforms SPY weekly

## Entry / Exit
Entry: Short XLY when 'airline strikes' searches rise >15% week-over-week and XLY underperforms SPY weekly Exit: Cover after 3 weeks or when search interest declines

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly for 'airline strikes' and Yahoo Finance weekly XLY prices via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Airline labor unrest is a recurring theme with frequent weekly interest spikes.

## Required Keys
- None
