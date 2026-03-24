# Vendor and Third-Party Risk Management Policy

**NIST CSF Functions: Identify (ID), Protect (PR)**

## Purpose
To establish requirements for assessing, managing, and monitoring security risks introduced by vendors, suppliers, and third-party service providers who have access to [Company Name] data, systems, or facilities.

## Scope
Applies to all third parties that access, process, store, or transmit [Company Name] data or that provide technology, services, or products integrated into [Company Name] operations. This includes cloud providers, managed service providers, software vendors, contractors, and consultants.

## Vendor Risk Tiers

### 4.1 Risk Tiering *(NIST CSF: ID.SC-1, ID.RA-3)*
Third parties are assigned a risk tier based on data access and criticality:

| Tier | Description | Assessment Frequency | Examples |
|------|-------------|---------------------|---------|
| **Critical** | Access to Restricted data or systems; business-critical services | Annual + event-triggered | Payroll processor, cloud infrastructure, MSP |
| **High** | Access to Confidential data; significant operational dependency | Annual | CRM vendors, accounting software, IT contractors |
| **Medium** | Access to Internal data; limited operational dependency | Every 2 years | HR platforms, project management tools |
| **Low** | No data access; minimal operational impact | Every 3 years | Office supplies, general utilities |

Risk tier assignment is performed by [Security Officer] during onboarding and reviewed annually.

## Vendor Onboarding

### 4.2 Pre-Engagement Assessment *(NIST CSF: ID.SC-1, ID.SC-2)*
Before engaging any Critical or High tier vendor:
- Complete the [Company Name] Vendor Security Questionnaire
- Review the vendor's most recent security certifications (SOC 2, ISO 27001, or equivalent)
- Confirm the vendor carries adequate cyber liability insurance
- Verify the vendor's data breach notification procedures align with [Company Name] requirements
- Document the assessment results and store in the vendor register

For Medium tier vendors:
- Abbreviated security questionnaire required
- Review publicly available security documentation

### 4.3 Contractual Requirements *(NIST CSF: ID.SC-3, ID.SC-4)*
All vendor contracts involving data access must include:
- **Data Processing Agreement (DPA)** or equivalent data protection terms
- Confidentiality and non-disclosure obligations
- Security incident notification within **72 hours** of discovery
- Right to audit security controls (or accept third-party audit reports)
- Data return and deletion requirements upon contract termination
- Sub-processor disclosure and approval requirements
- Compliance with applicable regulations (GDPR, HIPAA, PCI DSS, etc.)
- Liability provisions for data breaches caused by vendor negligence

Contracts must be reviewed by legal counsel before execution for Critical and High tier vendors.

### 4.4 Access Provisioning *(NIST CSF: PR.AC-1, PR.AC-3, PR.AC-5)*
- Vendor access follows the principle of least privilege
- Separate accounts must be created for each vendor; no shared credentials
- Vendor access must be time-limited and tied to the contract period
- Remote access requires VPN and MFA
- All vendor access must be logged and monitored
- Access must be revoked within 24 hours of contract termination or scope reduction

## Ongoing Vendor Management

### 4.5 Continuous Monitoring *(NIST CSF: ID.SC-4, DE.CM-6)*
- Monitor Critical vendors for security incidents using threat intelligence sources
- Review vendor security advisories and patch bulletins monthly
- Track vendor's security posture changes (certifications lapsed, data breaches reported)
- Review vendor access logs quarterly to verify access is appropriate and active

### 4.6 Periodic Reassessment *(NIST CSF: ID.SC-2, ID.RA-5)*
- Conduct formal reassessments on the schedule defined in the risk tier table (4.1)
- Reassessment must be triggered immediately by:
  - Vendor security incident or data breach
  - Significant change in vendor services or data access scope
  - Change in vendor ownership or business structure
  - Failed renewal of security certification
- Document reassessment results; escalate deteriorating risk posture to [Security Officer]

### 4.7 Vendor Security Questionnaire *(NIST CSF: ID.SC-2)*
The standard questionnaire for Critical and High tier vendors must cover:
- Information security program maturity
- Access control and authentication practices
- Encryption standards for data at rest and in transit
- Incident response capabilities and notification procedures
- Business continuity and disaster recovery plans
- Sub-processor and fourth-party risk management
- Compliance certifications and audit reports
- Vulnerability management and patch management practices
- Physical security controls

## Sub-Processor and Supply Chain Controls

### 4.8 Sub-Processor Management *(NIST CSF: ID.SC-1, ID.SC-3)*
- Critical and High tier vendors must disclose all sub-processors that handle [Company Name] data
- [Company Name] must approve changes to sub-processor lists before implementation
- Vendor agreements must flow down equivalent security requirements to sub-processors
- [Security Officer] maintains a register of known sub-processors and their risk ratings

### 4.9 Software Supply Chain *(NIST CSF: ID.SC-4, PR.DS-6)*
- Open-source and third-party software components must be inventoried (Software Bill of Materials)
- Known vulnerabilities in third-party software must be tracked and remediated per the Vulnerability Management Policy
- Software from sanctioned or high-risk origin countries must require additional review
- Code signing must be verified for software installed on [Company Name] systems

## Incident and Termination Procedures

### 4.10 Vendor Incident Response *(NIST CSF: RS.CO-3, RS.AN-2)*
- If a vendor reports a security incident affecting [Company Name] data, [Security Officer] must be notified immediately
- Vendor must be asked for a written incident report within 5 business days
- [Company Name] reserves the right to conduct its own investigation
- Vendor incidents must be tracked in the [Company Name] incident log
- Legal counsel must be consulted for incidents involving Restricted or regulated data

### 4.11 Vendor Offboarding *(NIST CSF: PR.AC-1, PR.DS-3, PR.IP-11)*
Upon contract termination or non-renewal:
- All vendor access credentials revoked within 24 hours
- Vendor must certify in writing that all [Company Name] data has been deleted or returned within 30 days
- Certificates of destruction required for Confidential and Restricted data
- All shared credentials or API keys rotated immediately
- Contract records and assessment documentation retained per data retention policy

## Compliance and Monitoring *(NIST CSF: DE.CM-1, ID.GV-3)*
- [Security Officer] maintains a vendor register updated in real-time for Critical/High vendors
- Monthly review of vendor access logs for unauthorized or excessive access
- Annual review of all vendor contracts and risk tier assignments
- Quarterly executive summary of top vendor risks reported to leadership

## Enforcement
Engaging vendors without completing required assessments, or failing to include mandatory contractual terms, constitutes a policy violation. Violations must be reported to [Security Officer] and may result in immediate contract suspension and disciplinary action for the responsible employee.

## References
- NIST CSF v1.1: ID.SC (Supply Chain Risk Management), ID.RA (Risk Assessment), PR.AC (Access Control)
- NIST SP 800-161: Cybersecurity Supply Chain Risk Management Practices
- ISO/IEC 27036: Information Security for Supplier Relationships

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Security Officer] | Initial release |
