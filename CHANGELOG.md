# Changelog

Dates are when work was completed, not necessarily pushed. This log
starts from the course's initial build — earlier history doesn't exist
(this is a new repo).

## 2026-08-09 — Course complete: all 13 chapters, 7 modules

- Repo scaffolded: curriculum map, repo architecture, templates, shared
  assets (rebranded from `rag-for-everyone`), `PROJECT_STATE.md`,
  `AI_HANDOFF.md`, `LICENSE` (MIT), `LICENSE-CONTENT` (CC BY 4.0).
- Chapter 4 ("Your First MCP Server") built as the reference chapter,
  validated against a course-specific quality bar (6 exercises / 6
  practice scenarios / 8 interview questions minimum).
- Chapters 1–3 (Modules 1–2): the integration problem MCP solves,
  host/client/server architecture, the stateless message lifecycle —
  the latter grounded directly in the official 2026-07-28 specification
  fetched from modelcontextprotocol.io.
- Chapters 5–6 (Module 3): resources & prompts, transports. Found and
  documented two real SDK behaviors: `list_resources()` vs.
  `list_resource_templates()` are separate discovery calls, and
  `stateless_http` defaults to `False` even under the "stateless" spec.
- Chapters 7–8 (Module 4): building a host (`ToyHost`), connecting
  multiple servers. Reproduced a real tool-name collision across two
  live servers and fixed it with namespacing.
- Chapters 9–10 (Module 5, the security differentiator): permission
  scoping (`require_scope`), prompt-injection defense (tested scanner,
  explicitly framed as one incomplete layer, not a solved problem).
  Found and fixed a course-wide bug: 17 files across 6 chapters called
  `asyncio.run(main())` unguarded at module level, crashing when
  imported from inside a running event loop.
- Chapters 11–12 (Module 6): structured observability via the real
  `Context` API (and the discovery that `ctx.info()`/`ctx.log()` are
  deprecated as of this exact spec version, SEP-2577); real, tested
  proof the SDK serves both modern and legacy protocol eras
  simultaneously by default.
- Chapter 13 (Module 7, capstone): a Level 4 architecture challenge —
  secure MCP infrastructure for a regulated healthcare enterprise, with
  a tested reference architecture, ADR template, and architecture-
  scenario interview questions.
- Website: root `index.html`, styled roadmap
  (`docs/curriculum/index.html`), GitHub Pages deploy.
- Live-site bug fixes (both user-reported): dangling module-exam links
  (all 7 modules linked to files that didn't exist); two CSS
  readability issues (missing `color-scheme: light` letting browser
  dark-mode auto-invert card contrast, and a global `p, li` color rule
  overriding the `.hook` callout's white text).
- Discipline maintained throughout: every code example in every chapter
  was installed and run against the real `mcp` SDK v2.0.0 before being
  written into a lesson, not written from memory.
- Polish: CI workflow (`ci.yml`) covering structure, placeholder-text,
  full solution.py execution, JS/chapter-path validation, and secret
  scanning; `scripts/local_check.sh` mirroring it for local use;
  `CONTRIBUTING.md`.
