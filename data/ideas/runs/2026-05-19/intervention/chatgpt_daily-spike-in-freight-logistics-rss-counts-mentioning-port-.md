# Daily Spike In Freight Logistics Rss Counts Mentioning Port Congestion Signals Supply Chain Stress

**Idea ID:** `daily-spike-in-freight-logistics-rss-counts-mentioning-port-`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
A surge in news mentioning port congestion indicates worsening logistics bottlenecks that can pressure industrial supply chains. Industrial and transportation sectors face input delays and higher costs during port congestion episodes.

## Universe
- XLI

## Data Sources
- RSS news feed counts for freight and shipping

## Signal Logic
Enter short XLI when daily RSS counts for 'port congestion' exceed 3 standard deviations above 30-day mean

## Entry / Exit
Entry: Enter short XLI when daily RSS counts for 'port congestion' exceed 3 standard deviations above 30-day mean Exit: Exit after 7 trading days or if counts revert below 1.5 std deviations

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news feed counts for freight and shipping via scrape (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: News cycles frequently report on port delays and congestion spikes.

## Required Keys
- None
