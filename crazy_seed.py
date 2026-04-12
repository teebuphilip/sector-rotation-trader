import argparse
from pathlib import Path

from crazy.seed import seed_all

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--algo-id", action="append", help="Algo id/name/class to seed (repeatable)")
    parser.add_argument("--algo-file", action="append", help="Algo .py file to seed (repeatable)")
    args = parser.parse_args()

    algo_ids = []
    if args.algo_id:
        algo_ids.extend(args.algo_id)
    if args.algo_file:
        for path in args.algo_file:
            stem = Path(path).stem
            algo_ids.append(stem.replace("_", "-"))

    seed_all(algo_ids or None)
