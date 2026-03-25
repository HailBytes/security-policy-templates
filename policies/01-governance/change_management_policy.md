# Change Management Policy

**NIST CSF Functions: Protect (PR), Identify (ID)**

## Purpose
To ensure that changes to [Company Name] IT systems, infrastructure, applications, and security controls are assessed, authorized, documented, and reviewed to minimize security risk and operational disruption.

## Scope
Applies to all changes to IT infrastructure, systems, applications, network configurations, cloud environments, security controls, and third-party integrations managed by [Company Name] or on its behalf.

## Change Types

### 1.1 Change Classification *(NIST CSF: PR.IP-1, PR.IP-3)*

| Type | Definition | Approval Required | Lead Time |
|------|-----------|-------------------|-----------|
| **Standard** | Pre-approved, low-risk, routine change with established procedure | Pre-approved; log only | Per procedure |
| **Normal** | Planned change requiring review and approval | Change Approver | Minimum 5 business days |
| **Emergency** | Unplanned change needed to restore service or address critical security issue | [IT Contact] + [Security Officer] | 2 hours minimum |
| **Major** | Significant change affecting multiple systems, architecture, or business processes | Executive + [Security Officer] | Minimum 10 business days |

All changes not fitting Standard or Emergency categories default to Normal.

## Change Request Process

### 1.2 Submitting a Change Request *(NIST CSF: PR.IP-3)*
All Normal and Major changes require a Change Request (CR) containing:
- Description of the change and business justification
- Systems and services affected
- Security impact assessment
- Risk rating (Low / Medium / High)
- Rollback plan
- Test plan and success criteria
- Proposed implementation date and maintenance window
- Name of the implementer and approver

Change Requests must be submitted via [approved change management tool or ticketing system].

### 1.3 Security Impact Assessment *(NIST CSF: PR.IP-3, ID.RA-1)*
Every Change Request must include a security impact assessment covering:
- Does the change alter authentication or access control settings?
- Does the change affect data encryption at rest or in transit?
- Does the change open new network ports or firewall rules?
- Does the change involve third-party software or services?
- Does the change affect logging, monitoring, or alerting capability?
- Does the change touch systems hosting Confidential or Restricted data?

Changes answering "Yes" to any question above require review by [IT Contact] or [Security Officer] before approval.

### 1.4 Change Approval *(NIST CSF: PR.IP-3, ID.GV-1)*
- **Low-risk Normal changes:** [IT Contact] approval sufficient
- **Medium-risk Normal changes:** [IT Contact] + system owner approval
- **High-risk Normal or Major changes:** [Security Officer] + executive approval
- **Emergency changes:** [IT Contact] approval required; [Security Officer] notification within 1 hour; formal post-change review within 3 business days

Approval must be recorded in the change management system before implementation begins.

## Implementation Controls

### 1.5 Testing Requirements *(NIST CSF: PR.IP-1, PR.IP-3)*
- All Normal and Major changes must be tested in a non-production environment before production deployment
- Test results must be documented and attached to the Change Request
- Security-relevant changes (firewall rules, access controls, authentication) must include a security validation test
- Changes affecting disaster recovery or business continuity capabilities must include a recovery test

### 1.6 Maintenance Windows *(NIST CSF: PR.IP-1)*
- Standard maintenance window: [Day of week], [Time range]
- Changes outside maintenance windows require explicit approval from [IT Contact]
- Maintenance windows must be communicated to affected stakeholders at least 48 hours in advance
- Emergency changes may occur outside maintenance windows; stakeholder notification within 2 hours

### 1.7 Rollback Procedures *(NIST CSF: PR.IP-1, RC.RP-1)*
- Every change must have a documented rollback plan before implementation begins
- Rollback must be triggered if success criteria are not met within the defined implementation window
- Rollback authority rests with the implementer unless otherwise specified in the CR
- Post-rollback, a new CR must be submitted before re-attempting the change

### 1.8 Change Documentation *(NIST CSF: PR.IP-1, ID.GV-1)*
After every change is completed:
- Document actual implementation steps taken
- Record any deviations from the approved plan
- Document test results and validation outcomes
- Note any unexpected impacts or side effects
- Update asset inventory, network diagrams, or system documentation as needed
- Close the Change Request with completion status

## Emergency Change Process

### 1.9 Emergency Change Procedure *(NIST CSF: RS.MI-1, PR.IP-3)*
When an emergency change is needed (e.g., active security incident, critical system failure):
1. [IT Contact] verbally authorizes the change
2. Implementer documents the change action with timestamp as it occurs
3. [Security Officer] is notified within 1 hour
4. Emergency CR is filed within 4 hours of change completion
5. Post-change security review completed within 3 business days
6. Emergency changes are reviewed in the next scheduled change review meeting

Emergency changes that alter security controls (firewall rules, access permissions, encryption) must be reviewed for rollback within 30 days if the underlying issue has been resolved.

## Configuration and Baseline Management

### 1.10 Configuration Baselines *(NIST CSF: PR.IP-1, PR.DS-7)*
- Approved configuration baselines must be maintained for all critical system types
- Changes from baseline must be documented via the change management process
- Unauthorized configuration drift must be detected and remediated within 14 days
- Configuration baselines must be reviewed and updated annually or after Major changes
- Infrastructure as Code (IaC) templates represent the baseline for cloud infrastructure

### 1.11 Change Calendar *(NIST CSF: PR.IP-3)*
- [IT Contact] maintains a forward schedule of all approved changes
- Change calendar must be reviewed weekly by [IT Contact]
- Conflicting changes must be identified and resolved before approval
- Change freeze periods (e.g., end-of-quarter, peak business periods) must be communicated and enforced

## Review and Audit

### 1.12 Post-Implementation Review *(NIST CSF: PR.IP-3, DE.AE-3)*
For Normal and Major changes:
- Post-implementation review must occur within 5 business days
- Review assesses: did the change achieve its objective, were there unintended impacts, were security controls maintained
- Lessons learned must be documented for Major and Emergency changes
- Recurring issues identified through change review must be escalated to [Security Officer]

## Compliance and Monitoring *(NIST CSF: DE.CM-1, ID.GV-3)*
- Monthly change log review by [IT Contact] to identify unauthorized changes
- Quarterly change process audit by [Security Officer]
- All changes to security controls are logged and retained for 1 year
- Unauthorized changes (changes implemented without a CR) are treated as security incidents

## Enforcement
Implementing changes without following this policy, bypassing required approvals, or failing to document changes constitutes a policy violation. All unauthorized changes must be reported to [Security Officer] and may be rolled back pending investigation. Repeated violations may result in loss of system access and disciplinary action.

## References
- NIST CSF v1.1: PR.IP (Information Protection Processes), ID.GV (Governance), RC.RP (Recovery Planning)
- NIST SP 800-128: Guide for Security-Focused Configuration Management
- ITIL Change Management best practices

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Security Officer] | Initial release |
