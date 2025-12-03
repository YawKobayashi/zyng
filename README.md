# Zyng

> A tiny timeline-first language for LLM workflows and logs.  
> Write prompts, workflows, and logs as one coherent text with time metadata.

---

## Overview

Zyng is a small experimental language for describing:

- prompts
- LLM workflows
- settings
- logs
- light tests

in **one text format**, instead of spreading them across Markdown, YAML, JSON, and ad-hoc scripts.

The core ideas are:

- **timeline-first**  
  “When did this happen?” is a first-class concept.  
  Zyng exposes time metadata such as `:::now`, `:::yest`, `:::tomo`, `:::at:"..."` directly in the language.
- **human-readable, model-friendly**  
  For humans, Zyng looks like slightly odd but readable English.  
  For LLMs, it is a semi-structured text that can be parsed or used as training / prompt material.

This repository currently contains a **very early pre-release (v0.0.1)**:

- a minimal runner
- a tiny core syntax around `show`
- the ability to run ```zyng blocks inside Markdown files

---

## What problem is Zyng trying to solve?

LLM projects often suffer from:

- README / docs drifting away from the actual prompts and code
- Human-facing logic scattered across:
  - Markdown
  - YAML / JSON
  - Python scripts
  - comments
- Logs that are hard to reuse:
  - we don’t know **when** a run happened
  - which **model / policy** was used
  - what the **intended use** of that text was (log? training? test? policy?)

Zyng aims to address this by:

- making **time** a first-class, explicit concept, and
- eventually exposing **role / kind / use** metadata at the text level,

so that LLM workflows and logs can be written as **reproducible, readable timelines**.

---

## Status

- Version: `0.0.1`
- Stability: **experimental / pre-release**
- Implemented in v0.0.1:
  - Python package `zyng`
  - A minimal runner: run ```zyng fenced code blocks inside Markdown
  - `show "..."` with simple metadata after `:::`
  - Basic handling of:
    - `:::now`
    - `:::yest`
    - `:::tomo`
    - `:::at:"2025-12-03T21:00:00+09:00"`

Example output (from `timetst.md`):

```text
[now] Now message
[yest] Yesterday message
[tomo] Tomorrow message
[at:"2025-12-03T21:00:00+09:00"] Exact time
```

At this stage, Zyng is best considered a **design sketch with a working minimal runner**.

---

## Installation

Zyng is published on PyPI.

```bash
pip install zyng==0.0.1
```

You can verify the installation with:

```bash
pip show zyng
```

---

## Minimal usage

Create a Markdown file, for example `timetst.md`:

```markdown
# Zyng time test

This is a minimal example of Zyng code inside a fenced block.

```zyng
show "Now message" :::now
show "Yesterday message" :::yest
show "Tomorrow message" :::tomo
show "Exact time" :::at:"2025-12-03T21:00:00+09:00"
```
```

Then run:

```bash
python -m zyng.runner timetst.md
```

The runner will:

1. Find ```zyng fenced blocks in the Markdown file
2. Parse each line
3. Execute `show` commands and print them with their metadata prefix

Current semantics (v0.0.1):

- `show "Message" :::now`  
  → prints `[now] Message`
- `show "Message" :::yest`  
  → prints `[yest] Message`
- `show "Message" :::tomo`  
  → prints `[tomo] Message`
- `show "Message" :::at:"2025-12-03T21:00:00+09:00"`  
  → prints `[at:"2025-12-03T21:00:00+09:00"] Message`

The metadata is not yet interpreted as real datetime objects; it is exposed as a readable, structured prefix.

---

## Core design ideas

Zyng’s long-term design revolves around four kinds of metadata:

- **time** – when is this about?
  - `now`, `yest`, `tomo`, `:::at:"..."`
- **role** – whose perspective is this?
  - e.g. `:::role:"self"`, `:::role:"planner-ai"` (future)
- **kind** – what type of statement is this?
  - e.g. `fact`, `feeling`, `plan`, `policy` (future)
- **use** – what will this line be used for?
  - e.g. `log`, `train`, `test`, `policy` (future)

In v0.0.1, only **time** is surfaced in the runner.  
`role`, `kind`, and `use` are still at the design level and may change.

The goal is to make it natural to write lines like:

```zyng
show "User asked about travel to Osaka." :::now :::role:"user" :::kind:"fact" :::use:"log"
```

and have both humans and models benefit from the explicit metadata.

---

## Roadmap (very early draft)

This is a rough, evolving plan.

### v0.0.x – Minimal runner (current)

- [x] Python package `zyng` on PyPI
- [x] Run ```zyng fenced blocks inside Markdown
- [x] Implement `show` with simple metadata prefix
- [x] Handle `now`, `yest`, `tomo`, `at:"..."` as raw time metadata

### v0.1 – README runner / Core language

- Stabilize the Core syntax for:
  - `show`
  - `read`
  - `write`
  - `use`
  - `let`
- Document the core in `docs/zyng_core_v0.1.md`
- Make project READMEs executable as Zyng scripts in a more robust way

### v0.2 – Importable by others

- Provide 2–3 sample projects:
  - logging / diary style
  - a small LLM workflow (even with dummy calls)
- Write a guide:  
  **“How to adopt Zyng in your own project”**
- Provide example mappings from Zyng to:
  - Python dicts
  - OpenAI / Claude / Gemini API calls
- Start treating Core spec as mostly backward-compatible

---

## Author

- Design & Implementation: **Yo Kobayashi**  
  - Contact: **yaw.kobayashi@proton.me**

Zyng is an experimental personal project exploring timeline-first, metadata-rich text for LLM workflows.  
If you build something inspired by Zyng, adding a note or link back here would be very welcome.

---

## License

Zyng is currently released under the **MIT License**.  
(If this changes in the future, this section will be updated.)
