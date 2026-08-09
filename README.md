# MCP for Everyone

Free, interactive Model Context Protocol course and build-in-public
engineering track: visual lessons, working server/client labs, security
exercises, evaluation practice, interview prep, and portfolio projects.

🔗 **Repo:** <https://github.com/TechNaom/mcp-for-everyone>
🔗 **Live UI:** <https://technaom.github.io/mcp-for-everyone/>
*(GitHub Pages not yet enabled — no root `index.html` yet, see `PROJECT_STATE.md`)*

This course follows the same philosophy as `python-for-everyone` and
`rag-for-everyone`:

- Plain-language first, without hiding the real engineering.
- One chapter at a time, validated before scaling.
- No signup required.
- Browser-first learning pages.
- Hands-on code and projects.
- Interview-ready explanations.
- Strong architecture and trade-off thinking.

All examples, stories, exercises, projects, and thought-process journals in
this course are original to MCP server/client development, protocol
security, and production AI tool integration.

## What this is

`MCP for Everyone` teaches learners to safely and correctly connect AI
systems to real tools, data, and services using the Model Context Protocol
— the standard that replaces bespoke, one-off tool integrations with a
common client/server contract.

## Spec version

This course teaches **MCP specification 2026-07-28** (the current,
finalized, stateless-core spec) as primary, with explicit callouts where
learners will encounter the older stateful **2025-11-25** spec in existing
servers. See `docs/course-architecture.md` for the full policy and
`CHANGELOG.md` for revision history.

## Who this is for

- **Beginners** who've never built a tool-using AI system.
- **Developers** who want to ship a working MCP server or client.
- **Senior engineers** who need production hardening and security depth.
- **Tech leads** choosing build-vs-adopt for MCP servers.
- **Architects** designing multi-server, multi-tenant MCP platforms.

## Learning path

See [`docs/curriculum/CURRICULUM_MAP.md`](docs/curriculum/CURRICULUM_MAP.md)
for the full module/chapter roadmap, learning outcomes, and project ladder.

## Repository structure

```text
mcp-for-everyone/
  chapters/            per-chapter lessons, quizzes, labs, interview prep
  docs/curriculum/      curriculum map (source of truth) + styled roadmap
  docs/course-architecture.md
  templates/            reusable chapter/quiz/lab/project templates
  assessments/          quizzes, written exams, interview questions, ADR-style
                         architecture challenges
  quality-audits/       per-chapter quality gate checklists
  codebase/              starters, solutions, shared code, datasets
  assets/                shared site styling, sidebar, progress, quiz engine
  PROJECT_STATE.md       current build status (read this first)
  AI_HANDOFF.md          for any AI coding assistant picking this up cold
```

## How to start

This repo is under active construction. See `PROJECT_STATE.md` for what's
built and what's next.

## Projects

Four project levels, from guided to architecture-challenge — see the
curriculum map's Projects section.

## Capstone

Enterprise MCP platform: multiple servers behind a gateway, per-team
permission model, audit logging, tool-call accuracy evaluation, full ADR
set, deployment plan. Details in `docs/production-and-capstone-projects.md`
(written alongside Module 7).

## License

Code is licensed under [MIT](LICENSE). Educational content (lessons,
diagrams, exercises, interview questions) is licensed under
[CC BY 4.0](LICENSE-CONTENT).
