# Password Protection Policy

**NIST CSF Functions: Protect (PR)**

## Purpose
To establish requirements for creating, managing, and protecting passwords to ensure secure access to company systems and data.

## Scope
Applies to all passwords used to access company systems, applications, and services.

## Password Requirements

### 7.1 Password Complexity *(NIST CSF: PR.AA-01, PR.AA-03; NIST SP 800-63B §5.1.1)*
**Minimum Requirements:**
- Minimum 12 characters for regular accounts
- Minimum 15 characters for administrative accounts
- All printable ASCII characters and Unicode supported — longer passphrases are encouraged
- No reuse of last 12 passwords
- **Must be checked against known-compromised password lists** (e.g., NIST-maintained lists, HaveIBeenPwned corpus) at set-time and reset-time

> **Note:** Per NIST SP 800-63B §5.1.1.2, composition rules that mandate specific character types (e.g., "must include a number and special character") are **not recommended** — they produce predictable substitutions (e.g., `Password1!`) without improving security. Prioritize length and compromised-password screening instead.

### 7.2 Password Management *(NIST CSF: PR.AA-01)*
- Use approved password management tools for generating and storing passwords
- Each account must have a unique password
- Passwords must not be shared between users
- Document service account passwords in secure, approved locations

### 7.3 Multi-Factor Authentication *(NIST CSF: PR.AA-03)*
**Required for:**
- All administrative accounts
- Remote access to company systems
- Email and cloud service access
- Financial and sensitive business applications

**Approved MFA Methods:**
- Hardware security keys (preferred)
- Mobile app authenticators
- SMS text codes (least preferred)

## Password Security Practices

### 7.4 Password Protection *(NIST CSF: PR.AA-01, PR.AT-01)*
- Never write passwords down in unsecured locations
- Do not share passwords via email, phone, or messaging
- Use secure channels for initial password distribution
- Change default passwords immediately on new systems
- Report suspected password compromise immediately

### 7.5 Password Changes *(NIST CSF: PR.AA-01; NIST SP 800-63B §5.1.1.2)*
- Change passwords immediately if compromise is suspected or confirmed
- Update service account passwords during regular maintenance windows
- Change passwords when employees with access leave the company
- **Do not require periodic arbitrary rotation** (e.g., forced 90-day resets) — per NIST SP 800-63B, routine forced rotation leads to predictable incremental changes (e.g., `Summer2024!` → `Fall2024!`) and reduces security; rotate only on evidence of compromise
- Exception: shared/service accounts with no MFA should be rotated at least annually as a compensating control

### 7.6 System Configuration *(NIST CSF: PR.AA-03, PR.PS-04)*
- Configure account lockout after 5 failed login attempts
- Implement password expiration warnings (14 days advance notice)
- Enable logging of authentication events
- Configure automatic screen locks (15 minutes maximum)

## Special Circumstances

### 7.7 Emergency Access *(NIST CSF: PR.AA-05, PR.PS-01)*
- Maintain secure emergency access procedures
- Document emergency password usage and rotation
- Require dual authorization for emergency access
- Review and audit emergency access quarterly

### 7.8 Third-Party and Vendor Access *(NIST CSF: GV.SC-05, PR.IR-01)*
- Require vendors to comply with password policy
- Use separate accounts for vendor access
- Monitor and audit third-party access regularly
- Revoke vendor access immediately upon contract termination

## Compliance and Monitoring *(NIST CSF: DE.CM-01, DE.CM-01)*
- Regular audits of password compliance
- Monitor for weak or compromised passwords
- Track password policy violations
- Provide additional training for policy violations

## Enforcement
Failure to comply with password requirements, sharing credentials, or failure to report a suspected compromised account are policy violations. Violations must be reported to [Security Officer] and may result in immediate account suspension, disciplinary action up to and including termination, and potential legal action where applicable.

## References
- NIST CSF 2.0: PR.AA (Access Control), PR.AT (Awareness and Training), PR.PS (Protective Technology)
- NIST SP 800-63B: Digital Identity Guidelines — Authentication and Lifecycle Management (§5.1.1 Memorized Secrets)

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Security Officer] | Initial release |