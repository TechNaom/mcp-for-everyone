"""
Chapter 6 mini project: an MCP health-check probe.

A small script an ops team could actually run (or wire into a load
balancer health check) to verify a Streamable HTTP MCP server is up and
its tools are callable -- not just that the port is open.

Fill in the TODOs. See solution.py for a reference implementation.
"""

import asyncio
import sys

from mcp import Client


async def check_server(url: str) -> bool:
    """Return True if the server at `url` is reachable and at least one
    tool call succeeds. Never raises -- a health check that crashes is
    worse than useless."""
    # TODO 1: Connect a Client to `url`. If connecting raises an
    # exception, catch it, print a clear failure reason, and return
    # False -- don't let the exception propagate.

    # TODO 2: Call `list_tools()`. If the server has zero tools, treat
    # that as a failure too (a server with no tools is suspicious, not
    # healthy) -- print why and return False.

    # TODO 3 (production-gear): Call the first tool in the list with an
    # empty arguments dict `{}`. This will fail for most real tools
    # (wrong arguments) -- that's fine and expected. What you actually
    # want to confirm is that the server responded at all (didn't hang,
    # didn't crash the connection), regardless of whether the specific
    # call succeeded. Use `asyncio.wait_for` with a short timeout so a
    # hung server doesn't hang your health check forever.

    return False  # replace with your real result


async def main() -> None:
    url = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8767/mcp"
    healthy = await check_server(url)
    print("HEALTHY" if healthy else "UNHEALTHY")
    sys.exit(0 if healthy else 1)


asyncio.run(main())
