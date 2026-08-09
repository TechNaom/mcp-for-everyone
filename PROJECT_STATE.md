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

## Pending / Not Started

- [ ] Step 6: Build remaining 12 chapters, module by module, validating
      after each module.
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

- Chapter 4 references forward to Chapters 6, 9, and 12, which don't
  exist yet — links are plain text ("see Chapter 6"), not hyperlinks, so
  nothing is broken, but re-verify the claims once those chapters are
  written.
- No root `index.html` yet, so Chapter 4 isn't reachable by navigating
  the site — only by opening its files directly. Sidebar/progress/quiz
  JS is wired and will work once `index.html` exists (Step 9).

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

Start Step 6: build Chapters 1–3 (Module 1–2, "Why MCP Exists" and "MCP
Core Concepts") using Chapter 4 as the template reference — see
`chapters/chapter-04-your-first-mcp-server/` for the full page set
(lesson/quiz/exercises/practice/interview/project) and
`quality-audits/chapter-04-audit.md` for the bar to hit. Validate each
chapter with a fresh `quality-audits/chapter-0N-audit.md` before moving
to the next. Chapters 1–2 are conceptual (no code labs required per the
curriculum map); Chapter 3 will need the same "test code against the
real SDK before writing it into the lesson" discipline used in Chapter 4,
since it covers the stateless JSON-RPC message lifecycle directly.
