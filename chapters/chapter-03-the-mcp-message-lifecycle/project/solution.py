"""Chapter 3 mini project — reference solution: a message-lifecycle logger."""

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
    print(f">> tools/call  name={tool_name!r}  arguments={arguments}")

    start = time.monotonic()
    result = await client.call_tool(tool_name, arguments)
    elapsed_ms = (time.monotonic() - start) * 1000

    print(
        f"<< result_type={result.result_type!r}  is_error={result.is_error}  "
        f"meta={result.meta}  ({elapsed_ms:.2f}ms)"
    )
    print()


async def main() -> None:
    async with Client(mcp) as client:
        await traced_call(client, "save_note", {"title": "trace-demo", "body": "hello"})
        await traced_call(client, "list_notes", {})

        # Production-gear finding, confirmed by actually running this
        # (not assumed): calling a tool that doesn't exist comes back
        # exactly the same shape as a ValueError raised inside a real
        # tool -- result_type="complete", is_error=True -- not a raised
        # Python exception on the client and not a distinct "unknown
        # tool" shape. This matters for error handling: code that
        # branches on is_error already covers "tool doesn't exist" for
        # free, but code that only wraps calls in try/except would miss
        # both cases identically.
        await traced_call(client, "nonexistent_tool", {})


if __name__ == "__main__":
    asyncio.run(main())
