# Chapter Quality Audit: Testing, Debugging & Observability

## Summary

- Chapter: 11 — Testing, Debugging & Observability
- Reviewer: Claude (self-audit against `chapter-audit.template.md`)
- Date: 2026-08-09
- Status: Pass

## Scores

| Dimension | Score | Notes |
|---|---:|---|
| Conversational clarity | 5/5 | Opens by naming every prior chapter's diagnostic moment, tying observability to lived course experience rather than an abstract new topic |
| Production depth | 5/5 | Production scenario (unresolved incident) is a realistic, non-cartoonish consequence of missing trace correlation |
| Real-time adoption usefulness | 5/5 | Discovered and reported a genuine, current spec-version deprecation (ctx.info/log, SEP-2577) by testing against the installed SDK, not from documentation |
| Architecture and diagrams | 4/5 | Cheat-sheet code and the debugging-workflow narrative carry the architecture |
| Exercises | 6/6 | 6 tasks, 3 production-gear; task 4 has the learner reconstruct a realistic multi-trace incident themselves |
| Practice bank | 6/6 | 6 scenarios: operations, cost, support, debugging, compliance, evaluation |
| Interview preparation | 8/8 | 8 questions across all 4 levels; architect Q8 directly connects logging schema to measurable SLOs, closing the loop with the project |
| Project implementation | 5/5 | SLO calculator tested against real generated traffic (not synthetic logs), correctly computing success rate and p95 latency including a deliberate failure case |
| Builder thought-process layer | 5/5 | Documents the actual investigation that found the deprecation, including the wrong initial assumption |
| Navigation/template consistency | 5/5 | Matches established page set |
| Accessibility/readability | 4/5 | Semantic headings throughout |
| Public artifact readiness | 5/5 | No secrets, no placeholders |

## Required Checks

- [x] Lesson starts with a problem, not jargon.
- [x] Lesson includes core concepts, a genuine current-spec finding (deprecation), worked example, production scenario, common mistakes, thought-process journal, summary/cheat-sheet.
- [x] Exercises include at least 6 tasks, with at least 3 production-gear tasks.
- [x] Practice bank includes at least 6 realistic scenarios.
- [x] Interview bank includes at least 8 questions spanning beginner/intermediate/senior/architect.
- [x] Project includes a meaningful implementation, verified runnable end-to-end against real (not synthetic) generated log data.
- [x] Chapter includes diagrams or visual/text architecture aids. (Cheat-sheet, debugging-workflow narrative.)
- [x] Chapter includes a thinking journal.
- [x] Navigation follows lesson -> quiz -> exercises -> practice -> interview -> project.
- [x] Content is original and not copied from reference repos.
- [x] Any code example has been executed against the real SDK/spec version. This chapter's central finding (ctx.info/log deprecated as of 2026-07-28, SEP-2577) came directly from a runtime deprecation warning triggered by calling the real API, corrected the chapter's planned approach mid-build, and is now the chapter's core recommendation.

## Follow-Up Tasks

- None outstanding. Worth periodically re-verifying the SEP-2577 deprecation status against a newer SDK release if the course is updated later, in case the capability is fully removed (not just deprecated) in a future spec revision.
