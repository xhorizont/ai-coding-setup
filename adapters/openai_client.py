"""Adapter for OpenAI responses."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class OpenAIConfig:
    api_key: str
    model: str


class OpenAIClient:
    def __init__(self, config: OpenAIConfig) -> None:
        self.config = config

    def review(self, diff: str, instructions: str) -> Dict[str, Any]:
        """Stub review call for PR feedback."""

        return {
            "model": self.config.model,
            "summary": "Review not yet implemented.",
            "diff": diff,
            "instructions": instructions,
        }
