# Module 6 Written Exam — Production MCP

Covers: Chapter 11 (Testing, Debugging & Observability), Chapter 12
(Versioning, Errors & Production Hardening)

No open resources needed beyond the chapters themselves. Write full
sentences — a bullet list of keywords doesn't demonstrate understanding.

## Concept Questions

1. What does the Context parameter give a tool access to, and why
   doesn't it appear in the tool's model-visible schema?
2. Why is `ctx.info()`/`ctx.log()` no longer the recommended way to
   build server-side observability, and what should be used instead?
3. Explain what "dual-era by default" means for an MCP server built
   with the current SDK, and why it doesn't guarantee identical
   behavior across both eras.

## Scenario Questions

4. A user reports an issue but support has no trace ID for the affected
   request. Using Chapter 11's logging pattern, what should have existed
   beforehand to make this investigable, and why wasn't a timestamp
   alone sufficient?
5. A server passes all its tests, all written against the SDK's default
   (modern-mode) client. A partner using an older client library reports
   a subtle behavior difference. What kind of test would have caught
   this before it reached production?

## Debugging / Judgment Questions

6. A structured log shows a tool call with `is_error: false`, but the
   user insists the call failed from their perspective. Name two
   different explanations consistent with this symptom, at two
   different layers of the system.
7. A tool's own code never fails, but a downstream database it depends
   on periodically goes down. Why isn't type-hint-driven argument
   validation sufficient to handle this failure mode?

## Architecture / Production Questions

8. Design the production-readiness checklist a new MCP server must pass
   before it's allowed to go live at your organization. Reference at
   least four concrete practices from Chapters 1–12 (not generic
   security/testing advice), and specify which would be hard gates
   versus soft recommendations.

## Self-Check

Compare your answers against Chapters 11–12 and their interview-questions
pages. There is no answer key published — if you can defend your answer
against the "red flag" descriptions there, you've answered it well.
