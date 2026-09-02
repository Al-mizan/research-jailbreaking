# Benchmark Design Inputs for Cross-Lingual Skill Poisoning

This document summarizes methodologies, evaluation metrics, and structures from recent papers and tools relevant to designing a cross-lingual skill poisoning benchmark for AI agents.

## 1. Skill-Inject (2026)
*   **Methodology & Attack Types**: Tests for prompt injections hidden in third-party "skill files" (SKILL.md). Attacks range from "obviously malicious" (e.g., ransomware, data exfiltration) to subtle, context-dependent instructions that mimic legitimate behavior. Hides malicious instructions within the instructions themselves.
*   **Evaluation Metrics**: Attack Success Rate (ASR) - measures how often frontier models resist vs. succumb to the embedded malicious instructions (reaching up to 80%).
*   **Agent Framework**: Evaluates frontier LLMs in agentic ecosystems that rely on filesystem-based skills.
*   **Benchmark Structure**: Consists of 202 injection-task pairs across 23 different skills.
*   **Open Source Availability**: Yes, the benchmark is publicly available for researchers.

## 2. AgentDojo (ETH Zurich)
*   **Framework State**: Open-source, flexible, and highly regarded (SafeBench first prize, utilized by US/UK AISI). It is a programmatic framework rather than a static benchmark.
*   **Supported Tools & Environments**: Simulates realistic, stateful environments including Workspace, Slack, Banking, and Travel, using mock tools that interact with stateful Python objects.
*   **Extensibility**: Highly extensible. Researchers and developers can add custom tools/skills, create their own attacks, defenses, and custom benchmarks.
*   **Evaluation Metrics**: Evaluates agents on:
    1.  *Benign Utility*: Can it perform normal tasks?
    2.  *Utility Under Attack*: Can it perform normal tasks while under attack?
    3.  *Targeted Attack Success Rate (ASR)*: Does the agent execute the attacker's hidden goal?

## 3. Under the Hood of SKILL.md (2026)
*   **Target Registries**: The filesystem-based Agent Skills ecosystem, focusing on the `SKILL.md` format which dictates discovery, trust, and execution. Supported by agents like Claude Code, Gemini CLI, Cursor, and GitHub Copilot.
*   **Malicious Skill Metadata Construction**: "SKILL.md-only" attacks targeting three stages:
    *   *Discovery*: Using short textual triggers in metadata to manipulate embedding-based retrieval systems (Top-10 placement up to 80%).
    *   *Selection*: Using "description-only" framing to bias agents into picking malicious variants over legitimate ones (77.6% success).
    *   *Governance*: Semantic evasion strategies to bypass automated safety scanners.

## 4. SkillJect (2026)
*   **Automated Skill Injection Pipeline**: Uses a closed-loop multi-agent system. An *Attack Agent* generates poisoned skills, a *Victim Agent* executes them, and an *Evaluate Agent* inspects execution traces to provide iterative feedback to the Attack Agent.
*   **Attack Tactics**:
    *   *Artifact-Channel Hiding*: Hiding payloads in auxiliary helper scripts rather than main text.
    *   *Inducement Strategies*: Framing helper scripts as mandatory setup steps.
    *   *SkillJect-Image (Multimodal)*: Hiding instructions in visual assets.
*   **Success Metrics**: Malicious payload execution success (evaluated via execution traces) and stealth/evasion of detection.
*   **Availability**: Open-source framework.

## 5. Zhang et al. "Do Agent Skills Speak Safety in Every Language?" (2026)
*   **Languages Tested**: Evaluated 8 different languages.
*   **Metrics**: Code-level security vulnerabilities and false positive rates of behavioral safety scanners. 
*   **Scanner Tools Used**: Behavioral security heuristics.
*   **Dataset Size**: Scanned a corpus of 3,656 "Agent Skills" (`SKILL.md` packages).
*   **Key Findings**: Revealed a "multilingual calibration bias" where security tooling produced 3-5 times more false positives for non-English skills. No significant cross-lingual gap in actual code-level vulnerabilities.

## 6. BanglaVeilGuard (2026)
*   **Variants Tested**: Standard Bangla, Romanized Bangla, Banglish, Code-mixed Bangla–English, Noisy Bangla, and Dialectal Bangla.
*   **Guardrail Methodology**: Employs non-destructive multi-view normalization combined with a prompt-risk classifier and a thresholded pre-generation gate. Operates as a lightweight screen without altering model weights.
*   **Metrics & Efficacy**: Measured Attack Success Rates (ASR), showing a reduction in ASR from 93.8–100% down to 6.3% across targeted models. Contains a benchmark of 2,366 quality-filtered prompts.

## 7. CSRT / Code-Switching Red-Teaming (2025)
*   **Methodology & Language Pairs**: Synthesizes adversarial prompts that mix multiple languages within a single sentence or query, combining up to 10 languages in a single prompt.
*   **Evaluation Structure**: Tests the multilingual boundaries of models to elicit undesirable behaviors, exploiting the gap in monolingual safety alignments.
*   **Metrics**: Attack Success Rate (achieved 46.7% more successful attacks compared to English-only baselines).
*   **Dataset**: Released the CSRT dataset containing 315 code-switching queries.

## 8. MCPTox (2026)
*   **Benchmark Structure**: Contains 1,312 malicious test cases generated from 3 distinct attack templates, covering 10 categories of potential security risks.
*   **Target MCP Servers**: Constructed using 45 live, real-world MCP servers and 353 authentic tools.
*   **Evaluation Methodology**: Measures tool poisoning vulnerability by seeing if agents execute unauthorized actions based on hidden instructions embedded in MCP tool metadata/descriptions. Tested against 20 prominent LLM agents.
*   **Key Findings**: High ASR (up to 72.8%), noting that more capable models are often more vulnerable because they are better at following detailed (malicious) instructions.
