# Ransomware Response Policy

**NIST CSF Functions: Protect (PR), Detect (DE), Respond (RS), Recover (RC)**

## Purpose

To establish specific procedures for detecting, containing, and recovering from ransomware attacks, minimizing data loss and downtime, and ensuring [Company Name] meets cyber liability insurance requirements for ransomware preparedness.

## Scope

Applies to all systems, endpoints, servers, and cloud environments operated by [Company Name]. All employees, contractors, and vendors with system access are subject to this policy.

## Ransomware Prevention Controls *(NIST CSF: PR.AC-4, PR.DS-1, PR.IP-12)*

### 3.1 Backup Architecture

- Maintain at least three backup copies following the 3-2-1 rule: three copies, two different media types, one offsite or air-gapped
- Test backup restoration monthly; document results and store test logs for auditors
- Isolate backup systems from production networks so ransomware cannot encrypt backup targets
- Store immutable backups for a minimum of 30 days

### 3.2 Access Hardening

- Enforce least-privilege access; no user account should have write access to systems outside their job function
- Disable SMBv1, RDP on internet-facing systems, and unused admin shares
- Require multi-factor authentication for all remote access, VPN, and privileged accounts
- Segment networks to limit lateral movement: endpoints, servers, OT/IoT, and guest should be on separate VLANs

### 3.3 Detection Tuning *(NIST CSF: DE.CM-1, DE.CM-4)*

- Deploy endpoint detection and response (EDR) on all managed endpoints
- Alert on mass file rename events, volume shadow copy deletion (`vssadmin delete shadows`), and unexpected encryption activity
- Monitor DNS for known ransomware command-and-control (C2) domains via threat intelligence feeds
- Review Windows event logs for suspicious use of `wmic`, `PsExec`, and `certutil`

## Incident Response Procedures

### 4.1 Detection and Initial Triage *(NIST CSF: DE.AE-1, DE.AE-2, RS.AN-1)*

**Immediate Actions (0–30 minutes):**

- Employee who discovers encrypted files or ransom note contacts [IT Contact] immediately; do not pay any ransom or interact with attacker portal without legal authorization
- [IT Contact] confirms the incident is ransomware (look for encrypted file extensions, ransom notes, disabled shadow copies)
- Notify [Security Officer] and activate the Incident Response Team per the Security Response Plan Policy
- Record the exact time of discovery and the first affected system

### 4.2 Containment *(NIST CSF: RS.RP-1, RS.MI-1, RS.MI-2)*

**Network Isolation (0–1 hour):**

- Immediately disconnect affected systems from the network at the switch port or firewall level — do NOT simply power off (preserves volatile memory for forensics)
- Identify the patient-zero system by reviewing EDR telemetry and Windows event logs for earliest encryption timestamps
- Block all outbound traffic from affected VLANs at the perimeter firewall
- Revoke or rotate all service account credentials and shared passwords that existed on affected systems
- Notify cloud service providers if any cloud-synced drives (SharePoint, OneDrive, Google Drive) may have propagated encrypted files; pause sync immediately

**Scope Assessment (1–4 hours):**

- Enumerate all affected endpoints, servers, and shared drives
- Determine the ransomware variant using file extension lookup or services such as ID Ransomware
- Identify the initial attack vector: phishing email, exposed RDP, compromised VPN credential, or vulnerable software
- Assess whether data exfiltration occurred prior to encryption (double-extortion model); check firewall egress logs for large outbound transfers

### 4.3 Notification Requirements *(NIST CSF: RS.CO-2, RS.CO-3)*

**Immediate internal notifications:**

- [Security Officer] notifies [Title/Role] (executive sponsor) within 2 hours of confirmed incident
- [Legal Counsel – Contact Info] assessed for mandatory regulatory reporting obligations (breach notification laws, SEC, HIPAA, PCI DSS as applicable)
- Cyber liability insurer contacted within 24 hours — most policies require prompt notification and pre-authorize ransom decisions; failure to notify may void coverage

**External notifications (as required):**

- Regulatory authorities notified within legally required timeframes (72 hours under GDPR; varies by US state)
- Affected customers or partners notified once scope is confirmed and legal counsel approves messaging
- Law enforcement (FBI IC3 or local equivalent) — reporting does not obligate specific action and provides access to decryptors when available

### 4.4 Ransom Decision Framework *(NIST CSF: RS.AN-4)*

Paying a ransom is a legal and business decision, not a technical one. The following criteria guide evaluation:

| Factor | Consider Payment | Avoid Payment |
|--------|-----------------|---------------|
| Backup availability | Clean backups unavailable or corrupted | Clean backups confirmed restorable |
| Data criticality | Life-safety or irreplaceable data at risk | Data is reproducible or non-critical |
| Decryptor availability | No public decryptor exists | Free decryptor available (check NoMoreRansom.org) |
| Legal restrictions | Legal counsel confirms payment is permissible | Attacker group is OFAC-sanctioned |
| Insurer guidance | Insurer recommends and covers payment | Insurer recommends against payment |

**Decision authority**: [Title/Role] (executive sponsor), with mandatory legal counsel sign-off. [Security Officer] documents the decision rationale regardless of outcome.

### 4.5 Eradication and Recovery *(NIST CSF: RC.RP-1, RC.RP-2, RC.IM-1)*

**Eradication (before any restoration):**

- Rebuild affected systems from known-clean OS images — do not attempt to clean infected systems in place
- Remove all attacker persistence mechanisms: scheduled tasks, registry run keys, new user accounts, modified startup scripts
- Patch the vulnerability used as the initial attack vector before any system returns to production
- Reset all credentials that existed on compromised systems, including service accounts and shared passwords

**Staged recovery:**

1. Restore and validate critical infrastructure first (domain controllers, identity providers, core network services)
2. Restore servers and shared storage from the most recent pre-attack immutable backup
3. Restore endpoints only after network defenses are confirmed clean
4. Reintroduce cloud sync after verifying no encrypted files remain in backup snapshots
5. Monitor restored systems continuously for 72 hours before declaring full recovery

**Validation checklist before returning systems to production:**

- [ ] No ransomware indicators of compromise (IoCs) detected by EDR
- [ ] All credentials rotated
- [ ] Vulnerable software patched or mitigated
- [ ] Backup integrity confirmed for future recovery
- [ ] Logging and alerting verified operational

## Compliance and Enforcement *(NIST CSF: GV.PO-1)*

[Company Name] employees who fail to report suspected ransomware activity promptly, or who independently attempt to negotiate with attackers, may face disciplinary action up to and including termination. Deliberate interference with containment or recovery efforts will be treated as a serious policy violation.

All personnel with privileged access must complete ransomware awareness training annually, including tabletop exercises simulating a ransomware event.

## Post-Incident Review *(NIST CSF: RC.IM-2)*

A post-incident review must be completed within 14 days of recovery using the Post-Incident Review Template. At minimum, the review must cover:

- Root cause and initial attack vector
- Timeline of detection, containment, and recovery
- Effectiveness of backups and recovery procedures
- Changes to controls, procedures, or training required
- Cyber insurance claim documentation

Results are reported to [Title/Role] and retained for a minimum of three years.

## References

- NIST CSF 2.0: PR.AC, PR.DS, DE.CM, DE.AE, RS.RP, RS.AN, RS.MI, RS.CO, RC.RP, RC.IM, GV.PO
- NIST SP 800-184: Guide for Cybersecurity Event Recovery
- CISA Ransomware Guide (stopransomware.gov)
- NoMoreRansom.org: Free decryptors for known ransomware variants
- FBI IC3 Ransomware Reporting: ic3.gov
- Related policies: Security Response Plan Policy, Data Breach Response Policy, Disaster Recovery Plan Policy, Cloud Security Policy

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Security Officer] | Initial release |
