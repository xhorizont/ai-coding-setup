"""Generate AI-assisted PR review notes."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from adapters.openai_client import OpenAIClient, OpenAIConfig

PROMPT_PATH = Path(__file__).resolve().parents[2] / "prompts" / "global" / "review_checklist.md"


def main() -> None:
    parser = argparse.ArgumentParser(description="AI review helper")
    parser.add_argument("--diff", required=True, help="Path to diff file")
    parser.add_argument("--model", default="o3-mini-high")
    args = parser.parse_args()

    diff_text = Path(args.diff).read_text(encoding="utf-8")
    config = OpenAIConfig(api_key="sk-placeholder", model=args.model)
    client = OpenAIClient(config)
    instructions = PROMPT_PATH.read_text(encoding="utf-8")

    review = client.review(diff_text, instructions)
    print(json.dumps(review, indent=2))


if __name__ == "__main__":
    main()
