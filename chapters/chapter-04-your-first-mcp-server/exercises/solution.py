"""Chapter 4 exercises — reference solution."""

from mcp.server import MCPServer

mcp = MCPServer("notes")

_NOTES: dict[str, str] = {}
_MAX_BODY_LENGTH = 10_000


@mcp.tool()
def save_note(title: str, body: str) -> str:
    """Save a note under a title. Overwrites any existing note with the same title."""
    if not title.strip():
        raise ValueError("Note title cannot be empty.")
    if len(body) > _MAX_BODY_LENGTH:
        raise ValueError(
            f"Note body too long ({len(body)} chars, max {_MAX_BODY_LENGTH})."
        )
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


@mcp.tool()
def delete_note(title: str) -> str:
    """Delete a note by title."""
    if title not in _NOTES:
        raise ValueError(f"No note titled '{title}'")
    del _NOTES[title]
    return f"Deleted note '{title}'."


@mcp.tool()
def search_notes(query: str) -> list[str]:
    """Return the titles of notes whose body contains the query (case-insensitive)."""
    needle = query.lower()
    return [title for title, body in _NOTES.items() if needle in body.lower()]


@mcp.tool()
def note_count() -> int:
    """Return how many notes are currently saved.

    Modeled as a tool, not a resource: resources are addressed by a fixed
    or templated URI representing a piece of data a client already knows
    it wants to read (e.g. `note://todo`). A count is a computed summary
    with no natural URI of its own, and callers reach for it as an
    action ("how many do I have?") rather than a document to load into
    context — that reads more naturally as a tool call.
    """
    return len(_NOTES)


@mcp.tool()
def rename_note(old_title: str, new_title: str) -> str:
    """Rename a note. Refuses to overwrite an existing note at the new title."""
    if old_title not in _NOTES:
        raise ValueError(f"No note titled '{old_title}'")
    if new_title in _NOTES:
        raise ValueError(
            f"A note titled '{new_title}' already exists; refusing to overwrite it."
        )
    _NOTES[new_title] = _NOTES.pop(old_title)
    return f"Renamed '{old_title}' to '{new_title}'."


if __name__ == "__main__":
    mcp.run(transport="stdio")
