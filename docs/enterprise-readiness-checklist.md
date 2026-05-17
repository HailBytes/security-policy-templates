# Enterprise Readiness Checklist

**What enterprise buyers will ask for — and what most SMBs can't answer yet.**

This checklist captures the gaps that consistently surface in enterprise procurement, vendor security reviews, and pre-contract due diligence. It is framed around what the *buyer's* security team will actually ask, not what looks good in a policy document.

HailBytes works with organizations at every stage of this checklist. If you have the policies from this repo but need help closing the gaps below, [request an enterprise trust package](https://hailbytes.com/enterprise?utm_source=github&utm_medium=docs&utm_campaign=enterprise-trust).

---

## Gap 1: SOC 2 Attestation

**What enterprise buyers ask:**
> *"Can you provide your SOC 2 Type II report?"*

**Why it kills deals:** For mid-market and enterprise buyers — especially in financial services, healthcare, and SaaS — a SOC 2 Type II report from a licensed CPA firm is table stakes. A policy document is not a substitute. Buyers who ask for SOC 2 and receive "we follow NIST CSF" will typically move to a vendor who has the report.

**The gap:** Most SMBs have zero auditor-issued attestation. Having this repo's policies is a strong start on *design evidence*, but SOC 2 also requires:
- 6–12 months of *operating evidence* (logs, access reviews, change tickets, training records)
- A licensed CPA firm to conduct the audit
- A defined audit scope (systems, services, Trust Services Criteria)

**Closing the gap:**
- [ ] Define SOC 2 scope — which systems and services are in-scope
- [ ] Identify which Trust Services Criteria apply (Security is mandatory; add Availability, Confidentiality as appropriate)
- [ ] Implement evidence collection for all in-scope CC criteria — see [SOC 2 mappings](../mappings/soc2.md)
- [ ] Select a readiness assessment firm (pre-audit) to identify gaps before the formal audit
- [ ] Engage a licensed CPA firm for the Type I audit (point-in-time) then Type II (12-month observation period)
- [ ] Budget: Type I typically $15K–$40K; Type II $25K–$75K+ depending on scope and firm

**Timeline:** 9–18 months from policy implementation to issued Type II report.

---

## Gap 2: Formal Penetration Test

**What enterprise buyers ask:**
> *"Do you have a penetration test report from the past 12 months?"*

**Why it kills deals:** Vulnerability scans (even continuous ASM) are not pen tests. Enterprise procurement teams — and their cyber insurance underwriters — distinguish between automated scanning and human-led adversarial testing. A dated pen test report, or no report at all, signals immaturity.

**The gap:** Most SMBs have never commissioned a formal pen test. Common objections:
- "We're too small to be a target" — the pen test is for the *buyer's* risk tolerance, not yours
- "We do continuous scanning" — ASM finds known vulnerabilities; pen testers find logic flaws, misconfigurations, and chained attacks

**Closing the gap:**
- [ ] Define scope: external network, web application, internal network, social engineering, or combined
- [ ] Select a qualified testing firm (look for OSCP, CREST, or GPEN certifications among testers)
- [ ] Remediate findings from the report — the report alone is not the deliverable; the remediation evidence is
- [ ] Retain the report and remediation documentation for buyer disclosure
- [ ] Schedule annual re-testing; buyers will ask for "most recent" not "we did one in 2022"
- [ ] Budget: $5K–$25K for a scoped external/web application test; more for internal or red team engagements

**Note for Brazil / BACEN-regulated entities:** BACEN Resolution 4,893/2021 Art. 5 IV explicitly requires vulnerability testing. A formal pen test satisfies this requirement and should be referenced in your BACEN cybersecurity policy.

---

## Gap 3: Customer / Reference Accounts

**What enterprise buyers ask:**
> *"Can you provide references from similar-sized customers in our industry?"*

**Why it kills deals:** Enterprise procurement — especially for security tools or managed services — requires social proof at the right tier. References from three 5-person startups do not satisfy the procurement committee of a 2,000-person financial institution. This gap is often underestimated because it is not a technical control.

**The gap:** Reference gaps manifest in two ways:
1. **Size mismatch** — existing customers are too small to validate enterprise readiness
2. **Industry mismatch** — no references in the buyer's regulated sector (financial services, healthcare, government)

**Closing the gap:**
- [ ] Identify 2–3 existing customers who can be referenced by enterprise buyers; get pre-approval
- [ ] Build a case study library — written or video — that can be shared without direct reference calls
- [ ] For regulated industries (financial, healthcare): pursue at least one named customer in that sector before major enterprise outreach
- [ ] If references are thin: offer a paid pilot program with defined success criteria — reduces procurement risk and builds the reference pipeline
- [ ] Document customer outcomes (incident reduction %, compliance milestone achieved, audit finding closure) — outcomes beat logos

---

## Gap 4: Tech E&O and Cyber Liability Insurance

**What enterprise buyers ask:**
> *"What are your technology E&O and cyber liability coverage limits?"*

**Why it kills deals:** Enterprise procurement agreements typically require minimum insurance coverage as a contractual prerequisite. If your policy limits are below the buyer's minimums — or you have no coverage — the legal team will block the deal regardless of technical merit.

**Common enterprise minimums:**
| Coverage Type | Typical SMB Coverage | Enterprise Buyer Minimum |
|--------------|---------------------|--------------------------|
| Cyber Liability | $1M or none | $1M–$5M per occurrence |
| Tech E&O | $1M or none | $1M–$5M per occurrence |
| General Liability | $1M/$2M | $1M/$2M (standard) |
| Workers Comp | Varies | Required in most contracts |

**The gap:** Most SMBs either lack cyber liability coverage entirely, have limits that are too low for enterprise contracts, or have coverage that excludes key scenarios (cloud, third-party liability, regulatory fines).

**Closing the gap:**
- [ ] Obtain Cyber Liability Insurance — minimum $1M per occurrence / $2M aggregate to start
- [ ] Obtain Technology E&O (Errors & Omissions) coverage — covers claims arising from your technology services or products
- [ ] Verify your policy covers: first-party breach costs, third-party liability, regulatory defense costs, and cloud/SaaS services
- [ ] Request a certificate of insurance (COI) you can provide to enterprise buyers during procurement
- [ ] Budget: $2K–$15K annually depending on revenue, scope, and claims history
- [ ] Review coverage annually — limits that satisfied a buyer last year may not satisfy a new buyer this year

**Note for LGPD / Brazil deals:** Brazilian data protection law (LGPD Art. 52) allows ANPD fines of up to 2% of Brazilian revenue (capped at R$50M per infraction). Ensure your cyber liability policy covers regulatory defense and fines in Brazilian jurisdiction if you process Brazilian personal data.

---

## Bonus Gap: Formal Vendor Security Questionnaire (VSQ) Readiness

**What enterprise buyers ask:**
> *"Please complete our vendor security questionnaire."* (CAIQ, SIG, custom 200-question spreadsheet)

**Why it matters:** VSQs arrive without warning and have tight deadlines. Organizations without documented answers to standard questions scramble, provide inconsistent answers, or miss submissions. This creates audit findings even when the underlying controls are solid.

**Closing the gap:**
- [ ] Build a master VSQ response library — standard answers to CAIQ v3.1, SIG Lite, and your top buyer's custom questionnaire
- [ ] Map your policies in this repo to VSQ question categories — the [`/mappings`](../mappings/) directory gives you a head start
- [ ] Assign a DRI (directly responsible individual) for VSQ completion
- [ ] Review and update your VSQ library quarterly, or whenever a major policy changes

---

## Enterprise Readiness Score Card

Use this to track progress:

| Item | Status | Owner | Target Date |
|------|--------|-------|-------------|
| Policy documentation (this repo) | ✅ In progress | | |
| SOC 2 scope defined | ⬜ | | |
| SOC 2 readiness assessment complete | ⬜ | | |
| SOC 2 Type I issued | ⬜ | | |
| SOC 2 Type II issued | ⬜ | | |
| Annual penetration test completed | ⬜ | | |
| Pen test findings remediated | ⬜ | | |
| Cyber liability insurance obtained ($1M+) | ⬜ | | |
| Tech E&O insurance obtained ($1M+) | ⬜ | | |
| 3 referenceable enterprise customers | ⬜ | | |
| Master VSQ response library built | ⬜ | | |
| LGPD / ANPD notification procedures documented | ⬜ | | |
| BACEN 4,893 cybersecurity policy filed (if applicable) | ⬜ | | |

---

## Working With HailBytes

HailBytes helps organizations close these gaps as a managed program — not a one-time engagement. Our enterprise trust package includes:

- Policy operationalization via SAT and ASM platforms (controls, not just documents)
- SOC 2 readiness support and auditor introductions
- Pen test partner network (scoped to your stack and compliance goals)
- VSQ response library and support
- LGPD / BACEN compliance guidance for Brazil-market deals

> [Request an enterprise trust package →](https://hailbytes.com/enterprise?utm_source=github&utm_medium=docs&utm_campaign=enterprise-trust)  
> [Book a 30-minute enterprise readiness call →](https://hailbytes.com/contact?utm_source=github&utm_medium=docs&utm_campaign=enterprise-trust)

---

*Last updated: May 2026. Enterprise procurement requirements evolve — review this checklist annually and after any major enterprise sales loss to identify new gaps.*
