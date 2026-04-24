# Retail Apparel Price Collapse Google Search Decay

**Idea ID:** `retail-apparel-price-collapse-google-search-decay`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Google searches for clearance clothing fall >30% week-over-week after seasonal peaks, signaling buyer exhaustion and inventory overhang clearing. Apparel weakness in search signals consumer pullback in discretionary spending and potential markdowns ahead.

## Universe
- XLY

## Data Sources
- Google Trends weekly search volume for 'clearance clothing sales' via google_trends adapter

## Signal Logic
If 'clearance clothing sales' searches drop >30% from prior week and volume is above median, short XLY

## Entry / Exit
Entry: If 'clearance clothing sales' searches drop >30% from prior week and volume is above median, short XLY Exit: Exit after 9 trading days or if searches rebound above 90-day median

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search volume for 'clearance clothing sales' via google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seasonal clothing clearance cycles drive weekly search swings; collapses occur post-holiday and end-of-season, firing multiple times per quarter.

## Required Keys
- None
