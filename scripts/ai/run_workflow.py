"""Entry point for running AI workflows."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict

import yaml

CONFIG_ROOT = Path(__file__).resolve().parents[2] / "configs"
WORKFLOW_ROOT = Path(__file__).resolve().parents[2] / "workflows"


def load_yaml(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run AI workflow")
    parser.add_argument("--task", required=True, help="Workflow name (e.g., spec-first)")
    parser.add_argument("--assistant", required=True, help="assistant path like provider/model")
    args = parser.parse_args()

    workflow_file = WORKFLOW_ROOT / f"{args.task}.yml"
    if not workflow_file.exists():
        raise SystemExit(f"Workflow {args.task} not found: {workflow_file}")

    config = load_yaml(CONFIG_ROOT / "assistants.yaml")
    assigned = config.get("tasks", {}).get(args.task)
    if assigned and assigned != args.assistant:
        print(f"[warn] Task {args.task} typically uses {assigned}, overriding with {args.assistant}")

    workflow = load_yaml(workflow_file)
    print(json.dumps({"assistant": args.assistant, "workflow": workflow}, indent=2))


if __name__ == "__main__":
    main()
