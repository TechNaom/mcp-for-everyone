# PROJECT_STATE.md — MCP for Everyone

Last updated: 2026-08-09

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

## Pending / Not Started

- [ ] Step 6 continued: build Chapters 7–13 (Modules 4–7), module by
      module, validating after each module.
- [ ] Step 7: Build project implementations (L1–L4) and tests.
- [ ] Step 8: Assessments — quizzes, written exams, interview questions,
      architecture challenges (beyond what ships per-chapter).
- [x] Step 9 (partial): Website shell live — root `index.html`,
      `docs/curriculum/index.html` styled roadmap, GitHub Pages deploy
      (`.github/workflows/pages.yml`, copied from `rag-for-everyone`
      unmodified). Live at https://technaom.github.io/mcp-for-everyone/.
      Still pending: MCP-specific interactive assets
      (`message-flow.js`, `server-playground.js`, `permission-scoper.js`)
      mentioned in `docs/course-architecture.md` — deferred until more
      chapters exist to justify them.
- [ ] Step 10: Capstone (Chapter 13 content + rubric doc).
- [ ] Step 11: Interview layer polish across all chapters.
- [ ] Step 12: Polish — tests, link validation, security scan, curriculum
      consistency review, CI beyond Pages deploy (lint/test workflows).
- [ ] `CONTRIBUTING.md`, `CHANGELOG.md`, `.env.example`,
      `requirements.txt` — not yet written. (`LICENSE`/`LICENSE-CONTENT`
      done, see Open Decisions.)
- [ ] `docs/production-and-capstone-projects.md` — capstone rubric detail.

## Known Issues

- Chapters 3–4 reference forward to Chapters 6, 9, and 12, which don't
  exist yet — links are plain text ("see Chapter 6"), not hyperlinks, so
  nothing is broken, but re-verify the claims once those chapters are
  written.
- Chapter 3's exercises/project import Chapter 4's solution server via a
  relative `sys.path` hack (`parents[2] / "chapter-04-.../exercises"`).
  This is intentional (avoids duplicating the notes server a third time)
  but it's a real coupling: if Chapter 4's `exercises/solution.py` moves
  or its function signatures change, Chapter 3's code breaks silently
  until someone runs it. Re-run Chapter 3's exercises/project any time
  Chapter 4's exercises/solution.py changes.
- Chapter 3's lesson worked-trace is labeled as "constructed from the
  spec's defined shapes," not a literal raw-byte packet capture — see
  Follow-Up Tasks in `quality-audits/chapter-03-audit.md`.

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

Module 4 (Chapters 7–8): "Building an MCP Client/Host" and "Connecting
Multiple Servers to One Agent." Chapter 7 should build an actual host
loop — connect a client to a server, list tools, and drive a (mocked or
simple rule-based) decision about which tool to call, since no prior
chapter has built the *host* side, only servers and raw clients. Chapter
8 needs at least two live servers connected simultaneously from one
host process, with a real tool-name collision to resolve (per Chapter
2's Q3/Q7 interview questions, which already promised this would be
covered). Test everything against the real SDK before writing it into a
lesson, same discipline as every chapter so far. Validate each with a
fresh `quality-audits/chapter-0N-audit.md`, write the Module 4 exam once
both chapters are done, before moving to Module 5 (security — this
course's stated differentiator).
