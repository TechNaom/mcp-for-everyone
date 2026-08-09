# Chapter Quality Audit: Permissions, Scopes & Sandboxing

## Summary

- Chapter: 9 — Permissions, Scopes & Sandboxing
- Reviewer: Claude (self-audit against `chapter-audit.template.md`)
- Date: 2026-08-09
- Status: Pass

## Scores

| Dimension | Score | Notes |
|---|---:|---|
| Conversational clarity | 5/5 | Opens by naming the exact gap every prior chapter's tools have had — no permission checks at all |
| Production depth | 5/5 | Production scenario distinguishes code-level vs. infrastructure-level enforcement, a genuine senior-level distinction |
| Real-time adoption usefulness | 5/5 | Scope decorator tested with 3 real scenarios (no scope, wrong scope, correct scope); explicitly honest about where the demo simplifies (identity verification) vs. where it doesn't (enforcement pattern), and names the SDK's real AuthSettings/authenticated_principal mechanism |
| Architecture and diagrams | 4/5 | Cheat-sheet code and the scopes-vs-sandboxing distinction carry the architecture |
| Exercises | 6/6 | 6 tasks, 3 production-gear; task 6 has the learner reproduce a missing-check regression themselves |
| Practice bank | 6/6 | 6 scenarios: security, compliance, support, operations, cost, evaluation |
| Interview preparation | 8/8 | 8 questions across all 4 levels; senior/architect questions cover scope taxonomy, testing philosophy, and platform-level design |
| Project implementation | 5/5 | Permission audit tool tested against both a passing and a deliberately-broken case; required fixing a real bug found during testing (missing introspection marker) before it worked |
| Builder thought-process layer | 5/5 | Honest about the identity-verification simplification and why it was made |
| Navigation/template consistency | 5/5 | Matches established page set |
| Accessibility/readability | 4/5 | Semantic headings throughout |
| Public artifact readiness | 5/5 | No secrets, no placeholders |

## Required Checks

- [x] Lesson starts with a problem, not jargon.
- [x] Lesson includes core concepts, worked example, a real production scenario distinguishing code vs. infrastructure enforcement, common mistakes, thought-process journal, summary/cheat-sheet.
- [x] Exercises include at least 6 tasks, with at least 3 production-gear tasks.
- [x] Practice bank includes at least 6 realistic scenarios.
- [x] Interview bank includes at least 8 questions spanning beginner/intermediate/senior/architect.
- [x] Project includes a meaningful implementation, verified runnable end-to-end against both a passing and a failing case.
- [x] Chapter includes diagrams or visual/text architecture aids. (Cheat-sheet code, scopes-vs-sandboxing distinction.)
- [x] Chapter includes a thinking journal.
- [x] Navigation follows lesson -> quiz -> exercises -> practice -> interview -> project.
- [x] Content is original and not copied from reference repos.
- [x] Any code example has been executed against the real SDK/spec version. This chapter's project caught a real bug during testing: the `require_scope` decorator initially lacked the `_required_scope` introspection marker the audit tool depended on -- discovered because the audit tool falsely flagged every tool as unscoped, traced to the missing marker, and fixed across the lesson, exercises/starter.py, and exercises/solution.py consistently.

## Follow-Up Tasks

- None outstanding. Note: this chapter's identity-verification simplification (contextvar instead of real OAuth) is intentional and explained in the lesson; a future "AI Security for Everyone" course (per the TechNaom roadmap) would be the natural place for full auth-server implementation depth.
