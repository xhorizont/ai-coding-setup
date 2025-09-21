# Claude Code Playbook

This repository follows Anthropic's Claude Code best practices for agentic development.

## Overview
- **Goal:** Provide a safe, spec-driven environment for AI pair programming.
- **Primary assistant:** `anthropic/claude-3.7-sonnet` (see `assistants/anthropic/models/claude-3.7-sonnet.yaml`).
- **Supporting tools:** Model Context Protocol (MCP) servers for filesystem, Git, HTTP, and GitHub interactions (`mcp/servers/*.json`).

## Repo map
- `docs/` – Specifications, decisions, prompting guides.
- `prompts/` – Modular prompt snippets to compose workflows.
- `assistants/` – Model parameters, safety rails, and workflow bindings.
- `scripts/ai/` – Entry points for spec-first planning, implementation, and PR review.
- `workflows/` – YAML recipes orchestrating multi-step tasks.
- `tests/` – Unit and e2e suites (create new modules per feature).

## Setup & test
```bash
python scripts/repo/setup_wizard.py
make setup
make test
```
Run the wizard whenever you change assistant routing or credentials (`--check` performs validation without prompts).

## Run & test
```bash
make setup
make test
```

Ensure tests are green before enabling auto-accept or merging.

## Collaboration contract
1. **Spec-first:** Draft or update `PROJECT_SPEC.md` and `TECHNICAL_SPEC.md` before coding. Request Claude to critique specs prior to implementation.
2. **Plan → Implement → Test → Review:** Follow `workflows/spec-first.yml`. Each stage outputs artifacts and checkpoints.
3. **Git hygiene:**
   - Keep the working tree clean (`git status`).
   - Commit frequently with descriptive messages (`docs/DECISIONS.md` for rationale).
   - Store safe checkpoints before large refactors.
4. **Auto-accept discipline:**
   - Default `auto_accept: false` (see model configs).
   - Only enable in experimental branches with manual oversight and immediate review.
5. **Tool use:**
   - Prefer MCP servers instead of raw shell commands for sensitive operations.
   - Avoid destructive commands (`rm -rf`, schema migrations) without explicit human approval.
6. **Security:**
   - Secrets stay in `.env` (never commit).
   - Follow `docs/SECURITY.md` guidelines for data handling.

## Review loop
- Self-review using `prompts/global/review_checklist.md` before requesting human review.
- Run `make check` locally to lint, type-check, and test.
- Tag PRs with spec/test links for traceability.

## Escalation
- If Claude is uncertain, request clarification or fallback to human pairing.
- Document any limitations or blocked tasks in `docs/DECISIONS.md` or issue tracker.
