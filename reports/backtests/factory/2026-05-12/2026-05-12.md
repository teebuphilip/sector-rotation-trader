# Professional Backtest V1

- Run date: 2026-05-12
- Window: 2024-01-01 to 2026-05-12
- Slippage: 5.0 bps per trade
- Method: signal after close, execute next trading day open, long/cash only, SPY benchmark.

## Counts

- LIVE_ONLY_NON_PRICE: 10
- NEEDS_HISTORY: 1

## Results

| Algo | Family | Status | Alpha vs SPY | Trades | Reason |
| --- | --- | --- | ---: | ---: | --- |
| Daily Jump In Google Trends For Emergency Roadside Assistance Signals Consumer Stress Impacting Discretionary Sector | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Daily Jump In Openchargemap Ev Charger Counts In Key States Signals Tech Sector Acceleration | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.openchargemap |
| Ev Charger Network Expansion Sentiment Surge | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Healthcare Procedure Google Trends Demand Resurgence | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Weekly Google Trends Surge For Small Business Loan Application Signals Financial Sector Activity Boost | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Weekly Google Trends Surge For Truck Tire Replacement Searches Signals Industrial Sector Repair Cycle | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Weekly Jump In Google Trends For Job Quitting Searches Signals Labor Market Tightness Benefiting Financial Sector | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Weekly Jump In Google Trends Home Pest Control Emergency Searches Signals Consumer Stress And Discretionary Rebound | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Weekly Spike In Freight Container Volumes At East Coast Ports Signals Industrial Sector Strength | crazy | NEEDS_HISTORY |  |  | Historical seed exists, but V1 cannot prove point-in-time price-only behavior |
| Weekly Surge In Google Trends Diy Home Roofing Repair Searches Signals Industrial Sector Demand Spike | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Weekly Surge In Google Trends For Sudden Appliance Breakdowns Signals Discretionary Sector Rebound | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |

This is experimental research, not investment advice. Past performance does not predict future results.
