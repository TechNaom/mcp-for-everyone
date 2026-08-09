"""Chapter 7 exercises — reference solution."""

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
    def __init__(self, client):
        self.client = client
        self.tools_by_name: dict = {}

    async def discover(self):
        result = await self.client.list_tools()
        self.tools_by_name = {t.name: t for t in result.tools}
        return list(self.tools_by_name.keys())

    def known_tool_count(self) -> int:
        return len(self.tools_by_name)

    async def handle(self, command: str) -> str:
        return await self.handle_with_args(command, {})

    async def handle_with_args(self, command: str, arguments: dict) -> str:
        if self.known_tool_count() == 0:
            return "Host has no discovered tools yet -- call discover() first."
        if command not in self.tools_by_name:
            return f"I don't know how to '{command}' -- available: {list(self.tools_by_name)}"
        result = await self.client.call_tool(command, arguments)
        if result.is_error:
            return f"Tool '{command}' failed: {result.content[0].text}"
        return str(result.structured_content)


async def main() -> None:
    mod = _load_chapter_4_module()
    async with Client(mod.mcp) as client:
        host = ToyHost(client)
        await host.discover()

        print(await host.handle_with_args("save_note", {"title": "t", "body": "hello"}))
        print(await host.handle("list_notes"))
        print(await host.handle("list_note"))  # typo -- exercise 3


asyncio.run(main())
