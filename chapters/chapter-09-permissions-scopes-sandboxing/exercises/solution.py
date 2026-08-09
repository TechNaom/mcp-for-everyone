"""Chapter 9 exercises — reference solution."""

import asyncio
import functools
from contextvars import ContextVar

from mcp.server import MCPServer
from mcp import Client

current_scopes: ContextVar[frozenset[str]] = ContextVar(
    "current_scopes", default=frozenset()
)


def require_scope(scope: str):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            if scope not in current_scopes.get():
                raise PermissionError(f"missing required scope '{scope}'")
            return fn(*args, **kwargs)

        wrapper._required_scope = scope  # lets Chapter 9's audit project introspect this
        return wrapper

    return decorator


mcp = MCPServer("scoped-notes")
_NOTES: dict[str, str] = {}


@mcp.tool()
@require_scope("notes:write")
def save_note(title: str, body: str) -> str:
    """Save a note under a title."""
    _NOTES[title] = body
    return f"Saved note '{title}'."


@mcp.tool()
@require_scope("notes:read")
def list_notes() -> list[str]:
    """List note titles."""
    return list(_NOTES.keys())


@mcp.tool()
@require_scope("notes:delete")
def delete_note(title: str) -> str:
    """Delete a note by title. Requires a separate, higher-risk scope
    from notes:write -- writing and deleting are not the same risk."""
    _NOTES.pop(title, None)
    return f"Deleted '{title}'."


async def try_call(client: "Client", scopes: frozenset[str], tool_name: str, arguments: dict):
    token = current_scopes.set(scopes)
    try:
        return await client.call_tool(tool_name, arguments)
    finally:
        current_scopes.reset(token)


async def main() -> None:
    async with Client(mcp) as client:
        write_only = frozenset({"notes:write"})
        write_and_delete = frozenset({"notes:write", "notes:delete"})

        r1 = await try_call(client, write_only, "save_note", {"title": "t", "body": "x"})
        print("write-only, save_note ->", r1.is_error, r1.structured_content)

        r2 = await try_call(client, write_only, "delete_note", {"title": "t"})
        print("write-only, delete_note ->", r2.is_error, r2.content[0].text)

        r3 = await try_call(client, write_and_delete, "delete_note", {"title": "t"})
        print("write+delete, delete_note ->", r3.is_error, r3.structured_content)


if __name__ == "__main__":
    asyncio.run(main())
