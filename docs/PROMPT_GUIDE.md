# Internal Prompting Guide

1. **Spec-first mindset**
   - Draft `PROJECT_SPEC.md` and `TECHNICAL_SPEC.md` before coding.
   - Summarize acceptance criteria and tests to guide AI responses.

2. **Context windows**
   - Link to relevant files via `files_include` instead of pasting long snippets.
   - Reference `docs/CLAUDE.md` for repo map and testing strategy.

3. **Review loops**
   - Ask assistants to self-critique using `prompts/global/review_checklist.md`.
   - Capture key decisions in `docs/DECISIONS.md`.

4. **Tool safety**
   - Prefer MCP servers defined in `mcp/servers/*.json` for filesystem, Git, HTTP.
   - Avoid direct shell commands with side effects unless running locally with manual approval.

5. **Git hygiene**
   - Require clean working trees before enabling auto-accept.
   - Commit frequently with descriptive messages to preserve rollback points.
