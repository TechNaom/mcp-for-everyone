"""Chapter 12 exercises — reference solution."""

import asyncio

from mcp.server import MCPServer
from mcp import Client

mcp = MCPServer("hardening-demo")

_SIMULATE_DB_DOWN = False


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


@mcp.tool()
def fetch_user_count() -> int:
    """Query the (simulated) database for a user count."""
    if _SIMULATE_DB_DOWN:
        raise ValueError("database connection failed: could not reach db host")
    return 42


async def confirm_dual_era() -> None:
    async with Client(mcp, mode="auto") as client:
        print("auto mode protocol_version:", client.protocol_version)
    async with Client(mcp, mode="legacy") as client:
        print("legacy mode protocol_version:", client.protocol_version)


async def confirm_validation_errors() -> None:
    async with Client(mcp) as client:
        r1 = await client.call_tool("add", {"a": 1})
        print("missing arg -> is_error:", r1.is_error)

        r2 = await client.call_tool("add", {"a": "nope", "b": 2})
        print("wrong type -> is_error:", r2.is_error)


async def confirm_dependency_failure() -> None:
    global _SIMULATE_DB_DOWN

    async with Client(mcp) as client:
        _SIMULATE_DB_DOWN = True
        r1 = await client.call_tool("fetch_user_count", {})
        print("db down -> is_error:", r1.is_error, r1.content[0].text)

        _SIMULATE_DB_DOWN = False
        r2 = await client.call_tool("fetch_user_count", {})
        print("db up -> is_error:", r2.is_error, r2.structured_content)


async def main() -> None:
    await confirm_dual_era()
    await confirm_validation_errors()
    await confirm_dependency_failure()


if __name__ == "__main__":
    asyncio.run(main())
