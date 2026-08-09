"""
Chapter 12 mini project: a dual-era behavior-parity checker.

Connects to a server under both mode="auto" (modern) and mode="legacy",
runs the same set of tool calls against each, and flags any call whose
result differs between eras -- the exact test this chapter's senior
interview question described, built for real.

Fill in the TODOs. See solution.py for a reference implementation.
"""

import asyncio
import importlib.util
from pathlib import Path

from mcp import Client


def load_exercises_module():
    ex_path = Path(__file__).parents[1] / "exercises" / "solution.py"
    spec = importlib.util.spec_from_file_location("ch12_exercises", ex_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


async def run_calls(client: "Client", calls: list[tuple[str, dict]]) -> list[dict]:
    """Run a list of (tool_name, arguments) calls and return a list of
    {"tool": ..., "is_error": ..., "result": ...} dicts."""
    # TODO 1: For each (tool_name, arguments) in `calls`, call it and
    # record the tool name, is_error, and structured_content (or the
    # error text if is_error). Return the list.
    return []


async def check_parity(mcp, calls: list[tuple[str, dict]]) -> list[str]:
    """Run `calls` against both eras and return a list of human-readable
    mismatch descriptions (empty list means full parity)."""
    # TODO 2: Connect with mode="auto", run_calls, then connect with
    # mode="legacy", run_calls again. Compare the two result lists
    # pairwise (same call, same position) and collect a description of
    # any difference (different is_error, or different result value).


if __name__ == "__main__":
    ch12 = load_exercises_module()

    calls = [
        ("add", {"a": 2, "b": 3}),
        ("add", {"a": 1}),  # missing arg, should error identically both eras
        ("fetch_user_count", {}),
    ]

    mismatches = asyncio.run(check_parity(ch12.mcp, calls))
    if not mismatches:
        print("PASS: identical behavior across modern and legacy eras.")
    else:
        print(f"FAIL: {len(mismatches)} mismatch(es):")
        for m in mismatches:
            print(" ", m)
