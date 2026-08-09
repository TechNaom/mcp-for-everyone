"""Chapter 8 mini project — reference solution: a two-server CLI host."""

import asyncio
import importlib.util
import shlex
import sys
from pathlib import Path

from mcp import Client


def _load_module(relative_path: str, module_name: str):
    full_path = Path(__file__).parents[2] / relative_path
    spec = importlib.util.spec_from_file_location(module_name, full_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def parse_line(line: str) -> tuple[str, dict]:
    """Parse "tool key=value key2=[a,b,c]" -- bracketed values become
    lists, since some tools (like add_bookmark's `tags`) require one and
    a naive string-only parser can't satisfy that schema."""
    parts = shlex.split(line)
    if not parts:
        return "", {}
    args = {}
    for part in parts[1:]:
        if "=" not in part:
            continue
        key, _, value = part.partition("=")
        if value.startswith("[") and value.endswith("]"):
            value = [v.strip() for v in value[1:-1].split(",") if v.strip()]
        args[key] = value
    return parts[0], args


class MultiServerHost:
    def __init__(self):
        self.catalog: dict = {}  # "namespace.tool" -> (namespace, tool)
        self.clients_by_namespace: dict = {}

    async def connect(self, namespace: str, client: "Client") -> None:
        self.clients_by_namespace[namespace] = client
        tools = await client.list_tools()
        for t in tools.tools:
            self.catalog[f"{namespace}.{t.name}"] = (namespace, t)

    async def run_line(self, line: str) -> str:
        command, args = parse_line(line)
        if not command:
            return ""
        if command not in self.catalog:
            return f"Unknown command '{command}'. Known: {list(self.catalog)}"

        namespace, _, tool_name = command.partition(".")
        client = self.clients_by_namespace[namespace]
        result = await client.call_tool(tool_name, args)
        if result.is_error:
            return f"Error: {result.content[0].text}"
        return str(result.structured_content)


async def main() -> None:
    notes_mod = _load_module(
        "chapter-04-your-first-mcp-server/exercises/solution.py", "ch4_notes"
    )
    bookmarks_mod = _load_module(
        "chapter-04-your-first-mcp-server/project/solution.py", "ch4_bookmarks"
    )

    async with Client(notes_mod.mcp) as notes_client, Client(
        bookmarks_mod.mcp
    ) as bookmarks_client:
        host = MultiServerHost()
        await host.connect("notes", notes_client)
        await host.connect("bookmarks", bookmarks_client)
        print(f"Ready. Known commands: {list(host.catalog)}")

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
