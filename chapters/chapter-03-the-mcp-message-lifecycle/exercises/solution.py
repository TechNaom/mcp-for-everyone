"""Chapter 3 exercise — reference solution."""

import asyncio
import sys
from pathlib import Path

sys.path.insert(
    0, str(Path(__file__).parents[2] / "chapter-04-your-first-mcp-server" / "exercises")
)
from solution import mcp  # noqa: E402

from mcp import Client


async def main() -> None:
    async with Client(mcp) as client:
        save_result = await client.call_tool(
            "save_note", {"title": "lifecycle", "body": "tracing this by hand"}
        )
        print("=== save_note result ===")
        print("result_type:", save_result.result_type)
        print("is_error:", save_result.is_error)
        print("structured_content:", save_result.structured_content)
        print("meta:", save_result.meta)
        print()

        list_result = await client.call_tool("list_notes", {})
        print("=== list_notes result ===")
        print("result_type:", list_result.result_type)
        print("structured_content:", list_result.structured_content)
        print("meta:", list_result.meta)


asyncio.run(main())
