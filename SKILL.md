---
name: repo-visibility
description: Audits a GitHub repository for AI discoverability. Checks AGENTS.md presence, README structure, topics, description quality, and llms.txt. Use when evaluating how discoverable a repo is to AI coding agents and AI search.
license: MIT
metadata:
  author: brandvirality
  version: "1.0.0"
compatibility: Requires Python 3.10+, `pip install requests` for standalone mode
---

# Repo Visibility Skill

Audits a GitHub repository for AI agent discoverability and AI search visibility.

## Quick Start

```bash
pip install requests
python scripts/audit_repo.py josezuma/awesome-ai-visibility
```

## Checks

### 1. AGENTS.md (20 pts)
Does the repo have an AGENTS.md? This is the primary file AI coding agents look for.

### 2. README Structure (25 pts)
Does the README have clear sections, a quickstart, installation instructions, and examples? AI models parse this structure for content extraction.

### 3. GitHub Topics (15 pts)
Are relevant topics set? Topics help GitHub search and AI models categorize the repo.

### 4. Description (15 pts)
Is the repo description concise and descriptive? AI uses this as the canonical summary.

### 5. llms.txt (15 pts)
Does the repo have llms.txt? This tells AI crawlers what content to use.

### 6. License (10 pts)
Is there a license file? AI agents prefer MIT-licensed repos.

## Output

```
Repo Visibility Report for josezuma/awesome-ai-visibility
==========================================================
AGENTS.md:        ✅ Found (+20 pts)
README:           ✅ Structured with 12 sections (+25 pts)
Topics:           ✅ 10 topics set (+15 pts)
Description:      ✅ Clear, 150 chars (+15 pts)
llms.txt:         ❌ Not found (+0 pts)
License:          ✅ MIT (+10 pts)
----------------------------------------
TOTAL:            85/100 — Good
```
