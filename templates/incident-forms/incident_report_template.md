# Incident Report Template

**NIST CSF Functions: Detect (DE), Respond (RS)**

---

## Incident Information

**Incident ID:** [AUTO-GENERATED OR ASSIGNED]  
**Report Date:** [DATE]  
**Reporter Name:** [NAME]  
**Reporter Contact:** [EMAIL/PHONE]  
**Reporter Role/Department:** [TITLE/DEPARTMENT]

---

## Initial Classification *(NIST CSF: DE.AE-2)*

**Incident Type:** ☐ Malware ☐ Phishing ☐ Data Breach ☐ Unauthorized Access ☐ System Outage ☐ Other: _______

**Severity Level:** *(Based on Security Response Plan Policy)*
- ☐ **Critical** (Response within 1 hour)
- ☐ **High** (Response within 4 hours)  
- ☐ **Medium** (Response within 24 hours)
- ☐ **Low** (Response within 72 hours)

**Discovery Method:** *(NIST CSF: DE.AE-1)*
☐ Automated monitoring/alerts ☐ User report ☐ Routine audit ☐ External notification ☐ Other: _______

---

## Incident Details *(NIST CSF: DE.DP-4)*

### When Did It Occur?
**Date/Time of Incident:** [DATE/TIME]  
**Date/Time Discovered:** [DATE/TIME]  
**Timezone:** [TIMEZONE]

### What Happened?
**Brief Description:**
[Describe what happened in 2-3 sentences]

**Detailed Description:**
[Provide comprehensive details of the incident, including sequence of events]

### Where Did It Occur?
**Affected Systems/Applications:**
- [ ] Email systems
- [ ] File servers
- [ ] Database servers
- [ ] Network infrastructure
- [ ] Workstations/laptops
- [ ] Mobile devices
- [ ] Cloud services
- [ ] Other: _______________

**Specific System Details:**
- System names: [LIST SYSTEMS]
- IP addresses: [LIST IPs]
- Network segments: [LIST SEGMENTS]

### Who Was Involved?
**Affected Users/Accounts:**
[Number of users affected: ___]
[List specific accounts if applicable]

**Potential Threat Actors:**
☐ Internal user ☐ External attacker ☐ Unknown ☐ System malfunction

---

## Impact Assessment *(NIST CSF: RS.AN-3)*

### Business Impact
**Operations Affected:**
☐ Email ☐ File access ☐ Internet access ☐ Critical applications ☐ Customer services ☐ Financial systems

**Impact Level:**
☐ No business impact ☐ Minor impact ☐ Moderate impact ☐ Significant impact ☐ Severe impact

**Estimated Financial Impact:** $________

**Affected Customers/Partners:** [NUMBER/NAMES]

### Data Impact *(NIST CSF: PR.DS-1)*
**Data Types Potentially Affected:**
☐ Personal information (PII) ☐ Financial data ☐ Health information ☐ Intellectual property ☐ Business confidential

**Data Classification Level:**
☐ Public ☐ Internal ☐ Confidential ☐ Restricted

**Estimated Records Affected:** [NUMBER]

---

## Immediate Response Actions *(NIST CSF: RS.RP-1)*

### Containment Actions Taken *(NIST CSF: RS.MI-2)*
☐ Isolated affected systems ☐ Disabled user accounts ☐ Changed passwords ☐ Applied security patches  
☐ Blocked malicious IP addresses ☐ Quarantined malware ☐ Other: _______________

**Actions Taken:**
[Describe specific containment actions with timestamps]

### Evidence Preservation *(NIST CSF: RS.AN-1)*
☐ System logs collected ☐ Memory dumps captured ☐ Network traffic captured ☐ Screenshots taken  
☐ Physical evidence secured ☐ Chain of custody established ☐ Forensic images created

**Evidence Location:** [WHERE EVIDENCE IS STORED]

### Notifications Made *(NIST CSF: RS.CO-2)*
☐ IT Security team ☐ Management ☐ Legal counsel ☐ HR department  
☐ Customers ☐ Vendors ☐ Law enforcement ☐ Regulatory authorities

**Notification Details:**
| Who | When | Method | Response |
|-----|------|--------|----------|
| [NAME/ROLE] | [TIME] | [EMAIL/PHONE] | [RESPONSE] |

---

## Analysis and Investigation *(NIST CSF: RS.AN-2)*

### Root Cause Analysis
**Likely Cause:**
☐ Human error ☐ System vulnerability ☐ Malware ☐ Social engineering  
☐ Physical security breach ☐ Vendor/supplier issue ☐ Unknown

**Contributing Factors:**
[List factors that contributed to the incident]

### Attack Vector *(NIST CSF: DE.AE-2)*
☐ Email attachment ☐ Malicious website ☐ USB device ☐ Network intrusion  
☐ Credential compromise ☐ Physical access ☐ Social engineering ☐ Other: _______

### Indicators of Compromise (IoCs)
**File Hashes:** [LIST HASHES]  
**IP Addresses:** [LIST IPs]  
**Domain Names:** [LIST DOMAINS]  
**Email Addresses:** [LIST EMAILS]  
**Other Indicators:** [LIST OTHER IoCs]

---

## Recovery Actions *(NIST CSF: RC.RP-1)*

### Systems Recovery
☐ Systems restored from backup ☐ Security patches applied ☐ Configurations updated  
☐ Monitoring enhanced ☐ Access controls strengthened

**Recovery Steps Taken:**
[Describe recovery actions with timestamps]

### Validation and Testing *(NIST CSF: RC.IM-1)*
☐ System functionality verified ☐ Security controls tested ☐ Data integrity confirmed  
☐ Performance validated ☐ User access restored

---

## Lessons Learned and Recommendations *(NIST CSF: RC.IM-2)*

### What Worked Well?
[List effective response elements]

### What Could Be Improved?
[List areas for improvement]

### Recommended Actions
**Immediate (0-30 days):**
- [ ] [ACTION ITEM] - Owner: [NAME] - Due: [DATE]
- [ ] [ACTION ITEM] - Owner: [NAME] - Due: [DATE]

**Short-term (30-90 days):**
- [ ] [ACTION ITEM] - Owner: [NAME] - Due: [DATE]
- [ ] [ACTION ITEM] - Owner: [NAME] - Due: [DATE]

**Long-term (90+ days):**
- [ ] [ACTION ITEM] - Owner: [NAME] - Due: [DATE]
- [ ] [ACTION ITEM] - Owner: [NAME] - Due: [DATE]

### Policy Updates Required
☐ Update incident response procedures ☐ Revise security policies ☐ Enhance training programs  
☐ Improve monitoring capabilities ☐ Strengthen access controls

---

## Regulatory and Legal Considerations

### Notification Requirements *(NIST CSF: RS.CO-3)*
☐ Data breach notification laws apply ☐ Industry regulations apply ☐ Contractual obligations exist

**Regulatory Requirements:**
[List applicable regulations and notification timeframes]

### Legal Hold Requirements
☐ Legal hold implemented ☐ Attorney-client privilege considerations ☐ Law enforcement coordination

---

## Incident Closure

### Resolution Status
☐ **Resolved** - Incident fully contained and systems restored  
☐ **Ongoing** - Response activities continue  
☐ **Monitoring** - Watching for additional activity

### Final Impact Summary
**Total Business Downtime:** [HOURS]  
**Final Financial Impact:** $[AMOUNT]  
**Records Actually Affected:** [NUMBER]

### Incident Commander Sign-off
**Name:** [NAME]  
**Signature:** ___________________  
**Date:** [DATE]

---

## Supporting Documentation

### Attachments
☐ System logs ☐ Network captures ☐ Screenshots ☐ Forensic reports  
☐ Communication logs ☐ Recovery procedures ☐ Other: _______________

### Related Incidents
**Previous Related Incidents:** [INCIDENT IDs]  
**Follow-up Actions Required:** [LIST ACTIONS]

---

**Document Control**  
**Version:** 1.0  
**Last Updated:** [DATE]  
**Next Review:** [DATE]  
**Owner:** [INCIDENT RESPONSE TEAM]