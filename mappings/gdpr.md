# GDPR (General Data Protection Regulation) Mappings

This file maps each policy template to the relevant provisions of the EU **General Data Protection Regulation** (Regulation (EU) 2016/679, GDPR), which applies to any organization that processes personal data of individuals in the European Economic Area (EEA), regardless of where the organization is based.

These mappings support enterprise deals involving EU data subjects, regulatory filings with EEA supervisory authorities (e.g., the ICO, CNIL, BfDI), and vendor security questionnaires from EU-headquartered customers.

> **Disclaimer:** This mapping is intended to assist compliance practitioners and should not substitute for legal advice. GDPR enforcement is led by national supervisory authorities under the European Data Protection Board (EDPB). Consult qualified EU data protection counsel for formal compliance determinations.

---

## Article 5 — Principles of Personal Data Processing

Art. 5 establishes 7 foundational principles that apply to all personal data processing activities.

| Principle | Policy File | How It Satisfies |
|-----------|-------------|------------------|
| **Lawfulness, fairness, transparency** (Art. 5(1)(a)) | `policies/01-governance/acceptable_use_policy.md` | Documents lawful basis and transparency obligations for employee data monitoring |
| **Purpose limitation** (Art. 5(1)(b)) | `policies/01-governance/data_classification_policy.md` | Classification schema requires documented purpose for each data category |
| **Data minimisation** (Art. 5(1)(c)) | `policies/01-governance/ai_usage_governance_policy.md` | Restricts input of personal data to AI systems to the minimum necessary |
| **Data minimisation** (Art. 5(1)(c)) | `policies/01-governance/data_classification_policy.md` | Collection limited to data required for the stated processing purpose |
| **Accuracy** (Art. 5(1)(d)) | `policies/01-governance/data_classification_policy.md` | Data quality and accuracy maintenance requirements per classification tier |
| **Storage limitation** (Art. 5(1)(e)) | `policies/01-governance/data_classification_policy.md` | Retention schedules and disposal requirements by data classification |
| **Integrity and confidentiality** (Art. 5(1)(f)) | `policies/02-access-control/password_protection_policy.md` | Technical access controls protecting personal data confidentiality |
| **Integrity and confidentiality** (Art. 5(1)(f)) | `policies/05-infrastructure/server_security_policy.md` | Infrastructure security ensuring integrity of systems processing personal data |
| **Accountability** (Art. 5(2)) | `policies/01-governance/vendor_third_party_risk_policy.md` | Controller accountability for third-party processor arrangements |
| **Accountability** (Art. 5(2)) | `policies/01-governance/change_management_policy.md` | Documented controls demonstrating ongoing compliance |

---

## Article 6 — Lawfulness of Processing

Art. 6 requires that every processing activity has a documented legal basis.

| Legal Basis | Policy File | How It Satisfies |
|-------------|-------------|------------------|
| Art. 6(1)(a) — Consent | `policies/01-governance/data_classification_policy.md` | Consent documentation requirements in data handling procedures |
| Art. 6(1)(b) — Contract performance | `policies/01-governance/acceptable_use_policy.md` | Processing of employee data for HR and IT management contracts |
| Art. 6(1)(c) — Legal obligation | `policies/04-incident-response/data_breach_response_policy.md` | Processing necessary to comply with GDPR breach notification obligation |
| Art. 6(1)(f) — Legitimate interests | `policies/01-governance/acceptable_use_policy.md` | Legitimate-interests basis documented for IT-resource monitoring |
| Art. 6(1)(f) — Legitimate interests | `policies/05-infrastructure/server_security_policy.md` | Security logging and monitoring under legitimate interests basis |

---

## Article 9 — Special Categories of Personal Data

Art. 9 prohibits processing of sensitive personal data (health, biometric, racial/ethnic origin, etc.) without explicit consent or a specific legal exception.

| Policy File | How It Satisfies |
|-------------|------------------|
| `policies/01-governance/data_classification_policy.md` | Restricted classification tier covers special-category data with enhanced handling controls |
| `policies/01-governance/acceptable_use_policy.md` | Prohibits processing of special-category data outside approved systems |
| `policies/02-access-control/password_protection_policy.md` | Elevated access controls required for systems processing special-category data |

---

## Articles 12–22 — Data Subject Rights

GDPR grants eight core rights to individuals; the policies below provide supporting governance to operationalize them.

| Right | Article | Policy File | Supporting Governance |
|-------|---------|-------------|----------------------|
| Transparent information | Art. 12–13 | `policies/01-governance/data_classification_policy.md` | Classification enables identification of what data is held and for what purpose |
| Right of access | Art. 15 | `policies/01-governance/data_classification_policy.md` | Data catalog supports identification and retrieval of personal data per request |
| Right to rectification | Art. 16 | `policies/01-governance/data_classification_policy.md` | Data accuracy requirements and update procedures by classification tier |
| Right to erasure ("right to be forgotten") | Art. 17 | `policies/01-governance/data_classification_policy.md` | Data retention and disposal schedules enable erasure on request |
| Right to restriction of processing | Art. 18 | `policies/02-access-control/password_protection_policy.md` | Access controls enable restriction of processing for flagged records |
| Right to data portability | Art. 20 | `policies/01-governance/data_classification_policy.md` | Data cataloging and structured formats support portability responses |
| Right to object | Art. 21 | `policies/01-governance/acceptable_use_policy.md` | Procedures for halting legitimate-interest processing on objection |
| Rights re. automated decision-making | Art. 22 | `policies/01-governance/ai_usage_governance_policy.md` | Restrictions on automated profiling; human review requirements |

---

## Article 24 — Responsibility of the Controller

*The controller shall implement appropriate technical and organisational measures to ensure and be able to demonstrate that processing is performed in accordance with this Regulation.*

| Policy File | Requirement Satisfied |
|-------------|----------------------|
| `policies/01-governance/data_classification_policy.md` | Documented data governance demonstrating controller accountability |
| `policies/01-governance/change_management_policy.md` | Controlled change process maintaining compliance through system modifications |
| `policies/01-governance/vendor_third_party_risk_policy.md` | Oversight of processors with documented due diligence |
| `policies/05-infrastructure/vulnerability_patch_management_policy.md` | Ongoing technical measures demonstrating active compliance maintenance |

---

## Article 25 — Data Protection by Design and by Default

*The controller shall implement data-protection principles in an integrated manner in the design of processing systems and practices.*

| Policy File | Requirement Satisfied |
|-------------|----------------------|
| `policies/05-infrastructure/cloud_security_policy.md` | Security and privacy requirements embedded in cloud architecture and procurement |
| `policies/01-governance/change_management_policy.md` | Privacy and security review gates in the change approval process |
| `policies/05-infrastructure/vulnerability_patch_management_policy.md` | Ongoing security maintenance as part of system lifecycle (privacy by default) |
| `policies/01-governance/ai_usage_governance_policy.md` | Privacy-by-design requirements for AI system selection and configuration |
| `policies/01-governance/data_classification_policy.md` | Default data minimisation and retention requirements built into classification |

---

## Article 28 — Processor Obligations (Data Processing Agreements)

*Processing by a processor shall be governed by a contract or legal act under Union or Member State law that sets out the subject-matter and duration of processing, the nature and purpose of the processing, the type of personal data and categories of data subjects, and the obligations and rights of the controller.*

| Policy File | Requirement Satisfied |
|-------------|----------------------|
| `policies/01-governance/vendor_third_party_risk_policy.md` | DPA requirements in third-party contracts; processor vetting and oversight |
| `policies/05-infrastructure/cloud_security_policy.md` | Cloud provider Art. 28 compliance assessment and DPA execution requirements |

---

## Article 30 — Records of Processing Activities (RoPA)

*Each controller shall maintain a record of processing activities under its responsibility containing: name and contact details, purposes of processing, description of categories of data subjects and personal data, recipients, transfers, retention periods, and security measures.*

| Policy File | Requirement Satisfied |
|-------------|----------------------|
| `policies/01-governance/data_classification_policy.md` | Data inventory and classification schema provides the foundation for a RoPA |
| `policies/01-governance/vendor_third_party_risk_policy.md` | Third-party data flows and recipients documented through vendor risk process |
| `policies/01-governance/ai_usage_governance_policy.md` | AI-system data processing cataloged with purpose, inputs, and data subjects |

---

## Article 32 — Security of Processing

*The controller and the processor shall implement appropriate technical and organisational measures to ensure a level of security appropriate to the risk, including pseudonymisation and encryption, ability to ensure ongoing confidentiality/integrity/availability, and processes for testing.*

### Technical Measures

| Policy File | Security Requirement Satisfied |
|-------------|-------------------------------|
| `policies/02-access-control/password_protection_policy.md` | Authentication, access control, and MFA for systems processing personal data |
| `policies/05-infrastructure/server_security_policy.md` | Infrastructure hardening; encryption at rest and in transit |
| `policies/05-infrastructure/cloud_security_policy.md` | Cloud encryption controls and shared-responsibility security boundaries |
| `policies/05-infrastructure/wireless_communication_policy.md` | Network security measures for wireless transmission of personal data |
| `policies/02-access-control/remote_work_byod_policy.md` | Security measures for remote personal data access (VPN, device encryption) |
| `policies/05-infrastructure/vulnerability_patch_management_policy.md` | Ongoing vulnerability management to maintain security of processing systems |

### Organisational Measures

| Policy File | Security Requirement Satisfied |
|-------------|-------------------------------|
| `policies/01-governance/acceptable_use_policy.md` | Organisational controls and acceptable-use rules for personal data systems |
| `policies/02-access-control/clean_desk_policy.md` | Physical security controls for personal data handling in the workplace |
| `policies/03-communications/email_policy.md` | Controls protecting personal data in electronic communications |
| `policies/01-governance/vendor_third_party_risk_policy.md` | Contractual and organisational controls for sub-processors (Art. 28 chain) |
| `policies/01-governance/change_management_policy.md` | Process controls preventing inadvertent exposure through system changes |

### Testing and Evaluation

| Policy File | Security Requirement Satisfied |
|-------------|-------------------------------|
| `policies/05-infrastructure/vulnerability_patch_management_policy.md` | Regular testing and evaluation of effectiveness of security measures |
| `policies/06-continuity/disaster_recovery_plan_policy.md` | Ability to restore availability and access to personal data after incidents |

---

## Article 33 — Notification of a Personal Data Breach to the Supervisory Authority

*In the case of a personal data breach, the controller shall without undue delay — and, where feasible, not later than **72 hours** after having become aware of it — notify the competent supervisory authority.*

| Policy File | Requirement Satisfied |
|-------------|----------------------|
| `policies/04-incident-response/data_breach_response_policy.md` | Breach detection, severity assessment, and 72-hour supervisory authority notification workflow |
| `policies/04-incident-response/security_response_plan_policy.md` | Incident escalation and triage procedures enabling timely detection and regulatory notification |

> **Note on the 72-hour clock:** The clock starts when the controller becomes "aware" of a breach — not when it is confirmed. Controllers should document the time of initial awareness and the timeline of investigation to demonstrate good-faith compliance with the notification window.

---

## Article 34 — Communication of a Personal Data Breach to the Data Subject

*When a breach is likely to result in a high risk to the rights and freedoms of natural persons, the controller shall communicate the breach to the data subject without undue delay.*

| Policy File | Requirement Satisfied |
|-------------|----------------------|
| `policies/04-incident-response/data_breach_response_policy.md` | High-risk breach communication procedures for notifying affected individuals |
| `policies/04-incident-response/security_response_plan_policy.md` | Severity classification enabling the Art. 34 "high risk" threshold assessment |

---

## Article 35 — Data Protection Impact Assessment (DPIA)

*A DPIA is required prior to processing that is likely to result in a high risk to individuals — in particular for systematic evaluation, large-scale processing of special categories, or systematic monitoring of publicly accessible areas.*

| Policy File | Requirement Satisfied |
|-------------|----------------------|
| `policies/01-governance/ai_usage_governance_policy.md` | AI system adoption triggers a privacy risk assessment analogous to a DPIA |
| `policies/05-infrastructure/cloud_security_policy.md` | Cloud migration security assessments cover privacy risk evaluation |
| `policies/01-governance/change_management_policy.md` | Change risk assessment process provides the mechanism to trigger DPIAs for high-risk changes |
| `policies/01-governance/data_classification_policy.md` | Classification of personal data tiers enables identification of DPIA-triggering processing activities |

---

## Articles 37–39 — Data Protection Officer (DPO)

*Certain controllers and processors must designate a DPO (mandatory for public authorities, systematic large-scale monitoring, or large-scale processing of special categories). The DPO must be given resources, access, and independence.*

| Policy File | Requirement Satisfied |
|-------------|----------------------|
| `policies/01-governance/data_classification_policy.md` | Data governance owner roles provide the organisational basis for a DPO appointment |
| `policies/04-incident-response/data_breach_response_policy.md` | DPO notification and involvement procedures in the breach response workflow |
| `policies/01-governance/ethics_policy.md` | DPO independence and non-penalisation for performing duties |

> **SMB Guidance:** Most SMBs are not required to appoint a DPO unless they engage in large-scale systematic monitoring (e.g., CCTV across public spaces) or process special-category data at scale. However, voluntarily designating a privacy lead — even part-time — demonstrates accountability under Art. 24. Update the `[IT Security Contact]` placeholder in your policies to reflect this role.

---

## Articles 44–49 — International Transfers of Personal Data

*Transfers of personal data to third countries (outside the EEA) are only lawful where the destination country offers an adequate level of protection or where appropriate safeguards exist.*

| Transfer Mechanism | Policy File | How It Satisfies |
|--------------------|-------------|------------------|
| Adequacy decisions (Art. 45) | `policies/01-governance/vendor_third_party_risk_policy.md` | Vendor risk assessment verifies destination country adequacy status |
| Standard Contractual Clauses / SCCs (Art. 46(2)(c)) | `policies/01-governance/vendor_third_party_risk_policy.md` | SCC execution requirements in third-party contracts for non-adequate countries |
| Binding Corporate Rules / BCRs (Art. 47) | `policies/01-governance/vendor_third_party_risk_policy.md` | BCR verification for intra-group transfers |
| Cloud transfers (Art. 46) | `policies/05-infrastructure/cloud_security_policy.md` | Cloud provider data residency and transfer mechanism verification |

> **Note on EU–US Transfers:** The EU–U.S. Data Privacy Framework (DPF), adopted July 2023, currently provides an adequacy basis for transfers to DPF-certified U.S. organizations. Verify your U.S. vendors' DPF certification status at [dataprivacyframework.gov](https://www.dataprivacyframework.gov) as part of your vendor risk review process. If certification lapses, fall back to SCCs.

---

## GDPR Fines Overview — Article 83

Organizations should be aware of the two-tier fine structure when assessing GDPR compliance investment:

| Tier | Maximum Fine | Example Violations |
|------|-------------|-------------------|
| **Lower tier** (Art. 83(4)) | €10 million or 2% of global annual turnover (whichever is higher) | Violations of Art. 25 (privacy by design), Art. 30 (RoPA), Art. 32 (security), Art. 33–34 (breach notification), Art. 37–39 (DPO) |
| **Upper tier** (Art. 83(5)) | €20 million or 4% of global annual turnover (whichever is higher) | Violations of Art. 5–9 (principles and lawfulness), Art. 12–22 (data subject rights), Art. 44–49 (international transfers) |

---

## GDPR Audit Readiness Notes

These policy documents establish **design evidence** for the GDPR requirements above. For a defensible compliance position, you will additionally need:

1. **Records of Processing Activities (RoPA)** — a live inventory of all processing activities per Art. 30
2. **Data Processing Agreements (DPAs)** — signed Art. 28 agreements with all processors
3. **Privacy Notices** — Art. 13/14 notices for all data collection points (website, HR, customer contracts)
4. **DPIA documentation** — for any high-risk processing activities identified via change management
5. **Breach response logs** — documented evidence of breach awareness timestamps and notification timelines
6. **Training records** — completion records for staff data protection training

See the [Enterprise Readiness Checklist](../docs/enterprise-readiness-checklist.md) for the broader compliance evidence gap list.

---

## Related Resources

- [ISO 27001 Mappings](./iso-27001.md)
- [NIST CSF Mappings](./nist-csf.md)
- [SOC 2 Mappings](./soc2.md)
- [LGPD Mappings](./lgpd.md) — Brazilian data protection law with similar principles to GDPR
- [HIPAA Mappings](./hipaa.md)
- [CIS Controls v8 Mappings](./cis-controls.md)
- [Enterprise Readiness Checklist](../docs/enterprise-readiness-checklist.md)
