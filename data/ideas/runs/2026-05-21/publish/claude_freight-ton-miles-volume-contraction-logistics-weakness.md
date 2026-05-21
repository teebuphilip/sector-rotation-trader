# Freight Ton-miles Volume Contraction Logistics Weakness

**Idea ID:** `freight-ton-miles-volume-contraction-logistics-weakness`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Rail freight revenue drops >5% week-over-week, signaling reduced shipping activity and slowing supply-chain throughput. Rail freight is leading indicator of industrial production and transportation demand; contraction signals recession risk.

## Universe
- XLI

## Data Sources
- FRED series LRMVSL (Railroads Revenue Freight Services) weekly via fred_series adapter

## Signal Logic
If LRMVSL drops >5% from prior week close and is below 8-week MA

## Entry / Exit
Entry: If LRMVSL drops >5% from prior week close and is below 8-week MA Exit: After 3 weeks or when LRMVSL rebounds above 8-week MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series LRMVSL (Railroads Revenue Freight Services) weekly via fred_series adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Rail data is lumpy and seasonal; multi-week downside streaks occur 3-5 times per year.

## Required Keys
- None
