# Contributing to Security Policy Templates

Thank you for helping make these templates more valuable for the community! This guide explains how to contribute new policies, improve existing ones, or add supporting materials.

## Table of Contents

- [Who Should Contribute](#who-should-contribute)
- [Types of Contributions](#types-of-contributions)
- [Policy Template Structure](#policy-template-structure)
- [Placeholder Conventions](#placeholder-conventions)
- [NIST CSF Mapping Requirements](#nist-csf-mapping-requirements)
- [Version History Requirements](#version-history-requirements)
- [Submitting a Pull Request](#submitting-a-pull-request)
- [Style Guide](#style-guide)
- [Reviewing Contributions](#reviewing-contributions)

---

## Who Should Contribute

We welcome contributions from:
- Security practitioners and consultants
- IT managers and system administrators
- Compliance professionals
- Lawyers with information security experience
- Academics and researchers

> **Note:** All contributions are reviewed for accuracy and SMB-appropriateness before merging. Legal review of policy content is the responsibility of the implementing organization.

---

## Types of Contributions

| Type | Examples |
|------|---------|
| New policy templates | Cloud Security Policy, BYOD Policy, Data Classification |
| Industry-specific overlays | HIPAA additions, PCI DSS overlays |
| Supporting templates | Checklists, forms, training materials |
| Documentation improvements | Clearer guidance, better examples |
| Framework mappings | CIS Controls, ISO 27001, SOC 2 cross-references |
| Bug fixes | Correcting NIST CSF references, fixing placeholder names |
| Translations | Policies in languages other than English |

---

## Policy Template Structure

Every policy template **must** follow this structure. Copy the block below as your starting point:

```markdown
# [Policy Name]

**NIST CSF Functions: [List applicable functions: Identify / Protect / Detect / Respond / Recover]**

## Purpose
[One to two sentences describing why this policy exists.]

## Scope
[Who and what this policy applies to.]

## [Section Title]

### [Section Number].[Subsection Number] [Subsection Title] *(NIST CSF: [Category].[Subcategory])*
- Requirement one
- Requirement two
- Requirement three

## Compliance and Monitoring *(NIST CSF: DE.CM-1, DE.CM-7)*
- How compliance is measured and enforced.

## Enforcement
[Consequences for policy violations.]

## References
- NIST CSF v1.1: [Relevant categories]

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [YYYY-MM-DD] | [Name/Role] | Initial release |
```

### Required Sections

| Section | Required | Notes |
|---------|----------|-------|
| Title | Yes | Use Title Case |
| NIST CSF Functions | Yes | List all applicable functions |
| Purpose | Yes | 1–2 sentences |
| Scope | Yes | Be specific about who/what is covered |
| Policy body | Yes | At least 3 subsections with NIST citations |
| Compliance and Monitoring | Yes | |
| Enforcement | Yes | |
| References | Yes | Always include NIST CSF v1.1 |
| Version History | Yes | Start at 1.0 |

---

## Placeholder Conventions

Use these **exact** placeholder strings so the automation script (`scripts/customize.sh`) can replace them:

| Placeholder | Replaced With |
|-------------|--------------|
| `[Company Name]` | Organization's legal name |
| `[Date]` | Policy effective date (YYYY-MM-DD) |
| `[IT Contact]` | IT department contact name or email |
| `[Security Officer]` | CISO or security lead name/title |
| `[Review Date]` | Next scheduled review date |
| `[Department]` | Owning department |
| `[Industry]` | Organization's industry sector |

**Rules:**
- Always use square brackets: `[Placeholder Name]`
- Use Title Case inside brackets
- Never invent new placeholders — use existing ones where possible
- If a new placeholder is truly needed, document it in your PR description

---

## NIST CSF Mapping Requirements

Every policy section **must** cite at least one NIST CSF subcategory in the format:

```
*(NIST CSF: XX.XX-X)*
```

**Common mappings by policy area:**

| Policy Area | Key NIST CSF References |
|-------------|------------------------|
| Access Control | PR.AC-1, PR.AC-3, PR.AC-4, PR.AC-5, PR.AC-6, PR.AC-7 |
| Asset Management | ID.AM-1, ID.AM-2, ID.AM-3, ID.AM-4, ID.AM-5 |
| Awareness & Training | PR.AT-1, PR.AT-2, PR.AT-3, PR.AT-4, PR.AT-5 |
| Data Security | PR.DS-1, PR.DS-2, PR.DS-3, PR.DS-4, PR.DS-5 |
| Incident Response | RS.RP-1, RS.CO-1, RS.AN-1, RS.MI-1, RS.IM-1 |
| Risk Assessment | ID.RA-1, ID.RA-2, ID.RA-3, ID.RA-4, ID.RA-5, ID.RA-6 |
| Supply Chain | ID.SC-1, ID.SC-2, ID.SC-3, ID.SC-4, ID.SC-5 |
| Detection | DE.CM-1, DE.CM-3, DE.CM-7, DE.AE-1, DE.AE-2 |
| Recovery | RC.RP-1, RC.IM-1, RC.IM-2, RC.CO-1, RC.CO-3 |

Full NIST CSF reference: https://www.nist.gov/cyberframework

---

## Version History Requirements

All templates must include a version history table at the bottom:

```markdown
## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [YYYY-MM-DD] | [Name/Role] | Initial release |
```

- Start all new templates at version `1.0`
- When updating an existing template, increment the version (1.0 → 1.1 for minor, 1.x → 2.0 for major rewrites)
- Add a new row for each change — do not overwrite previous entries

---

## Submitting a Pull Request

1. **Fork** the repository and create a branch from `main`:
   ```bash
   git checkout -b add-cloud-security-policy
   ```

2. **Add or edit** your template following the structure above.

3. **Test the automation script** to confirm your placeholders work:
   ```bash
   ./scripts/customize.sh --company "Acme Corp" --date "2025-01-01" --dry-run
   ```

4. **Update `README.md`** if you added a new policy — add it to the template list table.

5. **Open a pull request** with:
   - A clear title: `Add [Policy Name]` or `Update [Policy Name]: [what changed]`
   - A brief description of what the policy covers and why it's valuable
   - Confirmation that NIST CSF mappings are accurate
   - Note any sections that should be reviewed by a lawyer before use

### PR Checklist

- [ ] Template follows the required structure
- [ ] All sections include NIST CSF citations
- [ ] All placeholders use the standard format `[Placeholder Name]`
- [ ] Version history table is present and starts at 1.0
- [ ] README.md updated if a new policy was added
- [ ] Automation script tested with `--dry-run`
- [ ] No personally identifiable information or real company data included

---

## Style Guide

- **Tone:** Professional, direct, imperative. ("Employees must..." not "Employees should consider...")
- **Length:** Aim for 300–800 lines for a full policy; 100–300 for checklists/forms
- **Lists:** Use bullet lists for requirements; numbered lists for sequential steps
- **Headings:** Use `##` for major sections, `###` for subsections
- **Specificity:** Include concrete values where possible (e.g., "15-minute timeout" not "reasonable timeout")
- **Avoid jargon** that SMB staff without security backgrounds won't understand — or define terms when first used

---

## Reviewing Contributions

Maintainers review PRs for:

1. **Accuracy** — Is the security guidance sound and current?
2. **Structure** — Does it follow the required template format?
3. **NIST alignment** — Are CSF citations correct?
4. **SMB appropriateness** — Is this achievable for a 10–500 person organization?
5. **Clarity** — Would a non-security IT manager understand and implement this?

Reviews typically happen within 2 weeks. We may request changes before merging.

---

## Questions?

Open a GitHub Issue with the label `question` and we'll get back to you.
