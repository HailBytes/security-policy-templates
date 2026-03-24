# Remote Work and BYOD Policy

**NIST CSF Functions: Protect (PR), Detect (DE)**

## Purpose
To establish security requirements for employees working remotely and for the use of personal devices (Bring Your Own Device) to access [Company Name] systems, data, and networks.

## Scope
Applies to all [Company Name] employees, contractors, and third parties who work remotely or use personally owned devices to access company resources.

## Remote Work Security Requirements

### 3.1 Approved Work Locations *(NIST CSF: PR.AC-3, PR.DS-2)*
- Remote work must be conducted in a physically secure, private location
- Employees must not work from public locations (cafes, airports, libraries) without VPN active
- Shoulder surfing risks must be mitigated — use privacy screens in public spaces
- Home offices must have a lockable door or secure area for sensitive work

### 3.2 Network Security *(NIST CSF: PR.AC-3, PR.PT-4)*
- All remote access to [Company Name] systems requires an approved VPN connection
- Home routers must use WPA2 or WPA3 encryption; default passwords must be changed
- Public Wi-Fi networks must not be used without VPN active
- Split tunneling is prohibited unless explicitly approved by [IT Contact]
- Network access control logs must be retained for a minimum of 90 days

### 3.3 VPN and Authentication *(NIST CSF: PR.AC-7, PR.AC-3)*
- Multi-factor authentication (MFA) is required for all remote access
- VPN credentials must not be shared between users
- Sessions must be terminated after 30 minutes of inactivity
- Failed VPN login attempts must be logged and reviewed weekly by [IT Contact]

### 3.4 Physical Security of Work Environment *(NIST CSF: PR.AC-2, PR.DS-1)*
- Company devices and sensitive documents must be secured when not in use
- Screen locks must be enabled and activate within 15 minutes of inactivity
- Company data must not be printed in unsecured home environments without business justification
- Printed sensitive materials must be shredded using cross-cut shredder when no longer needed

## BYOD Requirements

### 3.5 Device Eligibility *(NIST CSF: ID.AM-1, PR.AC-1)*
- Personal devices must be approved by [IT Contact] before accessing company resources
- Supported operating systems: Windows 10/11, macOS 12+, iOS 15+, Android 11+
- Devices must be running current OS security patches (within 30 days of release)
- Jailbroken or rooted devices are prohibited from accessing company resources
- Device inventory must be maintained by [IT Contact] and reviewed quarterly

### 3.6 Required Security Controls on Personal Devices *(NIST CSF: PR.AC-1, PR.DS-1)*
- Screen lock with PIN, password, or biometric authentication required
- Full-disk encryption must be enabled
- Approved endpoint security software must be installed and active
- Automatic OS and application updates must be enabled
- Company Mobile Device Management (MDM) profile must be installed and active

### 3.7 Acceptable Use on Personal Devices *(NIST CSF: PR.AT-1, PR.DS-5)*
- Company data must only be stored in approved cloud applications or encrypted containers
- Personal and company data must be kept logically separate (MDM enforced where possible)
- Company email must be accessed through the approved application only
- Screenshots or recordings of company data are prohibited on personal devices
- Company data must not be backed up to personal cloud storage (e.g., personal iCloud, Google Drive)

### 3.8 Lost or Stolen Devices *(NIST CSF: RS.CO-2, PR.IP-1)*
- Lost or stolen devices must be reported to [IT Contact] and [Security Officer] within 2 hours of discovery
- [IT Contact] will initiate remote wipe of company data within 4 hours of notification
- Employees consent to remote wipe of company data partition upon device enrollment
- A police report may be required for stolen devices
- Incident must be documented and reviewed per the Incident Response policy

## Software and Data Controls

### 3.9 Approved Applications *(NIST CSF: PR.DS-1, PR.IP-1)*
- Only approved applications may be used to access, store, or transmit company data
- Shadow IT applications are prohibited; employees must request new tools through [IT Contact]
- Applications must come from official app stores (Apple App Store, Google Play, vendor websites)
- All applications must be kept updated to current supported versions

### 3.10 Data Handling *(NIST CSF: PR.DS-1, PR.DS-2, PR.DS-5)*
- Sensitive and confidential data must be accessed via secure remote desktop or approved SaaS tools — not downloaded to personal devices
- Data classified as Confidential or higher must not be stored locally on personal devices
- Transfer of company data to personal email accounts is prohibited
- USB drives and removable media are prohibited on devices accessing company resources unless encrypted and approved

### 3.11 Monitoring and Auditing *(NIST CSF: DE.CM-1, DE.CM-3, DE.AE-3)*
- Company-issued devices used remotely are subject to monitoring of network traffic and application usage
- MDM enrollment provides [Company Name] visibility into device compliance status
- Employees acknowledge that company data on personal devices may be reviewed during a security incident
- Compliance status reports will be reviewed monthly by [IT Contact]

## Employee Responsibilities

### 3.12 Training and Acknowledgment *(NIST CSF: PR.AT-1, PR.AT-2)*
- All remote workers and BYOD users must complete remote work security training annually
- Employees must sign the Remote Work and BYOD Acknowledgment Form before gaining remote access
- Employees are responsible for understanding and following this policy
- Policy changes will be communicated with 30 days notice; re-acknowledgment required for major changes

### 3.13 Termination and Offboarding *(NIST CSF: PR.AC-1, PR.IP-11)*
- Remote access credentials must be revoked on the last day of employment
- Company data and applications must be removed from personal devices within 5 business days of termination
- Company-issued equipment must be returned within 5 business days of termination
- Employees must certify in writing that all company data has been removed from personal devices

## Compliance and Monitoring *(NIST CSF: DE.CM-1, DE.CM-7)*
- Quarterly audits of remote access logs and active VPN accounts
- Monthly review of MDM device compliance reports
- Annual remote work security assessment by [IT Contact]
- Non-compliance must be escalated to [Security Officer] and may result in access revocation

## Enforcement
Violations of this policy may result in immediate suspension of remote access privileges, disciplinary action up to and including termination, and potential legal action for intentional data exposure. All violations must be reported to [Security Officer].

## References
- NIST CSF v1.1: PR.AC (Access Control), PR.DS (Data Security), PR.AT (Awareness and Training), DE.CM (Security Continuous Monitoring)
- NIST SP 800-114: User's Guide to Telework and Bring Your Own Device (BYOD) Security
- NIST SP 800-46: Guide to Enterprise Telework, Remote Access, and BYOD Security

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Security Officer] | Initial release |
