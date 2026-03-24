# Finance / PCI DSS & SOX Industry Overlay

**Applies to:** Organizations that process, store, or transmit payment card data (PCI DSS) and/or publicly traded companies or their subsidiaries subject to the Sarbanes-Oxley Act (SOX).

> **How to use this overlay:** Read each section alongside the corresponding base policy template. Where this overlay conflicts with a base policy, the overlay takes precedence. Engage your legal counsel and a qualified security assessor (QSA for PCI DSS) before finalizing policies.

---

## Who Needs This Overlay

**PCI DSS applies to:**
- Merchants accepting credit/debit card payments (any size)
- Payment processors and acquirers
- Point-of-sale (POS) system operators
- E-commerce businesses accepting cards online
- Any organization that stores, processes, or transmits cardholder data

**SOX applies to:**
- US publicly traded companies (SEC registrants)
- Subsidiaries and affiliates of public companies
- Companies preparing for IPO

---

## Definitions

| Term | Meaning |
|------|---------|
| **CHD** | Cardholder Data — PAN, cardholder name, expiration date, service code |
| **SAD** | Sensitive Authentication Data — CVV, PIN, full magnetic stripe data (never store after authorization) |
| **CDE** | Cardholder Data Environment — systems that store, process, or transmit CHD |
| **PAN** | Primary Account Number — the 16-digit card number |
| **QSA** | Qualified Security Assessor — PCI-certified assessor |
| **SAQ** | Self-Assessment Questionnaire — PCI compliance self-assessment |
| **ITGC** | IT General Controls — SOX controls over IT systems |
| **SOD** | Segregation of Duties — preventing a single person from completing high-risk tasks alone |

---

## PCI DSS Additions by Policy Area

PCI DSS v4.0 is organized into 12 requirements. Below are additions to base templates mapped to PCI requirements.

### 1. Governance (Acceptable Use / Ethics Policy)

**PCI DSS Req. 12 — Maintain an Information Security Policy:**
- Maintain a formal, documented security policy reviewed annually and after significant changes
- Assign a **PCI DSS Security Officer** responsible for ongoing compliance
- Document scope of the Cardholder Data Environment (CDE) — which systems are in scope
- Complete annual **PCI DSS Self-Assessment Questionnaire (SAQ)** or engage a QSA for Report on Compliance (ROC) depending on merchant level
- Maintain a **PCI compliance inventory** of all policies, procedures, and controls with owner assignments

### 2. Access Control (Password / Remote Work / BYOD)

**PCI DSS Req. 7 — Restrict Access to System Components by Business Need:**
- Access to CHD must be restricted to individuals whose job requires it — document all role-based access
- Access control lists must define minimum required access for each role in the CDE

**PCI DSS Req. 8 — Identify Users and Authenticate Access:**
- Unique IDs required for all users accessing CDE — shared credentials prohibited
- MFA required for all non-console administrative access to the CDE
- MFA required for all remote network access to the CDE
- Password minimum: 12 characters; complexity required; no reuse of last 4 passwords
- Account lockout: After 10 failed attempts for PCI DSS (note: tighter than base template's 5)
- Session idle timeout: 15 minutes for CDE systems

**PCI DSS Req. 12.3 — Hardware and Software Technologies:**
- Maintain an inventory of all hardware and software technologies in the CDE
- Review and confirm PCI DSS scope annually and after significant changes

### 3. Data Classification

**PCI DSS Req. 3 — Protect Stored Account Data:**
- CHD must be classified as **Restricted** — highest protection level
- **Sensitive Authentication Data (SAD) must NEVER be stored after authorization** — even if encrypted
  - This includes: full magnetic stripe, CVV/CVC, PIN/PIN block
- PAN must be masked when displayed (show only first 6 and last 4 digits at most)
- PAN must be rendered unreadable in storage — use tokenization, truncation, or AES-256 encryption with key management controls
- Data retention: Define and enforce a data retention policy for CHD; delete CHD that is no longer needed at least quarterly

**PCI DSS Req. 9 — Restrict Physical Access:**
- Physical media containing CHD must be physically secured
- Periodic media inventories required for physical media containing CHD
- Media must be destroyed so CHD cannot be reconstructed before disposal

### 4. Infrastructure / Networking / Cloud

**PCI DSS Req. 1 — Network Security Controls:**
- Network segmentation must isolate the CDE from all other networks — document network diagrams showing CDE boundaries
- Restrict inbound and outbound traffic to that necessary for the CDE
- Review firewall and router rule sets every 6 months

**PCI DSS Req. 2 — Apply Secure Configurations:**
- All system components in CDE must have vendor-supplied default settings changed before deployment
- Develop configuration standards based on CIS Benchmarks or vendor hardening guides
- Enable only necessary services, protocols, and ports on CDE systems

**PCI DSS Req. 4 — Protect Cardholder Data with Strong Cryptography During Transmission:**
- CHD must never be sent over open public networks unencrypted
- TLS 1.2 minimum (TLS 1.3 preferred) for all CHD transmissions
- Certificates must be from trusted CAs; expired or self-signed certificates prohibited for CHD transmission

**PCI DSS Req. 5 — Protect All Systems Against Malware:**
- Anti-malware must be deployed on all CDE systems
- Anti-malware definitions must be updated automatically
- Scans must run regularly; logs reviewed

**PCI DSS Req. 6 — Develop and Maintain Secure Systems and Software:**
- Apply critical security patches within 1 month of release for CDE systems
- All custom-developed applications exposed to the internet must be reviewed for OWASP Top 10 vulnerabilities annually or after changes
- Use a Web Application Firewall (WAF) for all internet-facing web applications in CDE

### 5. Monitoring and Incident Response

**PCI DSS Req. 10 — Log and Monitor All Access:**
- Log all access to CDE systems and CHD — logs must capture user ID, type of event, date/time, success/failure, origin, affected data
- Retain logs for at least 12 months, with the most recent 3 months immediately available
- Review logs daily for all CDE systems using automated tools (SIEM recommended)
- Use time-synchronization technology (NTP) on all CDE systems; clock discrepancies alert within 2 hours

**PCI DSS Req. 11 — Test Security of Systems and Networks:**
- Quarterly external and internal vulnerability scans by a PCI-approved scanning vendor (ASV) for external scans
- Annual penetration test of CDE by qualified internal or external tester
- Penetration test methodology must address OWASP and PTES standards

**PCI DSS Req. 12 — Incident Response:**
- Maintain an incident response plan specific to CHD breaches
- Plan must be reviewed annually and tested
- Immediately notify acquiring bank and card brands (Visa, Mastercard, etc.) upon suspected CHD compromise
- Engage a PCI Forensic Investigator (PFI) for confirmed CHD breaches

### 6. Vendor / Third-Party Risk

**PCI DSS Req. 12.8 — Manage Risk Associated with TPSPs:**
- Maintain a list of all Third-Party Service Providers (TPSPs) with access to CHD or CDE
- Written acknowledgment from each TSP that they are responsible for the security of CHD they possess
- Monitor TPSPs' PCI DSS compliance status annually (obtain their AoC — Attestation of Compliance)
- Contractually require TPSPs to immediately notify [Company Name] of any security incident affecting CHD

---

## SOX IT General Controls (ITGC) Additions

SOX Section 404 requires companies to document and test internal controls over financial reporting. IT systems that support financial processes must have robust IT General Controls (ITGCs).

### SOX ITGC Areas

**1. Access Management Controls (relates to: Access Control, Password policies)**
- Implement and document role-based access to financial systems (ERP, accounting, banking)
- Enforce **Segregation of Duties (SOD)** — the person who initiates a transaction must not be the same person who approves it; document and enforce SOD rules in financial systems
- Quarterly access reviews required for all financial systems — document user access lists, review and certify by business owners
- Provisioning and de-provisioning procedures must be documented with approvals; terminated employee access must be revoked same business day
- Privileged access to financial systems must be logged and reviewed monthly

**2. Change Management Controls (relates to: Change Management Policy)**
- All changes to systems supporting financial reporting require documented approval, testing, and sign-off before production deployment
- Separation of development and production environments required for financial systems
- Emergency changes to financial systems must receive additional post-change review within 5 business days
- Change logs for financial systems must be retained for 7 years

**3. Computer Operations Controls (relates to: Infrastructure, Disaster Recovery)**
- Automated jobs and batch processes supporting financial reporting must be monitored for failures
- Job failures must trigger alerts and be resolved within defined SLAs
- Backup and recovery procedures for financial systems must be tested at least annually; results documented

**4. Logical Access to Programs and Data (relates to: Data Classification, Access Control)**
- Financial data must be classified as **Confidential** at minimum; highly sensitive financial data (e.g., earnings pre-announcement) as **Restricted**
- Database-level access to financial system databases must be restricted and logged
- Query and reporting tool access to financial data must be controlled and audited

**5. IT Audit Logging (relates to: Infrastructure, Cloud Security)**
- Financial systems must maintain audit logs of all transactions, user access, and changes
- Log retention: minimum **7 years** for SOX (align with records retention requirements)
- Logs must be reviewed quarterly for anomalies; results documented for external auditors

---

## Compliance Calendar Additions

| Frequency | Activity |
|-----------|---------|
| Daily | Review CDE security logs (PCI Req. 10) |
| Monthly | Privileged access review for financial systems (SOX ITGC) |
| Quarterly | External vulnerability scan (PCI ASV scan); CHD inventory review; SOX access certification |
| Semi-annually | Internal vulnerability scan; firewall rule review (PCI Req. 11, 1) |
| Annually | Penetration test; PCI SAQ or QSA assessment; SOX ITGC testing; TPSP AoC review |

---

## Key References

| Standard | Resource |
|----------|---------|
| PCI DSS v4.0 | PCI Security Standards Council — pcisecuritystandards.org |
| SOX Section 404 | SEC guidance on ICFR — sec.gov |
| PCAOB AS 2201 | Auditing internal control over financial reporting |
| COSO Internal Control Framework | Committee of Sponsoring Organizations |

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Security Officer] | Initial release |
