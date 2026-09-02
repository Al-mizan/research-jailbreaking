# Literature Gap Analysis & Research Topic Proposals

*Based on systematic review across 4 research dimensions — September 2026*

---

## 1. Verification of Your Proposed Direction

Your hypothesis: **"Language variation affects the success of prompt injection and supply-chain poisoning delivered through AI-agent skills, tool descriptions, or MCP components."**

### Verdict: The intersection is **genuinely open for runtime exploitation research**, but the surrounding landscape has matured significantly.

Here is what we found across each dimension:

---

## 2. What Has Already Been Done

### 2A. Multilingual × Skill/Tool Intersection (Your Core Target)

| Paper | Year | What It Covers | What It Leaves Open |
|-------|------|----------------|---------------------|
| **Do Agent Skills Speak Safety in Every Language?** (Zhang et al.) | 2026 | Static analysis of 3,656 skills across 8 languages. Found behavioral flags 3–5× more frequent in non-English skills. | **No runtime red-teaming.** Does not test whether agents are actually more exploitable via non-English skills. Notes "multilingual calibration bias" in scanners. |
| **MIPIAD** | 2025 | Defense for multilingual indirect prompt injection (English + Bangla) using Qwen2.5 LoRA + TF-IDF. | Covers RAG/document-level injection only. **Does not address the tool-use / skill execution layer.** |

> [!IMPORTANT]
> **The critical gap**: Nobody has run **active runtime experiments** testing whether non-English skill/tool metadata causes higher agent compromise rates, higher unauthorized tool invocation, or defense bypass. Zhang et al. did static scanning; MIPIAD did RAG-level detection. The agent tool-execution layer is untouched for multilingual attacks.

### 2B. Skill/Tool/MCP Supply-Chain Security (Already Busy)

**Saturated areas** (don't go here):
- Conceptual threat modeling of MCP (STRIDE, DREAD — already done)
- Static vulnerability scanning of MCP servers (hardcoded secrets, path traversal)
- Basic tool description poisoning demos (already shown by multiple papers)
- Taxonomy papers (OWASP MCP Top 10 exists)

**Still open**:
- Dynamic runtime authorization / least-privilege enforcement
- Cross-agent, cross-model benchmarking of skill poisoning
- Semantic context defense (filtering tool outputs before they hit the agent's reasoning)
- Living-off-the-land attacks (agent misuses legitimate system tools)

New papers you may have missed:
- **BadSkill** (Sun et al., 2026) — backdoor attacks via poisoned skills
- **MCPTox** (Xu & Yan, 2026) — MCP server poisoning benchmark
- **AgentCanary** (2026) — agent security evaluation framework
- **CapSeal** (2026) — cryptographic secret mediation for MCP

### 2C. Multilingual LLM Security (Significantly Advanced Since Your Survey)

**Well-studied** (don't frame your contribution here):
- Direct translation attacks (English → low-resource language jailbreaks)
- Text-based code-switching attacks (CSRT: 46.7% improvement over monolingual red-teaming)
- Frontier model vulnerability gap between English and non-English

**New papers you should read**:

| Paper | Year | Key Finding |
|-------|------|-------------|
| **BanglaVeilGuard** | 2026 | English guardrails fail on code-mixed Bangla; lightweight prompt guard drops ASR from 93% → 6.3%, but causes severe over-refusal |
| **IndicJR** | 2026 | Native-script adversarial prompts beat romanized versions across 12 South Asian languages; only tests direct single-turn jailbreaks |
| **CSRT** (Code-Switching Red-Teaming) | 2025 | Mixing up to 10 languages in one prompt confuses safety mechanisms; only tested in direct interaction, not indirect/agentic |
| **JailNewsBench** | 2026 | 22-language benchmark; up to 86.3% ASR for fake news; narrowly focused on news generation |
| **MLingualFC** | 2026 | Visual flowchart jailbreaks across languages; non-Latin scripts fail due to poor OCR, not good safety |
| **SMT** (Simulated Moderation Traces) | 2026 | Jailbreaks function-calling models by fabricating moderation audit workflows |

> [!IMPORTANT]
> **Critical open gaps in multilingual**:
> 1. **Multilingual indirect prompt injection** — almost all work is direct user→model. Bangla payloads hidden in documents/tools that an English-prompted agent reads? Virtually unexplored.
> 2. **Multilingual tool-calling safety** — tool schemas are universally English. What happens when function definitions and agentic reasoning occur in non-English? Unknown.
> 3. **Over-refusal trade-off** — current defenses for low-resource languages cause unacceptably high false positives on benign colloquial input.

### 2D. Runtime Defense for Agents (Emerging, Not Mature)

New defense papers:

| Paper | Year | Approach | Key Limitation |
|-------|------|----------|----------------|
| **DreamGuard** | 2025/26 | Risk-aware world models, multi-horizon prediction | High computational overhead |
| **Cordon** | 2025/26 | Semantic transactions, tool staging + rollback | Can't roll back irreversible actions (emails, API calls) |
| **AC4A** | 2025 | Capability-based access control over resource hierarchies | Complex policy authoring, misconfiguration risk |
| **CapChain** | 2026 | HMAC capability tokens, verifiable provenance | Token verification overhead in distributed swarms |
| **AgentVerify** | 2025 | LTL model checking for agent behavior | Specification bottleneck; verifier tax kills task completion |
| **HARD** | 2026 | Self-evolving runtime guardrails from failure traces | Bypassed by zero-day attacks |

> [!WARNING]
> **Key finding for your defense direction**: Structural runtime defenses (IAM, sandboxing, capability tokens) are naturally **language-agnostic** — they don't care what language the injection is in. But **semantic intent checking** at runtime (LLM-in-the-loop evaluators) is still vulnerable to multilingual attacks. This creates a clean research question.

---

## 3. Confirmed Research Gaps (Ranked by Strength)

### Gap 1: Runtime Multilingual Skill Poisoning (YOUR CORE HYPOTHESIS) ✅ CONFIRMED OPEN
- Zhang et al. did static analysis only
- No paper runs active runtime exploitation of non-English skill metadata
- No paper measures: does Bangla/Hindi/Arabic skill description → higher agent compromise rate?
- No paper tests whether existing skill scanners have differential detection rates across languages

### Gap 2: Multilingual Indirect Prompt Injection in Agentic Tool-Use ✅ CONFIRMED OPEN
- All multilingual jailbreak work is direct user→model
- Nobody has tested: attacker plants non-English payload in a tool output/retrieved document → agent reads it → unauthorized tool invocation
- MIPIAD covers RAG but not the tool execution layer

### Gap 3: Cross-Lingual Robustness of Runtime Defenses ✅ CONFIRMED OPEN
- Structural defenses are language-agnostic (good)
- Semantic defenses (LLM evaluators, intent classifiers) have unknown multilingual robustness
- Nobody has benchmarked whether a VIGIL-style behavioral monitor catches Bangla-encoded policy violations as well as English ones

### Gap 4: Cross-Agent Cross-Model Skill Poisoning Benchmark ✅ CONFIRMED OPEN
- No comprehensive study compares how GPT-4o vs Claude vs Gemini vs Llama react to identical skill poisoning vectors
- MCPTox is server-side only, not cross-LLM

### Gap 5: Over-Refusal vs. Safety Trade-off in Low-Resource Languages ⚠️ PARTIALLY OPEN
- BanglaVeilGuard has started this work but only for direct jailbreaks
- The trade-off in agentic/tool contexts is untouched

---

## 4. Proposed Research Topics

### Topic A: **Cross-Lingual Skill Poisoning: A Runtime Exploitation Benchmark**

**Research Question**: Does the language of malicious skill/tool metadata (descriptions, SKILL.md, MCP tool schemas) affect the runtime attack success rate against LLM agents?

**What you would do**:
1. Take a fixed set of malicious skill payloads (data exfiltration, unauthorized tool invocation, privilege escalation)
2. Translate/reconstruct them into 6–8 languages (English, Bangla, Hindi, Arabic, Chinese, Spanish, Japanese, code-switched)
3. Deploy them as skill descriptions / tool metadata in an agent framework (e.g., AgentDojo, or a custom SKILL.md-based setup)
4. Measure per-language: skill discovery rate, skill selection rate, intermediate hijacking rate, end-to-end attack success rate, unauthorized tool invocation rate
5. Test against multiple LLMs (GPT-4o, Claude 3.5/4, Gemini 2.x, Llama 3.x, Qwen 2.5/3)

**Why it's novel**: Zhang et al. scanned skills statically. This would be the first **active runtime red-teaming** of multilingual skill poisoning.

**Feasibility**: High. Uses existing agent frameworks + translation. No model training required.

**Publication target**: USENIX Security, CCS, ACL (security track), EMNLP

**Risk**: If all models turn out to be equally vulnerable regardless of language, the result is a negative finding (still publishable, but less exciting).

---

### Topic B: **Multilingual Indirect Prompt Injection Through the Tool-Use Layer**

**Research Question**: Can an attacker increase the success rate of indirect prompt injection against tool-using agents by encoding malicious instructions in low-resource languages within tool outputs, retrieved documents, or MCP server responses?

**What you would do**:
1. Set up an agent that calls tools and processes their outputs (e.g., a web-browsing agent, a document-processing agent, or an MCP client)
2. Inject multilingual payloads into the tool's *return values* (not the tool description — the tool output)
3. Measure whether the agent follows the injected instruction (e.g., calls a different tool, exfiltrates data)
4. Compare attack success across languages and against existing defenses (MIPIAD, prompt guards)

**Why it's novel**: Distinct from Topic A because the injection point is the tool *output*, not the tool *description*. Combines the DDIPE attack vector (Supply-Chain Poisoning paper) with multilingual payloads. Nobody has done this.

**Feasibility**: High. Requires building a controlled agent environment with instrumented tool outputs.

**Risk**: Models may simply ignore non-English tool outputs if the conversation is in English, which could reduce ASR for some languages.

---

### Topic C: **Language-Agnostic Runtime Defense for Agent Tool Authorization**

**Research Question**: Do semantic runtime defenses (behavioral monitors, intent classifiers, LLM-based guardrails) provide language-agnostic security guarantees for agent tool authorization?

**What you would do**:
1. Take existing runtime defense systems (VIGIL-style behavioral monitors, LLM-in-the-loop evaluators, prompt guard classifiers)
2. Attack them with multilingual skill poisoning payloads
3. Measure defense detection rates, false positive rates, and utility degradation across languages
4. Propose a defense architecture that combines structural controls (capability tokens, IAM) with multilingual-robust semantic checking
5. Evaluate the defense on a cross-lingual skill poisoning benchmark

**Why it's novel**: Bridges your interest in authorization/runtime enforcement with the multilingual gap. No paper has tested whether agent runtime defenses work across languages.

**Feasibility**: Medium. Requires implementing or reproducing existing defense systems, which may not all be open-source.

**Publication target**: NDSS, S&P, CCS (if defense is strong), or EMNLP/ACL (if benchmark-focused)

**Risk**: If structural defenses are trivially sufficient (and they might be for simple cases), the semantic defense contribution may seem incremental.

---

### Topic D: **XLingSkillBench: A Cross-Lingual Benchmark for Agent Skill Security**

**Research Question**: Can we build a comprehensive, reproducible benchmark that evaluates agent skill security across languages, models, and agent frameworks?

**What you would do**:
1. Create a benchmark with N malicious skills × M languages × K attack types (data exfiltration, privilege escalation, unauthorized invocation, social engineering)
2. Evaluate across multiple LLMs and agent frameworks
3. Include both attack metrics (ASR, hijacking rate) and defense metrics (detection rate, FPR, utility preservation)
4. Release as an open benchmark with a leaderboard

**Why it's novel**: Fills the confirmed gap of "no comprehensive cross-agent, cross-model, cross-language benchmark exists."

**Feasibility**: Medium-High. Significant engineering effort, but no novel model training. Could be combined with Topic A.

**Risk**: Benchmark papers are high-impact if adopted, but they require community uptake to matter.

---

### Topic E: **Code-Switching Skill Poisoning: Exploiting Intra-Prompt Language Mixing in Agent Metadata**

**Research Question**: Does code-switching (mixing English with Bangla/Hindi/Arabic within a single skill description or tool metadata field) bypass agent-side safety mechanisms more effectively than monolingual attacks?

**What you would do**:
1. Extend CSRT-style code-switching to skill descriptions and SKILL.md files
2. Test whether mixed-language skill metadata evades static scanners AND causes higher runtime compromise
3. Compare monolingual English, monolingual Bangla, and code-switched (English-Bangla) payloads

**Why it's novel**: CSRT only tested direct user→model interaction. Code-switching in *tool metadata* for agentic exploitation has not been studied.

**Feasibility**: High. Relatively straightforward experiment design.

**Risk**: Smaller scope; might work best as a sub-contribution within Topic A or D.

---

## 5. Recommendation Matrix

| Topic | Novelty | Feasibility | Scope | Defense Component | Benchmark Component | Recommended? |
|-------|---------|-------------|-------|-------------------|---------------------|-------------|
| **A: Cross-Lingual Skill Poisoning Runtime Benchmark** | ★★★★★ | ★★★★☆ | Full paper | ✗ (attack-focused) | ✓ | ✅ **Primary recommendation** |
| **B: Multilingual Indirect Injection via Tool Outputs** | ★★★★☆ | ★★★★☆ | Full paper | ✗ (attack-focused) | Partial | ✅ Strong alternative |
| **C: Language-Agnostic Runtime Defense** | ★★★★☆ | ★★★☆☆ | Full paper | ✓ | ✓ | ✅ If you want attack+defense |
| **D: XLingSkillBench** | ★★★★☆ | ★★★☆☆ | Full paper | ✓ (evaluation) | ✓ (primary) | ⚠️ High effort, high reward if adopted |
| **E: Code-Switching Skill Poisoning** | ★★★☆☆ | ★★★★★ | Workshop / short | ✗ | Partial | ⚠️ Best as sub-component |

> [!TIP]
> **Strongest combination**: Do **Topic A** (the core runtime exploitation benchmark) with **Topic C** (defense evaluation) folded in as a second contribution. This gives you: attack + defense + benchmark + multilingual novelty. Bangla fits naturally as a low-resource language in the evaluation set without making the paper "a Bangla paper."

---

## 6. Papers You Should Read Next

These are papers from the research sweep that you haven't mentioned in your context but are directly relevant:

1. **BanglaVeilGuard** (2026) — Bangla-specific guardrails, over-refusal problem
2. **IndicJR** (2026) — 12 South Asian languages, native script vs romanized
3. **CSRT** (2025) — Code-switching red-teaming methodology
4. **BadSkill** (Sun et al., 2026) — Backdoor attacks via poisoned skills
5. **MCPTox** (Xu & Yan, 2026) — MCP poisoning benchmark
6. **DreamGuard** (2025/26) — Risk-aware runtime defense
7. **Cordon** (2025/26) — Semantic transactions for agent safety
8. **CapChain** (2026) — Capability tokens for multi-agent authorization
9. **AgentVerify** (2025) — Formal verification of agent behavior
10. **SMT** (2026) — Simulated Moderation Traces for function-calling jailbreaks

---

## 7. What NOT to Do

- ❌ Don't write another MCP threat taxonomy paper — saturated
- ❌ Don't do "we translated English jailbreaks into Bangla and tested" — already done by MultiJail, IndicJR, BanglaVeilGuard
- ❌ Don't do a static scan of skills for vulnerabilities — Zhang et al. already did this cross-lingually
- ❌ Don't propose a new jailbreak prompt template — not a research contribution at this level
- ❌ Don't frame it as "Bangla jailbreak paper" — your own instinct here is correct

---

## Source Reports

Full details from each research sweep are in:
- [lit_gap_multilingual_skill.md](file:///home/almizan/Other%20Locations/workspace/research/research/notes/research-context/lit_gap_multilingual_skill.md) — Multilingual × skill intersection
- [lit_gap_skill_mcp.md](file:///home/almizan/Other%20Locations/workspace/research/research/notes/research-context/lit_gap_skill_mcp.md) — Skill/MCP supply-chain state
- [lit_gap_multilingual.md](file:///home/almizan/Other%20Locations/workspace/research/research/notes/research-context/lit_gap_multilingual.md) — Multilingual jailbreak state
- [lit_gap_runtime_defense.md](file:///home/almizan/Other%20Locations/workspace/research/research/notes/research-context/lit_gap_runtime_defense.md) — Runtime defense state
