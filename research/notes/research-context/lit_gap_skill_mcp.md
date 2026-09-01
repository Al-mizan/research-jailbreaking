# Literature Gap Analysis: AI Agent Skill, Tool, and MCP Supply-Chain Security

## 1. New Papers (Mid-2026 Onwards)

Based on a review of recent literature beyond the provided list, the following new papers from mid-2026 have been identified:

*   **BadSkill: Backdoor Attacks on Agent Skills via Poisoning (Sun et al., 2026)**
    *   **What it covers:** Explores "model-in-skill" backdoor attacks, demonstrating how corrupted skills or tools can plant hidden backdoors that execute with the ambient privileges of the agent.
    *   **Key gap it leaves:** Focuses primarily on backdoor triggers and payload injection, but lacks comprehensive proposals for dynamic runtime enforcement or cross-model defense transferability.
*   **MCPTox (Xu & Yan, 2026)**
    *   **What it covers:** Introduces a benchmarking framework specifically designed for evaluating tool poisoning vulnerabilities across real-world Model Context Protocol (MCP) servers.
    *   **Key gap it leaves:** As an evaluation suite, it highlights vulnerabilities on the server side but leaves the implementation of active, agent-side runtime defenses unaddressed. It also does not deeply explore cross-agent framework dynamics.
*   **AgentCanary (2026)**
    *   **What it covers:** Provides a security evaluation framework and benchmark for autonomous agents operating in executable, realistic environments.
    *   **Key gap it leaves:** Maintains a broad scope on general agent execution security rather than exclusively addressing the nuances of the MCP or skill supply chain.
*   **CapSeal (2026)**
    *   **What it covers:** Proposes a "Capability-Sealed" secret mediation architecture, using cryptographic defenses to prevent agents from mishandling low-level credentials in MCP workflows.
    *   **Key gap it leaves:** Narrowly focused on secret and credential leakage; largely ignores arbitrary command execution, semantic prompt poisoning in skills, or living-off-the-land attacks.

## 2. Attack Surfaces: Benchmarked vs. Untested

*   **Thoroughly Benchmarked:** Tool description poisoning (manipulating schemas/metadata), static skill file injection (e.g., malicious payloads in `SKILL.md` or configuration files), basic confused deputy attacks (e.g., unauthorized file read/write), and credential exposure via poorly authenticated MCP servers.
*   **Largely Untested:** Dynamic payload injection during complex, multi-tool workflows, stateful protocol manipulation (and how agent memory retains poisoned context over long sessions), and "living-off-the-land" attacks where malicious MCP servers weaponize legitimate, signed system binaries (e.g., `node`, `curl`) to bypass EDR/DLP.

## 3. Defense Mechanisms: Existing vs. Gaps

*   **Existing Defenses:** Cryptographic mediation for secrets (e.g., CapSeal), static application security testing (SAST) for MCP server code, basic OAuth integration (though adoption is low, ~8.5%), the establishment of the OWASP MCP Top 10, and updates to the MCP specification to enforce a stateless core.
*   **Defense Gaps:** Semantic validation of tool outputs before they are ingested into an agent's context window. There is a distinct lack of robust integrity checks for natural language instructions in tool metadata, and defenses against fileless exfiltration via the agent's trusted execution environment remain weak.

## 4. Runtime Enforcement / Authorization / Least-Privilege

**Status: Still largely OPEN.**
While theoretical frameworks like "agentic governance" and broad least-privilege policies are frequently mentioned in 2026 literature, granular runtime enforcement remains poorly studied and thinly implemented. Most current defenses are static (e.g., blocking a known bad server). Dynamic, context-aware authorization—such as approving specific, high-risk actions in real-time without causing severe user prompt fatigue—is still an open research problem. 

## 5. Comprehensive Cross-Agent, Cross-Model Benchmarking

**Status: Still OPEN.**
While benchmarks like *MCPTox* evaluate tool poisoning on MCP servers and *AgentCanary* evaluates general agent environments, there is currently no comprehensive study that maps how different foundational models (e.g., GPT-4o vs. Claude 3.5 Sonnet vs. Llama 3) react to the exact same skill poisoning vectors across different agent architectures (e.g., AutoGen vs. LangChain vs. Antigravity).

---

## Summary: Saturated vs. Open Aspects

### Saturated Aspects
*   **Conceptual Threat Modeling:** The theoretical risks of MCP and skill poisoning (confused deputy, ambient authority, tool description manipulation) are well-documented.
*   **Static Vulnerability Identification:** Finding hardcoded credentials, path traversal, and command injection flaws in MCP server implementations.
*   **Basic Prompt/Schema Injection:** Demonstrating that an agent will follow malicious instructions if they are placed in a tool's description.

### Open Aspects
*   **Semantic Context Defense:** Filtering and sanitizing the natural language outputs of tools *before* they influence the agent's reasoning process.
*   **Dynamic Runtime Authorization:** Creating usable, low-friction least-privilege enforcement mechanisms for agents during active execution.
*   **Cross-Ecosystem Benchmarking:** Large-scale empirical studies comparing the resilience of different LLMs and agent frameworks to standardized supply-chain poisoning attacks.
*   **Living-off-the-Land (LotL) Agent Attacks:** Detecting and mitigating attacks where the agent is manipulated into using legitimate system tools for malicious purposes.
