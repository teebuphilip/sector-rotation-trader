# Regional Earthquake Cluster Insurance Demand Spike

**Idea ID:** `regional-earthquake-cluster-insurance-demand-spike`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Clusters of 4+ earthquakes in 7 days (any US region, magnitude 3.5+) trigger 40-60% surge in insurance/inspection searches within 48 hours. Real estate and property stocks (builders, insurers) experience brief bullish pressure as emergency repair demand rises. Earthquake clusters drive near-term demand for property inspections, repairs, and insurance policy uptake; benefits regional real estate and construction activity.

## Universe
- XLRE

## Data Sources
- USGS earthquake_activity daily feed (magnitude 3.5+) via earthquake_activity adapter; paired with Google Trends searches for 'earthquake insurance' and 'home inspection'

## Signal Logic
4+ magnitude 3.5+ earthquakes within 7 days in same US region; Google Trends 'earthquake insurance' index rises 40%+ week-over-week; enter long XLRE

## Entry / Exit
Entry: 4+ magnitude 3.5+ earthquakes within 7 days in same US region; Google Trends 'earthquake insurance' index rises 40%+ week-over-week; enter long XLRE Exit: After 5 trading days OR Google Trends 'earthquake insurance' returns to baseline, whichever first

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS earthquake_activity daily feed (magnitude 3.5+) via earthquake_activity adapter; paired with Google Trends searches for 'earthquake insurance' and 'home inspection' via api (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: USGS earthquake data is continuous; regional clusters occur 2-3 times per quarter; Google Trends lags by 1-2 days; 5-day position window ensures frequent fire opportunities.

## Required Keys
- None
