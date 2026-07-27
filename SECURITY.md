# Security Policy

This repository publishes security policy *templates* — Markdown documents, plus a
Bash customization script and CI workflow used to generate them. This document
covers vulnerabilities in that tooling, not disagreements with policy content.

## Reporting a Vulnerability

If you believe you've found a security vulnerability in this repository — for
example, a shell injection or path-traversal issue in `scripts/customize.sh`, or
an unsafe pattern in the GitHub Actions workflow (`.github/workflows/ci.yml`) —
please report it privately using GitHub's built-in reporting tool rather than
opening a public issue:

1. Go to the [Security tab](../../security/advisories/new) of this repository.
2. Click **Report a vulnerability** to open a draft security advisory.
3. Include a description of the issue, steps to reproduce, and the potential
   impact.

We'll acknowledge reports as soon as possible and work with you on a fix and
coordinated disclosure timeline before any public advisory is published.

## Scope

In scope:
- `scripts/customize.sh` and any other executable code added to this repo
- `.github/workflows/*.yml` CI/CD configuration

Out of scope (use a regular [issue](../../issues) instead):
- Factual, legal, or compliance-mapping corrections to policy text under
  `policies/`, `templates/`, `industry-variants/`, `mappings/`, or `docs/`
- Suggestions to strengthen a *recommended* control described in a template

## Supported Versions

This project does not maintain release branches; only the latest commit on
`main` is supported. Please base reports on the current `main` branch.
