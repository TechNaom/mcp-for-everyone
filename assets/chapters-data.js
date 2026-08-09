/*
  Single source of truth for the MCP for Everyone chapter roster.
  Mirrors the rag-for-everyone / python-for-everyone pattern: sidebar.js
  and home.js render navigation from this file. A chapter is "live" iff
  it has a `path` — omit `path` for chapters that don't exist yet, do not
  set a placeholder path, or sidebar/home will link to a 404. The same
  rule applies to a module's `examPath`: set it to null until that
  module's written exam actually exists in
  assessments/written-exams/ -- do not pre-fill a path for an exam that
  hasn't been written yet.
  Chapters 1-5 have content today — see PROJECT_STATE.md.
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
        subtopics: [
          { id: "hook", title: "An assistant that can reason but can't act" },
          { id: "bespoke", title: "The bespoke-integration trap" },
          { id: "n-times-m", title: "N tools times M models" },
          { id: "what-mcp-is", title: "What MCP actually is" },
          { id: "not-a-silver-bullet", title: "What MCP doesn't solve" },
          { id: "recap", title: "Points to remember" }
        ]
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
        subtopics: [
          { id: "hook", title: "Where does \"the AI\" actually live?" },
          { id: "three-roles", title: "The three roles" },
          { id: "one-host-many-servers", title: "One host, many servers" },
          { id: "real-mapping", title: "Mapping this onto a real product" },
          { id: "architecture-view", title: "Architecture view" },
          { id: "recap", title: "Points to remember" }
        ]
      },
      {
        id: "chapter-03",
        num: 3,
        title: "The MCP Message Lifecycle",
        path: "chapters/chapter-03-the-mcp-message-lifecycle/lesson.html",
        description: "Stateless JSON-RPC, capability negotiation, and the 2026-07-28 vs 2025-11-25 compatibility story.",
        subtopics: [
          { id: "hook", title: "Why \"just JSON-RPC\" isn't the whole story" },
          { id: "three-message-types", title: "The three JSON-RPC message types" },
          { id: "meta", title: "Where protocol version and capabilities live" },
          { id: "worked-trace", title: "A worked exchange, field by field" },
          { id: "statelessness", title: "What \"stateless\" really means" },
          { id: "compatibility", title: "Modern vs. legacy compatibility" },
          { id: "recap", title: "Points to remember" }
        ]
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
        subtopics: [
          { id: "hook", title: "The tool you shouldn't have built" },
          { id: "static-vs-templated", title: "Static vs. templated resources" },
          { id: "the-gotcha", title: "The gotcha: two separate lists" },
          { id: "prompts", title: "Prompts: the skipped primitive" },
          { id: "when-to-use-what", title: "Choosing the right primitive" },
          { id: "recap", title: "Points to remember" }
        ]
      },
      {
        id: "chapter-06",
        num: 6,
        title: "Transports: stdio vs. Streamable HTTP",
        path: "chapters/chapter-06-transports/lesson.html",
        description: "Choosing a transport, and a tested gotcha: the SDK's Streamable HTTP defaults to session-based even under the stateless spec.",
        subtopics: [
          { id: "hook", title: "What stdio can't do" },
          { id: "stdio-recap", title: "stdio: what it actually is" },
          { id: "streamable-http", title: "Streamable HTTP: running it for real" },
          { id: "the-gotcha", title: "The gotcha: stateless_http defaults to False" },
          { id: "choosing", title: "Choosing a transport" },
          { id: "recap", title: "Points to remember" }
        ]
      }
    ]
  },
  {
    title: "Module 4 — Building Clients & Hosts",
    summary: "The other half of the wire: connecting an agent to servers.",
    examPath: null, /* written when Module 4's chapters are complete */
    chapters: [
      {
        id: "chapter-07",
        num: 7,
        title: "Building an MCP Client/Host",
        description: "Connect an agent loop to a running server."
      },
      {
        id: "chapter-08",
        num: 8,
        title: "Connecting Multiple Servers to One Agent",
        description: "Merging tool catalogs and resolving conflicts."
      }
    ]
  },
  {
    title: "Module 5 — Security & Trust Boundaries",
    summary: "MCP-specific security thinking: the course's core differentiator.",
    examPath: null, /* written when Module 5's chapters are complete */
    chapters: [
      {
        id: "chapter-09",
        num: 9,
        title: "Permissions, Scopes & Sandboxing",
        description: "Least privilege for tool access."
      },
      {
        id: "chapter-10",
        num: 10,
        title: "Prompt Injection & Tool-Output Trust",
        description: "Defending against untrusted tool results."
      }
    ]
  },
  {
    title: "Module 6 — Production MCP",
    summary: "What changes between a demo server and one that survives production.",
    examPath: null, /* written when Module 6's chapters are complete */
    chapters: [
      {
        id: "chapter-11",
        num: 11,
        title: "Testing, Debugging & Observability",
        description: "Traces, logs, and realistic failure diagnosis."
      },
      {
        id: "chapter-12",
        num: 12,
        title: "Versioning, Errors & Production Hardening",
        description: "Spec-version compatibility and graceful degradation."
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
        description: "Design secure, multi-tenant MCP infrastructure for a regulated enterprise."
      }
    ]
  }
];
