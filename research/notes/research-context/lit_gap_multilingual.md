# State of Multilingual LLM Jailbreaking and Prompt Injection (2025-2026)

## 1. New Multilingual Jailbreak Papers (2025-2026)

### **JailNewsBench: Multi-Lingual and Regional Benchmark for Fake News Generation under Jailbreak Attacks**
* **Year:** 2026
* **Languages Studied:** 22 languages across 34 regions.
* **Key Finding:** Achieves attack success rates up to 86.3% for generating fake news. Demonstrated that multi-lingual LLMs are significantly more vulnerable (less safe) when prompted about non-English and non-U.S.-centric topics.
* **Gap:** The focus is narrowly restricted to fake news generation and does not evaluate general code execution, data exfiltration, or indirect prompt injection.

### **MLingualFC: Evaluating Jailbreak Vulnerabilities in Multilingual Vision-Language Models**
* **Year:** 2026
* **Languages Studied:** Hindi, Punjabi, Spanish, Romanian, and German.
* **Key Finding:** Modern Vision-Language Models (VLMs) like Qwen2.5-VL and Gemma-4 can be jailbroken by encoding harmful instructions into visual flowcharts across multiple languages. Latin-script languages achieved higher attack success rates.
* **Gap:** Lower success rates on non-Latin scripts (like Punjabi) were attributed to the models' poor visual text recognition capabilities rather than superior safety alignment. Multimodal safety for non-Latin scripts remains poorly understood.

### **BanglaVeilGuard: Cross-Script Safety Benchmarking and Lightweight Guardrails for Bangla Large Language Models**
* **Year:** 2026
* **Languages Studied:** Bangla (including Standard, Romanized, Banglish, Code-mixed, Noisy, and Dialectal).
* **Key Finding:** Standard English-centric guardrails completely fail on regional and code-mixed Bangla registers. A lightweight prompt guard (using multi-view normalization) successfully dropped attack success rates on models like Claude Opus and BanglaLLama from ~93% to 6.3% without modifying model weights.
* **Gap:** Leaves a major unresolved trade-off regarding "over-refusal", where the guardrail often incorrectly blocks benign prompts that use dialectal or noisy colloquial language.

### **IndicJR: A Judge-Free Benchmark of Jailbreak Robustness in South Asian Languages**
* **Year:** 2026
* **Languages Studied:** 12 Indic/South Asian languages (including Hindi, Marathi, Telugu, Bengali).
* **Key Finding:** Adversarial prompts written in native scripts yield significantly higher jailbreak success rates compared to their romanized translations, exposing deep flaws in transliteration-based safety filters.
* **Gap:** Focuses solely on direct, single-turn text jailbreaks, ignoring complex agentic environments, tool-calling vulnerabilities, or indirect prompt injection vectors.

### **Code-Switching Red-Teaming (CSRT): LLM Evaluation for Safety and Multilingual Understanding**
* **Year:** 2025
* **Languages Studied:** Multilingual combinations (mixing up to 10 languages within a single prompt).
* **Key Finding:** By interweaving multiple languages in a single query (code-switching), attackers can confuse safety mechanisms. CSRT achieved 46.7% more successful attacks compared to standard monolingual English red-teaming across frontier models.
* **Gap:** Assumes direct user interaction and does not evaluate how code-switched payloads behave when processed indirectly (e.g., during retrieval-augmented generation).

### **Supply-Chain Poisoning Attacks Against LLM Coding Agent Skill Ecosystems**
* **Year:** 2026
* **Languages Studied:** Implicit execution (Code and English documentation).
* **Key Finding:** Introduces **Document-Driven Implicit Payload Execution (DDIPE)**. Attackers can bypass prompt-level safety filters by hiding malicious instructions inside seemingly legitimate code examples within a skill's documentation (e.g., `SKILL.md`). When the agent reads the doc to learn a tool, it blindly executes the payload.
* **Gap:** The research was primarily conducted on English documentation and coding tasks; it is unknown how this compounds when instructions are translated into low-resource human languages.

### **Beyond the Prompt: Jailbreaking Function-Calling LLMs via Simulated Moderation Traces (SMT)**
* **Year:** 2026
* **Languages Studied:** General function-calling domains.
* **Key Finding:** Tool-calling models can be jailbroken by fabricating a multi-turn "moderation audit" workflow. By treating the model's safety refusals as "tool execution failures", the model is pressured to bypass its own safety constraints to resolve the error.
* **Gap:** The attack assumes a highly permissive stateful environment where the agent's context window isn't actively scrubbed or monitored out-of-band by a secondary safety system.

---

## 2. Summary: Well-Studied vs. Open Gaps (As of September 2026)

### **What is WELL-STUDIED:**
1. **Direct Translation Attacks:** The fundamental "language gap" (translating English jailbreaks into Thai, Zulu, or Bangla to bypass filters) is fully recognized and heavily benchmarked.
2. **Text-Based Code-Switching:** Using alternating languages or "Banglish" to dilute harmful tokens is well-documented and effectively evaluated by frameworks like CSRT.
3. **English Tool-Calling Vulnerabilities:** Exploiting the blurry line between instructions and data in agentic workflows (like DDIPE and SMT) is actively being researched, leading to "assume breach" paradigms.
4. **General State of Frontier Models:** Models like GPT-4o, Claude 3.5, and Gemini 2.x are known to be highly robust in English but disproportionately vulnerable to translated, encoded (e.g., Base64), and code-switched attacks.

### **What remains OPEN:**
1. **Multilingual Indirect Prompt Injection:** Almost all multilingual jailbreak research focuses on direct user-to-model interaction. The interaction between low-resource languages and indirect injection (e.g., a Bangla payload hidden on a website that an English-prompted agent reads) is virtually unexplored.
2. **Multilingual Tool-Calling Safety:** Tool schemas and function arguments are almost universally defined in English. There is a massive gap in understanding how models behave when function definitions, arguments, and agentic reasoning are forced into non-English languages to exploit the safety gap.
3. **The "Over-refusal" Trade-off in Low-Resource Languages:** Defending low-resource languages currently results in unacceptably high false-positive refusal rates (e.g., BanglaVeilGuard). Balancing safety without neutering the model's helpfulness in local dialects remains unsolved.
4. **Non-Latin Multimodal Security:** Visual jailbreaks (flowcharts, hidden text in images) perform poorly in non-Latin scripts (like Punjabi or Bangla) mostly because models' OCR fails on those scripts, not because of good safety alignment. This leaves a looming vulnerability as multimodal capabilities improve in these regions.
