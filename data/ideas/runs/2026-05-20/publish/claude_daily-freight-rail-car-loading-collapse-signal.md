# Daily Freight Rail Car Loading Collapse Signal

**Idea ID:** `daily-freight-rail-car-loading-collapse-signal`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Rapid decline in rail car loadings precedes industrial contraction; freight logistics weakness is an early warning for manufacturing and consumer discretionary demand. Rail car loadings are a leading indicator of industrial production and inventory builds; collapse signals recession risk.

## Universe
- XLI

## Data Sources
- AAR (Association of American Railroads) weekly rail car loadings via html_table scrape, converted to daily proxies

## Signal Logic
When weekly rail car loadings fall 8% or more below the prior 12-week average

## Entry / Exit
Entry: When weekly rail car loadings fall 8% or more below the prior 12-week average Exit: After 15 trading days or once loadings stabilize within 3% of 12-week average for 2 consecutive weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use AAR (Association of American Railroads) weekly rail car loadings via html_table scrape, converted to daily proxies via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Rail loadings fluctuate seasonally and cyclically; 8% drops occur 2–3 times per year, reliably generating signals within monthly windows.

## Required Keys
- None
