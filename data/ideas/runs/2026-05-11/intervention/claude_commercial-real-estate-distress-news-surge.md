# Commercial Real Estate Distress News Surge

**Idea ID:** `commercial-real-estate-distress-news-surge`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When daily RSS article count on commercial property defaults, office vacancy, or REIT stress spikes 120%+ above baseline, financials derating begins. CRE distress signals declining REIT fundamentals, loan losses, and balance sheet deterioration for financial sector.

## Universe
- XLRE

## Data Sources
- RSS feed count from CRE news outlets (CoStar, Real Capital Analytics) via rss_count adapter

## Signal Logic
If CRE distress RSS count exceeds 20-day average by 120%

## Entry / Exit
Entry: If CRE distress RSS count exceeds 20-day average by 120% Exit: After 10 trading days or if articles drop to <110% of baseline for 2 days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS feed count from CRE news outlets (CoStar, Real Capital Analytics) via rss_count adapter via scrape (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: CRE volatility is constant; distress stories spike weekly during earnings seasons and when major properties enter default cycles.

## Required Keys
- None
