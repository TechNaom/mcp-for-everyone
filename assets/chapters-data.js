/*
  Single source of truth for the MCP for Everyone chapter roster.
  Mirrors the rag-for-everyone / python-for-everyone pattern: sidebar.js
  renders navigation from this file, and roadmap pages are kept in sync
  with it. Only Chapter 4 has content today — see PROJECT_STATE.md.
*/

window.MFE_MODULES = [
  {
    title: "Module 1 — Why MCP Exists",
    summary: "Motivate the protocol before naming it: the N x M integration problem.",
    examPath: "assessments/written-exams/module-1-exam.md",
    chapters: [
      {
        id: "chapter-01",
        num: 1,
        title: "The Integration Problem MCP Solves",
        path: "chapters/chapter-01-the-integration-problem-mcp-solves/lesson.html",
        description: "Why bespoke tool integrations don't scale across many models and many tools.",
        status: "planned"
      }
    ]
  },
  {
    title: "Module 2 — MCP Core Concepts",
    summary: "Host, client, server, JSON-RPC, stateless request/response, capability negotiation.",
    examPath: "assessments/written-exams/module-2-exam.md",
    chapters: [
      {
        id: "chapter-02",
        num: 2,
        title: "MCP Architecture: Hosts, Clients, Servers",
        path: "chapters/chapter-02-mcp-architecture-hosts-clients-servers/lesson.html",
        description: "The three roles and how they relate.",
        status: "planned"
      },
      {
        id: "chapter-03",
        num: 3,
        title: "The MCP Message Lifecycle",
        path: "chapters/chapter-03-the-mcp-message-lifecycle/lesson.html",
        description: "Stateless JSON-RPC, capability negotiation, and the 2026-07-28 vs 2025-11-25 compatibility story.",
        status: "planned"
      }
    ]
  },
  {
    title: "Module 3 — Building MCP Servers",
    summary: "Hands-on server construction with the Python SDK.",
    examPath: "assessments/written-exams/module-3-exam.md",
    chapters: [
      {
        id: "chapter-04",
        num: 4,
        title: "Your First MCP Server (Tools)",
        path: "chapters/chapter-04-your-first-mcp-server/lesson.html",
        description: "Build, run, and test a real MCP server exposing tools and a resource with the Python SDK.",
        status: "live",
        subtopics: [
          { id: "hook", title: "The problem: an assistant that can't act" },
          { id: "core-concepts", title: "Tools, resources, and the server object" },
          { id: "internals", title: "What happens when a tool is called" },
          { id: "build", title: "Build: a notes server" },
          { id: "failure-lab", title: "Failure lab: break the schema" },
          { id: "production", title: "Production scenario: banking runbook tool" },
          { id: "security", title: "Security considerations" },
          { id: "recap", title: "Points to remember" }
        ]
      },
      {
        id: "chapter-05",
        num: 5,
        title: "Resources & Prompts",
        path: "chapters/chapter-05-resources-and-prompts/lesson.html",
        description: "The other two MCP primitives and when to reach for each.",
        status: "planned"
      },
      {
        id: "chapter-06",
        num: 6,
        title: "Transports: stdio vs. Streamable HTTP",
        path: "chapters/chapter-06-transports/lesson.html",
        description: "Choosing a transport and the stateful/stateless compatibility story.",
        status: "planned"
      }
    ]
  },
  {
    title: "Module 4 — Building Clients & Hosts",
    summary: "The other half of the wire: connecting an agent to servers.",
    examPath: "assessments/written-exams/module-4-exam.md",
    chapters: [
      {
        id: "chapter-07",
        num: 7,
        title: "Building an MCP Client/Host",
        path: "chapters/chapter-07-building-an-mcp-client-host/lesson.html",
        description: "Connect an agent loop to a running server.",
        status: "planned"
      },
      {
        id: "chapter-08",
        num: 8,
        title: "Connecting Multiple Servers to One Agent",
        path: "chapters/chapter-08-connecting-multiple-servers/lesson.html",
        description: "Merging tool catalogs and resolving conflicts.",
        status: "planned"
      }
    ]
  },
  {
    title: "Module 5 — Security & Trust Boundaries",
    summary: "MCP-specific security thinking: the course's core differentiator.",
    examPath: "assessments/written-exams/module-5-exam.md",
    chapters: [
      {
        id: "chapter-09",
        num: 9,
        title: "Permissions, Scopes & Sandboxing",
        path: "chapters/chapter-09-permissions-scopes-sandboxing/lesson.html",
        description: "Least privilege for tool access.",
        status: "planned"
      },
      {
        id: "chapter-10",
        num: 10,
        title: "Prompt Injection & Tool-Output Trust",
        path: "chapters/chapter-10-prompt-injection-and-tool-output-trust/lesson.html",
        description: "Defending against untrusted tool results.",
        status: "planned"
      }
    ]
  },
  {
    title: "Module 6 — Production MCP",
    summary: "What changes between a demo server and one that survives production.",
    examPath: "assessments/written-exams/module-6-exam.md",
    chapters: [
      {
        id: "chapter-11",
        num: 11,
        title: "Testing, Debugging & Observability",
        path: "chapters/chapter-11-testing-debugging-observability/lesson.html",
        description: "Traces, logs, and realistic failure diagnosis.",
        status: "planned"
      },
      {
        id: "chapter-12",
        num: 12,
        title: "Versioning, Errors & Production Hardening",
        path: "chapters/chapter-12-versioning-errors-production-hardening/lesson.html",
        description: "Spec-version compatibility and graceful degradation.",
        status: "planned"
      }
    ]
  },
  {
    title: "Module 7 — Architecture & Capstone",
    summary: "Think like an architect, not just a builder.",
    examPath: null,
    chapters: [
      {
        id: "chapter-13",
        num: 13,
        title: "Capstone: Enterprise MCP Platform Architecture",
        path: "chapters/chapter-13-capstone-enterprise-mcp-platform/lesson.html",
        description: "Design secure, multi-tenant MCP infrastructure for a regulated enterprise.",
        status: "planned"
      }
    ]
  }
];
