# Data Classification Policy

**NIST CSF Functions: Identify (ID), Protect (PR)**

## Purpose
To establish a framework for classifying [Company Name] data based on sensitivity and business value, ensuring appropriate protection controls are applied throughout the data lifecycle.

## Scope
Applies to all data created, received, processed, stored, or transmitted by [Company Name] employees, contractors, and third parties, regardless of format (digital or physical) or location.

## Data Classification Levels

### 2.1 Classification Tiers *(NIST CSF: ID.AM-5, PR.DS-1)*

[Company Name] uses four classification levels:

| Level | Label | Description | Examples |
|-------|-------|-------------|---------|
| Level 1 | **Public** | Information approved for public release | Marketing materials, published job postings, public website content |
| Level 2 | **Internal** | General business information for internal use | Internal announcements, non-sensitive procedures, general policies |
| Level 3 | **Confidential** | Sensitive business information requiring protection | Financial data, employee records, client information, contracts |
| Level 4 | **Restricted** | Highly sensitive; unauthorized disclosure causes severe harm | Passwords/credentials, regulated personal data (PII/PHI), trade secrets, legal holds |

### 2.2 Default Classification *(NIST CSF: ID.AM-5)*
- Data with no assigned classification defaults to **Confidential** until reviewed
- Data owners are responsible for classifying data under their control
- Classification must be assigned at the time of data creation or receipt

## Data Ownership and Responsibility

### 2.3 Data Owner Responsibilities *(NIST CSF: ID.AM-5, ID.GV-1)*
- Assign and maintain accurate classifications for data in their custody
- Review and update classifications at least annually
- Approve access requests for Confidential and Restricted data
- Ensure proper handling procedures are followed by their teams
- Report misclassification or handling violations to [Security Officer]

### 2.4 Data Custodian Responsibilities *(NIST CSF: PR.DS-1, PR.AC-4)*
- Implement technical controls aligned to classification level
- Maintain access control lists per data owner direction
- Report data handling issues to the data owner
- Ensure backups are protected at the same level as source data

### 2.5 Employee Responsibilities *(NIST CSF: PR.AT-1)*
- Handle data according to its classification level at all times
- Do not reclassify data without data owner approval
- Report suspected misclassification or unauthorized access to [IT Contact]
- Complete annual data handling training

## Handling Requirements by Classification

### 2.6 Public Data *(NIST CSF: PR.DS-1)*
- **Storage:** Any approved system
- **Transmission:** No restrictions
- **Sharing:** May be shared externally without restriction
- **Disposal:** Standard deletion or recycling
- **Labeling:** No labeling required

### 2.7 Internal Data *(NIST CSF: PR.DS-1, PR.DS-2)*
- **Storage:** Company-approved systems; must not be stored on unapproved personal cloud storage
- **Transmission:** Internal channels acceptable; encrypt if transmitted externally
- **Sharing:** Employees and authorized contractors only; written approval for external sharing
- **Disposal:** Secure deletion (overwrite or shred)
- **Labeling:** "INTERNAL" header/footer on documents when shared externally

### 2.8 Confidential Data *(NIST CSF: PR.DS-1, PR.DS-2, PR.AC-4)*
- **Storage:** Encrypted at rest; access restricted to authorized personnel only
- **Transmission:** Encrypted in transit (TLS 1.2+); encrypted email or secure file transfer
- **Sharing:** Need-to-know basis; non-disclosure agreement required for external parties
- **Disposal:** Certified secure deletion (DoD 5220.22-M standard or equivalent); physical shredding
- **Labeling:** "CONFIDENTIAL" watermark or header on all documents
- **Printing:** Retrieve immediately from printers; never leave unattended

### 2.9 Restricted Data *(NIST CSF: PR.DS-1, PR.DS-2, PR.AC-4, PR.DS-5)*
- **Storage:** Encrypted at rest with AES-256 or equivalent; stored in dedicated secure systems; access logged
- **Transmission:** End-to-end encryption required; no transmission via standard email unless encrypted
- **Sharing:** Explicit written authorization from data owner and [Security Officer]; contractual data protection agreements required
- **Disposal:** Cryptographic erasure plus verified overwrite; certificates of destruction required
- **Labeling:** "RESTRICTED" watermark on all copies; numbered copy tracking for physical documents
- **Access logging:** All access must be logged with user, time, and action; logs reviewed monthly

## Data Lifecycle Controls

### 2.10 Data Retention *(NIST CSF: PR.DS-3, PR.IP-6)*

| Classification | Minimum Retention | Maximum Retention | Review Frequency |
|---------------|-------------------|-------------------|-----------------|
| Public | As needed | No limit | N/A |
| Internal | 1 year | 7 years | Annual |
| Confidential | Per legal/regulatory requirement | Per requirement | Annual |
| Restricted | Per legal/regulatory requirement | Per requirement | Bi-annual |

- Retention schedules must comply with applicable laws and regulations
- Legal holds override standard retention schedules
- [Security Officer] must approve any retention schedule deviations

### 2.11 Data Disposal *(NIST CSF: PR.DS-3)*
- Disposal methods must match the classification level (see 2.6–2.9 above)
- Disposal of Confidential and Restricted data must be documented
- Third-party disposal vendors must provide certificates of destruction
- Hard drives and removable media must be physically destroyed or certified wiped before disposal

### 2.12 Cloud and Third-Party Storage *(NIST CSF: PR.DS-1, ID.SC-3)*
- Confidential and Restricted data may only be stored in cloud services approved by [IT Contact]
- Cloud service agreements must include appropriate data protection, audit rights, and deletion guarantees
- Data residency requirements must be confirmed for regulated data (e.g., EU data under GDPR)
- Third parties storing Confidential or Restricted data must complete a vendor security assessment annually

## Compliance and Monitoring *(NIST CSF: DE.CM-1, DE.CM-7)*
- Annual data inventory and classification review by data owners
- Quarterly spot checks by [IT Contact] to verify classification and handling compliance
- Access reviews for Confidential and Restricted data systems conducted quarterly
- Data handling violations logged, reviewed, and reported to [Security Officer] monthly

## Enforcement
Mishandling of classified data, unauthorized disclosure, or failure to apply required controls may result in disciplinary action up to and including termination, and potential legal liability. All incidents involving Restricted data must be reported to [Security Officer] within 24 hours.

## References
- NIST CSF v1.1: ID.AM (Asset Management), PR.DS (Data Security), PR.AC (Access Control)
- NIST SP 800-60: Guide for Mapping Types of Information and Information Systems to Security Categories
- NIST SP 800-188: De-Identification of Government Datasets

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Security Officer] | Initial release |
