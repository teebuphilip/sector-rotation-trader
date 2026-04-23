# Grocery Demand Surge From Layoff Chatter

**Idea ID:** `grocery-demand-surge-from-layoff-chatter`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Spikes in job-loss-related searches precede stress-buying of shelf-stable foods and household essentials. Staples retailers see margin expansion and volume lift as households shift spending from discretionary to staples. Consumer staples outperform when households face job anxiety; defensive rotation into grocery/essentials is immediate and predictable.

## Universe
- XLP

## Data Sources
- Google Trends weekly search volume for 'layoffs near me' and 'how to apply for unemployment' via google_trends adapter, plus XLP (consumer staples) weekly close via price_only adapter

## Signal Logic
If Google Trends 'layoffs near me' + 'unemployment application' combined score rises >40% week-over-week AND XLP RSI(14) < 65 AND XLP closes > open

## Entry / Exit
Entry: If Google Trends 'layoffs near me' + 'unemployment application' combined score rises >40% week-over-week AND XLP RSI(14) < 65 AND XLP closes > open Exit: After 14 calendar days OR if layoff search trend falls >30% from peak

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search volume for 'layoffs near me' and 'how to apply for unemployment' via google_trends adapter, plus XLP (consumer staples) weekly close via price_only adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Quarterly earnings cuts and macro disappointments trigger layoff announcements and chatter; each cycle fires the signal 2–3 times.

## Required Keys
- None
