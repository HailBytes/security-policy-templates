# Security Policy

## Scope

This repository distributes documentation: security policy templates, compliance
framework mappings, and a Bash customization script (`scripts/customize.sh`). It
has no runtime application and no software dependencies, so most traditional
vulnerability classes (e.g. dependency CVEs) don't apply. The relevant attack
surface is:

- `scripts/customize.sh` — a shell script users run locally, and the
  `.github/workflows/ci.yml` GitHub Actions workflows that run it in CI
- Any injected or malicious content in a pull request (e.g. a template edit
  that introduces a shell-injection vector into `customize.sh`, or a
  supply-chain issue in a GitHub Actions workflow change)

Incorrect or outdated compliance/framework citations (e.g. a wrong NIST CSF or
ISO 27001 control reference) are **content accuracy issues**, not security
vulnerabilities — please report those as a regular
[GitHub issue](https://github.com/HailBytes/security-policy-templates/issues) rather than through this policy.

## Reporting a Vulnerability

If you find a security issue in `scripts/customize.sh`, a GitHub Actions
workflow, or anything else in this repository that could lead to code
execution, secret exposure, or a supply-chain compromise, please report it
privately rather than opening a public issue:

1. Use GitHub's [private vulnerability reporting](https://github.com/HailBytes/security-policy-templates/security/advisories/new)
   for this repository ("Security" tab → "Report a vulnerability"), or
2. If that's unavailable, open a regular issue asking a maintainer to enable
   private reporting or provide an alternate contact, without including
   exploit details in the public issue body.

Please include:

- A description of the issue and its potential impact
- Steps to reproduce (a minimal `customize.sh` invocation or workflow diff is
  ideal)
- Any suggested remediation, if you have one

## Response

This is a community-maintained repository. There is no guaranteed SLA, but
reports are reviewed as they arrive and valid fixes are prioritized ahead of
routine content contributions. You'll receive an acknowledgement once your
report has been triaged.
