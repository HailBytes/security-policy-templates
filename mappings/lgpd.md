# LGPD (Lei Geral de Proteção de Dados) Mappings

This file maps each policy template to the relevant provisions of Brazil's **Lei Geral de Proteção de Dados Pessoais** (Law No. 13,709/2018, LGPD) and, where applicable, to **BACEN Resolution 4,893/2021** (cybersecurity requirements for financial institutions regulated by the Brazilian Central Bank).

These mappings support enterprise deals involving Brazilian data subjects, ANPD compliance filings, and financial-sector vendor security questionnaires (relevant to IBM Brazil, banking, fintech, and healthcare clients).

> **Disclaimer:** This mapping is intended to assist compliance practitioners and should not substitute for legal advice. LGPD enforcement is led by the **Autoridade Nacional de Proteção de Dados (ANPD)**. Consult qualified Brazilian legal counsel for formal compliance determinations.

---

## LGPD Core Principles — Article 6

Art. 6 establishes 10 principles that apply to all personal data processing activities.

| Principle | Policy File | How It Satisfies |
|-----------|-------------|------------------|
| **Finalidade** (Purpose limitation — Art. 6 I) | `policies/01-governance/data_classification_policy.md` | Classification schema requires documented purpose for each data category |
| **Adequação** (Adequacy — Art. 6 II) | `policies/01-governance/data_classification_policy.md` | Data use must align with declared classification and purpose |
| **Necessidade** (Necessity/data minimization — Art. 6 III) | `policies/01-governance/ai_usage_governance_policy.md` | Restricts input of personal data to AI systems to what is necessary |
| **Livre acesso** (Free access — Art. 6 IV) | `policies/01-governance/data_classification_policy.md` | Data subject rights procedures reference classification tiers |
| **Qualidade dos dados** (Data quality — Art. 6 V) | `policies/01-governance/data_classification_policy.md` | Data accuracy and update requirements |
| **Transparência** (Transparency — Art. 6 VI) | `policies/01-governance/ethics_policy.md` | Transparency obligations for organizational data practices |
| **Segurança** (Security — Art. 6 VII) | `policies/02-access-control/password_protection_policy.md` | Technical security measures for personal data access |
| **Segurança** (Art. 6 VII) | `policies/05-infrastructure/server_security_policy.md` | Infrastructure security measures protecting personal data |
| **Prevenção** (Prevention — Art. 6 VIII) | `policies/05-infrastructure/vulnerability_patch_management_policy.md` | Proactive vulnerability management to prevent data incidents |
| **Não discriminação** (Non-discrimination — Art. 6 IX) | `policies/01-governance/ethics_policy.md` | Non-discriminatory data use principles |
| **Responsabilização** (Accountability — Art. 6 X) | `policies/01-governance/vendor_third_party_risk_policy.md` | Operator accountability for sub-processor arrangements |

---

## LGPD Legal Bases — Article 7

| Legal Basis | Policy File | How It Satisfies |
|-------------|-------------|------------------|
| Art. 7 II — Legitimate interests | `policies/01-governance/acceptable_use_policy.md` | Documents legitimate interests for monitoring IT resources |
| Art. 7 IX — Legitimate interests of controller | `policies/01-governance/data_classification_policy.md` | Basis documentation for each data processing category |

---

## LGPD Security Obligations — Articles 46–49

These articles impose the most direct technical and organizational security requirements under LGPD.

### Article 46 — Security Measures
*Controllers and operators must adopt security, technical, and administrative measures to protect personal data from unauthorized access and accidental or unlawful destruction, loss, alteration, communication, or any improper or unlawful treatment.*

| Policy File | Article 46 Requirement Satisfied |
|-------------|----------------------------------|
| `policies/02-access-control/password_protection_policy.md` | Technical access control measures |
| `policies/02-access-control/clean_desk_policy.md` | Physical security measures for personal data handling |
| `policies/02-access-control/remote_work_byod_policy.md` | Security measures for remote personal data access |
| `policies/03-communications/email_policy.md` | Measures protecting personal data in electronic communications |
| `policies/05-infrastructure/server_security_policy.md` | Infrastructure security measures for systems processing personal data |
| `policies/05-infrastructure/cloud_security_policy.md` | Cloud security measures for personal data in hosted environments |
| `policies/05-infrastructure/wireless_communication_policy.md` | Network security measures for wireless personal data transmission |
| `policies/05-infrastructure/vulnerability_patch_management_policy.md` | Ongoing technical measures to prevent exploitation of known vulnerabilities |
| `policies/01-governance/data_classification_policy.md` | Administrative measures through data classification and handling rules |
| `policies/01-governance/vendor_third_party_risk_policy.md` | Contractual and administrative measures for sub-processors |
| `policies/01-governance/change_management_policy.md` | Process controls to prevent inadvertent personal data exposure through changes |

### Article 47 — Confidentiality Obligation
*Agents that access personal data in the processing chain must maintain confidentiality, even after the end of the processing.*

| Policy File | Article 47 Requirement Satisfied |
|-------------|----------------------------------|
| `policies/01-governance/ethics_policy.md` | Confidentiality obligations for staff handling personal data |
| `policies/01-governance/acceptable_use_policy.md` | Confidentiality requirements for IT systems containing personal data |
| `policies/01-governance/vendor_third_party_risk_policy.md` | Contractual confidentiality obligations for third-party processors |

### Article 48 — Security Incident Notification
*Controllers must notify the ANPD and data subjects of security incidents that may create risk or relevant harm to data subjects, within a reasonable timeframe.*

| Policy File | Article 48 Requirement Satisfied |
|-------------|----------------------------------|
| `policies/04-incident-response/data_breach_response_policy.md` | Breach detection, assessment, and ANPD notification procedures |
| `policies/04-incident-response/security_response_plan_policy.md` | Incident escalation to enable timely regulatory notification |

> **ANPD Guidance:** The ANPD Resolution CD/ANPD No. 15/2024 requires notification within **3 working days** of becoming aware of a high-risk incident. Update your Data Breach Response Policy placeholder timelines to reflect this.

### Article 49 — Security by Design
*Systems used for personal data processing must be designed from the ground up to meet security requirements and data protection standards.*

| Policy File | Article 49 Requirement Satisfied |
|-------------|----------------------------------|
| `policies/05-infrastructure/cloud_security_policy.md` | Security requirements embedded in cloud architecture and procurement |
| `policies/01-governance/change_management_policy.md` | Security review gates in the change approval process |
| `policies/05-infrastructure/vulnerability_patch_management_policy.md` | Ongoing security maintenance as part of system lifecycle |

---

## LGPD Data Subject Rights — Articles 17–22

These rights must be operationalized through internal procedures; the policies below provide supporting governance.

| Right | Policy File | Supporting Governance |
|-------|-------------|----------------------|
| Access (Art. 18 I) | `policies/01-governance/data_classification_policy.md` | Classification enables identification of where subject data is held |
| Correction (Art. 18 III) | `policies/01-governance/data_classification_policy.md` | Data quality requirements support correction obligations |
| Deletion (Art. 18 VI) | `policies/01-governance/data_classification_policy.md` | Data retention and disposal schedules by classification tier |
| Portability (Art. 18 V) | `policies/01-governance/data_classification_policy.md` | Data cataloging enables portability response |
| Information on sharing (Art. 18 VII) | `policies/01-governance/vendor_third_party_risk_policy.md` | Third-party data flows documented through vendor risk process |

---

## BACEN Resolution 4,893/2021 — Cybersecurity Requirements

BACEN 4,893/2021 applies to financial institutions, payment institutions, and other entities regulated by the Banco Central do Brasil. It requires a formal cybersecurity policy and minimum technical controls.

### Article 4 — Cybersecurity Policy Requirements
*The institution must maintain a cybersecurity policy covering action procedures and controls to reduce vulnerability to cyber incidents.*

| Policy File | Art. 4 Requirement Satisfied |
|-------------|------------------------------|
| `policies/01-governance/acceptable_use_policy.md` | Action procedures for acceptable IT use |
| `policies/02-access-control/password_protection_policy.md` | Access control measures reducing credential-based attack vectors |
| `policies/03-communications/email_policy.md` | Controls reducing phishing and social engineering vulnerabilities |
| `policies/05-infrastructure/server_security_policy.md` | Server hardening reducing infrastructure vulnerabilities |
| `policies/05-infrastructure/cloud_security_policy.md` | Cloud security controls and shared responsibility boundaries |
| `policies/02-access-control/remote_work_byod_policy.md` | Remote access controls reducing endpoint vulnerabilities |

### Article 5 — Minimum Security Actions
*Institutions must implement authentication, encryption, data prevention controls, vulnerability testing, and incident response.*

| Policy File | Art. 5 Requirement Satisfied |
|-------------|------------------------------|
| `policies/02-access-control/password_protection_policy.md` | Authentication controls (Art. 5 I) |
| `policies/01-governance/data_classification_policy.md` | Data encryption requirements by classification (Art. 5 II) |
| `policies/05-infrastructure/vulnerability_patch_management_policy.md` | Vulnerability testing and management (Art. 5 IV) |
| `policies/04-incident-response/security_response_plan_policy.md` | Incident response procedures (Art. 5 V) |
| `policies/01-governance/change_management_policy.md` | Controlled system changes (Art. 5 VI) |

### Article 6 — Business Continuity
*Institutions must maintain a business continuity plan for cyber incidents.*

| Policy File | Art. 6 Requirement Satisfied |
|-------------|------------------------------|
| `policies/06-continuity/disaster_recovery_plan_policy.md` | Cyber incident recovery procedures and RTO/RPO objectives |

### Article 7 — Third-Party Services (Cloud)
*Institutions must assess cybersecurity risks in contracted cloud services and data processing.*

| Policy File | Art. 7 Requirement Satisfied |
|-------------|------------------------------|
| `policies/01-governance/vendor_third_party_risk_policy.md` | Third-party cloud service risk assessment and contractual requirements |
| `policies/05-infrastructure/cloud_security_policy.md` | Cloud-specific security controls and provider assessment |

### Article 11 — Incident Reporting
*Incidents with potential systemic impact must be reported to BACEN within defined timeframes.*

| Policy File | Art. 11 Requirement Satisfied |
|-------------|-------------------------------|
| `policies/04-incident-response/data_breach_response_policy.md` | Regulatory notification procedures including BACEN reporting obligations |
| `policies/04-incident-response/security_response_plan_policy.md` | Incident severity classification enabling Art. 11 threshold assessment |

---

## LATAM Compliance Notes

For organizations operating across Latin America, note the following additional frameworks:

| Country | Framework | Key Similarity to LGPD |
|---------|-----------|------------------------|
| Argentina | Personal Data Protection Law (Law 25,326) + Draft Reform | Similar principles; stricter on cross-border transfer |
| Mexico | LFPDPPP (Federal Law on Protection of Personal Data) | Consent-first; ARCO rights analogous to LGPD Arts. 17-22 |
| Colombia | Law 1581/2012 (Habeas Data) | Authorization-based; SIC as supervisory authority |
| Chile | Law 19,628 + 2024 Reform (Law 21,719) | 2024 reform closely mirrors LGPD structure |

> **Full LATAM mapping matrix** → [HailBytes/latam-compliance-mappings](https://github.com/HailBytes/latam-compliance-mappings) *(coming soon)*

---

## Related Resources

- [ISO 27001 Mappings](./iso-27001.md)
- [NIST CSF Mappings](./nist-csf.md)
- [SOC 2 Mappings](./soc2.md)
- [Enterprise Readiness Checklist](../docs/enterprise-readiness-checklist.md)
- [HailBytes Enterprise Trust Package](https://hailbytes.com/enterprise?utm_source=github&utm_medium=mapping&utm_campaign=enterprise-trust)
