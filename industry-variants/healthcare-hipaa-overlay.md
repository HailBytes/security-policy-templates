# Healthcare / HIPAA Industry Overlay

**Applies to:** Organizations subject to the Health Insurance Portability and Accountability Act (HIPAA) — covered entities and business associates handling Protected Health Information (PHI).

> **How to use this overlay:** This document describes additions and modifications to make when applying the base security policy templates to a healthcare organization. Read each section alongside the corresponding base policy. Where this overlay conflicts with a base policy, the overlay takes precedence for healthcare organizations. Always obtain legal review from healthcare compliance counsel before finalizing policies.

---

## Who Needs This Overlay

- Hospitals, clinics, and physician practices
- Health plans and insurers
- Healthcare clearinghouses
- Business associates with access to PHI (billing companies, EHR vendors, MSPs)
- Telehealth and digital health platforms

---

## Definitions

| Term | Meaning |
|------|---------|
| **PHI** | Protected Health Information — individually identifiable health information in any form |
| **ePHI** | Electronic PHI — PHI in electronic format |
| **Covered Entity (CE)** | Healthcare providers, health plans, and clearinghouses subject to HIPAA |
| **Business Associate (BA)** | Third parties that create, receive, maintain, or transmit PHI on behalf of a CE |
| **BAA** | Business Associate Agreement — required contract between CE and BA |
| **Minimum Necessary** | HIPAA principle: access/disclosure of PHI limited to the minimum needed for the purpose |

---

## HIPAA-Specific Additions by Policy Area

### 1. Governance (Acceptable Use / Ethics Policy)

**Add the following requirements:**
- Designate a **HIPAA Privacy Officer** and **HIPAA Security Officer** (may be the same person for small organizations); document roles and responsibilities
- Maintain a **current HIPAA Risk Analysis** — required by 45 CFR §164.308(a)(1); must be reviewed annually and after significant operational changes
- Implement a **HIPAA Sanction Policy** — document specific sanctions for workforce members who violate HIPAA; sanctions must be applied consistently
- Maintain a **HIPAA Policies and Procedures** document set; retain for 6 years from creation date or last effective date, whichever is later
- Workforce members must be trained on HIPAA Privacy and Security Rules within 60 days of hire and annually thereafter; training must be documented with attestation

### 2. Access Control (Password / Remote Work / BYOD)

**Add the following requirements:**
- Implement the **Minimum Necessary standard** — access to ePHI must be restricted to the minimum information needed for the workforce member's role (45 CFR §164.514(d))
- Maintain **Access Control Lists** documenting who has access to each ePHI system; review at least quarterly
- **Automatic logoff** is required for workstations accessing ePHI — maximum 15 minutes of inactivity (required addressable specification)
- **Unique user identification** required — no sharing of login credentials for systems containing ePHI (45 CFR §164.312(a)(2)(i))
- **Emergency access procedure** required — document how ePHI can be accessed during system failures or emergencies (45 CFR §164.312(a)(2)(ii))
- Remote access to ePHI must use encrypted VPN; unencrypted remote access to ePHI is prohibited
- BYOD devices used to access ePHI must have MDM enrolled; capability to remote wipe ePHI is required

### 3. Data Classification

**Map PHI to the highest classification tier:**
- All PHI and ePHI must be classified as **Restricted** regardless of the general sensitivity of the health information
- De-identified data (meeting HIPAA Safe Harbor or Expert Determination standards) may be reclassified to Internal or Public
- Retention of PHI: minimum **6 years** from creation date or last effective date for HIPAA records; medical records retention varies by state law (often 7–10 years; check applicable state law)
- **De-identification** before disposal of ePHI is not sufficient — certified destruction is required

### 4. Communications / Email

**Add the following requirements:**
- ePHI must not be transmitted via unencrypted email — use encrypted email or a secure patient messaging portal
- Patient authorization (or applicable exception) is required before communicating PHI via email, text, or fax
- Fax transmissions of PHI must include a confidentiality notice and be verified recipient before sending
- Maintain a **Communications Log** for disclosures of PHI outside treatment, payment, and operations (45 CFR §164.528)

### 5. Incident Response / Data Breach

**Replace or supplement breach notification timelines:**
- **HIPAA Breach Notification Rule (45 CFR §164.400–414):**
  - Notify affected individuals: **within 60 days** of breach discovery
  - Notify HHS Secretary: within 60 days of year-end for breaches affecting fewer than 500 individuals (annual log); **within 60 days of discovery** for breaches of 500+ individuals
  - Notify prominent media outlets in affected state/jurisdiction for breaches affecting 500+ individuals in that jurisdiction: within 60 days
- **Breach assessment** — document the 4-factor risk assessment to determine if an incident qualifies as a reportable breach:
  1. Nature and extent of PHI involved
  2. Who used or received the PHI
  3. Whether PHI was actually acquired or viewed
  4. Extent to which risk has been mitigated
- Maintain a **Breach Log** for all PHI incidents regardless of whether reportable
- Business Associate breaches: BAs must notify the Covered Entity **without unreasonable delay** and within 60 days of discovery

### 6. Infrastructure / Server / Cloud Security

**Add the following requirements:**
- **Audit controls** required: implement hardware, software, or procedural mechanisms to record and examine access to ePHI systems (45 CFR §164.312(b)) — audit logs must cover all access to ePHI
- ePHI audit logs must be retained for **6 years**
- **Integrity controls** required: implement mechanisms to authenticate ePHI and detect unauthorized alteration (45 CFR §164.312(c))
- **Transmission security** required: encrypt ePHI in transit; TLS 1.2+ required for all ePHI transmissions
- Cloud storage of ePHI requires a signed **Business Associate Agreement (BAA)** with the cloud provider before any ePHI is stored — storing ePHI in a cloud service without a BAA is a HIPAA violation
- Verify that cloud providers offer a BAA (major providers — AWS, Azure, GCP, Microsoft 365 — offer these) before storing ePHI

### 7. Vendor / Third-Party Risk

**Add the following requirements:**
- A signed **Business Associate Agreement (BAA)** is legally required before sharing ePHI with any vendor, contractor, or service provider — no exceptions (45 CFR §164.308(b))
- BAA must include: permitted uses and disclosures of PHI, safeguards required, breach reporting requirements, sub-contractor requirements, and return/destruction of PHI at termination
- Maintain a **BA Register** — list all business associates and BAA execution dates; review annually
- Subcontractors of Business Associates who access ePHI must also have BAAs in place
- Upon contract termination, BAs must return or destroy all PHI; if destruction not feasible, protections must continue

### 8. Disaster Recovery / Business Continuity

**Add the following requirements:**
- HIPAA requires a formal **Contingency Plan** (45 CFR §164.308(a)(7)) covering:
  - Data backup plan for ePHI
  - Disaster recovery plan
  - Emergency mode operation plan
  - Testing and revision procedures
  - Applications and data criticality analysis
- Contingency plan must be tested at least annually
- Backup of ePHI must be encrypted and tested for restoration quarterly
- Document and test procedures for operating under emergency conditions while maintaining minimum ePHI access

---

## HIPAA Compliance Checklist Additions

- [ ] HIPAA Risk Analysis completed and current (within 12 months)
- [ ] HIPAA Privacy Officer designated and documented
- [ ] HIPAA Security Officer designated and documented
- [ ] All workforce members trained on HIPAA within 60 days of hire
- [ ] Annual HIPAA training completed and documented for all workforce
- [ ] HIPAA Sanction Policy documented and communicated
- [ ] BAA register maintained and all active BAAs current
- [ ] PHI access log/audit controls enabled on all ePHI systems
- [ ] Breach notification procedures tested annually
- [ ] HIPAA Risk Analysis reviewed after significant operational changes

---

## Key HIPAA References

| Rule | Citation | Topic |
|------|----------|-------|
| Privacy Rule | 45 CFR Part 164, Subparts A and E | PHI use and disclosure |
| Security Rule | 45 CFR Part 164, Subparts A and C | ePHI safeguards |
| Breach Notification Rule | 45 CFR Part 164, Subparts A and D | Breach reporting |
| Enforcement Rule | 45 CFR Part 160, Subparts C-E | Penalties and enforcement |

Penalty tiers range from $100 to $50,000 per violation (up to $1.9M per violation category per year) depending on culpability. Willful neglect penalties start at $10,000 per violation.

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Security Officer] | Initial release |
