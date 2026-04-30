# Rail Carload Contraction Signal

**Idea ID:** `rail-carload-contraction-signal`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Weekly total carloads drop 8% or more from prior-year equivalent week, signaling sharp freight demand collapse and economic slowdown. Rail carload data is a leading indicator of industrial production, construction input, and commodity demand.

## Universe
- XLI

## Data Sources
- Association of American Railroads weekly carload reports through html_table adapter scraping AAR public tables

## Signal Logic
If latest week carloads are 8%+ below prior-year same week and 4-week average is negative

## Entry / Exit
Entry: If latest week carloads are 8%+ below prior-year same week and 4-week average is negative Exit: After 10 trading days or when year-over-year carloads return to +2%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Association of American Railroads weekly carload reports through html_table adapter scraping AAR public tables via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Carload volatility is seasonal; 8% YoY declines occur 2-4 times per year during demand shocks or inventory cycles.

## Required Keys
- None
