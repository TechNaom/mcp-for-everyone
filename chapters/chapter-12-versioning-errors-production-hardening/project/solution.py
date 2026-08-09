"""Chapter 12 mini project — reference solution: a dual-era behavior-parity checker."""

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
    results = []
    for tool_name, arguments in calls:
        result = await client.call_tool(tool_name, arguments)
        if result.is_error:
            value = result.content[0].text if result.content else None
        else:
            value = result.structured_content
        results.append({"tool": tool_name, "is_error": result.is_error, "result": value})
    return results


async def check_parity(mcp, calls: list[tuple[str, dict]]) -> list[str]:
    async with Client(mcp, mode="auto") as modern_client:
        modern_results = await run_calls(modern_client, calls)

    async with Client(mcp, mode="legacy") as legacy_client:
        legacy_results = await run_calls(legacy_client, calls)

    mismatches = []
    for (tool_name, arguments), modern, legacy in zip(calls, modern_results, legacy_results):
        if modern["is_error"] != legacy["is_error"]:
            mismatches.append(
                f"{tool_name}{arguments}: is_error differs "
                f"(modern={modern['is_error']}, legacy={legacy['is_error']})"
            )
        elif not modern["is_error"] and modern["result"] != legacy["result"]:
            mismatches.append(
                f"{tool_name}{arguments}: result differs "
                f"(modern={modern['result']!r}, legacy={legacy['result']!r})"
            )
    return mismatches


if __name__ == "__main__":
    ch12 = load_exercises_module()

    calls = [
        ("add", {"a": 2, "b": 3}),
        ("add", {"a": 1}),
        ("fetch_user_count", {}),
    ]

    mismatches = asyncio.run(check_parity(ch12.mcp, calls))
    if not mismatches:
        print("PASS: identical behavior across modern and legacy eras.")
    else:
        print(f"FAIL: {len(mismatches)} mismatch(es):")
        for m in mismatches:
            print(" ", m)
