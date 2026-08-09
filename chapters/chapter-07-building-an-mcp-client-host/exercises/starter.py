"""
Chapter 7 exercises: extend ToyHost with argument-taking commands and
proper validation.

Fill in the TODOs. Run `python solution.py` for reference once stuck.
"""

import asyncio
import importlib.util
from pathlib import Path

from mcp import Client


def _load_chapter_4_module():
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


class ToyHost:
    """See lesson.html for the full docstring on why this uses keyword
    matching instead of a real LLM."""

    def __init__(self, client):
        self.client = client
        self.tools_by_name: dict = {}

    async def discover(self):
        result = await self.client.list_tools()
        self.tools_by_name = {t.name: t for t in result.tools}
        return list(self.tools_by_name.keys())

    async def handle(self, command: str) -> str:
        if command not in self.tools_by_name:
            return f"I don't know how to '{command}' -- available: {list(self.tools_by_name)}"
        result = await self.client.call_tool(command, {})
        if result.is_error:
            return f"Tool '{command}' failed: {result.content[0].text}"
        return str(result.structured_content)


# TODO 1: Add a `handle_with_args(self, command: str, arguments: dict) -> str`
# method to ToyHost that works like `handle` but passes `arguments`
# through to `call_tool` instead of an empty dict. `handle` should still
# work for zero-argument tools.


# TODO 2 (production-gear): Add a `known_tool_count(self) -> int` method
# and a corresponding check in `handle_with_args` that refuses to call
# any tool if `discover()` hasn't been called yet (self.tools_by_name is
# empty) -- return a clear message instead of a confusing KeyError-style
# failure.


# TODO 3 (production-gear): Write a small test that calls `handle` with
# a command containing a typo (e.g. "list_note" instead of "list_notes")
# and confirms the host's response is a clear, actionable message -- not
# a raw exception traceback.


async def main() -> None:
    mod = _load_chapter_4_module()
    async with Client(mod.mcp) as client:
        host = ToyHost(client)
        await host.discover()
        # Exercise your new methods here.


asyncio.run(main())
