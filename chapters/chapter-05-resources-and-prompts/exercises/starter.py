"""
Chapter 5 exercises: add a static resource and a prompt to the notes
server from Chapter 4.

Fill in the TODOs. Run `python solution.py` for reference once stuck.
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


# TODO 1: Add a static resource `stats://notes` that returns a short
# summary string like "3 notes, 42 total characters" -- no parameters,
# fixed URI.


# TODO 2: Add a prompt `summarize_note(title: str) -> str` that returns
# a string asking the model to summarize the named note's contents in
# one sentence. Don't fetch the note's body yourself inside the prompt --
# a prompt returns instruction text, it doesn't execute logic against
# your data (that's what a tool or resource is for).


# TODO 3 (production-gear): Write a small discovery check -- call both
# `list_resources()` and `list_resource_templates()` against this server
# and print both lists. Confirm your static resource appears in one and
# your templated resource appears in the other, never both.


if __name__ == "__main__":
    mcp.run(transport="stdio")
