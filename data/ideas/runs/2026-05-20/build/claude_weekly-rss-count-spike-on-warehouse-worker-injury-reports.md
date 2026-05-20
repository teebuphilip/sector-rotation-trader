# Weekly Rss Count Spike On Warehouse Worker Injury Reports

**Idea ID:** `weekly-rss-count-spike-on-warehouse-worker-injury-reports`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Spikes in reported warehouse worker injuries signal labor market stress, wage pressure, and operational cost escalation in logistics; presages margin compression. Rising workplace injuries reflect labor shortage, safety corner-cutting, and wage inflation that compress industrial sector profitability.

## Universe
- XLI

## Data Sources
- RSS feed count aggregation for labor safety violations and warehouse injury reports via rss_count adapter

## Signal Logic
When weekly RSS injury report count rises 40% above the 4-week rolling average

## Entry / Exit
Entry: When weekly RSS injury report count rises 40% above the 4-week rolling average Exit: After 12 trading days or once count returns to within 10% of rolling average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS feed count aggregation for labor safety violations and warehouse injury reports via rss_count adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Warehouse injury reports are published regularly; threshold captures seasonal peaks and labor stress cycles; fires 1–2 times per month.

## Required Keys
- None
