# Contributing

Thank you for helping build this AI coding toolkit.

## Workflow
1. Open an issue describing the change.
2. Update `PROJECT_SPEC.md` or `TECHNICAL_SPEC.md` if the scope impacts product or architecture.
3. Implement changes in a feature branch, keeping commits small and reversible.
4. Run `make check` before opening a PR.
5. Request AI + human review.

## Commit conventions
- Use conventional commits (`feat:`, `fix:`, `docs:` ...).
- Reference related ADRs when appropriate.

## Code style
- Python: Black + Ruff enforced via pre-commit.
- Markdown: wrap at 100 characters when possible.

## Testing
- Add or update tests in `tests/`.
- Include regression coverage for bug fixes.

## Security & privacy
- Do not commit secrets.
- Use MCP tools for privileged operations; avoid shell scripts with destructive commands.
