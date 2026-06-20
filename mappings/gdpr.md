# GDPR (General Data Protection Regulation) Mappings

This file maps each policy template to the relevant provisions of the **EU General Data Protection Regulation** (Regulation (EU) 2016/679, GDPR), which applies to any organisation processing personal data of individuals in the European Economic Area regardless of where the organisation is established.

These mappings support enterprise deals involving EU data subjects, Data Processing Agreements (DPAs), vendor security questionnaires, and audit evidence packages for customers in GDPR-regulated markets.

> **Disclaimer:** This mapping is intended to assist compliance practitioners and should not substitute for legal advice. GDPR enforcement is led by national **Data Protection Authorities (DPAs)** coordinated through the **European Data Protection Board (EDPB)**. Consult qualified legal counsel for formal compliance determinations.

---

## Chapter II — Data Protection Principles (Article 5)

Article 5 establishes seven core principles that govern all personal data processing.

| Principle | Policy File | How It Satisfies |
|-----------|-------------|------------------|
| **Lawfulness, fairness and transparency** (Art. 5(1)(a)) | `policies/01-governance/acceptable_use_policy.md` | Documents lawful basis for monitoring IT resources used to process personal data |
| **Lawfulness, fairness and transparency** (Art. 5(1)(a)) | `policies/01-governance/ethics_policy.md` | Establishes transparency obligations for organizational data practices |
| **Purpose limitation** (Art. 5(1)(b)) | `policies/01-governance/data_classification_policy.md` | Classification schema requires documented purpose for each personal data category; prohibits secondary use |
| **Data minimisation** (Art. 5(1)(c)) | `policies/01-governance/data_classification_policy.md` | Retention schedules and minimum-necessary collection requirements by classification tier |
| **Data minimisation** (Art. 5(1)(c)) | `policies/01-governance/ai_usage_governance_policy.md` | Restricts personal data input to AI systems to what is strictly necessary |
| **Accuracy** (Art. 5(1)(d)) | `policies/01-governance/data_classification_policy.md` | Data quality and accuracy requirements; procedures for correcting inaccurate personal data |
| **Storage limitation** (Art. 5(1)(e)) | `policies/01-governance/data_classification_policy.md` | Retention schedules define maximum storage periods per classification tier |
| **Integrity and confidentiality** (Art. 5(1)(f)) | `policies/02-access-control/password_protection_policy.md` | Technical access controls protecting personal data from unauthorized access |
| **Integrity and confidentiality** (Art. 5(1)(f)) | `policies/05-infrastructure/server_security_policy.md` | Infrastructure security measures protecting systems that process personal data |
| **Integrity and confidentiality** (Art. 5(1)(f)) | `policies/05-infrastructure/cloud_security_policy.md` | Cloud security controls and encryption for personal data in hosted environments |
| **Accountability** (Art. 5(2)) | `policies/01-governance/vendor_third_party_risk_policy.md` | Documented accountability for sub-processors and data sharing arrangements |
| **Accountability** (Art. 5(2)) | `policies/01-governance/change_management_policy.md` | Audit trails of decisions affecting personal data processing systems |

---

## Article 6 — Lawfulness of Processing

Article 6 requires that every processing activity has a documented legal basis.

| Legal Basis | Policy File | How It Satisfies |
|-------------|-------------|------------------|
| Art. 6(1)(a) — Consent | `policies/01-governance/data_classification_policy.md` | Classification framework identifies data sets requiring consent as a legal basis |
| Art. 6(1)(b) — Performance of contract | `policies/01-governance/acceptable_use_policy.md` | IT resource monitoring justified as necessary for employment contract performance |
| Art. 6(1)(c) — Legal obligation | `policies/04-incident-response/data_breach_response_policy.md` | Breach notification processing justified under Art. 33/34 legal obligation |
| Art. 6(1)(f) — Legitimate interests | `policies/01-governance/acceptable_use_policy.md` | Legitimate-interest assessment for IT monitoring documented in policy scope |

---

## Article 9 — Special Categories of Personal Data

Article 9 imposes heightened protection for health, biometric, racial, political, religious, and similar sensitive data.

| Requirement | Policy File | How It Satisfies |
|-------------|-------------|------------------|
| Explicit consent or other Art. 9(2) basis required | `policies/01-governance/data_classification_policy.md` | Restricted classification tier captures special-category data with enhanced handling rules |
| Appropriate technical safeguards | `policies/05-infrastructure/server_security_policy.md` | Enhanced access controls and encryption for restricted-tier data stores |
| Appropriate organizational safeguards | `policies/01-governance/vendor_third_party_risk_policy.md` | Heightened vendor assessment requirements when sub-processors handle special-category data |

---

## Chapter III — Data Subject Rights (Articles 15–21)

These rights must be operationalized through internal procedures; the policies below provide supporting governance and evidence.

| Right | Article | Policy File | Supporting Governance |
|-------|---------|-------------|----------------------|
| Right of access | Art. 15 | `policies/01-governance/data_classification_policy.md` | Classification enables identification of where subject data is held to fulfil subject access requests |
| Right to rectification | Art. 16 | `policies/01-governance/data_classification_policy.md` | Data quality requirements and update procedures support rectification obligations |
| Right to erasure ("right to be forgotten") | Art. 17 | `policies/01-governance/data_classification_policy.md` | Retention and disposal schedules define deletion timelines by classification tier |
| Right to restriction of processing | Art. 18 | `policies/01-governance/data_classification_policy.md` | Classification and data-flow documentation enables targeted processing restrictions |
| Right to data portability | Art. 20 | `policies/01-governance/data_classification_policy.md` | Data cataloguing and classification supports structured portability responses |
| Right to object | Art. 21 | `policies/01-governance/data_classification_policy.md` | Classification framework identifies processing activities subject to objection rights |
| Rights related to automated decision-making | Art. 22 | `policies/01-governance/ai_usage_governance_policy.md` | AI governance policy requires human oversight and safeguards against purely automated decisions with significant effect |

---

## Chapter IV — Controller and Processor Obligations

### Article 24 — Responsibility of the Controller

*Controllers must implement appropriate technical and organizational measures and be able to demonstrate compliance.*

| Policy File | Article 24 Requirement Satisfied |
|-------------|----------------------------------|
| `policies/01-governance/data_classification_policy.md` | Technical and organizational data protection measures documented and enforced |
| `policies/01-governance/change_management_policy.md` | Change management creates an audit trail demonstrating controls are maintained over time |
| `policies/01-governance/vendor_third_party_risk_policy.md` | Controller accountability extended to processor oversight and contractual controls |

---

### Article 25 — Data Protection by Design and by Default

*Personal data protection must be integrated into processing systems from the design stage, and only data necessary for the specified purpose must be processed by default.*

| Policy File | Article 25 Requirement Satisfied |
|-------------|----------------------------------|
| `policies/05-infrastructure/cloud_security_policy.md` | Security and privacy requirements embedded in cloud architecture selection and procurement |
| `policies/01-governance/change_management_policy.md` | Privacy and security review gates in the change approval process (privacy-by-design) |
| `policies/05-infrastructure/vulnerability_patch_management_policy.md` | Security maintenance embedded in system lifecycle (not bolted on after deployment) |
| `policies/01-governance/ai_usage_governance_policy.md` | AI systems required to implement data minimisation and default-off data collection |

---

### Article 28 — Processor Contracts (DPA Requirement)

*Controllers must only use processors providing sufficient guarantees; processing must be governed by a binding contract (Data Processing Agreement).*

| Policy File | Article 28 Requirement Satisfied |
|-------------|----------------------------------|
| `policies/01-governance/vendor_third_party_risk_policy.md` | Mandatory DPA requirements, security standards, audit rights, and sub-processor approval clauses for all vendors processing personal data |
| `policies/05-infrastructure/cloud_security_policy.md` | Cloud provider DPA and security addendum requirements as part of cloud procurement |

---

### Article 30 — Records of Processing Activities (RoPA)

*Controllers and processors must maintain a written record of processing activities, including purposes, categories of data and data subjects, recipients, and retention periods.*

| Policy File | Article 30 Requirement Satisfied |
|-------------|----------------------------------|
| `policies/01-governance/data_classification_policy.md` | Classification schema captures the categories of personal data, purposes, and retention periods required for the RoPA |
| `policies/01-governance/vendor_third_party_risk_policy.md` | Third-party data flows and processor inventory documented through vendor risk process, feeding the RoPA controller entries |

---

### Article 32 — Security of Processing

*Controllers and processors must implement appropriate technical and organizational security measures, taking into account the state of the art, costs, and the risk to data subjects.*

| Policy File | Article 32 Requirement Satisfied |
|-------------|----------------------------------|
| `policies/02-access-control/password_protection_policy.md` | Pseudonymisation and access controls (Art. 32(1)(a)–(b)) |
| `policies/02-access-control/remote_work_byod_policy.md` | Security measures for remote and endpoint personal data access |
| `policies/02-access-control/clean_desk_policy.md` | Physical security measures for personal data handling in workspaces |
| `policies/03-communications/email_policy.md` | Measures protecting personal data in electronic communications |
| `policies/05-infrastructure/server_security_policy.md` | Confidentiality, integrity, availability and resilience of processing systems (Art. 32(1)(b)) |
| `policies/05-infrastructure/cloud_security_policy.md` | Cloud workload security measures and encryption for personal data |
| `policies/05-infrastructure/wireless_communication_policy.md` | Network security for wireless personal data transmission |
| `policies/05-infrastructure/vulnerability_patch_management_policy.md` | Ongoing measures to ensure continued confidentiality and to address vulnerabilities |
| `policies/06-continuity/disaster_recovery_plan_policy.md` | Ability to restore availability and access to personal data in a timely manner after an incident (Art. 32(1)(c)) |

---

### Article 33 — Notification of a Personal Data Breach to the Supervisory Authority

*The controller must notify the competent supervisory authority within **72 hours** of becoming aware of a personal data breach, unless the breach is unlikely to result in a risk to the rights and freedoms of natural persons.*

| Policy File | Article 33 Requirement Satisfied |
|-------------|----------------------------------|
| `policies/04-incident-response/data_breach_response_policy.md` | Breach detection, severity assessment, and 72-hour supervisory authority notification procedure |
| `policies/04-incident-response/security_response_plan_policy.md` | Incident escalation pathway to enable timely breach assessment and regulatory notification |

> **Practical note:** The 72-hour clock starts from the point the controller *becomes aware* (Art. 33(1)). Your Data Breach Response Policy must define the internal escalation path that ensures decision-makers are notified quickly enough to meet this deadline. Processors must notify the controller *without undue delay* under Art. 33(2) — ensure this obligation is included in your vendor DPA clauses (see Art. 28 above).

---

### Article 34 — Communication of a Personal Data Breach to the Data Subject

*When a breach is likely to result in a high risk to individuals, the controller must inform affected data subjects without undue delay.*

| Policy File | Article 34 Requirement Satisfied |
|-------------|----------------------------------|
| `policies/04-incident-response/data_breach_response_policy.md` | Data subject notification procedures, content requirements, and communication channels |
| `policies/03-communications/email_policy.md` | Secure communication channel controls for breach notification communications |

---

### Article 35 — Data Protection Impact Assessment (DPIA)

*A DPIA is mandatory before processing likely to result in high risk to individuals (large-scale processing of sensitive data, systematic profiling, monitoring of public areas, etc.).*

| Policy File | Article 35 Requirement Satisfied |
|-------------|----------------------------------|
| `policies/01-governance/data_classification_policy.md` | Risk-based classification framework identifies processing activities likely to require a DPIA |
| `policies/01-governance/ai_usage_governance_policy.md` | AI risk assessment requirements align with DPIA triggers for profiling and automated decision-making |
| `policies/01-governance/vendor_third_party_risk_policy.md` | Vendor risk assessment process incorporates DPIA trigger evaluation for third-party processing |
| `policies/01-governance/change_management_policy.md` | Change approval gates require privacy impact review for changes affecting personal data systems |

---

### Article 37 — Designation of a Data Protection Officer (DPO)

*A DPO is mandatory for public authorities, organisations carrying out large-scale systematic monitoring, and organisations processing special-category data at scale.*

| Policy File | Article 37 Requirement Satisfied |
|-------------|----------------------------------|
| `policies/04-incident-response/security_response_plan_policy.md` | Incident escalation hierarchy documents the privacy/DPO contact role for breach response |
| `policies/01-governance/data_classification_policy.md` | Classification framework supports the DPO's monitoring function by documenting data flows and risks |

---

## Chapter V — International Data Transfers (Articles 44–49)

*Transfers of personal data to third countries are only permitted where an adequacy decision, appropriate safeguards (e.g., Standard Contractual Clauses — SCCs), or a specific derogation applies.*

| Mechanism | Policy File | How It Satisfies |
|-----------|-------------|------------------|
| Adequacy / SCCs / Binding Corporate Rules | `policies/01-governance/vendor_third_party_risk_policy.md` | Third-party contracts require lawful transfer mechanisms and documentation of the applicable basis |
| Security standards for transferred data | `policies/05-infrastructure/cloud_security_policy.md` | Cloud security policy specifies encryption and access controls for data transferred to cloud providers in third countries |

---

## Article 83 — Administrative Fines

*GDPR fines can reach €20,000,000 or 4 % of global annual turnover (whichever is higher) for infringement of the core principles, data subject rights, or international transfer rules.*

The policies above collectively reduce the risk of the most common fine triggers:

| Risk Category | Key Mitigating Policies |
|---------------|-------------------------|
| Insufficient legal basis | `data_classification_policy.md`, `acceptable_use_policy.md` |
| Failure to implement adequate security | `server_security_policy.md`, `password_protection_policy.md`, `vulnerability_patch_management_policy.md` |
| Failure to notify breach within 72 hours | `data_breach_response_policy.md`, `security_response_plan_policy.md` |
| Unlawful international transfers | `vendor_third_party_risk_policy.md`, `cloud_security_policy.md` |
| Non-cooperation with supervisory authority | `data_breach_response_policy.md` |

---

## GDPR Compliance Gap Checklist

These policy documents establish **documented controls** for GDPR. To achieve full compliance readiness you will additionally need:

1. **Records of Processing Activities (RoPA)** — Art. 30 requires a written inventory; the policies support it but do not replace the inventory itself.
2. **Data Processing Agreements (DPAs)** — Signed DPAs with every processor (cloud providers, SaaS tools, IT suppliers). See `vendor_third_party_risk_policy.md`.
3. **Privacy Notices** — Data subjects must be informed at collection (Arts. 13–14); these are not covered by internal security policies.
4. **Data Subject Request procedure** — Operational workflow to receive, verify, and respond to DSARs within one month (Art. 12(3)).
5. **DPIA register** — Documented DPIAs for high-risk processing activities identified through your classification framework.
6. **DPO appointment** (where mandatory) — Check Art. 37 criteria; even where not mandatory, a named privacy contact is recommended.
7. **Transfer impact assessments** — Required when using SCCs post-Schrems II for transfers to countries without adequacy decisions.

---

## Related Resources

- [ISO 27001 Mappings](./iso-27001.md)
- [NIST CSF Mappings](./nist-csf.md)
- [SOC 2 Mappings](./soc2.md)
- [LGPD Mappings](./lgpd.md) — Brazil's equivalent data protection regulation, closely modelled on GDPR
- [Enterprise Readiness Checklist](../docs/enterprise-readiness-checklist.md)
- [HailBytes Enterprise Trust Package](https://hailbytes.com/enterprise?utm_source=github&utm_medium=mapping&utm_campaign=enterprise-trust)
