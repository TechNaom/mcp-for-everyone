"""
Chapter 11 mini project: an SLO calculator.

Ingests structured log lines (the format this chapter's exercises
produce) and computes success rate and p95 latency per tool -- the
measurable foundation for the SLOs this chapter's architect interview
question asked about.

Fill in the TODOs. See solution.py for a reference implementation.
"""

import importlib.util
import json
from pathlib import Path


def load_exercises_module():
    ex_path = Path(__file__).parents[1] / "exercises" / "solution.py"
    spec = importlib.util.spec_from_file_location("ch11_exercises", ex_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def compute_slo_report(log_lines: list[str]) -> dict[str, dict]:
    """Return {tool_name: {"success_rate": float, "p95_ms": float,
    "call_count": int}} computed from "tool_call_end" events only."""
    # TODO 1: Parse each line as JSON. Skip lines that aren't valid
    # JSON or aren't "tool_call_end" events.

    # TODO 2: Group the end-events by "tool" name.

    # TODO 3: For each tool, compute:
    #   - call_count: how many end-events
    #   - success_rate: fraction where is_error is False
    #   - p95_ms: the 95th percentile of elapsed_ms (sort the values,
    #     index = int(0.95 * (len(values) - 1)))
    return {}


def print_report(report: dict[str, dict]) -> None:
    # TODO 4: Print a clean per-tool summary line, e.g.:
    #   save_note: 12 calls, 100.0% success, p95=4.20ms
    pass


if __name__ == "__main__":
    # Generate some real log data by actually calling the notes server,
    # capturing what its logger emits.
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
            # Per Ch.3/4: a raised ValueError inside a tool comes back as
            # a normal is_error=True result, not a client-side exception
            # -- no try/except needed here, we're just generating a
            # failure log entry on purpose.
            await client.call_tool("delete_note", {"title": "nonexistent"})

    asyncio.run(generate_traffic())

    report = compute_slo_report(captured)
    print_report(report)
