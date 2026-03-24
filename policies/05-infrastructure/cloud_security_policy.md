# Cloud Security Policy

**NIST CSF Functions: Identify (ID), Protect (PR), Detect (DE)**

## Purpose
To establish security requirements for [Company Name]'s use of cloud services (IaaS, PaaS, and SaaS), ensuring that data and workloads in cloud environments are protected with controls equivalent to on-premises standards.

## Scope
Applies to all cloud services used by [Company Name] employees, contractors, and systems, including but not limited to Infrastructure as a Service (IaaS), Platform as a Service (PaaS), and Software as a Service (SaaS). Unauthorized (shadow IT) cloud use is covered by this policy.

## Cloud Service Governance

### 5.1 Approved Cloud Services *(NIST CSF: ID.AM-2, ID.GV-1)*
- All cloud services must be reviewed and approved by [IT Contact] before use
- [IT Contact] maintains a register of approved cloud services with classification, data types permitted, and risk tier
- Approved cloud services register must be reviewed and updated quarterly
- Employees must not use unapproved cloud services to store, process, or transmit [Company Name] data
- Discovery of shadow IT cloud usage must be reported to [IT Contact] within 5 business days

### 5.2 Cloud Procurement Requirements *(NIST CSF: ID.SC-3, ID.SC-4)*
Before approving a cloud service:
- Vendor must complete [Company Name] Vendor Security Questionnaire (see Vendor Risk Policy)
- Service must support required data residency (geographic region for data storage)
- Vendor must provide evidence of SOC 2 Type II, ISO 27001, or equivalent certification for Critical/High data services
- Data Processing Agreement (DPA) must be executed before processing any personal data
- Multi-factor authentication support must be confirmed
- Data export and portability capabilities must be verified

## Identity and Access Management

### 5.3 Cloud Access Controls *(NIST CSF: PR.AC-1, PR.AC-3, PR.AC-4)*
- Unique, individual accounts required for all cloud service users — no shared credentials
- Multi-factor authentication (MFA) required for all cloud services that support it
- Privileged (admin) cloud accounts must use hardware security keys or equivalent strong MFA
- Administrative access must be role-based and limited to the minimum required (least privilege)
- Unused accounts must be disabled within 30 days of last login
- Federated identity (SSO) via [Company Name]'s identity provider is preferred over direct cloud accounts

### 5.4 Privileged Access in Cloud *(NIST CSF: PR.AC-4, PR.AC-6)*
- Cloud console root/owner accounts must have MFA enforced and stored credentials secured in a vault
- Root/owner accounts must not be used for daily operations
- Privileged access sessions in cloud management consoles must be logged
- Privileged role assignments must be reviewed monthly by [IT Contact]
- Just-in-time (JIT) privileged access is recommended for production environments

## Data Protection in Cloud

### 5.5 Data Encryption *(NIST CSF: PR.DS-1, PR.DS-2)*
- Confidential and Restricted data must be encrypted at rest using AES-256 or equivalent
- All data in transit to and from cloud services must use TLS 1.2 or higher
- [Company Name]-managed encryption keys are required for Restricted data; cloud provider-managed keys acceptable for Confidential data
- Encryption key management procedures must be documented and reviewed annually
- Key rotation must occur at least annually for customer-managed keys

### 5.6 Data Residency and Sovereignty *(NIST CSF: PR.DS-1, ID.GV-3)*
- Regulated personal data (e.g., EU personal data) must remain within approved geographic regions
- Cloud service region configuration must be verified during provisioning and reviewed annually
- Data residency requirements must be documented per service in the approved cloud register
- Cloud service data replication or CDN configurations must not violate residency requirements

### 5.7 Data Backup and Recovery *(NIST CSF: PR.DS-4, RC.RP-1)*
- Cloud-hosted data must be backed up per the same schedule as equivalent on-premises data
- Backups must be stored in a geographically separate cloud region or provider
- Backup restoration must be tested at least annually
- Recovery Time Objective (RTO) and Recovery Point Objective (RPO) must be defined per service

## Cloud Configuration Security

### 5.8 Secure Configuration Baselines *(NIST CSF: PR.IP-1, PR.PT-3)*
- All cloud resources must be provisioned from approved configuration templates (Infrastructure as Code where possible)
- Public access must be disabled by default for storage buckets, databases, and compute instances
- Default service account credentials and API keys must be rotated immediately upon provisioning
- Network security groups and firewall rules must follow deny-by-default with explicit allow rules
- Cloud security posture management (CSPM) tools must be used to detect misconfigurations

### 5.9 Network Segmentation *(NIST CSF: PR.AC-5, PR.PT-4)*
- Production, development, and testing environments must be logically separated
- Inbound access to management interfaces must be restricted to known IPs or VPN
- Inter-service communication must use private networking where available
- Public-facing endpoints must be protected by a Web Application Firewall (WAF) for web services

### 5.10 Infrastructure as Code (IaC) Security *(NIST CSF: PR.IP-1, PR.DS-6)*
- Infrastructure as Code templates must be stored in version-controlled repositories
- IaC changes must go through peer review and automated security scanning before deployment
- Hardcoded credentials in IaC files are prohibited; use secrets management services
- IaC security scanning must run as part of CI/CD pipelines

## Monitoring and Incident Response

### 5.11 Cloud Logging and Monitoring *(NIST CSF: DE.CM-1, DE.CM-3, DE.AE-3)*
- Cloud audit logging (e.g., AWS CloudTrail, Azure Monitor, GCP Audit Logs) must be enabled for all services
- Logs must be retained for a minimum of 90 days in cloud (1 year in aggregate)
- Logs must be exported to a centralized, tamper-evident log management system
- Alerts must be configured for: unauthorized access attempts, privilege escalation, public exposure of resources, large data transfers, and configuration changes to security controls
- Log alerts must be reviewed within 24 hours

### 5.12 Cloud Security Incident Response *(NIST CSF: RS.RP-1, RS.CO-2)*
- Cloud security incidents follow the [Company Name] Incident Response Policy
- Cloud provider security advisories must be reviewed weekly by [IT Contact]
- Credentials suspected of compromise must be rotated within 1 hour
- Exposed Restricted data in cloud storage must trigger immediate notification to [Security Officer] and follow the Data Breach Response Policy

## Compliance and Monitoring *(NIST CSF: DE.CM-7, ID.GV-3)*
- Quarterly cloud security posture review using CSPM tooling
- Annual third-party review of cloud configurations for Critical services
- Monthly review of identity and access management (IAM) policies and role assignments
- Cloud security metrics must be included in the security KPI dashboard

## Enforcement
Using unapproved cloud services, misconfiguring cloud security controls, or exposing company data in cloud storage without authorization are serious policy violations. Violations must be reported to [Security Officer] and may result in disciplinary action and service suspension.

## References
- NIST CSF v1.1: ID.AM, PR.AC, PR.DS, DE.CM
- NIST SP 800-144: Guidelines on Security and Privacy in Public Cloud Computing
- NIST SP 800-190: Application Container Security Guide
- CIS Benchmarks for AWS, Azure, GCP (as applicable)

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Security Officer] | Initial release |
