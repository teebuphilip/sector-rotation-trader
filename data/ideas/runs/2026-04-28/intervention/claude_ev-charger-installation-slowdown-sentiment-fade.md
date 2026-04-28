# Ev Charger Installation Slowdown Sentiment Fade

**Idea ID:** `ev-charger-installation-slowdown-sentiment-fade`
**Family:** `travel_mobility`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When weekly EV charger installation growth (count delta) falls >15% below its 12-week rolling average, it signals EV infrastructure investment cooling. Sentiment on clean energy capex fades. EV charger slowdown signals weakening clean tech capex and consumer EV adoption confidence, pressuring semiconductor and software exposure in energy transition.

## Universe
- XLK

## Data Sources
- OpenChargeMap API monthly charger count growth; cross-reference with FRED vehicle sales series

## Signal Logic
Weekly charger net adds fall >15% below 12-week rolling average; close below prior week close

## Entry / Exit
Entry: Weekly charger net adds fall >15% below 12-week rolling average; close below prior week close Exit: Weekly adds rebound above 10-week rolling average or 12 trading days elapsed

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap API monthly charger count growth; cross-reference with FRED vehicle sales series via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: EV charging growth is lumpy; seasonality and policy cycles cause >15% swings 3–4 times per year. Signal matures in 2–3 weeks.

## Required Keys
- None
