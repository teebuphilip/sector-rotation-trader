# Weekly Surge In Rss News Count Mentioning Union Contract Dispute Triggers Bearish Financial Sector

**Idea ID:** `weekly-surge-in-rss-news-count-mentioning-union-contract-dis`
**Family:** `political_insider_filing`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Growing media attention on union disputes signals rising labor risk and uncertainty for financials exposed to unionized labor. Increased labor disputes raise operational risk and costs for financial institutions.

## Universe
- XLF

## Data Sources
- RSS feed count of labor union dispute news

## Signal Logic
Enter short XLF when weekly RSS count for 'union contract dispute' rises 50% above 12-week average

## Entry / Exit
Entry: Enter short XLF when weekly RSS count for 'union contract dispute' rises 50% above 12-week average Exit: Exit after 4 weeks or when counts revert below 12-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS feed count of labor union dispute news via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Labor disputes flare regularly, generating multiple weekly news spikes.

## Required Keys
- None
