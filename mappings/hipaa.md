# HIPAA Security Rule Mappings

This file maps each policy template to specific requirements under the HIPAA Security Rule (45 CFR Part 164, Subparts A and C). Use this during internal audits, risk assessments, or when preparing evidence packages for HHS reviews, OCR investigations, or pre-audit gap analyses.

> **Scope note:** The HIPAA Security Rule applies to **electronic Protected Health Information (ePHI)** only. Covered Entities (CEs) and Business Associates (BAs) must comply with all Required specifications; Addressable specifications must either be implemented or documented with a compliant alternative. Policy documents establish administrative controls — you also need operational evidence (training records, access logs, risk analysis documentation, BAA registers). See the [Healthcare/HIPAA Industry Overlay](../industry-variants/healthcare-hipaa-overlay.md) for implementation guidance.

> **Penalty reminder:** Violations range from $137 to $68,928 per violation (as of 2024 inflation adjustments), up to $2.07M per violation category per year. Willful neglect with no correction starts at $68,928 per violation.

---

## §164.308 — Administrative Safeguards

### §164.308(a)(1) — Security Management Process

| Requirement | Specification | Policy File | Evidence Provided |
|-------------|--------------|-------------|-------------------|
| §164.308(a)(1)(ii)(A) | Risk Analysis *(Required)* | `policies/05-infrastructure/vulnerability_patch_management_policy.md` | CVSS-based vulnerability scoring and risk prioritization process |
| §164.308(a)(1)(ii)(A) | Risk Analysis *(Required)* | `policies/01-governance/data_classification_policy.md` | Data classification tiers drive scope of risk analysis for ePHI assets |
| §164.308(a)(1)(ii)(B) | Risk Management *(Required)* | `policies/05-infrastructure/vulnerability_patch_management_policy.md` | Risk-tiered remediation SLAs (Critical 24h / High 7d / Medium 30d) |
| §164.308(a)(1)(ii)(C) | Sanction Policy *(Required)* | `policies/01-governance/acceptable_use_policy.md` | Policy enforcement and sanction framework for workforce violations |
| §164.308(a)(1)(ii)(C) | Sanction Policy *(Required)* | `policies/01-governance/ethics_policy.md` | Disciplinary procedures for ethics and policy violations |
| §164.308(a)(1)(ii)(D) | Information System Activity Review *(Required)* | `policies/05-infrastructure/server_security_policy.md` | Centralized logging, SIEM integration, and audit log review requirements |

---

### §164.308(a)(2) — Assigned Security Responsibility

| Requirement | Specification | Policy File | Evidence Provided |
|-------------|--------------|-------------|-------------------|
| §164.308(a)(2) | Security Officer designation *(Required)* | `policies/01-governance/acceptable_use_policy.md` | Documents IT/Security Officer responsibility for policy oversight |
| §164.308(a)(2) | Security Officer designation *(Required)* | `policies/04-incident-response/security_response_plan_policy.md` | Security Officer role in incident escalation and response authority |

---

### §164.308(a)(3) — Workforce Security

| Requirement | Specification | Policy File | Evidence Provided |
|-------------|--------------|-------------|-------------------|
| §164.308(a)(3)(ii)(A) | Authorization and Supervision *(Addressable)* | `policies/02-access-control/password_protection_policy.md` | Role-based access provisioning and authorization workflows |
| §164.308(a)(3)(ii)(B) | Workforce Clearance Procedure *(Addressable)* | `policies/01-governance/vendor_third_party_risk_policy.md` | Background check and onboarding security requirements |
| §164.308(a)(3)(ii)(C) | Termination Procedures *(Addressable)* | `policies/02-access-control/password_protection_policy.md` | Account deprovisioning requirements upon termination |
| §164.308(a)(3)(ii)(C) | Termination Procedures *(Addressable)* | `policies/01-governance/vendor_third_party_risk_policy.md` | Vendor offboarding and access revocation procedures |

---

### §164.308(a)(4) — Information Access Management

| Requirement | Specification | Policy File | Evidence Provided |
|-------------|--------------|-------------|-------------------|
| §164.308(a)(4)(ii)(A) | Isolating Healthcare Clearinghouse Functions *(Required, if applicable)* | `policies/05-infrastructure/cloud_security_policy.md` | Network segmentation and environment isolation controls |
| §164.308(a)(4)(ii)(B) | Access Authorization *(Addressable)* | `policies/02-access-control/password_protection_policy.md` | Least privilege access provisioning and approval process |
| §164.308(a)(4)(ii)(B) | Access Authorization *(Addressable)* | `policies/01-governance/data_classification_policy.md` | Access authorization requirements by data classification tier |
| §164.308(a)(4)(ii)(C) | Access Establishment and Modification *(Addressable)* | `policies/02-access-control/password_protection_policy.md` | Access review cadence and modification approval requirements |

---

### §164.308(a)(5) — Security Awareness and Training

| Requirement | Specification | Policy File | Evidence Provided |
|-------------|--------------|-------------|-------------------|
| §164.308(a)(5)(ii)(A) | Security Reminders *(Addressable)* | `policies/01-governance/acceptable_use_policy.md` | Annual policy acknowledgment and awareness communication requirements |
| §164.308(a)(5)(ii)(B) | Protection from Malicious Software *(Addressable)* | `policies/05-infrastructure/server_security_policy.md` | Anti-malware deployment, update, and monitoring requirements |
| §164.308(a)(5)(ii)(B) | Protection from Malicious Software *(Addressable)* | `policies/03-communications/email_policy.md` | Email-borne threat controls and attachment filtering requirements |
| §164.308(a)(5)(ii)(C) | Log-in Monitoring *(Addressable)* | `policies/05-infrastructure/server_security_policy.md` | Failed login alerting and account lockout policy requirements |
| §164.308(a)(5)(ii)(D) | Password Management *(Addressable)* | `policies/02-access-control/password_protection_policy.md` | Password complexity, rotation, and MFA requirements |

---

### §164.308(a)(6) — Security Incident Procedures

| Requirement | Specification | Policy File | Evidence Provided |
|-------------|--------------|-------------|-------------------|
| §164.308(a)(6)(ii) | Response and Reporting *(Required)* | `policies/04-incident-response/security_response_plan_policy.md` | Full incident response lifecycle: detection, triage, containment, eradication, recovery, closure |
| §164.308(a)(6)(ii) | Response and Reporting *(Required)* | `policies/04-incident-response/data_breach_response_policy.md` | PHI breach assessment (4-factor test), notification timelines, and HHS reporting obligations |

---

### §164.308(a)(7) — Contingency Plan

| Requirement | Specification | Policy File | Evidence Provided |
|-------------|--------------|-------------|-------------------|
| §164.308(a)(7)(ii)(A) | Data Backup Plan *(Required)* | `policies/06-continuity/disaster_recovery_plan_policy.md` | 3-2-1 backup strategy with ePHI backup and encryption requirements |
| §164.308(a)(7)(ii)(B) | Disaster Recovery Plan *(Required)* | `policies/06-continuity/disaster_recovery_plan_policy.md` | Full DR execution plan with RTO/RPO objectives and recovery procedures |
| §164.308(a)(7)(ii)(C) | Emergency Mode Operation Plan *(Required)* | `policies/06-continuity/disaster_recovery_plan_policy.md` | Emergency operations procedures maintaining minimum ePHI access during failures |
| §164.308(a)(7)(ii)(D) | Testing and Revision *(Addressable)* | `policies/06-continuity/disaster_recovery_plan_policy.md` | Annual DR test schedule, tabletop exercise requirements, and revision triggers |
| §164.308(a)(7)(ii)(E) | Applications and Data Criticality Analysis *(Addressable)* | `policies/01-governance/data_classification_policy.md` | Asset criticality rankings driving recovery prioritization |

---

### §164.308(a)(8) — Evaluation

| Requirement | Specification | Policy File | Evidence Provided |
|-------------|--------------|-------------|-------------------|
| §164.308(a)(8) | Periodic Technical and Non-Technical Evaluation *(Required)* | `policies/05-infrastructure/vulnerability_patch_management_policy.md` | Scheduled vulnerability assessments and penetration testing cadence |
| §164.308(a)(8) | Periodic Technical and Non-Technical Evaluation *(Required)* | `policies/01-governance/change_management_policy.md` | Security impact review as part of change management approval workflow |

---

### §164.308(b) — Business Associate Contracts

| Requirement | Specification | Policy File | Evidence Provided |
|-------------|--------------|-------------|-------------------|
| §164.308(b)(1) | Business Associate Contracts *(Required)* | `policies/01-governance/vendor_third_party_risk_policy.md` | BA contract requirements, BAA register, and vendor security assessment lifecycle |

---

## §164.310 — Physical Safeguards

### §164.310(a) — Facility Access Controls

| Requirement | Specification | Policy File | Evidence Provided |
|-------------|--------------|-------------|-------------------|
| §164.310(a)(2)(i) | Contingency Operations *(Addressable)* | `policies/06-continuity/disaster_recovery_plan_policy.md` | Physical access procedures during emergency and recovery operations |
| §164.310(a)(2)(ii) | Facility Security Plan *(Addressable)* | `policies/02-access-control/clean_desk_policy.md` | Physical security controls for workspaces, equipment, and sensitive media |
| §164.310(a)(2)(iii) | Access Control and Validation Procedures *(Addressable)* | `policies/02-access-control/clean_desk_policy.md` | Visitor access controls and physical access validation requirements |
| §164.310(a)(2)(iv) | Maintenance Records *(Addressable)* | `policies/01-governance/change_management_policy.md` | Physical infrastructure change tracking and maintenance documentation |

---

### §164.310(b) — Workstation Use

| Requirement | Specification | Policy File | Evidence Provided |
|-------------|--------------|-------------|-------------------|
| §164.310(b) | Workstation Use *(Required)* | `policies/01-governance/acceptable_use_policy.md` | Authorized use requirements for workstations accessing organizational systems |
| §164.310(b) | Workstation Use *(Required)* | `policies/02-access-control/remote_work_byod_policy.md` | Remote workstation usage requirements and ePHI handling restrictions |

---

### §164.310(c) — Workstation Security

| Requirement | Specification | Policy File | Evidence Provided |
|-------------|--------------|-------------|-------------------|
| §164.310(c) | Workstation Security *(Required)* | `policies/02-access-control/clean_desk_policy.md` | Physical safeguards for workstations: screen locks, unattended workstation controls |
| §164.310(c) | Workstation Security *(Required)* | `policies/05-infrastructure/server_security_policy.md` | Endpoint hardening baselines and workstation security configuration requirements |

---

### §164.310(d) — Device and Media Controls

| Requirement | Specification | Policy File | Evidence Provided |
|-------------|--------------|-------------|-------------------|
| §164.310(d)(2)(i) | Disposal *(Required)* | `policies/01-governance/data_classification_policy.md` | Certified destruction requirements for media containing Restricted/ePHI data |
| §164.310(d)(2)(ii) | Media Re-Use *(Required)* | `policies/01-governance/data_classification_policy.md` | Secure sanitization requirements before media re-use |
| §164.310(d)(2)(iii) | Accountability *(Addressable)* | `policies/02-access-control/remote_work_byod_policy.md` | Device inventory, MDM enrollment, and remote wipe capability for mobile ePHI access |
| §164.310(d)(2)(iv) | Data Backup and Storage *(Addressable)* | `policies/06-continuity/disaster_recovery_plan_policy.md` | Encrypted backup storage requirements for ePHI |

---

## §164.312 — Technical Safeguards

### §164.312(a) — Access Control

| Requirement | Specification | Policy File | Evidence Provided |
|-------------|--------------|-------------|-------------------|
| §164.312(a)(2)(i) | Unique User Identification *(Required)* | `policies/02-access-control/password_protection_policy.md` | Unique user ID requirements; prohibition on shared credentials |
| §164.312(a)(2)(ii) | Emergency Access Procedure *(Required)* | `policies/04-incident-response/security_response_plan_policy.md` | Emergency access procedures for ePHI during system failures |
| §164.312(a)(2)(iii) | Automatic Logoff *(Addressable)* | `policies/02-access-control/password_protection_policy.md` | Session timeout and automatic logoff requirements for inactive sessions |
| §164.312(a)(2)(iii) | Automatic Logoff *(Addressable)* | `policies/02-access-control/clean_desk_policy.md` | Screen lock requirements for unattended workstations |
| §164.312(a)(2)(iv) | Encryption and Decryption *(Addressable)* | `policies/01-governance/data_classification_policy.md` | Encryption requirements for Restricted data (maps to ePHI) at rest |
| §164.312(a)(2)(iv) | Encryption and Decryption *(Addressable)* | `policies/05-infrastructure/cloud_security_policy.md` | Cloud storage encryption controls for ePHI |

---

### §164.312(b) — Audit Controls

| Requirement | Specification | Policy File | Evidence Provided |
|-------------|--------------|-------------|-------------------|
| §164.312(b) | Audit Controls *(Required)* | `policies/05-infrastructure/server_security_policy.md` | Audit logging requirements: all access to ePHI systems, 6-year retention, SIEM integration |
| §164.312(b) | Audit Controls *(Required)* | `policies/05-infrastructure/cloud_security_policy.md` | Cloud audit trail requirements: CloudTrail/activity logs for all ePHI access events |

---

### §164.312(c) — Integrity

| Requirement | Specification | Policy File | Evidence Provided |
|-------------|--------------|-------------|-------------------|
| §164.312(c)(2) | Mechanism to Authenticate ePHI *(Addressable)* | `policies/05-infrastructure/server_security_policy.md` | File integrity monitoring and hash verification requirements for ePHI data |
| §164.312(c)(2) | Mechanism to Authenticate ePHI *(Addressable)* | `policies/06-continuity/disaster_recovery_plan_policy.md` | Backup integrity verification requirements (quarterly restoration tests) |

---

### §164.312(d) — Person or Entity Authentication

| Requirement | Specification | Policy File | Evidence Provided |
|-------------|--------------|-------------|-------------------|
| §164.312(d) | Authentication *(Required)* | `policies/02-access-control/password_protection_policy.md` | MFA requirements for all user accounts; authentication standards for system and service accounts |
| §164.312(d) | Authentication *(Required)* | `policies/02-access-control/remote_work_byod_policy.md` | Multi-factor authentication requirements for all remote ePHI access |

---

### §164.312(e) — Transmission Security

| Requirement | Specification | Policy File | Evidence Provided |
|-------------|--------------|-------------|-------------------|
| §164.312(e)(2)(i) | Integrity Controls *(Addressable)* | `policies/03-communications/email_policy.md` | Encrypted email requirements; message integrity controls for ePHI in transit |
| §164.312(e)(2)(ii) | Encryption *(Addressable)* | `policies/03-communications/email_policy.md` | TLS requirements for email transmission; prohibition on unencrypted ePHI via email |
| §164.312(e)(2)(ii) | Encryption *(Addressable)* | `policies/05-infrastructure/wireless_communication_policy.md` | WPA3/WPA2-Enterprise requirements; prohibition on transmitting ePHI over unsecured wireless |
| §164.312(e)(2)(ii) | Encryption *(Addressable)* | `policies/02-access-control/remote_work_byod_policy.md` | Encrypted VPN requirement for all remote access to ePHI systems |
| §164.312(e)(2)(ii) | Encryption *(Addressable)* | `policies/05-infrastructure/cloud_security_policy.md` | TLS 1.2+ requirement for all cloud API and data transfer involving ePHI |

---

## §164.314 — Organizational Requirements

### §164.314(a) — Business Associate Contracts and Other Arrangements

| Requirement | Specification | Policy File | Evidence Provided |
|-------------|--------------|-------------|-------------------|
| §164.314(a)(1) | Business Associate Contracts *(Required)* | `policies/01-governance/vendor_third_party_risk_policy.md` | BAA execution requirements before ePHI sharing; BAA content requirements; BA register maintenance |
| §164.314(a)(2) | Other Arrangements *(Required, if applicable)* | `policies/01-governance/vendor_third_party_risk_policy.md` | Subcontractor chain-of-trust requirements and downstream BA obligations |

---

## §164.316 — Policies and Procedures

| Requirement | Specification | Policy File | Evidence Provided |
|-------------|--------------|-------------|-------------------|
| §164.316(a) | Policies and Procedures *(Required)* | All policies in `policies/` | Written policies implementing Security Rule requirements |
| §164.316(b)(1) | Documentation *(Required)* | All policies in `policies/` | Dated, written policies retained for minimum 6 years from creation or last effective date |
| §164.316(b)(2)(i) | Time Limit *(Required)* | All policies in `policies/` | Version history and effective dates documented in each policy |
| §164.316(b)(2)(ii) | Availability *(Required)* | All policies in `policies/` | Policies available to workforce responsible for implementation |
| §164.316(b)(2)(iii) | Updates *(Required)* | `policies/01-governance/change_management_policy.md` | Policy review cycle and update procedures triggered by environmental or operational changes |

---

## HIPAA Privacy Rule Cross-Reference

The HIPAA Privacy Rule (45 CFR Part 164, Subparts A and E) governs uses and disclosures of PHI in all forms (not just electronic). The policies below support Privacy Rule compliance even though the Security Rule is the primary scope of this mapping.

| Privacy Rule Requirement | Policy File | Support Provided |
|--------------------------|-------------|-----------------|
| Minimum Necessary standard (§164.514(d)) | `policies/02-access-control/password_protection_policy.md` | Least privilege access controls limit ePHI exposure to minimum necessary |
| Accounting of disclosures (§164.528) | `policies/05-infrastructure/server_security_policy.md` | Audit logs provide basis for accounting of disclosures |
| Notice of Privacy Practices | `policies/01-governance/data_classification_policy.md` | Data classification framework governs handling requirements communicated in NPP |

---

## Breach Notification Rule Cross-Reference

The HIPAA Breach Notification Rule (45 CFR Part 164, Subparts A and D) requires notification of affected individuals, HHS, and (for large breaches) media.

| Notification Timeline | Requirement | Policy File | Evidence Provided |
|----------------------|-------------|-------------|-------------------|
| Individual notification within 60 days | §164.404 | `policies/04-incident-response/data_breach_response_policy.md` | Breach notification timelines and stakeholder communication procedures |
| HHS notification within 60 days of year-end (< 500 individuals) | §164.408 | `policies/04-incident-response/data_breach_response_policy.md` | Annual breach log and HHS reporting obligations |
| HHS notification within 60 days of discovery (≥ 500 individuals) | §164.408 | `policies/04-incident-response/data_breach_response_policy.md` | Large-breach escalation triggers and regulatory notification path |
| Media notification within 60 days (≥ 500 in a jurisdiction) | §164.406 | `policies/04-incident-response/data_breach_response_policy.md` | Public disclosure procedures for major breach events |
| Business Associate notification without unreasonable delay | §164.410 | `policies/01-governance/vendor_third_party_risk_policy.md` | Vendor incident notification requirements and SLA for BA-to-CE reporting |

---

## HIPAA Audit Readiness Notes

Policy documents establish **administrative controls and written policies** required by the Security Rule. For OCR audits or internal gap assessments, you will additionally need:

1. **Current HIPAA Risk Analysis** — required by §164.308(a)(1); must be completed and updated after significant changes
2. **Training records** — documented evidence of workforce HIPAA training (within 60 days of hire, annually thereafter)
3. **BAA register** — list of all Business Associates with BAA execution dates and annual review records
4. **Audit log samples** — evidence of ePHI access audit controls operating effectively
5. **Incident log** — all security incidents and breaches logged with 4-factor risk assessment documentation
6. **Sanction records** — documented application of the workforce sanction policy

See the [Healthcare/HIPAA Industry Overlay](../industry-variants/healthcare-hipaa-overlay.md) for detailed implementation instructions on each requirement.

> [Talk to HailBytes about HIPAA compliance readiness →](https://hailbytes.com/enterprise?utm_source=github&utm_medium=mapping&utm_campaign=hipaa-readiness)

---

## Related Resources

- [ISO 27001 Mappings](./iso-27001.md)
- [NIST CSF Mappings](./nist-csf.md)
- [SOC 2 Mappings](./soc2.md)
- [LGPD Mappings](./lgpd.md)
- [GDPR Mappings](./gdpr.md)
- [CIS Controls v8 Mappings](./cis-controls.md)
- [Healthcare/HIPAA Industry Overlay](../industry-variants/healthcare-hipaa-overlay.md)
- [Enterprise Readiness Checklist](../docs/enterprise-readiness-checklist.md)
