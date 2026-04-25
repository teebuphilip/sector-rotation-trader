# Healthcare Labor Shortage Search Spike

**Idea ID:** `healthcare-labor-shortage-search-spike`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Spikes in healthcare labor shortage searches indicate wage pressure and operational stress in hospitals, signaling margin compression and staffing cost inflation in healthcare providers. Healthcare labor shortages increase wage costs and operational inefficiency, compressing provider margins and driving negative earnings revisions.

## Universe
- XLV

## Data Sources
- Google Trends weekly search volume for 'nursing shortage', 'healthcare staffing crisis', 'hospital hiring'

## Signal Logic
If 3-week average search volume exceeds 70th percentile of prior 52-week distribution

## Entry / Exit
Entry: If 3-week average search volume exceeds 70th percentile of prior 52-week distribution Exit: After 14 trading days or if search volume falls below 50th percentile for 2 consecutive weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search volume for 'nursing shortage', 'healthcare staffing crisis', 'hospital hiring' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Healthcare labor discussions are seasonal and persistent; search volume surges occur regularly with winter illness cycles and seasonal hiring windows.

## Required Keys
- None
