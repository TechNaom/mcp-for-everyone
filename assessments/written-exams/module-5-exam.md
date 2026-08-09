# Module 5 Written Exam — Security & Trust Boundaries

Covers: Chapter 9 (Permissions, Scopes & Sandboxing), Chapter 10 (Prompt
Injection & Tool-Output Trust)

No open resources needed beyond the chapters themselves. Write full
sentences — a bullet list of keywords doesn't demonstrate understanding.

## Concept Questions

1. Does MCP provide a permission model? What does `require_scope` in
   this module actually enforce, and at what layer?
2. Explain the difference between the threat Chapter 9 addresses and
   the threat Chapter 10 addresses. Could a caller be fully authorized
   (per Chapter 9) and still be part of a Chapter 10-style attack?
3. Why is a regex-based injection scanner described as "one layer,"
   not "the solution"? What specifically can it not catch?

## Scenario Questions

4. A tool is supposed to be read-only but connects to a database with
   full write access. Using Chapter 9's production scenario, explain
   why "the tool's own code never writes" is not a sufficient safety
   guarantee.
5. A host processes a fetched document that contains text attempting to
   redirect the model's behavior. The affected session has no scope for
   any destructive tool. Using Chapter 10's argument, why does this
   limit the actual damage even if the injection "works" on the model?

## Debugging / Judgment Questions

6. A permission system's test suite has 100% pass rate, but only tests
   that authorized calls succeed. What's missing, and why does this
   matter more for a security control than for ordinary functionality?
7. A teammate proposes marking the "prompt injection" risk as "resolved"
   after shipping a keyword scanner. How do you respond, and what
   status would you propose instead?

## Architecture / Production Questions

8. Design the security posture for an MCP server that summarizes
   user-uploaded documents and has tools that can send emails. Specify:
   how scopes are structured, what triggers human confirmation, and how
   incident response would work if a successful injection were
   suspected.

## Self-Check

Compare your answers against Chapters 9–10 and their interview-questions
pages. There is no answer key published — if you can defend your answer
against the "red flag" descriptions there, you've answered it well.
