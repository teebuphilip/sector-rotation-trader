# Daily Jump In Rss News Counts Mentioning Labor Strike Signals Imminent Industrial Disruption

**Idea ID:** `daily-jump-in-rss-news-counts-mentioning-labor-strike-signal`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
A sudden increase in news volume on labor strikes typically precedes actual work stoppages affecting industries. Strikes disrupt industrial production and supply chains, hurting sector earnings.

## Universe
- XLI

## Data Sources
- RSS/news feed counts

## Signal Logic
If daily labor strike news count spikes 50% above 7-day average

## Entry / Exit
Entry: If daily labor strike news count spikes 50% above 7-day average Exit: When news counts fall below 20% above 7-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS/news feed counts via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Labor strike news surges frequently around contract talks and economic stress.

## Required Keys
- None
