# Advanced Skill & Tool Poisoning Benchmarks for LLM Agents

This document outlines the latest and most advanced GitHub repositories focusing on skill poisoning, tool poisoning, MCP configuration injection, and overall agentic prompt injection, going beyond the foundational `skill-inject` benchmark (published ~2025).

## 1. Ranked Repositories (Most Advanced & Latest First)

| Rank | Repository / Benchmark | Core Focus | Paper / Link | Setup Difficulty |
| :--- | :--- | :--- | :--- | :--- |
| 1 | **MalSkillBench** | Code injection, prompt injection, and hybrid attacks in skills | [lxyeternal/MalSkillBench](https://github.com/lxyeternal/MalSkillBench) | Medium |
| 2 | **InjecAgent** | Tool-integrated IPI (Indirect Prompt Injection) scale | [uiuc-kang-lab/InjecAgent](https://github.com/uiuc-kang-lab/InjecAgent) | Easy |
| 3 | **AgentDojo** | Dynamic security & utility evaluation against IPI via tools | [ethz-spylab/agentdojo](https://github.com/ethz-spylab/agentdojo) | Medium |
| 4 | **ToolSword** | Safety across 3 stages of tool learning (Input, Exec, Feedback)| [ToolSword Paper](https://arxiv.org/abs/2402.10704) | Hard |
| 5 | **HarmfulSkillBench**| Agent refusal rates on malicious/harmful skills | [TrustAIRLab/HarmfulSkillBench](https://github.com/TrustAIRLab/HarmfulSkillBench) | Easy |
| 6 | **SkillHarm** | Fixed-Payload Poisoning (FPP) & Self-Mutating Poisoning (SMP) | [AutoSkillHarm/fixed-payload-poisoning](https://github.com/AutoSkillHarm/fixed-payload-poisoning)| Medium |

---

## 2. Detailed Breakdown of Each Repo

### A. MalSkillBench
* **URL:** `https://github.com/lxyeternal/MalSkillBench`
* **Created/Updated:** Late 2025 / 2026
* **Why it's more advanced:** Unlike `skill-inject` which focuses mainly on contextual and obvious instructions, MalSkillBench is a large-scale, **runtime-verified** benchmark covering code injection, standard prompt injection, and mixed (instruction-code) attacks within skills.
* **Tested Agents:** Various LLM agent frameworks supporting custom code/skills.
* **Runnable:** Yes, includes a runtime execution sandbox.

### B. InjecAgent
* **URL:** `https://github.com/uiuc-kang-lab/InjecAgent`
* **Paper:** "InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents" (Zhan et al.)
* **Why it's more advanced:** Massive scale. Features **1,054 test cases** utilizing 17 user tools and 62 attacker tools. It evaluates over 30 distinct agents (including ReAct and function-calling finetunes).
* **Tested Agents:** GPT-3.5/4, Claude, Llama variants across 30 configurations.
* **Runnable:** Yes, easy to run via provided Python evaluation scripts.

### C. AgentDojo
* **URL:** `https://github.com/ethz-spylab/agentdojo`
* **Paper:** (ETH Zurich & Invariant Labs)
* **Why it's more advanced:** It goes beyond static tests. AgentDojo is an **extensible, dynamic environment** testing both utility (can it do the job?) and security (can it be hijacked?). Used by US/UK AISI for red-teaming Claude 3.5 Sonnet.
* **Tested Agents:** Standard models (GPT-4o, Claude 3.5) with built-in defenses like tool filters and prompt guards.
* **Runnable:** Yes, excellent CLI and documentation.

### D. ToolSword
* **URL:** (Associated with ACL 2024 / GitHub releases for ToolSword)
* **Why it's more advanced:** Examines tool poisoning across a chronological lifecycle: Input (malicious query), Execution (corrupted tool results), and Feedback (conflicting post-execution feedback). 440 targeted test cases.
* **Tested Agents:** General tool-augmented LLMs.
* **Runnable:** Yes, though requires setting up specific evaluation stages.

### E. HarmfulSkillBench
* **URL:** `https://github.com/TrustAIRLab/HarmfulSkillBench`
* **Why it's more advanced:** Shifts the focus slightly to measure how well agents *refuse* 200 harmful skills spread across 20 distinct categories, acting as an audit of agent alignment when exposed to malicious tool definitions.

---

## 3. Comparison Table: skill-inject vs. New Repos

| Feature | `skill-inject` (Baseline) | `MalSkillBench` | `InjecAgent` | `AgentDojo` |
| :--- | :--- | :--- | :--- | :--- |
| **Attack Scale** | ~71 injections, 44 skills | Large-scale | 1,054 test cases | Dynamic suites |
| **Attack Vector Focus** | `SKILL.md` / Agent Configs | Code & Prompt in Skills | Tool-fetched IPI | IPI via Tool Retrieval |
| **Evaluation Method** | Isolated Docker runs | Runtime Sandbox Verification | Scripted Eval across 30 agents| Dynamic environment (Extensible) |
| **Defense Testing** | Ablation studies (Best-of-N) | Included | Built-in | Tool filters, Prompt guards |
| **New Attack Types** | Standard contextual IPI | Mixed Instruction/Code | Tool Exfiltration | Adaptive/Generative Attacks |

---

## 4. Recommendations & Next Steps

**Where to start:**
1. **For pure skill-file / config-file poisoning:** Start with **[MalSkillBench](https://github.com/lxyeternal/MalSkillBench)**. It is the spiritual successor to `skill-inject`, focusing directly on how malicious skills combine code and prompt injection.
2. **For Tool/Function-Calling Poisoning:** Run **[InjecAgent](https://github.com/uiuc-kang-lab/InjecAgent)**. The setup is straightforward, and the 1,054 test cases will give you a comprehensive understanding of indirect prompt injections via tools.
3. **For Advanced/Dynamic Red Teaming:** Look into **[AgentDojo](https://github.com/ethz-spylab/agentdojo)**. If you are building defenses (like MCP security gateways or tool wrappers), AgentDojo allows you to implement custom defenses and test them dynamically.

**Notes on MCP Security:**
If you are looking specifically at Model Context Protocol (MCP) attacks, review open-source auditing tools like `mcp-audit-tool` (audits MCP configs for supply chain risks) and `mcp-fence` (provides agent guardrails against jailbreaks).
