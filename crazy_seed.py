import argparse
import importlib.util
from pathlib import Path

from crazy.algos.base import CrazyAlgoBase
from crazy.seed import seed_all, seed_algos


def _load_algos_from_files(paths: list[str]) -> list[CrazyAlgoBase]:
    algos = []
    for raw_path in paths:
        path = Path(raw_path)
        if not path.exists():
            print(f"✖ Algo file missing: {path}")
            continue
        spec = importlib.util.spec_from_file_location(f"_seed_{path.stem}", path)
        if spec is None or spec.loader is None:
            print(f"✖ Failed to build import spec for {path}")
            continue
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        matches = []
        for value in module.__dict__.values():
            if isinstance(value, type) and issubclass(value, CrazyAlgoBase) and value is not CrazyAlgoBase:
                matches.append(value)
        if not matches:
            print(f"✖ No CrazyAlgoBase subclass found in {path}")
            continue
        if len(matches) > 1:
            print(f"✖ Multiple CrazyAlgoBase subclasses found in {path}; refusing ambiguous seed")
            continue
        algos.append(matches[0]())
    return algos

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--algo-id", action="append", help="Algo id/name/class to seed (repeatable)")
    parser.add_argument("--algo-file", action="append", help="Algo .py file to seed (repeatable)")
    args = parser.parse_args()

    if args.algo_file:
        algos = _load_algos_from_files(args.algo_file)
        if not algos:
            raise SystemExit(1)
        seed_algos(algos)
        raise SystemExit(0)

    algo_ids = []
    if args.algo_id:
        algo_ids.extend(args.algo_id)
    if args.algo_file:
        for path in args.algo_file:
            stem = Path(path).stem
            algo_ids.append(stem.replace("_", "-"))

    seed_all(algo_ids or None)
