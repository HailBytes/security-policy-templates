## What does this PR do?

<!-- Clear description: new policy, updated policy, mapping fix, documentation change, etc. -->

## Type of change

- [ ] New policy template
- [ ] Industry-specific overlay
- [ ] Supporting template (checklist, form, training material)
- [ ] Documentation improvement
- [ ] Framework mapping (CIS Controls, ISO 27001, SOC 2, etc.)
- [ ] Bug fix (NIST CSF reference, placeholder name, broken link, etc.)
- [ ] Translation

## PR Checklist

See [CONTRIBUTING.md](../CONTRIBUTING.md) for full requirements.

- [ ] Template follows the [required structure](../CONTRIBUTING.md#policy-template-structure)
- [ ] All sections include NIST CSF citations
- [ ] All placeholders use the standard format `[Placeholder Name]` and match the [placeholder conventions table](../CONTRIBUTING.md#placeholder-conventions)
- [ ] Version history table is present and starts at `1.0` (or increments correctly for an existing template)
- [ ] `README.md` updated if a new policy was added
- [ ] Automation script tested with `--dry-run`:
  ```bash
  ./scripts/customize.sh --company "Acme Corp" --date "2025-01-01" --dry-run
  ```
- [ ] No personally identifiable information or real company data included

## Additional notes

<!-- Confirmation that NIST CSF mappings are accurate. Note any sections that should be reviewed by a lawyer before use. -->
