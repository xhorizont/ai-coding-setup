"""Adapter for Google Gemini models."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class GoogleConfig:
    api_key: str
    model: str


class GoogleClient:
    def __init__(self, config: GoogleConfig) -> None:
        self.config = config

    def ideate(self, topic: str) -> Dict[str, Any]:
        """Return brainstorming suggestions (stub)."""

        return {
            "model": self.config.model,
            "ideas": [f"Investigate {topic} with design spikes."],
        }
