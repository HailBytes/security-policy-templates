# Wireless Communication Policy

**NIST CSF Functions: Protect (PR), Detect (DE)**

## Purpose
To establish security requirements for wireless networks and devices to protect against unauthorized access and ensure secure wireless communications.

## Scope
Applies to all wireless networks, access points, and wireless-enabled devices used for business purposes.

## Wireless Network Security *(NIST CSF: PR.AC-3, PR.DS-2)*

### 10.1 Network Authentication and Encryption
- Implement WPA3 encryption (WPA2 minimum acceptable)
- Use enterprise authentication (802.1X) for business networks
- Configure strong pre-shared keys (minimum 20 characters) for small networks
- Disable WPS (Wi-Fi Protected Setup) functionality
- Implement certificate-based authentication where possible

### 10.2 Network Segmentation *(NIST CSF: PR.AC-5, PR.DS-7)*
- Separate guest networks from business networks
- Isolate IoT and personal devices on dedicated networks
- Implement network access control (NAC) for device authentication
- Configure firewall rules between wireless network segments
- Monitor inter-network communications

## Access Point Configuration *(NIST CSF: PR.PT-1, PR.IP-1)*

### 10.3 Secure Configuration
- Change default administrative credentials immediately
- Disable SSID broadcasting for internal business networks
- Configure automatic firmware updates where supported
- Enable MAC address filtering for high-security networks
- Position access points to minimize signal outside business premises

### 10.4 Access Point Management *(NIST CSF: PR.AC-1, PR.MA-2)*
- Use centralized wireless management systems
- Implement role-based administration
- Enable encrypted management protocols (HTTPS, SSH)
- Configure automatic session timeouts for administrative access
- Maintain inventory of all wireless access points

## Device Security *(NIST CSF: PR.AC-1, PR.DS-1)*

### 10.5 Personal Device Usage (BYOD)
- Require device registration and approval
- Implement mobile device management (MDM) solutions
- Enforce device encryption for business data access
- Configure automatic screen locks and remote wipe capabilities
- Separate business data from personal data

### 10.6 Corporate Device Management
- Install and maintain endpoint security software
- Configure automatic security updates
- Implement certificate-based network authentication
- Monitor device compliance with security policies
- Maintain device inventory and ownership records

## Monitoring and Detection *(NIST CSF: DE.CM-1, DE.AE-1)*

### 10.7 Wireless Security Monitoring
- Implement wireless intrusion detection systems (WIDS)
- Monitor for rogue access points and unauthorized devices
- Scan for weak encryption and security misconfigurations
- Detect wireless network attacks and anomalies
- Log and analyze wireless network traffic patterns

### 10.8 Incident Response *(NIST CSF: DE.AE-2, RS.RP-1)*
- Establish procedures for wireless security incidents
- Quarantine suspicious devices immediately
- Investigate unauthorized network access attempts
- Document security events and response actions
- Update security configurations based on incident findings

## Guest Network Management *(NIST CSF: PR.AC-4, PR.AC-6)*

### 10.9 Guest Access Controls
- Implement time-limited guest access credentials
- Require guest registration and acknowledgment of terms
- Isolate guest traffic from business networks
- Monitor guest network usage and bandwidth
- Provide guest access documentation and support

## Compliance and Auditing *(NIST CSF: PR.IP-3, DE.CM-8)*

### 10.10 Wireless Security Assessment
- Conduct quarterly wireless security assessments
- Perform annual penetration testing of wireless networks
- Audit device compliance with security policies
- Review and update wireless security configurations
- Document assessment findings and remediation actions

## References
- NIST CSF v1.1: PR.AC (Access Control), PR.DS (Data Security), PR.PT (Protective Technology), DE.CM (Security Continuous Monitoring)