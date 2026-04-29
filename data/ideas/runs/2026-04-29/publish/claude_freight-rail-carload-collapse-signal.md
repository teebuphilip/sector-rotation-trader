# Freight Rail Carload Collapse Signal

**Idea ID:** `freight-rail-carload-collapse-signal`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When weekly carloads (cars loaded with freight) drop 8%+ vs. year-ago week, it signals industrial production weakness; this often precedes equity weakness in materials and industrials. Carload collapse is a leading indicator of manufacturing and construction slowdown.

## Universe
- XLI

## Data Sources
- Association of American Railroads weekly carload data via fred_series adapter (AAR feeds FRED)

## Signal Logic
If weekly carloads fall 8%+ year-over-year AND are below their 13-week rolling average

## Entry / Exit
Entry: If weekly carloads fall 8%+ year-over-year AND are below their 13-week rolling average Exit: After 6 weeks or when carloads stabilize above the 13-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Association of American Railroads weekly carload data via fred_series adapter (AAR feeds FRED) via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Carload data is weekly and volatile; seasonal dips and cyclical weakness create multiple entry points per quarter.

## Required Keys
- None
