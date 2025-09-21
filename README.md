# AI Coding Setup

Repository skeleton for orchestrating AI-assisted software development across multiple providers (Anthropic Claude, OpenAI, Google Gemini, DeepSeek, Ollama, ...). It codifies spec-first habits, safe Git checkpoints, MCP tool access, and shared prompts so teams can bootstrap new projects quickly.

## Quick start

1. Copy `.env.example` to `.env` and fill in provider API keys.
2. Run `make setup` to install dependencies and register recommended pre-commit hooks.
3. Explore the docs:
   - `docs/PROJECT_SPEC.md` for business goals
   - `docs/TECHNICAL_SPEC.md` for architecture plans
   - `docs/CLAUDE.md` for Claude-oriented practices (MCP, git hygiene, auto-accept policy)
4. Trigger workflows with `python scripts/ai/run_workflow.py --task spec-first --assistant anthropic/claude-3.7-sonnet`.

## Repository layout

See `docs/CLAUDE.md` and `docs/PROJECT_SPEC.md` for full descriptions. Highlights:

- `assistants/` – parameter files per provider/model.
- `prompts/` – reusable prompt modules (system/global/task).
- `workflows/` – orchestration recipes for spec-first, review, and migration flows.
- `mcp/servers/` – Model Context Protocol definitions for safe tool use.
- `scripts/` – automation helpers (AI workflows + repo bootstrap/validation).

## Recommended reading

- [Claude Code best practices](https://www.anthropic.com/engineering/claude-code-best-practices)
- [Claude Code quickstart (YouTube)](https://www.youtube.com/watch?v=amEUIuBKwvg)
- [Agentic workflows deep-dive (YouTube)](https://www.youtube.com/watch?v=T0zFZsr_d0Q)

Adopt spec-first planning and commit often for recoverable checkpoints.
