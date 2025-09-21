Safety constraints:
- Never execute destructive commands (e.g., `rm -rf`, dropping databases) without explicit human approval.
- Do not exfiltrate secrets; redact tokens and credentials.
- Prefer MCP tools over raw shell access for filesystem/Git/HTTP interactions.
- Pause and request clarification when requirements conflict with `docs/SECURITY.md`.
