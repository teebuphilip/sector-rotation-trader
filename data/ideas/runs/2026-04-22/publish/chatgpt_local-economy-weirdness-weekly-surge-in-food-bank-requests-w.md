# Local Economy Weirdness Weekly Surge In Food Bank Requests With Xlp Weakness

**Idea ID:** `local-economy-weirdness-weekly-surge-in-food-bank-requests-w`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increasing food bank demand signals rising consumer hardship, often preceding consumer staples sector weakness. Consumer staples can be pressured by growing economic hardship signals.

## Universe
- XLP

## Data Sources
- Weekly food bank request counts scraped from public local charity tables and Yahoo Finance weekly XLP prices

## Signal Logic
Short XLP when food bank requests increase >10% week-over-week and XLP underperforms SPY

## Entry / Exit
Entry: Short XLP when food bank requests increase >10% week-over-week and XLP underperforms SPY Exit: Cover after 4 weeks or when requests flatten or decline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Weekly food bank request counts scraped from public local charity tables and Yahoo Finance weekly XLP prices via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Food bank request data updates weekly and spikes with local economic stress.

## Required Keys
- None
