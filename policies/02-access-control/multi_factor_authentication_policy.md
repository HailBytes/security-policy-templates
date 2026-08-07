# Multi-Factor Authentication (MFA) Policy

**NIST CSF Functions: Protect (PR), Detect (DE)**

## Purpose
To require and standardize the use of multi-factor authentication (MFA) across all [Company Name] systems so that stolen or guessed credentials alone cannot grant unauthorized access.

## Scope
Applies to all [Company Name] employees, contractors, and third parties who authenticate to any company-owned or company-managed system, application, or cloud service.

## MFA Requirements

### 2.1 Mandatory MFA Coverage *(NIST CSF: PR.AA-03, PR.AA-01)*
MFA is required for all of the following:
- All accounts with administrative or privileged access
- Remote access, including VPN and jump servers
- Email and collaboration platforms (e.g., Microsoft 365, Google Workspace)
- Cloud management consoles (AWS, Azure, GCP, and equivalents)
- Code repositories and CI/CD pipelines
- Financial, payroll, and HR systems
- Identity and access management (IAM) systems
- Any system storing Confidential or Restricted data (as defined in the Data Classification Policy)

### 2.2 Approved MFA Methods *(NIST CSF: PR.AA-03)*
Methods are listed in order of preference:

| Tier | Method | Use Case |
|------|--------|----------|
| 1 (Preferred) | Hardware security keys (FIDO2/WebAuthn) | All accounts; required for privileged access |
| 2 | Time-based one-time password (TOTP) authenticator app | Standard user accounts |
| 3 | Push notification via approved authenticator | Standard user accounts where TOTP is impractical |
| 4 (Least Preferred) | SMS one-time code | Only where no higher-tier method is supported by the system |

SMS one-time codes must not be used for administrative, privileged, or remote-access accounts.

### 2.3 Accounts Exempt from MFA *(NIST CSF: PR.AA-05, PR.PS-01)*
Only the following account types may be exempt, with documented justification and compensating controls:
- Service accounts with no interactive login capability, where API key or certificate-based auth is enforced instead
- Legacy systems that technically cannot support MFA, subject to [Security Officer] approval and quarterly review

All exemptions must be recorded in the access control register maintained by [IT Contact].

## Enrollment and Management

### 2.4 Enrollment Requirements *(NIST CSF: PR.AA-01, PR.AT-01)*
- MFA must be enrolled before a user account is granted access to any system listed in §2.1
- Enrollment must be completed within 24 hours of account creation
- Users must register a minimum of two MFA methods (primary + backup) to prevent lockout
- [IT Contact] is responsible for verifying enrollment and auditing the register quarterly

### 2.5 Recovery and Lost-Device Procedures *(NIST CSF: PR.AA-05, PR.AA-01)*
- Recovery codes must be generated at enrollment, stored in the company password manager, and not transmitted via email or SMS
- MFA reset requests must be submitted through the official IT helpdesk ticket system and require identity verification by [IT Contact] before processing
- Self-service resets without identity verification are prohibited
- If an MFA device is lost or stolen, [IT Contact] must be notified within 4 hours; the old factor must be removed and a new one enrolled before access is restored

### 2.6 MFA for Service Accounts and APIs *(NIST CSF: PR.AA-01, PR.IR-01)*
- Service accounts must use certificate-based authentication, API keys with IP restrictions, or OAuth 2.0 client credentials—not MFA bypass tokens
- API keys and certificates must be rotated at least every 90 days
- [IT Contact] must maintain an inventory of all service account credentials and review it quarterly

## System Configuration Standards

### 2.7 Technical Controls *(NIST CSF: PR.AA-03, PR.PS-04)*
[IT Contact] must configure authentication systems to:
- Enforce MFA as a required step (not optional) for all accounts in §2.1
- Reject authentication if the MFA step is not completed within 5 minutes
- Lock an account after 5 consecutive failed MFA attempts; unlock requires helpdesk intervention
- Record every authentication event (success, failure, method used) and retain logs for a minimum of 90 days
- Apply Conditional Access or equivalent policies to block access from untrusted networks without a valid MFA challenge

### 2.8 Phishing-Resistant MFA for High-Risk Roles *(NIST CSF: PR.AA-03, PR.AA-05)*
The following roles must use FIDO2/WebAuthn hardware keys (Tier 1 only) and may not fall back to TOTP or SMS:
- System administrators and IT operations staff
- Executives and board members with access to financial or strategic data
- Finance and payroll personnel
- Accounts with write access to production infrastructure or code repositories

## Compliance and Monitoring *(NIST CSF: DE.CM-01, DE.CM-01)*
- [IT Contact] must generate a monthly MFA coverage report showing the percentage of in-scope accounts with MFA enrolled
- Any in-scope account without MFA enrolled must be flagged within 24 hours and remediated within 48 hours
- [Security Officer] must review exemptions quarterly and revoke any that no longer meet documented criteria
- MFA logs must be correlated with failed login alerts and reviewed weekly for anomalies
- The MFA coverage metric must be included in the quarterly security KPI dashboard

## Enforcement
Accounts found to be out of compliance with this policy will be suspended until MFA is enrolled. Repeat violations or deliberate circumvention of MFA controls will result in disciplinary action up to and including termination, and may be escalated to legal counsel if external systems were accessed without authorization.

## References
- NIST CSF 2.0: PR.AA (Access Control), PR.AT (Awareness and Training), PR.PS (Protective Technology), DE.CM (Security Continuous Monitoring)
- NIST SP 800-63B: Digital Identity Guidelines — Authentication and Lifecycle Management
- CISA: More Than a Password — MFA Guidance for Organizations
- Related policies: Password Protection Policy, Remote Work and BYOD Policy, Data Classification Policy

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Security Officer] | Initial release |
