"""Thin wrapper for Anthropic Claude models."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class AnthropicConfig:
    api_key: str
    model: str
    max_tokens: int = 4096


class AnthropicClient:
    """Minimal client interface for workflows."""

    def __init__(self, config: AnthropicConfig) -> None:
        self.config = config

    def invoke(self, prompt: str, **kwargs: Any) -> Dict[str, Any]:
        """Stub method to invoke Claude API.

        Replace with real anthropic SDK calls. Keep parameters explicit to make auditing easy.
        """

        return {
            "model": self.config.model,
            "prompt": prompt,
            "metadata": {"max_tokens": kwargs.get("max_tokens", self.config.max_tokens)},
        }
