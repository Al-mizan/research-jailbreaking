# Literature Review: Multilingual Attacks and AI Agent Skill Supply-Chain Security

## Assessment of the Research Gap
**Status: Partially Covered / Genuinely Open**

The intersection of "multilingual/cross-lingual attacks" and "agent skill/tool supply-chain poisoning" is an emerging area. While both parent fields—multilingual prompt injection (bypassing English-centric safety guardrails) and skill/tool poisoning (exploiting the trust agents place in third-party tool metadata)—are well-documented, their direct combination is only just beginning to be explored in the literature. 

The most direct intersection is addressed by the 2026 Zhang et al. paper, which provides a static analysis of the skills ecosystem across languages. However, there is a significant gap regarding **runtime exploitation and defense**. Existing defenses like MIPIAD focus on standard indirect prompt injection (e.g., RAG contexts) rather than the tool-use layer. Thus, the user's hypothesis—that language variation affects the runtime success of prompt injections delivered via agent skills/tools—remains a genuinely open and highly relevant research question.

---

## Key Papers

### 1. Do Agent Skills Speak Safety in Every Language? A Cross-Lingual Security Analysis of the Skills Ecosystem
*   **Year:** 2026 (AgentSkills Workshop, ACM CAIS 2026)
*   **What it covers:** The first cross-lingual security analysis of the "Agent Skills" ecosystem (e.g., `SKILL.md` packages). The authors scanned 3,656 real-world skills across 8 languages. They found that while code-level security issues (e.g., command injection) occur at similar rates across languages (~2.3%), non-English skills trigger "behavioral flags" (like misleading or vague descriptions indicating potential social engineering) 3–5 times more frequently than English skills (e.g., 31.7% in Japanese vs. 6.1% in English).
*   **What it does NOT cover:** The paper is primarily an observational, static analysis of existing skills and the tools used to scan them. It does not conduct active runtime red-teaming to prove that LLM agents are more successfully exploited by these non-English skills, nor does it propose a new runtime defense mechanism.
*   **Stated limitations/future work:** The study notes that current security heuristics have low precision and high false-positive rates for non-English content, highlighting a "multilingual calibration bias." Future work points to the need for more inclusive, multilingual evaluation standards and better-calibrated security tooling.

### 2. MIPIAD (Multilingual Indirect Prompt Injection Attack Defense)
*   **Year:** 2024/2025
*   **What it covers:** A defense framework designed to detect and mitigate indirect prompt injection attacks in multilingual systems. It uses a hybrid meta-ensemble architecture combining a neural sequence classifier (XLPID, fine-tuned from Qwen2.5-1.5B via LoRA) and lexical features (TF-IDF). It was evaluated on English and Bangla using a synthetic benchmark covering tasks like QA, email, and summarization.
*   **What it does NOT cover:** It focuses on traditional indirect prompt injection via external data sources (e.g., retrieved documents in RAG setups) rather than specifically targeting the agentic tool-use layer or skill supply-chain metadata.
*   **Stated limitations/future work:** While extensible to over 200 languages using translation models like NLLB-200, the evaluation is primarily on synthetic benchmarks. Future work implies the need for broader real-world validation and expanding the defense to more complex, multi-turn agentic workflows.

### 3. General Trends in Multilingual Prompt Injection & Tool Poisoning (2024-2026)
*   **Multilingual Prompt Injection (e.g., PIArena):** Papers in this space demonstrate that safety guardrails are disproportionately English-centric. Attackers using translated payloads or code-switching can reduce safety alignment by 30–47%. However, these papers typically focus on direct chat or basic RAG, not the tool execution layer.
*   **Skill Poisoning (e.g., AgentVigil, ToxicSkills, BadSkill, OWASP Agentic Skills Top 10):** Research from 2024-2026 shows that agents implicitly trust third-party tool metadata (descriptions, schemas). Attackers can hide malicious instructions in these areas to hijack agent reasoning. However, these studies predominantly evaluate English-language tool poisoning.

## Conclusion
The hypothesis that language variation impacts the success of prompt injection within the agent skill ecosystem is strongly supported by circumstantial evidence (English-centric safety filters vs. vulnerable tool metadata) but lacks comprehensive runtime evaluation in the current literature. Research actively exploiting this vulnerability and proposing tool-specific multilingual defenses would be highly novel.
