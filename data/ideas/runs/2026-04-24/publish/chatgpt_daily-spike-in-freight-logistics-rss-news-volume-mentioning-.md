# Daily Spike In Freight Logistics Rss News Volume Mentioning Port Labor Strike Triggers Bearish Xli

**Idea ID:** `daily-spike-in-freight-logistics-rss-news-volume-mentioning-`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Labor disruptions at ports typically cause immediate shipment delays and supply chain bottlenecks affecting industrial goods. Industrial sector suffers from logistics interruptions caused by labor disputes.

## Universe
- XLI

## Data Sources
- RSS news feed counts

## Signal Logic
If daily RSS counts for 'port labor strike' exceed 3x average daily baseline

## Entry / Exit
Entry: If daily RSS counts for 'port labor strike' exceed 3x average daily baseline Exit: Exit after 7 trading days or when RSS count returns below 1.5x baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news feed counts via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Labor disputes and strike news spikes are common and generate quick media surges impacting logistics.

## Required Keys
- None
