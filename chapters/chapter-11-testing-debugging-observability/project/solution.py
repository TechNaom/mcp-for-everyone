"""Chapter 11 mini project — reference solution: an SLO calculator."""

import importlib.util
import json
from collections import defaultdict
from pathlib import Path


def load_exercises_module():
    ex_path = Path(__file__).parents[1] / "exercises" / "solution.py"
    spec = importlib.util.spec_from_file_location("ch11_exercises", ex_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def compute_slo_report(log_lines: list[str]) -> dict[str, dict]:
    end_events_by_tool: dict[str, list[dict]] = defaultdict(list)

    for line in log_lines:
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            continue
        if record.get("event") != "tool_call_end":
            continue
        tool = record.get("tool")
        if tool:
            end_events_by_tool[tool].append(record)

    report = {}
    for tool, events in end_events_by_tool.items():
        call_count = len(events)
        success_count = sum(1 for e in events if not e.get("is_error", False))
        success_rate = success_count / call_count if call_count else 0.0

        latencies = sorted(e.get("elapsed_ms", 0.0) for e in events)
        p95_index = int(0.95 * (len(latencies) - 1)) if latencies else 0
        p95_ms = latencies[p95_index] if latencies else 0.0

        report[tool] = {
            "call_count": call_count,
            "success_rate": round(success_rate, 4),
            "p95_ms": round(p95_ms, 2),
        }
    return report


def print_report(report: dict[str, dict]) -> None:
    if not report:
        print("No tool_call_end events found.")
        return
    for tool, stats in report.items():
        pct = stats["success_rate"] * 100
        print(
            f"{tool}: {stats['call_count']} calls, "
            f"{pct:.1f}% success, p95={stats['p95_ms']:.2f}ms"
        )


if __name__ == "__main__":
    import asyncio
    import logging

    ch11 = load_exercises_module()
    captured: list[str] = []

    class ListHandler(logging.Handler):
        def emit(self, record):
            captured.append(record.getMessage())

    ch11.logger.addHandler(ListHandler())
    ch11.logger.setLevel(logging.INFO)

    async def generate_traffic():
        from mcp import Client

        async with Client(ch11.mcp) as client:
            for i in range(10):
                await client.call_tool(
                    "save_note", {"title": f"t{i}", "body": "x"},
                    meta={"traceparent": f"trace-{i}"},
                )
            await client.call_tool("delete_note", {"title": "nonexistent"})

    asyncio.run(generate_traffic())

    report = compute_slo_report(captured)
    print_report(report)
