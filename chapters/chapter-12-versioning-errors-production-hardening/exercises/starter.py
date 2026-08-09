"""
Chapter 12 exercises: confirm dual-era behavior yourself, and harden a
tool against a simulated dependency failure.

Fill in the TODOs. Run `python solution.py` for reference once stuck.
"""

import asyncio

from mcp.server import MCPServer
from mcp import Client

mcp = MCPServer("hardening-demo")

_SIMULATE_DB_DOWN = False


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


# TODO 1 (production-gear): Add a `fetch_user_count() -> int` tool that
# "queries a database" (just return a fixed number like 42). If
# `_SIMULATE_DB_DOWN` is True, raise a ValueError with a clear message
# instead of returning a value -- simulating a downstream dependency
# failure. This should NOT crash the server; a raised ValueError inside
# a tool becomes a normal is_error result, per every prior chapter.


async def confirm_dual_era() -> None:
    # TODO 2: Connect to `mcp` twice -- once with the default mode, once
    # with mode="legacy" -- and print client.protocol_version for each,
    # confirming they differ (2026-07-28 vs 2025-11-25).
    pass


async def confirm_validation_errors() -> None:
    # TODO 3 (production-gear): Call `add` with a missing argument, then
    # with a wrong-typed argument. Print whether each is_error, and the
    # error message. Confirm both come back as is_error=True, not a
    # raised client-side exception.
    pass


async def confirm_dependency_failure() -> None:
    # TODO 4 (production-gear): Set _SIMULATE_DB_DOWN to True (use
    # `global` inside this function), call fetch_user_count, confirm
    # is_error=True with a clear message, then set it back to False and
    # confirm a normal call succeeds.
    pass


async def main() -> None:
    await confirm_dual_era()
    async with Client(mcp) as client:
        await confirm_validation_errors()
        await confirm_dependency_failure()


if __name__ == "__main__":
    asyncio.run(main())
