# Module 4 Written Exam — Building Clients & Hosts

Covers: Chapter 7 (Building an MCP Client/Host), Chapter 8 (Connecting
Multiple Servers to One Agent)

No open resources needed beyond the chapters themselves. Write full
sentences — a bullet list of keywords doesn't demonstrate understanding.

## Concept Questions

1. What are a host's two core jobs, and which parts of that are defined
   by the MCP protocol versus pure application code you write yourself?
2. Explain, precisely, what happens when a naive dict-by-name merge of
   two servers' tool catalogs encounters a name collision. Does it
   error? What's actually left in the merged catalog?
3. Describe the two separate steps required to correctly support
   multiple servers with colliding tool names.

## Scenario Questions

4. A host reports a tool call as successful, but nothing actually
   happened from the user's perspective. Walk through your debugging
   process, referencing the specific SDK behavior involved.
5. You're adding a third MCP server to a host that already connects to
   two. What would you check before deploying, given this module's
   central lesson about collisions?

## Debugging / Judgment Questions

6. A colleague's host implementation calls `list_tools()` fresh before
   every single tool invocation, even within one ongoing conversation.
   Is this wrong? What would you ask them before deciding whether to
   flag it in review?
7. Your namespaced merge test (`len(catalog) == sum(...)`) starts
   failing after a routine deploy that touched no host code. What's your
   first hypothesis, given what changed operationally rather than in
   code?

## Architecture / Production Questions

8. Design a host that connects to 6 independently-owned MCP servers
   across different teams. Specify: how you handle tool-name collisions,
   how you decide when to re-discover a server's catalog, and one
   organizational (not just technical) practice you'd put in place to
   reduce how often collisions happen in the first place.

## Self-Check

Compare your answers against Chapters 7–8 and their interview-questions
pages. There is no answer key published — if you can defend your answer
against the "red flag" descriptions there, you've answered it well.
