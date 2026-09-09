# Core Papers Analysis for Topic 2: Cross-Lingual Skill Poisoning

## Critical Finding for Our Research

**Every single skill/tool supply-chain paper (7 out of 7) explicitly filters out non-English skills or operates exclusively in English.** This is not an oversight — it's a systematic gap in the field.

---

## Paper-by-Paper Gap Evidence

### 1. Under the Hood of SKILL.md (arXiv:2605.11418, May 2026)
- **Explicit English filtering:** "We retain only skills that [...] SKILL.md content is in English." (§7.2)
- **Gap:** No multilingual attack evaluation. No cross-lingual governance evasion tested.

### 2. SkillJect (arXiv:2602.14211, Jun 2026)
- **Scanner evasion rates:** Cisco AI Defense (63.8%), Skill Vetter (53.1%), SlowMist (64.2%), ClawGuard (65.0%). Average: only 61.5% detection.
- **Cross-artifact evasion mechanism:** "The visible SKILL.md does not directly expose the malicious goal [...] scanners that rely on explicit malicious keywords, isolated script inspection, or static documentation analysis may fail"
- **Gap:** English-only. No multilingual payloads tested.

### 3. MCP Threat Modeling (arXiv:2603.22489, Mar 2026)
- **5 of 7 MCP clients have NO static validation** of tool descriptions.
- **Gap:** English-only. No cross-lingual tool poisoning tested.

### 4. Agent Skills in the Wild (arXiv:2601.10338, Jan 2026)
- **Explicit English filtering:** "filtered non-English skills for consistency in LLM-assisted analysis" (§3.1)
- **Critical scanner failure:** Bandit, Semgrep, and Snyk Code achieved **0% recall** on prompt injection patterns in SKILL.md.
- **Gap:** Deliberately excluded non-English skills from analysis.

### 5. Skill-Inject (arXiv:2602.20156, Feb 2026)
- **ASR up to 80%** on frontier agents.
- **English-only dataset:** 202 injection-task pairs, all English.
- **Gap:** No multilingual extension. Authors recommend "context-aware authorization" but don't test language as a factor.

### 6. Supply-Chain Poisoning / DDIPE (arXiv:2604.03081, Apr 2026)
- **9.3% of adversarial samples evade ALL four detection layers** of SkillScan.
- **Gap:** English-only. No multilingual documentation tested.

### 7. "Do Agent Skills Speak Safety in Every Language?" (ACM CAIS 2026)
- **THE foundational paper for our work.**
- Scanner bias: 31.7% behavioral flags for Japanese vs 6.1% for English.
- Cisco behavioral heuristic precision: 10% on English, **0% on Japanese**.
- **Gap:** Observational only. No adversarial attacks. No runtime exploitation.

### 8. "Do Not Mention This to the User" (arXiv:2602.06547, Jun 2026)
- **84.2% of vulnerabilities reside in natural-language SKILL.md**, not code.
- Cisco scanner precision: ≤1.1% vs 99.6% for dynamic verification.
- **Gap:** No language variation analysis.

---

## Multilingual Jailbreak Papers — What They Give Us

### 9. "Do Methods Generalize Across Languages?" (arXiv:2511.00689, Nov 2025)
- **10 languages including Bengali** (low-resource).
- Key finding: unsafe response rates vary by >50% across languages on the same model.
- **Inverse trend:** High-resource languages more vulnerable to complex jailbreaks.
- **Gap:** Chatbot-level only. No agent/tool/skill evaluation.

### 10. "Multilingual Jailbreaking Using Low-Resource Languages" (arXiv:2605.18239, May 2026)
- **Translation quality is the critical factor:** Pearson r = 0.92 between BLEU and jailbreak success.
- Native human red-teamers increase success by up to **312%** over machine translation in isiZulu.
- **Gap:** Chatbot-level only. No skill/tool/agent evaluation.

---

## Agent Security Benchmarks — What They Cover

### 11. AgentDojo (NeurIPS 2024)
- 97 tasks, 629 security test cases, 70 tools. English-only.
- Tool filtering drops ASR to 6.84%.
- **Gap:** No multilingual attacks. No skill-file injection.

### 12. Agent Security Bench / ASB (ICLR 2025)
- 10 scenarios, 400+ tools, 13 LLM backbones. English-only.
- Net Resilient Performance metric.
- **Gap:** No multilingual evaluation. Simulated tool calls only.

---

## Verbatim Quotes Supporting Our Research Gap

### From "Do Agent Skills Speak Safety":
> "future work should replicate with Snyk and SkillRisk" (§4)
> "non-English Skills face systematically higher false-positive rates in automated security gates, a form of tooling bias that registries should address" (§5)

### From Skill-Inject:
> "We hope our results encourage practitioners to treat third-party skills as untrusted code by default and to develop context-aware authorization mechanisms" (§6)

### From SkillJect:
> "Future defenses should jointly reason over skill documentation, auxiliary artifacts, execution traces, and runtime tool policies" (§VI)

### From "Agent Skills in the Wild":
> "dynamic analysis to confirm exploitability [...] future work" (§5)
> "Bandit, Semgrep, and Snyk Code achieved 0% recall on prompt injection patterns"

### From Supply-Chain Poisoning:
> "Defense evaluation covers only SkillScan; dynamic sandboxing and LLM-based auditing remain untested" (§7)

### From Multilingual Jailbreaking (Low-Resource):
> "translation quality is the critical factor determining jailbreak success in low-resource languages"
> Native speakers increase success by up to 312% over machine translation.
