# Chapter Quality Audit: Transports: stdio vs. Streamable HTTP

## Summary

- Chapter: 6 — Transports: stdio vs. Streamable HTTP
- Reviewer: Claude (self-audit against `chapter-audit.template.md`)
- Date: 2026-08-09
- Status: Pass

## Scores

| Dimension | Score | Notes |
|---|---:|---|
| Conversational clarity | 5/5 | Opens from what every prior chapter already used (stdio) before introducing the new transport |
| Production depth | 5/5 | Load-balancer scenario is a real, common deployment failure mode directly caused by the chapter's core finding |
| Real-time adoption usefulness | 5/5 | The chapter's central claim (`stateless_http` defaults to False) was discovered by inspecting the installed SDK's actual function signature, not documentation or memory — genuinely non-obvious and dated (v2.0.0) |
| Architecture and diagrams | 4/5 | Transport-choice decision table; wire-level curl output serves as the diagram for this content |
| Exercises | 5/5 | 6 tasks, 3 production-gear; task 3 has the learner reproduce the exact 400 error from the lesson themselves |
| Practice bank | 5/5 | 6 scenarios spanning operations, cost, security, debugging, support, evaluation |
| Interview preparation | 5/5 | 8 questions across all 4 levels; architect question correctly distinguishes session bookkeeping from authentication, setting up Module 5 |
| Project implementation | 5/5 | Health-check probe tested against both a live and a stopped server, correct exit codes verified |
| Builder thought-process layer | 5/5 | Documents the actual investigation (assumption → test → contradiction → source inspection → validation) that produced this chapter's core finding |
| Navigation/template consistency | 5/5 | Matches established page set |
| Accessibility/readability | 4/5 | Semantic headings, table with proper thead/tbody |
| Public artifact readiness | 5/5 | No secrets, no placeholders |

## Required Checks

- [x] Lesson starts with a problem, not jargon.
- [x] Lesson includes core concepts, worked examples, a genuine debugging narrative, production scenario, common mistakes, thought-process journal, summary/cheat-sheet.
- [x] Exercises include at least 6 tasks, with at least 3 production-gear tasks.
- [x] Practice bank includes at least 6 realistic scenarios.
- [x] Interview bank includes at least 8 questions spanning beginner/intermediate/senior/architect.
- [x] Project includes a meaningful implementation, verified runnable end-to-end against both a healthy and an unreachable server.
- [x] Chapter includes diagrams or visual/text architecture aids. (Decision table + real wire output.)
- [x] Chapter includes a thinking journal.
- [x] Navigation follows lesson -> quiz -> exercises -> practice -> interview -> project.
- [x] Content is original and not copied from reference repos.
- [x] Any code example has been executed against the real SDK/spec version. This is the chapter where that discipline mattered most: the lesson's central claim came directly from running `inspect.signature()` against the installed SDK and testing raw curl requests against a live server on two different ports (session-based and stateless), not from documentation.

## Follow-Up Tasks

- None outstanding. Note for future maintenance: `stateless_http`'s default is an SDK implementation choice, not a spec requirement — re-verify this default hasn't changed if the course is updated against a newer SDK version.
