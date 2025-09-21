# Security Guidelines

## Secrets management
- Store credentials in `.env` (never commit to Git).
- Limit scope of API keys (read-only where possible).

## Access controls
- Use MCP servers with scoped permissions (see `mcp/servers/*.json`).
- Rotate API keys quarterly and after incidents.

## Data handling
- Redact PII before pasting into prompts.
- Avoid exporting production data; prefer synthetic fixtures.

## Incident response
- Document incidents in `docs/DECISIONS.md` (link to ticket).
- Revoke compromised keys and regenerate.

## Compliance
- Ensure third-party providers comply with company policy (GDPR, SOC2, etc.).
