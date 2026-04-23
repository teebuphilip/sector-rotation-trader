# Healthcare Cost Panic From Medical Billing Scandal News Surge

**Idea ID:** `healthcare-cost-panic-from-medical-billing-scandal-news-surg`
**Family:** `attention_sentiment`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Spikes in news coverage of medical billing errors, surprise hospital bills, or insurance denials trigger consumer anxiety. Healthcare stocks dip on regulatory scrutiny fear, then recover as overshooting subsides. News surges on billing scandals create temporary fear of margin compression and regulatory action, causing tactical healthcare sector weakness.

## Universe
- XLV

## Data Sources
- RSS feed article count from healthcare/medical billing news sites (healthcare.gov, CMS press releases, major medical journals) via rss_count adapter, plus XLV (healthcare) weekly close via price_only adapter

## Signal Logic
If weekly RSS article count from healthcare billing topics exceeds 200% of 4-week MA AND XLV closes < 20-day SMA AND article count rises >50% week-over-week

## Entry / Exit
Entry: If weekly RSS article count from healthcare billing topics exceeds 200% of 4-week MA AND XLV closes < 20-day SMA AND article count rises >50% week-over-week Exit: After 7 calendar days OR if article count falls below 120% of 4-week MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS feed article count from healthcare/medical billing news sites (healthcare.gov, CMS press releases, major medical journals) via rss_count adapter, plus XLV (healthcare) weekly close via price_only adapter via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Medical billing scandals emerge periodically; each major news cycle (Congressional hearings, investigative reports) fires the signal.

## Required Keys
- None
