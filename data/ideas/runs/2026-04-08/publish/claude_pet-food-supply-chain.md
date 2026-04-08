# Pet Food Supply Chain Disruption

**Idea ID:** `pet-food-supply-chain`
**Source:** anthropic / claude-3-haiku-20240307
**Frequency:** monthly

## Thesis
The pet food industry is highly sensitive to supply chain disruptions. By monitoring key indicators, we can potentially identify upcoming shortages or price increases and trade accordingly.

## Universe
- PETS
- CHWY
- CENT
- CENTA

## Data Sources
- US Department of Agriculture (USDA) reports on pet food production and inventory
- Federal Reserve's Freight Transportation Services Index
- Google Trends data on pet food-related searches

## Signal Logic
{'pet_food_production_decline': 'If USDA monthly pet food production index drops by more than 5% year-over-year', 'freight_transportation_index_drop': 'If Freight Transportation Services Index falls by more than 3% month-over-month', 'pet_food_search_spike': 'If Google Trends index for pet food-related searches increases by more than 20% month-over-month'}

## Entry / Exit
{'entry': 'If 2 out of 3 signals are triggered, enter long positions in major pet food manufacturers', 'exit': 'If all 3 signals return to normal levels, exit long positions'}

## Position Sizing
Equal-weight positions, sizing based on overall portfolio risk tolerance

## Risks
{'false_signals': 'Signals may be triggered by temporary or isolated events, leading to incorrect trades', 'demand_changes': 'Unexpected changes in pet ownership or consumer preferences could impact the effectiveness of the strategy'}

## Implementation Notes
{'steps': ['Collect monthly USDA pet food production data', 'Monitor Freight Transportation Services Index', 'Scrape Google Trends data for pet food-related searches', 'Develop logic to identify signal triggers', 'Backtest strategy on historical data', 'Implement trading system with position sizing and risk management']}

## Required Keys
- None
