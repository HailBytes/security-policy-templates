# Incident Response Checklist

**NIST CSF Functions: Detect (DE), Respond (RS), Recover (RC)**

---

## Incident Information

**Incident ID:** ___________  
**Date/Time Discovered:** ___________  
**Incident Commander:** ___________  
**Discovery Method:** ☐ Automated Alert ☐ User Report ☐ External Notification ☐ Other  
**Initial Severity:** ☐ Critical ☐ High ☐ Medium ☐ Low

---

## Phase 1: Immediate Response (0-1 Hours) *(NIST CSF: DE.AE-1, RS.RP-1)*

### Initial Detection and Assessment *(NIST CSF: DE.AE-2)*
☐ **Incident discovered and documented**  
   - Time: ___________  
   - Discoverer: ___________  
   - Initial description: ___________

☐ **Incident Commander notified**  
   - Time: ___________  
   - Method: ☐ Phone ☐ Email ☐ Pager ☐ In-person  
   - Response time: ___________ (Target: 15 minutes)

☐ **Initial incident classification completed**  
   - Incident type: ☐ Malware ☐ Phishing ☐ Data Breach ☐ Unauthorized Access ☐ System Outage ☐ Other  
   - Affected systems: ___________  
   - Estimated scope: ___________

☐ **Core response team assembled** *(NIST CSF: RS.CO-1)*  
   - Incident Commander: ☐ Notified ☐ On-site ☐ Remote  
   - Security Analyst: ☐ Notified ☐ On-site ☐ Remote  
   - IT Operations: ☐ Notified ☐ On-site ☐ Remote  
   - Business Representative: ☐ Notified ☐ On-site ☐ Remote

### Immediate Containment *(NIST CSF: RS.MI-2)*
☐ **Prevent further damage**  
   - ☐ Isolate affected systems from network  
   - ☐ Disable compromised user accounts  
   - ☐ Block malicious IP addresses/domains  
   - ☐ Quarantine malicious files/emails

☐ **Preserve evidence** *(NIST CSF: RS.AN-1)*  
   - ☐ Take screenshots of current system state  
   - ☐ Preserve system logs before they rotate  
   - ☐ Document all actions taken with timestamps  
   - ☐ Avoid powering down systems unless necessary

☐ **Establish secure communication**  
   - ☐ Set up secure communication channel for team  
   - ☐ Create incident war room (physical or virtual)  
   - ☐ Establish regular update schedule (every hour initially)

---

## Phase 2: Short-term Response (1-4 Hours) *(NIST CSF: RS.AN-2)*

### Detailed Analysis and Investigation *(NIST CSF: RS.AN-1)*
☐ **Comprehensive system analysis**  
   - ☐ Identify attack vector and entry point  
   - ☐ Determine scope of compromise  
   - ☐ Assess data potentially affected  
   - ☐ Identify indicators of compromise (IoCs)

☐ **Evidence collection and preservation**  
   - ☐ Create forensic images of affected systems  
   - ☐ Collect and preserve system logs  
   - ☐ Document network traffic captures  
   - ☐ Preserve email evidence if applicable

☐ **Impact assessment** *(NIST CSF: RS.AN-3)*  
   - Business impact: ☐ None ☐ Minor ☐ Moderate ☐ Significant ☐ Severe  
   - Data impact: ☐ None ☐ Internal ☐ Confidential ☐ Restricted  
   - Estimated records affected: ___________  
   - Estimated financial impact: $___________

### Extended Team Activation
☐ **Notify extended team members**  
   - Legal Counsel: ☐ Notified Time: ___________  
   - HR Representative: ☐ Notified Time: ___________  
   - Communications Lead: ☐ Notified Time: ___________  
   - External Consultant: ☐ Notified Time: ___________

☐ **Escalate to senior management**  
   - CIO/CISO: ☐ Notified Time: ___________  
   - CEO: ☐ Notified Time: ___________  
   - Legal: ☐ Notified Time: ___________  
   - Board (if required): ☐ Notified Time: ___________

### Enhanced Containment *(NIST CSF: RS.MI-3)*
☐ **Implement additional security controls**  
   - ☐ Apply emergency firewall rules  
   - ☐ Enhance monitoring on critical systems  
   - ☐ Implement additional access controls  
   - ☐ Deploy additional security tools

☐ **Search for lateral movement**  
   - ☐ Scan for suspicious activity on other systems  
   - ☐ Review authentication logs for compromised accounts  
   - ☐ Check for privilege escalation attempts  
   - ☐ Monitor for data exfiltration activities

---

## Phase 3: Investigation and Analysis (4-24 Hours) *(NIST CSF: RS.AN-2)*

### Comprehensive Forensic Analysis
☐ **Deep forensic investigation**  
   - ☐ Analyze forensic images for evidence  
   - ☐ Reconstruct attack timeline  
   - ☐ Identify all affected systems and data  
   - ☐ Determine persistence mechanisms

☐ **Malware analysis** (if applicable)  
   - ☐ Isolate and analyze malware samples  
   - ☐ Determine malware capabilities and intent  
   - ☐ Identify command and control infrastructure  
   - ☐ Create detection signatures

☐ **Root cause analysis** *(NIST CSF: RS.AN-4)*  
   - ☐ Identify how the incident occurred  
   - ☐ Determine security control failures  
   - ☐ Assess human factors involved  
   - ☐ Document lessons learned

### Threat Intelligence and Attribution
☐ **Threat intelligence analysis**  
   - ☐ Research known threat actors and campaigns  
   - ☐ Correlate with external threat intelligence  
   - ☐ Identify tactics, techniques, and procedures (TTPs)  
   - ☐ Assess likelihood of future attacks

☐ **Share threat intelligence**  
   - ☐ Share IoCs with industry partners  
   - ☐ Report to relevant authorities (if required)  
   - ☐ Update threat intelligence platforms  
   - ☐ Inform vendors and security community

### Notification and Communication *(NIST CSF: RS.CO-2)*
☐ **Internal communications**  
   - ☐ Regular updates to executive team  
   - ☐ Employee communications (if needed)  
   - ☐ Department-specific briefings  
   - ☐ Board notification (if required)

☐ **External notifications** *(NIST CSF: RS.CO-3)*  
   - ☐ Customer notifications (if required)  
   - ☐ Partner/vendor notifications  
   - ☐ Regulatory notifications (within required timeframes)  
   - ☐ Law enforcement (if criminal activity suspected)

☐ **Media and public relations** (if required)  
   - ☐ Prepare public statements  
   - ☐ Coordinate with PR team/agency  
   - ☐ Monitor social media and news coverage  
   - ☐ Respond to media inquiries

---

## Phase 4: Eradication and Recovery (24-72 Hours) *(NIST CSF: RC.RP-1)*

### Eradication Activities *(NIST CSF: RS.MI-3)*
☐ **Remove threat presence**  
   - ☐ Remove malware from all infected systems  
   - ☐ Close all unauthorized access points  
   - ☐ Revoke compromised credentials  
   - ☐ Patch vulnerabilities that enabled the attack

☐ **Strengthen security controls**  
   - ☐ Update security configurations  
   - ☐ Deploy additional monitoring  
   - ☐ Implement enhanced access controls  
   - ☐ Update security policies and procedures

☐ **Validate eradication**  
   - ☐ Conduct thorough security scans  
   - ☐ Verify no remaining threat presence  
   - ☐ Test security controls effectiveness  
   - ☐ Confirm system integrity

### Recovery Planning *(NIST CSF: RC.RP-1)*
☐ **Develop recovery strategy**  
   - ☐ Prioritize systems for recovery  
   - ☐ Plan recovery sequence and dependencies  
   - ☐ Establish recovery criteria and validation  
   - ☐ Coordinate with business stakeholders

☐ **Backup and restore operations**  
   - ☐ Identify clean backup sources  
   - ☐ Verify backup integrity  
   - ☐ Restore systems from clean backups  
   - ☐ Test restored systems functionality

☐ **System restoration and validation** *(NIST CSF: RC.RP-1)*  
   - ☐ Restore systems to production  
   - ☐ Validate business functionality  
   - ☐ Confirm security controls are active  
   - ☐ Monitor for signs of reinfection

### Enhanced Monitoring *(NIST CSF: RC.CO-1)*
☐ **Implement enhanced monitoring**  
   - ☐ Deploy additional monitoring tools  
   - ☐ Increase log collection and analysis  
   - ☐ Monitor for similar attack indicators  
   - ☐ Establish ongoing threat hunting activities

---

## Phase 5: Post-Incident Activities (72+ Hours) *(NIST CSF: RC.IM-1)*

### Return to Normal Operations *(NIST CSF: RC.CO-3)*
☐ **Gradual service restoration**  
   - ☐ Restore systems in planned sequence  
   - ☐ Monitor system performance and stability  
   - ☐ Validate business process functionality  
   - ☐ Communicate restoration status to stakeholders

☐ **User access restoration**  
   - ☐ Restore user accounts and access  
   - ☐ Reset passwords where required  
   - ☐ Validate user authentication systems  
   - ☐ Provide user training on any changes

☐ **Business continuity validation**  
   - ☐ Confirm all business processes operational  
   - ☐ Validate data integrity and completeness  
   - ☐ Test disaster recovery capabilities  
   - ☐ Update business continuity plans

### Post-Incident Review *(NIST CSF: RC.IM-2)*
☐ **Conduct lessons learned session**  
   - ☐ Schedule review meeting with all stakeholders  
   - ☐ Document what worked well  
   - ☐ Identify areas for improvement  
   - ☐ Create action plan for improvements

☐ **Update policies and procedures**  
   - ☐ Revise incident response procedures  
   - ☐ Update security policies based on lessons learned  
   - ☐ Enhance monitoring and detection capabilities  
   - ☐ Improve security controls and configurations

☐ **Training and awareness updates**  
   - ☐ Update security training materials  
   - ☐ Conduct additional training for staff  
   - ☐ Share lessons learned with organization  
   - ☐ Update tabletop exercise scenarios

### Legal and Compliance Follow-up
☐ **Legal documentation**  
   - ☐ Preserve evidence for potential legal action  
   - ☐ Document chain of custody for evidence  
   - ☐ Coordinate with law enforcement (if involved)  
   - ☐ Prepare for potential litigation

☐ **Regulatory compliance**  
   - ☐ Complete required regulatory filings  
   - ☐ Respond to regulatory inquiries  
   - ☐ Document compliance efforts  
   - ☐ Plan for potential audits or investigations

☐ **Insurance claims**  
   - ☐ Notify cyber insurance carrier  
   - ☐ Document all incident costs  
   - ☐ Provide required documentation  
   - ☐ Coordinate with insurance adjusters

---

## Incident Metrics and Tracking *(NIST CSF: DE.CM-8)*

### Response Time Metrics
- **Time to Detection:** ___________ (Discovery to confirmation)  
- **Time to Response:** ___________ (Detection to team assembly)  
- **Time to Containment:** ___________ (Response to initial containment)  
- **Time to Recovery:** ___________ (Containment to normal operations)

### Impact Metrics
- **Systems Affected:** ___________  
- **Users Impacted:** ___________  
- **Downtime Duration:** ___________  
- **Data Records Affected:** ___________  
- **Financial Impact:** $___________

### Response Effectiveness Metrics
- **Detection Method:** ☐ Automated ☐ Manual ☐ External ☐ User Report  
- **Containment Success:** ☐ Excellent ☐ Good ☐ Fair ☐ Poor  
- **Communication Effectiveness:** ☐ Excellent ☐ Good ☐ Fair ☐ Poor  
- **Recovery Success:** ☐ Excellent ☐ Good ☐ Fair ☐ Poor

---

## Communication Log *(NIST CSF: RS.CO-2)*

### Internal Communications
| Time | Recipient | Method | Message Summary | Response |
|------|-----------|---------|-----------------|----------|
| [TIME] | [NAME/ROLE] | [EMAIL/PHONE/IN-PERSON] | [MESSAGE] | [RESPONSE] |
| [TIME] | [NAME/ROLE] | [EMAIL/PHONE/IN-PERSON] | [MESSAGE] | [RESPONSE] |

### External Communications
| Time | Recipient | Method | Message Summary | Response |
|------|-----------|---------|-----------------|----------|
| [TIME] | [ORGANIZATION] | [EMAIL/PHONE/LETTER] | [MESSAGE] | [RESPONSE] |
| [TIME] | [ORGANIZATION] | [EMAIL/PHONE/LETTER] | [MESSAGE] | [RESPONSE] |

---

## Evidence Log *(NIST CSF: RS.AN-1)*

### Digital Evidence Collected
| Item | Type | Collection Time | Collected By | Storage Location | Chain of Custody |
|------|------|----------------|--------------|------------------|------------------|
| [ITEM ID] | [TYPE] | [TIME] | [NAME] | [LOCATION] | [SIGNATURE] |
| [ITEM ID] | [TYPE] | [TIME] | [NAME] | [LOCATION] | [SIGNATURE] |

### Physical Evidence Collected
| Item | Description | Collection Time | Collected By | Storage Location | Chain of Custody |
|------|-------------|----------------|--------------|------------------|------------------|
| [ITEM ID] | [DESCRIPTION] | [TIME] | [NAME] | [LOCATION] | [SIGNATURE] |

---

## Action Items and Follow-up *(NIST CSF: RC.IM-2)*

### Immediate Actions (0-7 Days)
| Action | Owner | Due Date | Status | Notes |
|--------|-------|----------|---------|-------|
| [ACTION DESCRIPTION] | [NAME] | [DATE] | [STATUS] | [NOTES] |
| [ACTION DESCRIPTION] | [NAME] | [DATE] | [STATUS] | [NOTES] |

### Short-term Actions (7-30 Days)
| Action | Owner | Due Date | Status | Notes |
|--------|-------|----------|---------|-------|
| [ACTION DESCRIPTION] | [NAME] | [DATE] | [STATUS] | [NOTES] |
| [ACTION DESCRIPTION] | [NAME] | [DATE] | [STATUS] | [NOTES] |

### Long-term Actions (30+ Days)
| Action | Owner | Due Date | Status | Notes |
|--------|-------|----------|---------|-------|
| [ACTION DESCRIPTION] | [NAME] | [DATE] | [STATUS] | [NOTES] |
| [ACTION DESCRIPTION] | [NAME] | [DATE] | [STATUS] | [NOTES] |

---

## Vendor and Third-Party Coordination *(NIST CSF: ID.SC-4)*

### Vendor Notifications
☐ **Critical vendors notified**  
   - Cloud service providers: ☐ Notified Time: ___________  
   - Managed service providers: ☐ Notified Time: ___________  
   - Security vendors: ☐ Notified Time: ___________  
   - Business partners: ☐ Notified Time: ___________

☐ **Vendor support engaged**  
   - Technical support tickets opened: ___________  
   - Emergency response services activated: ___________  
   - Forensic services engaged: ___________  
   - Legal counsel engaged: ___________

### External Expert Assistance
☐ **Incident response services**  
   - External IR team: ☐ Engaged ☐ Not needed  
   - Forensic experts: ☐ Engaged ☐ Not needed  
   - Legal counsel: ☐ Engaged ☐ Not needed  
   - Public relations: ☐ Engaged ☐ Not needed

---

## Regulatory and Legal Checklist *(NIST CSF: RS.CO-3)*

### Notification Requirements Assessment
☐ **Determine notification obligations**  
   - Data breach notification laws: ☐ Apply ☐ Do not apply  
   - Industry regulations: ☐ Apply ☐ Do not apply  
   - Contractual obligations: ☐ Apply ☐ Do not apply  
   - International requirements: ☐ Apply ☐ Do not apply

### Required Notifications
☐ **Regulatory authorities**  
   - [Authority 1]: ☐ Required ☐ Not required ☐ Completed Time: ___________  
   - [Authority 2]: ☐ Required ☐ Not required ☐ Completed Time: ___________

☐ **Affected individuals**  
   - Notification required: ☐ Yes ☐ No  
   - Number of individuals: ___________  
   - Notification method: ☐ Email ☐ Mail ☐ Phone ☐ Website  
   - Notification completed: ☐ Yes ☐ No Time: ___________

☐ **Business partners**  
   - Customer notifications: ☐ Required ☐ Completed Time: ___________  
   - Partner notifications: ☐ Required ☐ Completed Time: ___________  
   - Vendor notifications: ☐ Required ☐ Completed Time: ___________

### Legal Documentation
☐ **Legal hold implemented**  
   - Relevant documents preserved: ☐ Yes ☐ No  
   - Email preservation: ☐ Yes ☐ No  
   - System logs preserved: ☐ Yes ☐ No  
   - Legal counsel consulted: ☐ Yes ☐ No

---

## Cost Tracking and Financial Impact

### Direct Costs
- **Staff overtime costs:** $___________  
- **External consultant fees:** $___________  
- **Technology and tool costs:** $___________  
- **Legal and regulatory costs:** $___________  
- **Communication and notification costs:** $___________

### Indirect Costs
- **Business disruption costs:** $___________  
- **Lost productivity:** $___________  
- **Customer impact and potential losses:** $___________  
- **Reputation and brand impact:** $___________

### Recovery Costs
- **System restoration costs:** $___________  
- **Data recovery costs:** $___________  
- **Additional security measures:** $___________  
- **Training and awareness costs:** $___________

**Total Estimated Cost:** $___________

---

## Incident Closure *(NIST CSF: RC.IM-1)*

### Closure Criteria Assessment
☐ **All affected systems restored to normal operation**  
☐ **Security vulnerabilities patched or mitigated**  
☐ **Enhanced monitoring implemented**  
☐ **All required notifications completed**  
☐ **Evidence properly preserved and documented**  
☐ **Post-incident review completed**

### Final Status
**Incident Status:** ☐ Resolved ☐ Ongoing ☐ Monitoring  
**Business Impact:** ☐ Resolved ☐ Ongoing impacts  
**Security Posture:** ☐ Improved ☐ Restored ☐ Enhanced monitoring

### Sign-off
**Incident Commander:** ___________________ Date: ___________  
**IT Security Manager:** ___________________ Date: ___________  
**Business Representative:** ___________________ Date: ___________  
**Executive Sponsor:** ___________________ Date: ___________

---

## Special Considerations by Incident Type

### Data Breach Specific Checklist *(NIST CSF: RS.CO-3)*
☐ **Identify data types affected**  
   - Personal information (PII): ☐ Yes ☐ No  
   - Financial information: ☐ Yes ☐ No  
   - Health information (PHI): ☐ Yes ☐ No  
   - Intellectual property: ☐ Yes ☐ No

☐ **Assess regulatory requirements**  
   - GDPR applicability: ☐ Yes ☐ No  
   - HIPAA requirements: ☐ Yes ☐ No  
   - State breach laws: ☐ Yes ☐ No  
   - Industry regulations: ☐ Yes ☐ No

☐ **Implement breach-specific response**  
   - Credit monitoring services: ☐ Required ☐ Not required  
   - Identity protection services: ☐ Required ☐ Not required  
   - Call center setup: ☐ Required ☐ Not required

### Ransomware Specific Checklist *(NIST CSF: RS.MI-2)*
☐ **Ransomware response actions**  
   - Isolate infected systems immediately: ☐ Completed  
   - Identify ransomware variant: ☐ Completed  
   - Assess backup integrity: ☐ Completed  
   - Contact law enforcement: ☐ Yes ☐ No ☐ Completed

☐ **Recovery decisions**  
   - Restore from backups: ☐ Possible ☐ Not possible  
   - Payment consideration: ☐ Authorized ☐ Not authorized  
   - Alternative recovery methods: ☐ Available ☐ Not available

### Malware Incident Checklist *(NIST CSF: RS.AN-1)*
☐ **Malware analysis**  
   - Malware samples collected: ☐ Yes ☐ No  
   - Malware capabilities identified: ☐ Yes ☐ No  
   - Command and control identified: ☐ Yes ☐ No  
   - Persistence mechanisms found: ☐ Yes ☐ No

☐ **Malware eradication**  
   - Antivirus signatures updated: ☐ Yes ☐ No  
   - All infected systems cleaned: ☐ Yes ☐ No  
   - Network indicators blocked: ☐ Yes ☐ No  
   - Vulnerability patched: ☐ Yes ☐ No

### Phishing Incident Checklist *(NIST CSF: DE.AE-2)*
☐ **Phishing response**  
   - Malicious emails quarantined: ☐ Yes ☐ No  
   - Affected users identified: ☐ Yes ☐ No  
   - Compromised credentials reset: ☐ Yes ☐ No  
   - Additional training provided: ☐ Yes ☐ No

☐ **Email security enhancement**  
   - Email filters updated: ☐ Yes ☐ No  
   - Additional authentication required: ☐ Yes ☐ No  
   - User awareness campaign launched: ☐ Yes ☐ No

---

## Quality Assurance and Review

### Checklist Completion Review
☐ **All phases completed appropriately**  
☐ **All required notifications made within timeframes**  
☐ **All evidence properly collected and preserved**  
☐ **All stakeholders appropriately involved**  
☐ **All documentation completed and accurate**

### Process Improvement Opportunities
**What worked well:**
- ___________________________________
- ___________________________________
- ___________________________________

**What could be improved:**
- ___________________________________
- ___________________________________
- ___________________________________

**Recommended changes to checklist:**
- ___________________________________
- ___________________________________
- ___________________________________

---

## Document Control

**Checklist Version:** 1.0  
**Incident Date:** ___________  
**Last Updated:** ___________  
**Next Review:** ___________  
**Owner:** [INCIDENT RESPONSE TEAM]  
**Retention:** [7 YEARS]

---

**Important Reminders:**
- This checklist should be customized based on your specific incident response procedures
- All times should be documented in UTC or local time zone (specify which)
- Evidence handling must follow established chain of custody procedures
- Legal counsel should be consulted early for any potential data breach
- Communication with media should only be done by authorized personnel
- This checklist serves as a guide - use judgment for specific incident circumstances