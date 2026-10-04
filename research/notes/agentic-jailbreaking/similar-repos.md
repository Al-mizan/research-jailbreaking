# GitHub Repositories for Agentic Jailbreaking and Prompt Injection Research

This document compiles 20 GitHub repositories highly relevant to research in agentic jailbreaking, prompt injection, and LLM security, particularly focusing on benchmarks, red-teaming frameworks, and tool-use vulnerabilities similar to `skill-inject`.

## 1. Benchmarks for Agentic Security & Tool-Use (Most similar to `skill-inject`)

*   **Agent Security Bench (ASB)**
    *   **URL:** https://github.com/Zhang-Henry/ASB
    *   **Description:** A formal framework for benchmarking adversarial attacks and defenses in LLM-based agents across 10 diverse scenarios.
    *   **Relevance:** Evaluates threats like plan-of-thought (PoT) backdoor attacks and memory poisoning in agents, aligning closely with agentic security testing.
    *   **Content:** Code and datasets.
*   **AgentLAB**
    *   **URL:** https://github.com/tanqiu-jiang/AgentLAB
    *   **Description:** A framework evaluating agent susceptibility to adaptive, long-horizon adversarial attacks over multi-turn interactions.
    *   **Relevance:** Goes beyond static benchmarks, crucial for testing real-world agent interactions where attackers adapt over time.
    *   **Content:** Code and datasets.
*   **LLM-Agent-Security**
    *   **URL:** https://github.com/theconsciouslab-ai/llm-agent-security
    *   **Description:** Security testing framework that evaluates agents across Function Calling and Model Context Protocol (MCP) paradigms.
    *   **Relevance:** Highly relevant for tool-use and MCP prompt injection testing, matching the focus on skill execution vulnerabilities.
    *   **Content:** Code.
*   **RAS-Eval**
    *   **URL:** https://github.com/lanzer-tree/RAS-Eval
    *   **Description:** Evaluates security risks in real-world environments, testing agent performance when interacting with toolkits like LangGraph and MCP.
    *   **Relevance:** Provides a practical assessment of popular toolkits used to build autonomous agents.
    *   **Content:** Code and datasets.
*   **SCR-Bench**
    *   **URL:** https://github.com/saint-viperx/SCR_Bench
    *   **Description:** Evaluates security risks within "skill ecosystems," investigating how benign individual skills become harmful when composed by an agent.
    *   **Relevance:** Extremely similar conceptually to `skill-inject`, focusing on compositional harms and skill execution.
    *   **Content:** Code.

## 2. General LLM Jailbreak & Vulnerability Benchmarks

*   **JailbreakBench**
    *   **URL:** https://github.com/JailbreakBench/jailbreakbench
    *   **Description:** An open-source robustness benchmark designed to track progress in generating and defending against jailbreak attacks.
    *   **Relevance:** Provides a standardized framework, leaderboard, and dataset (100 misuse behaviors) for foundational jailbreak research.
    *   **Content:** Code and datasets.
*   **JailJudge**
    *   **URL:** https://github.com/wuzhiyu123/JailJudge
    *   **Description:** A multi-agent framework that provides reasoning, explainability, and fine-grained "jailbroken scores" for model outputs.
    *   **Relevance:** Helpful for automatically evaluating the success rate of complex jailbreak attempts on agents.
    *   **Content:** Code and datasets.
*   **JailBench**
    *   **URL:** https://github.com/vibheksoni/jailbench
    *   **Description:** Lightweight tool for evaluating jailbreak resilience across providers, featuring adversarial model-vs-model testing.
    *   **Relevance:** Useful for continuous security auditing of base models used by agents.
    *   **Content:** Code.
*   **GuidedBench**
    *   **URL:** https://github.com/SproutNan/GuidedBench
    *   **Description:** A guideline-grounded evaluation approach assessing whether model responses violate specific entity/action guidelines.
    *   **Relevance:** Offers a more nuanced evaluation than simple binary harmful/not-harmful metrics.
    *   **Content:** Code.

## 3. Red-Teaming and Attack Frameworks

*   **promptfoo**
    *   **URL:** https://github.com/promptfoo/promptfoo
    *   **Description:** A widely used CLI and library for evaluating LLM output quality, red teaming, and vulnerability scanning.
    *   **Relevance:** An industry-standard tool for testing prompt injection and security in agents and RAG pipelines; integrates into CI/CD.
    *   **Content:** Code and predefined attack templates.
*   **garak**
    *   **URL:** https://github.com/nvidia/garak
    *   **Description:** NVIDIA's LLM vulnerability scanner that probes models for weaknesses, including prompt injection, data leakage, and jailbreaks.
    *   **Relevance:** Extensive automated vulnerability discovery for LLM applications.
    *   **Content:** Code.
*   **HouYi**
    *   **URL:** https://github.com/LLMSecurity/HouYi
    *   **Description:** Automated framework designed to inject prompts into LLM-integrated applications.
    *   **Relevance:** Focuses on black-box application testing, simulating how an attacker might target an agentic system.
    *   **Content:** Code.
*   **PromptInject**
    *   **URL:** https://github.com/agency-risk/PromptInject
    *   **Description:** Modular framework assembling prompts for quantitative analysis of goal hijacking and prompt leaking.
    *   **Relevance:** Useful for building systematic test cases for adversarial prompt attacks.
    *   **Content:** Code.
*   **aiapwn**
    *   **URL:** https://github.com/karimhabush/aiapwn
    *   **Description:** Automates the detection of prompt injection vulnerabilities specifically in AI agents using reconnaissance and testing engines.
    *   **Relevance:** Agent-specific security scanning tailored for autonomous behaviors.
    *   **Content:** Code.
*   **spikee**
    *   **URL:** https://github.com/ReversecLabs/spikee
    *   **Description:** Modular toolkit for assessing the resilience of LLMs, guardrails, and integrated applications against injection.
    *   **Relevance:** Good for testing defensive mechanisms (guardrails) around agents.
    *   **Content:** Code.
*   **Augustus**
    *   **URL:** https://github.com/praetorian-inc/augustus
    *   **Description:** A security testing framework (by Praetorian) that includes 190+ probes to detect prompt injection and adversarial attacks.
    *   **Relevance:** A comprehensive red-teaming tool from a cybersecurity firm.
    *   **Content:** Code.

## 4. Indirect Prompt Injection and RAG Security

*   **AgentForensics (agentzt)**
    *   **URL:** https://github.com/openafw/agentzt
    *   **Description:** Tool to monitor LLM agent sessions to detect prompt injections in real-time.
    *   **Relevance:** Relevant for researching defensive strategies and monitoring live agent activity during indirect prompt injection attempts.
    *   **Content:** Code.
*   **indirect-prompt-injection**
    *   **URL:** https://github.com/federicotorrielli/indirect-prompt-injection
    *   **Description:** Explores how hidden payloads can manipulate AI-assisted processes, such as academic peer reviews.
    *   **Relevance:** Focuses explicitly on the vulnerability where untrusted retrieved data (RAG) hijacks the model's instructions.
    *   **Content:** Code and datasets/demonstrations.
*   **example-indirect-promptinjection**
    *   **URL:** https://github.com/layerupai/example-indirect-promptinjection
    *   **Description:** Practical demonstrations of how hidden prompts embedded in HTML can deceive LLM workflows.
    *   **Relevance:** Excellent tangible examples of web-based indirect prompt injection affecting agents scraping the web.
    *   **Content:** Code examples.

## 5. Datasets and Knowledge Bases

*   **Awesome-Jailbreak-on-LLMs**
    *   **URL:** https://github.com/yueliu1999/Awesome-Jailbreak-on-LLMs
    *   **Description:** A curated, high-quality collection of papers, datasets, and methodologies related to LLM jailbreak attacks.
    *   **Relevance:** Essential starting point for literature reviews, finding new attack vectors, and discovering specialized datasets.
    *   **Content:** Curated Lists (Markdown).
