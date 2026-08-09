# Module 3 Written Exam — Building MCP Servers

Covers: Chapter 4 (Your First MCP Server), Chapter 5 (Resources &
Prompts), Chapter 6 (Transports)

No open resources needed beyond the chapters themselves. Write full
sentences — a bullet list of keywords doesn't demonstrate understanding.

## Concept Questions

1. Explain the difference between a tool, a static resource, a
   templated resource, and a prompt. For each, state whether calling it
   can have a side effect.
2. Why does a missing type hint on a tool parameter not crash the
   server, and why is that more dangerous than a crash would be?
3. Explain what `stateless_http=True` actually changes about a
   Streamable HTTP server's behavior, using the raw-request evidence
   from Chapter 6, not just the parameter's name.

## Scenario Questions

4. A host reports it can't find a resource you know exists. Walk
   through your two-step debugging process, referencing the specific
   client methods involved.
5. You're deploying a new MCP server behind a load balancer for the
   first time. What two questions do you need to answer before choosing
   `stateless_http`'s value, and why does getting this wrong cause
   intermittent, hard-to-reproduce failures rather than an obvious one?

## Debugging / Judgment Questions

6. A teammate's tool function raises a `ValueError` for bad input, and
   they've wrapped every call site in `try/except` expecting to catch
   it. Will this work? Explain using what Chapter 3 and Chapter 4
   together established about how tool errors surface.
7. You're reviewing a PR that adds a resource called
   `get_active_user_count` implemented as a **tool**. Do you request a
   change? Justify your answer either way.

## Architecture / Production Questions

8. Design the deployment for an MCP server that must be reachable by
   three different internal products, scaled across multiple instances
   for availability. Specify: transport, `stateless_http` setting, and
   one thing you'd add to catch the class of bug in Chapter 6's
   production scenario before it reaches users.

## Self-Check

Compare your answers against Chapters 4-6 and their interview-questions
pages. There is no answer key published — if you can defend your answer
against the "red flag" descriptions there, you've answered it well.
