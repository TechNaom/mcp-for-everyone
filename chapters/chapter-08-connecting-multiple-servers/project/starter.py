"""
Chapter 8 mini project: extend Chapter 7's CLI host to connect to TWO
real servers at once (notes + bookmarks from Chapter 4), using the
namespaced-merge pattern from this chapter.

Commands now look like: notes.save_note title="x" body="y"
                         bookmarks.add_bookmark url="..." title="..." tags="mcp"

Fill in the TODOs. See solution.py for a reference implementation.
"""

import asyncio
import importlib.util
import shlex
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

    # TODO 1: Implement `async def connect(self, namespace: str, client)`.
    # Stores the client under `namespace`, calls `list_tools()`, and adds
    # every tool to self.catalog under the key f"{namespace}.{tool.name}".

    # TODO 2: Implement `async def run_line(self, line: str) -> str`.
    # Parse the line, look up the full "namespace.tool" key in
    # self.catalog (the command IS the namespaced name here, e.g.
    # "notes.save_note"), route to the right client, check is_error,
    # and return a result string -- same discipline as Chapter 7.


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
        # TODO 3: Connect both clients under namespaces "notes" and
        # "bookmarks", then print the full merged catalog's keys.
        pass


asyncio.run(main())
