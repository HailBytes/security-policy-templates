# RMM Technician Access Review Checklist

**NIST CSF Functions: Protect (PR)**

## Purpose

Use this checklist to review who can perform privileged work through a remote monitoring and management (RMM) platform. It helps an organization document scope, business need, authentication controls, approvals, exceptions, and remediation without storing passwords, recovery codes, tokens, or other secrets in the review record.

## Scope

This checklist applies to employees, contractors, service-provider personnel, service accounts, API integrations, and roles that can access or administer an RMM platform used by `[Company Name]`. Complete a review before production access is granted, at the scheduled review date, after a role or employment change, and when a customer or system boundary changes.

---

## Review Information

**Organization:** `[Company Name]`<br>
**System or RMM platform:** ___________________________________<br>
**Review owner:** `[Security Officer]`<br>
**Review date:** ___________________________________<br>
**Next review date:** `[Review Date]`<br>
**In-scope customer or business units:** ___________________________________<br>
**Evidence location or ticket:** ___________________________________

---

## 1. Establish the Review Boundary *(NIST CSF: PR.AA-01, PR.AA-05)*

- [ ] List every human identity, service account, API integration, and inherited role with access to the RMM platform.
- [ ] Record employment or contract status and confirm that each identity is still active and authorized.
- [ ] Identify the customer, tenant, business unit, site, and device groups available to each assignment.
- [ ] Distinguish production, pilot, lab, and emergency-access scope.
- [ ] Identify access inherited from groups, parent roles, reseller relationships, or platform-wide defaults.
- [ ] Reconcile the list against the identity provider, RMM console, privileged-access system, and current personnel records.
- [ ] Assign an owner to investigate every identity or entitlement that cannot be reconciled.

**Evidence to retain:** identity export, role export, group membership, integration inventory, personnel-status confirmation, and reconciliation ticket.

---

## 2. Verify Identity and Authentication *(NIST CSF: PR.AA-01, PR.AA-03)*

- [ ] Every person uses an individual, attributable identity; shared technician accounts are prohibited or have a documented, time-bounded exception.
- [ ] Multifactor authentication is enforced for interactive access.
- [ ] Recovery methods and break-glass credentials are restricted, monitored, and periodically tested.
- [ ] Privileged access is limited to managed administrative devices where the organization can enforce security controls.
- [ ] Session lifetime, reauthentication, invitation expiry, and revocation behavior are documented and tested.
- [ ] Service accounts and API integrations use non-human identities with a named owner and rotation or revocation procedure.
- [ ] Disabled or terminated identities cannot retain active sessions, API tokens, or unattended remote-access paths.

**Evidence to retain:** MFA status, session-policy configuration, managed-device requirement, service-account owner, and revocation test result. Do not copy secrets into the evidence record.

---

## 3. Review Privileged Capabilities *(NIST CSF: PR.AA-05)*

Review each capability separately. A narrow permission applied to every customer can still be excessive privilege.

| Capability | None | Read | Limited / Attended | Full / Administrative | Business Need Verified | Evidence |
|---|---|---|---|---|---|---|
| RMM console access | ☐ | ☐ | ☐ | ☐ | ☐ | ___________ |
| Customer or tenant visibility | ☐ | ☐ | ☐ | ☐ | ☐ | ___________ |
| Remote control | ☐ | ☐ | ☐ | ☐ | ☐ | ___________ |
| Background tools or shell | ☐ | ☐ | ☐ | ☐ | ☐ | ___________ |
| File transfer | ☐ | ☐ | ☐ | ☐ | ☐ | ___________ |
| Script execution | ☐ | ☐ | ☐ | ☐ | ☐ | ___________ |
| Automation creation or editing | ☐ | ☐ | ☐ | ☐ | ☐ | ___________ |
| Patch approval or policy changes | ☐ | ☐ | ☐ | ☐ | ☐ | ___________ |
| Alert and monitoring configuration | ☐ | ☐ | ☐ | ☐ | ☐ | ___________ |
| Credential or vault access | ☐ | ☐ | ☐ | ☐ | ☐ | ___________ |
| User and role administration | ☐ | ☐ | ☐ | ☐ | ☐ | ___________ |
| API and integration administration | ☐ | ☐ | ☐ | ☐ | ☐ | ___________ |
| Billing or commercial data | ☐ | ☐ | ☐ | ☐ | ☐ | ___________ |
| Audit-log deletion or retention changes | ☐ | ☐ | ☐ | ☐ | ☐ | ___________ |

For every granted capability:

- [ ] Record the task or responsibility that requires the access.
- [ ] Limit scope to the minimum customers, sites, devices, and time period needed.
- [ ] Verify that read-only, attended, approval-gated, or temporary access cannot meet the same need.
- [ ] Check for toxic combinations that defeat separation of duties, such as requesting and approving the same privileged change.
- [ ] Test at least one denied action for limited roles rather than relying only on the role name.

---

## 4. Confirm Approval and Evidence *(NIST CSF: PR.AA-05)*

- [ ] The system, customer, or data owner approved the assignment.
- [ ] Approval identifies the exact role, scope, capabilities, and business justification.
- [ ] Approval time and approving person are recorded in an auditable system.
- [ ] Temporary or elevated access has an explicit expiration time.
- [ ] Emergency access has after-the-fact review requirements and an assigned reviewer.
- [ ] The review record links to evidence without embedding passwords, private keys, recovery codes, session cookies, or API tokens.
- [ ] Audit logs can reconstruct privileged actions by actor, target, time, source, action, and result.

---

## 5. Review Joiner, Mover, and Leaver Events *(NIST CSF: PR.AA-01, PR.AA-05)*

- [ ] New access is provisioned only from an approved request.
- [ ] Role or customer-scope changes trigger a new access decision rather than copying the previous role.
- [ ] Access is removed promptly when employment, contract status, customer assignment, or job duties change.
- [ ] Active sessions, API tokens, remote-access components, delegated credentials, and group memberships are included in revocation.
- [ ] Customer offboarding removes access from both the primary RMM and connected tools.
- [ ] Termination and transfer tests confirm that removed access no longer works.
- [ ] Orphaned roles, integrations, service accounts, and invitations are disabled or assigned a current owner.

---

## 6. Record the Decision and Remediation *(NIST CSF: PR.AA-05)*

Select one decision for every assignment:

- [ ] **Retain** — access is necessary, approved, and appropriately scoped.
- [ ] **Reduce** — remove capabilities or narrow customer, site, device, or time scope.
- [ ] **Revoke** — access is no longer authorized or required.
- [ ] **Investigate** — evidence is incomplete; assign an owner and due date while applying a risk-appropriate restriction.

| Assignment or Role | Decision | Exception or Ticket | Remediation Owner | Due Date | Verified By | Closed Date |
|---|---|---|---|---|---|---|
| __________________ | ________ | ___________________ | _________________ | ________ | ___________ | ___________ |
| __________________ | ________ | ___________________ | _________________ | ________ | ___________ | ___________ |
| __________________ | ________ | ___________________ | _________________ | ________ | ___________ | ___________ |

- [ ] Every reduction or revocation has an owner and due date.
- [ ] Every accepted exception identifies the risk owner, compensating controls, expiration, and review date.
- [ ] A second person verifies completed remediation for high-impact capabilities.
- [ ] The final reviewer confirms that all assignments have a decision and no unresolved row is silently treated as approved.

---

## Compliance and Monitoring *(NIST CSF: PR.AA-05)*

- Conduct reviews at least quarterly for privileged and cross-customer roles, and at least annually for all other RMM access unless risk requires a shorter interval.
- Trigger an out-of-cycle review after employment or contract changes, customer onboarding or offboarding, security incidents, material role changes, platform migrations, and newly enabled integrations.
- Track completion rate, overdue reviews, excessive-access findings, time to revoke access, expired exceptions, and failed revocation tests.
- Preserve review records according to `[Company Name]`'s retention requirements and applicable customer or regulatory obligations.
- Sample denied actions and completed remediation to verify that console configuration matches the approved record.

## Enforcement

Access that lacks an owner, business justification, required authentication control, or current approval must be restricted or removed according to `[Company Name]`'s access-control and exception-management procedures. Suspected unauthorized access must be escalated through the organization's incident-response process.

## References

- [NIST Cybersecurity Framework 2.0](https://doi.org/10.6028/NIST.CSWP.29), especially PR.AA-01, PR.AA-03, and PR.AA-05.
- [NIST CSF 2.0 Implementation Examples](https://www.nist.gov/document/csf-20-implementations-pdf), including periodic privilege review, prompt revocation, least privilege, and separation of duties.
- [CISA: Protecting Against Cyber Threats to Managed Service Providers and their Customers](https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-131a).

## Version History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-11-01 | Kip Ecklund / Nizlo | Initial RMM technician access review checklist |

---

This checklist is an operational starting point, not legal advice, an audit opinion, or a product certification. Adapt its scope and review frequency to the organization's risks, contracts, technology, and applicable requirements.
