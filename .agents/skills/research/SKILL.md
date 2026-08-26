---
name: research
description: Investigate a question against high-trust primary sources and capture the findings as a Markdown file in the repo. Use when the user wants a topic researched, docs or API facts gathered, or reading legwork delegated to a background agent.
---

Spin up a **background agent** to do the research, so you keep working while it reads.

Its job:

1. **Check the local corpus first.** This repo's primary sources live on disk: PDFs under `papers/` (`papers/AgenticJailbreaking/`, `papers/RAGJailbreaking/`, etc). If the question concerns a paper or the benchmark, read the actual local file directly — don't search the web for a summary of a paper that's already sitting in this repo. Only search the web for sources not present locally (work these papers cite but that isn't downloaded, or anything published after them).
2. Investigate the question against **primary sources** (the local corpus above, or — when nothing local covers it — official docs, source code, specs, first-party APIs), not a secondary write-up of them. Follow every claim back to the source that owns it.
3. Write the findings to a single Markdown file, citing each claim's source. For local papers, cite section or page, not just the filename.
4. Save it to `research/notes/`, following the `<cluster>/<paper-id>.md` convention (e.g. `research/notes/agentic-jailbreaking/2410.02644v4.md`). If a note for that source already exists, update it rather than duplicating.