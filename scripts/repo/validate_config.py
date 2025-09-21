"""Validate assistant configuration files."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Dict

import yaml

ROOT = Path(__file__).resolve().parents[2]
ASSISTANTS_DIR = ROOT / "assistants"


def validate_yaml(path: Path) -> None:
    with path.open("r", encoding="utf-8") as handle:
        yaml.safe_load(handle)


def validate_json(path: Path) -> None:
    json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    yaml_files = list(ROOT.glob("**/*.yaml")) + list(ROOT.glob("**/*.yml"))
    json_files = list(ROOT.glob("**/*.json"))

    for file in yaml_files:
        validate_yaml(file)
    for file in json_files:
        validate_json(file)

    providers: Dict[str, int] = {}
    for model_file in ASSISTANTS_DIR.glob("**/*.yaml"):
        data = yaml.safe_load(model_file.read_text(encoding="utf-8"))
        provider = data.get("provider")
        if not provider:
            continue
        providers[provider] = providers.get(provider, 0) + 1

    print("Validated configuration files.")
    print("Model counts by provider:", providers)


if __name__ == "__main__":
    main()
