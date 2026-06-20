# SOC 2 Trust Services Criteria (TSC) Mappings

This file maps each policy template to the AICPA Trust Services Criteria used in SOC 2 Type I and Type II audits. Use this to build your evidence library, prepare auditor walkthroughs, or identify gaps before engaging a SOC 2 auditor.

> **Scope note:** SOC 2 auditors evaluate whether controls are **designed** (Type I) and **operating effectively over time** (Type II). Policy documents satisfy design evidence. You will also need operational evidence (logs, access reviews, training records) — see the [Enterprise Readiness Checklist](../docs/enterprise-readiness-checklist.md).

---

## CC1 — Control Environment

*Demonstrates that the organization has commitment to integrity, ethical values, and board oversight.*

| Criterion | Policy File | Evidence Provided |
|-----------|-------------|-------------------|
| CC1.1: Commitment to integrity and ethical values | `policies/01-governance/ethics_policy.md` | Documents organizational ethics standards and enforcement |
| CC1.1 | `policies/01-governance/acceptable_use_policy.md` | Establishes behavioral expectations for IT resource use |
| CC1.2: Board oversight of internal controls | `policies/01-governance/change_management_policy.md` | Change approval authority and oversight structure |
| CC1.3: Organizational structures and reporting lines | `policies/04-incident-response/security_response_plan_policy.md` | Incident escalation hierarchy and executive reporting |
| CC1.4: Commitment to attract and retain competent staff | `policies/01-governance/acceptable_use_policy.md` | Policy acknowledgment process as part of onboarding |
| CC1.5: Accountability for internal control responsibilities | `policies/01-governance/data_classification_policy.md` | Data owner accountability assignments |

---

## CC2 — Communication and Information

*Ensures the organization obtains, generates, and uses relevant, quality information.*

| Criterion | Policy File | Evidence Provided |
|-----------|-------------|-------------------|
| CC2.2: Internal communication of objectives | `policies/01-governance/acceptable_use_policy.md` | Policy distribution and acknowledgment records |
| CC2.2 | `policies/03-communications/email_policy.md` | Secure communication standards and awareness requirements |
| CC2.3: External communication of commitments | `policies/04-incident-response/data_breach_response_policy.md` | External stakeholder notification procedures and timelines |

---

## CC3 — Risk Assessment

*Demonstrates that the organization specifies objectives and identifies and analyzes risks.*

| Criterion | Policy File | Evidence Provided |
|-----------|-------------|-------------------|
| CC3.1: Defined objectives | `policies/01-governance/data_classification_policy.md` | Data protection objectives by classification tier |
| CC3.2: Risk identification and analysis | `policies/01-governance/data_classification_policy.md` | Risk-based classification framework for information assets |
| CC3.2 | `policies/01-governance/ai_usage_governance_policy.md` | AI-specific risk identification and analysis |
| CC3.3: Fraud risk considered | `policies/01-governance/ethics_policy.md` | Fraud prevention and reporting obligations |
| CC3.4: Change and disruption effects identified | `policies/01-governance/change_management_policy.md` | Change impact assessment and risk documentation |

---

## CC4 — Monitoring Activities

*Demonstrates that the organization selects and develops ongoing evaluations.*

| Criterion | Policy File | Evidence Provided |
|-----------|-------------|-------------------|
| CC4.1: Ongoing and separate evaluations | `policies/05-infrastructure/vulnerability_patch_management_policy.md` | Continuous vulnerability scanning and periodic assessments |
| CC4.2: Evaluation results communicated | `policies/04-incident-response/security_response_plan_policy.md` | Security monitoring results escalation to management |

---

## CC5 — Control Activities

*Demonstrates that the organization selects and develops control activities.*

| Criterion | Policy File | Evidence Provided |
|-----------|-------------|-------------------|
| CC5.1: Controls selected to mitigate risks | `policies/05-infrastructure/server_security_policy.md` | Risk-based hardening controls for server infrastructure |
| CC5.2: Technology controls selected | `policies/05-infrastructure/cloud_security_policy.md` | Technical controls for cloud environment security |
| CC5.3: Control policies and procedures deployed | `policies/01-governance/change_management_policy.md` | Operational procedures for configuration change control |

---

## CC6 — Logical and Physical Access Controls

*The most commonly tested SOC 2 criteria category.*

| Criterion | Policy File | Evidence Provided |
|-----------|-------------|-------------------|
| CC6.1: Logical access security measures | `policies/02-access-control/password_protection_policy.md` | MFA, password complexity, account provisioning/deprovisioning |
| CC6.1 | `policies/01-governance/acceptable_use_policy.md` | Authorized use boundaries for system access |
| CC6.2: Authentication prior to access | `policies/02-access-control/password_protection_policy.md` | Authentication requirements for all systems |
| CC6.3: Role-based access and least privilege | `policies/02-access-control/password_protection_policy.md` | Role-based access provisioning and periodic review |
| CC6.3 | `policies/05-infrastructure/server_security_policy.md` | Privileged access controls and admin account management |
| CC6.4: Physical access restricted | `policies/02-access-control/clean_desk_policy.md` | Physical security controls for work areas and equipment |
| CC6.6: Logical access for remote and third parties | `policies/02-access-control/remote_work_byod_policy.md` | Remote access controls, VPN requirements, BYOD policy |
| CC6.6 | `policies/01-governance/vendor_third_party_risk_policy.md` | Third-party access provisioning and revocation procedures |
| CC6.7: Restriction of unauthorized access | `policies/05-infrastructure/wireless_communication_policy.md` | Wireless network segmentation and unauthorized access controls |
| CC6.8: Malicious software prevented | `policies/03-communications/email_policy.md` | Email-borne malware controls and attachment policies |
| CC6.8 | `policies/05-infrastructure/server_security_policy.md` | Anti-malware deployment and update requirements |

---

## CC7 — System Operations

*Demonstrates that the system operates to meet commitments.*

| Criterion | Policy File | Evidence Provided |
|-----------|-------------|-------------------|
| CC7.1: Vulnerabilities managed | `policies/05-infrastructure/vulnerability_patch_management_policy.md` | Full vulnerability management lifecycle with SLA requirements |
| CC7.1 | `policies/05-infrastructure/server_security_policy.md` | Server-level vulnerability detection and remediation |
| CC7.2: System components monitored | `policies/05-infrastructure/server_security_policy.md` | Logging, SIEM integration, and alerting requirements |
| CC7.2 | `policies/05-infrastructure/cloud_security_policy.md` | Cloud workload monitoring and threat detection |
| CC7.3: Evaluation of security events | `policies/04-incident-response/security_response_plan_policy.md` | Security event triage, classification, and escalation |
| CC7.4: Identification of and response to security incidents | `policies/04-incident-response/data_breach_response_policy.md` | Full breach detection and response lifecycle |
| CC7.4 | `policies/04-incident-response/security_response_plan_policy.md` | Incident response procedures from detection to closure |
| CC7.5: Identified security incidents addressed | `policies/04-incident-response/security_response_plan_policy.md` | Post-incident remediation and lessons-learned requirements |

---

## CC8 — Change Management

*Demonstrates that changes to infrastructure, data, software, and procedures are authorized.*

| Criterion | Policy File | Evidence Provided |
|-----------|-------------|-------------------|
| CC8.1: Changes authorized, designed, developed, tested, approved | `policies/01-governance/change_management_policy.md` | Full ITSM change lifecycle with approval gates and rollback |

---

## CC9 — Risk Mitigation

*Demonstrates that the organization identifies and manages risk from business disruption and vendor/business partner relationships.*

| Criterion | Policy File | Evidence Provided |
|-----------|-------------|-------------------|
| CC9.1: Risk mitigation activities | `policies/06-continuity/disaster_recovery_plan_policy.md` | Business continuity and DR as risk mitigation |
| CC9.2: Vendor and business partner risk | `policies/01-governance/vendor_third_party_risk_policy.md` | Third-party risk assessment, contracts, and monitoring |

---

## Availability (A1)

*Required for SOC 2 reports with Availability in scope.*

| Criterion | Policy File | Evidence Provided |
|-----------|-------------|-------------------|
| A1.1: Availability commitments and requirements identified | `policies/06-continuity/disaster_recovery_plan_policy.md` | RTO/RPO objectives and availability SLA documentation |
| A1.2: Environmental threats and vulnerabilities managed | `policies/06-continuity/disaster_recovery_plan_policy.md` | Environmental risk controls and backup infrastructure |
| A1.3: Recovery plan tested | `policies/06-continuity/disaster_recovery_plan_policy.md` | DR test schedule and tabletop exercise requirements |

---

## Confidentiality (C1)

*Required for SOC 2 reports with Confidentiality in scope.*

| Criterion | Policy File | Evidence Provided |
|-----------|-------------|-------------------|
| C1.1: Confidential information identified | `policies/01-governance/data_classification_policy.md` | Classification tiers including Confidential and Restricted |
| C1.2: Confidential information protected | `policies/01-governance/data_classification_policy.md` | Encryption, access, and handling controls by tier |
| C1.2 | `policies/02-access-control/password_protection_policy.md` | Access controls protecting confidential information |

---

## SOC 2 Audit Readiness Notes

These policy documents establish **design evidence** for the criteria above. For Type II audits, you will additionally need:

1. **Evidence of operation** — access review records, training completion logs, change tickets, scan results
2. **SOC 2 attestation** — requires a licensed CPA firm; HailBytes can facilitate introductions
3. **Pen test report** — most auditors expect one within the prior 12 months
4. **Vendor contracts** — signed DPAs and security addenda for material third parties

See the [Enterprise Readiness Checklist](../docs/enterprise-readiness-checklist.md) for the full gap list.

> [Talk to HailBytes about SOC 2 readiness →](https://hailbytes.com/enterprise?utm_source=github&utm_medium=mapping&utm_campaign=enterprise-trust)

---

## Related Resources

- [ISO 27001 Mappings](./iso-27001.md)
- [NIST CSF Mappings](./nist-csf.md)
- [LGPD Mappings](./lgpd.md)
- [GDPR Mappings](./gdpr.md)
- [Enterprise Readiness Checklist](../docs/enterprise-readiness-checklist.md)
