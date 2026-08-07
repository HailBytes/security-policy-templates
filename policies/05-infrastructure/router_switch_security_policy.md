# Router and Switch Security Policy

**NIST CSF Functions: Protect (PR), Detect (DE)**

## Purpose
To establish security requirements for network infrastructure devices to protect against unauthorized access and ensure network integrity.

## Scope
Applies to all routers, switches, and network infrastructure devices in company facilities and remote locations.

## Access Control *(NIST CSF: PR.AA-01, PR.AA-03)*

### 9.1 Administrative Access
- Change all default usernames and passwords immediately
- Use role-based access with principle of least privilege
- Implement strong authentication (minimum 15-character passwords)
- Enable multi-factor authentication where supported
- Maintain current list of authorized administrators

### 9.2 Remote Access *(NIST CSF: PR.AA-05, PR.PS-02)*
- Disable unused remote access protocols (Telnet, HTTP)
- Use encrypted protocols only (SSH, HTTPS, SNMP v3)
- Implement VPN access for remote management
- Configure source IP restrictions for management access
- Enable automatic session timeouts (15 minutes maximum)

## Configuration Security *(NIST CSF: PR.PS-01, PR.PS-04)*

### 9.3 Secure Configuration Standards
- Disable unnecessary services and protocols
- Configure secure management protocols only
- Implement network access control lists (ACLs)
- Enable encryption for all management traffic
- Configure NTP for accurate time synchronization

### 9.4 VLAN and Network Segmentation *(NIST CSF: PR.IR-01, PR.DS-07)*
- Segment networks by function and security requirements
- Isolate management networks from user networks
- Configure inter-VLAN routing restrictions
- Implement network access control for device connections
- Document network topology and VLAN assignments

## Monitoring and Logging *(NIST CSF: DE.CM-01, DE.CM-01)*

### 9.5 Security Monitoring
- Enable comprehensive logging of administrative actions
- Configure SNMP monitoring with secure community strings
- Implement network flow monitoring and analysis
- Set up alerting for unauthorized configuration changes
- Monitor for unusual network traffic patterns

### 9.6 Log Management *(NIST CSF: DE.AE-03, PR.PS-04)*
- Forward logs to centralized logging system
- Retain logs for minimum 90 days
- Protect log integrity with secure storage
- Review logs regularly for security events
- Correlate network events with security incidents

## Physical Security *(NIST CSF: PR.AA-06, PR.DS-08)*

### 9.7 Physical Protection
- Install network equipment in locked, secure locations
- Implement environmental controls (temperature, humidity)
- Restrict physical access to authorized personnel only
- Secure console ports and unused network ports
- Use cable locks and security enclosures where appropriate

## Maintenance and Updates *(NIST CSF: PR.PS-03, ID.RA-01)*

### 9.8 Patch Management
- Maintain current firmware versions on all devices
- Test updates in non-production environment first
- Schedule maintenance windows for critical updates
- Document configuration changes and rollback procedures
- Verify security configurations after updates

### 9.9 Configuration Management *(NIST CSF: PR.DS-11, PR.DS-09)*
- Backup configurations before making changes
- Use configuration management tools where possible
- Document all configuration changes with approval
- Implement change control procedures
- Regularly verify configurations against baselines

## Incident Response *(NIST CSF: DE.AE-01, RS.MA-01)*

### 9.10 Network Security Incidents
- Monitor for indicators of compromise on network devices
- Isolate compromised devices immediately
- Preserve evidence for incident analysis
- Implement emergency access procedures if needed
- Update security configurations based on incident findings

## Enforcement
Unauthorized modification of network device configurations, disabling required security controls, or failure to apply firmware updates within defined timelines are policy violations. Violations must be escalated to [Security Officer] and may result in device isolation, service suspension, and disciplinary action up to and including termination.

## References
- NIST CSF 2.0: PR.AA (Access Control), PR.PS (Protective Technology), DE.CM (Security Continuous Monitoring)

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Security Officer] | Initial release |