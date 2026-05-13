# News Article Count Spike On Financial Services Regulatory Failures Triggers Banking Sector Selloff

**Idea ID:** `news-article-count-spike-on-financial-services-regulatory-fa`
**Family:** `attention_sentiment`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Regulatory enforcement news and compliance scandals cluster around specific institutions or industry-wide reviews. A 40%+ spike in weekly enforcement/violation articles signals sell-first sentiment in financials. Bank regulatory news drives short-term risk-off sentiment and increases long-term cost expectations. Enforcement news is processed quickly by markets.

## Universe
- XLF

## Data Sources
- RSS feed count for news articles mentioning 'bank regulation', 'compliance violation', 'federal reserve enforcement' via rss_count adapter, weekly aggregates

## Signal Logic
When weekly RSS article count for banking regulatory keywords increases 40% or more from prior week

## Entry / Exit
Entry: When weekly RSS article count for banking regulatory keywords increases 40% or more from prior week Exit: After 6 trading days or when article count reverts below 20% above baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS feed count for news articles mentioning 'bank regulation', 'compliance violation', 'federal reserve enforcement' via rss_count adapter, weekly aggregates via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Regulatory cycles produce multiple enforcement actions per quarter. Stress tests, compliance exams, and scandal-driven coverage create regular 30-60% spikes in article counts.

## Required Keys
- None
