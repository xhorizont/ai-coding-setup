# Test Strategy

## Principles
- Write tests alongside specifications (TDD/BDD hybrid).
- Ensure each AI-generated change ships with unit coverage and, where relevant, e2e validation.

## Layers
1. **Unit tests** – Fast, deterministic, run on save.
2. **Integration tests** – Cover API/service boundaries.
3. **End-to-end tests** – Validate core user journeys with fixture data.

## Automation
- CI workflow (`.github/workflows/ci.yml`) blocks merges on failing tests.
- `scripts/ai/run_workflow.py` can request assistants to generate missing tests before implementation.

## Edge cases
- Document tricky scenarios in `prompts/global/test_plan_template.md`.
- Add regression tests whenever bugs are triaged.

## Tooling
- `pytest` with coverage.
- Optional: property-based testing via `hypothesis` (add to `requirements.txt` when needed).
