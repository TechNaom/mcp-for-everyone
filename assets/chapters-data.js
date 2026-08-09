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
    examPath: "assessments/written-exams/module-4-exam.md",
    chapters: [
      {
        id: "chapter-07",
        num: 7,
        title: "Building an MCP Client/Host",
        path: "chapters/chapter-07-building-an-mcp-client-host/lesson.html",
        description: "Build the other half of the wire: a host that discovers tools and decides what to call, tested end-to-end.",
        subtopics: [
          { id: "hook", title: "What a host actually does" },
          { id: "two-jobs", title: "The host's two jobs" },
          { id: "toy-host", title: "Build: a minimal host" },
          { id: "where-llm-fits", title: "Where a real LLM fits in" },
          { id: "recap", title: "Points to remember" }
        ]
      },
      {
        id: "chapter-08",
        num: 8,
        title: "Connecting Multiple Servers to One Agent",
        path: "chapters/chapter-08-connecting-multiple-servers/lesson.html",
        description: "Merging tool catalogs and resolving a real, reproduced tool-name collision with namespacing.",
        subtopics: [
          { id: "hook", title: "Two servers, one host" },
          { id: "the-collision", title: "Reproducing the collision" },
          { id: "namespacing", title: "The fix: namespacing" },
          { id: "routing-calls", title: "Routing calls back to the right server" },
          { id: "recap", title: "Points to remember" }
        ]
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
        description: "Enforce least privilege on MCP tools with a real, tested scope-checking pattern.",
        subtopics: [
          { id: "hook", title: "What every tool in this course has assumed" },
          { id: "least-privilege", title: "Least privilege, concretely" },
          { id: "scope-decorator", title: "Build: a scope-enforcing decorator" },
          { id: "real-auth", title: "What a production system uses instead" },
          { id: "sandboxing", title: "Sandboxing: the other half of containment" },
          { id: "recap", title: "Points to remember" }
        ]
      },
      {
        id: "chapter-10",
        num: 10,
        title: "Prompt Injection & Tool-Output Trust",
        path: "chapters/chapter-10-prompt-injection-and-tool-output-trust/lesson.html",
        description: "Defend against untrusted tool results with a tested detection pattern, and understand why detection alone isn't enough.",
        subtopics: [
          { id: "hook", title: "The attacker who never calls a tool" },
          { id: "the-attack", title: "A concrete injection attempt" },
          { id: "detection", title: "Build: a detection pattern" },
          { id: "why-not-enough", title: "Why detection alone isn't enough" },
          { id: "real-mitigations", title: "The mitigations that actually hold" },
          { id: "recap", title: "Points to remember" }
        ]
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
        description: "Structured logging and trace correlation with the real Context API, including a current spec deprecation this course caught by testing.",
        subtopics: [
          { id: "hook", title: "What \"it's not working\" actually means" },
          { id: "the-context-object", title: "Meet Context" },
          { id: "deprecated-logging", title: "A real deprecation, found by testing" },
          { id: "structured-logging", title: "Build: structured logging with trace correlation" },
          { id: "debugging-workflow", title: "A debugging workflow that uses this" },
          { id: "recap", title: "Points to remember" }
        ]
      },
      {
        id: "chapter-12",
        num: 12,
        title: "Versioning, Errors & Production Hardening",
        path: "chapters/chapter-12-versioning-errors-production-hardening/lesson.html",
        description: "Real, tested proof that the SDK serves both modern and legacy clients simultaneously, plus a hardened error-handling pattern.",
        subtopics: [
          { id: "hook", title: "What Chapter 3 promised, tested for real" },
          { id: "dual-era-proof", title: "Proof: the SDK is dual-era by default" },
          { id: "what-this-means", title: "What this means for you" },
          { id: "error-hardening", title: "Build: hardening against bad input" },
          { id: "graceful-degradation", title: "Graceful degradation beyond validation" },
          { id: "recap", title: "Points to remember" }
        ]
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
        description: "Design secure, multi-tenant MCP infrastructure for a regulated enterprise -- a Level 4 architecture challenge with a tested reference skeleton to build from.",
        subtopics: [
          { id: "hook", title: "The business problem" },
          { id: "requirements", title: "What you're actually designing" },
          { id: "reference-architecture", title: "A tested reference architecture" },
          { id: "what-to-produce", title: "What to produce" },
          { id: "adr-format", title: "ADR format" },
          { id: "rubric", title: "Rubric" }
        ]
      }
    ]
  }
];
