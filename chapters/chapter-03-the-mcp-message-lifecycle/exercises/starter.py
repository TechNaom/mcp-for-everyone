"""
Chapter 3 exercise: capture a real exchange and trace it by hand.

This reuses the Chapter 4 notes server. Fill in TODO 1-2, run this
script, then answer the questions in exercises/index.html using the
printed output — no guessing, trace what actually came back.
"""

import asyncio
import sys
from pathlib import Path

# Reuse the Chapter 4 solution server instead of duplicating it.
sys.path.insert(
    0, str(Path(__file__).parents[2] / "chapter-04-your-first-mcp-server" / "exercises")
)
from solution import mcp  # noqa: E402  (import after sys.path edit, intentional)

from mcp import Client


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
