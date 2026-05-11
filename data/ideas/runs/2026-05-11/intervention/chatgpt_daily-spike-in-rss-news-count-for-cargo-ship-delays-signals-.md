# Daily Spike In Rss News Count For Cargo Ship Delays Signals Upcoming Freight Logistics Slowdowns

**Idea ID:** `daily-spike-in-rss-news-count-for-cargo-ship-delays-signals-`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Increased media mentions of cargo ship delays often precede measurable freight and supply chain bottlenecks. Freight delays reduce industrial throughput and pressure industrial sector earnings.

## Universe
- XLI

## Data Sources
- RSS news feed counts

## Signal Logic
Enter short XLI when daily RSS count for 'cargo ship delay' articles rises 50%+ day-over-day

## Entry / Exit
Entry: Enter short XLI when daily RSS count for 'cargo ship delay' articles rises 50%+ day-over-day Exit: Exit after 5 trading days or when RSS counts normalize

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news feed counts via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: News cycles around freight delays spike frequently due to port congestion and weather.

## Required Keys
- None
