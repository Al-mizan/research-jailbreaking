# AI Agent Security & Multilingual Jailbreaking Research

Repository dedicated to empirical research on LLM agent vulnerabilities, indirect prompt injection (IPI), agent skill/tool supply-chain security, and cross-lingual safety alignment disparities.

---

## 🗺️ Repository Architecture & Sitemap

This map allows human researchers and AI agents to navigate the workspace directly without expensive recursive directory traversals.

| Directory / File | Description & Contents |
| :--- | :--- |
| **`CONTEXT.md`** | **Canonical Domain Glossary**. Authoritative definitions, trust boundaries, threat taxonomy, and prohibited aliases (`_Avoid_`). |
| **`AGENTS.md`** | Agent guidelines, issue tracking specs (`.scratch/<feature-slug>/`), and triage labels. |
| **`docs/adr/`** | **Architecture Decision Records**. Core technical decisions (e.g., ADR-0001 on separating IPI from jailbreaks, ADR-0002 on deterministic policy enforcement). |
| **`papers/`** | **Primary Literature & Decks**. Original research PDFs and presentation decks. |
| ├─ `Tools and skills supply chain attacks/` | Part 1 & Part 2 supply-chain papers (MCP poisoning, SKILL.md lifecycle, DDIPE, 31k/98k skills audits). |
| ├─ `Multilingual/` | Cross-lingual jailbreak benchmarks and low-resource African language attack studies. |
| ├─ `AgenticJailbreaking/` | Agentic loop vulnerabilities, confused deputy attacks, and memory poisoning papers. |
| ├─ `RAGJailbreaking/` | Knowledge poisoning, retrieval manipulation, and context exploitation literature. |
| └─ `*.pptx` | Executive slide decks for literature reviews and supervisor presentations. |
| **`research/notes/`** | **Synthesized Research & Gap Analyses**. |
| ├─ `Cross-Lingual + AI Agent Skills.../` | Synthesized cross-lingual and supply-chain literature maps and research questions. |
| ├─ `research-context/` | Granular research gap analyses, benchmark design inputs, and review logs. |
| ├─ `raw/` | Heavy web crawls, raw evidence dumps (e.g., `ai-agent-security-and-jailbreaks-raw-v3.md`). *Agents: Avoid reading in bulk.* |
| └─ `literature_gap_analysis.md` | Formal literature gap assessment and PhD proposal foundations. |
| **`repos/BIPIA/`** | **Benchmark Codebase**. Indirect Prompt Injection Attack benchmark, model wrappers, metrics, and defense modules. |
| **`.agents/skills/`** | Specialized agent skills (`improve-codebase-architecture`, `codebase-design`, `domain-modeling`, `research-proposal`, etc.). |

---

## 🤖 Directives for AI Agents (Antigravity AI)

1. **Check `CONTEXT.md` First**: Always use canonical project vocabulary (e.g., *Policy Enforcement Module*, *Data Thief*, *DDIPE*, *English Calibration Gap*). Never use prohibited aliases.
2. **Respect Architectural Decisions**: Do not re-litigate decisions in `docs/adr/`.
3. **Minimize Token Consumption**:
   - Do **not** run unconstrained recursive directory traversals.
   - Do **not** ingest full raw dumps under `research/notes/raw/` unless explicitly instructed to parse raw evidence.
   - Target files directly using the sitemap above.
