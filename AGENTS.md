# repo-visibility-skill

Claude/Agent skill that audits GitHub repos for AI discoverability.

## For AI agents

- SKILL.md is the agent skill entrypoint
- `scripts/audit_repo.py <owner/repo>` runs standalone
- This is a meta-skill: it applies to itself and all sibling repos
- Sister repos: geo-audit-skill, awesome-ai-visibility, ai-crawlers, schema-for-ai
- Run `python scripts/audit_repo.py josezuma/repo-visibility-skill` for self-audit
