# Deterministic Runtime Policy Enforcement Seam for Tool Execution

## Context

Current agent frameworks frequently allow LLMs to invoke external tool adapters directly upon generating a function call. As proven across benchmarks (`Agent Security Bench`, `AgentDojo`, `VIGIL`), soft prompt-level delimiters and heuristic guardrails fail to prevent confused deputy attacks and indirect prompt injection when untrusted Data Plane content enters the agent's context.

## Decision

We introduce an in-process **Policy Enforcement Module** positioned at the execution seam between the Reasoning Plane and external Tool Adapters. All tool calls must pass through a single, deep `dispatch(request, context)` interface that deterministically evaluates declarative tool specification manifests, session taint provenance, and behavioral invariants (Mandatory Access Control) before invoking any external adapter.

## Consequences

- Direct, unmediated invocation of tool adapters from the agent reasoning loop is strictly prohibited.
- Tool adapters must register declarative manifests defining parameter schemas, side-effect classifications, and allowed destination invariants.
- Verification is decoupled from LLM stochasticity: security invariants and MAC policies are verified deterministically against the `dispatch()` interface using an in-memory mock adapter in unit test suites.
