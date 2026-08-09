"""
Chapter 8 exercises: reproduce the tool-name collision, then fix it
with namespacing and routing.

Fill in the TODOs. Run `python solution.py` for reference once stuck.
"""

import asyncio

from mcp.server import MCPServer
from mcp import Client

server_a = MCPServer("notes-service")


@server_a.tool()
def search(query: str) -> list[str]:
    """Search notes for a query."""
    return [f"note-match-for-{query}"]


server_b = MCPServer("docs-service")


@server_b.tool()
def search(query: str) -> list[str]:
    """Search documentation for a query."""
    return [f"doc-match-for-{query}"]


async def naive_merge(client_a: "Client", client_b: "Client") -> dict:
    """Reproduce the collision: a plain dict-by-name merge."""
    tools_a = await client_a.list_tools()
    tools_b = await client_b.list_tools()
    merged = {}
    for t in tools_a.tools:
        merged[t.name] = ("notes-service", t)
    for t in tools_b.tools:
        merged[t.name] = ("docs-service", t)
    return merged


# TODO 1: Write `namespaced_merge(client_a, client_b)` that returns a
# dict keyed by "server-name.tool-name" instead, so both tools survive.
# Return the same (namespace, tool) tuple values as naive_merge.


# TODO 2: Write `async def call_namespaced(catalog, clients_by_namespace,
# namespaced_name, arguments)` that splits the namespace off the tool
# name, looks up the right client, and calls the real tool. Return the
# call_tool result.


# TODO 3 (production-gear): Write `assert_no_collisions(client_a,
# client_b)` that raises an AssertionError with a clear message if the
# naive merge would have dropped any tools (compare its length against
# the sum of each source catalog's length).


async def main() -> None:
    async with Client(server_a) as client_a, Client(server_b) as client_b:
        naive = await naive_merge(client_a, client_b)
        print("Naive merge (buggy):", {k: v[0] for k, v in naive.items()})

        # Exercise your TODOs here once implemented.


if __name__ == "__main__":
    asyncio.run(main())
