# Separation of Indirect Prompt Injection from Content Safety Jailbreaks in Agent Threat Modeling

## Context

Popular discourse and early LLM security literature frequently overload the term "jailbreak" to describe any adversarial prompt manipulation. In agentic and RAG workflows, however, untrusted data can hijack tool execution or exfiltrate private information without ever producing toxic, harmful, or prohibited textual output that triggers safety alignment boundaries.

## Decision

We strictly separate the adversarial mechanism (**Indirect Prompt Injection** / **Direct Prompt Injection**), the policy violation outcome (**Jailbreak**), and the execution outcome (**Tool Hijack** / **Data Exfiltration**). We reject using "Agentic Jailbreak" as a catch-all umbrella for tool misuse.

## Consequences

Research benchmarks and threat modeling across this repository will evaluate tool hijacking and data leakage independently of content safety filters. Mitigations must address control-data separation rather than relying solely on post-generation toxicity/safety guardrails.
