# Temperature Shock Utility Bill Anxiety Google Spike

**Idea ID:** `temperature-shock-utility-bill-anxiety-google-spike`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Extreme heat or cold events trigger simultaneous Google Trends spikes in utility cost anxiety searches, signaling consumer stress pickup and household budget pressure. Elevated utility bill anxiety dampens discretionary spending; consumer goods and leisure stocks face demand leakage.

## Universe
- XLY

## Data Sources
- Google Trends weekly 'electricity bill shock' + 'high utility costs' through google_trends adapter, paired with Open-Meteo daily max temps for regional anomaly

## Signal Logic
If weekly Trends index for utility bill keywords >65 AND regional temp anomaly >+8°F or <-8°F from 30-year normal, short XLY

## Entry / Exit
Entry: If weekly Trends index for utility bill keywords >65 AND regional temp anomaly >+8°F or <-8°F from 30-year normal, short XLY Exit: After 7 trading days or when Trends index falls below 50

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly 'electricity bill shock' + 'high utility costs' through google_trends adapter, paired with Open-Meteo daily max temps for regional anomaly via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seasonal temperature extremes (summer heat, winter cold) occur reliably; anxiety spikes fire monthly in most years.

## Required Keys
- None
