# Mortgage Application Volume Waterfall Signals Housing Demand Collapse

**Idea ID:** `mortgage-application-volume-waterfall-signals-housing-demand`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Sharp week-over-week drops in mortgage applications signal housing demand evaporates due to rate shocks or affordability crisis, impacting construction, materials, and consumer sentiment. Mortgage application collapses reduce demand for construction materials, lumber, and finished housing inventory.

## Universe
- XLB

## Data Sources
- Mortgage Bankers Association weekly applications index through html_table adapter

## Signal Logic
If weekly mortgage applications fall 20% or more below prior week, short XLB for 10 days.

## Entry / Exit
Entry: If weekly mortgage applications fall 20% or more below prior week, short XLB for 10 days. Exit: Exit after 10 trading days or when applications stabilize.

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Mortgage Bankers Association weekly applications index through html_table adapter via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Mortgage applications swing 20%+ weekly due to rate announcements and seasonal factors, firing 2–4 times per month.

## Required Keys
- None
