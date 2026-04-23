# Freight Rail Carload Plunge From Manufacturing Slowdown

**Idea ID:** `freight-rail-carload-plunge-from-manufacturing-slowdown`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Carload volumes fall sharply when manufacturing activity weakens. A >5% drop in weekly carloads vs 4-week MA signals demand destruction; industrials and materials underperform within 2 weeks. Rail carload data is a real-time proxy for industrial production; sharp declines precede earnings misses and guidance cuts.

## Universe
- XLI

## Data Sources
- FRED series RAILFRTCG (railroad freight carloads, weekly) via fred_series adapter, plus XLI (industrials) weekly close via price_only adapter

## Signal Logic
If RAILFRTCG weekly < 4-week MA × 0.95 AND XLI closes below 20-day SMA AND XLI RSI(14) < 50

## Entry / Exit
Entry: If RAILFRTCG weekly < 4-week MA × 0.95 AND XLI closes below 20-day SMA AND XLI RSI(14) < 50 Exit: After 10 trading days OR if RAILFRTCG recovers to 4-week MA for 2 consecutive weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series RAILFRTCG (railroad freight carloads, weekly) via fred_series adapter, plus XLI (industrials) weekly close via price_only adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Quarterly inventory corrections and seasonal demand shifts trigger carload drops reliably; signal fires every 4–6 weeks.

## Required Keys
- None
