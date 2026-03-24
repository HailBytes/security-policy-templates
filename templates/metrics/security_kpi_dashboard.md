# Security KPI Dashboard Template

**Organization:** [Company Name]
**Reporting Period:** [Month/Quarter YYYY]
**Prepared By:** [IT Contact]
**Reviewed By:** [Security Officer]
**Report Date:** [Date]

---

> **How to use this template:** Complete each section monthly. Share the Executive Summary with leadership. Share the full report with IT and security staff. Archive completed reports for trend analysis and compliance evidence. Cells marked `—` indicate metrics not yet tracked; establish a baseline before setting targets.

---

## Executive Summary

| Status | Metric | This Period | Last Period | Target | Trend |
|--------|--------|-------------|-------------|--------|-------|
| 🟢/🟡/🔴 | Open Critical/High Vulnerabilities | | | 0 Critical, <5 High | |
| 🟢/🟡/🔴 | Patch Compliance Rate | | | ≥95% | |
| 🟢/🟡/🔴 | Security Incidents | | | <[baseline] | |
| 🟢/🟡/🔴 | MFA Coverage | | | 100% | |
| 🟢/🟡/🔴 | Security Training Completion | | | 100% | |
| 🟢/🟡/🔴 | Vendor Assessments Current | | | 100% of Critical/High | |

**Status Key:** 🟢 On target | 🟡 At risk (within 10% of target) | 🔴 Off target

**Summary Notes:**
> [2–3 sentences: key wins, active concerns, and any items requiring leadership decision or awareness]

---

## 1. Vulnerability Management

### 1.1 Open Vulnerabilities by Severity

| Severity | Open This Period | Opened This Period | Closed This Period | Overdue (Past SLA) |
|----------|-----------------|-------------------|-------------------|-------------------|
| Critical | | | | |
| High | | | | |
| Medium | | | | |
| Low | | | | |
| **Total** | | | | |

**SLA Targets:** Critical ≤72 hrs | High ≤14 days | Medium ≤30 days | Low ≤90 days

### 1.2 Remediation Performance

| Metric | This Period | Last Period | 3-Month Avg | Target |
|--------|------------|------------|-------------|--------|
| Mean Time to Remediate — Critical (hours) | | | | ≤72 |
| Mean Time to Remediate — High (days) | | | | ≤14 |
| % Vulnerabilities Remediated Within SLA | | | | ≥95% |
| Vulnerabilities in Exception Status | | | | 0 Critical, <3 High |
| Scan Coverage (% of assets scanned) | | | | 100% |

### 1.3 Top Open Vulnerabilities

| # | CVE / Finding | Severity | System(s) | Days Open | Assigned To | Target Remediation |
|---|---------------|----------|-----------|-----------|-------------|-------------------|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |

---

## 2. Patch Management

### 2.1 Patch Compliance Rate

| Asset Type | Total Assets | Fully Patched | % Compliant | Target |
|-----------|-------------|---------------|-------------|--------|
| Servers (Windows) | | | | ≥98% |
| Servers (Linux) | | | | ≥98% |
| Workstations | | | | ≥95% |
| Network Devices | | | | ≥95% |
| Cloud Infrastructure | | | | ≥99% |
| **Overall** | | | | ≥95% |

### 2.2 Patch Deployment Activity

| Metric | This Period | Last Period | Target |
|--------|-----------|------------|--------|
| Critical patches deployed | | | All within 72 hrs |
| High patches deployed | | | All within 14 days |
| Patches pending (overdue) | | | 0 Critical/High |
| Failed patches requiring re-deployment | | | <5% failure rate |
| Unpatched EOL systems | | | 0 |

---

## 3. Incident Management

### 3.1 Incident Summary

| Metric | This Period | Last Period | YTD | Target |
|--------|-----------|------------|-----|--------|
| Total incidents reported | | | | |
| Critical incidents (P1) | | | | 0 |
| High incidents (P2) | | | | |
| Security incidents (policy violations, unauthorized access, malware) | | | | |
| Data breach incidents | | | | 0 |
| Mean Time to Detect (MTTD) — hours | | | | <24 |
| Mean Time to Respond (MTTR) — hours | | | | <4 (P1), <24 (P2) |
| Mean Time to Resolve — days | | | | <1 (P1), <7 (P2) |

### 3.2 Incident Categories

| Category | Count This Period | Count Last Period | Notable Incidents |
|----------|-----------------|-----------------|------------------|
| Phishing/Social Engineering | | | |
| Malware / Ransomware | | | |
| Unauthorized Access | | | |
| Data Exposure / Leakage | | | |
| Policy Violation | | | |
| Account Compromise | | | |
| Physical Security | | | |
| Third-Party / Vendor | | | |
| Other | | | |

### 3.3 Open Incidents

| # | Incident ID | Category | Priority | Date Opened | Status | Owner | ETA |
|---|------------|----------|----------|-------------|--------|-------|-----|
| 1 | | | | | | | |
| 2 | | | | | | | |

---

## 4. Access Control and Identity

### 4.1 MFA and Authentication Coverage

| System / Service | Total Accounts | MFA Enabled | % Coverage | Target |
|-----------------|---------------|-------------|------------|--------|
| Email / Microsoft 365 / Google Workspace | | | | 100% |
| VPN | | | | 100% |
| Cloud Console (AWS/Azure/GCP) | | | | 100% |
| Business Applications (list key apps) | | | | 100% |
| Privileged / Admin Accounts | | | | 100% |
| **Overall MFA Coverage** | | | | 100% |

### 4.2 Access Management Activity

| Metric | This Period | Last Period | Target |
|--------|-----------|------------|--------|
| Access provisioning requests processed | | | |
| Access de-provisioning requests (terminations) | | | |
| Avg time to revoke access post-termination (hours) | | | ≤4 |
| Stale accounts disabled (inactive >90 days) | | | |
| Quarterly access review completion rate | | | 100% |
| Privileged accounts in use | | | <[baseline] |
| Shared credentials identified and eliminated | | | 0 |

---

## 5. Security Awareness and Training

### 5.1 Training Completion

| Training Program | Employees Required | Completed | % Complete | Due Date | Target |
|----------------|-------------------|-----------|------------|----------|--------|
| Annual Security Awareness | | | | | 100% |
| Phishing Simulation | | | | | |
| New Hire Security Onboarding | | | | | 100% within 30 days |
| Remote Work / BYOD Training | | | | | 100% |
| Role-Specific (IT/Admin) | | | | | 100% |
| HIPAA Training (if applicable) | | | | | 100% |
| Policy Acknowledgment (Annual) | | | | | 100% |

### 5.2 Phishing Simulation Results

| Metric | This Period | Last Period | Target |
|--------|-----------|------------|--------|
| Emails sent | | | |
| Click rate | | | <5% |
| Credential submission rate | | | <2% |
| Reported by users | | | >80% |
| Users requiring remedial training | | | |

---

## 6. Vendor and Third-Party Risk

### 6.1 Vendor Risk Status

| Metric | This Period | Last Period | Target |
|--------|-----------|------------|--------|
| Critical vendors with current assessment | | | 100% |
| High vendors with current assessment | | | 100% |
| Vendors with overdue reassessment | | | 0 |
| New vendor onboardings completed this period | | | |
| Vendors flagged for security issues | | | 0 |
| BAAs / DPAs in place (if applicable) | | | 100% of data-sharing vendors |

### 6.2 Vendor Issues

| Vendor | Issue | Severity | Status | Remediation Date |
|--------|-------|----------|--------|-----------------|
| | | | | |

---

## 7. Compliance and Policy

### 7.1 Policy Compliance

| Policy | Last Review Date | Next Review Due | Status | Outstanding Items |
|--------|-----------------|----------------|--------|------------------|
| Acceptable Use Policy | | | | |
| Password Protection Policy | | | | |
| Remote Work / BYOD Policy | | | | |
| Data Classification Policy | | | | |
| Incident Response Policy | | | | |
| Vendor Risk Policy | | | | |
| Cloud Security Policy | | | | |
| Vulnerability Management Policy | | | | |
| Change Management Policy | | | | |

### 7.2 Audit and Assessment Activity

| Activity | Date Completed | Findings | Open Items | Next Due |
|----------|---------------|---------|------------|---------|
| Internal compliance audit | | | | |
| External vulnerability assessment | | | | |
| Penetration test | | | | |
| Disaster recovery test | | | | |
| Backup restoration test | | | | |
| Cloud security posture review | | | | |

---

## 8. Security Investment and Capacity

### 8.1 Security Tool Health

| Tool / Service | Status | License Expiry | Issues | Action Needed |
|---------------|--------|---------------|--------|--------------|
| Endpoint protection (AV/EDR) | | | | |
| Vulnerability scanner | | | | |
| SIEM / Log management | | | | |
| Email security (anti-spam, anti-phish) | | | | |
| Password manager | | | | |
| MDM / Endpoint management | | | | |
| Backup solution | | | | |
| MFA solution | | | | |

### 8.2 Open Security Projects

| Project | Owner | Status | Target Completion | Notes |
|---------|-------|--------|------------------|-------|
| | | | | |
| | | | | |

---

## 9. Key Actions and Decisions Required

> **[IT Contact] to complete before distributing report]**

### Actions This Period

| # | Action Item | Owner | Due Date | Status |
|---|------------|-------|----------|--------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

### Decisions Required from Leadership

| # | Decision | Context | Options | Deadline |
|---|---------|---------|---------|---------|
| 1 | | | | |

---

## Appendix: Trend Charts

> **Instructions:** Copy the metric data below into a spreadsheet to generate trend charts for leadership presentations.

### Vulnerability Trend Data (rolling 6 months)

| Month | Critical Open | High Open | MTTR Critical (hrs) | % Within SLA |
|-------|-------------|----------|---------------------|-------------|
| Month -5 | | | | |
| Month -4 | | | | |
| Month -3 | | | | |
| Month -2 | | | | |
| Month -1 | | | | |
| This Month | | | | |

### Incident Trend Data (rolling 6 months)

| Month | Total Incidents | P1 Incidents | MTTD (hrs) | MTTR (hrs) |
|-------|----------------|-------------|------------|-----------|
| Month -5 | | | | |
| Month -4 | | | | |
| Month -3 | | | | |
| Month -2 | | | | |
| Month -1 | | | | |
| This Month | | | | |

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Security Officer] | Initial release |
