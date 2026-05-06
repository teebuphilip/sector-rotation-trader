# Financial Services Cybersecurity Threat Alert Sentiment Swing

**Idea ID:** `financial-services-cybersecurity-threat-alert-sentiment-swin`
**Family:** `attention_sentiment`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When weekly cybersecurity threat article counts mentioning financial services spike 40%+ above baseline, XLF often experiences a 2-4 day selloff followed by mean reversion as investors realize systemic risk remains contained. Cybersecurity headline spikes create short-term financial sector rotation but typically resolve as false alarms within a week.

## Universe
- XLF

## Data Sources
- RSS feed count aggregation from Krebs on Security + Dark Reading + SC Magazine weekly mentions of 'banking' + 'fintech' + 'breach' through rss_count adapter

## Signal Logic
If weekly fintech/banking cybersecurity threat article count exceeds 40% of trailing 4-week average, short XLF on next open

## Entry / Exit
Entry: If weekly fintech/banking cybersecurity threat article count exceeds 40% of trailing 4-week average, short XLF on next open Exit: Exit after 5 trading days or if article count falls below 120% of baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS feed count aggregation from Krebs on Security + Dark Reading + SC Magazine weekly mentions of 'banking' + 'fintech' + 'breach' through rss_count adapter via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Cybersecurity news is volatile and clustered; 40% spikes above baseline occur every 2-3 weeks during threat seasons.

## Required Keys
- None
