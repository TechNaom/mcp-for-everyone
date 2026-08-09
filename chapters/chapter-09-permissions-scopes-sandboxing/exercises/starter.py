"""
Chapter 9 exercises: extend the scope-checking pattern to the notes
server from Chapter 4, and add a scope-aware wrapper.

Fill in the TODOs. Run `python solution.py` for reference once stuck.
"""

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


# TODO 1: Add a `delete_note(title: str) -> str` tool requiring a NEW
# scope `notes:delete` -- distinct from `notes:write`, since deleting is
# a different (and arguably higher) risk than writing, per this
# chapter's senior interview question about scope taxonomy.


# TODO 2 (production-gear): Write `async def try_call(client, scopes,
# tool_name, arguments)` that sets current_scopes to the given scopes,
# calls the tool, resets current_scopes back to empty afterward (even if
# the call raises), and returns the result. Use try/finally to guarantee
# the reset happens.


# TODO 3 (production-gear): Using try_call, write a test that confirms a
# caller with `{"notes:write"}` scope can save a note but NOT delete it,
# and a caller with `{"notes:write", "notes:delete"}` can do both.


async def main() -> None:
    async with Client(mcp) as client:
        pass  # exercise your TODOs here


asyncio.run(main())
