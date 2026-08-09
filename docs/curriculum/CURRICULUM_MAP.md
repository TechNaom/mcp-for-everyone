# MCP for Everyone — Curriculum Map

LAST_REVIEWED: 2026-08-09
Spec baseline: MCP specification **2026-07-28** (finalized, stateless core).
Prior stable spec referenced for compatibility: **2025-11-25** (stateful,
`initialize` handshake) — most deployed servers as of this writing still
speak this version; see the compatibility note in Module 2 and Module 6.

## Course Size

Focused emerging topic: 13 chapters, 4 projects (L1–L4), 1 capstone.
Depth over breadth — every chapter must clear the quality gates in
`quality-audits/chapter-audit.template.md` before it counts as done.

## Personas

- **Beginner** — never touched tool-calling or agents before.
- **Developer** — wants to ship a working MCP server/client.
- **Senior engineer** — needs production hardening, security, debugging.
- **Tech lead** — chooses build-vs-adopt, sets team conventions.
- **Architect** — designs multi-server, multi-tenant MCP platforms.

## Prerequisites

- Comfortable reading/writing Python (functions, classes, async basics).
- Understands JSON and basic HTTP concepts.
- Has a working mental model of "an LLM can call a tool" — if not, read
  `genai-for-everyone` session-4-2 (Function/Tool Calling) first. This
  course does not re-teach that.

## Learning Outcomes

By the end, a learner can:

1. Explain the integration problem MCP solves and why a protocol beats
   bespoke per-tool integrations.
2. Describe the host/client/server architecture and the stateless
   request/response model of the current spec.
3. Build an MCP server exposing tools, resources, and prompts.
4. Build a client/host that connects to one or more servers.
5. Choose the right transport (stdio vs. Streamable HTTP) for a given
   deployment.
6. Reason about permission scopes, sandboxing, and least privilege for
   tool access.
7. Recognize and defend against prompt injection via tool output and
   over-permissioned tools.
8. Test, debug, and observe an MCP server in production.
9. Version and harden a server against breaking changes and errors.
10. Design MCP infrastructure for a multi-team, regulated enterprise,
    including ADRs and a security model.

## Module Architecture

### Module 1 — Why MCP Exists
**Purpose:** motivate the protocol before naming it.
**Outcomes:** learner can explain the N×M integration problem and why
ad hoc function-calling doesn't scale across many tools/many models.
**Chapters:** 1
**Labs:** none (conceptual)
**Assessment:** concept quiz

### Module 2 — MCP Core Concepts
**Purpose:** the mental model: host, client, server, JSON-RPC, stateless
request/response, capability negotiation.
**Prerequisites:** Module 1
**Outcomes:** learner can diagram an MCP interaction end to end and name
the three primitives (tools, resources, prompts).
**Chapters:** 2, 3
**Labs:** trace a captured JSON-RPC exchange by hand
**Assessment:** concept quiz + diagram exercise

### Module 3 — Building MCP Servers
**Purpose:** hands-on server construction with the Python SDK.
**Prerequisites:** Module 2
**Outcomes:** learner ships a working server exposing all three
primitives over both standard transports.
**Chapters:** 4, 5, 6
**Labs:** filesystem tool server; resource-backed docs server; transport
swap exercise (stdio → Streamable HTTP)
**Assessment:** written check + working code review checklist

### Module 4 — Building Clients & Hosts
**Purpose:** the other half of the wire — connecting an agent to servers.
**Prerequisites:** Module 3
**Outcomes:** learner builds a host that talks to multiple servers and
merges their tool catalogs into one agent loop.
**Chapters:** 7, 8
**Labs:** multi-server host; tool-catalog conflict resolution exercise
**Assessment:** working code review checklist

### Module 5 — Security & Trust Boundaries
**Purpose:** MCP-specific security thinking — this is the course's core
differentiator.
**Prerequisites:** Module 4
**Outcomes:** learner can scope permissions, sandbox a server, and
detect/mitigate prompt injection carried in tool results.
**Chapters:** 9, 10
**Labs:** permission-scoping exercise; deliberately-vulnerable server the
learner must break, then fix
**Assessment:** security review written exam

### Module 6 — Production MCP
**Purpose:** what changes between a demo server and one that survives
production.
**Prerequisites:** Module 5
**Outcomes:** learner can test, observe, version, and harden a server;
knows the stateful/stateless compatibility story.
**Chapters:** 11, 12
**Labs:** add tracing/logging to a server; simulate a spec-version
mismatch and handle it gracefully
**Assessment:** production-readiness checklist exam

### Module 7 — Architecture & Capstone
**Purpose:** think like an architect, not just a builder.
**Prerequisites:** Module 6
**Outcomes:** learner produces a full architecture doc + ADRs for a
regulated-enterprise MCP platform.
**Chapters:** 13
**Labs:** none — this chapter is the capstone
**Assessment:** capstone rubric (architecture challenge, Level 4)

## Chapter Roadmap

| # | Chapter | Module | Difficulty |
|---|---------|--------|------------|
| 1 | The Integration Problem MCP Solves | 1 | Beginner |
| 2 | MCP Architecture: Hosts, Clients, Servers | 2 | Beginner |
| 3 | The MCP Message Lifecycle (stateless JSON-RPC) | 2 | Intermediate |
| 4 | Your First MCP Server (Tools) — **reference chapter** | 3 | Intermediate |
| 5 | Resources & Prompts | 3 | Intermediate |
| 6 | Transports: stdio vs. Streamable HTTP | 3 | Intermediate |
| 7 | Building an MCP Client/Host | 4 | Intermediate |
| 8 | Connecting Multiple Servers to One Agent | 4 | Advanced |
| 9 | Permissions, Scopes & Sandboxing | 5 | Advanced |
| 10 | Prompt Injection & Tool-Output Trust | 5 | Advanced |
| 11 | Testing, Debugging & Observability | 6 | Advanced |
| 12 | Versioning, Errors & Production Hardening | 6 | Advanced |
| 13 | Capstone: Enterprise MCP Platform Architecture | 7 | Architect |

## Projects

- **L1 Guided** — Local filesystem MCP server + CLI client (ships after
  Ch. 4).
- **L2 Assisted** — Internal-docs-search MCP server, partial scaffold
  provided, connects conceptually to `rag-for-everyone`'s retrieval work
  (ships after Ch. 6).
- **L3 Independent** — Multi-tool incident-runbook MCP server built from
  a written spec, no scaffold (ships after Ch. 10).
- **L4 Architecture Challenge** — Secure, multi-tenant MCP platform for a
  regulated enterprise; business problem only, learner produces the full
  architecture + ADRs (this is the capstone, Ch. 13).

## Capstone Requirements

See `docs/production-and-capstone-projects.md` (to be written alongside
Module 7) for the full rubric: problem statement, functional/non-functional
requirements, architecture, data flow, security model, evaluation strategy,
observability strategy, cost estimate, deployment strategy, failure
handling, testing, documentation, demo, ADRs.

## Interview Preparation

Every chapter ends with beginner/intermediate/senior/architect interview
questions. Architecture-level scenarios (design secure enterprise MCP
infra, design a multi-tenant MCP gateway) live in
`assessments/architecture-challenges/`.

## Cross-Course Links

- Builds on: `genai-for-everyone` (tool calling, agents intro)
- Feeds: `AI Coding Agents for Everyone` (planned), `AI Security for
  Everyone` (planned — deepens Module 5 content)
