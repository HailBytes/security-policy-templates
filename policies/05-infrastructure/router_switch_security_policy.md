# Router and Switch Security Policy

**NIST CSF Functions: Protect (PR), Detect (DE)**

## Purpose
To establish security requirements for network infrastructure devices to protect against unauthorized access and ensure network integrity.

## Scope
Applies to all routers, switches, and network infrastructure devices in company facilities and remote locations.

## Access Control *(NIST CSF: PR.AC-1, PR.AC-3)*

### 9.1 Administrative Access
- Change all default usernames and passwords immediately
- Use role-based access with principle of least privilege
- Implement strong authentication (minimum 15-character passwords)
- Enable multi-factor authentication where supported
- Maintain current list of authorized administrators

### 9.2 Remote Access *(NIST CSF: PR.AC-4, PR.MA-2)*
- Disable unused remote access protocols (Telnet, HTTP)
- Use encrypted protocols only (SSH, HTTPS, SNMP v3)
- Implement VPN access for remote management
- Configure source IP restrictions for management access
- Enable automatic session timeouts (15 minutes maximum)

## Configuration Security *(NIST CSF: PR.IP-1, PR.PT-1)*

### 9.3 Secure Configuration Standards
- Disable unnecessary services and protocols
- Configure secure management protocols only
- Implement network access control lists (ACLs)
- Enable encryption for all management traffic
- Configure NTP for accurate time synchronization

### 9.4 VLAN and Network Segmentation *(NIST CSF: PR.AC-5, PR.DS-7)*
- Segment networks by function and security requirements
- Isolate management networks from user networks
- Configure inter-VLAN routing restrictions
- Implement network access control for device connections
- Document network topology and VLAN assignments

## Monitoring and Logging *(NIST CSF: DE.CM-1, DE.CM-3)*

### 9.5 Security Monitoring
- Enable comprehensive logging of administrative actions
- Configure SNMP monitoring with secure community strings
- Implement network flow monitoring and analysis
- Set up alerting for unauthorized configuration changes
- Monitor for unusual network traffic patterns

### 9.6 Log Management *(NIST CSF: DE.AE-3, PR.PT-1)*
- Forward logs to centralized logging system
- Retain logs for minimum 90 days
- Protect log integrity with secure storage
- Review logs regularly for security events
- Correlate network events with security incidents

## Physical Security *(NIST CSF: PR.AC-2, PR.DS-8)*

### 9.7 Physical Protection
- Install network equipment in locked, secure locations
- Implement environmental controls (temperature, humidity)
- Restrict physical access to authorized personnel only
- Secure console ports and unused network ports
- Use cable locks and security enclosures where appropriate

## Maintenance and Updates *(NIST CSF: PR.MA-1, PR.IP-12)*

### 9.8 Patch Management
- Maintain current firmware versions on all devices
- Test updates in non-production environment first
- Schedule maintenance windows for critical updates
- Document configuration changes and rollback procedures
- Verify security configurations after updates

### 9.9 Configuration Management *(NIST CSF: PR.IP-4, PR.IP-6)*
- Backup configurations before making changes
- Use configuration management tools where possible
- Document all configuration changes with approval
- Implement change control procedures
- Regularly verify configurations against baselines

## Incident Response *(NIST CSF: DE.AE-1, RS.RP-1)*

### 9.10 Network Security Incidents
- Monitor for indicators of compromise on network devices
- Isolate compromised devices immediately
- Preserve evidence for incident analysis
- Implement emergency access procedures if needed
- Update security configurations based on incident findings

## References
- NIST CSF v1.1: PR.AC (Access Control), PR.PT (Protective Technology), DE.CM (Security Continuous Monitoring)