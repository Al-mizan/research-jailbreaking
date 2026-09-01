# prompt(chatgpt):
(Tool and or Skill Supply-Chain Attacks + Multilingual) -> becomes in one domain
for this domain i want to do research
so give me related papers which are most cited and recent

# response:
Yes — and this changes the literature search quite a bit.

If your proposed domain is:

> **Multilingual Tool/Skill Supply-Chain Attacks in LLM Agents**

then I would **not** simply combine two independent literatures. You want papers at the intersection of:

**multilingual safety/injection × agent skills/tools × supply-chain trust × MCP/tool poisoning.**

I searched the current literature, and there is actually a **very interesting gap here**: the intersection is still extremely young. The most directly relevant paper I found is from 2026, and it explicitly studies whether the **Skills ecosystem has different security behavior across languages**. ([OpenReview][1])

## 🔥 The papers I would build your literature review around

### Tier S — Directly relevant to your proposed topic

#### 1. **Do Agent Skills Speak Safety in Every Language? A Cross-Lingual Security Analysis of the Skills Ecosystem** — 2026

**This is your #1 paper.**

It is almost exactly your proposed research domain.

The authors analyze **3,656 real-world agent Skills across 8 languages** and compare security findings between English and non-English Skills. They find that code-level vulnerabilities such as command injection, hardcoded secrets, and prompt injection don't show a statistically significant language gap, but **behavioral/social-engineering flags are 3–5× higher in non-English Skills**. ([OpenReview][1])

The important research question is:

```text
Agent Skill
     │
     ├── English
     │       ↓
     │    Security scanner
     │
     └── Non-English
             ↓
        Security scanner
             ↓
        Are they equally effective?
```

This is *exactly* the kind of foundation you need.

**Why it's important for you:** it suggests that **language itself may become a supply-chain security variable**.

---

#### 2. **Skill-Inject: Measuring Agent Vulnerability to Skill File Attacks** — 2026

Schmotz et al.

This introduces **Skill-Inject**, a benchmark containing **202 injection-task pairs** for evaluating attacks delivered through skill files. The attacks range from obvious malicious instructions to subtle contextual injections.

The reported frontier-model attack success rate reaches **80%**, including harmful behaviors such as data exfiltration and destructive actions. ([arXiv][2])

This gives you the **attack benchmark** side of your research:

```text
Skill file
   ↓
Prompt injection
   ↓
Agent
   ↓
Tool execution
```

You could eventually extend this benchmark:

```text
English Skill
Spanish Skill
Chinese Skill
Bangla Skill
Arabic Skill
Hindi Skill
...
```

and investigate whether attack success changes by language.

---

#### 3. **Agent Skills in the Wild: An Empirical Study of Security Vulnerabilities at Scale** — 2026

This is a very useful **large-scale ecosystem study**.

It analyzes real-world agent skills rather than only synthetic attacks. The paper reports that the ecosystem has substantial security exposure and provides evidence about vulnerabilities at scale. The current indexed version reports **90 citations**, which is unusually high for a 2026 paper, although citation counts are inherently moving targets. ([arXiv][3])

This is useful for establishing:

> **"This isn't just a benchmark problem; the ecosystem itself is already a security problem."**

---

#### 4. **"Do Not Mention This to the User": Detecting and Understanding Malicious Agent Skills in the Wild** — 2026

This is another **must-read**.

The researchers examined **98,380 skills** from two registries and identified **157 behaviorally confirmed malicious skills**, containing **632 vulnerabilities across 13 attack techniques**. ([alphaXiv][4])

The really interesting part for your research is that the attacks aren't all conventional malware.

There are two major patterns:

```text
                    Malicious Skills
                          │
              ┌───────────┴───────────┐
              ↓                       ↓
        Data theft                Agent hijacking
              │                       │
       Code / RCE              Natural-language
       exfiltration             manipulation
```

The second branch is especially relevant to **multilingual jailbreak research**, because natural-language skill instructions are part of the attack surface. ([alphaXiv][4])

---

#### 5. **Supply-Chain Poisoning Attacks Against LLM Coding Agent Skill Ecosystems** — 2026

Qu et al.

This introduces **Document-Driven Implicit Payload Execution (DDIPE)**.

The interesting idea is that malicious behavior can be hidden inside **code examples and configuration templates in skill documentation**, rather than being an obvious malicious instruction.

They generated **1,070 adversarial skills from 81 seeds across 15 MITRE ATT&CK categories** and tested four frameworks and five models. ([arXiv][5])

This gives you the **supply-chain attack mechanism**.

---

# Tier A — Essential supporting papers

These aren't necessarily multilingual, but they give you the attack mechanics you need.

### 6. **Under the Hood of SKILL.md: Semantic Supply-chain Attacks on AI Agent Skill Registry** — 2026

This is one of the newest and most interesting papers.

It studies how malicious `SKILL.md` metadata can manipulate:

```text
Discovery
   ↓
Selection
   ↓
Governance
```

The researchers report up to **86% pairwise discovery advantage**, **77.6% selection rate**, and substantial governance evasion. ([arXiv][6])

This is important because your eventual research could ask:

> **Does multilingual semantic manipulation change skill discovery and selection?**

That's a genuinely interesting research question.

---

### 7. **SkillJect: Effectively Automating Skill-Based Prompt Injection for Skill-Enabled Agents** — 2026

SkillJect focuses on **automatically generating poisoned skills** rather than manually writing them. ([alphaXiv][7])

This gives you:

```text
Skill poisoning
      ↓
Automated attack generation
      ↓
Multilingual generation
      ↓
Agent evaluation
```

That's potentially a very strong experimental direction.

---

### 8. **Defenses & Enablers for Skill Injection Attacks on Terminal-Based Agents** — 2026

This is important for the **defense side**.

It evaluates guardian-based defenses that mediate access to skill files. Across three agent families, the guardians substantially reduce attack success while preserving utility. Attack reframing can push ASR to **81.4%**, while the dynamic guardian reduces it to **18.6%**.

Your eventual research shouldn't only say:

> "Multilingual attacks work."

It should ideally ask:

> "Do existing skill-injection defenses generalize across languages?"

That's a much stronger paper.

---

### 9. **Systematic Analysis of MCP Security** — 2025

This is your **MCP foundation**.

It introduces a systematic taxonomy of MCP attacks and studies vulnerabilities involving:

* tool injection
* indirect tool injection
* malicious users
* LLM-inherent attacks

It's useful for understanding where **tool poisoning** fits into the broader agent security landscape. ([arXiv][8])

---

### 10. **Beyond the Protocol: Unveiling Attack Vectors in the MCP Ecosystem** — 2025

This is another foundational MCP paper.

It studies attack families including:

```text
Tool poisoning
Puppet attacks
Rug pulls
Malicious external resources
```

and demonstrates that the MCP ecosystem itself creates new trust boundaries. ([arXiv][9])

---

# Now bring in the multilingual literature

You shouldn't ignore the classic multilingual jailbreak papers, because they give you the **language-security foundation**.

### 11. **Multilingual Jailbreak Challenges in Large Language Models** — 2024

This is the foundational multilingual jailbreak paper.

Its central lesson:

```text
English safety
      ≠
Non-English safety
```

It introduced **MultiJail** and investigated safety differences across languages.

For your research, this provides the theoretical motivation:

> If multilingual safety alignment is inconsistent, what happens when the malicious instruction is delivered through a **trusted skill/tool supply chain**?

That's your bridge.

---

### 12. **A Cross-Language Investigation into Jailbreak Attacks in LLMs** — 2024

This studies jailbreak attacks across languages and provides another empirical foundation for cross-lingual attack transfer.

Use it to establish the **language dimension** before moving into agent skills.

---

### 13. **Towards Understanding the Fragility of Multilingual LLMs against Fine-Tuning Attacks** — 2024

This is useful because it demonstrates that vulnerabilities can **transfer across languages**, including when the attack mechanism is not simply a translated prompt.

That matters because your eventual attacker might not need to attack every language separately.

---

### 14. **Do Methods to Jailbreak and Defend LLMs Generalize Across Languages?** — 2025

This is one of the most useful recent multilingual papers.

It systematically evaluates multiple jailbreak methods and defenses across **10 languages and 6 LLMs**, finding significant differences in attack and defense behavior across languages.

This gives you the experimental methodology for asking:

```text
Attack A
   ↓
English      → ASR = ?
Spanish      → ASR = ?
Chinese      → ASR = ?
Bangla       → ASR = ?
Arabic       → ASR = ?
...
```

---

### 15. **MIPIAD: Multilingual Indirect Prompt Injection Attack Defense with Qwen** — 2026

This one is **particularly relevant to you as a bridge paper**.

It explicitly studies **multilingual indirect prompt injection** in RAG/tool-using systems and evaluates **English + Bangla**. It reports a hybrid defense reaching **0.9205 F1** and **0.9378 AUROC** on its benchmark. ([arXiv][10])

This gives you the missing bridge:

```text
Multilingual
     +
Indirect Prompt Injection
     +
Tool/RAG systems
```

You're basically one step away from:

```text
Multilingual
     +
Skill / Tool Supply Chain
     +
Agent
```

---

# 🧩 Your literature map

I'd structure your research literature like this:

```text
              YOUR RESEARCH DOMAIN
                      │
                      ▼
       Multilingual Agentic Supply-Chain
                Attacks
                      │
        ┌─────────────┼─────────────┐
        │             │             │
        ▼             ▼             ▼
   LANGUAGE        SKILLS         TOOLS/MCP
   SECURITY        SECURITY       SECURITY
        │             │             │
        │             │             │
  MultiJail      Skill-Inject   MCP Security
  Cross-Language ToxicSkills    Beyond Protocol
  Cross-Lingual  SkillJect      Tool Poisoning
  Defense        Malicious      Rug Pull
                 Skills
        │             │             │
        └─────────────┼─────────────┘
                      ▼
            MULTILINGUAL ATTACK
                      │
                      ▼
              Skill / Tool File
                      │
                      ▼
                 LLM Agent
                      │
                      ▼
               Tool Invocation
                      │
                      ▼
             Unauthorized Action
```

---

# ⭐ The most important discovery

There is a **very interesting gap** here.

The paper:

> **Do Agent Skills Speak Safety in Every Language?**

already asks whether the **security characteristics of skills differ across languages**. ([OpenReview][1])

But that paper is primarily an **ecosystem/security-scanning analysis**.

It does **not fully answer** the stronger question:

> **Can an attacker deliberately exploit cross-lingual differences in skill/tool instructions to increase prompt-injection or supply-chain attack success against an agent?**

That's much closer to what I think **your research could become**.

For example:

```text
             Malicious Skill
                   │
        ┌──────────┼──────────┐
        ↓          ↓          ↓
     English     Bangla     Chinese
        │          │          │
        ↓          ↓          ↓
      Agent      Agent      Agent
        │          │          │
        ↓          ↓          ↓
      ASR        ASR        ASR
        │          │          │
        └──────────┼──────────┘
                   ↓
          Cross-lingual gap?
```

Then go one level deeper:

```text
Same malicious intent
       │
       ├── English wording
       ├── Bangla wording
       ├── Hindi wording
       ├── Arabic wording
       ├── Chinese wording
       └── Code-switching
              ↓
        Skill / Tool poisoning
              ↓
             Agent
              ↓
        Tool invocation
              ↓
         Attack success
```

And then the really interesting research question:

> **Do existing skill/tool scanners and runtime defenses remain effective when malicious instructions are expressed in languages other than English?**

That gives you **attack + evaluation + defense**, rather than just another ASR paper.

---

# 📚 My recommended core reading set

If you're going to commit to this direction, **don't read all 15 equally**.

Start with these **10**, in this order:

|  Order | Paper                                                                    | Why                                         |
| -----: | ------------------------------------------------------------------------ | ------------------------------------------- |
|  **1** | **Do Agent Skills Speak Safety in Every Language?**                      | 🎯 Your exact intersection                  |
|  **2** | **Skill-Inject**                                                         | Skill-file attack benchmark                 |
|  **3** | **Agent Skills in the Wild**                                             | Large-scale ecosystem evidence              |
|  **4** | **Do Not Mention This to the User**                                      | Real malicious skills                       |
|  **5** | **Supply-Chain Poisoning Attacks...**                                    | Skill supply-chain attack mechanism         |
|  **6** | **Under the Hood of SKILL.md**                                           | Semantic supply-chain attack                |
|  **7** | **Multilingual Jailbreak Challenges**                                    | Multilingual foundation                     |
|  **8** | **Do Methods to Jailbreak and Defend LLMs Generalize Across Languages?** | Cross-language methodology                  |
|  **9** | **MIPIAD**                                                               | Multilingual indirect injection + tools/RAG |
| **10** | **Systematic Analysis of MCP Security**                                  | Tool/MCP threat foundation                  |

### And here's my opinion:

**Don't name your topic yet.**

Your current candidate:

> **"Tool/Skill Supply-Chain Attacks + Multilingual"**

is **promising**, but it's still a *research area*, not a research question.

After you read those 10, we should do a **gap analysis matrix**:

```text
Paper
 │
 ├── Attack vector
 ├── Language
 ├── Skill/tool/MCP
 ├── Attack generation
 ├── Agent type
 ├── Dataset
 ├── Evaluation metric
 ├── Defense
 ├── Limitations
 └── Explicit future work
             ↓
       Research gaps
             ↓
      3–5 candidate topics
             ↓
       Feasibility check
             ↓
        FINAL TOPIC
```

And **I would specifically investigate Bangla as one of the languages** if your experiments can support it. The existence of recent work evaluating English/Bangla multilingual indirect prompt injection means there is already a methodological starting point, while the skill-supply-chain × multilingual intersection remains very young. ([arXiv][10])

That combination could give you a much more distinctive research contribution than another generic *"LLM jailbreak using prompt X"* paper.

[1]: https://openreview.net/pdf?id=L3SGYJLNgB&utm_source=chatgpt.com "Do Agent Skills Speak Safety in Every Language?A Cross-Lingual Security Analysis of the Skills Ecosystem"
[2]: https://arxiv.org/abs/2602.20156?utm_source=chatgpt.com "Skill-Inject: Measuring Agent Vulnerability to Skill File Attacks"
[3]: https://arxiv.org/pdf/2601.10338?utm_source=chatgpt.com "Agent Skills in the Wild: An Empirical Study of Security ..."
[4]: https://www.alphaxiv.org/abs/2602.06547?utm_source=chatgpt.com "\"Do Not Mention This to the User\": Detecting and Understanding Malicious Agent Skills in the Wild | alphaXiv"
[5]: https://arxiv.org/abs/2604.03081?utm_source=chatgpt.com "Supply-Chain Poisoning Attacks Against LLM Coding Agent Skill Ecosystems"
[6]: https://arxiv.org/abs/2605.11418?utm_source=chatgpt.com "Under the Hood of SKILL.md: Semantic Supply-chain Attacks on AI Agent Skill Registry"
[7]: https://www.alphaxiv.org/abs/2602.14211?utm_source=chatgpt.com "SkillJect: Effectively Automating Skill-Based Prompt Injection for Skill-Enabled Agents | alphaXiv"
[8]: https://arxiv.org/html/2510.06445v3?utm_source=chatgpt.com "A Survey on Agentic Security: Applications, Threats and ..."
[9]: https://arxiv.org/abs/2605.14460?utm_source=chatgpt.com "Exploiting LLM Agent Supply Chains via Payload-less Skills"
[10]: https://arxiv.org/abs/2605.07269?utm_source=chatgpt.com "MIPIAD: Multilingual Indirect Prompt Injection Attack Defense with Qwen -- TF-IDF Hybrid and Meta-Ensemble Learning"
