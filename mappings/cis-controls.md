# CIS Controls v8 Mappings

This file maps each policy template to specific CIS Controls v8 safeguards. Use this during vendor security questionnaires, security program gap assessments, or when planning your Implementation Group (IG) roadmap.

> **Implementation Groups:** CIS Controls v8 uses three tiered Implementation Groups.
> - **IG1** — Essential cyber hygiene; required by all organizations regardless of size or sector.
> - **IG2** — Adds controls for organizations handling sensitive data or with operational technology.
> - **IG3** — Adds controls required by organizations subject to regulatory or public-safety obligations.
>
> SMBs should prioritize IG1 safeguards first. The majority of IG1 safeguards are addressed by this template set.

---

## CIS Control 1 — Inventory and Control of Enterprise Assets

| Safeguard | IG | Policy File | How It Satisfies |
|-----------|----|-------------|------------------|
| 1.1 — Establish and maintain detailed enterprise asset inventory | IG1 | `policies/05-infrastructure/server_security_policy.md` | Requires hardware inventory with owner, location, and classification |
| 1.1 | IG1 | `policies/05-infrastructure/cloud_security_policy.md` | Cloud asset discovery and shadow IT identification requirements |
| 1.2 — Address unauthorized assets | IG1 | `policies/05-infrastructure/server_security_policy.md` | Procedures for detecting and quarantining unauthorized devices |

---

## CIS Control 2 — Inventory and Control of Software Assets

| Safeguard | IG | Policy File | How It Satisfies |
|-----------|----|-------------|------------------|
| 2.1 — Establish and maintain a software inventory | IG1 | `policies/05-infrastructure/server_security_policy.md` | Authorized software list and installation approval requirements |
| 2.2 — Ensure authorized software is currently supported | IG1 | `policies/05-infrastructure/vulnerability_patch_management_policy.md` | EOL software identification and replacement requirements |
| 2.3 — Address unauthorized software | IG1 | `policies/01-governance/change_management_policy.md` | Software change control process prevents unauthorized installations |
| 2.5 — Allowlist authorized software | IG2 | `policies/05-infrastructure/server_security_policy.md` | Application allowlisting requirements for servers |

---

## CIS Control 3 — Data Protection

| Safeguard | IG | Policy File | How It Satisfies |
|-----------|----|-------------|------------------|
| 3.1 — Establish and maintain a data management process | IG1 | `policies/01-governance/data_classification_policy.md` | Full data lifecycle governance and classification schema |
| 3.2 — Establish and maintain a data inventory | IG1 | `policies/01-governance/data_classification_policy.md` | Asset inventory requirements for all data containing personal or confidential information |
| 3.3 — Configure data access control lists | IG1 | `policies/02-access-control/password_protection_policy.md` | Least-privilege access requirements tied to classification tiers |
| 3.4 — Enforce data retention | IG1 | `policies/01-governance/data_classification_policy.md` | Retention schedules and secure disposal requirements by classification tier |
| 3.6 — Encrypt data on end-user devices | IG1 | `policies/02-access-control/remote_work_byod_policy.md` | Full-disk encryption required for all laptops and mobile devices |
| 3.11 — Encrypt sensitive data at rest | IG2 | `policies/01-governance/data_classification_policy.md` | Encryption requirements for Confidential and Restricted data tiers |
| 3.12 — Segment data processing and storage based on sensitivity | IG2 | `policies/01-governance/data_classification_policy.md` | Network and storage segmentation requirements for high-classification data |
| 3.14 — Log sensitive data access | IG2 | `policies/05-infrastructure/server_security_policy.md` | Audit logging requirements for access to sensitive systems and data stores |

---

## CIS Control 4 — Secure Configuration of Enterprise Assets and Software

| Safeguard | IG | Policy File | How It Satisfies |
|-----------|----|-------------|------------------|
| 4.1 — Establish and maintain a secure configuration process | IG1 | `policies/05-infrastructure/server_security_policy.md` | CIS Benchmark-aligned hardening baselines for all server types |
| 4.1 | IG1 | `policies/05-infrastructure/router_switch_security_policy.md` | Secure configuration baselines for network infrastructure |
| 4.2 — Establish and maintain a secure configuration process for network infrastructure | IG1 | `policies/05-infrastructure/router_switch_security_policy.md` | Network device configuration standards and change controls |
| 4.3 — Configure automatic session locking | IG1 | `policies/02-access-control/clean_desk_policy.md` | Workstation lock requirements (15-minute inactivity) |
| 4.4 — Implement and manage a firewall on servers | IG1 | `policies/05-infrastructure/server_security_policy.md` | Host-based firewall configuration requirements |
| 4.5 — Implement and manage a firewall on end-user devices | IG1 | `policies/02-access-control/remote_work_byod_policy.md` | Firewall requirements for remote and BYOD devices |
| 4.6 — Securely manage enterprise assets and software | IG2 | `policies/05-infrastructure/server_security_policy.md` | Privileged access and remote administration security requirements |
| 4.7 — Manage default accounts on enterprise assets and software | IG1 | `policies/05-infrastructure/server_security_policy.md` | Default credential removal and account rename requirements |

---

## CIS Control 5 — Account Management

| Safeguard | IG | Policy File | How It Satisfies |
|-----------|----|-------------|------------------|
| 5.1 — Establish and maintain an inventory of accounts | IG1 | `policies/02-access-control/password_protection_policy.md` | Account lifecycle management including provisioning and deprovisioning |
| 5.2 — Use unique passwords | IG1 | `policies/02-access-control/password_protection_policy.md` | Unique password requirements and prohibition of password reuse |
| 5.3 — Disable dormant accounts | IG1 | `policies/02-access-control/password_protection_policy.md` | 90-day dormancy review and automatic account disable procedures |
| 5.4 — Restrict administrator privileges to dedicated admin accounts | IG1 | `policies/05-infrastructure/server_security_policy.md` | Separation of privileged and standard user accounts |
| 5.5 — Establish and maintain an inventory of service accounts | IG2 | `policies/05-infrastructure/server_security_policy.md` | Service account inventory and rotation requirements |
| 5.6 — Centralize account management | IG2 | `policies/05-infrastructure/server_security_policy.md` | Directory service and centralized identity management requirements |

---

## CIS Control 6 — Access Control Management

| Safeguard | IG | Policy File | How It Satisfies |
|-----------|----|-------------|------------------|
| 6.1 — Establish an access-granting and -revoking process | IG1 | `policies/02-access-control/password_protection_policy.md` | Formal access provisioning and deprovisioning procedures |
| 6.2 — Establish an access review process | IG1 | `policies/02-access-control/password_protection_policy.md` | Quarterly access review requirements for all accounts |
| 6.3 — Require MFA for externally exposed applications | IG1 | `policies/02-access-control/password_protection_policy.md` | MFA required for all external-facing applications |
| 6.4 — Require MFA for remote network access | IG1 | `policies/02-access-control/remote_work_byod_policy.md` | MFA requirement for VPN and remote access solutions |
| 6.5 — Require MFA for administrative access | IG2 | `policies/02-access-control/password_protection_policy.md` | MFA required for all privileged and administrative accounts |
| 6.5 | IG2 | `policies/05-infrastructure/server_security_policy.md` | MFA enforcement for server and infrastructure admin access |
| 6.6 — Establish and maintain an inventory of authentication and authorization systems | IG2 | `policies/02-access-control/password_protection_policy.md` | SSO and identity provider inventory requirements |
| 6.7 — Centralize access control | IG3 | `policies/05-infrastructure/server_security_policy.md` | Centralized PAM and privileged session management requirements |
| 6.8 — Define and maintain role-based access control | IG3 | `policies/01-governance/data_classification_policy.md` | Role-based access tied to data classification levels |

---

## CIS Control 7 — Continuous Vulnerability Management

| Safeguard | IG | Policy File | How It Satisfies |
|-----------|----|-------------|------------------|
| 7.1 — Establish and maintain a vulnerability management process | IG1 | `policies/05-infrastructure/vulnerability_patch_management_policy.md` | End-to-end vulnerability lifecycle: scan → triage → remediate → verify |
| 7.2 — Establish and maintain a remediation process | IG1 | `policies/05-infrastructure/vulnerability_patch_management_policy.md` | Risk-tiered patching SLAs (Critical 24h / High 7d / Medium 30d) |
| 7.3 — Perform automated OS patch management | IG2 | `policies/05-infrastructure/vulnerability_patch_management_policy.md` | Automated patch deployment requirements and exception handling |
| 7.4 — Perform automated application patch management | IG2 | `policies/05-infrastructure/vulnerability_patch_management_policy.md` | Application patching requirements using CVSS scoring |
| 7.5 — Perform automated vulnerability scans of internal enterprise assets | IG2 | `policies/05-infrastructure/vulnerability_patch_management_policy.md` | Weekly internal scanning cadence and scope requirements |
| 7.6 — Perform automated vulnerability scans of externally exposed enterprise assets | IG2 | `policies/05-infrastructure/vulnerability_patch_management_policy.md` | Monthly external-facing scan requirements |
| 7.7 — Remediate detected vulnerabilities | IG2 | `policies/05-infrastructure/vulnerability_patch_management_policy.md` | Remediation verification and risk-acceptance exception process |

---

## CIS Control 8 — Audit Log Management

| Safeguard | IG | Policy File | How It Satisfies |
|-----------|----|-------------|------------------|
| 8.1 — Establish and maintain an audit log management process | IG1 | `policies/05-infrastructure/server_security_policy.md` | Log collection, retention (90-day minimum), and protection requirements |
| 8.2 — Collect audit logs | IG1 | `policies/05-infrastructure/server_security_policy.md` | Log source requirements for servers, applications, and authentication systems |
| 8.2 | IG1 | `policies/05-infrastructure/router_switch_security_policy.md` | Network device syslog and flow logging requirements |
| 8.3 — Ensure adequate storage for logs | IG2 | `policies/05-infrastructure/server_security_policy.md` | Log storage capacity planning and offload requirements |
| 8.7 — Collect URL request audit logs | IG2 | `policies/01-governance/acceptable_use_policy.md` | Web filtering and URL logging disclosure |
| 8.11 — Conduct audit log reviews | IG2 | `policies/04-incident-response/security_response_plan_policy.md` | Periodic log review requirements and anomaly escalation |

---

## CIS Control 9 — Email and Web Browser Protections

| Safeguard | IG | Policy File | How It Satisfies |
|-----------|----|-------------|------------------|
| 9.1 — Ensure use of only fully supported browsers and email clients | IG1 | `policies/03-communications/email_policy.md` | Approved email client list and update requirements |
| 9.2 — Use DNS filtering services | IG1 | `policies/01-governance/acceptable_use_policy.md` | DNS filtering and prohibited categories |
| 9.3 — Maintain and enforce network-based URL filters | IG2 | `policies/01-governance/acceptable_use_policy.md` | Web content filtering requirements and business-use justification process |
| 9.4 — Restrict unnecessary or unauthorized browser and email client extensions | IG2 | `policies/01-governance/acceptable_use_policy.md` | Browser extension allowlist and prohibition of unapproved add-ons |
| 9.5 — Implement DMARC and enable SMTP relay blocking | IG2 | `policies/03-communications/email_policy.md` | DMARC, DKIM, and SPF configuration requirements |
| 9.6 — Block unnecessary file types | IG2 | `policies/03-communications/email_policy.md` | Attachment type restrictions and file extension filtering |
| 9.7 — Deploy and maintain email server anti-malware protections | IG2 | `policies/03-communications/email_policy.md` | Anti-malware scanning requirements for inbound and outbound mail |

---

## CIS Control 10 — Malware Defenses

| Safeguard | IG | Policy File | How It Satisfies |
|-----------|----|-------------|------------------|
| 10.1 — Deploy and maintain anti-malware software | IG1 | `policies/05-infrastructure/server_security_policy.md` | Anti-malware deployment requirements for all endpoints and servers |
| 10.2 — Configure automatic anti-malware signature updates | IG1 | `policies/05-infrastructure/server_security_policy.md` | Signature and engine update cadence requirements |
| 10.2 | IG1 | `policies/05-infrastructure/vulnerability_patch_management_policy.md` | Security tooling update included in patch management scope |
| 10.3 — Disable autorun and autoplay for removable media | IG1 | `policies/02-access-control/clean_desk_policy.md` | Removable media controls including autorun disable |
| 10.5 — Enable anti-exploitation features | IG2 | `policies/05-infrastructure/server_security_policy.md` | OS-level exploit mitigation requirements (ASLR, DEP) |
| 10.6 — Centrally manage anti-malware software | IG2 | `policies/05-infrastructure/server_security_policy.md` | Centralized AV/EDR management and reporting requirements |
| 10.7 — Use behavior-based anti-malware software | IG2 | `policies/05-infrastructure/server_security_policy.md` | EDR/behavior-based detection requirements for servers |

---

## CIS Control 11 — Data Recovery

| Safeguard | IG | Policy File | How It Satisfies |
|-----------|----|-------------|------------------|
| 11.1 — Establish and maintain a data recovery process | IG1 | `policies/06-continuity/disaster_recovery_plan_policy.md` | Full data recovery lifecycle with defined RTO/RPO targets |
| 11.2 — Perform automated backups | IG1 | `policies/06-continuity/disaster_recovery_plan_policy.md` | Daily automated backup requirements for all critical systems |
| 11.3 — Protect recovery data | IG1 | `policies/06-continuity/disaster_recovery_plan_policy.md` | Backup encryption and access control requirements |
| 11.4 — Establish and maintain an isolated instance of recovery data | IG1 | `policies/06-continuity/disaster_recovery_plan_policy.md` | 3-2-1 backup strategy including offsite/offline copy |
| 11.5 — Test data recovery | IG2 | `policies/06-continuity/disaster_recovery_plan_policy.md` | Quarterly backup restore tests with documented results |

---

## CIS Control 12 — Network Infrastructure Management

| Safeguard | IG | Policy File | How It Satisfies |
|-----------|----|-------------|------------------|
| 12.1 — Ensure network infrastructure is up-to-date | IG1 | `policies/05-infrastructure/router_switch_security_policy.md` | Firmware update and EOL replacement requirements for network devices |
| 12.2 — Establish and maintain a secure network architecture | IG1 | `policies/05-infrastructure/router_switch_security_policy.md` | Network segmentation and DMZ design requirements |
| 12.2 | IG1 | `policies/05-infrastructure/wireless_communication_policy.md` | Wireless network isolation and guest VLAN requirements |
| 12.3 — Securely manage network infrastructure | IG2 | `policies/05-infrastructure/router_switch_security_policy.md` | Out-of-band management and secure protocol requirements (SSH, HTTPS) |
| 12.4 — Establish and maintain architecture diagram(s) | IG2 | `policies/05-infrastructure/router_switch_security_policy.md` | Network documentation and topology diagram requirements |
| 12.6 — Use secure network management and communication protocols | IG2 | `policies/05-infrastructure/router_switch_security_policy.md` | Deprecated protocol disable requirements (Telnet, SNMPv1/v2) |
| 12.7 — Ensure remote devices utilize a VPN | IG2 | `policies/02-access-control/remote_work_byod_policy.md` | Mandatory VPN requirements for remote access |
| 12.8 — Establish and maintain dedicated computing resources for administration | IG3 | `policies/05-infrastructure/server_security_policy.md` | Jump server / bastion host requirements for privileged access |

---

## CIS Control 13 — Network Monitoring and Defense

| Safeguard | IG | Policy File | How It Satisfies |
|-----------|----|-------------|------------------|
| 13.1 — Centralize security event alerting | IG2 | `policies/04-incident-response/security_response_plan_policy.md` | SIEM/log aggregation requirements and alert threshold definitions |
| 13.2 — Deploy a host-based intrusion detection solution | IG2 | `policies/05-infrastructure/server_security_policy.md` | Host IDS/IPS or EDR deployment requirements |
| 13.6 — Collect network traffic flow logs | IG2 | `policies/05-infrastructure/router_switch_security_policy.md` | NetFlow/IPFIX or equivalent traffic logging requirements |
| 13.7 — Deploy a host-based intrusion prevention solution | IG3 | `policies/05-infrastructure/server_security_policy.md` | Host-based IPS configuration and response policy |

---

## CIS Control 14 — Security Awareness and Skills Training

| Safeguard | IG | Policy File | How It Satisfies |
|-----------|----|-------------|------------------|
| 14.1 — Establish and maintain a security awareness program | IG1 | `policies/01-governance/acceptable_use_policy.md` | Annual security awareness training requirements for all employees |
| 14.2 — Train workforce members to recognize social engineering attacks | IG1 | `policies/03-communications/email_policy.md` | Phishing recognition and reporting training requirements |
| 14.3 — Train workforce members on authentication best practices | IG1 | `policies/02-access-control/password_protection_policy.md` | Password hygiene and MFA training requirements |
| 14.4 — Train workforce on data handling best practices | IG1 | `policies/01-governance/data_classification_policy.md` | Data classification training and handling procedure requirements |
| 14.5 — Train workforce members on causes of unintentional data exposure | IG1 | `policies/02-access-control/clean_desk_policy.md` | Physical security awareness and clean desk training |
| 14.6 — Train workforce members on recognizing and reporting security incidents | IG1 | `policies/04-incident-response/security_response_plan_policy.md` | Incident recognition and escalation training requirements |
| 14.7 — Train workforce on how to identify and report missing or broken security updates | IG2 | `policies/05-infrastructure/vulnerability_patch_management_policy.md` | End-user patch awareness and reporting procedures |
| 14.8 — Train workforce on the dangers of connecting to and transmitting data over insecure networks | IG2 | `policies/02-access-control/remote_work_byod_policy.md` | Public Wi-Fi prohibition and VPN use requirements |
| 14.9 — Conduct role-specific security awareness and skills training | IG3 | `policies/01-governance/acceptable_use_policy.md` | Role-differentiated training requirements for IT, executives, and general staff |

---

## CIS Control 15 — Service Provider Management

| Safeguard | IG | Policy File | How It Satisfies |
|-----------|----|-------------|------------------|
| 15.1 — Establish and maintain an inventory of service providers | IG1 | `policies/01-governance/vendor_third_party_risk_policy.md` | Vendor inventory with classification and contact information |
| 15.2 — Establish and maintain a service provider management policy | IG2 | `policies/01-governance/vendor_third_party_risk_policy.md` | Full vendor risk management lifecycle from onboarding to offboarding |
| 15.3 — Classify service providers | IG2 | `policies/01-governance/vendor_third_party_risk_policy.md` | Vendor risk tier classification (Critical / High / Standard) |
| 15.4 — Ensure service provider contracts include security requirements | IG2 | `policies/01-governance/vendor_third_party_risk_policy.md` | Minimum contractual security requirements and DPA provisions |
| 15.5 — Assess service providers | IG3 | `policies/01-governance/vendor_third_party_risk_policy.md` | Annual security re-assessment and questionnaire requirements |
| 15.6 — Monitor service providers | IG3 | `policies/01-governance/vendor_third_party_risk_policy.md` | Continuous monitoring and incident notification requirements |
| 15.7 — Securely decommission service providers | IG3 | `policies/01-governance/vendor_third_party_risk_policy.md` | Offboarding procedures for data deletion and access revocation |

---

## CIS Control 16 — Application Software Security

| Safeguard | IG | Policy File | How It Satisfies |
|-----------|----|-------------|------------------|
| 16.1 — Establish and maintain a secure application development process | IG2 | `policies/01-governance/change_management_policy.md` | Change control process provides partial governance for application changes |
| 16.2 — Establish and maintain a process to accept and address software vulnerabilities | IG2 | `policies/05-infrastructure/vulnerability_patch_management_policy.md` | Application vulnerability triage and patching SLAs |
| 16.6 — Establish and maintain a severity rating system for application vulnerabilities | IG2 | `policies/05-infrastructure/vulnerability_patch_management_policy.md` | CVSS-based severity rating and remediation timeline matrix |

> **Coverage gap:** CIS Control 16 safeguards related to secure SDLC, code review, penetration testing of custom applications, and web application firewall deployment are not fully addressed by this template set. Organizations that develop custom software should supplement with a Secure Software Development Lifecycle (SSDLC) policy.

---

## CIS Control 17 — Incident Response Management

| Safeguard | IG | Policy File | How It Satisfies |
|-----------|----|-------------|------------------|
| 17.1 — Designate personnel to manage incident handling | IG1 | `policies/04-incident-response/security_response_plan_policy.md` | Incident Response Team roles and designated coordinator |
| 17.2 — Establish and maintain contact information for reporting incidents | IG1 | `policies/04-incident-response/security_response_plan_policy.md` | Internal and external escalation contact lists |
| 17.2 | IG1 | `policies/04-incident-response/data_breach_response_policy.md` | Regulatory notification contacts (DPA, law enforcement) |
| 17.3 — Establish and maintain an enterprise process for reporting incidents | IG1 | `policies/04-incident-response/security_response_plan_policy.md` | Employee incident reporting channel and escalation path |
| 17.4 — Establish and maintain an incident response process | IG2 | `policies/04-incident-response/security_response_plan_policy.md` | End-to-end IR process: detection → containment → eradication → recovery |
| 17.5 — Assign key roles and responsibilities | IG2 | `policies/04-incident-response/security_response_plan_policy.md` | RACI matrix for incident response activities |
| 17.6 — Define mechanisms for communicating during incident response | IG2 | `policies/04-incident-response/data_breach_response_policy.md` | Communication protocols including out-of-band channels for major incidents |
| 17.7 — Conduct routine incident response exercises | IG2 | `policies/04-incident-response/security_response_plan_policy.md` | Annual tabletop and quarterly review exercise requirements |
| 17.8 — Conduct post-incident reviews | IG3 | `policies/04-incident-response/security_response_plan_policy.md` | Mandatory post-incident review and lessons-learned process |
| 17.9 — Establish and maintain security incident thresholds | IG3 | `policies/04-incident-response/security_response_plan_policy.md` | Severity classification matrix with escalation triggers |

---

## CIS Control 18 — Penetration Testing

| Safeguard | IG | Policy File | How It Satisfies |
|-----------|----|-------------|------------------|
| 18.2 — Perform periodic external penetration tests | IG2 | `policies/05-infrastructure/vulnerability_patch_management_policy.md` | Annual external assessment requirement as part of vulnerability management |
| 18.3 — Remediate penetration test findings | IG2 | `policies/05-infrastructure/vulnerability_patch_management_policy.md` | Remediation SLAs apply to findings from authorized assessments |

> **Coverage gap:** A formal penetration testing policy governing scope definition, rules of engagement, internal testing, and red team exercises is not included in this template set. Organizations subject to PCI DSS, SOC 2, or FedRAMP requirements should add a dedicated penetration testing policy.

---

## IG1 Coverage Summary

The following table shows which IG1 safeguards (essential cyber hygiene) are addressed by this template set. IG1 coverage is most relevant for small businesses (1–25 employees).

| CIS Control | IG1 Safeguards Total | Covered by Templates | Gap |
|-------------|----------------------|----------------------|-----|
| 1 — Asset Inventory | 2 | 2 | None |
| 2 — Software Inventory | 2 | 2 | None |
| 3 — Data Protection | 4 | 4 | None |
| 4 — Secure Configuration | 5 | 5 | None |
| 5 — Account Management | 4 | 4 | None |
| 6 — Access Control | 4 | 4 | None |
| 7 — Vulnerability Management | 2 | 2 | None |
| 8 — Audit Logs | 2 | 2 | None |
| 9 — Email & Web | 2 | 2 | None |
| 10 — Malware Defenses | 3 | 3 | None |
| 11 — Data Recovery | 4 | 4 | None |
| 12 — Network Infrastructure | 2 | 2 | None |
| 13 — Network Monitoring | 0 (IG2+) | — | IG2 only |
| 14 — Security Awareness | 6 | 6 | None |
| 15 — Service Providers | 1 | 1 | None |
| 16 — Application Security | 0 (IG2+) | — | IG2 only |
| 17 — Incident Response | 3 | 3 | None |
| 18 — Penetration Testing | 0 (IG2+) | — | IG2 only |

**All 52 IG1 safeguards that apply to this template set are addressed.** Controls 13, 16, and 18 have no IG1 safeguards; their IG2+ safeguards are partially covered.

---

## Related Resources

- [NIST CSF 2.0 Mappings](./nist-csf.md)
- [ISO 27001:2022 Mappings](./iso-27001.md)
- [SOC 2 Mappings](./soc2.md)
- [LGPD Mappings](./lgpd.md)
- [Framework Cross-Reference (all four frameworks in one table)](../docs/framework_mapping.md)
- [Enterprise Readiness Checklist](../docs/enterprise-readiness-checklist.md)
- [CIS Controls v8 (official)](https://www.cisecurity.org/controls/v8)
