"""Chapter 6 mini project — reference solution: an MCP health-check probe."""

import asyncio
import sys

from mcp import Client

_CALL_TIMEOUT_SECONDS = 3.0


async def check_server(url: str) -> bool:
    """Return True if the server at `url` is reachable and responsive.
    Never raises -- a health check that crashes is worse than useless."""
    try:
        async with Client(url) as client:
            tools = await client.list_tools()

            if not tools.tools:
                print(f"UNHEALTHY: {url} has zero tools registered")
                return False

            first_tool = tools.tools[0].name
            try:
                await asyncio.wait_for(
                    client.call_tool(first_tool, {}), timeout=_CALL_TIMEOUT_SECONDS
                )
                # A call that returns at all -- success or a clean
                # is_error=True -- proves the server is alive and
                # processing requests. We don't care whether the empty
                # arguments were valid for this particular tool.
            except asyncio.TimeoutError:
                print(f"UNHEALTHY: {url} did not respond within {_CALL_TIMEOUT_SECONDS}s")
                return False

            return True

    except Exception as exc:  # noqa: BLE001 -- health checks must not raise
        print(f"UNHEALTHY: could not connect to {url}: {type(exc).__name__}: {exc}")
        return False


async def main() -> None:
    url = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8767/mcp"
    healthy = await check_server(url)
    print("HEALTHY" if healthy else "UNHEALTHY")
    sys.exit(0 if healthy else 1)


asyncio.run(main())
