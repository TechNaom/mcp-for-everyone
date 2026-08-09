"""
Chapter 7 mini project: a command-line host for the notes server.

Reads commands from stdin, one per line, in the form:
    save_note title="todo" body="buy milk"
    list_notes
    delete_note title="todo"

and dispatches them to the real notes server using the ToyHost pattern
from the lesson. Type "quit" to exit.

Fill in the TODOs. See solution.py for a reference implementation.
"""

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
        # TODO 1: Parse the line with parse_line(). If the tool name
        # isn't in self.tools_by_name, return a clear "unknown command"
        # message listing what IS available.

        # TODO 2: Call the tool with the parsed arguments. Check
        # is_error (same discipline as every prior chapter) and return
        # either the error text or the structured content, as a string.

        return "not implemented"


async def main() -> None:
    mod = _load_chapter_4_module()
    async with Client(mod.mcp) as client:
        host = CLIHost(client)
        await host.discover()
        print(f"Ready. Known commands: {list(host.tools_by_name)}")

        # TODO 3: Read lines from stdin in a loop (`for line in
        # sys.stdin:` works fine here -- this is a CLI tool, not a
        # server juggling concurrent connections). Stop on "quit".
        # Print the result of each command via host.run_line().


asyncio.run(main())
