# Fred Jobless Claims Volatility Pop Reversion

**Idea ID:** `fred-jobless-claims-volatility-pop-reversion`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When initial jobless claims spike 20% week-over-week (often noise-driven or seasonal), they often revert sharply the following week, creating mean-reversion trading opportunity in defensive and cyclical sectors. Extreme jobless claim spikes are often false signals or seasonal; mean reversion favors cyclical consumer stocks.

## Universe
- XLY

## Data Sources
- FRED series ICSA (Initial Jobless Claims) weekly through fred_series adapter

## Signal Logic
If weekly ICSA increases >20% from prior week, enter long XLY at close

## Entry / Exit
Entry: If weekly ICSA increases >20% from prior week, enter long XLY at close Exit: After 5 trading days or if ICSA falls week-over-week

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series ICSA (Initial Jobless Claims) weekly through fred_series adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seasonal and holiday-related jobless claim spikes occur predictably; >20% moves happen 3–5 times annually.

## Required Keys
- None
