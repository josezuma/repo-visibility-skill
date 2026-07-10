#!/usr/bin/env python3
"""Audit a GitHub repo for AI discoverability."""

import sys
import json
import urllib.request
import urllib.error
import os

SCORE_TOTAL = 100
WEIGHTS = {
    'agents_md': 20,
    'readme': 25,
    'topics': 15,
    'description': 15,
    'llms_txt': 15,
    'license': 10,
}


def api_get(url):
    """Make a GitHub API GET request."""
    req = urllib.request.Request(url)
    token = os.environ.get('GITHUB_TOKEN', '')
    if token:
        req.add_header('Authorization', f'token {token}')
    req.add_header('Accept', 'application/vnd.github.v3+json')
    req.add_header('User-Agent', 'repo-visibility-audit/1.0')
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        body = e.read().decode()[:200]
        return {'error': f'HTTP {e.code}', 'raw': body, 'url': url}
    except Exception as e:
        return {'error': str(e), 'url': url}


def audit(repo_full):
    """Run the full audit on a repo."""
    parts = repo_full.split('/')
    owner, repo = parts[0], parts[1]

    results = {}
    total = 0
    findings = []

    # 1. Get repo metadata via GitHub API
    repo_data = api_get(f'https://api.github.com/repos/{owner}/{repo}')
    if 'error' in repo_data:
        return {'error': f'Cannot access {repo_full}: {repo_data["error"]}'}

    # Check description
    desc = repo_data.get('description', '') or ''
    if len(desc) >= 20:
        results['description'] = WEIGHTS['description']
        findings.append(f'✅ Description: {len(desc)} chars — good (+{WEIGHTS["description"]} pts)')
    elif desc:
        results['description'] = WEIGHTS['description'] // 2
        findings.append(f'⚠️ Description: only {len(desc)} chars — too short (+{results["description"]} pts)')
    else:
        results['description'] = 0
        findings.append(f'❌ No description (+0 pts)')

    # Check topics
    topics = repo_data.get('topics', [])
    if len(topics) >= 5:
        results['topics'] = WEIGHTS['topics']
        findings.append(f'✅ {len(topics)} topics set: {", ".join(topics[:5])} (+{WEIGHTS["topics"]} pts)')
    elif topics:
        results['topics'] = WEIGHTS['topics'] // 2
        findings.append(f'⚠️ Only {len(topics)} topics — add more (+{results["topics"]} pts)')
    else:
        results['topics'] = 0
        findings.append(f'❌ No topics set (+0 pts)')

    # Check license
    lic = repo_data.get('license')
    if lic:
        spdx = lic.get('spdx_id', '')
        results['license'] = WEIGHTS['license']
        findings.append(f'✅ License: {spdx} (+{WEIGHTS["license"]} pts)')
    else:
        results['license'] = 0
        findings.append(f'❌ No license file (+0 pts)')

    # 2. Check AGENTS.md
    contents = api_get(f'https://api.github.com/repos/{owner}/{repo}/contents/AGENTS.md')
    if 'error' not in contents:
        size = contents.get('size', 0)
        if size > 50:
            results['agents_md'] = WEIGHTS['agents_md']
            findings.append(f'✅ AGENTS.md found ({size} bytes) (+{WEIGHTS["agents_md"]} pts)')
        else:
            results['agents_md'] = WEIGHTS['agents_md'] // 2
            findings.append(f'⚠️ AGENTS.md exists but is only {size} bytes (+{results["agents_md"]} pts)')
    else:
        results['agents_md'] = 0
        findings.append(f'❌ No AGENTS.md (+0 pts)')

    # 3. Check README
    readme_data = api_get(f'https://api.github.com/repos/{owner}/{repo}/readme')
    if 'error' not in readme_data:
        size = readme_data.get('size', 0)
        if size > 1000:
            results['readme'] = WEIGHTS['readme']
            findings.append(f'✅ README found ({size} bytes) (+{WEIGHTS["readme"]} pts)')
        elif size > 200:
            results['readme'] = WEIGHTS['readme'] // 2
            findings.append(f'⚠️ README is only {size} bytes — could be more detailed (+{results["readme"]} pts)')
        else:
            results['readme'] = WEIGHTS['readme'] // 4
            findings.append(f'⚠️ README is minimal ({size} bytes) (+{results["readme"]} pts)')
    else:
        results['readme'] = 0
        findings.append(f'❌ No README found (+0 pts)')

    # 4. Check llms.txt (try common locations)
    llms_txt = api_get(f'https://api.github.com/repos/{owner}/{repo}/contents/llms.txt')
    if 'error' not in llms_txt:
        results['llms_txt'] = WEIGHTS['llms_txt']
        findings.append(f'✅ llms.txt found (+{WEIGHTS["llms_txt"]} pts)')
    else:
        results['llms_txt'] = 0
        findings.append(f'❌ No llms.txt (+0 pts)')

    total = sum(results.values())

    return {
        'repo': repo_full,
        'score': total,
        'max_score': SCORE_TOTAL,
        'checks': results,
        'findings': findings,
        'rating': 'Excellent' if total >= 90 else 'Good' if total >= 70 else 'Needs work' if total >= 50 else 'Poor',
    }


def main():
    if len(sys.argv) < 2:
        print('Usage: python audit_repo.py owner/repo [owner/repo ...]')
        sys.exit(1)

    repos = sys.argv[1:]
    all_results = []

    for repo_full in repos:
        print(f'\n📦 Auditing: {repo_full}')
        print('=' * 60)

        result = audit(repo_full)
        if 'error' in result:
            print(f'❌ {result["error"]}')
            continue

        all_results.append(result)

        for finding in result['findings']:
            print(f'  {finding}')

        print(f'\n  📊 Score: {result["score"]}/{result["max_score"]} — {result["rating"]}')
        print()

    # Save all results
    with open('audit_results.json', 'w') as f:
        json.dump(all_results, f, indent=2)
    print(f'Reports saved to audit_results.json')


if __name__ == '__main__':
    main()
