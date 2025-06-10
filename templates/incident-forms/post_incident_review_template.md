# Post-Incident Review Template

**NIST CSF Functions: Recover (RC), Identify (ID)**

---

## Review Information

**Incident ID:** [INCIDENT-ID]  
**Review Date:** [DATE]  
**Review Facilitator:** [NAME/ROLE]  
**Review Participants:** [LIST ALL ATTENDEES]

**Original Incident:**
- **Date Occurred:** [DATE]
- **Date Resolved:** [DATE]
- **Total Duration:** [HOURS/DAYS]
- **Severity Level:** [CRITICAL/HIGH/MEDIUM/LOW]

---

## Executive Summary *(NIST CSF: RC.IM-1)*

### Incident Overview
**What Happened:**
[Brief description of the incident - 2-3 sentences]

**Business Impact:**
- **Systems Affected:** [LIST]
- **Downtime:** [DURATION]
- **Users Impacted:** [NUMBER]
- **Financial Impact:** $[AMOUNT]
- **Data/Records Affected:** [NUMBER]

### Key Outcomes
**Positive Outcomes:**
- [List what went well during response]

**Areas for Improvement:**
- [List key improvement areas identified]

---

## Timeline Analysis *(NIST CSF: DE.AE-1)*

### Critical Timestamps
| Event | Target Time | Actual Time | Variance | NIST CSF Function |
|-------|-------------|-------------|----------|-------------------|
| **Initial Detection** | N/A | [TIME] | N/A | Detect (DE.AE-1) |
| **First Response** | [TARGET] | [ACTUAL] | [+/- TIME] | Respond (RS.RP-1) |
| **Containment Started** | [TARGET] | [ACTUAL] | [+/- TIME] | Respond (RS.MI-2) |
| **Stakeholders Notified** | [TARGET] | [ACTUAL] | [+/- TIME] | Respond (RS.CO-2) |
| **Root Cause Identified** | [TARGET] | [ACTUAL] | [+/- TIME] | Respond (RS.AN-1) |
| **Systems Restored** | [TARGET] | [ACTUAL] | [+/- TIME] | Recover (RC.RP-1) |
| **Normal Operations** | [TARGET] | [ACTUAL] | [+/- TIME] | Recover (RC.CO-3) |

### Timeline Performance Analysis
**Met Response Targets:** [PERCENTAGE]  
**Major Delays:** [LIST WITH REASONS]  
**Exceeded Expectations:** [LIST]

---

## Response Effectiveness Assessment *(NIST CSF: RS.IM-1)*

### Detection Capabilities *(NIST CSF: DE.CM-1)*
**How was the incident discovered?**
☐ Automated monitoring ☐ User report ☐ External notification ☐ Routine audit ☐ Other

**Detection Effectiveness Rating:** ☐ Excellent ☐ Good ☐ Fair ☐ Poor

**What Worked Well:**
- [List effective detection elements]

**What Could Be Improved:**
- [List detection improvements needed]

### Response Team Performance *(NIST CSF: RS.CO-1)*
**Team Assembly Time:** [MINUTES] (Target: [TARGET])  
**Communication Effectiveness:** ☐ Excellent ☐ Good ☐ Fair ☐ Poor  
**Decision Making:** ☐ Excellent ☐ Good ☐ Fair ☐ Poor

**Team Strengths:**
- [List what the team did well]

**Team Improvement Areas:**
- [List areas where team performance could improve]

### Containment Effectiveness *(NIST CSF: RS.MI-2)*
**Containment Success:** ☐ Excellent ☐ Good ☐ Fair ☐ Poor  
**Time to Containment:** [MINUTES/HOURS] (Target: [TARGET])

**Effective Containment Actions:**
- [List successful containment measures]

**Containment Challenges:**
- [List obstacles or issues with containment]

### Communication Performance *(NIST CSF: RS.CO-2)*
**Internal Communication:** ☐ Excellent ☐ Good ☐ Fair ☐ Poor  
**External Communication:** ☐ Excellent ☐ Good ☐ Fair ☐ Poor  
**Stakeholder Updates:** ☐ Timely ☐ Delayed ☐ Inadequate

**Communication Successes:**
- [List effective communications]

**Communication Improvements Needed:**
- [List communication gaps or issues]

---

## Root Cause Analysis *(NIST CSF: RS.AN-1)*

### Primary Root Cause
**Category:** ☐ Technical ☐ Process ☐ Human ☐ External

**Detailed Root Cause:**
[Describe the fundamental cause that led to the incident]

### Contributing Factors
1. **[Factor 1]** - [Description and impact]
2. **[Factor 2]** - [Description and impact]
3. **[Factor 3]** - [Description and impact]

### 5 Whys Analysis
1. **Why did the incident occur?** [Answer]
2. **Why did [Answer 1] happen?** [Answer]
3. **Why did [Answer 2] happen?** [Answer]
4. **Why did [Answer 3] happen?** [Answer]
5. **Why did [Answer 4] happen?** [Answer]

---

## Recovery Assessment *(NIST CSF: RC.RP-1)*

### Recovery Effectiveness
**Recovery Time Objective (RTO):** [TARGET] vs **Actual:** [ACTUAL]  
**Recovery Point Objective (RPO):** [TARGET] vs **Actual:** [ACTUAL]

**Recovery Success Rate:** [PERCENTAGE]

### Recovery Challenges
**Major Obstacles:**
- [List significant recovery challenges]

**Resource Constraints:**
- [List resource limitations that impacted recovery]

### Recovery Successes
**Effective Recovery Actions:**
- [List successful recovery measures]

**Lessons Learned for Future Recovery:**
- [List insights for improving recovery processes]

---

## Security Control Analysis *(NIST CSF: PR.IP-1)*

### Control Failures
**Failed Controls:**
| Control Type | Control Name | Failure Mode | Impact | NIST CSF Reference |
|--------------|--------------|--------------|--------|-------------------|
| [Technical/Administrative/Physical] | [Control Name] | [How it failed] | [Impact] | [NIST Reference] |

### Control Successes
**Effective Controls:**
| Control Type | Control Name | How It Helped | NIST CSF Reference |
|--------------|--------------|---------------|-------------------|
| [Type] | [Control Name] | [How it worked] | [NIST Reference] |

### Control Gaps Identified
**Missing Controls:**
- [List controls that should exist but don't]

**Inadequate Controls:**
- [List controls that exist but are insufficient]

---

## Lessons Learned *(NIST CSF: RC.IM-2)*

### What Worked Well
**Strengths to Maintain:**
1. **[Strength 1]** - [Description and why it was effective]
2. **[Strength 2]** - [Description and why it was effective]
3. **[Strength 3]** - [Description and why it was effective]

### What Didn't Work
**Areas for Immediate Improvement:**
1. **[Issue 1]** - [Description and impact]
2. **[Issue 2]** - [Description and impact]
3. **[Issue 3]** - [Description and impact]

### Key Insights
**Strategic Insights:**
- [High-level insights about security posture]

**Tactical Insights:**
- [Operational insights about procedures and tools]

**People Insights:**
- [Insights about training, roles, and responsibilities]

---

## Improvement Action Plan *(NIST CSF: RC.IM-2)*

### Immediate Actions (0-30 days)
| Action | Owner | Due Date | Priority | NIST CSF Function | Status |
|--------|--------|----------|----------|-------------------|---------|
| [Action Description] | [Name] | [Date] | [High/Medium/Low] | [Function] | [Not Started/In Progress/Complete] |

### Short-term Actions (30-90 days)
| Action | Owner | Due Date | Priority | NIST CSF Function | Status |
|--------|--------|----------|----------|-------------------|---------|
| [Action Description] | [Name] | [Date] | [High/Medium/Low] | [Function] | [Status] |

### Long-term Actions (90+ days)
| Action | Owner | Due Date | Priority | NIST CSF Function | Status |
|--------|--------|----------|----------|-------------------|---------|
| [Action Description] | [Name] | [Date] | [High/Medium/Low] | [Function] | [Status] |

---

## Policy and Procedure Updates *(NIST CSF: PR.IP-1)*

### Required Policy Updates
**Policies Requiring Updates:**
- [ ] **[Policy Name]** - [Required changes]
- [ ] **[Policy Name]** - [Required changes]

### Procedure Improvements
**Procedures Requiring Updates:**
- [ ] **[Procedure Name]** - [Required changes]
- [ ] **[Procedure Name]** - [Required changes]

### Training Updates Needed
**Training Areas to Address:**
- [ ] **[Training Topic]** - [Target audience and content]
- [ ] **[Training Topic]** - [Target audience and content]

---

## Technology and Tool Assessment *(NIST CSF: PR.PT-1)*

### Tool Effectiveness
**Tools That Performed Well:**
- **[Tool Name]** - [How it helped and why it was effective]

**Tools That Need Improvement:**
- **[Tool Name]** - [What issues were encountered and how to improve]

**Missing Tools/Capabilities:**
- **[Capability Gap]** - [Description and business justification]

### Technology Recommendations
**Immediate Technology Needs:**
- [List urgent technology requirements]

**Future Technology Considerations:**
- [List longer-term technology improvements]

---

## Metrics and Measurements *(NIST CSF: DE.CM-8)*

### Incident Metrics
**Key Performance Indicators:**
- **Mean Time to Detection (MTTD):** [TIME]
- **Mean Time to Response (MTTR):** [TIME]
- **Mean Time to Recovery (MTTR):** [TIME]
- **Recovery Time Objective Achievement:** [PERCENTAGE]
- **Recovery Point Objective Achievement:** [PERCENTAGE]

### Comparison to Previous Incidents
**Trend Analysis:**
- [Compare metrics to previous similar incidents]
- [Identify trends and patterns]

### Benchmark Comparison
**Industry Benchmarks:**
- [Compare performance to industry standards where available]

---

## Stakeholder Feedback *(NIST CSF: RS.CO-5)*

### Internal Stakeholder Feedback
**Executive Leadership:**
- [Feedback from leadership on response effectiveness]

**IT Team:**
- [Technical team feedback on tools, processes, and support]

**Business Users:**
- [User feedback on communication and impact]

### External Stakeholder Feedback
**Customers:**
- [Customer feedback on communication and impact]

**Partners/Vendors:**
- [Partner feedback on coordination and support]

**Regulatory/Legal:**
- [Feedback from legal counsel or regulatory contacts]

---

## Final Recommendations

### Strategic Recommendations
1. **[Recommendation 1]** - [Business justification and expected outcome]
2. **[Recommendation 2]** - [Business justification and expected outcome]

### Tactical Recommendations
1. **[Recommendation 1]** - [Implementation details and timeline]
2. **[Recommendation 2]** - [Implementation details and timeline]

### Resource Requirements
**Budget Impact:** $[AMOUNT]  
**Personnel Requirements:** [FTE or hours required]  
**Timeline for Implementation:** [TIMEFRAME]

---

## Review Approval

### Review Participants Sign-off
| Name | Role | Signature | Date |
|------|------|-----------|------|
| [Name] | [Role] | _________________ | [Date] |
| [Name] | [Role] | _________________ | [Date] |

### Management Approval
**Incident Commander:** _________________ Date: _______  
**IT Security Manager:** _________________ Date: _______  
**Executive Sponsor:** _________________ Date: _______

---

## Follow-up Schedule *(NIST CSF: RC.IM-1)*

**30-Day Follow-up:** [DATE] - Review action item progress  
**60-Day Follow-up:** [DATE] - Assess implementation effectiveness  
**90-Day Follow-up:** [DATE] - Final effectiveness review

**Next Scheduled Review of Lessons Learned:** [DATE]

---

## Appendices

### Appendix A: Detailed Timeline
[Attach detailed incident timeline with all events]

### Appendix B: Technical Analysis
[Attach detailed technical analysis and forensics results]

### Appendix C: Communication Logs
[Attach records of all incident communications]

### Appendix D: Evidence Inventory
[Attach list of all evidence collected and preserved]

---

**Document Control**  
**Version:** 1.0  
**Created:** [DATE]  
**Last Updated:** [DATE]  
**Next Review:** [DATE]  
**Owner:** [INCIDENT RESPONSE TEAM]