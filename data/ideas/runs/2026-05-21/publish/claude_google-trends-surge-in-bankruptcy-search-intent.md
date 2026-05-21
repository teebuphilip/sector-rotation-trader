# Google Trends Surge In Bankruptcy Search Intent

**Idea ID:** `google-trends-surge-in-bankruptcy-search-intent`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Bankruptcy-related search interest spikes >40% week-over-week, indicating rising consumer financial distress and debt stress. Rising bankruptcy intent signals credit deterioration, charge-offs, and loan loss reserve impacts on bank profitability.

## Universe
- XLF

## Data Sources
- Google Trends weekly search interest for 'bankruptcy filing' and 'how to declare bankruptcy' via google_trends adapter

## Signal Logic
If bankruptcy search volume exceeds 40% of prior week and is above 12-week median

## Entry / Exit
Entry: If bankruptcy search volume exceeds 40% of prior week and is above 12-week median Exit: After 2 weeks or when volume falls below 12-week median

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'bankruptcy filing' and 'how to declare bankruptcy' via google_trends adapter via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Search spikes occur 2-3 times per quarter during debt ceiling crises, rate hikes, or recession fears.

## Required Keys
- None
