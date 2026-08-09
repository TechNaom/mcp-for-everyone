# Chapter Quality Audit: Building an MCP Client/Host

## Summary

- Chapter: 7 — Building an MCP Client/Host
- Reviewer: Claude (self-audit against `chapter-audit.template.md`)
- Date: 2026-08-09
- Status: Pass

## Scores

| Dimension | Score | Notes |
|---|---:|---|
| Conversational clarity | 5/5 | Opens by clarifying a real confusion (Client vs. host) that six chapters of using Client could easily create |
| Production depth | 5/5 | Production scenario is a direct, honest consequence of skipping the exact check the chapter's own code includes |
| Real-time adoption usefulness | 5/5 | ToyHost tested end-to-end against the real notes server; honest about being a stand-in for LLM decision-making rather than pretending otherwise |
| Architecture and diagrams | 4/5 | Two-jobs framing and cheat-sheet code carry the architecture; no separate diagram needed for this content |
| Exercises | 6/6 | 6 tasks, 3 production-gear (guard, typo test, timeout); all extend tested code |
| Practice bank | 6/6 | 6 scenarios: support, product, cost, debugging, compliance, operations |
| Interview preparation | 8/8 | 8 questions across all 4 levels; architect questions foreshadow Module 5 security content deliberately |
| Project implementation | 5/5 | CLI host tested via piped stdin, including the unknown-command error path |
| Builder thought-process layer | 5/5 | Documents the actual design trade-off (exact-match vs. NLU) with genuine reasoning, not retrofitted |
| Navigation/template consistency | 5/5 | Matches established page set |
| Accessibility/readability | 4/5 | Semantic headings throughout |
| Public artifact readiness | 5/5 | No secrets, no placeholders |

## Required Checks

- [x] Lesson starts with a problem, not jargon. (Opens from a real ambiguity six prior chapters could have created.)
- [x] Lesson includes core concepts, worked example, production scenario, common mistakes, thought-process journal, summary/cheat-sheet.
- [x] Exercises include at least 6 tasks, with at least 3 production-gear tasks.
- [x] Practice bank includes at least 6 realistic scenarios.
- [x] Interview bank includes at least 8 questions spanning beginner/intermediate/senior/architect.
- [x] Project includes a meaningful implementation, verified runnable end-to-end (piped stdin test, including error path).
- [x] Chapter includes diagrams or visual/text architecture aids. (Cheat-sheet code block, two-jobs list.)
- [x] Chapter includes a thinking journal.
- [x] Navigation follows lesson -> quiz -> exercises -> practice -> interview -> project.
- [x] Content is original and not copied from reference repos.
- [x] Any code example has been executed against the real SDK/spec version. ToyHost, all exercises, and the CLI host project were all run against `mcp` v2.0.0 and the Chapter 4 notes server.

## Follow-Up Tasks

- None outstanding.
