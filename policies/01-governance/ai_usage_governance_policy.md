# Artificial Intelligence Usage and Governance Policy

**NIST CSF Functions: Identify (ID), Protect (PR), Detect (DE)**

## Purpose
To establish requirements for the responsible, secure, and ethical use of artificial intelligence (AI) tools, large language models (LLMs), AI agents, and AI-integrated software at [Company Name], including emerging technologies such as Model Context Protocol (MCP) servers and autonomous AI agent frameworks.

## Scope
Applies to all [Company Name] employees, contractors, and third parties who use, develop, deploy, or integrate AI tools in the course of work. Covered technologies include but are not limited to:
- AI assistant tools (e.g., ChatGPT, Claude, Microsoft Copilot, Gemini)
- AI-powered code generation tools (e.g., GitHub Copilot, Cursor, Tabnine)
- AI agent frameworks and orchestration platforms
- Model Context Protocol (MCP) servers and AI tool integrations
- AI features embedded in approved business software (e.g., CRM, HR, productivity suites)
- Internally developed or fine-tuned AI models

---

## AI Tool Governance

### 1.1 Approved AI Tools *(NIST CSF: ID.AM-2, ID.GV-1)*
- [IT Contact] maintains a register of approved AI tools, including permitted use cases and data classification limits for each tool
- Employees must not use unapproved AI tools to process [Company Name] data — this is a shadow IT violation (see Acceptable Use Policy)
- Requests for new AI tools must be submitted to [IT Contact] and reviewed within 10 business days
- Approval evaluation criteria include: data handling and retention practices, vendor security posture, privacy policy, compliance certifications, and contractual data protection commitments
- The AI tool register must be reviewed and updated quarterly

### 1.2 Data Classification Limits for AI Tools *(NIST CSF: PR.DS-1, PR.DS-5)*
Unless a tool has been explicitly approved for higher-classification data:

| Data Classification | Permitted in AI Tools |
|--------------------|-----------------------|
| Public | Permitted in approved tools |
| Internal | Permitted in approved tools with data residency confirmed |
| Confidential | Requires explicit approval from [Security Officer]; must use enterprise/private deployment or confirm no training use |
| Restricted | **Prohibited** — must not be entered into any AI tool without written authorization from [Security Officer] and legal review |

Employees must treat AI chat interfaces as potentially persistent and logged — never enter data you would not want stored on a third-party server.

### 1.3 Prohibited AI Uses *(NIST CSF: ID.GV-1, PR.DS-5)*
The following are prohibited regardless of the AI tool used:
- Entering passwords, API keys, credentials, or secrets into any AI tool
- Uploading or pasting Restricted data (PII, PHI, financial account data, trade secrets) into public AI interfaces
- Using AI tools to bypass security controls, access controls, or policy requirements
- Generating malicious code, phishing content, or deceptive materials
- Representing AI-generated content as independently authored work without disclosure where required (e.g., legal filings, regulated reports)
- Using AI tools to make fully automated decisions about individuals without human review where required by law or policy

---

## AI Agent and MCP Server Controls

Model Context Protocol (MCP) is a standard that allows AI assistants and agents to connect to external tools, data sources, APIs, and services. MCP servers extend AI capability significantly but introduce new security risks including prompt injection, excessive permissions, data exfiltration, and supply chain compromise.

### 1.4 Approved MCP Servers and AI Integrations *(NIST CSF: ID.AM-2, ID.SC-1)*
- Only MCP servers and AI tool integrations approved by [IT Contact] may be connected to [Company Name] systems or data
- [IT Contact] maintains a register of approved MCP servers including: name, source/publisher, version, permitted data access, and review date
- Approved MCP server register must be reviewed monthly due to the rapid pace of change in this technology area
- Connecting an unapproved MCP server to any [Company Name] system or data source constitutes a policy violation

### 1.5 MCP Server Security Assessment *(NIST CSF: ID.SC-2, ID.SC-4)*
Before approving any MCP server:
- Verify the source — prefer official, well-maintained MCP servers from reputable publishers
- Review the MCP server's source code or request a security review if source is unavailable
- Confirm the MCP server is pinned to a specific, reviewed version — do not use floating or auto-updating MCP servers without re-review
- Assess the tool's declared permissions and required access; reject any MCP server requesting broader access than its function requires
- Verify the MCP server does not exfiltrate data to undisclosed third-party endpoints
- Check the publisher's security disclosure policy and incident history

### 1.6 Principle of Least Privilege for AI Agents *(NIST CSF: PR.AC-4, PR.AC-6)*
- AI agents and MCP servers must be granted the minimum permissions required for their declared function
- MCP servers must not be granted write access to production systems, databases, or file systems unless the specific write operation is documented and approved
- AI agents operating on behalf of users must be scoped to that user's permissions — agents must not be granted administrative or elevated rights by default
- Credentials provided to MCP servers must be purpose-specific (e.g., read-only API keys) and must not be organization-wide admin credentials
- All credentials provisioned for AI agents and MCP servers must be stored in an approved secrets management solution — never hardcoded

### 1.7 Prompt Injection Risk Management *(NIST CSF: ID.RA-1, PR.DS-5)*
Prompt injection is an attack where malicious instructions embedded in data processed by an AI agent cause the agent to take unintended actions. Controls:
- AI agents that process external data (web content, emails, documents, database records) must be treated as potentially hostile inputs — never process external data with an agent that has write access to sensitive systems without human review of proposed actions
- MCP servers that retrieve external or user-supplied content must not be granted unrestricted ability to execute code, send communications, or modify data on the basis of that content alone
- High-risk agent actions (deleting files, sending emails, making financial transactions, modifying configurations) must require explicit human confirmation before execution
- Employees must be trained to recognize unexpected AI agent behavior as a potential prompt injection indicator and report it to [IT Contact]

### 1.8 AI Agent Monitoring and Logging *(NIST CSF: DE.CM-1, DE.AE-3)*
- All AI agent actions performed on [Company Name] systems must be logged with: timestamp, agent identity, action taken, data accessed, and outcome
- Agent activity logs must be retained for a minimum of 90 days
- Logs must be reviewed weekly by [IT Contact] for anomalous patterns (e.g., unexpected data access, unusual volume of API calls, access outside business hours)
- AI agents must not be permitted to modify or delete their own audit logs
- Alerts must be configured for: agent accessing data outside its defined scope, agent making high-volume requests, agent attempting privileged operations, agent communicating with unexpected external endpoints

### 1.9 AI Agent Supply Chain *(NIST CSF: ID.SC-4, PR.DS-6)*
- MCP server packages and AI agent dependencies must be sourced from official, verified repositories
- Dependencies must be pinned to specific versions; automatic updates require re-review before deployment
- A Software Bill of Materials (SBOM) must be maintained for internally deployed MCP servers and AI agent frameworks
- Known vulnerabilities in MCP server dependencies must be tracked and remediated per the Vulnerability Management Policy
- AI agents and MCP servers must not be deployed directly from unverified community sources without security review

---

## Data Privacy and AI

### 1.10 Personal Data and AI *(NIST CSF: PR.DS-1, PR.DS-5)*
- Personal data (names, contact details, financial information, health information) must not be submitted to public AI tools without explicit legal basis and [Security Officer] approval
- When using AI tools to process personal data in approved enterprise deployments, a Data Processing Agreement (DPA) must be in place with the AI provider
- AI-generated content derived from personal data is subject to the same data protection obligations as the source data
- Individuals whose data is used to train or fine-tune AI models must provide informed consent per applicable law (GDPR, CCPA, etc.)

### 1.11 Intellectual Property and AI Output *(NIST CSF: ID.GV-1)*
- Employees must not submit [Company Name] proprietary code, trade secrets, or confidential business information to AI tools that use inputs for model training
- AI-generated code incorporated into [Company Name] products must be reviewed for potential intellectual property issues and open-source license conflicts before use
- Employees must disclose the use of AI-generated content in deliverables where required by contract, regulation, or company policy

---

## AI Development and Deployment

### 1.12 Internally Developed AI Models *(NIST CSF: PR.IP-1, ID.RA-1)*
[Company Name] teams developing or fine-tuning AI models must:
- Conduct a security and privacy risk assessment before training or deploying any model on company data
- Document model purpose, training data sources, and data classification
- Ensure training data does not include Restricted data without explicit [Security Officer] authorization
- Test models for unintended outputs, bias, and security vulnerabilities before production deployment
- Implement model output filtering for production deployments that may produce sensitive or harmful content

### 1.13 AI in Automated Decision-Making *(NIST CSF: ID.GV-1, ID.GV-3)*
- AI must not be used to make fully automated decisions that have significant impact on individuals (hiring, termination, credit, benefits, legal status) without human review in the decision loop
- Any AI-assisted decision workflow affecting individuals must be documented with: the AI tool used, data inputs, how AI output is used in the decision, and who has final decision authority
- Employees may not use AI tool outputs as the sole basis for compliance determinations, legal conclusions, or financial approvals

---

## Awareness, Training, and Accountability

### 1.14 AI Security Training *(NIST CSF: PR.AT-1, PR.AT-2)*
- All employees must complete AI security awareness training within 60 days of policy effective date and annually thereafter
- Training must cover: approved tools and data limits, prohibited uses, prompt injection risks, recognizing AI-generated phishing and deepfakes, and reporting procedures
- Employees with technical roles deploying AI agents or MCP servers must complete additional role-based training covering agent security, least privilege for AI, and supply chain risks

### 1.15 Incident Reporting *(NIST CSF: RS.CO-2, DE.AE-1)*
The following must be reported to [IT Contact] and [Security Officer] within 24 hours of discovery:
- Accidental submission of Restricted or Confidential data to an unapproved AI tool
- AI agent behaving unexpectedly or performing actions outside its defined scope
- Discovery of an unapproved MCP server connected to company systems
- Suspected prompt injection attack against an AI agent
- AI tool producing output that appears to contain company data not provided in the current session
- Receipt of AI-generated phishing, deepfake, or social engineering content

### 1.16 Policy Acknowledgment *(NIST CSF: PR.AT-1)*
- All employees must sign the AI Usage Policy Acknowledgment Form before using AI tools for work purposes
- Acknowledgment must be renewed annually and when the policy is materially updated
- Employees who are uncertain whether a specific AI use is permitted must consult [IT Contact] before proceeding

## Compliance and Monitoring *(NIST CSF: DE.CM-1, DE.CM-7)*
- Monthly review of AI tool and MCP server register by [IT Contact]
- Quarterly audit of AI agent logs for anomalous activity
- Annual review of approved AI tools for continued security posture
- Shadow AI detection via network monitoring and data loss prevention (DLP) tools
- Policy violations reviewed by [Security Officer] and reported to leadership quarterly

## Enforcement
Violation of this policy — including use of unapproved AI tools to process company data, connecting unapproved MCP servers, or entering Restricted data into any AI tool — may result in immediate access suspension, disciplinary action up to and including termination, and potential legal liability for data breaches resulting from the violation. All violations must be reported to [Security Officer].

## References
- NIST CSF v1.1: ID.AM (Asset Management), ID.GV (Governance), ID.SC (Supply Chain), PR.DS (Data Security), PR.AC (Access Control), DE.CM (Continuous Monitoring)
- NIST AI RMF (AI Risk Management Framework) — ai.nist.gov
- OWASP Top 10 for LLM Applications — owasp.org
- Model Context Protocol specification — modelcontextprotocol.io
- EU AI Act (for organizations operating in or serving EU markets)
- CISA guidance on AI cybersecurity

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Security Officer] | Initial release |
