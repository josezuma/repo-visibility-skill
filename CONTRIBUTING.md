# Contributing to repo-visibility-skill

Thanks for contributing!

## Adding Audit Checks

1. Add the check logic to `scripts/audit_repo.py`
2. Add the weight to the `AUDIT_WEIGHTS` dict
3. Run `python scripts/audit_repo.py josezuma/repo-visibility-skill` to verify
4. Update SKILL.md documentation

## Standards

- Keep the scoring rubric documented in SKILL.md
- Real API calls only — no simulated data
- Each check must have a clear reason documented
