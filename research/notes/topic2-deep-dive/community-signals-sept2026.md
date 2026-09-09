# Community Signals & Threat Intelligence: August–September 2026
**Focus:** MCP Security, Skill Scanners, Cross-Lingual Injection, Claude Code `SKILL.md`, and Gemini CLI Security

---

`🌐 last30days · synced September 2026`

## Executive Summary & Research Gap Verification

Across Reddit (`r/LocalLLaMA`, `r/Netsec`, `r/MachineLearning`), Hacker News, GitHub, and X/Twitter over the last 30 days (August–September 2026), the developer and security communities are grappling with the shift from traditional software vulnerabilities to **Agentic Supply-Chain & Context Poisoning**.

### The Core Finding for Our Research:
**There is a near-total community and industry blindspot regarding multilingual / cross-lingual skill attacks.**
1. **Security Scanners are English-Centric:** All newly emerged scanners (NVIDIA SkillSpector, Snyk Agent Scan, Aguara, Cisco AI Agent Security Scanner) rely on English AST/regex heuristics or English-prompted LLM judges.
2. **The Only Academic Study (Zhang et al., ACM CAIS 2026):** Confirmed that non-English skills trigger 3–5× more false-positive "behavioral flags" due to scanner calibration bias, but only conducted static analysis on 3,656 skills—leaving **runtime exploitation completely untested**.
3. **Bifurcated Discourse:** Cross-lingual prompt injection is heavily discussed for direct chatbot jailbreaks and LLM-as-a-judge score manipulation, while MCP and agent skill security is discussed purely in an English system context. Nobody in the community has benchmarked or demonstrated runtime cross-lingual tool execution hijacking or skill poisoning.

---

## 1. Topic-by-Topic Intelligence

### Topic 1: MCP Security Vulnerabilities & Skill/Tool Injection
* **Community Pulse:**
  * **Hacker News:** Intense debates treating MCP as a "wire protocol" (like HTTP/TCP) rather than an inherently secure system. Commenters emphasize that MCP servers grant agents "God Mode" over local environments without native authentication, authorization, or audit logging.
  * **Reddit (`r/LocalLLaMA`):** Focus on the "Capability-Vulnerability Paradox"—models with stronger tool-use capabilities are more susceptible to indirect prompt injection and tool shadowing.
  * **X/Twitter & Cloud Security Alliance:** Discussion of the OWASP MCP Top 10 initiative and "Tool Poisoning" (manipulating tool descriptions/schemas to induce unauthorized function execution).
* **Architectural Shifts & Defenses:**
  * **AIP (Agent Identity Protocol):** A "Little Snitch"-style security proxy sitting between client and MCP server providing deep argument inspection and manifest-driven authorization.
  * **Driftcop:** Designed to counter "MCP rug pull attacks," detecting when MCP tool definitions or schemas mutate post-approval and requiring cryptographic re-authorization.
  * **CapSeal & Cordon:** Capability tokens and semantic transaction staging with rollback mechanisms.

### Topic 2: Agent Skill Marketplace Security Scanners
* **Community Pulse:**
  * Recognition that `SKILL.md` and MCP tools represent "natural language payloads"—malicious behavior often does not exist in traditional machine code until the LLM synthesizes it at runtime. Static AST analysis alone consistently fails.
  * High friction over "Alert Fatigue" in IDEs, pushing developers toward automated CI/CD scanner actions and formal verification.
* **New Scanners & Tooling (Released or Trending in 2026):**
  * **NVIDIA SkillSpector (Open-Source):** Two-stage scanner with fast static analysis (AST, YARA, OSV.dev) + LLM-based semantic validation across 71 vulnerability patterns. Employs anti-jailbreak protections for the evaluator LLM itself.
  * **Snyk Agent Scan:** Local discovery and vulnerability scanner for installed MCP servers and agent skills, focusing on credential leakage and prompt injection patterns.
  * **Aguara:** Go-based static analyzer for `SKILL.md`, YAML, and JSON skill definitions, executing completely offline without LLM API overhead.
  * **ClawCare:** Dual-layer system: static pre-commit linting + runtime execution hook that intercepts tool invocations in real-time.
  * **SkillFortify:** Applies formal verification to verify whether an agent skill's capabilities mathematically align with its stated documentation.
  * **SkillSecurer:** Red/Blue agentic framework that dynamically crafts context-compatible injections to test skill robustness and automatically suggest patches.
  * **OpenACA & AgentsArk:** Automated scanning against centralized CVE databases (OSV.dev) to catch vulnerable dependencies in agent harnesses.

### Topic 3: Cross-Lingual Prompt Injection in LLMs & Agents
* **Community Pulse:**
  * Cross-lingual injection is recognized as the premier evasion technique against safety guardrails (ranked under OWASP LLM01:2025/2026).
  * Attackers exploit the fact that safety guardrails, moderation APIs, and semantic firewalls are heavily optimized for English.
  * **Mechanism:** Malicious instructions translated into low-resource or non-English languages (e.g., Bangla, Hindi, Japanese, German) bypass regex and lightweight semantic filters. When combined with "exfiltrate data in language X", it simultaneously evades English-only PII data loss prevention (DLP) scanners.
  * **Unicode / Invisible Attacks:** Hacker News discussions highlight invisible token attacks, zero-width characters, and non-Latin homoglyphs that slip through tokenizers, leading to calls for deterministic cross-language linters.
  * **The Gap:** Discussions are 99% concentrated on direct user prompts, RAG document injection, and LLM judge distortion. Agentic tool metadata in non-English remains completely unaddressed by practitioners.

### Topic 4: Claude Code `SKILL.md` Security
* **Community Pulse:**
  * Claude Code's progressive disclosure model (loading `SKILL.md` only on demand) is praised for context efficiency, but flagged on Hacker News and Reddit as an uncontrolled supply-chain vector ("Agent Context Poisoning").
  * Developer consensus on HN: Native permission prompts provide a false sense of security due to user click-through fatigue. Developers strongly recommend running Claude Code inside hardened containers (Docker, Kata, microVMs) rather than relying on application-level guardrails.
* **Major Incidents & Disclosures (2026):**
  * **March 2026 Source Code Leak:** Accidental inclusion of source maps in an npm release package exposed proprietary Claude Code internal logic.
  * **Anthropic "Claude Code Security" Preview:** Research preview released to automate vulnerability finding and patch generation.

### Topic 5: Gemini CLI / Antigravity Skills Security
* **Community Pulse:**
  * Focus on the transition toward the unified Google Antigravity platform.
  * Gemini CLI relies on progressive disclosure (`SKILL.md` descriptions visible upfront, full contents and scripts loaded upon user-authorized activation).
  * Critical security friction in CI/CD automation: Headless usage with `--consent` or `--yolo` flags eliminates human review, turning indirect prompt injection into instant Remote Code Execution.

---

## 2. CVEs and Security Advisories Summary Table

| CVE / Advisory ID | Target / Affected System | Severity | Vulnerability Mechanism | Impact |
|:---|:---|:---|:---|:---|
| **CVE-2026-12537** *(GHSA-wpqr-6v78-jr5g)* | Gemini CLI (<0.39.1) & `run-gemini-cli` Action (<0.1.22) | **CVSS 10.0** (Critical) | Workspace trust bypass & tool allowlist flaw in `--yolo` / CI/CD mode | Full host-level RCE and secret exfiltration from CI/CD pipeline |
| **CVE-2026-59950** | MCP Python SDK (<1.28.1) | Medium / High | Missing Host/Origin header validation in WebSocket transport | Cross-site unauthorized WebSocket connections to local MCP servers |
| **CVE-2026-55607** | Claude Code | High | Git worktree config manipulation (`core.fsmonitor`) | Pre-execution RCE triggered before user approval prompts |
| **CVE-2026-24887** | Claude Code | High | Command injection via unsanitized parameter expansion | Execution of arbitrary system commands bypassing user approval |
| **CVE-2026-25723 / 25725** | Claude Code | Medium / High | Improper `sed` command validation & sandbox bypass | Unauthorized file system mutation and escape from restricted working paths |
| **CVE-2026-25724** | Claude Code | Medium | Directory traversal via symbolic links | Agent reads files outside project workspace boundaries |
| **CVE-2026-21852** | Claude Code | High | Unrestricted environment variable manipulation (`ANTHROPIC_BASE_URL`) | Redirection of traffic and exfiltration of API credentials to attacker servers |
| **CVE-2026-17623 / 17625 / 17626 / 17630** | Langflow OSS (MCP Integration) | High | OS command injection & improper file path validation | Arbitrary command execution via maliciously structured MCP tool schemas |
| **CVE-2026-19753** | `mcp-rdf-explorer` (v1.0.0) | High | Server-Side Request Forgery (SSRF) in tool endpoint | Internal network probing and service compromise |
| **CVE-2025-6514** | `mcp-remote` | **CVSS 9.6** (Critical) | OS command injection in remote agent invocation | Unauthorized remote shell execution |
| **CVE-2025-68143** | MCP Server Implementations | High | Arbitrary Path Traversal | Read/write access to sensitive files (`.env`, `id_rsa`) |

---

## 3. Key Research Gap Confirmation

### Is anyone talking about multilingual / cross-lingual skill attacks specifically?
* **No practical community discussion exists.**
* In developer forums, "cross-lingual" is exclusively discussed in terms of positive functionality (translation skills, cross-lingual routing) or generic chatbot jailbreaks (translating bomb recipes to Zulu/Bangla).
* **The lone academic touchpoint is Zhang et al. (AgentSkills @ ACM CAIS 2026):**
  * Statically audited 3,656 skills across 8 languages.
  * Found that non-English skills trigger 3–5× more behavioral warnings (Japanese: 31.7% vs English: 6.1%), but demonstrated this is due to **scanner calibration bias**.
  * Code vulnerabilities were roughly equal (~2.3%).
  * **Critical Gap:** They conducted **zero runtime exploitation**. They did not test whether agents executing non-English skills actually suffer from higher hijacking rates, tool poisoning, or unauthorized execution.

### New security scanners for agent skills
* **Static Scanners:** Aguara (Go), OpenACA (CVE-focused), Cisco AI Agent Security Scanner.
* **Hybrid (Static + LLM):** NVIDIA SkillSpector (71 rules, AST + LLM semantic filtering), Snyk Agent Scan.
* **Dynamic / Agentic:** SkillSecurer (Red/Blue multi-agent testing), AgentSeal (150+ adversarial probes).
* **Runtime Guards:** ClawCare, Driftcop, G0.
* **All English-centric.** None reports multilingual calibration or evaluation.

---

## 4. Strategic Validation for Topic 2

The community intelligence provides **rock-solid justification** for the proposed research:

1. **Massive Defensibility:** The industry is heavily investing in skill scanners (NVIDIA, Snyk, Cisco), yet all are calibrated strictly on English.
2. **Exploiting the Architectural Weakness:** Because tools like SkillSpector use LLM evaluators to filter false positives, multilingual payloads can potentially bypass both the static AST checks AND the secondary LLM semantic filter.
3. **High Practical Impact:** With CI/CD systems adopting Gemini CLI and Claude Code at scale, demonstrating that a non-English `SKILL.md` can reliably trigger unauthorized tool execution addresses an urgent real-world security vulnerability.
