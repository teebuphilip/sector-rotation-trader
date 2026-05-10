# Healthcare Cost Search Anxiety Surge

**Idea ID:** `healthcare-cost-search-anxiety-surge`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Spikes in healthcare cost searches signal consumer stress about medical expenses, often preceding healthcare sector volatility and consumer spending pullbacks. Healthcare cost anxiety may depress elective procedures and consumer pharmaceutical adherence, pressuring healthcare revenues.

## Universe
- XLV

## Data Sources
- Google Trends weekly search interest for 'prescription drug prices' and 'medical bill debt,' normalized to 12-week baseline

## Signal Logic
If either search term jumps >50% WoW above 12-week MA, short healthcare

## Entry / Exit
Entry: If either search term jumps >50% WoW above 12-week MA, short healthcare Exit: Exit after 9 trading days or if search interest normalizes to <115% of 12-week MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'prescription drug prices' and 'medical bill debt,' normalized to 12-week baseline via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Healthcare cost search spikes >50% occur 2–4 times per quarter, especially around earnings seasons, policy announcements, and seasonal insurance renewal cycles.

## Required Keys
- None
