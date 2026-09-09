# Research Context — Al-mizan

## 1. Researcher Profile

I am **Al-mizan**, a 4th-year Computer Science & Engineering undergraduate at **Jahangirnagar University, Bangladesh**.

I am doing ML/deep-learning research under **Dr. Md. Rafsan Jani**.

My previous technical background includes:

* Computer vision
* YOLOv11m vehicle detection
* EfficientNet-B0 + CBAM crop-disease detection
* Python / C/C++
* Backend engineering / Go
* Competitive programming
* General ML/deep-learning knowledge

I am now moving deeper into **LLM security / AI-agent security research**.

My research level should be treated as:

> **Strong software/ML engineer, growing researcher in LLM and agent security.**

Do not explain basic concepts like transformers, embeddings, training loops, etc. unless necessary. I need **mechanistic explanations**, research comparisons, assumptions, limitations, and experimental reasoning.

---

# 2. Current Research Direction

My research initially explored:

> **LLM jailbreaks + guardrails + adversarial ML**

Topics included:

* RLHF
* Constitutional AI
* inference-time defenses
* jailbreaks
* persona-based jailbreaks
* prompt injection
* adversarial suffixes
* GCG-style attacks
* multimodal jailbreaks

However, my research direction has increasingly shifted toward:

> **Agentic AI Security → Tool-use Security → Authorization / Least Privilege → Runtime Enforcement**

The important distinction is:

### Traditional LLM security

```text
User
 ↓
LLM
 ↓
Response
```

The main concern is whether the model produces harmful content.

### Agent security

```text
User
 ↓
LLM Agent
 ↓
Planning / Memory / Retrieval
 ↓
Tool selection
 ↓
Tool execution
 ↓
Real-world side effect
```

Now the critical question becomes:

> **Even if the model is manipulated, can the attacker make the agent perform an unauthorized action?**

This is much closer to traditional security engineering.

---

# 3. Research Theme We Were Converging Toward

The strongest direction identified so far is:

> **Security of tool-using LLM agents against indirect prompt injection, especially when untrusted/multilingual/multimodal content reaches the agent and attempts to induce unauthorized tool actions.**

A more security-oriented formulation is:

> **Runtime authorization and least-privilege enforcement for LLM agents under indirect prompt injection.**

And a potentially more novel extension:

> **Multilingual / cross-lingual indirect prompt injection against tool-using agents and whether authorization mechanisms remain language-agnostic.**

Another possible extension:

> **Tool / skill / plugin supply-chain attacks combined with multilingual or indirect prompt injection.**

This last idea came up explicitly as:

> **Tool and/or Skill Supply-Chain Attacks + Multilingual → one research domain**

But this should be treated as a **candidate direction**, not yet the final research topic.

---

# 4. Important Conceptual Shift

One of the key research insights is:

### Prompt-level defense

```text
Input
 ↓
Prompt filter
 ↓
LLM
 ↓
Tool
```

tries to determine:

> "Is this instruction malicious?"

Whereas a stronger security architecture asks:

> "Even if the LLM believes this instruction, is the resulting action authorized?"

For example:

```text
Untrusted document
       ↓
Indirect injection
       ↓
LLM believes attacker instruction
       ↓
Agent decides:
"Send email"
       ↓
Authorization layer
       ↓
❌ Unauthorized
```

The authorization layer does not necessarily need to understand whether the original text was a jailbreak.

It can enforce:

```text
WHO
WHAT
WHICH RESOURCE
UNDER WHICH CONDITIONS
WITH WHAT PRIVILEGE
```

This is potentially a more robust security boundary.

---

# 5. Important Agent Security Concepts

The research should consider the full agent pipeline:

```text
User Input
     ↓
Context Construction
     ↓
System Instructions
     ↓
Retrieved Content
     ↓
Memory
     ↓
Tool Outputs
     ↓
LLM Reasoning
     ↓
Tool Selection
     ↓
Authorization
     ↓
Tool Execution
     ↓
External Side Effect
```

Attack surfaces include:

1. Direct prompt injection
2. Indirect prompt injection
3. Tool-output injection
4. Retrieval poisoning
5. Memory poisoning
6. Tool manipulation
7. Malicious plugins/tools
8. Skill/plugin supply-chain attacks
9. Inter-agent communication
10. Excessive tool permissions
11. Long-horizon attack chains
12. Multilingual attacks
13. Multimodal attacks

---

# 6. Key Papers / Systems Already Explored

## AgentDojo

**AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents**

Debenedetti et al., 2024.

This is one of the central papers in my research.

AgentDojo evaluates tool-using agents under prompt injection.

It contains:

* 97 realistic tasks
* 629 security test cases
* tool-using environments
* attack scenarios
* defense mechanisms

The core idea is extremely important:

> External data returned by tools can contain malicious instructions that manipulate the agent.

([arXiv][1])

Repository:

[AgentDojo GitHub](https://github.com/sequrity-ai/agentdojo?utm_source=chatgpt.com)

---

# 7. Agent Security Bench — ASB

**Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents**

ICLR 2025.

This is another major benchmark we examined.

It evaluates:

* 10 scenarios
* 10 agents
* 400+ tools
* 27 attack/defense methods
* 13 LLM backbones
* 7 evaluation metrics

The benchmark covers attacks involving:

* system prompts
* user prompts
* tools
* memory
* mixed attacks
* backdoors

Reported attack success rates can be very high, with the paper reporting a maximum average ASR of **84.30%** for evaluated settings. ([ICLR Proceedings][2])

This is important because it demonstrates that agent security is not simply an ordinary LLM jailbreak problem.

---

# 8. Indirect Prompt Injection

This is one of the most important concepts for my research.

Traditional jailbreak:

```text
Attacker → directly talks to LLM
```

Indirect prompt injection:

```text
Attacker
   ↓
Malicious webpage/document/email/tool output
   ↓
Agent retrieves it
   ↓
LLM processes it as context
   ↓
Agent follows attacker-controlled instruction
```

The attacker may never directly communicate with the agent.

This creates a fundamental:

> **data vs instruction separation problem**

The agent has to distinguish:

```text
"Here is information you should read"
```

from:

```text
"Here is an instruction you should execute"
```

---

# 9. Tool-Use Security

The important security question is not simply:

> "Can the model resist prompt injection?"

Instead:

> **"What happens if the model fails?"**

Suppose an agent has:

```text
read_email()
send_email()
delete_email()
transfer_money()
```

If the LLM is compromised by indirect injection, unrestricted tool access can turn a language-model failure into a real security incident.

Therefore:

```text
LLM safety
      ≠
Agent security
```

A stronger architecture is:

```text
LLM
 ↓
Proposed Action
 ↓
Policy / Authorization Layer
 ↓
Tool
```

---

# 10. Least Privilege

This is one of the most promising concepts for the research.

Traditional security principle:

> Give a component only the permissions required to perform its task.

Applied to agents:

Instead of:

```text
Agent
 ├── read email
 ├── send email
 ├── delete email
 ├── access database
 ├── modify database
 └── transfer money
```

use:

```text
Task A
 ├── read email
 └── draft email

Task B
 ├── read database
 └── create report

Task C
 └── transfer money
       + additional authorization
```

The idea is:

> **Reduce the blast radius of a compromised agent.**

---

# 11. Runtime Enforcement

This is potentially more interesting than another prompt filter.

Architecture:

```text
                 ┌───────────────┐
User ──────────→ │   LLM Agent   │
                 └───────┬───────┘
                         │
                  Proposed Tool Call
                         │
                         ▼
              ┌─────────────────────┐
              │ Runtime Enforcement │
              │      Layer          │
              └─────────┬───────────┘
                        │
                 Authorization?
                    /       \
                  YES        NO
                   │          │
                   ▼          ▼
                 Tool       BLOCK
```

The enforcement layer could evaluate:

* tool identity
* user identity
* agent identity
* task context
* resource
* operation
* parameters
* risk level
* provenance
* current permissions
* previous actions
* policy

---

# 12. Multilingual Security

Another direction we became interested in is:

> **Does agent security generalize across languages?**

Most LLM security benchmarks are heavily English-centric.

Potential attack flow:

```text
English system policy
        ↓
Agent
        ↓
Bengali / Hindi / Arabic / Chinese / etc.
        ↓
Malicious retrieved content
        ↓
Tool invocation
```

Questions:

1. Does an injection detector trained/evaluated in English work in Bengali?
2. Does multilingual reasoning increase attack success?
3. Does code-switching weaken defenses?
4. Does translation before security filtering help or hurt?
5. Can an attacker hide malicious intent through cross-lingual transformation?
6. Does authorization remain robust even when the model interprets multilingual content incorrectly?

This is much more interesting if framed as an **agent security problem**, rather than simply "multilingual jailbreaks."

---

# 13. Multimodal Agent Security

Another previously explored direction was:

> **Multimodal Jailbreaking**

Potential attack path:

```text
Image / PDF / Screenshot / Webpage
             ↓
        Vision-Language Model
             ↓
       Agent reasoning
             ↓
          Tool call
```

The security problem becomes:

> Can malicious instructions embedded in images/documents influence tool use?

For example:

```text
Invoice image
     ↓
OCR / Vision
     ↓
"Send payment to this account"
     ↓
Agent
     ↓
Payment tool
```

This creates an intersection between:

* multimodal prompt injection
* indirect prompt injection
* tool-use security
* authorization

This is a promising area but potentially much broader than the multilingual direction.

---

# 14. Tool / Skill / Plugin Supply-Chain Security

Another research direction we explicitly discussed:

> **Tool and/or Skill Supply-Chain Attacks + Multilingual**

The intuition:

Modern agents increasingly depend on:

```text
Agent
 ↓
Tools
 ↓
Plugins
 ↓
Skills
 ↓
MCP servers / connectors
 ↓
External APIs
```

A malicious or compromised tool/skill could:

* return malicious instructions
* manipulate tool descriptions
* request excessive permissions
* exfiltrate information
* influence future agent decisions
* modify context
* exploit implicit trust

This is analogous to software supply-chain security.

Potential research question:

> **Can a compromised tool/skill induce unauthorized actions in an LLM agent despite runtime security controls?**

This could be combined with:

> multilingual tool descriptions / tool outputs

but should not become too broad.

---

# 15. Important Recent Research Signal

Recent research strongly supports the direction of focusing on **runtime enforcement and security–utility trade-offs**, rather than simply producing another prompt filter.

A 2025 paper on indirect prompt injections argues that existing agent benchmarks can become saturated by relatively simple defenses and calls for **stronger adaptive attacks and better evaluation metrics**. ([arXiv][3])

This is extremely relevant to my research-gap search.

It means:

> "We proposed another prompt-injection detector and got 95% ASR reduction on AgentDojo"

may **not** be a sufficiently strong research contribution.

The benchmark itself may be the problem.

---

# 16. Security–Utility Tradeoff

This is another major research issue.

A defense can simply block almost everything:

```text
Attack → blocked
Benign action → also blocked
```

Then:

```text
Security = high
Utility = terrible
```

For example, recent AgentDojo evaluations show large differences between defenses in attack success, benign utility, and available actions. ([MDPI][4])

Therefore experiments should measure at least:

### Security

* Attack Success Rate
* Unsafe Tool Action Rate
* Unauthorized Action Rate
* Data Exfiltration Rate

### Utility

* Task Success Rate
* Benign Task Success
* Tool availability
* Overblocking

### Operational cost

* latency
* token cost
* number of model calls
* computational overhead

---

# 17. Recent Benchmark Direction

A very relevant 2026 benchmark is **NetInjectBench**, which studies indirect prompt injection in network-operation agents.

It separates:

* untrusted artifact text
* trusted policy metadata
* evaluation labels

and evaluates tool-use attacks.

An important result is that prompt-level defenses reduce unsafe actions but can still leave significant failures, whereas a metadata-aware policy gate can enforce much stronger execution-time boundaries under its stated assumptions. ([arXiv][5])

This is highly relevant to the direction:

> **Prompt defense → authorization defense**

because it provides evidence that the security boundary can be moved closer to actual tool execution.

---

# 18. Current Research Gap Hypothesis

The current hypothesis is **not yet a proven literature gap**.

It needs systematic literature validation.

But the strongest candidate gap currently looks like:

> **Existing LLM-agent security research heavily evaluates prompt injection detection/sanitization, while comparatively less work systematically studies language-agnostic runtime authorization and least-privilege enforcement against multilingual indirect prompt injection in realistic tool-using agents.**

Potential novelty dimensions:

```text
                 Agent Security
                       │
        ┌──────────────┼──────────────┐
        │              │              │
   Multilingual    Tool Use       Runtime Auth
        │              │              │
        └──────────────┼──────────────┘
                       │
               Research Gap
```

But **do not claim this as a final gap yet**.

We need to verify:

1. Who has already studied multilingual agent attacks?
2. Who has studied multilingual indirect prompt injection?
3. Who has studied authorization-based defenses?
4. Who has studied least privilege for agents?
5. Who has combined multilingual attacks + authorization?
6. Which benchmarks support this?
7. Whether existing frameworks already implement it.
8. Whether recent 2026 papers have closed the gap.

---

# 19. Candidate Research Questions

### RQ1 — Attack robustness

> How effective are indirect prompt injections across different languages in tool-using LLM agents?

### RQ2 — Cross-lingual generalization

> Do existing prompt-injection defenses trained/evaluated primarily in English generalize to multilingual attacks?

### RQ3 — Authorization

> Can runtime authorization prevent unsafe tool actions even when the underlying LLM is successfully manipulated?

### RQ4 — Least privilege

> How does dynamically restricting agent permissions affect attack success and benign task utility?

### RQ5 — Security–utility tradeoff

> Can runtime authorization achieve better security–utility tradeoffs than prompt-level defenses?

### RQ6 — Adaptive attacks

> Can multilingual indirect injections adapt to the agent's available tools and authorization policies?

---

# 20. Possible Experimental Setup

A reasonable first prototype:

```text
                 AgentDojo / custom environment
                            │
                            ▼
                    Tool-using agent
                            │
              ┌─────────────┴─────────────┐
              │                           │
        English attacks             Multilingual attacks
              │                           │
              └─────────────┬─────────────┘
                            ▼
                     Defense layer
                            │
             ┌──────────────┼──────────────┐
             │              │              │
         No defense    Prompt defense   Runtime Auth
                                           │
                                      Least privilege
```

Compare:

### Baseline A

No defense.

### Baseline B

Prompt sanitization / injection detection.

### Baseline C

Tool filtering.

### Baseline D

Runtime authorization.

### Baseline E

Runtime authorization + least privilege.

Then evaluate:

```text
ASR
Unsafe Tool Action Rate
Task Success
Benign Utility
Overblocking
Latency
Cost
```

---

# 21. Potential Research Architecture

A stronger proposed architecture could be:

```text
             External Content
                    │
                    ▼
             ┌─────────────┐
             │ LLM Agent   │
             └──────┬──────┘
                    │
              Proposed Action
                    │
                    ▼
       ┌─────────────────────────┐
       │ Policy / Authorization  │
       │         Engine          │
       └────────────┬────────────┘
                    │
        ┌───────────┼───────────┐
        │           │           │
      Identity    Resource    Action
        │           │           │
        └───────────┼───────────┘
                    │
              Risk Assessment
                    │
             ┌──────┴──────┐
             │             │
           ALLOW          DENY
             │
             ▼
          Tool/API
```

Potentially add:

```text
Provenance
   +
Language
   +
Task context
   +
Permission scope
   +
Action history
```

---

# 22. Papers / Topics I Have Been Reading

The project has included discussion/review of papers around:

### Core agent security

* AgentDojo
* Agent Security Bench (ASB)
* LLM agent security surveys
* indirect prompt injection
* tool-use security
* runtime defense

### Jailbreaking / LLM safety

I have also studied or discussed papers involving:

* jailbreak attacks
* GCG / adversarial suffix attacks
* persona-based jailbreaks
* prompt injection
* guardrails
* RLHF
* Constitutional AI
* inference-time defenses
* multimodal jailbreaks

### Recent papers I explicitly brought into the project

I asked for abstract/introduction/section overviews of papers including:

* `2309.15817`
* `2511.00689`
* `2605.18239`
* `2605.11418`
* `2602.14211`
* `2603.22489`

Some of these were discussed section-by-section, while others were primarily abstract/introduction/conclusion reviews.

When continuing the research, **do not assume these papers are necessarily part of the final topic**. They represent the exploration phase.

---

# 23. My Research Folder / Workflow

I maintain a research folder for this work, including markdown notes and paper-related materials.

One structure I was using looked roughly like:

```text
research/
├── ai-agent-security-and-jailbreaks-raw-v3.md
├── images/
│   ├── Groq api.png
│   └── notebook.png
├── knowledge_accumulation_...
└── papers / notes
```

The goal is to accumulate knowledge rather than just collect papers.

I also use:

* ChatGPT
* Claude
* Antigravity / agentic coding tools
* GitHub
* Google Colab
* arXiv
* research papers
* potentially Figma/Canva for presentation preparation

---

# 24. How Research-Gap Analysis Should Be Done

Do **not** just search:

> "LLM agent security research gap"

and invent a novelty claim.

Instead construct a matrix.

## Dimension 1 — Attack

```text
Direct injection
Indirect injection
Tool-output injection
Memory poisoning
Multimodal injection
Multilingual injection
Supply-chain attack
```

## Dimension 2 — Agent component

```text
Prompt
RAG
Memory
Tool
Skill/plugin
MCP
Multi-agent communication
```

## Dimension 3 — Defense

```text
Prompt filtering
Input sanitization
Detection
Tool filtering
Sandboxing
Authorization
Least privilege
Runtime monitoring
Policy enforcement
```

## Dimension 4 — Evaluation

```text
ASR
Unsafe actions
Task success
Utility
Overblocking
Latency
Adaptive attacks
Cross-model generalization
Cross-language generalization
```

Then create:

```text
Paper × Attack × Component × Defense × Dataset × Model × Metric
```

The missing combinations are candidate gaps.

---

# 25. What Counts as a Strong Gap

A weak gap:

> "Nobody has studied X."

A stronger gap:

> "Existing approaches evaluate X under Y assumptions, but fail to evaluate Z."

An even stronger gap:

> "Existing defenses improve security on benchmark A but rely on assumptions B and C. Under adaptive/multilingual/tool-aware attacks, those assumptions may fail. No existing evaluation systematically measures the security–utility tradeoff under these conditions."

The final research proposal should ideally have:

```text
Existing limitation
       ↓
Specific hypothesis
       ↓
New threat model / method
       ↓
Controlled experiment
       ↓
Quantitative evaluation
       ↓
Security insight
```

---

# 26. Important Warning About Benchmark Research

A major lesson from recent literature:

> **Do not blindly trust benchmark ASR numbers.**

Recent work has pointed out issues such as:

* weak attacks
* flawed metrics
* implementation bugs
* benchmark saturation
* insufficient adaptive attacks

The 2025 indirect-injection/firewall work explicitly argues that existing benchmarks can give misleadingly strong-looking defense results because the attacks are not sufficiently strong. ([arXiv][3])

So if we propose a new defense, we should also ask:

> **Does it survive adaptive attacks designed specifically against the defense?**

---

# 27. Strong Candidate Research Directions

Ranked roughly by how interesting I currently think they are:

### 🥇 Direction 1 — Multilingual Indirect Prompt Injection + Runtime Authorization

```text
Multilingual malicious content
             ↓
       Agent retrieval
             ↓
       LLM manipulation
             ↓
       Proposed tool call
             ↓
     Runtime authorization
             ↓
       ALLOW / DENY
```

Research question:

> Can language-agnostic runtime authorization prevent unsafe agent actions even when multilingual indirect prompt injection successfully manipulates the LLM?

---

### 🥈 Direction 2 — Adaptive Indirect Injection + Least Privilege

Instead of asking whether the agent can detect attacks:

> What happens if the attacker knows the agent's tools and tries to maximize the damage possible with the agent's permissions?

Focus:

```text
Attack capability
       ×
Permission scope
       ×
Blast radius
```

This has a strong traditional security flavor.

---

### 🥉 Direction 3 — Tool/Skill Supply Chain + Runtime Enforcement

```text
Malicious/compromised skill
           ↓
       Tool output
           ↓
     Agent reasoning
           ↓
    Unauthorized action
           ↓
 Runtime policy enforcement
```

Potentially very relevant as agent ecosystems increasingly depend on external tools/connectors.

---

### Direction 4 — Multimodal Indirect Injection + Tool Security

```text
Image/PDF/Webpage
       ↓
Vision-language model
       ↓
Agent
       ↓
Tool
```

Interesting, but experimental complexity is higher.

---

# 28. What I Do NOT Want

Do not steer this project toward:

* generic ML research
* generic cybersecurity
* ordinary chatbot jailbreak generation
* simply collecting jailbreak prompts
* novel exploit scripts
* "make an LLM say something bad"
* another basic prompt filter
* a paper that only reports ASR on one benchmark
* ungrounded claims of novelty

Also:

> **Do not generate working jailbreak/attack scripts.**

We can discuss published attack mechanisms and design safe evaluation protocols, but the goal is defensive/security research.

---

# 29. What I Need From an AI Research Assistant

When helping me, prioritize:

### 1. Mechanism

Explain:

> **Why does this attack/defense work?**

not just:

> "This paper proposes X."

### 2. Threat model

Always identify:

```text
Attacker capability
Attacker knowledge
Attack surface
Target
Security objective
Assumptions
```

### 3. Evaluation

Ask:

```text
What dataset?
What agent?
What model?
What attack?
What defense?
What metric?
What baseline?
```

### 4. Limitations

Explicitly identify:

* weak assumptions
* unrealistic threat models
* benchmark artifacts
* missing baselines
* poor generalization
* security–utility tradeoffs
* adaptive attack weaknesses

### 5. Research gap

Separate:

> **What the paper says**

from:

> **What the paper fails to investigate**

and finally:

> **What could become a research question**

---

# 30. Paper Review Format

Whenever I give you a paper to review, use exactly:

```text
Title:
Authors:
Year:
Problem: What problem is solved?
Idea: One sentence explanation.
Method: How does it work?
Dataset:
Results:
Advantages:
Limitations:
Things I don't understand:
Questions:
```

Each field should be concise.

**Method** can be longer when the mechanism requires it.

For:

### Things I don't understand

Do not leave it blank just because I didn't ask anything.

Identify:

* genuinely ambiguous mechanisms
* underspecified experiments
* unclear assumptions
* potentially questionable claims
* missing implementation details
* contested conclusions

For:

### Questions

Give research-level questions worth asking the authors or investigating further.

---

# 31. Current Working Research Thesis

If I had to summarize the current research direction in one paragraph:

> **I am investigating security risks in tool-using LLM agents, with particular interest in indirect prompt injection and the transition from prompt-level defenses toward execution-time authorization and least-privilege enforcement. A promising unexplored intersection is multilingual indirect prompt injection, where attacker-controlled content in languages other than English manipulates agents into proposing unauthorized tool actions. The research goal is to determine whether language-agnostic runtime authorization can maintain security even when the underlying LLM is successfully manipulated, while preserving benign task utility.**

This is currently the **working hypothesis**, not a finalized claim of novelty.

---

# 32. Current Research-Gap Mission

The next step should **not** immediately be implementation.

The proper sequence is:

```text
                    Literature
                       │
                       ▼
              Build taxonomy
                       │
                       ▼
             Find existing work
                       │
                       ▼
             Identify overlap
                       │
                       ▼
              Find true gaps
                       │
                       ▼
             Select 1–2 gaps
                       │
                       ▼
             Formulate RQs
                       │
                       ▼
             Threat model
                       │
                       ▼
              Experiment design
                       │
                       ▼
               Prototype
                       │
                       ▼
                Evaluation
```

---

# 33. Immediate Next Task

The next research task I want an AI assistant to perform is:

> **Conduct a systematic research-gap analysis around multilingual indirect prompt injection, tool-using LLM agents, runtime authorization, least privilege, and tool/skill supply-chain security.**

Specifically search literature from approximately **2023–2026**, prioritizing:

1. Original research papers
2. Top ML/security conferences
3. arXiv when necessary
4. Benchmarks
5. Open-source implementations

Build a matrix like:

| Paper | Year | Attack | Agent | Tool | Multilingual | Supply Chain | Defense | Runtime Auth | Least Privilege | Benchmark | Main Limitation |
| ----- | ---: | ------ | ----- | ---- | ------------ | ------------ | ------- | ------------ | --------------- | --------- | --------------- |

Then identify:

### Gap A

What is already heavily studied?

### Gap B

What is partially studied?

### Gap C

What combinations appear genuinely underexplored?

### Gap D

Which gap is feasible for an undergraduate research project with limited compute?

### Gap E

Which gap has enough novelty for a publishable paper?

---

# 34. Important Current Literature Signal

The field is moving toward **defense-in-depth rather than relying solely on prompt filtering**. A 2026 survey explicitly frames agent security around vulnerabilities spanning retrieval, memory, tool invocation, and communication, and emphasizes combining preventive mechanisms with runtime monitoring and containment. ([Springer][6])

Another recent survey similarly highlights that agent security involves attack surfaces beyond the model itself, including tool invocation and long-horizon planning. ([ScienceDirect][7])

And recent work on indirect injection defenses is increasingly emphasizing the **security–utility tradeoff and stronger adaptive evaluation** rather than simply reporting lower ASR. ([MDPI][4])

That makes your move toward:

> **LLM manipulation → authorization boundary → actual tool execution**

a much more promising research framing than simply:

> **LLM manipulation → better prompt filter**

---

# 35. One-Sentence Handoff

If another AI needs the shortest possible context:

> **I am a 4th-year CSE student researching LLM/agent security, moving from jailbreaks and guardrails toward tool-using agent security; my current candidate research direction is multilingual indirect prompt injection against LLM agents and whether runtime authorization/least privilege can prevent unauthorized tool actions even when the LLM itself is successfully manipulated, with tool/skill supply-chain security as another possible extension. I need systematic literature-gap analysis before finalizing the topic, not an assumed novelty claim.**

---

## My recommendation for where we continue

I would **not lock the thesis topic yet**. The next step should be a proper **2023–2026 literature matrix** specifically covering:

**Multilingual × Indirect Prompt Injection × Tool Use × Runtime Authorization × Least Privilege × Tool/Skill Supply Chain**

and then score each candidate gap on:

> **Novelty × Feasibility × Benchmark availability × Compute requirement × Security significance × Publication potential.**

That will tell us whether the real opportunity is **multilingual agent attacks**, **authorization**, **least privilege**, **supply-chain security**, or—more interestingly—the intersection of two or three of them. Recent literature already suggests that generic prompt-injection defense is becoming crowded and benchmark-sensitive, so the intersection is where I'd look first. ([arXiv][3])

[1]: https://arxiv.org/abs/2406.13352?utm_source=chatgpt.com "AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents"
[2]: https://proceedings.iclr.cc/paper_files/paper/2025/hash/5750f91d8fb9d5c02bd8ad2c3b44456b-Abstract-Conference.html?utm_source=chatgpt.com "Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents"
[3]: https://arxiv.org/abs/2510.05244?utm_source=chatgpt.com "Indirect Prompt Injections: Are Firewalls All You Need, or Stronger Benchmarks?"
[4]: https://www.mdpi.com/2073-431X/15/9/570?utm_source=chatgpt.com "Evaluating Indirect Prompt Injection Defenses in Tool-Using LLM Agents: Security, Utility, and Replication"
[5]: https://arxiv.org/abs/2607.10490?utm_source=chatgpt.com "NetInjectBench: Benchmarking Indirect Prompt Injection in Tool-Using Large Language Model Agents for Network Operations"
[6]: https://link.springer.com/article/10.1007/s11416-026-00622-3?utm_source=chatgpt.com "Securing LLM-based agents against cyberattacks: a comprehensive survey on attack techniques and defense strategies | Journal of Computer Virology and Hacking Techniques | Springer Nature Link"
[7]: https://www.sciencedirect.com/science/article/pii/S1566253525010036?utm_source=chatgpt.com "Security of LLM-based agents regarding attacks, defenses, and applications: A comprehensive survey - ScienceDirect"
