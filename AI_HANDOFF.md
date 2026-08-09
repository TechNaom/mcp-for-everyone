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

## Current state (as of 2026-08-09): COURSE COMPLETE

**All 13 chapters across all 7 modules are built, tested, and live** at
https://technaom.github.io/mcp-for-everyone/. Only optional polish
remains (CI, CONTRIBUTING.md, etc. — see PROJECT_STATE.md's "Next
Recommended Task"). **Read `PROJECT_STATE.md` for the authoritative,
up-to-date status** — this file won't be as fresh as that one. What
exists:

- Directory skeleton (`chapters/`, `docs/`, `templates/`, `assessments/`,
  `codebase/`, `assets/`, `quality-audits/`, `scripts/`, `.github/workflows/`)
- `docs/curriculum/CURRICULUM_MAP.md` — the source-of-truth roadmap
- `docs/course-architecture.md` — structural + spec-version policy
- `README.md`, this file, `PROJECT_STATE.md`
- `templates/` and `assets/{style.css,sidebar.js,progress.js,quiz-engine.js,chapters-data.js}`
  copied from `rag-for-everyone` and rebranded (structure only), plus the
  full 13-chapter roster wired into `chapters-data.js` for sidebar nav
- **Chapters 1–10 (Modules 1–5) are fully built and validated** — same
  page set each: `lesson.html`, `quiz.html`, `interview-questions.html`,
  `exercises/{index.html,starter.py,solution.py or reasoning tasks}`,
  `practice/index.html`, `project/{index.html,...}`. Every Python example
  was installed and run against the real `mcp` SDK v2.0.0 before being
  written into a lesson — do not add new code examples to this course
  from memory; install `mcp[cli]` in a scratch venv and run them first.
  This discipline has caught real, non-obvious SDK/behavior issues
  repeatedly: Chapter 4's silent type-widening and URI-template `://`
  collision; Chapter 3's wrong assumption that calling a nonexistent
  tool raises a Python exception (it doesn't); Chapter 5's
  `list_resources()` vs. `list_resource_templates()` split; Chapter 6's
  `stateless_http` defaulting to `False` even under the "stateless"
  spec; Chapter 8's real, reproduced tool-name collision across two live
  servers; **Chapter 10's discovery that 8 prior chapters' files called
  `asyncio.run(main())` unguarded at module level, which crashes when
  imported from inside a running event loop** — fixed with
  `if __name__ == "__main__":` guards across 17 files spanning Chapters
  3, 6, 7, 8, 9, 10. Chapters 1–2 are conceptual (no code, per the
  curriculum map) with written-memo/diagram projects instead. Chapters
  3, 5, 6, 7, 8, 9, and 10 reuse Chapter 4's `solution.py` (and
  sometimes each other's) via `importlib.util.spec_from_file_location`
  (NOT a `sys.path` + `import solution` trick — that broke depending on
  invocation method since multiple files share the name `solution.py`;
  see any `_load_chapter_4_module()`-style docstring for why). **Any new
  file that imports another chapter's module MUST end with
  `if __name__ == "__main__": asyncio.run(main())`, never a bare
  top-level `asyncio.run(main())`** — this is now a hard rule for this
  repo, not a style preference. If you ever change Chapter 4's
  `exercises/solution.py` or `project/solution.py` function signatures,
  re-run every chapter that imports it. Chapter 9's `require_scope`
  decorator sets a `_required_scope` marker attribute specifically so
  Chapter 9's audit-tool project can introspect it — don't remove that
  marker line if editing `require_scope`. Chapters 11–13 continue the
  same pattern: Chapter 11 formalizes structured, trace-correlated
  logging via the real `Context` API and documents that
  `ctx.info()`/`ctx.log()` are deprecated as of this exact spec version
  (SEP-2577) — confirmed by a live warning, not assumed. Chapter 12
  proves (not just describes) that the SDK's `MCPServer` is dual-era by
  default: `Client(mcp, mode="legacy")` completes a real `initialize`
  handshake successfully against every server in this course. Chapter
  13 (the capstone) ships a tested reference architecture combining
  namespacing/scoping/injection-scanning/logging across two servers,
  with honestly documented gaps — `solution.py` there closes one gap as
  a worked example, explicitly not "the" correct capstone answer, since
  it's an open architecture challenge. Audits:
  `quality-audits/chapter-0{1..9}-audit.md`, `chapter-1{0,1,2,3}-audit.md`.
- **Root website is live**: `index.html`, `docs/curriculum/index.html`
  (styled roadmap), deployed via `.github/workflows/pages.yml` to
  https://technaom.github.io/mcp-for-everyone/. `assets/chapters-data.js`
  is the single source of truth for what's "live" — a chapter needs a
  `path` field to render as a link; a module needs a real `examPath` to
  link its written exam. Omitting either renders as non-linked/hidden
  rather than a link to a 404 — **this exact mistake shipped once**
  (all 7 modules linked to exam files that didn't exist) and was reported
  by the user as a live bug; don't repeat it for chapters or exams.
- **CSS**: `color-scheme: light` is declared in `:root` — don't remove
  it, it prevents browser/OS dark-mode auto-inversion from breaking card
  contrast. The global `p, li { color: var(--color-text) }` rule beats
  inherited text color from any dark-background ancestor (like `.hook`)
  — any new dark callout box that contains `<p>`/`<li>` needs its own
  `.your-class p, .your-class li { color: inherit }` override, following
  `.hook`'s pattern in `style.css`.

All 13 chapters exist. A full regression pass across every chapter's
`exercises/solution.py` and `project/solution.py` (2026-08-09, after
Chapter 13 shipped) confirms no tracebacks anywhere in the repo.

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
- Don't mass-generate remaining chapters ahead of validation — build one
  module at a time, run a `quality-audits/chapter-0N-audit.md` for each,
  same as Chapters 1–4. That's the explicit build order in
  `PROJECT_STATE.md`.
- Don't add a `path` to a chapter in `assets/chapters-data.js` until that
  chapter's `lesson.html` actually exists — sidebar.js and home.js treat
  `path` presence as "live," so a premature path 404s.
- Don't copy lesson content, examples, or project stories from other
  TechNaom repos — structure/templates only.

## Current task

None — the course is complete. If you were pointed here to "continue
building," check with the user before assuming there's more content
work to do; there isn't, by design. See PROJECT_STATE.md's "Next
Recommended Task" for the remaining optional polish items (CI,
CONTRIBUTING.md, etc.) if that's what's actually being asked for.

## Next task after that

N/A unless the user requests new content (e.g., expanding beyond 13
chapters, which would be a deliberate scope-change decision to make
explicitly, not a default next step) or polish work from
PROJECT_STATE.md.

## Important architectural decisions (see PROJECT_STATE.md for full detail)

1. MCP spec 2026-07-28 (stateless) is the taught baseline.
2. 13 chapters, focused-topic sizing — the course is complete at this
   size; don't expand without a strong, explicit reason from the user.
3. Static site, no backend required for the default learning path.
4. Repo structure mirrors existing TechNaom course repos exactly.
5. Every code example in every chapter was run against the real `mcp`
   SDK before being written into a lesson — this is the single most
   load-bearing practice in this repo and caught real bugs repeatedly
   (see "Current state" above for the full list). Do not relax this for
   future edits, however small they seem.
