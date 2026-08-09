# Module 2 Written Exam — MCP Core Concepts

Covers: Chapter 2 (MCP Architecture: Hosts, Clients, Servers), Chapter 3
(The MCP Message Lifecycle)

No open resources needed beyond the chapters themselves. Write full
sentences — a bullet list of keywords doesn't demonstrate understanding.

## Concept Questions

1. Define host, client, and server in MCP, and explain where the LLM
   itself fits (or doesn't fit) into this model.
2. What is the difference between a JSON-RPC request, a result response,
   and a notification? Which one(s) include an `id`?
3. Explain what "stateless" means in the 2026-07-28 spec, using the
   spec's own rule about what a server must not infer from prior
   requests on the same connection.

## Scenario Questions

4. A host connects to 4 MCP servers simultaneously. Two of them expose a
   tool called `search`. Using Chapter 2's model, whose responsibility is
   it to resolve this naming collision, and what's one way to do it?
5. Your client is modern (2026-07-28). You connect it to a server built
   in early 2026, before the spec update. Using the compatibility matrix
   from Chapter 3, what's the likely outcome, and why might the failure
   not be immediately obvious?

## Debugging / Judgment Questions

6. A response you captured has no `resultType` field at all. Per the
   spec's backward-compatibility rule, how should a well-behaved modern
   client interpret this, and what does its absence tell you about the
   server?
7. You inspect a request's `_meta` and see
   `io.modelcontextprotocol/clientInfo` claiming to be a specific
   internal tool. Can you rely on this for an audit log proving which
   team made the request? Why or why not?

## Architecture / Production Questions

8. Design the ownership model for an internal MCP server that started
   with one consumer and now has five. What roles/processes do you put
   in place, and how does this connect to the host/client/server
   boundaries from Chapter 2?

## Self-Check

Compare your answers against `chapters/chapter-02-mcp-architecture-hosts-clients-servers/`
and `chapters/chapter-03-the-mcp-message-lifecycle/`, especially their
interview-questions.html pages. There is no answer key published — if
you can defend your answer against the "red flag" descriptions there,
you've answered it well.
