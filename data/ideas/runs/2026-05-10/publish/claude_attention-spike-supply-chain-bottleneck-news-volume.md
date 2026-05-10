# Attention Spike Supply Chain Bottleneck News Volume

**Idea ID:** `attention-spike-supply-chain-bottleneck-news-volume`
**Family:** `attention_sentiment`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Daily spikes in supply chain disruption news coverage correlate with industrial demand shocks and equity rotation into defensive sectors. Supply chain news spikes signal production headwinds and cost pressures that depress industrial equipment and manufacturing valuations.

## Universe
- XLI

## Data Sources
- RSS feed article count monitoring 'supply chain disruption' and 'logistics backlog' across major financial news sites, daily updates

## Signal Logic
If daily RSS article count for supply chain keywords exceeds 150% of 20-day moving average, short industrials

## Entry / Exit
Entry: If daily RSS article count for supply chain keywords exceeds 150% of 20-day moving average, short industrials Exit: Exit after 7 trading days or if RSS count returns to <120% of 20-day MA for 2 consecutive days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS feed article count monitoring 'supply chain disruption' and 'logistics backlog' across major financial news sites, daily updates via scrape (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Supply chain news spikes above 150% threshold occur 3–6 times per quarter due to port congestion, carrier bankruptcies, and seasonal demand shocks.

## Required Keys
- None
