# Electric Vehicle Charge Station Density

**Idea ID:** `electric-vehicle-charge-station-density`
**Source:** anthropic / claude-3-haiku-20240307
**Frequency:** monthly

## Thesis
The density of electric vehicle charge stations in a geographic region can provide insights into the adoption of electric vehicles and future demand. This signal can be used to identify regions primed for EV growth and investment opportunities.

## Universe
- Tesla (TSLA)
- ChargePoint (CHPT)
- Blink Charging (BLNK)
- Volta (VLTA)

## Data Sources
- U.S. Department of Energy Alternative Fuels Data Center
- OpenChargeMap API

## Signal Logic
Calculate the density of electric vehicle charge stations per square mile or square kilometer in a given region. Monitor changes in charge station density over time to identify regions with accelerating EV adoption.

## Entry / Exit
Enter long positions in companies with exposure to regions with increasing charge station density. Exit positions as density growth slows or levels off.

## Position Sizing
Size positions based on the rate of change in charge station density. Larger positions for regions with rapidly increasing density, smaller positions for regions with slower growth.

## Risks
Charge station data may not be comprehensive, regional adoption patterns may diverge from national trends, and competitive landscape changes could impact investment thesis.

## Implementation Notes
1. Collect charge station data from DOE and OpenChargeMap APIs. 2. Calculate charge station density for regions of interest. 3. Analyze density trends and changes over time. 4. Integrate density data with stock prices to generate trading signals.

## Required Keys
- OpenChargeMap API key
