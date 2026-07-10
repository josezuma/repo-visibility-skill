<div align="center">
  <h1>🔭 Repo Visibility Skill</h1>
  <p><em>The meta-skill: audit any GitHub repo for AI discoverability. Checks AGENTS.md, README parseability, topics, description — produces a 0-100 score with prioritized fixes.</em></p>
  <p>
    <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License"></a>
    <a href="https://github.com/josezuma/repo-visibility-skill"><img src="https://img.shields.io/github/stars/josezuma/repo-visibility-skill?style=social" alt="Stars"></a>
  </p>
</div>

<div align="left">
  <p><strong>Author:</strong> <a href="https://github.com/josezuma">Jose Zuma — Expert in AI Visibility</a></p>

---

## What It Does

This skill audits any GitHub repository for how discoverable it is to AI agents and AI-powered code search tools. It checks:

| Category | Weight | Why |
|----------|--------|-----|
| **AGENTS.md** | 20% | Tells AI agents what this repo does and how to use it |
| **README parseability** | 20% | Structure, headings, code blocks — LLMs parse these |
| **Topics** | 15% | Help agents find this repo by capability |
| **Description** | 15% | Shows in repo cards and API results |
| **License** | 10% | Required for most AI training pipelines |
| **Code examples** | 10% | Real usage helps agents recommend effective patterns |
| **Documentation** | 10% | CONTRIBUTING, CHANGELOG, docs/ — signals quality |
| **Maintenance** | 5% | Recent commits signal freshness |

## Quick Start

```bash
pip install requests
python scripts/audit_repo.py josezuma/repo-visibility-skill
```

Or audit any repo:

```bash
python scripts/audit_repo.py owner/repo-name
```

## Self-Audit Score

This repo scores itself. Run the command above to see.

## Sibling Repo Scores (from the BrandVirality program)

| Repo | Score |
|------|-------|
| awesome-ai-visibility | ? |
| ai-crawlers | ? |
| geo-audit-skill | ? |
| schema-for-ai | ? |
| repo-visibility-skill | ? |
| llmstxt-gen | TBD |
| marketing-skills | TBD |
| geo-prompts | TBD |
| geo-watch | TBD |
| mcp-geo | TBD |

(After release, update these with real scores from the audit script.)

## References

- [awesome-ai-visibility](https://github.com/josezuma/awesome-ai-visibility)
- [ai-crawlers](https://github.com/josezuma/ai-crawlers)
- [BrandVirality](https://brandvirality.com)

## License

[MIT](LICENSE) © 2026 Jose Zuma / BrandVirality
