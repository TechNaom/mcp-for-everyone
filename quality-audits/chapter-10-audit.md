# Chapter Quality Audit: Prompt Injection & Tool-Output Trust

## Summary

- Chapter: 10 — Prompt Injection & Tool-Output Trust
- Reviewer: Claude (self-audit against `chapter-audit.template.md`)
- Date: 2026-08-09
- Status: Pass

## Scores

| Dimension | Score | Notes |
|---|---:|---|
| Conversational clarity | 5/5 | Explicitly distinguishes this threat from Chapter 9's, opening with "the attacker who never calls a tool" |
| Production depth | 5/5 | Production scenario is subtle and realistic (non-malicious customer, distorted summary) rather than a cartoonish attack |
| Real-time adoption usefulness | 5/5 | Real scanner tested against real benign/malicious/sneaky content; explicitly honest about incompleteness rather than overclaiming |
| Architecture and diagrams | 4/5 | Layered cheat-sheet (4 mitigation layers) carries the architecture |
| Exercises | 6/6 | 6 tasks, 3 production-gear; task 5 explicitly has the learner prove the scanner's incompleteness themselves |
| Practice bank | 6/6 | 6 scenarios: security, product, support, compliance, cost, operations |
| Interview preparation | 8/8 | 8 questions across all 4 levels; architect questions cover incident response and risk-combination assessment |
| Project implementation | 5/5 | ContentFirewall tested end-to-end; building it surfaced and fixed a real, general bug (unguarded asyncio.run at import time) retroactively applied across 8 prior chapters |
| Builder thought-process layer | 5/5 | Honest about the no-live-LLM constraint and how the chapter worked around it without overclaiming |
| Navigation/template consistency | 5/5 | Matches established page set |
| Accessibility/readability | 4/5 | Semantic headings throughout |
| Public artifact readiness | 5/5 | No secrets, no placeholders |

## Required Checks

- [x] Lesson starts with a problem, not jargon.
- [x] Lesson includes core concepts, worked example, an explicit "why this isn't a complete solution" section, production scenario, common mistakes, thought-process journal, summary/cheat-sheet.
- [x] Exercises include at least 6 tasks, with at least 3 production-gear tasks.
- [x] Practice bank includes at least 6 realistic scenarios.
- [x] Interview bank includes at least 8 questions spanning beginner/intermediate/senior/architect.
- [x] Project includes a meaningful implementation, verified runnable end-to-end.
- [x] Chapter includes diagrams or visual/text architecture aids. (Layered cheat-sheet.)
- [x] Chapter includes a thinking journal.
- [x] Navigation follows lesson -> quiz -> exercises -> practice -> interview -> project.
- [x] Content is original and not copied from reference repos.
- [x] Any code example has been executed against the real SDK/spec version. Building this chapter's project caught a significant, general bug: 8 prior chapters' exercises/project files called `asyncio.run(main())` unconditionally at module level, which crashes when the file is imported from inside an already-running event loop (exactly what a firewall wrapper does). Fixed with `if __name__ == "__main__":` guards across all 17 affected files (Chapters 3, 6, 7, 8, 9, 10), verified by re-running every chapter's exercises and project solutions after the fix.

## Follow-Up Tasks

- None outstanding. This chapter's own retroactive bug-fix (the asyncio.run guard) is documented in PROJECT_STATE.md as a course-wide fix, not just a Chapter 10 fix.
