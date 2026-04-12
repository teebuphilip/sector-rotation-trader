import importlib
from pathlib import Path


REGISTRY_PATH = Path("data/algos_registry_crazy.txt")


def get_crazy_algos():
    if not REGISTRY_PATH.exists():
        print(f"[registry] missing {REGISTRY_PATH}, no crazy algos loaded")
        return []

    algos = []
    lines = REGISTRY_PATH.read_text(encoding="utf-8").splitlines()
    for line in lines:
        raw = line.strip()
        if not raw or raw.startswith("#"):
            continue
        if ":" not in raw:
            print(f"[registry] bad line: {raw}")
            continue
        module_name, class_name = raw.split(":", 1)
        module_name = module_name.strip()
        class_name = class_name.strip()
        try:
            module = importlib.import_module(f"crazy.algos.{module_name}")
            cls = getattr(module, class_name)
            algos.append(cls())
        except Exception as exc:
            print(f"[registry] failed to load {module_name}:{class_name} -> {exc}")

    return algos
