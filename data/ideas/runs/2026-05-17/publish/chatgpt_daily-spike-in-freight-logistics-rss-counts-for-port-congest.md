# Daily Spike In Freight Logistics Rss Counts For Port Congestion Reports Signals Supply Chain Pressure

**Idea ID:** `daily-spike-in-freight-logistics-rss-counts-for-port-congest`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
A daily surge in port congestion news signals increasing supply chain bottlenecks impacting industrial throughput. Industrial sector performance is sensitive to supply chain disruptions and logistics constraints.

## Universe
- XLI

## Data Sources
- RSS news feed counts mentioning 'port congestion' or 'logistics delays'

## Signal Logic
Enter short XLI if daily RSS feed count for 'port congestion' doubles relative to 7-day average

## Entry / Exit
Entry: Enter short XLI if daily RSS feed count for 'port congestion' doubles relative to 7-day average Exit: Exit after 5 trading days or when count returns to normal levels

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news feed counts mentioning 'port congestion' or 'logistics delays' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Supply chain news tends to cluster around port congestion spikes periodically.

## Required Keys
- None
