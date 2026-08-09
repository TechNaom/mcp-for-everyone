"""Chapter 3 exercise — reference solution."""

import asyncio
import importlib.util
from pathlib import Path

from mcp import Client


def _load_chapter_4_module():
    """Load Chapter 4's notes-server solution by explicit file path.

    Both this file and Chapter 4's are named solution.py -- a plain
    sys.path + `import solution` trick resolves inconsistently depending
    on how this file itself is invoked (works when run as `python
    solution.py` directly, breaks under `python -c "import solution"` or
    when a test runner imports this file by name, due to a circular
    self-import). Loading by explicit path avoids the collision entirely.
    """
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
