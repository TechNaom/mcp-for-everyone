"""Chapter 11 exercises — reference solution."""

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
    logger.info(json.dumps({"event": event, "ts": time.time(), **fields}))


@mcp.tool()
def save_note(ctx: Context, title: str, body: str) -> str:
    """Save a note under a title."""
    meta = ctx.request_context.meta or {}
    trace_id = meta.get("traceparent", "no-trace")
    start = time.monotonic()

    log_structured(
        "tool_call_start", tool="save_note", request_id=ctx.request_id, trace_id=trace_id
    )
    _NOTES[title] = body
    elapsed_ms = (time.monotonic() - start) * 1000
    log_structured(
        "tool_call_end", tool="save_note", request_id=ctx.request_id,
        trace_id=trace_id, elapsed_ms=round(elapsed_ms, 2), is_error=False,
    )
    return f"Saved '{title}'."


@mcp.tool()
def list_notes() -> list[str]:
    """List note titles."""
    return list(_NOTES.keys())


@mcp.tool()
def delete_note(ctx: Context, title: str) -> str:
    """Delete a note by title."""
    meta = ctx.request_context.meta or {}
    trace_id = meta.get("traceparent", "no-trace")
    start = time.monotonic()

    log_structured(
        "tool_call_start", tool="delete_note", request_id=ctx.request_id, trace_id=trace_id
    )

    if title not in _NOTES:
        elapsed_ms = (time.monotonic() - start) * 1000
        log_structured(
            "tool_call_end", tool="delete_note", request_id=ctx.request_id,
            trace_id=trace_id, elapsed_ms=round(elapsed_ms, 2),
            is_error=True, reason=f"no note titled '{title}'",
        )
        raise ValueError(f"No note titled '{title}'")

    del _NOTES[title]
    elapsed_ms = (time.monotonic() - start) * 1000
    log_structured(
        "tool_call_end", tool="delete_note", request_id=ctx.request_id,
        trace_id=trace_id, elapsed_ms=round(elapsed_ms, 2), is_error=False,
    )
    return f"Deleted '{title}'."


def find_calls_for_trace(log_lines: list[str], trace_id: str) -> list[dict]:
    """Given raw JSON log lines, return only those matching trace_id."""
    matches = []
    for line in log_lines:
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            continue
        if record.get("trace_id") == trace_id:
            matches.append(record)
    return matches


async def main() -> None:
    async with Client(mcp) as client:
        trace_id = "trace-exercise-1"
        await client.call_tool(
            "save_note", {"title": "t", "body": "x"}, meta={"traceparent": trace_id}
        )
        await client.call_tool("list_notes", {}, meta={"traceparent": trace_id})

        other_trace = "trace-other"
        await client.call_tool(
            "save_note", {"title": "u", "body": "y"}, meta={"traceparent": other_trace}
        )

        # Simulate reading back the log and filtering to one trace
        sample_logs = [
            json.dumps({"event": "tool_call_start", "trace_id": trace_id, "tool": "save_note"}),
            json.dumps({"event": "tool_call_end", "trace_id": trace_id, "tool": "save_note"}),
            json.dumps({"event": "tool_call_start", "trace_id": other_trace, "tool": "save_note"}),
        ]
        matches = find_calls_for_trace(sample_logs, trace_id)
        print(f"Found {len(matches)} log lines for trace '{trace_id}':")
        for m in matches:
            print(" ", m)


if __name__ == "__main__":
    asyncio.run(main())
