# Weekly Spike In Rss Count For Inflation-related News

**Idea ID:** `weekly-spike-in-rss-count-for-inflation-related-news`
**Family:** `attention_sentiment`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Sudden increase in inflation-related news volume tends to raise market anxiety and pressure cyclicals. Materials sector is sensitive to inflation pressures and input cost volatility.

## Universe
- XLB

## Data Sources
- RSS feed aggregation counts for 'inflation' keyword weekly

## Signal Logic
Enter short XLB when weekly inflation-related RSS count rises 40% above 8-week average

## Entry / Exit
Entry: Enter short XLB when weekly inflation-related RSS count rises 40% above 8-week average Exit: Exit after 3 weeks or when count drops below 20% above average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS feed aggregation counts for 'inflation' keyword weekly via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Inflation news cycles spike multiple times per year, especially around Fed announcements.

## Required Keys
- None
