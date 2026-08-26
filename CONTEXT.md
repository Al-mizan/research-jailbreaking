# AI Agent Security & Jailbreaking Research

Domain model and canonical vocabulary for research on AI agent vulnerabilities, indirect prompt injection (IPI), RAG knowledge poisoning, and agentic execution hijacks.

## Core Concepts & Trust Boundaries

**Control Plane**:
The privileged channel comprising developer system prompts, safety guidelines, and authenticated user instructions.
_Avoid_: User space, prompt channel

**Reasoning Plane**:
The intermediate state space where the agent plans, decomposes tasks, maintains scratchpads, and executes reasoning steps (e.g. ReAct loops).
_Avoid_: Cognitive plane, internal state

**Data Plane**:
The untrusted channel carrying retrieved documents, API responses, tool observation outputs, and external content.
_Avoid_: External data, payload plane

**Control-Data Conflation**:
The architectural flaw where an LLM interprets text from the untrusted Data Plane as privileged directives from the Control Plane.
_Avoid_: Prompt mixing, input confusion

**Confused Deputy**:
A vulnerability where an agent with high system permissions is tricked by untrusted data into executing unauthorized actions on behalf of an attacker.
_Avoid_: Agent proxy exploit

## Attack Taxonomy & Outcomes

**Indirect Prompt Injection (IPI)**:
An attack where adversarial instructions embedded in passive third-party content (web pages, files, emails, RAG chunks) hijack agent execution flow.
_Avoid_: Data injection, second-order prompt injection

**Direct Prompt Injection (DPI)**:
An attack where the direct user deliberately crafts adversarial prompts to override system instructions or developer constraints.
_Avoid_: Prompt hacking, prompt override

**Jailbreak**:
An attack that bypasses safety alignment training or guardrail policies to cause the model to generate prohibited content or violate safety boundaries.
_Avoid_: Tool exploit, prompt injection (when not bypassing safety policies)

**Tool Hijack**:
An exploit where injected instructions coerce an agent into invoking external tools with attacker-chosen arguments or malicious side-effects.
_Avoid_: Function spoofing, tool misuse (when unintentional)

**Data Exfiltration**:
The unauthorized extraction and transmission of private context, memory, or user data to an attacker-controlled receiver.
_Avoid_: Data leakage, information bleeding

## Agentic State & Memory Vulnerabilities

**Scratchpad Pollution**:
The transient poisoning of an agent's working memory or chain-of-thought during a single execution turn, corrupting intermediate reasoning steps.
_Avoid_: Thought injection, reasoning poisoning

**Episodic Memory Poisoning**:
The contamination of multi-turn conversational history or session logs, causing malicious instructions to persist across subsequent turns in an active session.
_Avoid_: Conversation hijacking, chat history corruption

**Semantic Memory Poisoning**:
The persistent injection of malicious payloads into long-term retrieval databases, user profiles, or knowledge stores that survive across distinct user sessions.
_Avoid_: Long-term memory backdoor, vector memory corruption

## Threat Actors & Interaction Modes

**Passive Adversary**:
An attacker who implants static payloads in external data sources (websites, files, emails) and relies on the agent fetching them during benign workflows without real-time feedback.
_Avoid_: Static attacker, offline adversary

**Active Adversary**:
An attacker who interacts with the agent dynamically across multiple turns, observing tool execution feedback and adapting injected payloads in real time.
_Avoid_: Interactive attacker, dynamic adversary

**Collusive Adversary**:
A threat scenario where an untrusted data provider coordinates with a malicious internal user to bypass authorization or sandbox controls.
_Avoid_: Hybrid attacker, dual-threat agent

## RAG Attack Lifecycle

**Knowledge Poisoning**:
The corruption of the RAG knowledge base, source repositories, or data loaders to place adversarial content into the corpus prior to indexing.
_Avoid_: Corpus poisoning, document contamination

**Retrieval Manipulation**:
Attacks manipulating embedding distances, keyword frequencies, or rankers to force poisoned passages into top-k retrieved results.
_Avoid_: Search hijacking, embedding collision

**Context Exploitation**:
The activation and execution of adversarial instructions contained within retrieved passages once assembled into the model generation prompt.
_Avoid_: Chunk activation, retrieval execution

## Defensive Architecture

**Prompt-Level Isolation**:
Heuristic formatting mechanisms (delimiters, XML tags, border strings, spotlighting) used within prompts to visually separate untrusted data from instructions.
_Avoid_: Soft defense, prompt guarding

**Guardrail Classifier**:
An auxiliary model or heuristic filter (input scanner, LLM judge, perplexity checker) that inspects inputs or outputs for adversarial content before propagation.
_Avoid_: Outer guard, input shield

**Architectural Segregation**:
A system design pattern (such as Dual-LLM or Split-Context) that physically separates privileged planning LLMs from unprivileged data-processing LLMs.
_Avoid_: Two-tier LLM, sandbox model

**Runtime Policy Enforcement**:
Deterministic execution controls (Mandatory Access Control, capability tokens, schema validation, human approval gates) that govern tool calls independently of LLM reasoning.
_Avoid_: Tool sandbox, runtime firewall

## Evaluation Metrics

**Attack Success Rate (ASR)**:
The percentage of attack attempts that successfully achieve the adversary's objective (e.g., executing a target tool, leaking secrets, or violating policy).
_Avoid_: Compromise rate, hack rate

**Benign Utility Retention (BUR)**:
The percentage of benign tasks successfully completed without false-positive refusal or execution degradation when defenses are enabled.
_Avoid_: Clean accuracy, task preservation

**Defense Robustness Rate (DRR)**:
The quantitative reduction in Attack Success Rate achieved by a defense against adaptive or secondary attack mutations.
_Avoid_: Defense effectiveness, mitigation score
