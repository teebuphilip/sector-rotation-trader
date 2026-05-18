# Regional Bank Cds Spread Widening Signals Financial System Stress

**Idea ID:** `regional-bank-cds-spread-widening-signals-financial-system-s`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When regional bank credit default swap spreads widen sharply, it signals market-perceived stress in the mid-sized financial system, often preceding credit market seizures or deposit runs. CDS spread widening indicates markets price higher default risk for regional banks, compressing equity valuations and reducing lending.

## Universe
- XLF

## Data Sources
- FRED regional bank CDS indices (5-year spreads) and daily price tracking through fred_series adapter

## Signal Logic
If daily regional bank CDS spread widens 30+ basis points in a single day or rises 50+ bps over 5 days, short XLF.

## Entry / Exit
Entry: If daily regional bank CDS spread widens 30+ basis points in a single day or rises 50+ bps over 5 days, short XLF. Exit: Exit after 8 trading days or when spreads contract 20+ bps.

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED regional bank CDS indices (5-year spreads) and daily price tracking through fred_series adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Regional bank CDS spreads experience 30+ bps daily moves during periods of financial uncertainty, which occur multiple times per quarter.

## Required Keys
- None
