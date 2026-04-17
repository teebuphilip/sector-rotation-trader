import os
from datetime import date

from crazy.config import CRAZY_COMBINED_DASHBOARD


def generate_combined_dashboard(summaries):
    os.makedirs(os.path.dirname(CRAZY_COMBINED_DASHBOARD), exist_ok=True)

    idle_count = sum(
        1 for s in summaries
        if s.get("num_trades", 0) == 0 and abs(s.get("net_pnl", 0.0)) < 0.005
    )
    active_count = len(summaries) - idle_count
    lab_starts = sorted(s.get("sim_start") for s in summaries if s.get("sim_start"))
    lab_start = lab_starts[0] if lab_starts else "unknown"

    rows = ""
    for s in summaries:
        pnl_color = "#0dd39b" if s["net_pnl"] >= 0 else "#ff6b6b"
        is_idle = s.get("num_trades", 0) == 0 and abs(s.get("net_pnl", 0.0)) < 0.005
        status = "Idle / never fired" if is_idle else "Active"
        status_class = "idle" if is_idle else "active"
        rows += f"""
        <tr class="{status_class}">
          <td class="name">{s['name']}</td>
          <td>${s['equity']:,.0f}</td>
          <td style="color:{pnl_color}">${s['net_pnl']:+,.0f}</td>
          <td>{s['sharpe']:.2f}</td>
          <td>{s['max_drawdown_pct']:.2f}%</td>
          <td>{s['last_signal']}</td>
          <td>{s.get('num_trades', 0)}</td>
          <td>{status}</td>
          <td><a href="../algos/{s['algo_id']}/index.html">Open</a></td>
        </tr>
        """

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Crazy Algos Dashboard</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=IBM+Plex+Mono:wght@400;600&display=swap');
  :root {{
    --bg: #0f1d1a;
    --bg-2: #12312a;
    --card: #152a25;
    --accent: #18d6a1;
    --muted: #9db7ad;
    --text: #e6f3ee;
    --warn: #ff6b6b;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0;
    font-family: 'Space Grotesk', system-ui, sans-serif;
    color: var(--text);
    background: radial-gradient(1200px 600px at 10% -20%, #1f4a3d, transparent),
                radial-gradient(1000px 800px at 100% 0%, #1a3f35, transparent),
                var(--bg);
  }}
  header {{
    padding: 28px 28px 12px;
    border-bottom: 1px solid rgba(255,255,255,0.08);
  }}
  header h1 {{
    margin: 0;
    font-size: 28px;
    letter-spacing: 0.5px;
  }}
  header p {{
    margin: 6px 0 0;
    color: var(--muted);
    font-family: 'IBM Plex Mono', ui-monospace, monospace;
    font-size: 12px;
  }}
  .wrap {{ padding: 24px; }}
  .card {{
    background: var(--card);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 14px;
    padding: 16px;
    box-shadow: 0 18px 40px rgba(0,0,0,0.25);
  }}
  table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 14px;
  }}
  th, td {{
    padding: 10px 8px;
    border-bottom: 1px solid rgba(255,255,255,0.08);
  }}
  th {{
    text-align: left;
    font-size: 12px;
    text-transform: uppercase;
    color: var(--muted);
    letter-spacing: 0.08em;
  }}
  td.name {{ font-weight: 600; }}
  tr.idle td {{ color: rgba(230, 243, 238, 0.62); }}
  tr.idle td.name {{ color: rgba(230, 243, 238, 0.82); }}
  a {{ color: var(--accent); text-decoration: none; }}
  a:hover {{ text-decoration: underline; }}
  .lab-note {{
    margin-bottom: 18px;
    padding: 14px 16px;
    border: 1px solid rgba(255, 255, 255, 0.10);
    border-radius: 12px;
    background: rgba(255, 107, 107, 0.08);
    color: var(--text);
    font-family: 'IBM Plex Mono', ui-monospace, monospace;
    font-size: 12px;
    line-height: 1.7;
  }}
  .lab-note strong {{ color: var(--warn); }}
  .disclaimer {{
    margin-top: 18px;
    color: var(--muted);
    font-family: 'IBM Plex Mono', ui-monospace, monospace;
    font-size: 11px;
    line-height: 1.7;
  }}
  @media (max-width: 760px) {{
    table, thead, tbody, th, td, tr {{ display: block; }}
    tr {{ margin-bottom: 14px; }}
    th {{ border-bottom: none; }}
    td {{ border-bottom: none; padding: 6px 0; }}
  }}
</style>
</head>
<body>
  <header>
    <h1>Crazy Algos — Portfolio Overview</h1>
    <p>Lab started: {lab_start} · Last updated: {date.today()}</p>
  </header>
  <div class="wrap">
    <div class="lab-note">
      <strong>{idle_count} of {len(summaries)} crazy algos are currently idle.</strong>
      Idle means the algo is running but has no recorded trades in its current state history.
      That is not a crash; it means the trigger has not fired yet, the adapter returned no usable signal,
      or the strategy is still waiting for live evidence.
      Active algos: {active_count}.
    </div>
    <div class="card">
      <table>
        <thead>
          <tr>
            <th>Strategy</th>
            <th>Equity</th>
            <th>Net P&L</th>
            <th>Sharpe</th>
            <th>Max DD</th>
            <th>Signal</th>
            <th>Trades</th>
            <th>Status</th>
            <th>Dashboard</th>
          </tr>
        </thead>
        <tbody>
          {rows}
        </tbody>
      </table>
    </div>
    <div class="disclaimer">
      Not investment advice. This is experimental research. Past signal performance does not predict future results.<br>
      Always do your own research. Paper-traded only &mdash; no real money at risk.
    </div>
  </div>
</body>
</html>"""

    with open(CRAZY_COMBINED_DASHBOARD, "w") as f:
        f.write(html)
