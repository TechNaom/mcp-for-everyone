"""Chapter 8 exercises — reference solution."""

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
    tools_a = await client_a.list_tools()
    tools_b = await client_b.list_tools()
    merged = {}
    for t in tools_a.tools:
        merged[t.name] = ("notes-service", t)
    for t in tools_b.tools:
        merged[t.name] = ("docs-service", t)
    return merged


async def namespaced_merge(client_a: "Client", client_b: "Client") -> dict:
    tools_a = await client_a.list_tools()
    tools_b = await client_b.list_tools()
    merged = {}
    for t in tools_a.tools:
        merged[f"notes-service.{t.name}"] = ("notes-service", t)
    for t in tools_b.tools:
        merged[f"docs-service.{t.name}"] = ("docs-service", t)
    return merged


async def call_namespaced(catalog, clients_by_namespace, namespaced_name, arguments):
    if namespaced_name not in catalog:
        raise ValueError(f"Unknown tool '{namespaced_name}'")
    namespace, _, tool_name = namespaced_name.partition(".")
    client = clients_by_namespace[namespace]
    return await client.call_tool(tool_name, arguments)


async def assert_no_collisions(client_a: "Client", client_b: "Client") -> None:
    tools_a = await client_a.list_tools()
    tools_b = await client_b.list_tools()
    naive = await naive_merge(client_a, client_b)
    expected = len(tools_a.tools) + len(tools_b.tools)
    if len(naive) != expected:
        raise AssertionError(
            f"Tool-name collision detected: naive merge has {len(naive)} "
            f"entries but source catalogs have {expected} tools total. "
            f"Some tool names were silently dropped."
        )


async def main() -> None:
    async with Client(server_a) as client_a, Client(server_b) as client_b:
        naive = await naive_merge(client_a, client_b)
        print("Naive merge (buggy):", {k: v[0] for k, v in naive.items()})

        namespaced = await namespaced_merge(client_a, client_b)
        print("Namespaced merge:", list(namespaced.keys()))

        clients_by_namespace = {"notes-service": client_a, "docs-service": client_b}
        result_a = await call_namespaced(
            namespaced, clients_by_namespace, "notes-service.search", {"query": "milk"}
        )
        result_b = await call_namespaced(
            namespaced, clients_by_namespace, "docs-service.search", {"query": "milk"}
        )
        print("notes-service.search ->", result_a.structured_content)
        print("docs-service.search ->", result_b.structured_content)

        try:
            await assert_no_collisions(client_a, client_b)
            print("No collisions detected (unexpected!)")
        except AssertionError as exc:
            print(f"Collision test caught it: {exc}")


asyncio.run(main())
