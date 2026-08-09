# Chapter Quality Audit: Connecting Multiple Servers to One Agent

## Summary

- Chapter: 8 — Connecting Multiple Servers to One Agent
- Reviewer: Claude (self-audit against `chapter-audit.template.md`)
- Date: 2026-08-09
- Status: Pass

## Scores

| Dimension | Score | Notes |
|---|---:|---|
| Conversational clarity | 5/5 | Delivers on a promise made explicitly in Chapter 2 ("this chapter covers it") |
| Production depth | 5/5 | Production scenario is the exact bug reproduced in the lesson, not a hypothetical variant |
| Real-time adoption usefulness | 5/5 | The collision, its silent failure, and the namespaced fix were all built and run against two real servers, not described abstractly |
| Architecture and diagrams | 4/5 | Code-based before/after (naive vs. namespaced merge output) serves as the diagram |
| Exercises | 6/6 | 6 tasks, 3 production-gear; tasks 4-5 have the learner extend to 3 and 4 servers and confirm the collision test generalizes |
| Practice bank | 6/6 | 6 scenarios: support, product, cost, debugging, operations, evaluation |
| Interview preparation | 8/8 | 8 questions across all 4 levels; architect Q8 correctly distinguishes naming collisions from a related but distinct multi-party trust problem |
| Project implementation | 5/5 | Two-server CLI host (notes + bookmarks) tested end-to-end; surfaced and fixed a real limitation (naive parser can't produce list-typed arguments) rather than hiding it |
| Builder thought-process layer | 5/5 | Documents the actual verify-then-fix methodology used to build the chapter's own core example |
| Navigation/template consistency | 5/5 | Matches established page set |
| Accessibility/readability | 4/5 | Semantic headings throughout |
| Public artifact readiness | 5/5 | No secrets, no placeholders |

## Required Checks

- [x] Lesson starts with a problem, not jargon. (Opens by fulfilling Chapter 2's explicit promise.)
- [x] Lesson includes core concepts, worked example (a real reproduced bug), production scenario, common mistakes, thought-process journal, summary/cheat-sheet.
- [x] Exercises include at least 6 tasks, with at least 3 production-gear tasks.
- [x] Practice bank includes at least 6 realistic scenarios.
- [x] Interview bank includes at least 8 questions spanning beginner/intermediate/senior/architect.
- [x] Project includes a meaningful implementation, verified runnable end-to-end against two real Chapter 4 servers.
- [x] Chapter includes diagrams or visual/text architecture aids. (Real before/after merge output.)
- [x] Chapter includes a thinking journal.
- [x] Navigation follows lesson -> quiz -> exercises -> practice -> interview -> project.
- [x] Content is original and not copied from reference repos.
- [x] Any code example has been executed against the real SDK/spec version. The lesson's central collision was reproduced with two real MCPServer instances sharing a tool name, confirmed with printed output showing the naive merge silently dropping one; the project's list-argument parsing bug was found and fixed the same way.

## Follow-Up Tasks

- None outstanding.
