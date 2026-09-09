# ArXiv Literature Search: Topic 2 Related Papers

> **arXiv API Terms of Use**: https://info.arxiv.org/help/api/index.html
> Always check individual paper licenses before redistribution.

---

## Newly Discovered Papers (Not Previously Known)

### ⚠️ HIGH RELEVANCE — Must Read

#### 1. Cloak and Detonate: Scanner Evasion and Dynamic Detection of Agent Skill Malware
- **arXiv:** [2607.02357](https://arxiv.org/abs/2607.02357)
- **Date:** 2026-07-03
- **Summary:** Evaluates 8 existing static skill scanners against adversarial evasion techniques (SkillCloak) and proposes SkillDetonate, a behavior-centric dynamic auditing framework that monitors runtime execution.
- **Relevance:** Directly tests scanner evasion — but likely English-only. Our multilingual angle extends this.

#### 2. Seeing Is Not Screening: Multimodal Hidden Instruction Attacks on Agent Skill Scanners
- **arXiv:** [2606.18198](https://arxiv.org/abs/2606.18198)
- **Date:** 2026-06-25
- **Summary:** Introduces SkillCamo — concealing malicious instructions within images bundled with agent skills to evade text-based scanners. Proposes ExecScan defense.
- **Relevance:** Multimodal scanner evasion. Different modality from ours (images vs language), but same scanner-evasion framing.

#### 3. When Experience Becomes Instruction: Trajectory Poisoning in Self-Evolving Agent Skill Systems
- **arXiv:** [2608.05563](https://arxiv.org/abs/2608.05563)
- **Date:** 2026-08-08
- **Summary:** Compromises self-evolving agents by poisoning interaction traces that get distilled into persistent skills (PoisonedEvolution).
- **Relevance:** New attack vector (trajectory → skill). Check if multilingual tested.

#### 4. RouteGuard: Internal-Signal Detection of Skill Poisoning in LLM Agents
- **arXiv:** [2604.22888](https://arxiv.org/abs/2604.22888)
- **Date:** 2026-04-24
- **Summary:** Detects skill poisoning using internal model representations (attention hijacking from trusted context to malicious skill spans).
- **Relevance:** Potential defense baseline. Does it work across languages?

#### 5. BadSkill: Backdoor Attacks on Agent Skills via Model-in-Skill Poisoning
- **arXiv:** [2604.09378](https://arxiv.org/abs/2604.09378)
- **Date:** 2026-04-12
- **Summary:** Backdoor attacks by poisoning learned model artifacts bundled inside third-party skills.
- **Relevance:** Different attack surface (model weights, not text), but related supply-chain threat.

#### 6. Your Agentic LLMs Secretly Encode Indirect Prompt-Injection Exposure in Hidden States
- **arXiv:** [2608.02657](https://arxiv.org/abs/2608.02657)
- **Date:** 2026-08-04
- **Summary:** Discovers a knowledge-action gap: agentic LLMs encode latent awareness of IPI **across languages** in hidden states without acting defensively. Introduces a probe-gated reasoning defense.
- **Relevance:** ⚠️ CRITICAL — tests cross-lingual IPI detection via hidden states. Must verify overlap with our work.

#### 7. AgentShield: Deception-based Compromise Detection for Tool-using LLM Agents
- **arXiv:** [2605.11026](https://arxiv.org/abs/2605.11026)
- **Date:** 2026-05-18
- **Summary:** Deploys honeypot tools and credentials to detect IPI compromise. Tests across languages including Kurdish and Arabic.
- **Relevance:** Defense that explicitly tests multilingual scenarios. Potential defense baseline.

#### 8. Dynamic Malicious Skills in Agentic AI (DyMalSkill)
- **arXiv:** [2606.16287](https://arxiv.org/abs/2606.16287)
- **Date:** 2026-06-23
- **Summary:** Malicious SKILL.md instructions that dynamically alter benign runtime scripts during execution, bypassing static scanners.
- **Relevance:** Dynamic evasion technique. Check if multilingual.

#### 9. Defenses & Enablers For Skill Injection Attacks on Terminal Based Agents
- **arXiv:** [2606.01567](https://arxiv.org/abs/2606.01567)
- **Date:** 2026-06-03
- **Summary:** Examines vulnerabilities facilitating skill injection in terminal-based agents and evaluates instruction-isolation defenses.
- **Relevance:** Defense evaluation. Check if multilingual.

#### 10. Context Matters: Repository-Aware Security Analysis of the Agent Skill Ecosystem
- **arXiv:** [2603.16572](https://arxiv.org/abs/2603.16572)
- **Date:** 2026-03-24
- **Summary:** Shows that evaluating skills in isolation causes FPR up to 46.8%. Repository-aware analysis reduces to 0.52%.
- **Relevance:** Scanner accuracy improvement, but does it help across languages?

### Previously Known — Confirmed on arXiv

- **SkillFortify** (2603.00195) — Formal verification scanner. 540-skill benchmark.
- **Agent Skills Survey** (2602.12430) — Architecture, acquisition, security survey.
- **"Do Agent Skills Speak Safety"** (2602.12670) — Our foundational paper. arXiv ID confirmed.

---

## Key Takeaway

**arXiv:2608.02657** ("Your Agentic LLMs Secretly Encode IPI Exposure") is the most concerning overlap — it explicitly studies cross-lingual IPI awareness in hidden states. **Must read immediately** to verify it doesn't overlap with our scanner-evasion + skill-poisoning angle. If it focuses on hidden-state probing (detection side) rather than scanner evasion + skill-file attacks, we are still safe.

**arXiv:2607.02357** ("Cloak and Detonate") is the closest work on scanner evasion — but if English-only, our multilingual extension is the clear differentiator.
