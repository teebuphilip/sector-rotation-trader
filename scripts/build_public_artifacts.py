#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PRODUCT_DIR = ROOT / 'data' / 'product'
SIGNALS_DIR = ROOT / 'docs' / 'signals'
ROLLING_PATH = ROOT / 'docs' / 'leaderboards' / 'rolling_30d.json'
RANK_HISTORY_PATH = ROOT / 'data' / 'rank_history.csv'
PUBLIC_DIR = ROOT / 'docs' / 'data' / 'public'
BENCHMARKS_DIR = PUBLIC_DIR / 'benchmarks'
PUBLIC_SIGNALS_DIR = PUBLIC_DIR / 'signals'


def _load_json(path: Path) -> Any:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except Exception:
        return None


def _write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + '\n', encoding='utf-8')


def _copy_signal_json_tree() -> int:
    if not SIGNALS_DIR.exists():
        return 0
    copied = 0
    for src in SIGNALS_DIR.rglob('*.json'):
        rel = src.relative_to(SIGNALS_DIR)
        dest = PUBLIC_SIGNALS_DIR / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, dest)
        copied += 1
    return copied


def _rank_map() -> dict[tuple[str, str], dict[str, Any]]:
    out: dict[tuple[str, str], dict[str, Any]] = {}
    if not RANK_HISTORY_PATH.exists():
        return out
    with RANK_HISTORY_PATH.open(encoding='utf-8', newline='') as f:
        rows = list(csv.DictReader(f))
    if not rows:
        return out
    latest_date = rows[-1].get('date')
    for row in rows:
        if row.get('date') != latest_date:
            continue
        algo_type = str(row.get('algo_type') or '').strip()
        algo_id = str(row.get('algo_id') or '').strip()
        if not algo_type or not algo_id:
            continue
        out[(algo_type, algo_id)] = row
    return out


def _rolling_map() -> tuple[dict[tuple[str, str], dict[str, Any]], dict[str, Any]]:
    data = _load_json(ROLLING_PATH)
    out: dict[tuple[str, str], dict[str, Any]] = {}
    if not isinstance(data, dict):
        return out, {}
    for row in data.get('entries', []):
        if not isinstance(row, dict):
            continue
        algo_id = str(row.get('algo_id') or '').strip()
        category = str(row.get('category') or '').strip().lower()
        if not algo_id:
            continue
        algo_type = 'normal' if category == 'standard' else category
        if algo_type not in {'normal', 'crazy'}:
            continue
        out[(algo_type, algo_id)] = row
    return out, data


def _to_float(value: Any) -> float | None:
    try:
        return float(value)
    except Exception:
        return None


def _strip_algo_row(
    item: dict[str, Any],
    rank: dict[str, Any] | None,
    rolling: dict[str, Any] | None,
    spy_ret_30d: float | None,
) -> dict[str, Any]:
    spy_pct = _to_float((rank or {}).get('spy_pct'))
    alpha_pct = _to_float((rank or {}).get('alpha_pct'))
    beat_spy_raw = (rank or {}).get('beat_spy')
    beat_spy = None
    if isinstance(beat_spy_raw, bool):
        beat_spy = beat_spy_raw
    elif isinstance(beat_spy_raw, str) and beat_spy_raw:
        beat_spy = beat_spy_raw.lower() == 'true'

    ret_30d = _to_float((rolling or {}).get('ret_30d'))
    spy_delta_30d = None
    if ret_30d is not None and spy_ret_30d is not None:
        spy_delta_30d = round((ret_30d - spy_ret_30d) * 100.0, 2)

    return {
        'key': item.get('key'),
        'algo_type': item.get('algo_type'),
        'algo_id': item.get('algo_id'),
        'name': item.get('name'),
        'family': item.get('family'),
        'status': item.get('status'),
        'evidence_class': item.get('evidence_class'),
        'rebalance_frequency': item.get('rebalance_frequency'),
        'ytd_pct': item.get('ytd_pct'),
        'days_running': int((rank or {}).get('days_running') or 0),
        'beat_spy': beat_spy,
        'spy_pct': spy_pct,
        'alpha_pct': alpha_pct,
        'ret_30d_pct': round(ret_30d * 100.0, 2) if ret_30d is not None else None,
        'spy_delta_30d_pct': spy_delta_30d,
        'last_snapshot': item.get('last_snapshot'),
        'new_algo_date': item.get('new_algo_date'),
    }


def _sort_public_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    def key(row: dict[str, Any]) -> tuple[float, float, str]:
        return (
            float(row.get('ytd_pct') or -9999.0),
            float(row.get('alpha_pct') or -9999.0),
            str(row.get('algo_id') or ''),
        )
    return sorted(rows, key=key, reverse=True)


def _build_benchmarks(rank_rows: dict[tuple[str, str], dict[str, Any]], rolling_doc: dict[str, Any]) -> dict[str, dict[str, Any]]:
    spy_ytd = None
    for row in rank_rows.values():
        spy_ytd = _to_float(row.get('spy_pct'))
        if spy_ytd is not None:
            break

    spy = {
        'symbol': 'SPY',
        'available': True,
        'generated_at': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'ytd_return_pct': spy_ytd,
        'rolling_30d_return_pct': round(float(rolling_doc.get('spy_ret_30d')) * 100.0, 2) if rolling_doc.get('spy_ret_30d') is not None else None,
        'source': 'data/rank_history.csv + docs/leaderboards/rolling_30d.json',
    }
    qqq = {
        'symbol': 'QQQ',
        'available': False,
        'generated_at': spy['generated_at'],
        'ytd_return_pct': None,
        'rolling_30d_return_pct': None,
        'source': None,
        'reason': 'QQQ nightly benchmark not wired yet; contract file exists now so the public site can rely on a stable path.',
    }
    return {'spy': spy, 'qqq': qqq}


def main() -> int:
    PUBLIC_DIR.mkdir(parents=True, exist_ok=True)
    BENCHMARKS_DIR.mkdir(parents=True, exist_ok=True)

    algos_index = _load_json(PRODUCT_DIR / 'algos_index.json') or {}
    daily_summary = _load_json(PRODUCT_DIR / 'daily_summary.json') or {}
    families = _load_json(PRODUCT_DIR / 'families.json') or {}
    watchlist = _load_json(PRODUCT_DIR / 'watchlist.json') or {}
    promoted = _load_json(PRODUCT_DIR / 'promoted.json') or {}
    graveyard = _load_json(PRODUCT_DIR / 'graveyard.json') or {}
    signals_index = _load_json(SIGNALS_DIR / 'index.json') or {}

    rank_rows = _rank_map()
    rolling_rows, rolling_doc = _rolling_map()

    spy_ret_30d = _to_float((rolling_doc or {}).get('spy_ret_30d'))

    public_algos = []
    for item in algos_index.get('algos', []):
        if not isinstance(item, dict):
            continue
        rank = rank_rows.get((str(item.get('algo_type') or ''), str(item.get('algo_id') or '')))
        rolling = rolling_rows.get((str(item.get('algo_type') or ''), str(item.get('algo_id') or '')))
        public_algos.append(_strip_algo_row(item, rank, rolling, spy_ret_30d))
    public_algos = _sort_public_rows(public_algos)

    def project_block(block: dict[str, Any]) -> dict[str, Any]:
        rows = []
        for item in block.get('algos', []):
            if not isinstance(item, dict):
                continue
            rank = rank_rows.get((str(item.get('algo_type') or ''), str(item.get('algo_id') or '')))
            rolling = rolling_rows.get((str(item.get('algo_type') or ''), str(item.get('algo_id') or '')))
            rows.append(_strip_algo_row(item, rank, rolling, spy_ret_30d))
        return {
            'generated_at': block.get('generated_at'),
            'algos': _sort_public_rows(rows),
        }

    public_families: dict[str, Any] = {'generated_at': families.get('generated_at'), 'families': {}}
    for family_name, payload in (families.get('families') or {}).items():
        rows = []
        for item in payload.get('leaders', []):
            if not isinstance(item, dict):
                continue
            rank = rank_rows.get((str(item.get('algo_type') or ''), str(item.get('algo_id') or '')))
            rolling = rolling_rows.get((str(item.get('algo_type') or ''), str(item.get('algo_id') or '')))
            rows.append(_strip_algo_row(item, rank, rolling, spy_ret_30d))
        public_families['families'][family_name] = {
            'family': payload.get('family', family_name),
            'count': payload.get('count', 0),
            'by_status': payload.get('by_status', {}),
            'by_evidence_class': payload.get('by_evidence_class', {}),
            'leaders': _sort_public_rows(rows)[:5],
        }

    daily_payload = {
        'run_date': daily_summary.get('run_date') or signals_index.get('generated'),
        'generated_at': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'counts': daily_summary.get('counts', {}),
        'by_status': daily_summary.get('by_status', {}),
        'by_evidence_class': daily_summary.get('by_evidence_class', {}),
        'new_algos_today': daily_summary.get('new_algos_today', []),
        'top_bullish_etfs': signals_index.get('top_bullish_etfs', []),
        'top_bearish_etfs': signals_index.get('top_bearish_etfs', []),
        'ticker_count': signals_index.get('ticker_count'),
        'signal_count': signals_index.get('signal_count'),
        'sector_summary': signals_index.get('sector_summary', {}),
        'top_live_ytd': _sort_public_rows([
            _strip_algo_row(
                item,
                rank_rows.get((str(item.get('algo_type') or ''), str(item.get('algo_id') or ''))),
                rolling_rows.get((str(item.get('algo_type') or ''), str(item.get('algo_id') or ''))),
                spy_ret_30d,
            )
            for item in daily_summary.get('top_live_ytd', [])
            if isinstance(item, dict)
        ])[:10],
        'rolling_30d': {
            'as_of': rolling_doc.get('as_of'),
            'spy_ret_30d_pct': round(float(rolling_doc.get('spy_ret_30d')) * 100.0, 2) if rolling_doc.get('spy_ret_30d') is not None else None,
            'leaders': [
                {
                    'algo_id': row.get('algo_id'),
                    'name': row.get('name'),
                    'algo_type': 'normal' if row.get('category') == 'standard' else row.get('category'),
                    'ret_30d_pct': round(float(row.get('ret_30d')) * 100.0, 2) if row.get('ret_30d') is not None else None,
                    'vs_spy_30d_pct': round((float(row.get('ret_30d')) - float(rolling_doc.get('spy_ret_30d'))) * 100.0, 2) if row.get('ret_30d') is not None and rolling_doc.get('spy_ret_30d') is not None else None,
                }
                for row in (rolling_doc.get('entries') or [])[:10]
                if isinstance(row, dict)
            ],
        },
    }

    leaderboard_payload = {
        'generated_at': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'counts': {
            'total': len(public_algos),
            'beating_spy': sum(1 for row in public_algos if row.get('beat_spy') is True),
        },
        'algos': public_algos,
    }

    _write_json(PUBLIC_DIR / 'daily.json', daily_payload)
    _write_json(PUBLIC_DIR / 'leaderboard.json', leaderboard_payload)
    _write_json(PUBLIC_DIR / 'families.json', public_families)
    _write_json(PUBLIC_DIR / 'watchlist.json', project_block(watchlist))
    _write_json(PUBLIC_DIR / 'promoted.json', project_block(promoted))
    _write_json(PUBLIC_DIR / 'graveyard.json', project_block(graveyard))

    benchmarks = _build_benchmarks(rank_rows, rolling_doc)
    _write_json(BENCHMARKS_DIR / 'spy.json', benchmarks['spy'])
    _write_json(BENCHMARKS_DIR / 'qqq.json', benchmarks['qqq'])

    copied = _copy_signal_json_tree()

    print(f'[public] wrote {PUBLIC_DIR / "daily.json"}')
    print(f'[public] wrote {PUBLIC_DIR / "leaderboard.json"}')
    print(f'[public] wrote {PUBLIC_DIR / "families.json"}')
    print(f'[public] wrote {PUBLIC_DIR / "watchlist.json"}')
    print(f'[public] wrote {PUBLIC_DIR / "promoted.json"}')
    print(f'[public] wrote {PUBLIC_DIR / "graveyard.json"}')
    print(f'[public] wrote {BENCHMARKS_DIR / "spy.json"}')
    print(f'[public] wrote {BENCHMARKS_DIR / "qqq.json"}')
    print(f'[public] copied {copied} signal JSON files into {PUBLIC_SIGNALS_DIR}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
