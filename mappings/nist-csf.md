# NIST Cybersecurity Framework (CSF) 2.0 Mappings

This file maps each policy template to specific NIST CSF 2.0 subcategories. Use this during risk assessments, board-level reporting, or when responding to enterprise vendor questionnaires that reference NIST CSF.

> **Version note:** Mappings reflect NIST CSF 2.0 (February 2024), which added the **Govern (GV)** function and renumbered several subcategories. CSF 1.1 equivalents are noted where subcategory IDs changed.

---

## GOVERN (GV)

*New in CSF 2.0 — establishes organizational cybersecurity strategy, expectations, and policy.*

| Subcategory | Policy File | How It Satisfies |
|-------------|-------------|------------------|
| GV.OC-01: Mission, stakeholder expectations | `policies/01-governance/ethics_policy.md` | Documents organizational values and stakeholder obligations for information use |
| GV.OC-03: Legal, regulatory, contractual requirements | `policies/01-governance/data_classification_policy.md` | Data classification drives identification of applicable legal obligations |
| GV.OC-03 | `policies/01-governance/vendor_third_party_risk_policy.md` | Regulatory and contractual obligations for supplier relationships |
| GV.RM-01: Risk management strategy | `policies/01-governance/change_management_policy.md` | Change risk assessment integrated into approval workflow |
| GV.RM-06: Risk tolerance | `policies/05-infrastructure/vulnerability_patch_management_policy.md` | CVSS-based patching SLAs codify organizational risk tolerance |
| GV.PO-01: Policy established and communicated | `policies/01-governance/acceptable_use_policy.md` | Top-level acceptable use policy; requires staff acknowledgment |
| GV.PO-01 | `policies/01-governance/ai_usage_governance_policy.md` | AI usage governance policy for emerging technology risk |
| GV.SC-01: Supply chain risk management | `policies/01-governance/vendor_third_party_risk_policy.md` | Full vendor risk lifecycle from assessment to offboarding |

---

## IDENTIFY (ID)

### ID.AM — Asset Management
| Subcategory | Policy File | How It Satisfies |
|-------------|-------------|------------------|
| ID.AM-01: Inventory of hardware assets | `policies/05-infrastructure/server_security_policy.md` | Server and endpoint inventory requirements |
| ID.AM-01 | `policies/05-infrastructure/cloud_security_policy.md` | Cloud asset discovery and shadow IT controls |
| ID.AM-02: Inventory of software assets | `policies/05-infrastructure/server_security_policy.md` | Authorized software list and installation controls |
| ID.AM-02 | `policies/01-governance/change_management_policy.md` | Software change tracking via change management process |
| ID.AM-03: Organizational communication and data flows | `policies/03-communications/email_policy.md` | Documents authorized communication channels |
| ID.AM-05: Resources prioritized by criticality | `policies/01-governance/data_classification_policy.md` | Classification tiers drive asset prioritization |
| ID.AM-07: IT/OT assets inventoried | `policies/05-infrastructure/router_switch_security_policy.md` | Network device inventory and documentation |

### ID.RA — Risk Assessment
| Subcategory | Policy File | How It Satisfies |
|-------------|-------------|------------------|
| ID.RA-01: Vulnerabilities identified | `policies/05-infrastructure/vulnerability_patch_management_policy.md` | Regular scanning schedule and vulnerability identification process |
| ID.RA-02: Threat intelligence received | `policies/04-incident-response/security_response_plan_policy.md` | Threat monitoring and intelligence integration in IR process |
| ID.RA-05: Threats, vulnerabilities, likelihoods determined | `policies/05-infrastructure/vulnerability_patch_management_policy.md` | CVSS scoring and exploitability assessment requirements |
| ID.RA-06: Risk responses prioritized | `policies/05-infrastructure/vulnerability_patch_management_policy.md` | Risk-tiered patching SLAs (Critical 24h / High 7d / Medium 30d) |

### ID.SC — Supply Chain Risk Management
| Subcategory | Policy File | How It Satisfies |
|-------------|-------------|------------------|
| ID.SC-01: Cyber supply chain risk management | `policies/01-governance/vendor_third_party_risk_policy.md` | Third-party risk assessment and categorization procedures |
| ID.SC-02: Suppliers assessed | `policies/01-governance/vendor_third_party_risk_policy.md` | Pre-engagement vendor security questionnaire requirements |
| ID.SC-04: Supplier performance monitored | `policies/01-governance/vendor_third_party_risk_policy.md` | Annual re-assessment and incident notification requirements |

---

## PROTECT (PR)

### PR.AA — Identity Management, Authentication, and Access Control
| Subcategory | Policy File | How It Satisfies |
|-------------|-------------|------------------|
| PR.AA-01: Identities and credentials managed | `policies/02-access-control/password_protection_policy.md` | Identity lifecycle: provisioning, rotation, deprovisioning |
| PR.AA-02: Identities proofed and bound to credentials | `policies/02-access-control/password_protection_policy.md` | MFA requirements and credential binding standards |
| PR.AA-03: Users, services, hardware authenticated | `policies/02-access-control/password_protection_policy.md` | Authentication requirements for all user and service accounts |
| PR.AA-04: Identity assertions protected | `policies/05-infrastructure/server_security_policy.md` | Privileged account controls and session management |
| PR.AA-05: Access permissions managed | `policies/02-access-control/password_protection_policy.md` | Least privilege and access review requirements |
| PR.AA-05 | `policies/02-access-control/remote_work_byod_policy.md` | Remote access permission scoping and VPN requirements |
| PR.AA-06: Physical access controlled | `policies/02-access-control/clean_desk_policy.md` | Physical access controls for workspaces and equipment |

### PR.AT — Awareness and Training
| Subcategory | Policy File | How It Satisfies |
|-------------|-------------|------------------|
| PR.AT-01: Personnel trained | `policies/01-governance/acceptable_use_policy.md` | Policy acknowledgment and annual training requirements |
| PR.AT-01 | `policies/03-communications/email_policy.md` | Phishing awareness and email threat training requirements |
| PR.AT-02: Privileged users trained | `policies/05-infrastructure/server_security_policy.md` | Elevated training requirements for system administrators |

### PR.DS — Data Security
| Subcategory | Policy File | How It Satisfies |
|-------------|-------------|------------------|
| PR.DS-01: Data-at-rest protected | `policies/01-governance/data_classification_policy.md` | Encryption requirements based on classification tier |
| PR.DS-02: Data-in-transit protected | `policies/03-communications/email_policy.md` | TLS and encryption requirements for email and data transfer |
| PR.DS-02 | `policies/05-infrastructure/wireless_communication_policy.md` | WPA3/WPA2-Enterprise and wireless encryption requirements |
| PR.DS-10: Data used only for intended purpose | `policies/01-governance/ai_usage_governance_policy.md` | Restricts use of organizational data in AI training and queries |

### PR.IP — Information Protection Processes and Procedures
| Subcategory | Policy File | How It Satisfies |
|-------------|-------------|------------------|
| PR.IP-01: Baseline configurations established | `policies/05-infrastructure/server_security_policy.md` | CIS Benchmark-aligned server hardening baselines |
| PR.IP-01 | `policies/05-infrastructure/router_switch_security_policy.md` | Network device configuration baselines |
| PR.IP-03: Configuration change control | `policies/01-governance/change_management_policy.md` | Full ITSM-aligned change request and approval process |
| PR.IP-04: Backups maintained | `policies/06-continuity/disaster_recovery_plan_policy.md` | 3-2-1 backup strategy with integrity testing schedule |
| PR.IP-06: Data destroyed per policy | `policies/01-governance/data_classification_policy.md` | Data retention and secure disposal requirements by tier |
| PR.IP-12: Vulnerabilities remediated | `policies/05-infrastructure/vulnerability_patch_management_policy.md` | Risk-tiered patching SLAs with exception handling process |

---

## DETECT (DE)

### DE.AE — Anomalies and Events
| Subcategory | Policy File | How It Satisfies |
|-------------|-------------|------------------|
| DE.AE-02: Events analyzed to understand attacks | `policies/04-incident-response/security_response_plan_policy.md` | Event correlation and attack pattern analysis requirements |
| DE.AE-03: Event data aggregated | `policies/05-infrastructure/server_security_policy.md` | Centralized logging requirements for server events |
| DE.AE-06: Alerts created | `policies/04-incident-response/security_response_plan_policy.md` | Alert thresholds and escalation triggers defined |

### DE.CM — Continuous Monitoring
| Subcategory | Policy File | How It Satisfies |
|-------------|-------------|------------------|
| DE.CM-01: Networks monitored | `policies/05-infrastructure/router_switch_security_policy.md` | Network traffic monitoring and anomaly detection requirements |
| DE.CM-03: Personnel activity monitored | `policies/01-governance/acceptable_use_policy.md` | IT resource monitoring disclosure and requirements |
| DE.CM-09: Computing hardware and software monitored | `policies/05-infrastructure/vulnerability_patch_management_policy.md` | Continuous vulnerability scanning cadence |

---

## RESPOND (RS)

### RS.MA — Incident Management
| Subcategory | Policy File | How It Satisfies |
|-------------|-------------|------------------|
| RS.MA-01: Incident response executed | `policies/04-incident-response/security_response_plan_policy.md` | Full IR lifecycle from detection to closure |
| RS.MA-02: Incidents triaged | `policies/04-incident-response/security_response_plan_policy.md` | Severity classification and triage decision criteria |
| RS.MA-03: Incidents categorized | `policies/04-incident-response/data_breach_response_policy.md` | Breach vs. security incident categorization |
| RS.MA-05: Incidents escalated | `policies/04-incident-response/security_response_plan_policy.md` | Escalation matrix with executive and regulatory notification paths |

### RS.CO — Incident Response Reporting and Communication
| Subcategory | Policy File | How It Satisfies |
|-------------|-------------|------------------|
| RS.CO-02: Events reported to appropriate stakeholders | `policies/04-incident-response/data_breach_response_policy.md` | Regulatory notification timelines (72h GDPR, LGPD) and stakeholder communication |
| RS.CO-03: Information shared with stakeholders | `policies/04-incident-response/security_response_plan_policy.md` | Internal and external communication protocols during incidents |

### RS.AN — Incident Analysis
| Subcategory | Policy File | How It Satisfies |
|-------------|-------------|------------------|
| RS.AN-03: Analysis performed to establish scope | `policies/04-incident-response/data_breach_response_policy.md` | Breach scope assessment and data subject impact analysis |
| RS.AN-06: Actions performed during investigation documented | `policies/04-incident-response/security_response_plan_policy.md` | Evidence preservation and chain of custody requirements |

---

## RECOVER (RC)

### RC.RP — Incident Recovery Plan Execution
| Subcategory | Policy File | How It Satisfies |
|-------------|-------------|------------------|
| RC.RP-01: Recovery plan executed | `policies/06-continuity/disaster_recovery_plan_policy.md` | Full DR execution plan with RTO/RPO objectives |
| RC.RP-02: Recovery actions selected | `policies/06-continuity/disaster_recovery_plan_policy.md` | Decision framework for recovery strategy selection |
| RC.RP-03: Recovery performed per plan | `policies/06-continuity/disaster_recovery_plan_policy.md` | Step-by-step system recovery procedures |
| RC.RP-04: Incidents considered closed | `policies/04-incident-response/security_response_plan_policy.md` | Incident closure criteria and post-incident review requirements |
| RC.RP-05: Recovery activities communicated | `policies/04-incident-response/data_breach_response_policy.md` | Post-breach communication to regulators and affected parties |

### RC.CO — Incident Recovery Communication
| Subcategory | Policy File | How It Satisfies |
|-------------|-------------|------------------|
| RC.CO-03: Recovery activities communicated to stakeholders | `policies/06-continuity/disaster_recovery_plan_policy.md` | Business continuity communication procedures |

---

## Related Resources

- [ISO 27001 Mappings](./iso-27001.md)
- [SOC 2 Mappings](./soc2.md)
- [LGPD Mappings](./lgpd.md)
- [GDPR Mappings](./gdpr.md)
- [HIPAA Mappings](./hipaa.md)
- [CIS Controls v8 Mappings](./cis-controls.md)
- [Enterprise Readiness Checklist](../docs/enterprise-readiness-checklist.md)
- [HailBytes Enterprise Trust Package](https://hailbytes.com/enterprise?utm_source=github&utm_medium=mapping&utm_campaign=enterprise-trust)
