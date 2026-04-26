# Hospital Admission Surge Detection Via Google Trends

**Idea ID:** `hospital-admission-surge-detection-via-google-trends`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Spikes in hospital/ER search interest signal acute health crisis events (seasonal flu, contamination events, heatwaves) that precede healthcare utilization surges and pharmaceutical demand. Hospital admission spikes drive emergency pharmaceutical demand, clinical supplies, and diagnostic testing—all benefiting healthcare sector.

## Universe
- XLV

## Data Sources
- Google Trends weekly interest for 'emergency room wait time', 'hospital admission process', 'urgent care near me' via google_trends adapter

## Signal Logic
If weekly search index exceeds 130% of 52-week median across 3+ major metros, go long XLV

## Entry / Exit
Entry: If weekly search index exceeds 130% of 52-week median across 3+ major metros, go long XLV Exit: After 3 weeks or if search index normalized to <110% of median

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly interest for 'emergency room wait time', 'hospital admission process', 'urgent care near me' via google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seasonal illness cycles, heatwave events, and contamination incidents trigger hospital search spikes multiple times per year, especially during winter and summer peaks.

## Required Keys
- None
