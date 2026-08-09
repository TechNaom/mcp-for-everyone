"""
Chapter 4 exercises — extend the notes server.

Fill in the TODOs. Run `python solution.py` for reference once you're
stuck, but try each task first.
"""

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


# TODO 1: Add a `delete_note(title: str) -> str` tool that removes a note
# and returns a confirmation message. Raise ValueError if the title
# doesn't exist.


# TODO 2: Add a `search_notes(query: str) -> list[str]` tool that returns
# the titles of every note whose body contains `query` (case-insensitive).


# TODO 3 (production-gear): `save_note` currently accepts a body of any
# length. Add a limit (say, 10,000 characters) and raise ValueError with
# a clear message if it's exceeded. Real tool servers must defend against
# unbounded input — a model can be prompted to send arbitrarily large
# arguments.


# TODO 4 (production-gear): Add a `note_count() -> int` tool, and write a
# short comment explaining why you would (or wouldn't) expose this as a
# resource instead of a tool. There's a defensible answer either way —
# the point is to reason about it explicitly.


# TODO 5 (production-gear): `save_note("", "some body")` currently
# succeeds and creates a note with no name, which is impossible to
# reference again by title. Reject empty/whitespace-only titles with a
# clear ValueError.


# TODO 6: Add a `rename_note(old_title: str, new_title: str) -> str`
# tool. Decide what happens if `new_title` already exists.


if __name__ == "__main__":
    mcp.run(transport="stdio")
