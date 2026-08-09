"""
Chapter 4 mini project: a bookmarks MCP server.

Build a server that manages bookmarks (url + title + tags), backed by a
JSON file so it survives restarts — the one limitation of the lesson's
in-memory notes server, deliberately left for you to fix here.

Fill in the TODOs. See solution.py for a reference implementation.
"""

import json
from pathlib import Path

from mcp.server import MCPServer

mcp = MCPServer("bookmarks")

_STORE_PATH = Path(__file__).parent / "bookmarks.json"


def _load() -> dict[str, dict]:
    if _STORE_PATH.exists():
        return json.loads(_STORE_PATH.read_text())
    return {}


def _save(data: dict[str, dict]) -> None:
    _STORE_PATH.write_text(json.dumps(data, indent=2))


# TODO 1: Implement `add_bookmark(url: str, title: str, tags: list[str]) -> str`
# as a tool. Load the store, add/overwrite the entry keyed by url, save
# the store, return a confirmation message.


# TODO 2: Implement `list_bookmarks(tag: str | None = None) -> list[str]`
# as a tool. If `tag` is given, only return URLs whose bookmark includes
# that tag. Otherwise return all URLs.


# TODO 3: Implement a `bookmark://{encoded_url}` resource that returns
# the title and tags for a given URL as a formatted string. Raise
# ValueError if the URL isn't bookmarked.
#
# Gotcha: a bare URL contains "://", which breaks MCP's own URI template
# matching (the template parser treats "://" as a scheme delimiter, not
# literal characters to capture). Percent-encode the URL when building
# the resource URI (`urllib.parse.quote(url, safe="")`) and decode it
# inside the resource function (`urllib.parse.unquote`).


# TODO 4 (production-gear): What happens if two clients call add_bookmark
# at nearly the same time? Add a comment describing the race condition in
# `_load`/`_save`, and what you'd change before running this with more
# than one concurrent user (you don't have to implement the fix).


if __name__ == "__main__":
    mcp.run(transport="stdio")
