# Quality Check — 2026-04-23

## SPY Benchmark
- Current Price: $708.45
- YTD Return: +3.98%
- YTD High: $711.21
- YTD Low: $631.97
- Max Drawdown: -11.14%

## Baseline (NRWise)
- Equity: $100,045.55 (+0.05%)
- Sector: XLU
- Last Snapshot: 2026-04-23
- Snapshots: 84
- Trades: 11
- Positions: 1
- Alpha vs SPY: -3.94%

## Normal Algos
  Algo                        Equity       YTD     Alpha  Trades      Signal    Last Run
  --------------------------------------------------------------------------------------
  baileymol              $105,781.58     5.78%     1.80%      30  XLE,XLK,XLY  2026-04-23
  dmsr                   $104,760.23     4.76%     0.78%      15        CASH  2026-04-23
  faber                  $103,846.61     3.85%    -0.14%       8        CASH  2026-04-23
  simple_monthly         $100,000.00     0.00%    -3.98%       0        CASH  2026-04-23
  biscotti                $99,880.80    -0.12%    -4.10%       5        CASH  2026-04-23

## Crazy Algos — Active (33/107)
  Algo                        Equity       YTD     Alpha  Trades      Signal    Last Run
  --------------------------------------------------------------------------------------
  finra-dark-pool-signal   $101,669.32     1.67%    -2.31%       2  HIGH_SHORT  2026-04-23
  uber-mobility          $101,066.05     1.07%    -2.92%       6    RISK_OFF  2026-04-23
  insider-trading-signals   $100,992.01     0.99%    -2.99%       1  INSIDER_DROUGHT  2026-04-23
  mortgage-rate-housing-proxy   $100,429.39     0.43%    -3.55%       2  HOUSING_HEADWIND  2026-04-23
  earthquake-aftershock-amplifier   $100,047.52     0.05%    -3.94%       2        HOLD  2026-04-23
  semiconductor-moonshot-warning   $100,045.62     0.05%    -3.94%       6        HOLD  2026-04-23
  copper-momentum        $100,032.35     0.03%    -3.95%       2  GLOBAL_GROWTH  2026-04-23
  materials-sector-weekly-positive-correlation-breakdown-with-   $100,025.87     0.03%    -3.96%       2        HOLD  2026-04-23
  staples-sector-drawdown-rapid-recovery   $100,024.70     0.02%    -3.96%       2        HOLD  2026-04-23
  electricity-consumption    $99,989.87    -0.01%    -3.99%      10  INDUSTRIAL_POWER_DEMAND  2026-04-23
  consumer-discretionary-google-trends-surge-for-sale-keywords    $99,960.96    -0.04%    -4.02%       6        HOLD  2026-04-23
  industrial-sector-weekly-earthquake-activity-correlation-dip    $99,958.22    -0.04%    -4.03%       5     RISK_ON  2026-04-23
  real-estate-sector-weekly-google-trends-home-buying-surge    $99,954.77    -0.05%    -4.03%       2        HOLD  2026-04-23
  news-sentiment-rotation-fade-trade    $99,929.81    -0.07%    -4.05%       2        HOLD  2026-04-23
  utilities-sector-negative-price-gap-fill    $99,921.53    -0.08%    -4.06%      14        HOLD  2026-04-23
  healthcare-sector-google-trends-spike-in-flu-symptoms    $99,917.38    -0.08%    -4.07%       6        HOLD  2026-04-23
  xlb-weekly-rss-news-count-spike-on-commodity-shortage    $99,913.68    -0.09%    -4.07%       4    RISK_OFF  2026-04-23
  retail-roulette         $99,913.43    -0.09%    -4.07%      12        HOLD  2026-04-23
  xlu-daily-electricity-demand-surge    $99,898.68    -0.10%    -4.08%      12        HOLD  2026-04-23
  google-gusts            $99,871.97    -0.13%    -4.11%       4        HOLD  2026-04-23
  tremor-tension          $99,864.21    -0.14%    -4.12%       8        HOLD  2026-04-23
  seismic-activity-construction-halt-signal    $99,861.92    -0.14%    -4.12%       6        HOLD  2026-04-23
  electricity-enlightenment    $99,857.33    -0.14%    -4.13%      10        HOLD  2026-04-23
  retail-sales-momentum    $99,826.75    -0.17%    -4.16%       2   EXPANDING  2026-04-23
  grocery-store-foot-traffic-collapse-signal    $99,688.36    -0.31%    -4.30%      20        HOLD  2026-04-23
  xle-weekly-drawdown-rebound-signal    $99,667.30    -0.33%    -4.32%      32        HOLD  2026-04-23
  healthcare-cost-shock-google-search-spike    $99,617.84    -0.38%    -4.37%      22        HOLD  2026-04-23
  xlc-weekly-google-trends-surge-in-5g-rollout    $99,592.39    -0.41%    -4.39%      46        HOLD  2026-04-23
  lumber-momentum         $99,510.21    -0.49%    -4.47%       2  BUILDING_DEMAND  2026-04-23
  biscotti                $97,786.99    -2.21%    -6.20%       5        HOLD  2026-04-23
  baileymol               $93,880.46    -6.12%   -10.10%      62  XLK|XLY|XLE  2026-04-23
  vix-term-structure      $93,788.26    -6.21%   -10.20%     106        HOLD  2026-04-23
  vix-fear-rotation       $91,997.66    -8.00%   -11.99%     118        HOLD  2026-04-23

## Crazy Algos — Idle (74/107)
  These algos are running but have no recorded trades in the current state history.
  That is not a crash; it means the trigger has not fired yet, the adapter returned no usable signal, or the strategy is still waiting for live evidence.

  airline-load-factor                  airport-security-surge               airport-shopping-spree               bankruptcy-filing-rate             
  calls311                             cardboard                            cloud-storage-demand-surge           congress                           
  consumer-sentiment                   craigslist                           credit-card-delinquency              crypto-capitulation-countdown      
  crypto-derivative-arbitrage          earthquake-energy-demand             electric-vehicle-charge-station-density  energy-sector-sudden-weekly-volatility-spike
  energy-sector-weekly-drawdown-exhaustion  ev-charger-density-saturation-play   ev-charging-boom                     ev-charging-station-stampede       
  ev-euphoria                          financial-sector-momentum-divergence-with-spy  fintech-disruption-wave              freight-rail-carloads              
  glassdoor                            global-tech-earnings-momentum        high-yield-spread-regime             housing-permit-velocity            
  job-posting-acceleration             linkedin                             liquor                               lumber-futures-rollercoaster       
  materials-sector-weekly-volatility-contraction-breakout  misery-rotation                      online-ad-impression-volatility      patent-filing-velocity             
  pet-food-supply-chain                port-congestion-squeeze              port-container-volume                reddit-emoji-sentiment-spike       
  reddit-gaming-thread-spike           reddit-mentions-volatility-spike     reddit-sentiment-spike-trend         reddit-sentiment-spike             
  reddit-sentiment-volatility-spike    reddit-subreddit-mention-spike       reddit-subreddit-sentiment-spike     reddit-subreddit-surge-momentum    
  reddit-volatility-spike              rental-car-shortage-volatility-spike  retail-rush-ahead-of-holidays        rss-roar                           
  shipping-container-squeeze-play      small-business-formation             social-media-sentiment-spike         solar-storm-scorcher               
  superbowl-futures-trade              technology-sector-daily-ev-charger-count-surge  temperature-shock-energy-demand-flip  truck-tonnage                      
  tsa                                  twitter-sentiment-spike              utilities-sector-weekly-temperature-drop-signal  utility-power-grid-stress          
  volatility-spike-follow-through      weather-disruption-ripple-effects    weather-volatility-spike             weather-windfall                   
  work-from-home-frenzy                xlb-daily-volatility-contraction-breakout  xlu-weekly-cold-snap-weather-correlation  xlv-google-trends-flu-search-spike 
  yelp-closure-velocity                yield-curve-regime                 

## Blocked Algos
- **EIA_API_KEY** (1 algos): Electricity Consumption
- **GLASSDOOR_KEY** (1 algos): Glassdoor Misery Gradient
- **GLASSDOOR_PARTNER_ID** (1 algos): Glassdoor Misery Gradient
- **YELP_API_KEY** (1 algos): Yelp Closure Velocity

## Flags & Warnings
- Total algos: 112
- Beating SPY: 2/112 (but only 2 have actually traded)
- Best: baileymol at +5.78%
- Worst: vix-fear-rotation at -8.00%

- CHURNING: baileymol has 62 trades but is down -6.12% — overtrading?
- CHURNING: vix-fear-rotation has 118 trades but is down -8.00% — overtrading?
- CHURNING: vix-term-structure has 106 trades but is down -6.21% — overtrading?

## Context Notes
- HELD POSITIONS WITH HOLD SIGNAL: 3 algos. HOLD means maintain/no rebalance here, not forced exit.
-   - biscotti (crazy) has 1 open positions
-   - vix-fear-rotation (crazy) has 2 open positions
-   - vix-term-structure (crazy) has 2 open positions

---
_Generated by `scripts/quality_check.py` at 2026-04-23 23:15 UTC_