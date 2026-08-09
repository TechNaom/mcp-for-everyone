"""
Chapter 3 exercise: capture a real exchange and trace it by hand.

This reuses the Chapter 4 notes server. Fill in TODO 1-2, run this
script, then answer the questions in exercises/index.html using the
printed output — no guessing, trace what actually came back.
"""

import asyncio
import importlib.util
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


async def main() -> None:
    async with Client(mcp) as client:
        # TODO 1: Call `save_note` with title="lifecycle" and
        # body="tracing this by hand". Print the full result object
        # (not just result.content) — you need to see `structured_content`,
        # `result_type`, and `meta` to answer the exercises.

        # TODO 2: Call `list_notes` with no arguments. Print the full
        # result object again.

        pass


asyncio.run(main())
