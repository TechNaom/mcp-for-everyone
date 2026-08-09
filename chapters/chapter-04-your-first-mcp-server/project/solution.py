"""Chapter 4 mini project — reference solution: a bookmarks MCP server."""

import json
from pathlib import Path
from urllib.parse import quote, unquote

from mcp.server import MCPServer

mcp = MCPServer("bookmarks")

_STORE_PATH = Path(__file__).parent / "bookmarks.json"


def _load() -> dict[str, dict]:
    if _STORE_PATH.exists():
        return json.loads(_STORE_PATH.read_text())
    return {}


def _save(data: dict[str, dict]) -> None:
    _STORE_PATH.write_text(json.dumps(data, indent=2))


@mcp.tool()
def add_bookmark(url: str, title: str, tags: list[str]) -> str:
    """Save a bookmark. Overwrites any existing bookmark for the same URL."""
    data = _load()
    data[url] = {"title": title, "tags": tags}
    _save(data)
    return f"Saved bookmark for '{title}' ({url})."


@mcp.tool()
def list_bookmarks(tag: str | None = None) -> list[str]:
    """List bookmarked URLs, optionally filtered to a single tag."""
    data = _load()
    if tag is None:
        return list(data.keys())
    return [url for url, entry in data.items() if tag in entry["tags"]]


@mcp.resource("bookmark://{encoded_url}")
def read_bookmark(encoded_url: str) -> str:
    """Read a bookmark's title and tags by URL.

    The URL is percent-encoded in the resource URI (`quote(url, safe="")`)
    because a bare URL contains `://`, which breaks MCP's own URI template
    matching — the template parser treats `://` as a scheme delimiter, not
    literal characters to capture. This bit us during testing: a naive
    `bookmark://{url}` template silently fails to match a real URL. Always
    encode any parameter that might itself contain URI-reserved characters.
    """
    url = unquote(encoded_url)
    data = _load()
    if url not in data:
        raise ValueError(f"No bookmark for '{url}'")
    entry = data[url]
    return f"{entry['title']} — tags: {', '.join(entry['tags']) or 'none'}"


def bookmark_resource_uri(url: str) -> str:
    """Build the correctly-encoded resource URI for a given bookmark URL."""
    return f"bookmark://{quote(url, safe='')}"


# Production-gear note (TODO 4): `_load` then `_save` is a read-modify-write
# with no locking. Two concurrent `add_bookmark` calls can race: both read
# the same on-disk state, both write, and the second write silently
# clobbers the first bookmark's addition. A JSON file with no locking is
# fine for one user on one laptop (this project's actual scope) but would
# need a real datastore with atomic writes, or at minimum a file lock,
# before more than one client could safely use it concurrently.


if __name__ == "__main__":
    mcp.run(transport="stdio")
