# Professional Backtest V1

- Run date: 2026-04-27
- Window: 2024-01-01 to 2026-04-27
- Slippage: 5.0 bps per trade
- Method: signal after close, execute next trading day open, long/cash only, SPY benchmark.

## Counts

- BACKTEST_WEAK: 1
- LIVE_ONLY_NON_PRICE: 4

## Results

| Algo | Family | Status | Alpha vs SPY | Trades | Reason |
| --- | --- | --- | ---: | ---: | --- |
| Daily Spike In Ev Charger Installations Signals Bullish Xlc | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.openchargemap |
| Ev Charger Network Density Surge Bullish Signal | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.openchargemap |
| Oil Price Momentum Reversal Energy Sector Bounce | crazy | BACKTEST_WEAK | -55.17 | 121 | Backtest completed |
| Weekly Google Trends Spike For Diy Car Repair Signals Bullish Xly | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Weekly Surge In Google Trends For Inflation Hedge Gold Signals Bullish Xlb | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |

This is experimental research, not investment advice. Past performance does not predict future results.
