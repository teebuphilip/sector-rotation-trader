#!/usr/bin/env python3
"""
Generate static public HTML pages from docs/data/public/ contract.

Generates:
  docs/leaderboard.html   — sector heatmap + top-10 leaderboard + ticker lookup
  docs/landing.html       — landing/CTA with pricing section + rolling 30D winners
  docs/premium.html       — premium teaser page for the July paid launch
"""
from __future__ import annotations
import json
import html
import sys
from pathlib import Path
from datetime import datetime

REPO = Path(__file__).parent.parent
PUBLIC = REPO / "docs" / "data" / "public"

SPECIAL = {
    "biscotti":  {"emoji": "\U0001f43e", "row_class": "row-biscotti",  "tip": "Named after Biscotti (2008\u20132026) \u2014 17.75 years of unconditional loyalty"},
    "baileymol": {"emoji": "\u26a1",      "row_class": "row-baileymol", "tip": "The Chaos Monger \u2014 thrives on volatility spikes"},
}

ETF_ORDER = ["XLK", "XLF", "XLV", "XLY", "XLI", "XLC", "XLP", "XLE", "XLB", "XLRE", "XLU"]

FREE_ROWS = 10


def _load(name: str) -> dict:
    p = PUBLIC / name
    if p.exists():
        return json.loads(p.read_text())
    return {}


def _e(s) -> str:
    return html.escape(str(s)) if s is not None else ""


def _fmt(n) -> str:
    if n is None:
        return "n/a"
    try:
        f = float(n)
        return ("+" if f > 0 else "") + f"{f:.2f}%"
    except (TypeError, ValueError):
        return "n/a"


def _ret_class(n) -> str:
    try:
        f = float(n)
        if f > 0:
            return "return-pos"
        if f < 0:
            return "return-neg"
    except (TypeError, ValueError):
        pass
    return "return-zero"


def _get_special(algo_id: str):
    for key, spec in SPECIAL.items():
        if key in str(algo_id):
            return spec
    return None


def _sector_heatmap_html(sector_summary: dict) -> str:
    parts = []
    for etf in ETF_ORDER:
        s = sector_summary.get(etf)
        if not s:
            continue
        label = _e(s.get("composite_label", "MIXED"))
        parts.append(
            f'<div class="sector-tile">'
            f'<div class="sector-tooltip">Composite: {_e(s.get("composite","?"))} '
            f'&bull; {_e(s.get("bullish_pct","?"))}% bullish</div>'
            f'<div class="etf">{_e(etf)}</div>'
            f'<div class="sector-name">{_e(s.get("sector",""))}</div>'
            f'<span class="verdict verdict-{label}">{label}</span>'
            f'</div>'
        )
    return "\n".join(parts) if parts else '<div class="loading">No sector data</div>'


def _comparator_badges_html(payload: dict | None) -> str:
    if not isinstance(payload, dict):
        return '<span class="comparator-na">n/a</span>'
    signals = payload.get("signals") or {}
    if not isinstance(signals, dict) or not signals:
        return '<span class="comparator-na">n/a</span>'
    label_map = {"momentum_5d": "5D", "momentum_20d": "20D"}
    badges = []
    for key in ("momentum_5d", "momentum_20d"):
        row = signals.get(key)
        if not isinstance(row, dict):
            continue
        direction = str(row.get("direction") or "NEUTRAL")
        cls = "comp-neutral"
        if direction == "UP":
            cls = "comp-up"
        elif direction == "DOWN":
            cls = "comp-down"
        badges.append(f'<span class="comp-badge {cls}">{label_map.get(key, key)} {direction}</span>')
    if not badges:
        return '<span class="comparator-na">n/a</span>'
    etf = payload.get("primary_etf")
    title = f'Current comparator directions for {etf}' if etf else 'Current comparator directions'
    return f'<div class="comparator-pack" title="{_e(title)}">' + ''.join(badges) + '</div>'


def _leaderboard_rows_html(ranked_algos: list[tuple[int, dict]], paywall: bool = True) -> str:
    rows = []
    for rank, a in ranked_algos:
        is_free = (rank <= FREE_ROWS) if paywall else True
        spec = _get_special(str(a.get("algo_id", "")))
        row_cls = spec["row_class"] if spec else ""
        paywall_cls = "" if is_free else " paywall-row"

        emoji = f'<span class="algo-emoji">{spec["emoji"]}</span>' if spec else ""
        if spec:
            name_html = (
                f'<span class="name-tooltip"><span class="algo-name">{emoji}{_e(a.get("name",""))}</span>'
                f'<span class="tip">{_e(spec["tip"])}</span></span>'
            )
        else:
            name_html = f'<span class="algo-name">{_e(a.get("name",""))}</span>'

        ytd = a.get("ytd_pct")
        spy = a.get("spy_pct")
        try:
            diff = float(ytd) - float(spy)
            diff_cls = "vs-spy-pos" if diff >= 0 else "vs-spy-neg"
            diff_str = ("+" if diff >= 0 else "") + f"{diff:.2f}%"
        except (TypeError, ValueError):
            diff_cls = "vs-spy-neg"
            diff_str = "n/a"

        status_html = (
            '<span class="status-beat">BEATING SPY</span>'
            if a.get("beat_spy")
            else '<span class="status-lag">LAGGING</span>'
        )
        algo_type = str(a.get("algo_type", ""))
        public_algo_type = "alternative" if algo_type == "crazy" else algo_type

        comparator_html = _comparator_badges_html(a.get('comparator'))

        rows.append(
            f'<tr class="{row_cls}{paywall_cls}">'
            f'<td class="rank">{rank}</td>'
            f'<td>{name_html}</td>'
            f'<td><span class="algo-type-badge">{_e(public_algo_type)}</span></td>'
            f'<td class="{_ret_class(ytd)}">{_fmt(ytd)}</td>'
            f'<td class="vs-spy {diff_cls}">{diff_str}</td>'
            f'<td>{comparator_html}</td>'
            f'<td class="days">{_e(a.get("days_running",""))}d</td>'
            f'<td>{status_html}</td>'
            f'</tr>'
        )

    if paywall:
        rows.append(
            '<tr class="paywall-cta-row">'
            '<td colspan="8"><a href="landing.html#waitlist">'
            '&rarr; Get the weekly lab notes</a></td>'
            '</tr>'
        )
    return "\n".join(rows)


def _is_zero_trade_algo(algo: dict) -> bool:
    try:
        return float(algo.get("ytd_pct") or 0) == 0.0
    except (TypeError, ValueError):
        return False


def _zero_trade_reason(algo: dict) -> str:
    evidence = str(algo.get("evidence_class") or "")
    status = str(algo.get("status") or "")
    if evidence == "needs_history":
        return "Needs more history before the signal can trade honestly."
    if evidence == "pending_seed":
        return "Seed/build pipeline finished late; still waiting on first live receipts."
    if status == "parked":
        return "Temporarily parked while the input or deployment path gets cleaned up."
    if status == "sandbox":
        return "Still in sandbox: visible on purpose, but not yet earning live receipts."
    if evidence == "v1_backtested":
        return "Rule exists, but live trading has not fired yet."
    return "Still visible, but no live trade has fired yet."


def _site_links() -> str:
    return (
        '<a href="landing.html">Home</a> &middot; '
        '<a href="leaderboard.html">Leaderboard</a> &middot; '
        '<a href="families.html">Families</a> &middot; '
        '<a href="daily.html">Daily Report</a> &middot; '
        '<a href="premium.html">Premium Preview</a> &middot; '
        '<a href="blog/index.html">Blog</a> &middot; '
        '<a href="legal.html">Legal</a>'
    )


def _pulse_block_html(daily: dict, total=None, beating=None) -> str:
    counts = daily.get("counts") or {}
    total = total if total is not None else counts.get("total", 0)
    top = (daily.get("top_live_ytd") or [])[:1]
    leader_text = ""
    if top:
        t = top[0]
        name = t.get("name", "")
        ytd = t.get("ytd_pct")
        try:
            r = float(ytd)
            sign = "+" if r >= 0 else ""
            leader_text = f"{name}: {sign}{r:.2f}% YTD"
        except (TypeError, ValueError):
            leader_text = name

    bullish = (daily.get("top_bullish_etfs") or [])[:1]
    bearish = (daily.get("top_bearish_etfs") or [])[:1]
    bullish_text = f"{bullish[0]} strongest consensus" if bullish else ""
    bearish_text = f"{bearish[0]} weakest consensus" if bearish else ""

    run_date = daily.get("run_date", "")

    items = []
    if leader_text:
        items.append(f'<span class="pulse-item">{_e(leader_text)}</span>')
    if beating is not None:
        items.append(f'<span class="pulse-item"><strong>{_e(beating)}</strong> of {_e(total)} beating SPY</span>')
    elif total:
        items.append(f'<span class="pulse-item"><strong>{_e(total)}</strong> algos tracked</span>')
    if bullish_text:
        items.append(f'<span class="pulse-item">{_e(bullish_text)}</span>')
    if bearish_text:
        items.append(f'<span class="pulse-item">{_e(bearish_text)}</span>')
    if run_date:
        items.append(f'<span class="pulse-item pulse-date">{_e(run_date)}</span>')

    inner = ' <span class="pulse-sep">&middot;</span> '.join(items)
    return f"""<div class="pulse">
  <div class="wrap">
    <span class="pulse-label">TODAY IN THE LAB</span>
    <div class="pulse-items">{inner}</div>
  </div>
</div>"""


def _footer_html(generated_at: str, run_date: str, label: str = "Updated nightly at 6:30 PM ET") -> str:
    return f"""
<footer>
  <div class="wrap">
    <div style="text-align:center;margin-top:8px;">{_site_links()}</div>
    <div style="width:100%;max-width:520px;height:1px;margin:14px auto 14px;background:rgba(255,255,255,0.10);"></div>
    <div style="display:block;width:100%;text-align:center;font-size:11px;font-style:italic;letter-spacing:0.2px;color:rgba(255,255,255,0.58);margin:0 auto 10px;">
      StockArithm powered by R&amp;B AlgoLabs, LLC.
    </div>
    <div style="text-align:center;font-size:11px;font-style:italic;letter-spacing:0.2px;color:rgba(255,255,255,0.50);margin-bottom:14px;">Last updated: {_e(generated_at or run_date)}</div>
    <div style="margin-top:12px;max-width:920px;margin-left:auto;margin-right:auto;text-align:center;font-size:11px;font-style:italic;letter-spacing:0.2px;color:rgba(255,255,255,0.58);">
      <strong>Signal Lab Notice:</strong> Experimental research only. Signals can and will fail. Do not interpret any signal as a recommendation.<br>
      <strong>Performance Disclosure:</strong> Leaderboards are model/simulation outputs and may not reflect slippage, fees, liquidity, execution delays, or market impact.<br>
      <strong>Data Disclaimer:</strong> Third-party data may be incomplete, delayed, inaccurate, or revised. Use at your own risk.<br>
      <strong>Not financial advice:</strong> Do your own research. You are responsible for your own decisions. Paper-traded only &mdash; no real money at risk.
    </div>
    <div style="margin:20px auto 0;padding-top:16px;border-top:1px solid var(--border);max-width:720px;text-align:center;font-size:10px;font-style:italic;letter-spacing:0.15px;color:rgba(255,255,255,0.42);">
      In loving memory of Biscotti (2008&ndash;2026). Good boy. Best algo. &hearts;
    </div>
  </div>
</footer>"""


CSS = """
  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=IBM+Plex+Mono:wght@400;600&display=swap');
  :root {
    --bg: #0a0a0a;
    --bg2: #111;
    --card: #161616;
    --border: rgba(255,255,255,0.08);
    --accent: #19d38f;
    --accent-dim: #12a06b;
    --red: #ef4444;
    --red-dim: #991b1b;
    --yellow: #eab308;
    --gold: #d4a017;
    --purple: #a855f7;
    --muted: #888;
    --text: #e8e8e8;
    --mono: 'IBM Plex Mono', ui-monospace, monospace;
    --sans: 'Space Grotesk', system-ui, sans-serif;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: var(--sans); color: var(--text); background: var(--bg); line-height: 1.5; -webkit-font-smoothing: antialiased; }
  .hero { text-align: center; padding: 60px 24px 48px; background: radial-gradient(800px 400px at 50% 0%, rgba(25,211,143,0.06), transparent), var(--bg); border-bottom: 1px solid var(--border); }
  .hero-badge { display: inline-block; font-family: var(--mono); font-size: 12px; color: var(--accent); border: 1px solid var(--accent-dim); border-radius: 20px; padding: 4px 14px; margin-bottom: 16px; letter-spacing: 0.5px; }
  .hero h1 { font-size: clamp(28px, 5vw, 48px); font-weight: 700; letter-spacing: -0.5px; margin-bottom: 12px; }
  .hero h1 span { color: var(--accent); }
  .hero-sub { font-family: var(--mono); font-size: 14px; color: var(--muted); margin-bottom: 8px; }
  .hero-stats { display: flex; justify-content: center; gap: 32px; margin: 24px 0; flex-wrap: wrap; }
  .hero-stat { text-align: center; }
  .hero-stat .num { font-size: 32px; font-weight: 700; font-family: var(--mono); color: var(--accent); }
  .hero-stat .label { font-size: 12px; color: var(--muted); text-transform: uppercase; letter-spacing: 1px; }
  .cta { display: inline-block; margin-top: 20px; padding: 12px 32px; background: var(--accent); color: #000; font-weight: 700; font-size: 15px; border: none; border-radius: 8px; cursor: pointer; text-decoration: none; transition: background 0.2s; }
  .cta:hover { background: #1ee89e; }
  .cta-sub { display: block; font-size: 12px; color: var(--muted); margin-top: 8px; }
  .hero-strip { display: flex; justify-content: center; gap: 10px; flex-wrap: wrap; }
  .pill { font-size: 12px; color: var(--muted); border: 1px solid rgba(255,255,255,0.08); border-radius: 999px; padding: 6px 10px; }
  .pill a { color: inherit; text-decoration: none; }
  .pill a:hover { text-decoration: underline; }
  .wrap { max-width: 1100px; margin: 0 auto; padding: 0 20px; }
  section { padding: 48px 0; }
  section + section { border-top: 1px solid var(--border); }
  .section-title { font-size: 22px; font-weight: 700; margin-bottom: 6px; }
  .section-sub { font-size: 13px; color: var(--muted); margin-bottom: 24px; }
  .heatmap { display: grid; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); gap: 10px; }
  .sector-tile { background: var(--card); border: 1px solid var(--border); border-radius: 10px; padding: 14px; text-align: center; cursor: default; transition: transform 0.15s, border-color 0.15s; position: relative; }
  .sector-tile:hover { transform: translateY(-2px); border-color: rgba(255,255,255,0.15); }
  .sector-tile .etf { font-family: var(--mono); font-size: 16px; font-weight: 700; }
  .sector-tile .sector-name { font-size: 11px; color: var(--muted); margin: 4px 0 8px; }
  .sector-tile .verdict { font-family: var(--mono); font-size: 11px; font-weight: 600; padding: 3px 10px; border-radius: 4px; display: inline-block; letter-spacing: 0.5px; }
  .verdict-BULLISH { background: rgba(25,211,143,0.15); color: var(--accent); }
  .verdict-BEARISH { background: rgba(239,68,68,0.15); color: var(--red); }
  .verdict-MIXED { background: rgba(234,179,8,0.15); color: var(--yellow); }
  .sector-tooltip { display: none; position: absolute; bottom: calc(100% + 8px); left: 50%; transform: translateX(-50%); background: #222; border: 1px solid var(--border); border-radius: 6px; padding: 8px 12px; font-family: var(--mono); font-size: 11px; color: var(--muted); white-space: nowrap; z-index: 10; pointer-events: none; }
  .sector-tile:hover .sector-tooltip { display: block; }
  .table-wrap { overflow-x: auto; border-radius: 10px; border: 1px solid var(--border); background: var(--card); }
  table { width: 100%; border-collapse: collapse; font-size: 14px; }
  thead th { text-align: left; padding: 12px 16px; font-size: 11px; text-transform: uppercase; letter-spacing: 1px; color: var(--muted); border-bottom: 1px solid var(--border); white-space: nowrap; font-weight: 600; }
  tbody td { padding: 12px 16px; border-bottom: 1px solid rgba(255,255,255,0.04); white-space: nowrap; }
  tbody tr:last-child td { border-bottom: none; }
  tbody tr:hover { background: rgba(255,255,255,0.02); }
  .rank { color: var(--muted); font-family: var(--mono); width: 40px; }
  .algo-name { font-weight: 600; display: flex; align-items: center; gap: 8px; }
  .algo-emoji { font-size: 18px; }
  .algo-type-badge { font-family: var(--mono); font-size: 10px; padding: 2px 6px; border-radius: 3px; background: rgba(255,255,255,0.06); color: var(--muted); text-transform: uppercase; letter-spacing: 0.5px; }
  .return-pos { color: var(--accent); font-family: var(--mono); font-weight: 600; }
  .return-neg { color: var(--red); font-family: var(--mono); font-weight: 600; }
  .return-zero { color: var(--muted); font-family: var(--mono); }
  .vs-spy { font-family: var(--mono); font-size: 12px; }
  .vs-spy-pos { color: var(--accent); }
  .vs-spy-neg { color: var(--red); }
  .days { font-family: var(--mono); color: var(--muted); }
  .status-beat { font-family: var(--mono); font-size: 11px; color: var(--accent); background: rgba(25,211,143,0.1); padding: 3px 8px; border-radius: 4px; letter-spacing: 0.3px; }
  .status-lag { font-family: var(--mono); font-size: 11px; color: var(--red); background: rgba(239,68,68,0.1); padding: 3px 8px; border-radius: 4px; letter-spacing: 0.3px; }
  .comparator-pack { display: flex; gap: 6px; flex-wrap: wrap; }
  .comp-badge { font-family: var(--mono); font-size: 10px; padding: 3px 6px; border-radius: 4px; letter-spacing: 0.3px; border: 1px solid rgba(255,255,255,0.08); }
  .comp-up { color: var(--accent); background: rgba(25,211,143,0.1); }
  .comp-down { color: var(--red); background: rgba(239,68,68,0.1); }
  .comp-neutral { color: var(--yellow); background: rgba(234,179,8,0.12); }
  .comparator-na { color: var(--muted); font-family: var(--mono); font-size: 11px; }
  .row-biscotti { border-left: 3px solid var(--gold) !important; }
  .row-baileymol { border-left: 3px solid var(--purple) !important; }
  .name-tooltip { position: relative; cursor: help; }
  .name-tooltip .tip { display: none; position: absolute; bottom: calc(100% + 6px); left: 0; background: #222; border: 1px solid var(--border); border-radius: 6px; padding: 8px 12px; font-size: 12px; font-weight: 400; color: var(--muted); white-space: nowrap; z-index: 20; pointer-events: none; }
  .name-tooltip:hover .tip { display: block; }
  .paywall-row td { color: rgba(255,255,255,0.15) !important; user-select: none; pointer-events: none; }
  .paywall-row .algo-name { filter: blur(4px); }
  .paywall-cta-row td { text-align: center; padding: 16px; border-bottom: none; }
  .paywall-cta-row a { color: var(--accent); font-weight: 600; text-decoration: none; font-size: 14px; }
  .paywall-cta-row a:hover { text-decoration: underline; }
  .ticker-check { max-width: 480px; }
  .ticker-input-wrap { display: flex; gap: 10px; margin-bottom: 16px; }
  .ticker-input { flex: 1; padding: 12px 16px; font-family: var(--mono); font-size: 16px; background: var(--card); border: 1px solid var(--border); border-radius: 8px; color: var(--text); outline: none; text-transform: uppercase; }
  .ticker-input::placeholder { color: rgba(255,255,255,0.2); }
  .ticker-input:focus { border-color: var(--accent-dim); }
  .ticker-btn { padding: 12px 20px; background: var(--accent); color: #000; font-weight: 700; font-size: 14px; border: none; border-radius: 8px; cursor: pointer; font-family: var(--sans); transition: background 0.2s; }
  .ticker-btn:hover { background: #1ee89e; }
  .ticker-result { background: var(--card); border: 1px solid var(--border); border-radius: 10px; padding: 20px; display: none; }
  .ticker-result.show { display: block; }
  .ticker-result .tr-ticker { font-family: var(--mono); font-size: 24px; font-weight: 700; }
  .ticker-result .tr-sector { font-size: 13px; color: var(--muted); margin: 4px 0 12px; }
  .ticker-result .tr-verdict { font-family: var(--mono); font-size: 14px; font-weight: 600; padding: 6px 14px; border-radius: 6px; display: inline-block; }
  .ticker-result .tr-unlock { display: block; margin-top: 16px; font-size: 13px; color: var(--muted); }
  .ticker-result .tr-unlock a { color: var(--accent); text-decoration: none; }
  .ticker-result .tr-unlock a:hover { text-decoration: underline; }
  .ticker-error { color: var(--red); font-family: var(--mono); font-size: 13px; display: none; }
  .ticker-error.show { display: block; }
  footer { border-top: 1px solid var(--border); padding: 32px 20px; text-align: center; font-size: 12px; color: var(--muted); line-height: 1.8; }
  footer a { color: var(--accent-dim); text-decoration: none; }
  footer a:hover { text-decoration: underline; }
  .rank-note { border: 1px solid var(--border); border-radius: 12px; background: rgba(255,255,255,0.035); padding: 14px 16px; margin: 14px 0 18px; color: var(--muted); font-size: 13px; line-height: 1.65; }
  .rank-note strong { color: var(--text); }
  .rank-note code { font-family: var(--mono); color: var(--gold); background: rgba(255,204,102,0.08); padding: 1px 5px; border-radius: 4px; }
  .pulse { background: rgba(25,211,143,0.04); border-top: 1px solid rgba(25,211,143,0.14); border-bottom: 1px solid rgba(25,211,143,0.14); padding: 12px 0; }
  .pulse .wrap { display: flex; align-items: center; gap: 16px; flex-wrap: wrap; }
  .pulse-label { font-family: var(--mono); font-size: 10px; color: var(--accent); letter-spacing: 1.5px; text-transform: uppercase; white-space: nowrap; flex-shrink: 0; }
  .pulse-items { display: flex; gap: 8px; flex-wrap: wrap; align-items: center; }
  .pulse-item { font-family: var(--mono); font-size: 13px; color: var(--text); }
  .pulse-sep { color: var(--muted); font-size: 13px; }
  .pulse-date { color: var(--muted); font-size: 11px; }
  .cred-strip { display: flex; justify-content: center; gap: 6px; align-items: center; flex-wrap: wrap; margin-top: 12px; padding-top: 12px; border-top: 1px solid rgba(255,255,255,0.06); }
  .cred-strip .cred-item { font-family: var(--mono); font-size: 11px; color: var(--muted); }
  .cred-strip .cred-dot { color: rgba(255,255,255,0.2); font-size: 11px; }
  @media (max-width: 600px) {
    .hero { padding: 40px 16px 32px; }
    .hero-stats { gap: 20px; }
    .hero-stat .num { font-size: 24px; }
    table { font-size: 13px; }
    thead th, tbody td { padding: 10px 10px; }
    .heatmap { grid-template-columns: repeat(auto-fill, minmax(110px, 1fr)); gap: 8px; }
    .sector-tile { padding: 10px; }
  }
"""

REPORT_CSS = CSS.replace(
    """  .paywall-row td { color: rgba(255,255,255,0.15) !important; user-select: none; pointer-events: none; }
  .paywall-row .algo-name { filter: blur(4px); }
  .paywall-cta-row td { text-align: center; padding: 16px; border-bottom: none; }
  .paywall-cta-row a { color: var(--accent); font-weight: 600; text-decoration: none; font-size: 14px; }
  .paywall-cta-row a:hover { text-decoration: underline; }
""",
    "",
)


def _pretty_label(value: str) -> str:
    return str(value).replace("_", " ").title()


def _status_mix_html(by_status: dict) -> str:
    items = []
    for status, count in sorted((by_status or {}).items()):
        items.append(
            f'<span class="algo-type-badge">{_e(_pretty_label(status))}: {_e(count)}</span>'
        )
    return " ".join(items) if items else '<span class="algo-type-badge">No status data</span>'


def build_leaderboard(daily: dict, leaderboard: dict) -> str:
    algos = leaderboard.get("algos", [])
    signal_count = daily.get("signal_count") or len(algos)
    counts = daily.get("counts", {})
    beating = sum(1 for a in algos if a.get("beat_spy"))
    total = counts.get("total") or len(algos)
    generated_at = daily.get("generated_at", "")
    run_date = daily.get("run_date", "")

    sector_html = _sector_heatmap_html(daily.get("sector_summary") or {})
    ranked_algos = list(enumerate(algos, start=1))
    active_ranked = [(rank, algo) for rank, algo in ranked_algos if not _is_zero_trade_algo(algo)]
    zero_ranked = [(rank, algo) for rank, algo in ranked_algos if _is_zero_trade_algo(algo)]
    table_rows = _leaderboard_rows_html(active_ranked)
    zero_rows = "\n".join(
        f"<tr>"
        f"<td class=\"rank\">{rank}</td>"
        f"<td>{_e(algo.get('name', ''))}</td>"
        f"<td><span class=\"algo-type-badge\">{_e('alternative' if str(algo.get('algo_type', '')) == 'crazy' else algo.get('algo_type', ''))}</span></td>"
        f"<td class=\"days\">{_e(algo.get('status', ''))}</td>"
        f"<td class=\"days\">{_e(algo.get('evidence_class', ''))}</td>"
        f"<td>{_e(_zero_trade_reason(algo))}</td>"
        f"</tr>"
        for rank, algo in zero_ranked
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>StockArithm \u2014 Live Signal Leaderboard</title>
<meta name="description" content="{_e(signal_count)} experimental trading algorithms running live. Track performance against SPY." />
<style>{CSS}</style>
</head>
<body>

<div class="hero">
  <div class="hero-badge">LIVE EXPERIMENT</div>
  <h1><span>{_e(signal_count)}</span> signals running</h1>
  <p class="hero-sub">We run alternative data signals in public. Most fail. We track every one against SPY.</p>
  <div class="hero-stats">
    <div class="hero-stat">
      <div class="num">{_e(total)}</div>
      <div class="label">Total Algos</div>
    </div>
    <div class="hero-stat">
      <div class="num">{_e(beating)}/{_e(total)}</div>
      <div class="label">Beating SPY</div>
    </div>
    <div class="hero-stat">
      <div class="num">11</div>
      <div class="label">Sectors Tracked</div>
    </div>
  </div>
  <a class="cta" href="landing.html#waitlist">Get the weekly lab notes</a>
  <span class="cta-sub">See which alternative signals are surviving, which are dead, and which are still unresolved.</span>
  <div class="cred-strip">
    <span class="cred-item">{_e(total)} signals tracked</span>
    <span class="cred-dot">&middot;</span>
    <span class="cred-item">failures stay visible</span>
    <span class="cred-dot">&middot;</span>
    <span class="cred-item">live since April 6, 2026</span>
  </div>
  <div class="hero-strip" style="justify-content:center; margin-top:12px;">
    <span class="pill">Start at <a href="landing.html" style="color:inherit;">Home</a></span>
    <span class="pill">Then <a href="families.html" style="color:inherit;">Families</a></span>
    <span class="pill">Then <a href="daily.html" style="color:inherit;">Daily Report</a></span>
    <span class="pill">Then <a href="blog/index.html" style="color:inherit;">Blog</a></span>
  </div>
</div>

{_pulse_block_html(daily, total, beating)}

<section>
  <div class="wrap">
    <h2 class="section-title">Sector Heatmap</h2>
    <p class="section-sub">Composite signal across all algorithms. Updated nightly.</p>
    <div class="heatmap">
{sector_html}
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2 class="section-title">Public Leaderboard</h2>
    <p class="section-sub">A stripped public view of the lab. The rows below are the names that have actually moved. The zero-trade names are collapsed underneath with reasons.</p>
    <div class="rank-note">
      <strong>How to read this:</strong>
      <code>Force rank</code> is the full-window, since-seed paper-traded ranking.
      <code>Rolling 30D</code> is recent momentum. A signal can look great over 30 days
      and still rank poorly over the full window, or the other way around.
      We show both because hiding that split would be dishonest.
      <code>Comparators</code> shows the current 5-day and 20-day momentum direction on the algo's primary sector ETF when that mapping is clean enough to show.
      Some signals are backtested under strict V1 rules. Others are live-only because the historical data is not clean enough to backfill honestly.
    </div>
    <div class="rank-note">
      <strong>Why comparators are here:</strong> Simple momentum baselines are the null hypothesis.
      If an alternative signal is useful, it should sometimes add information beyond raw price trend.
      These badges are context, not a final scorecard.
    </div>
    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th>#</th><th>Algorithm</th><th>Type</th>
            <th>Return</th><th>vs SPY</th><th>Comparators</th><th>Days</th><th>Status</th>
          </tr>
        </thead>
        <tbody>
{table_rows}
        </tbody>
      </table>
    </div>
    <details style="margin-top:16px;" class="card">
      <summary style="cursor:pointer; font-weight:700;">{_e(len(zero_ranked))} algos still flat or waiting on first live trade</summary>
      <p class="section-sub" style="margin-top:12px; margin-bottom:16px;">
        These are not hidden because that would be dishonest. Most are still in sandbox, still need more history, or have not fired a live trade yet.
      </p>
      <div class="table-wrap">
        <table>
          <thead>
            <tr>
              <th>#</th><th>Algorithm</th><th>Type</th><th>Status</th><th>Evidence</th><th>Why it is still flat</th>
            </tr>
          </thead>
          <tbody>
{zero_rows}
          </tbody>
        </table>
      </div>
    </details>
  </div>
</section>

<section>
  <div class="wrap">
    <h2 class="section-title">Ticker Quick Check</h2>
    <p class="section-sub">Look up any tracked stock to see the public composite signal. Free preview only.</p>
    <div class="ticker-check">
      <div class="ticker-input-wrap">
        <input type="text" class="ticker-input" id="ticker-input" placeholder="NVDA" maxlength="6" autocomplete="off" />
        <button class="ticker-btn" onclick="checkTicker()">Check</button>
      </div>
      <div class="ticker-error" id="ticker-error"></div>
      <div class="ticker-result" id="ticker-result">
        <div class="tr-ticker" id="tr-ticker"></div>
        <div class="tr-sector" id="tr-sector"></div>
        <div class="tr-verdict" id="tr-verdict"></div>
        <span class="tr-unlock">Want the full breakdown later? <a href="landing.html#waitlist">Get the weekly lab notes</a></span>
      </div>
    </div>
  </div>
</section>

{_footer_html(generated_at, run_date)}

<script>
(function() {{
  var SIGNALS = 'data/public/signals/';
  function escHtml(s) {{ var d = document.createElement('div'); d.textContent = s; return d.innerHTML; }}
  window.checkTicker = function() {{
    var input = document.getElementById('ticker-input');
    var ticker = input.value.trim().toUpperCase();
    var result = document.getElementById('ticker-result');
    var error = document.getElementById('ticker-error');
    result.classList.remove('show');
    error.classList.remove('show');
    if (!ticker) {{ error.textContent = 'Enter a ticker symbol.'; error.classList.add('show'); return; }}
    fetch(SIGNALS + ticker + '.json')
      .then(function(r) {{ if (!r.ok) throw new Error('not found'); return r.json(); }})
      .then(function(d) {{
        document.getElementById('tr-ticker').textContent = d.ticker;
        document.getElementById('tr-sector').textContent = (d.sector || '') + ' \u2022 ' + (d.sector_etf || '');
        var v = document.getElementById('tr-verdict');
        v.textContent = d.composite_label;
        v.className = 'tr-verdict verdict-' + d.composite_label;
        result.classList.add('show');
      }})
      .catch(function() {{
        error.textContent = ticker + ' not found in public signal data.';
        error.classList.add('show');
      }});
  }};
  document.getElementById('ticker-input').addEventListener('keydown', function(e) {{
    if (e.key === 'Enter') window.checkTicker();
  }});
}})();
</script>

</body>
</html>"""


LANDING_CSS = """
  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=IBM+Plex+Mono:wght@400;600&display=swap');
  :root {
    --bg: #0d1412;
    --bg-2: #13231f;
    --card: #182b26;
    --accent: #19d38f;
    --muted: #9ab0a7;
    --text: #ecf5f2;
  }
  * { box-sizing: border-box; }
  body { margin: 0; font-family: 'Space Grotesk', system-ui, sans-serif; color: var(--text); background: radial-gradient(1000px 600px at 15% -10%, #1e3f35, transparent), radial-gradient(900px 500px at 90% 0%, #1b352f, transparent), var(--bg); }
  header { padding: 28px; border-bottom: 1px solid rgba(255,255,255,0.08); }
  header h1 { margin: 0; font-size: 30px; letter-spacing: 0.5px; }
  header p { margin: 6px 0 0; color: var(--muted); font-family: 'IBM Plex Mono', ui-monospace, monospace; font-size: 12px; }
  .wrap { padding: 24px; }
  .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px; }
  .card { background: var(--card); border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 16px; box-shadow: 0 14px 30px rgba(0,0,0,0.22); }
  .card h2 { margin: 0 0 8px; font-size: 18px; }
  .card p { margin: 0 0 12px; color: var(--muted); font-size: 14px; line-height: 1.4; }
  .cta { display: inline-block; padding: 10px 12px; border-radius: 8px; border: 1px solid var(--accent); color: var(--accent); text-decoration: none; font-weight: 600; font-size: 13px; }
  .cta:hover { background: rgba(25, 211, 143, 0.1); }
  .winners h3 { margin: 0 0 8px; font-size: 16px; }
  .winners ul { margin: 0; padding: 0; list-style: none; }
  .winners li { padding: 6px 0; border-bottom: 1px solid rgba(255,255,255,0.06); font-size: 14px; }
  .winners li:last-child { border-bottom: none; }
  .muted { color: var(--muted); font-size: 12px; }
  .ret-pos { color: #19d38f; font-family: 'IBM Plex Mono', monospace; }
  .ret-neg { color: #ef4444; font-family: 'IBM Plex Mono', monospace; }
  .waitlist { margin-top: 16px; border: 1px solid rgba(25, 211, 143, 0.28); }
  .waitlist-form { display: grid; grid-template-columns: minmax(0, 1fr) auto; gap: 8px; margin-top: 12px; }
  .waitlist-form input { min-width: 0; border: 1px solid rgba(255,255,255,0.14); border-radius: 8px; background: #0f1c18; color: var(--text); padding: 10px 12px; font: inherit; font-size: 14px; }
  .waitlist-form button { border: 1px solid var(--accent); border-radius: 8px; background: transparent; color: var(--accent); padding: 10px 12px; font: inherit; font-size: 13px; font-weight: 700; cursor: pointer; }
  .waitlist-form button:hover { background: rgba(25, 211, 143, 0.1); }
  .notice { margin-top: 10px; color: var(--muted); font-size: 12px; line-height: 1.4; }
  .hero-actions { display: flex; gap: 10px; flex-wrap: wrap; margin-top: 14px; }
  .hero-actions .cta { padding: 10px 14px; }
  .cta-primary { background: var(--accent); color: #062018; font-weight: 700; }
  .cta-primary:hover { background: #33e3a3; }
  .hero-strip { margin-top: 16px; display: flex; gap: 10px; flex-wrap: wrap; }
  .pill { font-size: 12px; color: var(--muted); border: 1px solid rgba(255,255,255,0.08); border-radius: 999px; padding: 6px 10px; }
  @media (max-width: 560px) { .waitlist-form { grid-template-columns: 1fr; } }
"""


def _winners_li(entries: list) -> str:
    if not entries:
        return '<li class="muted">No data yet</li>'
    parts = []
    for i, w in enumerate(entries[:3]):
        ret = w.get("ret_30d_pct")
        try:
            r = float(ret)
            cls = "ret-pos" if r >= 0 else "ret-neg"
            ret_str = f'<span class="{cls}">' + ("+" if r >= 0 else "") + f"{r:.2f}%</span>"
        except (TypeError, ValueError):
            ret_str = "n/a"
        parts.append(
            f'<li>{i + 1}. {_e(w.get("name", ""))} &mdash; {ret_str}</li>'
        )
    return "\n".join(parts)


def build_landing(leaderboard: dict, daily: dict | None = None) -> str:
    entries = leaderboard.get("algos", [])
    winners_html = _winners_li(entries)
    counts = (daily or {}).get("counts", {})
    total = counts.get("total") or len(entries)
    watchlist = counts.get("watchlist", 0)
    promoted = counts.get("promoted", 0)
    graveyard = counts.get("graveyard", 0)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>StockArithm</title>
<style>{LANDING_CSS}</style>
</head>
<body>
  <header>
    <h1>Alternative data signals, run in public.</h1>
    <p>StockArithm is a public paper-trading lab for alternative data signals. Some are working. Some are failing. All of them stay visible.</p>
    <div class="hero-actions">
      <a class="cta cta-primary" href="leaderboard.html">See the public leaderboard</a>
      <a class="cta" href="#waitlist">Get the weekly lab notes</a>
    </div>
    <div class="hero-strip">
      <span class="pill">{_e(total)} algos tracked</span>
      <span class="pill">Updated nightly</span>
      <span class="pill">Paper-traded in public</span>
      <span class="pill">Failures stay visible</span>
    </div>
  </header>

  <div class="wrap">
    <div class="grid">
      <div class="card">
        <h2>What you're looking at</h2>
        <p>Each row is one live paper-traded signal. Some are working. Some are failing. One of them is named after my dog. That is the point.</p>
      </div>

      <div class="card">
        <h2>Why so many names stay flat</h2>
        <p>A lot of the lab is still collecting data, waiting on better history, or sitting in sandbox until the first real trade fires. We leave those names visible instead of pretending they do not exist.</p>
      </div>

      <div class="card winners">
        <h3>30-Day Rolling Leaders</h3>
        <ul>
{winners_html}
        </ul>
        <p class="muted">Source: rolling 30-day leaderboard &mdash; <a href="leaderboard.html">full leaderboard</a></p>
      </div>

      <div class="card">
        <h2>What You Can Verify</h2>
        <p>Public counts update nightly. Right now the lab shows <strong>{_e(total)}</strong> total algos, <strong>{_e(watchlist)}</strong> on the watchlist, <strong>{_e(promoted)}</strong> promoted, and <strong>{_e(graveyard)}</strong> in the graveyard.</p>
        <p class="muted" style="margin-top:10px;">Watchlist means worth monitoring but not yet trusted. Promoted means strong enough to feature publicly. Graveyard means the idea failed badly enough that we keep it visible as a dead end.</p>
        <a class="cta" href="daily.html">Read the daily snapshot</a>
      </div>

      <div class="card">
        <h2>Build Log</h2>
        <p>Ship notes, failures, receipts, and founder context. This is the public lab notebook, not a polished black box.</p>
        <a class="cta" href="blog/index.html">Read the blog</a>
      </div>
    </div>

    <div class="card waitlist" style="margin-top:16px;">
      <h2>How The Lab Works</h2>
      <p>We generate and ship new signals. If a signal can be backtested honestly under V1 rules, it gets a backtest grade. If not, it stays live-only and has to earn trust through receipts.</p>
      <p>Signals that have not traded recently can go idle. Signals that trade and underperform can fail. Both stay visible. That is the whole point.</p>
    </div>
    <div class="card waitlist" id="waitlist">
      <h2>Get the weekly lab notes.</h2>
      <p>A short weekly note on which signals are holding up, which are breaking, and what the lab learned.</p>
      <form
        class="waitlist-form"
        id="mailerlite-waitlist-form"
        action="https://assets.mailerlite.com/jsonp/2275606/forms/185025288971748377/subscribe"
        method="post"
        target="mailerlite-waitlist-frame"
      >
        <input type="email" name="fields[email]" placeholder="you@example.com" autocomplete="email" required />
        <input type="hidden" name="fields[source]" value="landing" />
        <input type="hidden" name="ml-submit" value="1" />
        <input type="hidden" name="anticsrf" value="true" />
        <button type="submit">Get the weekly notes</button>
      </form>
      <iframe name="mailerlite-waitlist-frame" title="Mailing list signup" style="display:none"></iframe>
      <div class="notice">No hype. Just the state of the lab.</div>
    </div>

    <div class="card waitlist" id="disclaimer">
      <h2>Disclaimer</h2>
      <p>The information provided by this website, its tools, and any associated content is for informational and educational purposes only. Nothing here is financial, investment, legal, or tax advice.</p>
      <p>This service publishes experimental signals, research outputs, and historical observations. These are not recommendations to buy, sell, or hold any asset.</p>
      <p>Trading and investing involve significant risk, including possible loss of principal. Past performance does not guarantee future results. Signals, models, results, and third-party data may be incomplete, incorrect, delayed, or revised.</p>
      <p>You are solely responsible for your own financial decisions. Do your own research and consult a qualified professional before making investment decisions.</p>
      <p>By using this service, you agree that the operators are not liable for losses, damages, or decisions made based on the information provided.</p>
      <p><a href="legal.html">Read the full legal/disclaimer page &rarr;</a></p>
    </div>
  </div>

{_footer_html((daily or {}).get("generated_at", ""), (daily or {}).get("run_date", ""), "Free public launch surface")}

</body>
</html>"""


PREMIUM_CSS = CSS + """
  .premium-badge { display: inline-block; font-family: var(--mono); font-size: 11px; color: var(--gold); border: 1px solid var(--gold); border-radius: 4px; padding: 2px 8px; margin-left: 8px; letter-spacing: 0.5px; vertical-align: middle; }
  .family-badge { font-family: var(--mono); font-size: 10px; padding: 2px 6px; border-radius: 3px; background: rgba(168,85,247,0.1); color: var(--purple); border: 1px solid rgba(168,85,247,0.2); }
  .ev-badge { font-family: var(--mono); font-size: 10px; padding: 2px 6px; border-radius: 3px; background: rgba(25,211,143,0.08); color: var(--accent-dim); border: 1px solid rgba(25,211,143,0.15); }
"""


def _premium_table_rows(algos: list) -> str:
    rows = []
    for i, a in enumerate(algos):
        rank = i + 1
        spec = _get_special(str(a.get("algo_id", "")))
        row_cls = spec["row_class"] if spec else ""

        emoji = f'<span class="algo-emoji">{spec["emoji"]}</span>' if spec else ""
        if spec:
            name_html = (
                f'<span class="name-tooltip"><span class="algo-name">{emoji}{_e(a.get("name",""))}</span>'
                f'<span class="tip">{_e(spec["tip"])}</span></span>'
            )
        else:
            name_html = f'<span class="algo-name">{_e(a.get("name",""))}</span>'

        ytd = a.get("ytd_pct")
        spy = a.get("spy_pct")
        ret30 = a.get("ret_30d_pct")
        try:
            diff = float(ytd) - float(spy)
            diff_cls = "vs-spy-pos" if diff >= 0 else "vs-spy-neg"
            diff_str = ("+" if diff >= 0 else "") + f"{diff:.2f}%"
        except (TypeError, ValueError):
            diff_cls = "vs-spy-neg"
            diff_str = "n/a"

        status_html = (
            '<span class="status-beat">BEATING SPY</span>'
            if a.get("beat_spy")
            else '<span class="status-lag">LAGGING</span>'
        )
        family = _e(a.get("family") or "")
        ev = _e(a.get("evidence_class") or "")
        algo_type = str(a.get("algo_type", ""))
        public_algo_type = "alternative" if algo_type == "crazy" else algo_type

        rows.append(
            f'<tr class="{row_cls}">'
            f'<td class="rank">{rank}</td>'
            f'<td>{name_html}</td>'
            f'<td><span class="algo-type-badge">{_e(public_algo_type)}</span></td>'
            f'<td class="{_ret_class(ytd)}">{_fmt(ytd)}</td>'
            f'<td class="vs-spy {diff_cls}">{diff_str}</td>'
            f'<td class="{_ret_class(ret30)}">{_fmt(ret30)}</td>'
            f'<td class="days">{_e(a.get("days_running",""))}d</td>'
            f'<td>{status_html}</td>'
            f'<td><span class="family-badge">{family}</span></td>'
            f'<td><span class="ev-badge">{ev}</span></td>'
            f'</tr>'
        )
    return "\n".join(rows)


def build_premium(daily: dict, leaderboard: dict) -> str:
    algos = leaderboard.get("algos", [])
    total = len(algos)
    beating = sum(1 for a in algos if a.get("beat_spy"))
    generated_at = daily.get("generated_at", "")
    run_date = daily.get("run_date", "")
    sector_html = _sector_heatmap_html(daily.get("sector_summary") or {})
    table_rows = _premium_table_rows(algos[:15])
    counts = daily.get("counts") or {}
    watchlist = counts.get("watchlist", 0)
    promoted = counts.get("promoted", 0)
    graveyard = counts.get("graveyard", 0)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>StockArithm \u2014 Premium Preview</title>
<style>{PREMIUM_CSS}</style>
</head>
<body>

<div class="hero">
  <div class="hero-badge">PREMIUM PREVIEW</div>
  <h1><span>July 1</span> premium launch</h1>
  <p class="hero-sub">June 15 is free public launch. July 1 adds the paid operating layer.</p>
  <div class="hero-stats">
    <div class="hero-stat">
      <div class="num">{_e(total)}</div>
      <div class="label">Total Algos</div>
    </div>
    <div class="hero-stat">
      <div class="num">{_e(beating)}/{_e(total)}</div>
      <div class="label">Beating SPY</div>
    </div>
    <div class="hero-stat">
      <div class="num">{_e(watchlist)}</div>
      <div class="label">Watchlist</div>
    </div>
  </div>
  <a class="cta" href="landing.html#waitlist">Join the waitlist</a>
  <span class="cta-sub">No checkout yet. Waitlist first, paid launch July 1.</span>
</div>

<section>
  <div class="wrap">
    <h2 class="section-title">What Premium Will Add</h2>
    <p class="section-sub">This page is a teaser, not a gated member area yet.</p>
    <div class="hero-stats" style="justify-content:flex-start; gap:20px; margin:0 0 24px;">
      <div class="hero-stat">
        <div class="num">{_e(promoted)}</div>
        <div class="label">Promoted</div>
      </div>
      <div class="hero-stat">
        <div class="num">{_e(graveyard)}</div>
        <div class="label">Graveyard</div>
      </div>
      <div class="hero-stat">
        <div class="num">11</div>
        <div class="label">Sectors</div>
      </div>
    </div>
    <div class="rank-note">
      <strong>Free on June 15:</strong> blog, stripped leaderboard, families, promoted/watchlist summaries, graveyard, public daily report, and public ticker pages.
      <br>
      <strong>Paid on July 1:</strong> full leaderboard, full per-algo detail, full per-ticker detail, trade history, equity curves, and premium summaries.
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2 class="section-title">Sector Heatmap</h2>
    <p class="section-sub">This stays in the free public site. Premium adds the deeper operating layer around it.</p>
    <div class="heatmap">
{sector_html}
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2 class="section-title">Premium Preview <span class="premium-badge">COMING LATER</span></h2>
    <p class="section-sub">Preview of the table shape. The live paid layer does not launch until July 1.</p>
    <div class="rank-note">
      <strong>Force rank</strong> = full-window/since-seed return. <strong>Rolling 30D</strong> = trailing 30-day return.
      <code>Family</code> = strategy category. <code>Evidence</code> = validation status.
      Free stays intentionally lighter. Premium is where the full operating detail goes.
    </div>
    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th>#</th><th>Algorithm</th><th>Type</th>
            <th>Return</th><th>vs SPY</th><th>30D</th><th>Days</th><th>Status</th>
            <th>Family</th><th>Evidence</th>
          </tr>
        </thead>
        <tbody>
{table_rows}
        </tbody>
      </table>
    </div>
    <div style="margin-top:18px;">
      <a class="cta" href="landing.html#waitlist">Join the waitlist</a>
      <span class="cta-sub">Free launch first. Paid layer starts July 1.</span>
    </div>
  </div>
</section>

{_footer_html(generated_at, run_date, "Premium preview")}

</body>
</html>"""


def build_families_page(families: dict, daily: dict) -> str:
    generated_at = families.get("generated_at", "")
    run_date = daily.get("run_date", "")
    cards = []
    for family_name, payload in sorted((families.get("families") or {}).items()):
        leaders = payload.get("leaders") or []
        status_mix_html = _status_mix_html(payload.get("by_status") or {})
        leader_rows = "".join(
            f"<li><strong>{_e(item.get('name'))}</strong> "
            f"<span class=\"{_ret_class(item.get('ytd_pct'))}\">{_fmt(item.get('ytd_pct'))}</span> "
            f"<span class=\"days\">({item.get('status') or 'n/a'})</span></li>"
            for item in leaders[:5]
        ) or "<li>No leaders yet.</li>"
        cards.append(
            f"""
      <div class="card">
        <h2>{_e(family_name)}</h2>
        <p class="muted">Signals: {_e(payload.get('count', 0))}</p>
        <div style="margin: 10px 0 2px;">{status_mix_html}</div>
        <ul style="margin: 12px 0 0 18px; line-height: 1.8;">
          {leader_rows}
        </ul>
      </div>"""
        )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>StockArithm — Families</title>
<style>{LANDING_CSS}</style>
</head>
<body>
  <header>
    <h1>Signal Families</h1>
    <p>The lab grouped by theme instead of one flat wall of random experiments.</p>
  </header>
  <div class="wrap">
    <div class="grid">
{''.join(cards)}
    </div>
  </div>
{_footer_html(generated_at, run_date, "Family view")}
</body>
</html>"""


def build_daily_page(daily: dict) -> str:
    generated_at = daily.get("generated_at", "")
    run_date = daily.get("run_date", "")
    top_rows = "".join(
        f"<tr><td>{i}</td><td>{_e(item.get('name'))}</td><td>{_e(item.get('family'))}</td>"
        f"<td class=\"{_ret_class(item.get('ytd_pct'))}\">{_fmt(item.get('ytd_pct'))}</td>"
        f"<td class=\"vs-spy {'vs-spy-pos' if (item.get('alpha_pct') or -999) >= 0 else 'vs-spy-neg'}\">{_fmt(item.get('alpha_pct'))}</td></tr>"
        for i, item in enumerate(daily.get("top_live_ytd", [])[:10], start=1)
    ) or '<tr><td colspan="5">No daily leaders yet.</td></tr>'
    rolling_rows = "".join(
        f"<li><strong>{_e(item.get('name'))}</strong> "
        f"<span class=\"{_ret_class(item.get('ret_30d_pct'))}\">{_fmt(item.get('ret_30d_pct'))}</span> "
        f"<span class=\"days\">vs SPY {_fmt(item.get('vs_spy_30d_pct'))}</span></li>"
        for item in (daily.get("rolling_30d") or {}).get("leaders", [])[:10]
    ) or "<li>No rolling 30D data yet.</li>"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>StockArithm — Daily Report</title>
<style>{REPORT_CSS}</style>
</head>
<body>
<div class="hero">
  <div class="hero-badge">DAILY REPORT</div>
  <h1><span>{_e(run_date)}</span> nightly snapshot</h1>
  <p class="hero-sub">What changed in the lab after the nightly run.</p>
</div>
{_pulse_block_html(daily)}
<section>
  <div class="wrap">
    <h2 class="section-title">Counts</h2>
    <p class="section-sub">Current product layer totals.</p>
    <div class="hero-stats">
      <div class="hero-stat"><div class="num">{_e((daily.get('counts') or {}).get('total', 0))}</div><div class="label">Total</div></div>
      <div class="hero-stat"><div class="num">{_e((daily.get('counts') or {}).get('watchlist', 0))}</div><div class="label">Watchlist</div></div>
      <div class="hero-stat"><div class="num">{_e((daily.get('counts') or {}).get('promoted', 0))}</div><div class="label">Promoted</div></div>
      <div class="hero-stat"><div class="num">{_e((daily.get('counts') or {}).get('graveyard', 0))}</div><div class="label">Graveyard</div></div>
    </div>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="rank-note">
      <strong>Comparator note:</strong> The lab now tracks simple always-on baselines in `docs/comparison/`.
      Today that means <code>momentum_5d</code> and <code>momentum_20d</code>.
      They are there to answer one question: does a signal add anything beyond price momentum alone?
    </div>
  </div>
</section>
<section>
  <div class="wrap">
    <h2 class="section-title">Top Live YTD</h2>
    <div class="table-wrap">
      <table>
        <thead><tr><th>#</th><th>Algorithm</th><th>Family</th><th>Return</th><th>Alpha vs SPY</th></tr></thead>
        <tbody>{top_rows}</tbody>
      </table>
    </div>
  </div>
</section>
<section>
  <div class="wrap">
    <h2 class="section-title">Rolling 30D Leaders</h2>
    <ul style="margin-left: 20px; line-height: 1.9;">{rolling_rows}</ul>
  </div>
</section>
{_footer_html(generated_at, run_date, "Daily report")}
</body>
</html>"""


def build_legal_page() -> str:
    legal_md = (REPO / "docs" / "legal" / "disclaimers.md").read_text(encoding="utf-8")
    sections = []
    current = []
    title = None
    for line in legal_md.splitlines():
        if line.startswith("## "):
            if title:
                sections.append((title, current))
            title = line[3:].strip()
            current = []
        elif line.strip():
            current.append(line.strip())
    if title:
        sections.append((title, current))

    body = []
    for title, lines in sections:
        paras = "\n".join(f"<p>{_e(line)}</p>" for line in lines)
        body.append(f"<section><div class=\"wrap\"><h2 class=\"section-title\">{_e(title)}</h2>{paras}</div></section>")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>StockArithm — Legal</title>
<style>{REPORT_CSS}</style>
</head>
<body>
<div class="hero">
  <div class="hero-badge">LEGAL</div>
  <h1><span>Disclaimers</span> and disclosures</h1>
  <p class="hero-sub">The plain-English rules for using this site and its signals.</p>
</div>
{''.join(body)}
{_footer_html('', '', 'Legal / disclosures')}
</body>
</html>"""


PRICING_SECTION = """
    <div class="card" id="pricing" style="border-color: rgba(25,211,143,0.3);">
      <h2>Premium is not open yet</h2>
      <p>For now, the public site is the proof. Paid access comes later, after the free surface is stable and worth charging for.</p>
      <a class="cta" href="{stripe_url}">Join the mailing list for updates</a>
      <div style="margin-top: 8px; font-size: 12px; color: var(--muted);">
        Free public launch comes first. Paid access starts after the public surface earns it.
      </div>
    </div>
"""

STRIPE_PAYMENT_URL = "#waitlist"


def build_main():
    daily = _load("daily.json")
    leaderboard = _load("leaderboard.json")
    families = _load("families.json")

    out_lb = REPO / "docs" / "leaderboard.html"
    out_lb.write_text(build_leaderboard(daily, leaderboard), encoding="utf-8")
    print(f"[pages] wrote {out_lb}")

    out_landing = REPO / "docs" / "landing.html"
    out_landing.write_text(build_landing(leaderboard, daily), encoding="utf-8")
    print(f"[pages] wrote {out_landing}")

    out_index = REPO / "docs" / "index.html"
    out_index.write_text(build_landing(leaderboard, daily), encoding="utf-8")
    print(f"[pages] wrote {out_index}")

    out_premium = REPO / "docs" / "premium.html"
    out_premium.write_text(build_premium(daily, leaderboard), encoding="utf-8")
    print(f"[pages] wrote {out_premium}")

    out_families = REPO / "docs" / "families.html"
    out_families.write_text(build_families_page(families, daily), encoding="utf-8")
    print(f"[pages] wrote {out_families}")

    out_daily = REPO / "docs" / "daily.html"
    out_daily.write_text(build_daily_page(daily), encoding="utf-8")
    print(f"[pages] wrote {out_daily}")

    out_legal = REPO / "docs" / "legal.html"
    out_legal.write_text(build_legal_page(), encoding="utf-8")
    print(f"[pages] wrote {out_legal}")


def main():
    build_main()


if __name__ == "__main__":
    main()
