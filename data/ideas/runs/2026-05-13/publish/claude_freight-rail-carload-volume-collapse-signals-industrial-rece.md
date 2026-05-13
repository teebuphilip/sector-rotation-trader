# Freight Rail Carload Volume Collapse Signals Industrial Recession Ahead

**Idea ID:** `freight-rail-carload-volume-collapse-signals-industrial-rece`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Rail carloads (especially coal, metals, autos) decline sharply when manufacturing orders weaken. A 6%+ drop week-over-week signals demand destruction 2-4 weeks ahead and triggers industrial ETF selloff. Industrial production and carload traffic are tightly coupled; falling carloads precede earnings misses in construction, manufacturing, and transportation.

## Universe
- XLI

## Data Sources
- AAR weekly carload traffic report via html_table scrape from Association of American Railroads public releases

## Signal Logic
When weekly total carloads decline 6% or more from prior week AND decline persists for 2 consecutive weeks

## Entry / Exit
Entry: When weekly total carloads decline 6% or more from prior week AND decline persists for 2 consecutive weeks Exit: After 8 trading days or when carloads stabilize and post 2 weeks of less than 2% decline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use AAR weekly carload traffic report via html_table scrape from Association of American Railroads public releases via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Carload cycles turn multiple times per year. Recessions, seasonal slowdowns, and trade shocks all produce multi-week drops. AAR data is reliable and published weekly.

## Required Keys
- None
