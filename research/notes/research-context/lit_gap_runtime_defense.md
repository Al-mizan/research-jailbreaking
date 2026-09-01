# Research Context: Runtime Defense and Authorization for LLM Agents (2025-2026)

## Overview
This report synthesizes the latest literature (2025-2026) on runtime defense, capability-based access control, and formal verification for AI agents. A key question is whether runtime enforcement can prevent unauthorized actions even if an agent is compromised via prompt injection. The consensus is that while prompt injection remains difficult to solve at the input level, structural runtime defenses—acting as an independent control plane—can effectively contain the blast radius and block unauthorized tool execution.

## Recent Papers (2025-2026)

### 1. DreamGuard (2025/2026)
*   **What it proposes:** Uses risk-aware world models to predict potential future hazards by maintaining a latent state of the agent's trajectory (multi-horizon defense).
*   **What it evaluates:** Evaluates the ability to detect "prefix risks" (sequences of individually benign actions that drift toward a hazardous state) across multi-step tasks.
*   **Key limitation:** High computational overhead to simulate latent states at runtime, potentially increasing latency for fast-acting agents.

### 2. Cordon (2025/2026)
*   **What it proposes:** Treats multi-step agent workflows as semantic transactions. It intercepts tool calls and allows for staging, validating, and rolling back actions if a hazard is detected.
*   **What it evaluates:** Success rate of intercepting and rolling back malicious tool chains triggered by prompt injections.
*   **Key limitation:** Irreversible actions (e.g., sending an email, physical actuation) cannot be easily rolled back, limiting its effectiveness in certain domains.

### 3. AC4A (2025)
*   **What it proposes:** A resource-centric Capability-Based Access Control (CapBAC) framework. It defines permissions over resources (hierarchical types) rather than just API endpoints.
*   **What it evaluates:** Uniform enforcement of least privilege across different agent environments and operational domains.
*   **Key limitation:** Complex policy authoring; requiring developers to map out detailed resource hierarchies can lead to misconfigurations.

### 4. CapChain (2026)
*   **What it proposes:** Uses HMAC-based capability tokens and verifiable provenance to ensure agents possess minimum necessary authority, allowing for "attenuation of authority" as tasks are delegated.
*   **What it evaluates:** Security of multi-agent interactions and supply chain risks, ensuring that permissions cannot be escalated by downstream sub-agents.
*   **Key limitation:** The overhead of token verification and the complexity of securely propagating cryptographic tokens across distributed agent swarms.

### 5. AgentVerify (2025)
*   **What it proposes:** A formal verification framework using Linear Temporal Logic (LTL) model checking to ensure agents adhere to predefined safety specifications.
*   **What it evaluates:** Theoretical soundness and the tradeoff between blocking unsafe actions and overall task completion rates.
*   **Key limitation:** "Specification bottleneck" (translating natural language safety rules to formal logic is error-prone) and a "verifier tax" (rigorous blocking of unsafe actions often reduces task completion rates by blocking safe, but unverified, alternative paths).

### 6. HARD (Harness-based Autonomous Runtime Defense Evolution) (2026)
*   **What it proposes:** A self-evolving defense mechanism that automatically adapts and improves its runtime guardrails by analyzing failure traces from previous agent attempts.
*   **What it evaluates:** The system's ability to autonomously patch vulnerabilities and adapt to novel attack vectors over time.
*   **Key limitation:** Can be bypassed by zero-day attacks before the system has a chance to observe and adapt to the new failure trace.

*(Note: The user also referenced SEAgent for least privilege and VIGIL for behavioral policies/execution traces, which represent the baseline for these 2025-2026 advancements).*

## The Multilingual Attack Gap
Have runtime defenses been tested against multilingual attacks? 
Most structural runtime defenses (like sandboxing, IAM, and capability tokens) are inherently **language-agnostic**—they do not care about the language of the prompt, only the semantics of the requested tool execution. Therefore, they are naturally resilient to multilingual prompt injections bypassing input filters.
However, for runtime defenses that rely on **semantic intent checking** (e.g., an LLM-in-the-loop evaluating if a tool call is safe), multilingual attacks remain a gap. Research shows that secondary evaluation models can still be confused by low-resource languages, indicating a need for more robust multilingual behavioral anomaly detection.

## State of Agent Authorization in Production Systems (2026)
*   **Anthropic:** Has heavily championed the **Model Context Protocol (MCP)**, which is becoming a standard for integrating tools with LLMs. MCP inherently supports capability-based security, standardizing how context and tool access are provisioned.
*   **Google:** Vertex AI focuses heavily on **Identity Bridges** and integrating agents with Google Cloud IAM (Service Account impersonation). Security policies are tied to the agent instance, enabling enterprise-grade least privilege.
*   **OpenAI:** The Assistants API emphasizes infrastructure-level **sandboxing** (e.g., Code Interpreter running in isolated microVMs) to contain the blast radius of compromised agents.

## Summary

**Is runtime defense for AI agents a MATURE or EMERGING field?**
It is firmly an **EMERGING** field. While the conceptual shift from reactive prompt-filtering to proactive, stateful, and structural runtime defense is established, the implementation frameworks are still evolving.

**What gaps exist?**
1.  **The Verifier Tax:** Balancing strict security policies with agent autonomy. Current formal verification often breaks agent workflows, leading to low completion rates.
2.  **Irreversible Actions:** Transactional rollback works for databases but fails for physical actuators or external communications.
3.  **Specification Bottleneck:** Translating human intent for safety into machine-enforceable policies or formal logic remains highly error-prone.
4.  **Multilingual Semantic Verification:** While structural controls resist multilingual attacks, semantic runtime checks (LLM evaluators) are still vulnerable.
5.  **Long-Term Memory Poisoning:** Distinguishing between benign learned context and malicious planted instructions over long time horizons is an unsolved challenge in behavioral anomaly detection.
