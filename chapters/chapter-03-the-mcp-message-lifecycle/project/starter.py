"""
Chapter 3 mini project: a message-lifecycle logger.

Wrap calls to the Chapter 4 notes server and print a structured trace of
each exchange -- the kind of debug logging you'd actually want when
diagnosing the "silent version mismatch" scenario from the lesson.

Fill in the TODOs. See solution.py for a reference implementation.
"""

import asyncio
import importlib.util
import time
from pathlib import Path

from mcp import Client


def _load_chapter_4_module():
    """Load Chapter 4's notes-server solution by explicit file path
    (avoids a solution.py/solution.py name collision -- see Chapter 3's
    exercises/solution.py for the full explanation)."""
    ch4_path = (
        Path(__file__).parents[2]
        / "chapter-04-your-first-mcp-server"
        / "exercises"
        / "solution.py"
    )
    spec = importlib.util.spec_from_file_location("chapter_04_notes", ch4_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


mcp = _load_chapter_4_module().mcp


async def traced_call(client: "Client", tool_name: str, arguments: dict) -> None:
    """Call a tool and print a lifecycle trace: what was sent, what came back."""
    # TODO 1: Print a line showing the "outgoing request" shape:
    # method ("tools/call"), the tool name, and the arguments. You're
    # simulating what a request log would show, since the SDK doesn't
    # expose raw JSON-RPC bytes directly.

    start = time.monotonic()

    # TODO 2: Actually call the tool via `client.call_tool(...)` and
    # store the result.

    elapsed_ms = (time.monotonic() - start) * 1000

    # TODO 3: Print a line showing the "incoming response" shape:
    # result_type, is_error, and meta (all attributes on the result
    # object -- see Chapter 3's exercises for the attribute names).
    # Include elapsed_ms so this reads like a real request log.


async def main() -> None:
    async with Client(mcp) as client:
        await traced_call(client, "save_note", {"title": "trace-demo", "body": "hello"})
        await traced_call(client, "list_notes", {})

        # TODO 4 (production-gear): call a tool that doesn't exist
        # (e.g. "nonexistent_tool") using traced_call and see what
        # actually comes back. Don't assume -- run it and read the
        # printed result_type/is_error. Add a comment explaining what
        # you observed and why it matters for how you'd write error
        # handling around tool calls.


if __name__ == "__main__":
    asyncio.run(main())
