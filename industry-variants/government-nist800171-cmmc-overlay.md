# Government Contractor / NIST SP 800-171 & CMMC Overlay

**Applies to:** Organizations that handle Controlled Unclassified Information (CUI) under US government contracts, including those subject to DFARS clause 252.204-7012 and the Cybersecurity Maturity Model Certification (CMMC) program.

> **How to use this overlay:** Read each section alongside the corresponding base policy template. Where this overlay conflicts with a base policy, this overlay takes precedence. Engage a Registered Practitioner Organization (RPO) or C3PAO for formal CMMC assessment preparation.

---

## Who Needs This Overlay

- Defense contractors and subcontractors (DFARS-covered contracts)
- Federal civilian agency contractors handling CUI
- Organizations pursuing CMMC Level 2 or Level 3 certification
- Research institutions with federal grants involving CUI
- Organizations receiving export-controlled data (EAR/ITAR)

---

## Definitions

| Term | Meaning |
|------|---------|
| **CUI** | Controlled Unclassified Information — information requiring safeguarding per law, regulation, or policy (defined by NARA CUI Registry) |
| **DFARS** | Defense Federal Acquisition Regulation Supplement |
| **CMMC** | Cybersecurity Maturity Model Certification — DoD framework for assessing contractor security |
| **CMMC Level 2** | Requires implementation of all 110 NIST SP 800-171 practices; third-party assessment required for critical programs |
| **CMMC Level 3** | Advanced — covers NIST SP 800-172 practices; government-led assessment |
| **FCI** | Federal Contract Information — information provided by or generated for the government under contract (not public) |
| **SSP** | System Security Plan — required document describing how security requirements are implemented |
| **POA&M** | Plan of Action and Milestones — documents deficiencies and remediation plans |
| **C3PAO** | CMMC Third-Party Assessment Organization |

---

## NIST SP 800-171 / CMMC Control Family Additions

NIST SP 800-171 has 14 control families covering 110 practices. Below are the most impactful additions to the base templates.

### 1. Governance — System Security Plan (SSP)

**NIST SP 800-171 Req. 3.12 — Assessment, Authorization, and Monitoring:**
- A **System Security Plan (SSP)** is required — document all systems that process, store, or transmit CUI, the security requirements that apply, and how each is implemented or planned
- SSP must include: system description, system boundary, network diagrams, hardware/software inventory, security control implementation statements
- SSP must be reviewed and updated at least annually and after significant changes
- A **Plan of Action and Milestones (POA&M)** must document any unimplemented controls, along with remediation timelines
- Designate a **CUI Program Manager** responsible for CUI identification, marking, and handling compliance

### 2. Access Control

**NIST SP 800-171 3.1 — Access Control (22 requirements):**
- Limit system access to authorized users and the transactions/functions they are permitted to execute
- Limit system access to the types of transactions and functions that authorized users are permitted to execute
- Control CUI posted or processed on publicly accessible systems — no CUI on public websites or portals unless explicitly authorized
- **Separate duties** of individuals to reduce the risk of malevolent activity (SOD)
- **Least privilege** — implement for accounts of all users, including administrators
- Control the use of portable storage devices on systems handling CUI — prohibit use of unapproved removable media
- Control CUI system access from external systems — require VPN and MFA for any external access to CUI systems
- Limit use of portable storage devices to authorized devices with documented approval

### 3. Awareness and Training

**NIST SP 800-171 3.2 — Awareness and Training:**
- All personnel who access CUI systems must receive **security awareness training** before access is granted and annually thereafter
- Training must cover: CUI identification and handling, insider threat awareness, social engineering/phishing, reporting procedures
- Personnel with significant security responsibilities (system admins, security staff) must receive **role-based security training** before assuming duties and annually
- Document all training completion with signed attestation; retain records

### 4. Audit and Accountability

**NIST SP 800-171 3.3 — Audit and Accountability:**
- **Create and retain system audit logs** to enable monitoring, analysis, investigation, and reporting of unlawful or unauthorized activity on CUI systems
- Audit logs must capture: user IDs, types of events, dates/times, success/failure indicators, origins, identities of accessed resources
- Audit logs for CUI systems must be retained for **3 years minimum** (check contract requirements — may be longer)
- Protect audit logs from unauthorized access, modification, and deletion — use a write-once or SIEM solution
- Review audit logs at least weekly using automated alerting for anomalies
- Ensure that actions of individual system users can be traced to those users

### 5. Configuration Management

**NIST SP 800-171 3.4 — Configuration Management:**
- Establish and document **configuration baselines** for all CUI systems
- Establish and enforce security configuration settings for IT products employed in CUI systems
- Track, review, approve, and log changes to CUI systems (see Change Management Policy additions)
- Analyze security impact of changes prior to implementation
- Define, document, approve, and enforce **physical and logical access restrictions** associated with changes
- Prevent or restrict installation of software without explicit authorization — use application whitelisting where feasible

### 6. Identification and Authentication

**NIST SP 800-171 3.5 — Identification and Authentication:**
- Identify system users, processes acting on behalf of users, and devices — unique IDs required
- Authenticate the identities of all users, processes, and devices before granting access to CUI systems
- Use **multifactor authentication** for local and network access to CUI systems — required for all privileged and non-privileged accounts
- MFA must use at least two different authentication factors: something you know, something you have, or something you are
- Password complexity: minimum 12 characters; complexity required; reuse of last 24 passwords prohibited
- **Temporary passwords must be changed upon first use**

### 7. Incident Response

**NIST SP 800-171 3.6 — Incident Response:**
- Establish an operational incident-handling capability covering **preparation, detection, analysis, containment, recovery, and user response**
- Track, document, and report incidents to appropriate organizational officials and government authorities
- **DFARS 252.204-7012 reporting requirement:** Report cyber incidents involving CUI to **US-CERT and the DoD** within **72 hours** of discovery
- Incident reports submitted via dibnet.dod.mil; preserve images of compromised systems for 90 days
- Preserve and protect information and evidence associated with CUI incidents
- Test incident response capability annually

### 8. Maintenance

**NIST SP 800-171 3.7 — Maintenance:**
- Perform maintenance on CUI systems using only approved tools and technicians
- Control all maintenance activities, whether performed on-site or remotely
- Sanitize equipment before allowing off-site maintenance — ensure CUI is removed or protected
- Check media containing diagnostic programs for malicious code before use
- Require MFA for remote maintenance sessions on CUI systems
- Supervise maintenance activities of personnel without required access authorization

### 9. Media Protection

**NIST SP 800-171 3.8 — Media Protection:**
- Protect (e.g., physically control and securely store) system media containing CUI
- Limit access to CUI on system media to authorized users
- Sanitize or destroy CUI before disposal or reuse — use NIST SP 800-88 methods
- Mark media containing CUI with required CUI markings per the CUI Registry
- Prohibit the use of portable storage without identifiable owner
- Protect CUI during transport (encrypt removable media; use sealed containers for physical shipment)

### 10. Physical Protection

**NIST SP 800-171 3.10 — Physical and Environmental Protection:**
- Limit physical access to CUI systems to authorized individuals
- Protect and monitor physical facility and infrastructure for CUI systems
- Escort visitors and monitor visitor activity in areas with CUI
- Maintain audit logs of physical access to areas with CUI systems
- Control and manage physical access devices (keys, combinations, access cards)
- Enforce safeguarding measures for CUI at alternate work sites (remote workers)

### 11. Risk Assessment

**NIST SP 800-171 3.11 — Risk Assessment:**
- Periodically assess risk to organizational operations, assets, and individuals from operating CUI systems
- Risk assessment must be documented and reviewed at least annually
- Scan for vulnerabilities in CUI systems periodically and when new vulnerabilities are identified
- Remediate vulnerabilities in accordance with risk assessments (see Vulnerability Management Policy)

### 12. System and Communications Protection

**NIST SP 800-171 3.13 — System and Communications Protection:**
- Monitor, control, and protect communications at external system boundaries and at key internal boundaries
- Implement **subnetworks for publicly accessible system components** separated from internal CUI networks
- Deny network communications traffic by default (deny all, permit by exception)
- Implement cryptographic mechanisms to prevent unauthorized disclosure of CUI during transmission
- Terminate network connections after defined period of inactivity — maximum 30 minutes for CUI sessions
- Employ FIPS-validated cryptography when used to protect CUI (FIPS 140-2 or 140-3 validated modules required)
- Prohibit remote activation of collaborative computing devices in spaces where CUI discussions occur (disable microphones/cameras in secure meeting areas unless required)

### 13. System and Information Integrity

**NIST SP 800-171 3.14 — System and Information Integrity:**
- Identify, report, and correct information and system flaws in a timely manner
- Provide protection from malicious code at appropriate locations — anti-malware required on all CUI systems
- Update malicious code protection mechanisms when new releases are available
- Monitor CUI systems to detect attacks and indicators of potential attacks
- Receive alerts from external organizations of threats to CUI systems and take action
- Identify unauthorized use of CUI systems

---

## Required Documentation (CMMC Level 2)

Beyond policy documents, maintain:

| Document | Description | Review Frequency |
|----------|-------------|-----------------|
| System Security Plan (SSP) | How each NIST SP 800-171 control is implemented | Annual + after changes |
| Plan of Action & Milestones (POA&M) | Controls not yet implemented + remediation timeline | Monthly |
| CUI Asset Inventory | All systems handling CUI with system boundary | Quarterly |
| Network Diagrams | CUI system boundaries and data flows | Annual + after changes |
| User Access List | All users with access to CUI systems | Quarterly review |
| Security Training Records | Completion dates and signatures | Maintained continuously |
| Incident Log | All incidents involving CUI | Maintained continuously |
| Configuration Baselines | Approved configurations for CUI systems | Annual + after changes |

---

## CMMC Level 2 Self-Assessment

Before engaging a C3PAO:
- Complete an internal gap assessment against all 110 NIST SP 800-171 practices
- Score using the DoD CMMC Assessment scoring methodology (110 points maximum)
- Contracts requiring CMMC Level 2 may require submission of a self-assessment score via SPRS (Supplier Performance Risk System)
- Scores must be updated within 90 days of significant changes

---

## Key References

| Resource | Source |
|----------|--------|
| NIST SP 800-171 Rev 3 | csrc.nist.gov |
| CMMC Model v2.0 | dodcmmc.mil |
| CUI Registry | archives.gov/cui |
| DFARS 252.204-7012 | acquisition.gov |
| NIST SP 800-172 (Enhanced) | csrc.nist.gov |
| DoD Cyber Crime Center (DC3) | dc3.mil |

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Security Officer] | Initial release |
