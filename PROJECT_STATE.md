# PROJECT_STATE.md — MCP for Everyone

Last updated: 2026-08-09

## Status: Course Complete (13/13 chapters, 7/7 modules)

Live at https://technaom.github.io/mcp-for-everyone/. See "Next
Recommended Task" below for remaining polish work — none of it blocks
the course from being usable end to end today.

## Course Objective

Teach learners (beginner → architect) to build, secure, test, and
architect systems using the Model Context Protocol, following the
TechNaom master course-building philosophy (layered depth, story-first,
production-grade, interview-ready, original content only).

## Architecture Decisions

- **Spec baseline: MCP 2026-07-28** (finalized, stateless core), taught as
  primary/current. The prior stable spec (2025-11-25, stateful
  `initialize` handshake) is covered as "what you'll see in the wild" via
  callouts in Chapters 3, 6, 12 — not a parallel track. Rationale and
  alternatives considered are in the curriculum map and in the
  conversation that produced this repo (see git log for the scaffold
  commit message once committed).
- **Course size: 13 chapters** (focused-topic sizing per the TechNaom
  prompt's model — MCP is a focused emerging topic, not a foundation
  topic).
- **Repo structure mirrors `rag-for-everyone`/`genai-for-everyone`**:
  static site, `chapters/chapter-XX-slug/`, `docs/curriculum/`,
  `templates/`, `assessments/`, `quality-audits/`, `codebase/`. Shared
  front-end assets (`style.css`, `sidebar.js`, `progress.js`,
  `quiz-engine.js`) and templates (lesson/quiz/exercises/interview/project)
  were copied from `rag-for-everyone` and rebranded — structure only, no
  content reused.
- **Reference chapter: Chapter 4 ("Your First MCP Server")** — chosen as
  the first chapter to build to full production quality per the master
  prompt's Step 4, because it's concrete enough to validate the whole
  chapter template without needing Chapters 1–3 finished first.

## Completed

- [x] Step 1: Discovery (course vision, personas, prerequisites, outcomes,
      modules, chapters, projects, capstone, repo architecture,
      differentiators, risks, build order) — captured in the conversation
      and summarized in `docs/curriculum/CURRICULUM_MAP.md`.
- [x] MCP spec research against primary sources (modelcontextprotocol.io,
      official MCP blog) — confirmed 2026-07-28 is the finalized current
      spec as of 2026-08-09, previous stable was 2025-11-25.
- [x] Step 2: Curriculum map (`docs/curriculum/CURRICULUM_MAP.md`)
- [x] Step 3: Repository architecture scaffolded (directories, templates,
      shared assets copied/rebranded, README, this file, AI_HANDOFF.md)
- [x] Step 4: Chapter 4 ("Your First MCP Server") built to full
      production quality — lesson (hook through cheat sheet), quiz (6
      questions), 6 exercises (3 production-gear) with tested
      starter/solution code, 6-scenario practice bank, 8 interview
      questions across all 4 levels, and a mini project (bookmarks MCP
      server, JSON-persisted). All Python code was installed and
      executed against the real `mcp` SDK v2.0.0 in a scratch venv, not
      written from memory — this caught two real bugs before they shipped:
      (1) a missing type hint silently widens a tool's accepted input
      instead of erroring, now the chapter's Failure Lab; (2) a bare URL
      used as a templated resource parameter (`bookmark://{url}`) breaks
      MCP's own URI-template matching because of the `://` in the URL —
      fixed with percent-encoding, now a documented gotcha in the project.
- [x] Step 5: Validated Chapter 4 against quality gates
      (`quality-audits/chapter-04-audit.md`) — passed. In the process,
      revised `quality-audits/chapter-audit.template.md`'s volume bar
      down from RAG's numbers (8 exercises/10 scenarios/15 interview Qs)
      to this course's documented, focused-topic bar (6/6/8) — see the
      template's new preamble and `docs/course-architecture.md`.
- [x] Step 6 (Modules 1–2): Chapters 1–3 built to full production
      quality and validated (`quality-audits/chapter-0{1,2,3}-audit.md`
      — all pass). Chapters 1–2 are conceptual (no code labs, per the
      curriculum map) with written/diagram project artifacts instead of
      code. Chapter 3 (message lifecycle) required the same
      test-before-writing discipline as Chapter 4: every JSON-RPC
      message shape, the full modern/legacy compatibility matrix, and
      the `_meta` field table in the lesson were fetched directly from
      the official 2026-07-28 spec pages on modelcontextprotocol.io, not
      recalled from memory.
- [x] Step 6 (Module 3): Chapters 5–6 built and validated, completing
      Module 3. Chapter 5 (Resources & Prompts) found and documented a
      real SDK behavior: `list_resources()` and `list_resource_templates()`
      are separate calls, and a client checking only the former silently
      can't discover templated resources — this became the chapter's
      production scenario. Chapter 6 (Transports) found a bigger one:
      `mcp.run(transport="streamable-http", ...)`'s `stateless_http`
      parameter defaults to `False`, so a fresh Streamable HTTP server
      rejects unauthenticated raw requests with a 400 ("Missing session
      ID") even though the 2026-07-28 spec's headline feature is
      statelessness — found by inspecting the installed SDK's actual
      function signature and confirmed with live curl requests on two
      ports. Wrote `assessments/written-exams/module-3-exam.md`.
      All 6 live chapters' interview banks have 8 questions each.
- [x] Fixed a site-wide bug (reported by user, 2026-08-09): every
      chapter sidebar linked to `assessments/written-exams/module-N-exam.md`
      for all 7 modules, but those files didn't exist yet — 404 on every
      chapter page. Wrote real exams for Modules 1–2 (the modules with
      complete chapters at the time), set `examPath: null` for modules
      whose exams don't exist yet (now the enforced convention, see
      `assets/chapters-data.js`'s header comment), and backfilled
      Module 3's exam/examPath once Chapter 6 completed that module.
- [x] Fixed a latent robustness bug (found while building Chapter 5):
      Chapter 3's and Chapter 5's exercises/project files import Chapter
      4's `solution.py` via a `sys.path.insert` + `import solution`
      trick that only works when the importing file is run directly as
      `python solution.py` — both files share the name `solution.py`, so
      importing by name (`python -c "import solution"`, or a test runner)
      triggers a circular self-import instead. Replaced with
      `importlib.util.spec_from_file_location` everywhere this pattern
      is used, verified under both invocation styles.
- [x] Fixed two CSS bugs (reported by user, 2026-08-09), both live-site
      readability issues: (1) missing `color-scheme: light` allowed
      browser/OS dark-mode auto-inversion to mismatch card backgrounds
      against unchanged text color; (2) the global `p, li { color:
      var(--color-text) }` rule overrides inherited white text inside
      `.hook` (every chapter's opening callout), since a rule matching an
      element directly always beats an inherited value from an ancestor
      regardless of the ancestor's specificity — fixed with an explicit
      `.hook p, .hook li { color: inherit }` override. Also raised
      several translucent card backgrounds from ~60% to ~92% opacity so
      the colorful gradient backdrop doesn't wash out text contrast, and
      defined two classes (`.thinking-box`, `.lesson-card`) used in every
      chapter's HTML but never actually defined in `style.css` — a gap
      inherited unnoticed from `rag-for-everyone`'s template.

- [x] Step 6 (Module 4): Chapters 7–8 built and validated, completing
      Module 4. Chapter 7 built the course's first *host* (`ToyHost`) —
      keyword matching stands in for an LLM's decision step, explicitly
      labeled as a simplification; discovery/invocation/error-handling
      mechanics are real and tested. Chapter 8 reproduced, for real, the
      tool-name collision Chapter 2 promised: two live MCPServer
      instances both exposing `search` merged with a naive dict, and
      server A's tool silently vanished — confirmed by running it.
      Fixed with namespacing + routing. Wrote
      `assessments/written-exams/module-4-exam.md`.
- [x] Step 6 (Module 5): Chapters 9–10 built and validated, completing
      Module 5 — this course's stated core differentiator (security).
      Chapter 9 built a tested `require_scope` decorator enforcing least
      privilege, explicit about where it simplifies (identity
      verification via a contextvar, not real auth) vs. where it doesn't
      (the enforcement pattern, which matches the SDK's real
      `AuthSettings`/`authenticated_principal` shape). Chapter 10 built
      and ran a real prompt-injection scanner against benign/malicious/
      sneaky tool output, explicitly framed as one incomplete layer, not
      a solved problem. Wrote `assessments/written-exams/module-5-exam.md`.
      **Building Chapter 10's project surfaced a significant, general
      bug**: 8 prior chapters' exercises/project files called
      `asyncio.run(main())` unconditionally at module level, which
      crashes when the file is imported from inside an already-running
      event loop — exactly what a firewall-style wrapper does. Fixed
      with `if __name__ == "__main__":` guards across all 17 affected
      files (Chapters 3, 6, 7, 8, 9, 10), verified every affected
      chapter's solutions still run correctly afterward.

- [x] Step 6 (Module 6): Chapters 11–12 built and validated, completing
      Module 6. Chapter 11 formalized the ad hoc logging every prior
      chapter built as needed into structured, trace-correlated logging
      via the real `Context` API — and found a genuinely current fact by
      testing: `ctx.info()`/`ctx.log()` are deprecated as of the exact
      2026-07-28 spec this course teaches (SEP-2577), confirmed by a
      live deprecation warning. Chapter 12 tested (not just described)
      Chapter 3's compatibility matrix: connecting a real
      `mode="legacy"` client to a modern `MCPServer` succeeded via a
      genuine `initialize` handshake, proving every server in this
      course has been dual-era by default all along. Wrote
      `assessments/written-exams/module-6-exam.md`.
- [x] Step 10 (Module 7 capstone): Chapter 13 built and validated —
      Level 4 architecture challenge (design secure MCP infrastructure
      for a regulated healthcare enterprise), with a tested reference
      architecture combining namespacing/scoping/injection-scanning/
      logging from Chapters 8–11, honestly documented gaps rather than
      a fictional complete solution, a full ADR template, and
      architecture-scenario interview questions matching the master
      prompt's format. No written exam for Module 7 (capstone rubric
      instead, per the curriculum map).

**All 13 chapters across all 7 modules are now complete, tested, and
live.** Every chapter's code was installed and run against the real
`mcp` SDK v2.0.0 before being written into a lesson. A full regression
pass across every chapter's `exercises/solution.py` and
`project/solution.py` (run 2026-08-09, after Chapter 13) confirms no
tracebacks anywhere in the repo.

## Pending / Not Started (polish only — no core content remains)

- [x] Step 9 (mostly complete): Website shell live — root `index.html`,
      `docs/curriculum/index.html` styled roadmap, GitHub Pages deploy.
      Live at https://technaom.github.io/mcp-for-everyone/. Still
      pending: MCP-specific interactive assets (`message-flow.js`,
      `server-playground.js`, `permission-scoper.js`) mentioned in
      `docs/course-architecture.md` — optional polish, not required for
      the course to be complete and usable.
- [ ] Step 12: Further polish — automated link-checking CI (currently
      verified manually per chapter), a lint/test GitHub Actions
      workflow beyond the existing Pages-deploy-only workflow, a
      security scan pass.
- [ ] `CONTRIBUTING.md`, `CHANGELOG.md`, `.env.example`,
      `requirements.txt` at the repo root — not yet written.
      (`LICENSE`/`LICENSE-CONTENT` done, see Open Decisions.)
- [ ] `docs/production-and-capstone-projects.md` — a standalone version
      of the capstone rubric doc; the rubric currently lives inline in
      Chapter 13's lesson, which is sufficient but a standalone doc
      would match the original architecture plan.
- [ ] Optional: revisit chapter interview-bank counts for full
      uniformity — most chapters have 8, a couple could be reviewed for
      consistency on a future polish pass.

## Known Issues

- Chapters 3–4's forward references (to Chapters 6, 9, 12) are now all
  resolved — those chapters exist. The references are still plain text
  ("see Chapter 6"), not hyperlinks; converting them to real links is
  low-priority cosmetic polish, not a correctness issue.
- Chapters 3, 5, 6, 7, 8, 9, and 10 import Chapter 4's (or each other's)
  solution modules via `importlib.util.spec_from_file_location` — this
  is intentional (avoids duplicating server code repeatedly) but is a
  real coupling: if Chapter 4's `exercises/solution.py` or
  `project/solution.py` function signatures ever change, every chapter
  that imports it needs to be re-run. A 2026-08-09 full regression pass
  confirms all imports currently resolve correctly.
- Chapter 3's lesson worked-trace is labeled as "constructed from the
  spec's defined shapes," not a literal raw-byte packet capture — see
  Follow-Up Tasks in `quality-audits/chapter-03-audit.md`.
- Chapter 13's capstone is intentionally open-ended with no single
  correct answer — `quality-audits/chapter-13-audit.md` uses an adapted
  rubric rather than the standard per-chapter checklist for this reason.

## Open Decisions

- **License**: confirmed 2026-08-09 — MIT for code (`LICENSE`), CC BY 4.0
  for educational content (`LICENSE-CONTENT`), matching
  `python-for-everyone`'s MIT license and the master prompt's default.
- **GitHub org/publish target**: confirmed 2026-08-09 —
  `github.com/TechNaom/mcp-for-everyone`, public, `main` branch. Matches
  `TechNaom/rag-for-everyone`'s exact convention (checked via `gh repo
  view` before creating).
- Whether to backfill `PROJECT_STATE.md`/`AI_HANDOFF.md` into the four
  existing TechNaom repos (`python-for-everyone`, `genai-for-everyone`,
  `rag-for-everyone`, `devops-for-everyone`) that don't have them yet —
  raised by the user as a general standard, not yet actioned.

## Design Standards

See `docs/course-architecture.md` for the full standard (spec version
policy, production depth standard, conversational clarity standard,
builder thought-process layer). Chapter completion bar is defined and
now MCP-specific in `quality-audits/chapter-audit.template.md` (6
exercises/6 practice scenarios/8 interview questions minimum, with
priority on depth over count).

## Next Recommended Task

**The core course is done.** All 13 chapters, 6 module exams, and the
capstone are built, tested, and live. What's left is optional polish,
roughly in priority order:

1. **`CONTRIBUTING.md` and `CHANGELOG.md`** — the master prompt expects
   these at the repo root; neither exists yet. `CHANGELOG.md` should
   probably start from this build (2026-08-09) rather than try to
   reconstruct history.
2. **Automated CI beyond Pages deploy** — a GitHub Actions workflow that
   runs `python -m py_compile` across `chapters/**/*.py` and a basic
   HTML link-checker on every push, so the manual regression passes
   done throughout this build become automatic. This is the single
   highest-leverage remaining task, given how many real bugs manual
   testing caught — codifying that testing into CI protects it going
   forward.
3. **`docs/production-and-capstone-projects.md`** — pull Chapter 13's
   inline rubric into a standalone doc, matching the original
   architecture plan (optional; the inline version is complete and
   usable as-is).
4. **MCP-specific interactive assets** (`message-flow.js`,
   `server-playground.js`, `permission-scoper.js`) mentioned in
   `docs/course-architecture.md` — genuinely optional; the static
   lesson content doesn't need them to be complete.
5. **Cross-repo**: consider backfilling `PROJECT_STATE.md`/`AI_HANDOFF.md`
   into `python-for-everyone`, `genai-for-everyone`, `rag-for-everyone`,
   `devops-for-everyone` per the user's standing instruction (see
   `[[feedback-project-state-ai-handoff-files]]` in the assistant's
   memory system, if picking this up as a fresh session with memory
   access) — not started, out of scope for this repo alone.

If resuming this repo cold in a new session: run the regression check
from `AI_HANDOFF.md`'s "Current state" section before assuming anything
still works — SDK point releases could change behavior this course's
lessons depend on (the SDK is young and moves fast, per Chapter 6 and
12's own findings about default-behavior surprises).
