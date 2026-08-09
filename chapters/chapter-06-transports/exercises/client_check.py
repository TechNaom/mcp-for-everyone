"""
Companion client for exercises/solution.py -- run the server first in
one terminal, then run this in another to exercise it over the network.

    python solution.py              # terminal 1
    python client_check.py          # terminal 2, port 8767

    python solution.py --stateless  # terminal 1
    python client_check.py --stateless   # terminal 2, port 8768
"""

import asyncio
import sys

from mcp import Client


async def main() -> None:
    port = 8768 if "--stateless" in sys.argv else 8767
    async with Client(f"http://127.0.0.1:{port}/mcp") as client:
        tools = await client.list_tools()
        print("TOOLS:", [t.name for t in tools.tools])
        result = await client.call_tool(
            "save_note", {"title": "http-demo", "body": "reached over the network"}
        )
        print("RESULT:", result.structured_content)


asyncio.run(main())
