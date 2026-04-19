# Xli Weekly Industrial Production Acceleration

**Idea ID:** `xli-weekly-industrial-production-acceleration`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Acceleration in industrial production growth often precedes strength in industrial sector ETFs. Industrial output gains drive industrial sector earnings.

## Universe
- XLI

## Data Sources
- FRED monthly industrial production index interpolated weekly

## Signal Logic
Enter long if weekly interpolated industrial production growth rate accelerates by 0.5%+ compared to prior week

## Entry / Exit
Entry: Enter long if weekly interpolated industrial production growth rate accelerates by 0.5%+ compared to prior week Exit: Exit after 4 weeks or if growth decelerates

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED monthly industrial production index interpolated weekly via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Industrial production shows measurable weekly acceleration patterns after monthly releases.

## Required Keys
- None
