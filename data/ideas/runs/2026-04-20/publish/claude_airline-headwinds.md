# Airline Headwinds

**Idea ID:** `airline-headwinds`
**Family:** ``
**Source:** anthropic / claude-3-haiku-20240307
**Frequency:** weekly

## Thesis
Declines in airline passenger traffic and load factors can signal broader economic uncertainty and reduced consumer demand for travel and leisure activities. Airline traffic is a leading indicator of consumer discretionary spending and the health of the travel and tourism industry.

## Universe
- XLY

## Data Sources
- BTS airline traffic data through bts_airline_load_factor adapter

## Signal Logic
If the weekly airline passenger load factor decreases by more than 3 percentage points compared to the prior week

## Entry / Exit
Entry: If the weekly airline passenger load factor decreases by more than 3 percentage points compared to the prior week Exit: After 2 weeks or once the load factor increases by 2 percentage points

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use BTS airline traffic data through bts_airline_load_factor adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Airline traffic can experience short-term fluctuations due to seasonal trends, economic conditions, and external events, which may trigger the signal within a 30-day timeframe.

## Required Keys
- None
