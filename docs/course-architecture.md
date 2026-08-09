# MCP for Everyone — Course Architecture

## Reference Pattern

Reference implementations for structure (not content): `TechNaom/python-for-everyone`
and `TechNaom/rag-for-everyone`. Reuse their proven learner-journey pattern:

- Root `index.html` as the GitHub Pages entry point.
- Shared `assets/` for design, sidebar, progress, quizzes.
- `docs/curriculum/CURRICULUM_MAP.md` as the readable source roadmap.
- `docs/curriculum/index.html` as the styled roadmap (built in the website
  phase, Step 9).
- `chapters/chapter-XX-topic/` for each chapter: lesson, quiz, exercises,
  practice bank, interview prep, project link.
- Written exams at module boundaries.
- Progress stored in browser local storage. No backend for the default
  learning path.

Do not reuse RAG/GenAI/Python course lesson content, examples, or project
stories. All MCP examples, server code, labs, and interview answers must be
original to this course.

## MCP-Specific Additions

Built on the same static stack, as `assets/` extensions:

- `message-flow.js` — animates a JSON-RPC request/response exchange
  (stateless, single round trip) so learners see the wire format without
  running a server.
- `server-playground.js` — lets a learner poke at a mock MCP server's
  `tools/list` and `tools/call` responses in-browser.
- `permission-scoper.js` — interactive exercise for Module 5: assign
  scopes to a tool catalog and see what an over-permissioned agent could
  do.

The course must work as static files first. Any live-backend lab (e.g. a
real running MCP server a learner connects to) is a stretch goal, not a
requirement for release.

## Spec Version Policy

This course teaches the MCP specification **2026-07-28** (stateless core)
as current. Because most servers in the wild as of this writing were built
against the prior stable spec (**2025-11-25**, stateful `initialize`
handshake), every chapter that touches the wire protocol (3, 6, 12) must
include a short "what you'll see in older servers" callout — not a full
parallel curriculum. Update `CHANGELOG.md` and `LAST_REVIEWED` in
`CURRICULUM_MAP.md` whenever the spec changes meaningfully.

## Production Depth Standard

Same bar as `rag-for-everyone`:

- At least 8–10 meaningful examples/checks per core-concept chapter (MCP's
  scope is narrower than RAG's, so this is a slightly lower floor than
  RAG's 10+, but never token "what is X" filler).
- Practice banks grounded in real security, reliability, cost, and
  operational scenarios.
- Explicit failure modes and what to inspect first.
- Trade-offs a senior engineer or architect would care about.

## Conversational Clarity Standard

Same as `rag-for-everyone`: explain like a helpful expert beside the
learner, introduce jargon only when needed, use stories before syntax,
keep senior-level trade-offs but unpack them patiently.

## Builder Thought-Process Layer

Every chapter includes a visible reasoning section (not hidden
chain-of-thought) covering: problem framing, approach options, chosen
approach, validation, observed failure, improvement, final decision — the
same "engineering decision journal" habit as other TechNaom courses,
adapted to MCP-building decisions (which transport, how to scope a
permission, how to structure a tool schema).
