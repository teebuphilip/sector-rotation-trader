# Analyzecatfoodsalestopredictpetcarestockperformance

**Idea ID:** `analyzecatfoodsalestopredictpetcarestockperformance`
**Source:**  / 
**Frequency:** weekly

## Thesis
Spikes in cat food sales may indicate increased pet ownership and spending, which could signal growth in the pet care industry. The consumer discretionary sector, including pet care stocks, could benefit from increased pet ownership and spending.

## Universe
- XLY

## Data Sources
- Nielson's Pet Food Sales data

## Signal Logic
If 4-week cat food sales growth exceeds 10% vs 3 months ago

## Entry / Exit
Entry: If 4-week cat food sales growth exceeds 10% vs 3 months ago Exit: After 2 weeks or if the 4-week sales growth drops below 5%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Nielson's Pet Food Sales data via api (weekly).

## Required Keys
- None
