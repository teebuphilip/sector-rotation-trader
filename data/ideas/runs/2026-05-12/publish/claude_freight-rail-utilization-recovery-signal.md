# Freight Rail Utilization Recovery Signal

**Idea ID:** `freight-rail-utilization-recovery-signal`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Weekly carload volume spikes above 12-week moving average signal sudden demand recovery in manufacturing and commodities, bullish for industrials and materials. Rail volume is a leading proxy for real economic activity; spikes correlate with factory orders and industrial production acceleration.

## Universe
- XLI

## Data Sources
- AAR (Association of American Railroads) weekly carload data via FRED series RAILCDF (carloads and intermodal) or scrape public AAR reports

## Signal Logic
If weekly carload count exceeds 12-week MA by >5% and volume increases YoY

## Entry / Exit
Entry: If weekly carload count exceeds 12-week MA by >5% and volume increases YoY Exit: After 3 weeks or when carloads fall back below 12-week MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use AAR (Association of American Railroads) weekly carload data via FRED series RAILCDF (carloads and intermodal) or scrape public AAR reports via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seasonal demand swings and supply-chain normalization events trigger rail spikes several times per quarter.

## Required Keys
- None
