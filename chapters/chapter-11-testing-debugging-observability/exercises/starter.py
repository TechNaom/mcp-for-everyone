"""
Chapter 11 exercises: add structured, trace-correlated logging to the
notes server, and use it to answer a "what happened" question.

Fill in the TODOs. Run `python solution.py` for reference once stuck.
"""

import asyncio
import json
import logging
import time

from mcp.server import MCPServer
from mcp.server.mcpserver import Context
from mcp import Client

logger = logging.getLogger("ch11-exercises")
logging.basicConfig(level=logging.INFO, format="%(message)s")

mcp = MCPServer("observable-notes")
_NOTES: dict[str, str] = {}


def log_structured(event: str, **fields) -> None:
    """Emit one structured JSON log line."""
    logger.info(json.dumps({"event": event, "ts": time.time(), **fields}))


# TODO 1: Add Context to save_note's signature (as the first parameter,
# type-annotated `ctx: Context`) and log a "tool_call_start" event
# before saving and a "tool_call_end" event after, including
# request_id, trace_id (from ctx.request_context.meta, default
# "no-trace" if absent), and elapsed_ms.
@mcp.tool()
def save_note(title: str, body: str) -> str:
    """Save a note under a title."""
    _NOTES[title] = body
    return f"Saved '{title}'."


@mcp.tool()
def list_notes() -> list[str]:
    """List note titles."""
    return list(_NOTES.keys())


# TODO 2 (production-gear): Do the same for delete_note -- add Context,
# log start/end -- but this time, if the title doesn't exist, log an
# "tool_call_end" event with is_error=True and a reason, BEFORE raising
# the ValueError. This way even a failed call leaves a log trail.
@mcp.tool()
def delete_note(title: str) -> str:
    """Delete a note by title."""
    if title not in _NOTES:
        raise ValueError(f"No note titled '{title}'")
    del _NOTES[title]
    return f"Deleted '{title}'."


# TODO 3 (production-gear): Write a small "log analysis" function
# `find_calls_for_trace(log_lines: list[str], trace_id: str) -> list[dict]`
# that parses a list of JSON log lines (each a string) and returns only
# the ones matching the given trace_id -- simulating the debugging
# workflow from the lesson: given a trace ID, find every log line for it.


async def main() -> None:
    async with Client(mcp) as client:
        trace_id = "trace-exercise-1"
        await client.call_tool(
            "save_note", {"title": "t", "body": "x"}, meta={"traceparent": trace_id}
        )
        await client.call_tool("list_notes", {}, meta={"traceparent": trace_id})


if __name__ == "__main__":
    asyncio.run(main())
