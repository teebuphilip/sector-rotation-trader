# Commercial Real Estate Distress News Spike

**Idea ID:** `commercial-real-estate-distress-news-spike`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Clusters of CRE distress stories signal property value compression and lender stress, creating mean reversion shorts in XLRE and bullish trades in restructuring-adjacent sectors. Rising CRE defaults and distress filings directly impair REIT asset values and dividend sustainability.

## Universe
- XLRE

## Data Sources
- RSS feed count from commercial real estate news sources and bankruptcy court filings mentioning office/retail defaults

## Signal Logic
If 3-day rolling count of CRE distress news articles exceeds 6 and is 60% above 30-day average

## Entry / Exit
Entry: If 3-day rolling count of CRE distress news articles exceeds 6 and is 60% above 30-day average Exit: After 10 trading days or if CRE distress news count falls to baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS feed count from commercial real estate news sources and bankruptcy court filings mentioning office/retail defaults via scrape (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: CRE stress cycles are persistent; distress news clusters occur regularly as office leasing cycles and loan maturity cohorts create recurring pressure windows.

## Required Keys
- None
