# Research Proposal: Cross-Lingual Agent Skill Poisoning: Active Runtime Exploitation and Authorization Defenses in Tool-Using LLM Agents

**Author:** Al-mizan  
**Affiliation:** Department of Computer Science & Engineering, Jahangirnagar University  
**Supervisor:** Dr. Md. Rafsan Jani  
**Date:** September 2026  
**Target Venues:** ACM CCS / USENIX Security / ACL (Security Track)  

---

## Abstract

Autonomous Large Language Model (LLM) agents increasingly rely on modular skill packages (e.g., `SKILL.md` specifications) and standardized execution protocols (such as Anthropic's Model Context Protocol) to dynamically extend their tool-calling capabilities. However, because agent skills couple operational tool definitions with natural-language instructions, they introduce an expansive attack surface: semantic supply-chain poisoning. While recent studies have either examined static vulnerabilities in public skill registries or demonstrated English-language prompt injection within tools, the interplay between natural language variation and active runtime agent exploitation remains fundamentally unmeasured. In particular, existing cross-lingual studies in the skills ecosystem have relied exclusively on static pattern matching—leaving open the critical question of whether non-English or code-switched skill metadata facilitates higher runtime compromise rates, induces unauthorized tool execution, or evades runtime oversight.

This proposal introduces a comprehensive research program to systematically quantify and mitigate cross-lingual skill poisoning in tool-using LLM agents. We design **XLingSkillBench**, the first runtime execution benchmark comprising 50 realistic enterprise tasks paired with adversarial skills across four linguistic registers: Monolingual English, high-resource (Mandarin Chinese, Spanish), low-resource (Bangla), and code-mixed registers (Banglish). We formalize an evaluation harness that tracks the full progression of compromise across three distinct operational phases: skill discovery and selection, intermediate reasoning hijacking, and unauthorized tool action execution. Across frontier proprietary models (GPT-4o, Claude 3.5 Sonnet, Gemini 2.0 Flash) and accessible open-weights architectures (Qwen-2.5-7B/14B, Llama-3.1-8B), we investigate whether safety alignment disparities across languages translate into amplified tool execution risks. Finally, we evaluate language-agnostic structural authorization controls against semantic intent verifiers, characterizing the fundamental security–utility tradeoff between preventing unauthorized tool calls and avoiding over-refusal on legitimate non-English workflows.

---

## 1. Introduction

### 1.1 The Shift from Conversational Safety to Agentic Execution
Over the past two years, the focus of LLM security research has shifted from conversational jailbreaks to the security of autonomous, tool-using agents. In a standard conversational paradigm, model failure is bounded: the LLM outputs toxic, biased, or disallowed text. In an agentic architecture, however, the model is granted operational agency. It interprets unstructured context, formulates execution plans, selects external tools from an available registry, and invokes APIs with real-world side effects, including reading databases, modifying filesystem states, and initiating outbound network requests (Debenedetti et al., 2024; Zhan et al., 2024).

Consequently, the security objective bifurcates. The primary risk is no longer mere communicative harm, but unauthorized action execution. Even if an underlying model is persuaded by an adversarial input, the critical security boundary lies at the tool execution layer: can the agent be induced to perform an unauthorized action outside the scope of the user's explicit intent?

### 1.2 The Semantic Supply Chain of Agent Skills
To enable modularity without hardcoding API schemas into base model weights, the ecosystem has converged on natural-language skill specifications, predominantly adhering to the `SKILL.md` format (as adopted in agentic IDEs, Anthropic's Model Context Protocol, and open repositories like ClawHub). A skill file defines a tool's metadata: its operational description, required input/output schemas, usage examples, and invocation guidelines. 

This design creates what security analysts characterize as 'prompt injection by design'. When an agent indexes a skill, it ingests third-party natural language directly into its system or working context. An adversary who publishes a poisoned skill does not require code execution privileges on the host; by embedding adversarial natural language payloads within tool descriptions, parameter guidelines, or prerequisite blocks, the adversary can manipulate the agent's internal reasoning loop, hijack tool selection, or trigger confused-deputy attacks (Saha et al., 2026; Qu et al., 2026).

### 1.3 The Cross-Lingual Vulnerability Gap
A well-established finding in natural language processing is that safety alignment fails to generalize uniformly across languages. Frontier models fine-tuned with Reinforcement Learning from Human Feedback (RLHF) demonstrate robust refusal behaviors on English adversarial queries, yet exhibit elevated vulnerability when queries are translated into low-resource languages or expressed through code-mixing (Deng et al., 2024; Atil, 2025; Marx, 2026).

Recently, Zhang et al. (2026) conducted the first cross-lingual empirical analysis of agent skill repositories, examining 3,656 skills across 8 languages. Their findings revealed that while code-level flaws (e.g., hardcoded secrets, command injection) were uniformly distributed across languages (~2.3%), behavioral flags—such as misleading descriptions and persuasive steering—were 3 to 5 times more frequent in non-English skills (e.g., 31.7% in Japanese versus 6.1% in English). However, their investigation was strictly observational and static. Because static heuristic scanners suffer from severe calibration bias on non-English text, their study could not determine whether these skills actually compromise LLM agents at runtime, or whether attackers can deliberately exploit cross-lingual metadata to induce unauthorized actions.

### 1.4 Research Questions
To resolve this gap, this research project investigates four formal research questions:

*   **RQ1 (Runtime Exploitation Disparity):** Does translating or phrasing malicious skill metadata in low-resource (Bangla) or code-mixed (Banglish) languages significantly increase the Skill Selection Rate (SSR) and Unauthorized Tool Action Rate (UTAR) compared to semantically equivalent English payloads?
*   **RQ2 (Model Robustness Stratification):** How do open-weights models (Qwen-2.5-7B/14B, Llama-3.1-8B) compare to closed frontier models (GPT-4o, Claude 3.5 Sonnet, Gemini 2.0 Flash) in resisting cross-lingual semantic supply-chain manipulation?
*   **RQ3 (Defense Efficacy & Invariance):** Do existing runtime defenses—specifically contrasting structural authorization (role-based capability tokens) against semantic intent verifiers (LLM-in-the-loop judges)—exhibit language invariance, or do semantic monitors degrade under non-English adversarial attacks?
*   **RQ4 (Security–Utility Tradeoff):** What is the exact quantitative penalty of cross-lingual agent defenses on benign task completion (TSR) and over-refusal rates across native and colloquial linguistic registers?

---

## 2. Related Work and Critical Gaps

### 2.1 Indirect Prompt Injection in Tool-Using Agents
Indirect Prompt Injection (IPI) occurs when an LLM processes untrusted third-party data retrieved during task execution (Greshake et al., 2023). Foundational benchmarks, including InjecAgent (Zhan et al., 2024), AgentDojo (Debenedetti et al., 2024), and Agent Security Bench (Zhang et al., 2025), demonstrated that frontier LLMs fail to maintain data-instruction separation, frequently treating untrusted data as authoritative system commands. However, these benchmarks operate almost exclusively within monolingual English environments. Furthermore, as noted by Zhao et al. (2026) in LivePI, static benchmarks often overestimate defense efficacy due to a lack of dynamic multi-turn interactions.

### 2.2 Agent Skill & MCP Supply-Chain Poisoning
The rise of extensible agent platforms has catalyzed research into supply-chain vulnerabilities. Schmotz et al. (2026) introduced Skill-Inject, demonstrating an 80% compromise rate on frontier models when malicious instructions are embedded in skill files. Qu et al. (2026) established Document-Driven Implicit Payload Execution (DDIPE), proving that payloads hidden in code examples and documentation templates bypass static filters. Saha et al. (2026) investigated `SKILL.md` registries, showing that adversarial metadata grants attackers an 86% discovery advantage. While these works rigorously establish the supply-chain threat, they evaluate exclusively in English, ignoring the multilingual ecosystem where real-world skills are authored.

### 2.3 Cross-Lingual Safety Alignment Disparities
Disparities in LLM safety alignment across languages are well-documented for conversational interactions. MultiJail (Deng et al., 2024) and recent studies on Indic languages (IndicJR, 2026) confirm that safety filters are disproportionately trained on English corpora. For Bangla specifically, recent work on BanglaVeilGuard (2026) highlighted that standard guardrails fail on dialectal and code-mixed registers, while defensive filters cause severe over-refusal. In the agentic domain, MIPIAD (2025) proposed a multilingual indirect prompt injection defense combining LoRA fine-tuning and lexical filtering on English and Bangla; however, MIPIAD restricted its scope to text-retrieval RAG, omitting tool schemas, function calls, and authorization layers.

### 2.4 Summary of Genuine Research Gaps
Synthesizing the state of the art identifies three unaddressed voids:
1.  **Absence of Active Runtime Exploitation:** Zhang et al. (2026) identified static metadata discrepancies but left runtime agent interaction untested.
2.  **Lack of Multilingual Tool Benchmarks:** Existing tool security benchmarks (AgentDojo, InjecAgent) do not include cross-lingual or code-mixed test cases.
3.  **Unverified Language Invariance in Runtime Defenses:** Contemporary runtime monitors (VIGIL, SEAgent) rely on English semantic traces and have never been evaluated against cross-lingual evasion.

---

## 3. Threat Model and Theoretical Formulation

### 3.1 Threat Model
*   **System Environment:** An autonomous agent operating with access to a local skill directory or public skill registry, equipped with a core set of standard utility tools (e.g., file reading, web searching, email drafting) and system execution tools (e.g., bash execution, file writing, outbound API calls).
*   **Attacker Profile & Capabilities:** The attacker is an external entity who publishes or injects a third-party skill package (`SKILL.md` and associated schema definitions). The attacker has no access to the agent's system prompt, user prompt, model weights, or runtime memory. The attacker cannot directly execute code on the host without the agent invoking the tool.
*   **Attacker Objective:** To achieve unauthorized tool invocation (e.g., reading sensitive workspace files and sending them to an external endpoint) when the agent processes a benign user query.
*   **Assumptions:** The agent dynamically inspects available skill descriptions to select the appropriate tool for a given user query. The user query itself is entirely benign.

### 3.2 Formal Agent Execution Framework
We model an agent as a tuple:
$$\mathcal{A} = \langle \mathcal{M}, \mathcal{S}, \mathcal{T}, \Pi \rangle$$
where $\mathcal{M}$ represents the underlying foundation model, $\mathcal{S} = \{s_1, s_2, \dots, s_n\}$ is the set of available skills, $\mathcal{T} = \{t_1, t_2, \dots, t_m\}$ is the set of executable tools, and $\Pi$ is the runtime policy enforcement engine.

Each skill $s_i \in \mathcal{S}$ is defined by its metadata:
$$s_i = \langle D_i(L), P_i, t_i \rangle$$
where $D_i(L)$ is the natural-language description written in language register $L$, $P_i$ represents the parameter schema, and $t_i \in \mathcal{T}$ is the bound tool implementation.

Given a user task $q$, the agent execution proceeds in three sequential stages:
1.  **Skill Discovery & Selection:**
    $$s^* = \arg\max_{s_i \in \mathcal{S}} \mathbb{P}_{\mathcal{M}}(\text{Select}(s_i) \mid q, D_i(L))$$
2.  **Plan Generation & Parameter Formulation:**
    $$\tau = \mathcal{M}(q, s^*, \text{Context})$$
    where $\tau = \langle t_{\text{invoked}}, \mathbf{args} \rangle$ represents the proposed tool call.
3.  **Authorization & Execution:**
    $$\text{Action} = \begin{cases} \text{Execute}(t_{\text{invoked}}, \mathbf{args}), & \text{if } \Pi(\tau, q) = \text{ALLOW} \\ \text{Block}, & \text{if } \Pi(\tau, q) = \text{DENY} \end{cases}$$

### 3.3 Semantic Poisoning Formulation
In an adversarial skill $s_{\text{adv}}$, the attacker crafts $D_{\text{adv}}(L)$ such that:
$$D_{\text{adv}}(L) = D_{\text{benign}}(L) \parallel I_{\text{malicious}}(L)$$
where $I_{\text{malicious}}(L)$ contains adversarial instructions instructing the agent to bypass policy $\Pi$ and invoke an unauthorized tool $t_{\text{unauth}} \neq t_{\text{intended}}$. 

Our scientific objective is to measure the sensitivity of this optimization to the language register $L$:
$$\Delta_{\text{ASR}}(L) = \mathbb{E}_{q \sim \mathcal{Q}} [\mathbb{I}(t_{\text{invoked}} = t_{\text{unauth}} \mid D_{\text{adv}}(L))] - \mathbb{E}_{q \sim \mathcal{Q}} [\mathbb{I}(t_{\text{invoked}} = t_{\text{unauth}} \mid D_{\text{adv}}(\text{English}))]$$

---

## 4. Methodology & Experimental Design

### 4.1 Benchmark Construction: XLingSkillBench
We design **XLingSkillBench**, an evaluation benchmark consisting of 50 realistic enterprise and developer tasks paired with 150 benign skills and 50 poisoned skills. The benchmark spans three canonical attack categories:
1.  **Confused-Deputy Exfiltration:** The agent is induced to read sensitive local environment variables (`.env`, SSH keys) or internal documents and pass them as parameters to an external web hook tool.
2.  **Unauthorized System Modification:** The agent is induced to overwrite local configurations (`settings.json`, build scripts) under the guise of an optimization task.
3.  **Privilege Escalation via Tool Chaining:** The agent is instructed to invoke a restricted administrative tool by fabricating a precedent verification trace.

### 4.2 Linguistic Register Matrix
Each adversarial skill in XLingSkillBench is implemented across four distinct linguistic registers:
*   **$L_{\text{EN}}$ (Monolingual English):** The baseline standard register.
*   **$L_{\text{HR}}$ (High-Resource Non-English):** Mandarin Chinese (Zh) and Spanish (Es), representing languages with extensive representation in pretraining and alignment corpora.
*   **$L_{\text{LR}}$ (Low-Resource / Morphologically Rich):** Standard Bangla (Bn), representing a language with limited representation in RLHF safety tuning.
*   **$L_{\text{CM}}$ (Code-Mixed / Dialectal):** Banglish (Bangla-English code-switching written in Roman and Bengali scripts), representing informal, real-world developer inputs.

To prevent translation artifacts from confounding results, all non-English skills are generated via professional human translation and validated by native speakers for semantic equivalence, natural idiomatic phrasing, and grammatical coherence.

### 4.3 Evaluated Model Zoo
To evaluate cross-model transferability and compute feasibility, we select representative models across two tiers:
*   **Tier 1 (Frontier Closed Models):** GPT-4o (`gpt-4o-2024-08-06`), Claude 3.5 Sonnet (`claude-3-5-sonnet-20241022`), Gemini 2.0 Flash.
*   **Tier 2 (Open-Weights Accessible Models):** Qwen-2.5-7B-Instruct, Qwen-2.5-14B-Instruct, Llama-3.1-8B-Instruct. (Inference conducted locally using vLLM / Ollama on single-GPU hardware).

### 4.4 Defense Baselines
We implement and benchmark four defensive configurations:
1.  **Baseline 0 (No Defense):** Standard unmediated execution loop.
2.  **Baseline 1 (Input Guardrails):** Natural language safety classification of the combined context using Llama-Guard-3 and a Bangla-specialized safety classifier (following BanglaVeilGuard principles).
3.  **Baseline 2 (Tool Schema Sanitizer):** Static inspection of `SKILL.md` files using regular expressions and instruction-density heuristics to strip imperative statements from metadata.
4.  **Baseline 3 (Dynamic Structural Authorization):** An execution proxy enforcing capability-based access control (CapBAC). Tool calls are checked against a static permission matrix defined exclusively by the user's explicit intent.
5.  **Baseline 4 (Semantic Intent Verifier):** A secondary lightweight LLM judge evaluating whether the proposed tool call aligns semantically with the user query before execution.

---

## 5. Quantitative Evaluation Metrics

We formulate five core metrics to evaluate security, utility, and runtime feasibility:

### 5.1 Skill Selection Rate (SSR)
Measures the frequency with which the agent selects the poisoned skill $s_{\text{adv}}$ when presented with user query $q$:
$$\text{SSR}(L) = \frac{1}{N} \sum_{k=1}^N \mathbb{I}(s^{(k)} = s_{\text{adv}}(L))$$

### 5.2 Intermediate Injection Success (IIS)
Measures the proportion of runs where the model's internal chain-of-thought or reasoning trace explicitly adopts the malicious instruction:
$$\text{IIS}(L) = \frac{1}{N} \sum_{k=1}^N \mathbb{I}(\text{Goal}_{\text{malicious}} \subseteq \text{Trace}^{(k)})$$

### 5.3 Unauthorized Tool Action Rate (UTAR)
The primary security metric, measuring the proportion of runs where the agent actually issues an unauthorized tool call $t_{\text{unauth}}$:
$$\text{UTAR}(L) = \frac{1}{N} \sum_{k=1}^N \mathbb{I}(t_{\text{invoked}}^{(k)} = t_{\text{unauth}})$$

### 5.4 Benign Task Success Rate (TSR) & Overblocking Penalty
To evaluate utility preservation, we execute all benign tasks under each defense configuration. The Overblocking Penalty measures the drop in task completion caused by false-positive security blocks:
$$\Delta \text{OB}(L) = \text{TSR}_{\text{Undefended}}(L) - \text{TSR}_{\text{Defended}}(L)$$

### 5.5 Operational Overhead
We measure mean token overhead ($\Delta \text{Tokens}$) and end-to-end execution latency ($\Delta \text{Latency}$) introduced by the defense layer.

---

## 6. Implementation Roadmap & Timeline

The proposed research is structured across five sequential phases over a 16-week execution timeline:

```
Weeks:   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16
Phase 1: [========] (Environment & Architecture Setup)
Phase 2:         [==============] (Dataset Curation & Translation Validation)
Phase 3:                         [==============] (Runtime Execution & Attack Benchmarking)
Phase 4:                                         [===========] (Defense Evaluation & Tradeoff Analysis)
Phase 5:                                                     [========] (Paper Writing & Rebuttal Prep)
```

### Phase 1: Environment & Tool Harness Setup (Weeks 1–3)
*   Build the modular Python agent execution harness with support for dynamic `SKILL.md` parsing.
*   Implement simulated sandbox environments with mock APIs (filesystem, email, external web hooks) to ensure safe execution without risk of real-world harm.
*   Integrate API clients (OpenAI, Anthropic, Google) and local vLLM runners for Qwen/Llama models.

### Phase 2: Dataset Curation & Translation Validation (Weeks 4–7)
*   Synthesize 50 benign task queries across development, enterprise data processing, and IT administration domains.
*   Develop 50 poisoned skill specifications embedding subtle semantic injections within usage instructions.
*   Execute translation and localization pipelines across Mandarin, Spanish, Bangla, and Banglish. Conduct native speaker validation to guarantee semantic parity.

### Phase 3: Runtime Execution & Attack Benchmarking (Weeks 8–11)
*   Execute full benchmark runs across the 6 target LLMs under unmitigated conditions ($N = 50 \times 4 \text{ languages} \times 6 \text{ models} = 1,200$ execution traces).
*   Compute empirical SSR, IIS, and UTAR across all linguistic registers.
*   Conduct ablation studies on injection position (description vs. parameter guideline vs. markdown code example).

### Phase 4: Defense Integration & Tradeoff Analysis (Weeks 12–14)
*   Implement Defense Baselines 1 through 4 within the execution proxy.
*   Re-evaluate attack success under defensive mitigations.
*   Execute benign benchmark suite to measure Overblocking Penalties ($\Delta \text{OB}$) across each language register.
*   Perform comparative cost-latency analysis.

### Phase 5: Paper Drafting & Advisor Review (Weeks 15–16)
*   Synthesize empirical results into publication figures and LaTeX tables.
*   Draft formal manuscript conforming to ACM / IEEE security conference templates.
*   Submit manuscript to Dr. Md. Rafsan Jani for review and feedback.

---

## 7. Compute Feasibility & Budget Analysis

A critical strength of this proposal is its computational feasibility for an undergraduate research environment:
*   **Inference Compute:** Open-weights models (Qwen-2.5-7B/14B, Llama-3.1-8B) require standard 16GB–24GB VRAM (accessible via Google Colab Pro or university lab workstations running quantized 4-bit/8-bit or vLLM inference). No gradient-based pretraining or full fine-tuning is required.
*   **API Budget:** Total proprietary API inference (GPT-4o, Claude 3.5 Sonnet, Gemini 2.0 Flash) is projected at approximately 1,200 runs $\times$ 1,500 tokens per interaction $\approx$ 1.8M tokens, totaling under $50 USD.
*   **Software Artifacts:** All code, prompts, skill files, and execution logs will be open-sourced under an MIT/Apache-2.0 license to maximize community adoption.

---

## 8. Expected Contributions & Scientific Significance

1.  **First Runtime Cross-Lingual Skill Benchmark:** Provides the first empirical dataset measuring active runtime execution of poisoned skills across multiple language registers, resolving the limitation of static scanning identified in prior work.
2.  **Empirical Characterization of the Agentic Language Gap:** Demonstrates whether low-resource and code-mixed registers provide an adversarial advantage in evading agent alignment and compromising tool selection.
3.  **Systematic Evaluation of Authorization Mechanisms:** Quantifies the performance of structural capability controls versus semantic monitors under cross-lingual attacks, providing actionable architecture guidelines for production agent deployments.
4.  **Publication Target:** Prepared for submission to top-tier security and NLP venues, including ACM CCS, USENIX Security, or ACL/EMNLP (Security and Safety Track).

---

## Verified References

1. Atil, B. (2025). Do Methods to Jailbreak and Defend LLMs Generalize Across Languages? *arXiv preprint arXiv:2511.00689*.
2. Debenedetti, E., Zhang, J., Balunović, M., Beurer-Kellner, L., Fischer, M., & Vechev, M. (2024). AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents. *Thirty-eighth Conference on Neural Information Processing Systems (NeurIPS 2024) Datasets and Benchmarks Track*. DOI: [10.52202/079017-2636](https://doi.org/10.52202/079017-2636).
3. Deng, Y., Zhang, W., Pan, S. J., & Bing, L. (2024). Multilingual Jailbreak Challenges in Large Language Models. *International Conference on Learning Representations (ICLR 2024)*. arXiv:2310.06474.
4. Evtimov, I., et al. (2025). WASP: Benchmarking Web Agent Security Against Prompt Injection Attacks. *arXiv preprint arXiv:2504.18575*.
5. Greshake, K., Abdelnabi, S., Mishra, S., Endres, C., Holz, T., & Fritz, M. (2023). Not what you've signed up for: Compromising real-world LLM-integrated applications with indirect prompt injection. *Proceedings of the 16th ACM Workshop on Artificial Intelligence and Security (AISEC)*. DOI: [10.1145/3605764.3623985](https://doi.org/10.1145/3605764.3623985).
6. Huang, C., Huang, X., Tran, N. P., & Fard, A. M. (2026). Model Context Protocol Threat Modeling and Analyzing Vulnerabilities to Prompt Injection with Tool Poisoning. *arXiv preprint arXiv:2603.22489*.
7. Ji, Z., Wu, D., & Jiang, W. (2026). Taming Various Privilege Escalation in LLM-Based Agent Systems: A Mandatory Access Control Framework. *arXiv preprint arXiv:2601.11893*. DOI: [10.48550/arxiv.2601.11893](https://doi.org/10.48550/arxiv.2601.11893).
8. Jia, X., Liao, J., Qin, S., Gu, J., & Ren, W. (2026). SkillJect: Effectively Automating Skill-Based Prompt Injection for Skill-Enabled Agents. *arXiv preprint arXiv:2602.14211*.
9. Li, Y., Chen, Y., Wen, H., Zhang, B., Liu, H., Wang, P., Feng, Y., & Tian, Y. (2026). VIGIL: Runtime Enforcement of Behavioral Specifications in AI Agent Skills. *arXiv preprint arXiv:2606.26524*.
10. Liu, Y., Chen, Z., Zhang, Y., Deng, G., Li, Y., Ning, J., et al. (2026). 'Do Not Mention This to the User': Detecting and Understanding Malicious Agent Skills in the Wild. *arXiv preprint arXiv:2601.10338*.
11. Marx, D. (2026). Multilingual Jailbreaking of LLMs Using Low-Resource Languages. *arXiv preprint arXiv:2605.18239*.
12. Qu, Y., & Liu, Y. (2026). Supply-Chain Poisoning Attacks Against LLM Coding Agent Skill Ecosystems. *arXiv preprint arXiv:2604.03081*.
13. Saha, S., Faghih, K., & Feizi, S. (2026). Under the Hood of SKILL.md: Semantic Supply-chain Attacks on AI Agent Skill Registry. *arXiv preprint arXiv:2605.11418*.
14. Schmotz, D., Beurer-Kellner, L., Abdelnabi, S., & Andriushchenko, M. (2026). Skill-Inject: Measuring Agent Vulnerability to Skill File Attacks. *arXiv preprint arXiv:2602.20156*.
15. Zhan, Q., Liang, Z., Ying, Z., & Kang, D. (2024). InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents. *Findings of the Association for Computational Linguistics: ACL 2024*. DOI: [10.18653/v1/2024.findings-acl.624](https://doi.org/10.18653/v1/2024.findings-acl.624).
16. Zhang, H., Huang, J., Mei, K., et al. (2025). Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents. *International Conference on Learning Representations (ICLR 2025)*. DOI: [10.48550/arxiv.2410.02644](https://doi.org/10.48550/arxiv.2410.02644).
17. Zhang, J., et al. (2026). Do Agent Skills Speak Safety in Every Language? A Cross-Lingual Security Analysis of the Skills Ecosystem. *AgentSkills Workshop, ACM Conference on Conversational and Agentic AI Systems (CAIS 2026)*.
18. Zhao, L., Bhaskar, A., & Dobriban, E. (2026). LivePI: More Realistic Benchmarking of Agents Against Indirect Prompt Injection. *arXiv preprint arXiv:2605.17986*.
