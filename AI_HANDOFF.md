# AI_HANDOFF.md — MCP for Everyone

Read this before touching anything in this repo. It's written so any AI
coding assistant (ChatGPT, Copilot, Codex, a different Claude session,
etc.) can pick this up cold, with zero prior context, and not redesign
decisions that were already made.

## What this repository is

An open-source, free technical course teaching the Model Context Protocol
(MCP), part of the **TechNaom "for Everyone"** course ecosystem
(`technaom.github.io`). It follows a very detailed master course-building
prompt (not stored in this repo — it lives in the maintainer's Claude
memory/conversation history) whose core rules are summarized in
`docs/course-architecture.md`. If you need the full philosophy, ask the
maintainer for "the TechNaom master prompt" rather than guessing.

## Design philosophy (non-negotiable)

- Every concept progresses WHY → WHAT → HOW → BUILD → BREAK → DEBUG →
  EVALUATE → SECURE → OPTIMIZE → SCALE → ARCHITECT. Never teach syntax
  before the problem it solves.
- Same content serves 5 personas (beginner/developer/senior/tech
  lead/architect) via layered depth, not separate tracks.
- Story-first: every major concept opens with a relatable problem before
  naming the technology.
- No shallow "collection of tutorials." Every chapter needs real depth:
  failure modes, trade-offs, security, cost, scale, interview prep.
- Quality over chapter count. This course is scoped to 13 chapters
  deliberately — do not pad it to hit a round number.
- All content (examples, server code, stories, exercises, interview
  answers) must be original. Other TechNaom repos are structural
  references only, never content sources.

## Current state (as of 2026-08-09)

**Read `PROJECT_STATE.md` for the authoritative, up-to-date status** —
this file won't be as fresh as that one. What exists:

- Directory skeleton (`chapters/`, `docs/`, `templates/`, `assessments/`,
  `codebase/`, `assets/`, `quality-audits/`, `scripts/`, `.github/workflows/`)
- `docs/curriculum/CURRICULUM_MAP.md` — the source-of-truth roadmap
- `docs/course-architecture.md` — structural + spec-version policy
- `README.md`, this file, `PROJECT_STATE.md`
- `templates/` and `assets/{style.css,sidebar.js,progress.js,quiz-engine.js,chapters-data.js}`
  copied from `rag-for-everyone` and rebranded (structure only), plus the
  full 13-chapter roster wired into `chapters-data.js` for sidebar nav
- **Chapter 4 ("Your First MCP Server") is fully built and validated** —
  the reference chapter: `chapters/chapter-04-your-first-mcp-server/`
  contains `lesson.html`, `quiz.html`, `interview-questions.html`,
  `exercises/{index.html,starter.py,solution.py}`,
  `practice/index.html`, `project/{index.html,starter.py,solution.py}`.
  Every Python example in it was installed and run against the real
  `mcp` SDK v2.0.0 before being written into the lesson — do not add new
  code examples to this course from memory; install `mcp[cli]` in a
  scratch venv and run them first, the same way this chapter's two real
  bugs (silent type-widening, URI-template `://` collision) were caught.
  Audit: `quality-audits/chapter-04-audit.md`.

Chapters 1–3 and 5–13 don't exist yet. No website
(`index.html` at root doesn't exist yet — that's Step 9, deliberately
deferred until content modules are built).

## Naming conventions

- Chapter folders: `chapters/chapter-NN-kebab-slug/` (two-digit, zero
  padded), matching `rag-for-everyone`'s convention (not
  `genai-for-everyone`'s `session-W-D-slug` convention — this course uses
  the RAG course's numbering style since it's not week/day structured).
- Repo name: `mcp-for-everyone`, GitHub org assumed `technaom` (not yet
  confirmed/created).

## What NOT to change

- Don't restructure the repo layout without checking `docs/course-architecture.md`
  first — it deliberately mirrors `rag-for-everyone`/`genai-for-everyone`
  for ecosystem consistency.
- Don't teach only the old stateful MCP spec (2025-11-25) as primary, and
  don't build a fully parallel "old vs new spec" curriculum either. The
  decision (documented in `PROJECT_STATE.md` and `docs/course-architecture.md`)
  is: teach 2026-07-28 (stateless) as current, with targeted callouts
  about the older stateful model in Chapters 3, 6, and 12 only.
  If the spec changes again, re-verify against modelcontextprotocol.io
  primary sources before touching chapter content — do not assume prior
  knowledge is current, MCP moves fast.
- Don't mass-generate all 13 chapters before Chapter 4 (the reference
  chapter) has been built and validated against the quality gates. That's
  the explicit build order in `PROJECT_STATE.md`.
- Don't copy lesson content, examples, or project stories from other
  TechNaom repos — structure/templates only.

## Current task

Chapter 4 is done and validated (see above). Next: build Chapters 1–3
(Modules 1–2) using Chapter 4's page set as the template, then validate
each with its own `quality-audits/chapter-0N-audit.md` before moving on
— see "Next Recommended Task" in `PROJECT_STATE.md`.

## Next task after that

Continue Module 3 (Chapters 5–6), then Module 4 (7–8), following the
curriculum map's build order — one module at a time, validated after
each, per the master workflow. Don't mass-generate ahead of validation.

## Important architectural decisions (see PROJECT_STATE.md for full detail)

1. MCP spec 2026-07-28 (stateless) is the taught baseline.
2. 13 chapters, focused-topic sizing — do not expand without a strong
   reason.
3. Static site, no backend required for the default learning path.
4. Repo structure mirrors existing TechNaom course repos exactly.
