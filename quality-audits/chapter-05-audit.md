# Chapter Quality Audit: Resources & Prompts

## Summary

- Chapter: 5 — Resources & Prompts
- Reviewer: Claude (self-audit against `chapter-audit.template.md`)
- Date: 2026-08-09
- Status: Pass

## Scores

| Dimension | Score | Notes |
|---|---:|---|
| Conversational clarity | 5/5 | Opens by questioning a "tool" that shouldn't have been a tool, grounded in the Chapter 4 notes server |
| Production depth | 5/5 | Real production scenario (invisible policy resources) traces to a genuine, non-obvious discovery-API gap |
| Real-time adoption usefulness | 5/5 | Every code sample and API detail (list_resources vs list_resource_templates, get_prompt's return shape, snake_case attribute names) verified against installed SDK v2.0.0 |
| Architecture and diagrams | 4/5 | Decision table (tool/resource/prompt) carries the chapter's core teaching; no image diagram needed for this content |
| Exercises | 5/5 | 6 tasks, 3 production-gear, task 3 has the learner reproduce the lesson's own discovery-split finding themselves |
| Practice bank | 5/5 | 6 scenarios spanning support, product, cost, compliance, operations, evaluation |
| Interview preparation | 5/5 | 8 questions across all 4 levels; architect questions connect forward to Chapter 3 (caching) and Chapter 10 (prompt injection) |
| Project implementation | 5/5 | Extends Chapter 4's bookmarks server; verified end-to-end against the real SDK |
| Builder thought-process layer | 5/5 | Thinking-box mirrors the actual debugging approach used to find the lesson's own production scenario |
| Navigation/template consistency | 5/5 | Matches established page set |
| Accessibility/readability | 4/5 | Semantic headings, table with proper thead/tbody |
| Public artifact readiness | 5/5 | No secrets, no placeholders |

## Required Checks

- [x] Lesson starts with a problem, not jargon.
- [x] Lesson includes core concepts, worked examples, production scenario, common mistakes, thought-process journal, summary/cheat-sheet.
- [x] Exercises include at least 6 tasks, with at least 3 production-gear tasks.
- [x] Practice bank includes at least 6 realistic scenarios.
- [x] Interview bank includes at least 8 questions spanning beginner/intermediate/senior/architect.
- [x] Project includes a meaningful implementation, verified runnable end-to-end.
- [x] Chapter includes diagrams or visual/text architecture aids. (Decision table.)
- [x] Chapter includes a thinking journal.
- [x] Navigation follows lesson -> quiz -> exercises -> practice -> interview -> project.
- [x] Content is original and not copied from reference repos.
- [x] Any code example has been executed against the real SDK/spec version. All lesson code blocks, exercises/solution.py, and project/solution.py were run against `mcp` v2.0.0. This also caught and fixed a real bug: the cross-chapter import pattern (sys.path + `import solution`) used in Chapter 3 and initially attempted here breaks depending on invocation method, since both files share the name `solution.py`. Fixed with `importlib.util.spec_from_file_location` in both chapters, verified under both script and import-by-name invocation.

## Follow-Up Tasks

- None outstanding.
