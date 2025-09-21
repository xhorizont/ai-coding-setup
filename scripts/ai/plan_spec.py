"""Helper to draft specs with AI assistance."""
from __future__ import annotations

import argparse
from pathlib import Path

import yaml

DOCS_ROOT = Path(__file__).resolve().parents[2] / "docs"


def read_markdown(filename: str) -> str:
    path = DOCS_ROOT / filename
    return path.read_text(encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Prepare spec context for AI")
    parser.add_argument("--project", default="PROJECT_SPEC.md")
    parser.add_argument("--technical", default="TECHNICAL_SPEC.md")
    args = parser.parse_args()

    context = {
        "project_spec": read_markdown(args.project),
        "technical_spec": read_markdown(args.technical),
        "prompt_guide": read_markdown("PROMPT_GUIDE.md"),
    }
    print(yaml.safe_dump(context, sort_keys=False))


if __name__ == "__main__":
    main()
