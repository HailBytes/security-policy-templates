# Password Protection Policy

**NIST CSF Functions: Protect (PR)**

## Purpose
To establish requirements for creating, managing, and protecting passwords to ensure secure access to company systems and data.

## Scope
Applies to all passwords used to access company systems, applications, and services.

## Password Requirements

### 7.1 Password Requirements *(NIST CSF: PR.AC-1, PR.AC-7)*
**Minimum Length (primary control):**
- Minimum 12 characters for regular accounts
- Minimum 15 characters for administrative accounts
- Passphrases of 4 or more random words (≥ 20 characters) are an equally acceptable alternative and are encouraged per NIST SP 800-63B

**Complexity (secondary control — apply only when your platform enforces it):**
- Where complexity rules are required by your authentication system or a compliance framework, require a mix of uppercase, lowercase, numbers, and special characters
- Note: NIST SP 800-63B recommends *against* mandatory character-class rules for user-chosen passwords because they drive predictable substitutions (e.g., P@ssw0rd1!); favour length and breach screening instead

**Prohibited patterns:**
- No personal information (names, birthdays, username) or predictable patterns (Season+Year, CompanyName+Number, etc.)
- No reuse of the last 12 passwords
- New passwords must be screened against known breached-password databases at enrollment and reset (e.g., check against the HIBP Pwned Passwords corpus or an equivalent offline list)

### 7.2 Password Management *(NIST CSF: PR.AC-1)*
- Use approved password management tools for generating and storing passwords
- Each account must have a unique password
- Passwords must not be shared between users
- Document service account passwords in secure, approved locations

### 7.3 Multi-Factor Authentication *(NIST CSF: PR.AC-7)*
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

### 7.4 Password Protection *(NIST CSF: PR.AC-1, PR.AT-1)*
- Never write passwords down in unsecured locations
- Do not share passwords via email, phone, or messaging
- Use secure channels for initial password distribution
- Change default passwords immediately on new systems
- Report suspected password compromise immediately

### 7.5 Password Changes *(NIST CSF: PR.AC-1)*
- Change passwords immediately if compromise is suspected
- Update service account passwords during regular maintenance windows
- Change passwords when employees with access leave the company
- Regular password rotation for shared or service accounts (90 days)

### 7.6 System Configuration *(NIST CSF: PR.AC-7, PR.PT-1)*
- Configure account lockout after 5 failed login attempts
- Implement password expiration warnings (14 days advance notice)
- Enable logging of authentication events
- Configure automatic screen locks (15 minutes maximum)

## Special Circumstances

### 7.7 Emergency Access *(NIST CSF: PR.AC-4, PR.IP-1)*
- Maintain secure emergency access procedures
- Document emergency password usage and rotation
- Require dual authorization for emergency access
- Review and audit emergency access quarterly

### 7.8 Third-Party and Vendor Access *(NIST CSF: ID.SC-3, PR.AC-5)*
- Require vendors to comply with password policy
- Use separate accounts for vendor access
- Monitor and audit third-party access regularly
- Revoke vendor access immediately upon contract termination

## Compliance and Monitoring *(NIST CSF: DE.CM-1, DE.CM-7)*
- Regular audits of password compliance
- Monitor for weak or compromised passwords
- Track password policy violations
- Provide additional training for policy violations

## References
- NIST CSF v1.1: PR.AC (Access Control), PR.AT (Awareness and Training), PR.PT (Protective Technology)
- NIST SP 800-63B: Digital Identity Guidelines — Memorized Secret Authenticators (§5.1)

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Security Officer] | Initial release |