"""Chapter 7 mini project — reference solution: a CLI host for the notes server."""

import asyncio
import importlib.util
import shlex
import sys
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


def parse_line(line: str) -> tuple[str, dict]:
    """Parse "tool_name key=\"value\" key2=value2" into (name, {key: value})."""
    parts = shlex.split(line)
    if not parts:
        return "", {}
    name = parts[0]
    args = {}
    for part in parts[1:]:
        if "=" not in part:
            continue
        key, _, value = part.partition("=")
        args[key] = value
    return name, args


class CLIHost:
    def __init__(self, client):
        self.client = client
        self.tools_by_name: dict = {}

    async def discover(self):
        result = await self.client.list_tools()
        self.tools_by_name = {t.name: t for t in result.tools}

    async def run_line(self, line: str) -> str:
        name, args = parse_line(line)
        if not name:
            return ""
        if name not in self.tools_by_name:
            return f"Unknown command '{name}'. Known: {list(self.tools_by_name)}"

        result = await self.client.call_tool(name, args)
        if result.is_error:
            return f"Error: {result.content[0].text}"
        return str(result.structured_content)


async def main() -> None:
    mod = _load_chapter_4_module()
    async with Client(mod.mcp) as client:
        host = CLIHost(client)
        await host.discover()
        print(f"Ready. Known commands: {list(host.tools_by_name)}")

        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            if line == "quit":
                break
            output = await host.run_line(line)
            if output:
                print(output)


if __name__ == "__main__":
    asyncio.run(main())
