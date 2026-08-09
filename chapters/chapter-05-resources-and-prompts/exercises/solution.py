"""Chapter 5 exercises — reference solution."""

import asyncio

from mcp.server import MCPServer

mcp = MCPServer("notes")

_NOTES: dict[str, str] = {}


@mcp.tool()
def save_note(title: str, body: str) -> str:
    """Save a note under a title. Overwrites any existing note with the same title."""
    _NOTES[title] = body
    return f"Saved note '{title}' ({len(body)} characters)."


@mcp.tool()
def list_notes() -> list[str]:
    """List the titles of every saved note."""
    return list(_NOTES.keys())


@mcp.resource("note://{title}")
def read_note(title: str) -> str:
    """Read the full body of a saved note by title."""
    if title not in _NOTES:
        raise ValueError(f"No note titled '{title}'")
    return _NOTES[title]


@mcp.resource("stats://notes")
def note_stats() -> str:
    """Static resource: a summary of how many notes exist and their total size."""
    total_chars = sum(len(body) for body in _NOTES.values())
    return f"{len(_NOTES)} notes, {total_chars} total characters"


@mcp.prompt()
def summarize_note(title: str) -> str:
    """Ask the model to summarize a saved note in one sentence."""
    return f"Summarize the note titled '{title}' in one sentence."


async def _discovery_check() -> None:
    from mcp import Client

    async with Client(mcp) as client:
        resources = await client.list_resources()
        templates = await client.list_resource_templates()
        print("STATIC RESOURCES:", [r.uri for r in resources.resources])
        print(
            "TEMPLATED RESOURCES:",
            [t.uri_template for t in templates.resource_templates],
        )


if __name__ == "__main__":
    import sys

    if "--check-discovery" in sys.argv:
        asyncio.run(_discovery_check())
    else:
        mcp.run(transport="stdio")
