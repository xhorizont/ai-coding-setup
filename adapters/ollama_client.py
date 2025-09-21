"""Adapter for local Ollama models."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class OllamaConfig:
    host: str
    model: str


class OllamaClient:
    def __init__(self, config: OllamaConfig) -> None:
        self.config = config

    def chat(self, prompt: str) -> Dict[str, Any]:
        """Return placeholder response for local experimentation."""

        return {
            "host": self.config.host,
            "model": self.config.model,
            "prompt": prompt,
        }
