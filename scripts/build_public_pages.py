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
import csv
import sys
from pathlib import Path
from datetime import datetime

REPO = Path(__file__).parent.parent
PUBLIC = REPO / "docs" / "data" / "public"

SPECIAL = {
    "biscotti":  {"emoji": "\U0001f43e", "row_class": "row-biscotti",  "tip": "Named after Biscotti (2008\u20132026) \u2014 17.75 years of unconditional loyalty"},
    "baileymol": {"emoji": "\u26a1",      "row_class": "row-baileymol", "tip": "The Chaos Monger \u2014 thrives on volatility spikes"},
}

ETF_ORDER = ["XLK", "XLF", "XLV", "XLY", "XLI", "XLP", "XLE", "XLB", "XLRE", "XLU", "XLC"]

FREE_ROWS = 10


def _load(name: str) -> dict:
    p = PUBLIC / name
    if p.exists():
        return json.loads(p.read_text())
    return {}


def _load_rank_history() -> list[dict]:
    p = REPO / "data" / "rank_history.csv"
    if not p.exists():
        return []
    with p.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


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
        public_algo_type = _public_algo_type(algo_type)

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
    links = [
        ("/landing.html", "Home"),
        ("/leaderboard.html", "Leaderboard"),
        ("/signals/index.html", "Signals"),
        ("/families.html", "Families"),
        ("/daily.html", "Daily Report"),
        ("/premium.html", "Premium Preview"),
        ("/blog/index.html", "Blog"),
        ("/legal.html", "Legal"),
    ]
    parts = []
    for i, (href, label) in enumerate(links):
        if i:
            parts.append('<span class="footer-sep">&middot;</span>')
        parts.append(f'<a href="{href}" style="color:rgba(255,255,255,0.58);text-decoration:none;white-space:nowrap;">{_e(label)}</a>')
    parts.append('<span class="footer-sep">&middot;</span>')
    parts.append('<a href="/biscotti.html" style="color:rgba(255,255,255,0.58);text-decoration:none;white-space:nowrap;">Biscotti</a>')
    return "".join(parts)


def _leader_chart_html(rank_history: list[dict], leaderboard: dict) -> str:
    sorted_top = sorted(
        [a for a in (leaderboard.get("algos") or []) if a.get("ret_30d_pct") is not None],
        key=lambda a: float(a.get("ret_30d_pct") or float("-inf")),
        reverse=True,
    )
    top = []
    seen_ids = set()
    for item in sorted_top:
        algo_id = str(item.get("algo_id") or "")
        if not algo_id or algo_id in seen_ids:
            continue
        seen_ids.add(algo_id)
        top.append(item)
    if not top:
        return '<p class="muted">Leader chart coming soon.</p>'
    chart_rows = {}
    spy_by_date = {}
    for row in rank_history:
        date = str(row.get("date") or "")
        if date:
            try:
                spy_by_date.setdefault(date, float(row.get("spy_pct") or 0))
            except (TypeError, ValueError):
                spy_by_date.setdefault(date, 0.0)
        key = (str(row.get("algo_id") or ""), str(row.get("algo_type") or ""))
        chart_rows.setdefault(key, []).append(row)

    timeline = sorted(spy_by_date)
    if len(timeline) < 2:
        return '<p class="muted">Top leader chart coming soon.</p>'

    palette = ["#19d38f", "#7da7ff", "#f7b267", "#e879f9", "#f87171", "#facc15", "#34d399", "#60a5fa", "#fb7185", "#a78bfa"]
    series = []
    for idx, leader in enumerate(top):
        if len(series) >= 10:
            break
        key = (str(leader.get("algo_id") or ""), "crazy" if str(leader.get("algo_type") or "") == "crazy" else "normal")
        rows = sorted(chart_rows.get(key, []), key=lambda row: row.get("date", ""))
        if len(rows) < 2:
            continue
        values_by_date: dict[str, float] = {}
        base = None
        for row in rows:
            date = str(row.get("date") or "")
            try:
                equity = float(row.get("equity") or 0)
            except (TypeError, ValueError):
                continue
            if base is None and equity > 0:
                base = equity
            if base and date:
                values_by_date[date] = equity / base * 100.0
        if len(values_by_date) < 2:
            continue
        series.append((str(leader.get("name") or "Leader"), values_by_date, palette[idx % len(palette)]))

    if not series:
        return '<p class="muted">Top leader chart unavailable.</p>'

    spy_values: dict[str, float] = {}
    spy_base = None
    for date in timeline:
        try:
            pct = float(spy_by_date.get(date) or 0)
        except (TypeError, ValueError):
            pct = 0.0
        if spy_base is None:
            spy_base = 1.0 + pct / 100.0
        if spy_base:
            spy_values[date] = (1.0 + pct / 100.0) / spy_base * 100.0

    values = list(spy_values.values())
    for _, values_by_date, _ in series:
        values.extend(v for v in (values_by_date.get(date) for date in timeline) if v is not None)
    min_v = min(values)
    max_v = max(values)
    if max_v - min_v < 1e-9:
        max_v += 1.0
        min_v -= 1.0

    width = 720
    height = 340
    pad_l = 58
    pad_r = 20
    pad_t = 18
    pad_b = 42
    chart_w = width - pad_l - pad_r
    chart_h = height - pad_t - pad_b
    steps = max(len(timeline) - 1, 1)

    def xy(index: int, value: float):
        x = pad_l + (chart_w * index / steps)
        y = pad_t + chart_h - ((value - min_v) / (max_v - min_v) * chart_h)
        return x, y

    def path(values_by_date: dict[str, float]) -> str:
        cmds = []
        last_value = None
        started = False
        for i, date in enumerate(timeline):
            value = values_by_date.get(date)
            if value is None:
                if last_value is None:
                    continue
                value = last_value
            else:
                last_value = value
            x, y = xy(i, value)
            cmds.append(f"{'M' if not started else 'L'} {x:.1f} {y:.1f}")
            started = True
        return " ".join(cmds)

    def fmt_value(value: float) -> str:
        return f"{value:.1f}"

    def fmt_date_label(value: str) -> str:
        try:
            dt = datetime.fromisoformat(value)
            return f"{dt.strftime('%b')} {dt.day}"
        except Exception:
            return value

    tick_values = [min_v, min_v + (max_v - min_v) * 0.33, min_v + (max_v - min_v) * 0.66, max_v]
    tick_points = [
        (pad_l, timeline[0], "start"),
        (pad_l + (chart_w * 0.5), timeline[len(timeline) // 2], "middle"),
        (width - pad_r, timeline[-1], "end"),
    ]
    spy_last = spy_values[timeline[-1]]
    spy_path = path(spy_values)
    series_paths = "".join(
        f'<path d="{path(values_by_date)}" fill="none" stroke="{color}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>'
        for _, values_by_date, color in series
    )
    y_ticks = "".join(
        f'<line x1="{pad_l}" y1="{xy(0, v)[1]:.1f}" x2="{width - pad_r}" y2="{xy(0, v)[1]:.1f}" stroke="rgba(255,255,255,0.08)" stroke-dasharray="4 6" stroke-width="1"/>'
        f'<text x="{pad_l - 10}" y="{xy(0, v)[1] + 4:.1f}" text-anchor="end" font-family="IBM Plex Mono, ui-monospace, monospace" font-size="10" fill="rgba(255,255,255,0.55)">{fmt_value(v)}</text>'
        for v in tick_values
    )
    x_labels = "".join(
        f'<text x="{x:.1f}" y="{height - 12}" text-anchor="{anchor}" font-family="IBM Plex Mono, ui-monospace, monospace" font-size="10" fill="rgba(255,255,255,0.55)">{_e(fmt_date_label(d))}</text>'
        for x, d, anchor in tick_points
    )

    beating_spy = sum(1 for a in (leaderboard.get("algos") or []) if a.get("beat_spy"))
    total_algos = len(leaderboard.get("algos") or [])
    weak_regime = beating_spy <= max(2, total_algos // 20)
    caption = (
        "Recent conditions have been rough and most signals are underwater. That is why we keep the full record visible."
        if weak_regime
        else
        "Recent conditions have improved and more signals are beating SPY. That is why we keep the full record visible."
    )

    return f"""
    <div class="mini-chart-wrap">
      <div class="mini-chart-meta">
        <div class="mini-chart-title">Top 10 rolling 30D leaders vs SPY</div>
        <div class="mini-chart-note">{_e(caption)}</div>
      </div>
      <svg class="mini-chart" viewBox="0 0 {width} {height}" role="img" aria-label="Top 10 rolling 30D leaders versus SPY chart">
        <rect x="0" y="0" width="{width}" height="{height}" rx="14" fill="#0f1c18" stroke="rgba(255,255,255,0.08)"/>
        {y_ticks}
        <line x1="{pad_l}" y1="{pad_t}" x2="{pad_l}" y2="{pad_t + chart_h}" stroke="rgba(255,255,255,0.14)" stroke-width="1"/>
        <line x1="{pad_l}" y1="{pad_t + chart_h}" x2="{width - pad_r}" y2="{pad_t + chart_h}" stroke="rgba(255,255,255,0.14)" stroke-width="1"/>
        <path d="{spy_path}" fill="none" stroke="#8faeff" stroke-width="4" stroke-dasharray="10 6" stroke-linecap="round" stroke-linejoin="round" opacity="0.95"/>
        {series_paths}
        {x_labels}
      </svg>
      <div class="mini-chart-legend">
        {''.join(f'<span><i style="background:{color};"></i>{_e(name)}</span>' for name, _, color in series)}
        <span><i style="background:none;border-top:3px dashed #8faeff;width:18px;height:0;border-radius:0;"></i>SPY baseline {spy_last:.1f}</span>
      </div>
    </div>
    """


def _biscotti_chart_html(snapshots: list[dict]) -> str:
    rows = [row for row in snapshots if row.get("date")]
    if not rows:
        return '<p class="muted">No Biscotti equity data yet.</p>'

    timeline = [str(row.get("date")) for row in rows]
    equity_by_date: dict[str, float] = {}
    spy_by_date: dict[str, float] = {}
    last_spy = None
    for row in rows:
        date = str(row.get("date") or "")
        if not date:
            continue
        try:
            equity_by_date[date] = float(row.get("equity") or 0.0)
        except (TypeError, ValueError):
            equity_by_date[date] = 0.0
        spy_value = row.get("spy_equity")
        if spy_value is not None:
            try:
                last_spy = float(spy_value)
            except (TypeError, ValueError):
                pass
        if last_spy is not None:
            spy_by_date[date] = last_spy
    if not equity_by_date:
        return '<p class="muted">No Biscotti equity data yet.</p>'

    values = list(equity_by_date.values()) + list(spy_by_date.values())
    min_v = min(values)
    max_v = max(values)
    if max_v == min_v:
        min_v -= 1.0
        max_v += 1.0
    pad = max((max_v - min_v) * 0.08, 100.0)
    min_v -= pad
    max_v += pad

    width = 860
    height = 330
    pad_l = 62
    pad_r = 18
    pad_t = 18
    pad_b = 42
    chart_w = width - pad_l - pad_r
    chart_h = height - pad_t - pad_b
    steps = max(len(timeline) - 1, 1)

    def xy(index: int, value: float):
        x = pad_l + (chart_w * index / steps)
        y = pad_t + chart_h - ((value - min_v) / (max_v - min_v) * chart_h)
        return x, y

    def path(values_by_date: dict[str, float]) -> str:
        cmds = []
        last_value = None
        started = False
        for i, date in enumerate(timeline):
            value = values_by_date.get(date)
            if value is None:
                if last_value is None:
                    continue
                value = last_value
            else:
                last_value = value
            x, y = xy(i, value)
            cmds.append(f"{'M' if not started else 'L'} {x:.1f} {y:.1f}")
            started = True
        return " ".join(cmds)

    def fmt_value(value: float) -> str:
        return f"{value:,.0f}"

    def fmt_date_label(value: str) -> str:
        try:
            dt = datetime.fromisoformat(value)
            return f"{dt.strftime('%b')} {dt.day}"
        except Exception:
            return value

    tick_values = [min_v, min_v + (max_v - min_v) * 0.33, min_v + (max_v - min_v) * 0.66, max_v]
    tick_points = [
        (pad_l, timeline[0], "start"),
        (pad_l + (chart_w * 0.5), timeline[len(timeline) // 2], "middle"),
        (width - pad_r, timeline[-1], "end"),
    ]
    equity_path = path(equity_by_date)
    spy_path = path(spy_by_date)
    current_equity = equity_by_date[timeline[-1]]
    current_spy = spy_by_date.get(timeline[-1], current_equity)
    title = "Equity curve vs carried-forward SPY baseline"
    note = "This is the actual Biscotti record: equity line, baseline line, and the trade log below."
    y_ticks = "".join(
        f'<line x1="{pad_l}" y1="{xy(0, v)[1]:.1f}" x2="{width - pad_r}" y2="{xy(0, v)[1]:.1f}" stroke="rgba(255,255,255,0.08)" stroke-dasharray="4 6" stroke-width="1"/>'
        f'<text x="{pad_l - 10}" y="{xy(0, v)[1] + 4:.1f}" text-anchor="end" font-family="IBM Plex Mono, ui-monospace, monospace" font-size="10" fill="rgba(255,255,255,0.55)">{fmt_value(v)}</text>'
        for v in tick_values
    )
    x_labels = "".join(
        f'<text x="{x:.1f}" y="{height - 12}" text-anchor="{anchor}" font-family="IBM Plex Mono, ui-monospace, monospace" font-size="10" fill="rgba(255,255,255,0.55)">{_e(fmt_date_label(d))}</text>'
        for x, d, anchor in tick_points
    )
    return f"""
    <div class="mini-chart-wrap">
      <div class="mini-chart-meta">
        <div class="mini-chart-title">{_e(title)}</div>
        <div class="mini-chart-note">{_e(note)}</div>
      </div>
      <svg class="mini-chart biscotti-chart" viewBox="0 0 {width} {height}" role="img" aria-label="Biscotti equity curve versus SPY baseline">
        <rect x="0" y="0" width="{width}" height="{height}" rx="14" fill="#0f0f0f" stroke="rgba(255,255,255,0.08)"/>
        {y_ticks}
        <line x1="{pad_l}" y1="{pad_t}" x2="{pad_l}" y2="{pad_t + chart_h}" stroke="rgba(255,255,255,0.14)" stroke-width="1"/>
        <line x1="{pad_l}" y1="{pad_t + chart_h}" x2="{width - pad_r}" y2="{pad_t + chart_h}" stroke="rgba(255,255,255,0.14)" stroke-width="1"/>
        <path d="{spy_path}" fill="none" stroke="#8faeff" stroke-width="4" stroke-dasharray="10 6" stroke-linecap="round" stroke-linejoin="round" opacity="0.92"/>
        <path d="{equity_path}" fill="none" stroke="#19d38f" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/>
        {x_labels}
      </svg>
      <div class="mini-chart-legend">
        <span><i style="background:#19d38f;"></i>Biscotti equity {current_equity:,.0f}</span>
        <span><i style="background:none;border-top:3px dashed #8faeff;width:18px;height:0;border-radius:0;"></i>SPY baseline {current_spy:,.0f}</span>
      </div>
    </div>
    """


def _signal_index_rows_html(entries: list[dict]) -> str:
    rows = []
    for item in sorted(entries, key=lambda row: (str(row.get("name") or "").lower(), str(row.get("algo_type") or ""))):
        rows.append(
            "<tr>"
            f"<td><strong>{_e(item.get('name'))}</strong></td>"
            f"<td>{_e(_public_algo_type(str(item.get('algo_type', ''))))}</td>"
            f"<td>{_e(FAMILY_TITLES.get(str(item.get('family') or ''), _pretty_label(item.get('family') or '')))}</td>"
            f"<td>{_e(_pretty_label(str(item.get('status') or '')))}</td>"
            f"<td>{_e(item.get('rebalance_frequency') or '')}</td>"
            "</tr>"
        )
    return "\n".join(rows) if rows else '<tr><td colspan="5">No signals yet.</td></tr>'


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
    <div class="footer-nav" style="margin-top:8px;display:flex;justify-content:center;align-items:center;flex-wrap:wrap;gap:0 8px;width:100%;font-family:var(--mono);font-size:11px;line-height:1.6;letter-spacing:0.2px;color:rgba(255,255,255,0.58);">{_site_links()}</div>
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
    --bg: #0d1412;
    --bg2: #13231f;
    --card: #182b26;
    --border: rgba(255,255,255,0.08);
    --accent: #19d38f;
    --accent-dim: #12a06b;
    --red: #ef4444;
    --red-dim: #991b1b;
    --yellow: #eab308;
    --gold: #d4a017;
    --purple: #a855f7;
    --muted: #9ab0a7;
    --text: #ecf5f2;
    --mono: 'IBM Plex Mono', ui-monospace, monospace;
    --sans: 'Space Grotesk', system-ui, sans-serif;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: var(--sans); color: var(--text); background: var(--bg); line-height: 1.5; -webkit-font-smoothing: antialiased; }
  .hero { text-align: center; padding: 60px 24px 48px; background: var(--bg); border-bottom: 1px solid var(--border); }
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
  .section-title { font-size: 22px; font-weight: 700; margin-bottom: 6px; color: var(--accent); }
  .section-sub { font-size: 13px; color: var(--muted); margin-bottom: 24px; }
  .heatmap { display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 10px; }
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
  .ticker-check { max-width: 480px; margin: 0 auto; }
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
  .footer-nav { margin-top: 8px; display: flex; justify-content: center; align-items: center; flex-wrap: wrap; gap: 0 8px; width: 100%; font-family: var(--mono); font-size: 11px; line-height: 1.6; letter-spacing: 0.2px; color: rgba(255,255,255,0.58); }
  .footer-nav a, .footer-nav a:visited { color: rgba(255,255,255,0.58); text-decoration: none; white-space: nowrap; }
  .footer-nav .footer-sep { color: rgba(255,255,255,0.40); }
  .footer-nav a:hover { text-decoration: underline; }
  .section-title { text-align: center; }
  .section-sub { text-align: center; }
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
    .heatmap { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px; }
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


def _public_algo_type(value: str) -> str:
    return "alternative" if str(value) == "crazy" else str(value)


def _status_legend_html() -> str:
    return """
    <div class="rank-note family-legend">
      <strong>Status legend:</strong>
      <ul>
        <li><code>live_only</code> means the signal is live and publishing receipts, but does not have a clean enough history for a strict backtest.</li>
        <li><code>sandbox</code> means visible in public on purpose, but still waiting on enough data or a first live trade.</li>
        <li><code>parked</code> means temporarily set aside while the input, build, or deployment path gets cleaned up.</li>
        <li><code>promoted</code> means strong enough to feature publicly.</li>
        <li><code>backtest_weak</code> means the historical test exists but has not earned much trust.</li>
        <li><code>graveyard</code> means the idea failed badly enough that we keep it visible as a dead end.</li>
      </ul>
    </div>
    """


FAMILY_DESCRIPTIONS = {
    "attention_sentiment": "Signals that try to catch sector moves through attention spikes, headlines, search interest, and sentiment shifts.",
    "consumer_stress": "Signals built around consumer pressure, housing, rates, and spending strain before that stress fully shows up in sector prices.",
    "core_rotation": "The cleaner baseline rotation rules: momentum, trend, and other simple sector-switching logic with fewer alternative inputs.",
    "freight_logistics": "Signals using shipping, freight, ports, and supply-chain activity as early reads on industrial and materials demand.",
    "labor_jobs": "Signals watching layoffs, hiring, labor stress, and job demand for clues about sector weakness or resilience.",
    "local_economy_weirdness": "Ground-level alternative signals from local behavior, foot traffic, closures, calls, and other messy real-world activity.",
    "macro_input_pressure": "Signals tied to macro shocks like volatility, weather, commodities, energy, and other broad external pressure inputs.",
    "political_insider_filing": "Signals built from insider flows, political filings, and dark-pool style positioning clues before the market fully reacts.",
    "travel_mobility": "Signals using movement, travel, transit, and mobility behavior as an early read on consumer and cyclical activity.",
}

FAMILY_TITLES = {
    "attention_sentiment": "Attention & Sentiment",
    "consumer_stress": "Consumer Stress",
    "core_rotation": "Core Rotation",
    "freight_logistics": "Freight & Logistics",
    "labor_jobs": "Labor & Jobs",
    "local_economy_weirdness": "Local Economy Signals",
    "macro_input_pressure": "Macro Input Pressure",
    "political_insider_filing": "Political & Insider Filings",
    "travel_mobility": "Travel & Mobility",
}


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
      Some signals are backtested under our standard rules. Others are live-only because the historical data is not clean enough to backfill honestly.
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
    --bg: #0a0d12;
    --bg-2: #111520;
    --card: #111520;
    --accent: #19d38f;
    --muted: #9ab0a7;
    --text: #ecf5f2;
  }
  * { box-sizing: border-box; }
  body { margin: 0; font-family: 'Space Grotesk', system-ui, sans-serif; color: var(--text); background: var(--bg); }
  header { padding: 28px; border-bottom: 1px solid rgba(255,255,255,0.08); text-align: center; }
  header h1 { margin: 0; font-size: 30px; letter-spacing: 0.5px; }
  header p { margin: 6px 0 0; color: var(--muted); font-family: 'IBM Plex Mono', ui-monospace, monospace; font-size: 12px; }
  .wrap { padding: 24px; }
  .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px; }
  .card { background: var(--card); border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 16px; box-shadow: 0 14px 30px rgba(0,0,0,0.22); }
  .card h2 { margin: 0 0 8px; font-size: 18px; }
  .card p { margin: 0 0 12px; color: var(--muted); font-size: 14px; line-height: 1.4; }
  .cta { display: inline-block; padding: 10px 12px; border-radius: 8px; border: none; background: var(--accent); color: #062018; text-decoration: none; font-weight: 700; font-size: 13px; transition: background 0.2s; }
  .cta:hover { background: #33e3a3; }
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
  .waitlist-form button { border: none; border-radius: 8px; background: var(--accent); color: #062018; padding: 10px 12px; font: inherit; font-size: 13px; font-weight: 700; cursor: pointer; transition: background 0.2s; }
  .waitlist-form button:hover { background: #33e3a3; }
  .waitlist-form button[disabled] { opacity: 0.72; cursor: wait; }
  .waitlist-status { display: none; margin-top: 10px; padding: 10px 12px; border-radius: 10px; font-size: 13px; line-height: 1.45; text-align: center; }
  .waitlist-status.is-active { display: block; }
  .waitlist-status.is-info { background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); color: var(--muted); }
  .waitlist-status.is-success { background: rgba(25,211,143,0.10); border: 1px solid rgba(25,211,143,0.24); color: var(--text); }
  .waitlist-status.is-warn { background: rgba(250,204,21,0.10); border: 1px solid rgba(250,204,21,0.20); color: var(--text); }
  .notice { margin-top: 10px; color: var(--muted); font-size: 12px; line-height: 1.4; }
  .hero-actions { display: flex; gap: 10px; flex-wrap: wrap; margin-top: 14px; justify-content: center; }
  .hero-actions .cta { padding: 10px 14px; }
  .hero-strip { margin-top: 16px; display: flex; gap: 10px; flex-wrap: wrap; justify-content: center; }
  .pill { font-size: 12px; color: var(--muted); border: 1px solid rgba(255,255,255,0.08); border-radius: 999px; padding: 6px 10px; }
  .hero-brand { font-size: clamp(42px, 7vw, 72px); font-weight: 700; letter-spacing: -1.5px; line-height: 1; color: var(--accent); margin: 0 0 10px; }
  .hero-tagline { font-family: 'IBM Plex Mono', ui-monospace, monospace; font-size: 14px; color: var(--muted); max-width: 860px; margin: 0 auto; }
  .home-shell { max-width: 1120px; margin: 0 auto; }
  .home-shell .card { text-align: center; display: flex; flex-direction: column; }
  .home-shell .card ul { display: inline-block; text-align: left; margin: 0 auto; }
  .home-shell .card .cta { margin-top: auto; }
  .home-shell .card .muted:last-of-type { margin-bottom: 12px; }
  .home-shell .card .card-actions { margin-top: auto; display: flex; gap: 10px; justify-content: center; flex-wrap: wrap; }
  .mini-chart-wrap { display: flex; flex-direction: column; gap: 10px; }
  .mini-chart-meta { display: flex; flex-direction: column; gap: 4px; }
  .mini-chart-title { font-size: 18px; font-weight: 700; }
  .mini-chart-note { color: var(--muted); font-size: 14px; line-height: 1.4; }
  .mini-chart { width: 100%; height: auto; display: block; }
  .mini-chart-legend { display: flex; gap: 12px; flex-wrap: wrap; align-items: center; font-size: 12px; color: var(--muted); }
  .mini-chart-legend span { display: inline-flex; align-items: center; gap: 6px; }
  .mini-chart-legend i { display: inline-block; width: 10px; height: 10px; border-radius: 999px; }
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


def build_landing(leaderboard: dict, daily: dict | None = None, rank_history: list[dict] | None = None) -> str:
    entries = leaderboard.get("algos", [])
    winners_html = _winners_li(entries)
    chart_html = _leader_chart_html(rank_history or [], leaderboard)
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
    <div class="hero-brand">StockArithm</div>
    <h1>Alternative data signals, run in public.</h1>
    <p class="hero-tagline">StockArithm is a public paper-trading lab for alternative data signals. Some are working. Some are failing. All of them stay visible.</p>
    <div class="hero-actions">
      <a class="cta" href="leaderboard.html">See the public leaderboard</a>
      <a class="cta" href="#waitlist">Get the weekly lab notes</a>
    </div>
    <div class="hero-strip">
      <span class="pill">{_e(total)} algos tracked</span>
      <span class="pill">Updated nightly</span>
      <span class="pill">Paper-traded in public</span>
      <span class="pill">Failures stay visible</span>
    </div>
  </header>

  <div class="wrap home-shell">
    <div class="card" style="margin-bottom:16px;">
      {chart_html}
    </div>

    <div class="card" style="margin-bottom:16px;">
      <h2>Start Here</h2>
      <p>StockArithm is a public lab for alternative data signals.</p>
      <p>We turn non-traditional inputs into trading ideas, test them honestly, and publish the results.</p>
      <p>Some signals work. Some fail. We keep both visible.</p>
      <h3 style="margin-top:16px;">What to look at first</h3>
      <ul>
        <li><strong>Leaderboard:</strong> which signals are working right now</li>
        <li><strong>Signals:</strong> the full public list of all {_e(total)} signals</li>
        <li><strong>Daily Report:</strong> what changed after the nightly run</li>
        <li><strong>Families:</strong> what each signal family is trying to measure</li>
      </ul>
      <h3 style="margin-top:16px;">How it works</h3>
      <p>Idea -> signal -> backtest if we can -> live run if we can’t -> public result.</p>
      <p>Signals can go idle. Signals that underperform can fail. We keep both visible.</p>
      <h3 style="margin-top:16px;">Why it matters</h3>
      <p>The point is not hype. The point is to see which signals add something beyond price alone.</p>
      <h3 style="margin-top:16px;">One example</h3>
      <p>If TSA volume spikes, the lab can turn that into a travel or consumer signal, run it against SPY, and show whether it actually helps.</p>
    </div>

    <div class="grid">
      <div class="card winners">
        <h3>30-Day Rolling Leaders</h3>
        <ul>
{winners_html}
        </ul>
        <p class="muted">Recent leaders over the last 30 days.</p>
        <a class="cta" href="leaderboard.html">View the leaderboard</a>
      </div>

      <div class="card">
        <h2>What You Can Verify</h2>
        <p>Public counts update nightly. Right now the lab shows <strong>{_e(total)}</strong> total algos, <strong>{_e(watchlist)}</strong> on the watchlist, <strong>{_e(promoted)}</strong> promoted, and <strong>{_e(graveyard)}</strong> in the graveyard.</p>
        <p class="muted" style="margin-top:10px;">Watchlist means worth monitoring but not yet trusted. Promoted means strong enough to feature publicly. Graveyard means the idea failed badly enough that we keep it visible as a dead end.</p>
        <a class="cta" href="daily.html">Read the daily snapshot</a>
      </div>

      <div class="card">
        <h2>Signal Index</h2>
        <p>All {_e(total)} signals in one public list. Names, families, and status only. No rank and no returns.</p>
        <p class="muted" style="margin-top:10px;">A lot of the lab is still collecting data, waiting on better history, or sitting in sandbox until the first real trade fires. Families show what each cluster is trying to measure.</p>
        <div class="card-actions">
          <a class="cta" href="signals/index.html">Browse all signals</a>
          <a class="cta" href="families.html">Browse families</a>
        </div>
      </div>
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
      <div class="waitlist-status" id="mailerlite-waitlist-status" aria-live="polite"></div>
      <div class="notice">No hype. Just the state of the lab.</div>
    </div>

    <div class="card waitlist" id="disclaimer">
      <h2>Disclaimer</h2>
      <p>The information provided by this website, its tools, and any associated content is for informational and educational purposes only. Nothing here is financial, investment, legal, or tax advice.</p>
      <p>This service publishes experimental signals, research outputs, and historical observations. These are not recommendations to buy, sell, or hold any asset.</p>
      <p>Trading and investing involve significant risk, including possible loss of principal. Past performance does not guarantee future results. Signals, models, results, and third-party data may be incomplete, incorrect, delayed, or revised.</p>
      <p>You are solely responsible for your own financial decisions. Do your own research and consult a qualified professional before making investment decisions.</p>
      <p>By using this service, you agree that the operators are not liable for losses, damages, or decisions made based on the information provided.</p>
      <div style="margin-top:14px;">
        <a class="cta" href="legal.html">Read the full legal/disclaimer page</a>
      </div>
    </div>
  </div>

{_footer_html((daily or {}).get("generated_at", ""), (daily or {}).get("run_date", ""), "Free public launch surface")}

<script>
  (function () {{
    const form = document.getElementById('mailerlite-waitlist-form');
    const frame = document.querySelector('iframe[name="mailerlite-waitlist-frame"]');
    const status = document.getElementById('mailerlite-waitlist-status');
    if (!form || !frame || !status) return;

    const submitButton = form.querySelector('button[type="submit"]');
    const defaultLabel = submitButton ? submitButton.textContent : '';
    let pending = false;
    let timeoutId = null;

    function setStatus(kind, message) {{
      status.className = 'waitlist-status is-active ' + kind;
      status.textContent = message;
    }}

    function resetButton() {{
      if (!submitButton) return;
      submitButton.disabled = false;
      submitButton.textContent = defaultLabel;
    }}

    form.addEventListener('submit', function () {{
      pending = true;
      if (submitButton) {{
        submitButton.disabled = true;
        submitButton.textContent = 'Submitting...';
      }}
      setStatus('is-info', 'Submitting... If this works, you will get a MailerLite email next.');
      clearTimeout(timeoutId);
      timeoutId = window.setTimeout(function () {{
        if (!pending) return;
        pending = false;
        resetButton();
        setStatus('is-warn', 'Submission sent, but no confirmation came back to the page. Check your email, and if nothing shows up, try again.');
      }}, 12000);
    }});

    frame.addEventListener('load', function () {{
      if (!pending) return;
      pending = false;
      clearTimeout(timeoutId);
      resetButton();
      setStatus('is-success', 'Thanks. Check your email for the confirmation from MailerLite.');
      form.reset();
    }});
  }})();
</script>

</body>
</html>"""


def build_signals_index(leaderboard: dict, daily: dict | None = None) -> str:
    entries = leaderboard.get("algos", [])
    total = len(entries)
    generated_at = (daily or {}).get("generated_at", "")
    run_date = (daily or {}).get("run_date", "")
    rows = _signal_index_rows_html(entries)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>StockArithm — Signals Index</title>
<style>{LANDING_CSS}
  .table-wrap {{ overflow-x: auto; border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; }}
  table {{ width: 100%; border-collapse: collapse; min-width: 760px; background: rgba(255,255,255,0.02); }}
  thead th {{ text-align: left; font-size: 12px; letter-spacing: 0.04em; text-transform: uppercase; color: var(--muted); padding: 12px 14px; border-bottom: 1px solid rgba(255,255,255,0.08); }}
  tbody td {{ padding: 12px 14px; border-bottom: 1px solid rgba(255,255,255,0.06); font-size: 14px; vertical-align: top; }}
  tbody tr:last-child td {{ border-bottom: none; }}
  tbody td strong {{ color: var(--text); }}
  .signal-note {{ color: var(--muted); font-size: 14px; line-height: 1.5; margin-top: 8px; }}
  .signal-table-sub {{ margin: 0 0 14px; color: var(--muted); font-size: 14px; }}
  .page-title {{ color: var(--accent); font-size: clamp(28px, 5vw, 48px); font-weight: 700; letter-spacing: -0.5px; margin: 0 0 12px; }}
</style>
</head>
<body>
    <header>
    <h1 class="page-title">All signals, no scoreboard.</h1>
    <p>StockArithm's public inventory: names, families, and status only. No rank and no returns.</p>
    <div class="hero-actions">
      <a class="cta" href="/leaderboard.html">See the public leaderboard</a>
      <a class="cta" href="/families.html">Browse families</a>
    </div>
    <div class="hero-strip">
      <span class="pill">{_e(total)} signals listed</span>
      <span class="pill">Alphabetical order</span>
      <span class="pill">No returns shown</span>
      <span class="pill">No rank shown</span>
    </div>
  </header>

  <div class="wrap">
    <div class="card">
      <h2>Public signal index</h2>
      <p class="signal-table-sub">This is the full public list. It exists so the site does not feel like it is hiding the inventory.</p>
      <div class="table-wrap">
        <table>
          <thead>
            <tr>
              <th>Name</th>
              <th>Type</th>
              <th>Family</th>
              <th>Status</th>
              <th>Frequency</th>
            </tr>
          </thead>
          <tbody>
{rows}
          </tbody>
        </table>
      </div>
      <p class="signal-note">Premium will link into the full per-algo pages later. This page stays public and stays scorecard-free.</p>
    </div>
  </div>

{_footer_html(generated_at, run_date, "Public signal index")}

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
        public_algo_type = _public_algo_type(algo_type)

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
  <p class="hero-sub">May 15 is free public launch. July 1 adds the paid operating layer.</p>
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
  <a class="cta" href="landing.html#waitlist">Get the weekly notes</a>
  <span class="cta-sub">No checkout yet. Waitlist first, paid launch July 1.</span>
</div>

<section>
  <div class="wrap">
    <h2 class="section-title">What Premium Will Add</h2>
    <p class="section-sub">This page is a teaser, not a gated member area yet.</p>
    <div class="hero-stats" style="justify-content:center; gap:20px; margin:0 0 24px;">
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
      <strong>Free on May 15:</strong> blog, stripped leaderboard, families, promoted/watchlist summaries, graveyard, public daily report, and public ticker pages.
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
    <div style="margin-top:18px; text-align:center;">
      <a class="cta" href="landing.html#waitlist">Get the weekly notes</a>
      <span class="cta-sub">Free launch first. Paid layer starts July 1.</span>
    </div>
  </div>
</section>

{_footer_html(generated_at, run_date, "Premium preview")}

</body>
</html>"""


def build_biscotti_page(trades_data: dict) -> str:
    trades = trades_data.get("trade_log") or []
    snapshots = trades_data.get("daily_snapshots") or []
    latest = snapshots[-1] if snapshots else {}
    last_date = str(latest.get("date") or "")
    start_equity = float(snapshots[0].get("equity") or 100000.0) if snapshots else 100000.0
    last_equity = float(latest.get("equity") or start_equity)

    max_peak = start_equity
    max_dd = 0.0
    for snap in snapshots:
        try:
            eq = float(snap.get("equity") or 0.0)
        except (TypeError, ValueError):
            continue
        max_peak = max(max_peak, eq)
        if max_peak:
            max_dd = min(max_dd, (eq - max_peak) / max_peak)

    completed = [t for t in trades if str(t.get("action") or "").upper() == "SELL"]
    wins = sum(1 for t in completed if float(t.get("pnl") or 0.0) > 0)
    win_rate = (wins / len(completed) * 100.0) if completed else 0.0
    open_positions = latest.get("positions") or {}

    open_rows = []
    for ticker, pos in sorted(open_positions.items()):
        current_price = float(pos.get("current_price") or 0.0)
        entry_price = float(pos.get("entry_price") or 0.0)
        market_value = float(pos.get("market_value") or 0.0)
        unrealized = float(pos.get("unrealized_pnl") or 0.0)
        open_rows.append(
            "<tr>"
            f"<td><strong>{_e(ticker)}</strong></td>"
            f"<td>${entry_price:,.2f}</td>"
            f"<td>${current_price:,.2f}</td>"
            f"<td class=\"{'return-pos' if unrealized >= 0 else 'return-neg'}\">${unrealized:,.2f}</td>"
            f"<td>${market_value:,.2f}</td>"
            f"<td>{_e(pos.get('entry_date') or '')}</td>"
            "</tr>"
        )
    if not open_rows:
        open_rows.append('<tr><td colspan="6">No open position right now.</td></tr>')

    trade_rows = []
    for trade in reversed(trades):
        action = str(trade.get("action") or "").upper()
        action_cls = "action-buy" if action == "BUY" else "action-sell"
        value = float(trade.get("cost") or trade.get("proceeds") or 0.0)
        pnl = trade.get("pnl")
        pnl_html = "—"
        if pnl is not None:
            pnl_val = float(pnl or 0.0)
            pnl_pct = float(trade.get("pnl_pct") or 0.0)
            pnl_html = f'<span class="{"return-pos" if pnl_val >= 0 else "return-neg"}">${pnl_val:,.2f} ({pnl_pct:+.1f}%)</span>'
        trade_rows.append(
            "<tr>"
            f"<td>{_e(trade.get('date') or '')}</td>"
            f"<td><span class=\"{action_cls}\">{_e(action)}</span></td>"
            f"<td><span class=\"ticker\">{_e(trade.get('ticker') or '')}</span></td>"
            f"<td>${float(trade.get('price') or 0.0):,.2f}</td>"
            f"<td>{float(trade.get('shares') or 0.0):,.4f}</td>"
            f"<td>${value:,.2f}</td>"
            f"<td>{pnl_html}</td>"
            f"<td>{_e(trade.get('reason') or ('entry' if action == 'BUY' else '—'))}</td>"
            "</tr>"
        )
    trade_rows_html = "\n".join(trade_rows) if trade_rows else '<tr><td colspan="8">No trade log available.</td></tr>'

    chart_html = _biscotti_chart_html(snapshots)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>StockArithm — Biscotti</title>
<style>{REPORT_CSS}</style>
<style>
  .biscotti-hero {{ text-align: center; }}
  .biscotti-title {{ color: var(--accent); text-align: center; }}
  .biscotti-sub {{ text-align: center; margin-top: 8px; color: var(--muted); font-family: var(--mono); font-size: 14px; }}
  .biscotti-top {{ display: grid; grid-template-columns: minmax(0, 280px) minmax(0, 1fr); gap: 20px; align-items: start; }}
  .biscotti-photo {{ width: 100%; border-radius: 12px; border: 1px solid var(--border); display: block; object-fit: cover; aspect-ratio: 1 / 1; background: #111; }}
  .biscotti-label {{ color: var(--muted); font-size: 12px; font-family: var(--mono); margin-top: 8px; text-align: center; }}
  .biscotti-summary {{ display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 10px; }}
  .biscotti-summary .hero-stat {{ background: rgba(255,255,255,0.02); border: 1px solid var(--border); border-radius: 12px; padding: 16px 14px; }}
  .biscotti-summary .hero-stat .num {{ font-size: 26px; }}
  .biscotti-summary .hero-stat .label {{ margin-top: 4px; }}
  .biscotti-note {{ margin-top: 12px; color: var(--muted); font-size: 13px; line-height: 1.6; }}
  .biscotti-chart {{ width: 100%; height: auto; display: block; margin: 0 auto; }}
  .biscotti-table-wrap {{ overflow-x: auto; border-radius: 12px; border: 1px solid var(--border); background: rgba(255,255,255,0.02); }}
  .biscotti-table-wrap table {{ min-width: 100%; }}
  .trade-table thead th, .trade-table tbody td {{ white-space: nowrap; }}
  .trade-table tbody tr:hover td {{ background: rgba(25,211,143,0.04); }}
  .free-preview-note {{ text-align: center; color: var(--muted); font-family: var(--mono); font-size: 12px; margin-top: 10px; }}
  @media (max-width: 900px) {{
    .biscotti-top {{ grid-template-columns: 1fr; }}
    .biscotti-summary {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }}
  }}
</style>
</head>
<body>
  <div class="hero biscotti-hero">
    <h1 class="biscotti-title">Algo Biscotti</h1>
    <div class="hero-badge">PUBLIC PREVIEW</div>
    <p class="hero-sub">Unconditional loyalty. A monthly contrarian rotation.</p>
    <div class="biscotti-sub">Public free view of the Biscotti page. The chart and trade log below are real; the deeper per-algo detail stays for premium later.</div>
  </div>

  <div class="wrap">
    <section style="padding-top: 24px;">
      <div class="card biscotti-top">
        <div>
          <img class="biscotti-photo" src="biscotti.jpg" alt="Biscotti" />
          <div class="biscotti-label">Biscotti. The original signal.</div>
          <div class="biscotti-label" style="margin-top:6px;color:var(--text);font-style:italic;font-size:13px;line-height:1.5;">the best there is, the best there was, and the best there ever will be</div>
        </div>
        <div>
          <h2 class="section-title">What Biscotti does</h2>
          <p class="section-sub">The monthly contrarian rule that keeps showing up for the most beaten-down sector.</p>
          <div class="biscotti-note">Find the weakest SPDR sector ETF by 30-day return on the last trading day of each month. Buy the loser. Hold for one month. Repeat. No filters, no hesitation.</div>
          <div class="biscotti-note"><strong style="color:var(--text);">Why it exists:</strong> it is the kind of idea that sounds too simple until the tape proves otherwise.</div>
          <div class="biscotti-note"><strong style="color:var(--text);">What this page shows:</strong> the live paper-trade record, the equity curve, and the actual trade log.</div>
        </div>
      </div>
    </section>

    <section>
      <div class="wrap">
        <h2 class="section-title">Current record</h2>
        <p class="section-sub">The live paper-trade record as of the latest snapshot.</p>
        <div class="biscotti-summary">
          <div class="hero-stat"><div class="num">${last_equity:,.0f}</div><div class="label">Total equity</div></div>
          <div class="hero-stat"><div class="num">{(last_equity - start_equity):+.0f}</div><div class="label">Net P&amp;L</div></div>
          <div class="hero-stat"><div class="num">{((last_equity / start_equity - 1) * 100.0):+.2f}%</div><div class="label">Return</div></div>
          <div class="hero-stat"><div class="num">{max_dd * 100.0:+.2f}%</div><div class="label">Max drawdown</div></div>
          <div class="hero-stat"><div class="num">{win_rate:.0f}%</div><div class="label">Win rate</div></div>
          <div class="hero-stat"><div class="num">{len(trades)}</div><div class="label">Trades</div></div>
          <div class="hero-stat"><div class="num">{len(open_positions)}</div><div class="label">Open positions</div></div>
          <div class="hero-stat"><div class="num">{len(completed)}</div><div class="label">Closed trades</div></div>
        </div>
      </div>
    </section>

    <section>
      <div class="wrap">
        {chart_html}
      </div>
    </section>

    <section>
      <div class="wrap">
        <h2 class="section-title">Open position</h2>
        <p class="section-sub">What Biscotti is holding right now.</p>
        <div class="biscotti-table-wrap">
          <table>
            <thead>
              <tr><th>Ticker</th><th>Entry</th><th>Current</th><th>Unrealized</th><th>Value</th><th>Opened</th></tr>
            </thead>
            <tbody>
              {''.join(open_rows)}
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <section>
      <div class="wrap">
        <h2 class="section-title">Trade log</h2>
        <p class="section-sub">The actual paper-trade history for the signal.</p>
        <div class="biscotti-table-wrap">
          <table class="trade-table">
            <thead>
              <tr><th>Date</th><th>Action</th><th>Ticker</th><th>Price</th><th>Shares</th><th>Value</th><th>P&amp;L</th><th>Notes</th></tr>
            </thead>
            <tbody>
              {trade_rows_html}
            </tbody>
          </table>
        </div>
      </div>
    </section>
  </div>
{_footer_html(last_date, last_date, "Biscotti view")}
</body>
</html>"""


def build_families_page(families: dict, daily: dict) -> str:
    generated_at = families.get("generated_at", "")
    run_date = daily.get("run_date", "")
    cards = []
    for family_name, payload in sorted((families.get("families") or {}).items()):
        leaders = payload.get("leaders") or []
        status_mix_html = _status_mix_html(payload.get("by_status") or {})
        family_desc = FAMILY_DESCRIPTIONS.get(family_name, "A cluster of related signals grouped by theme so the board is easier to read.")
        family_title = FAMILY_TITLES.get(family_name, family_name)
        leader_rows = "".join(
            f"<li><strong>{_e(item.get('name'))}</strong> "
            f"<span class=\"{_ret_class(item.get('ytd_pct'))}\">{_fmt(item.get('ytd_pct'))}</span> "
            f"<span class=\"days\">({_e(_pretty_label(item.get('status') or 'n/a'))})</span></li>"
            for item in leaders[:5]
        ) or "<li>No leaders yet.</li>"
        cards.append(
            f"""
      <div class="card">
        <h2>{_e(family_title)}</h2>
        <p class="muted">Signals: {_e(payload.get('count', 0))}</p>
        <p class="muted" style="margin-top:8px;">{_e(family_desc)}</p>
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
<style>
  .family-legend ul {{ margin: 10px 0 0 18px; line-height: 1.7; }}
  .family-grid {{ margin-top: 20px; }}
  .page-title {{ color: var(--accent); font-size: clamp(28px, 5vw, 48px); font-weight: 700; letter-spacing: -0.5px; margin: 0 0 12px; }}
</style>
</head>
<body>
  <header>
    <h1 class="page-title">Signal Families</h1>
    <p>The lab grouped by theme instead of one flat wall of alternative experiments.</p>
  </header>
  <div class="wrap">
    {_status_legend_html()}
    <div class="grid family-grid">
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
<style>
  .daily-title {{ color: var(--accent); }}
  .wrap-table table {{ width: 100%; min-width: 0; table-layout: fixed; }}
  .wrap-table th, .wrap-table td {{ white-space: normal; word-break: break-word; }}
  .daily-list {{ margin: 0 auto; max-width: 680px; padding-left: 0; list-style-position: inside; text-align: center; line-height: 1.9; }}
</style>
</head>
<body>
<div class="hero">
  <div class="hero-badge">DAILY REPORT</div>
  <h1 class="daily-title">{_e(run_date)} nightly snapshot</h1>
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
    <p class="section-sub">Top live performers by year-to-date return.</p>
    <div class="table-wrap wrap-table">
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
    <p class="section-sub">Recent leaders over the last 30 days.</p>
    <ul class="daily-list">{rolling_rows}</ul>
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
<style>
  .legal-title {{ color: var(--accent); text-align: center; }}
  .legal-hero {{ text-align: center; }}
  .legal-page section .wrap {{ text-align: center; }}
  .legal-page section .wrap p {{ margin-left: auto; margin-right: auto; max-width: 900px; }}
</style>
</head>
<body class="legal-page">
<div class="hero legal-hero">
  <h1 class="legal-title">Disclaimers and disclosures</h1>
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
    rank_history = _load_rank_history()
    biscotti = json.loads((REPO / "docs" / "normal" / "biscotti" / "trades.json").read_text(encoding="utf-8"))

    out_lb = REPO / "docs" / "leaderboard.html"
    out_lb.write_text(build_leaderboard(daily, leaderboard), encoding="utf-8")
    print(f"[pages] wrote {out_lb}")

    out_landing = REPO / "docs" / "landing.html"
    out_landing.write_text(build_landing(leaderboard, daily, rank_history), encoding="utf-8")
    print(f"[pages] wrote {out_landing}")

    out_index = REPO / "docs" / "index.html"
    out_index.write_text(build_landing(leaderboard, daily, rank_history), encoding="utf-8")
    print(f"[pages] wrote {out_index}")

    out_signals = REPO / "docs" / "signals" / "index.html"
    out_signals.write_text(build_signals_index(leaderboard, daily), encoding="utf-8")
    print(f"[pages] wrote {out_signals}")

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

    out_biscotti = REPO / "docs" / "biscotti.html"
    out_biscotti.write_text(build_biscotti_page(biscotti), encoding="utf-8")
    print(f"[pages] wrote {out_biscotti}")


def main():
    build_main()


if __name__ == "__main__":
    main()
