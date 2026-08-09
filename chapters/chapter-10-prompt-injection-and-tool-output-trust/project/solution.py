"""Chapter 10 mini project — reference solution: a tool-output firewall."""

import asyncio
import importlib.util
import time
from dataclasses import dataclass, field
from pathlib import Path

from mcp import Client


def _load_exercises_module():
    ex_path = Path(__file__).parents[1] / "exercises" / "solution.py"
    spec = importlib.util.spec_from_file_location("ch10_exercises", ex_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@dataclass
class FirewallVerdict:
    tool_name: str
    content: str
    hits: list[str]
    needs_confirmation: bool
    elapsed_ms: float


@dataclass
class ContentFirewall:
    client: "Client"
    log: list[dict] = field(default_factory=list)

    async def call(self, tool_name: str, arguments: dict) -> FirewallVerdict:
        mod = _load_exercises_module()

        start = time.monotonic()
        result = await self.client.call_tool(tool_name, arguments)
        elapsed_ms = (time.monotonic() - start) * 1000

        content = result.structured_content["result"] if not result.is_error else ""
        hits = mod.scan_for_injection(content) if content else []
        needs_confirmation = mod.should_require_confirmation(hits)

        self.log.append(
            {
                "tool_name": tool_name,
                "hit_count": len(hits),
                "needs_confirmation": needs_confirmation,
                "elapsed_ms": round(elapsed_ms, 2),
            }
        )

        return FirewallVerdict(
            tool_name=tool_name,
            content=content,
            hits=hits,
            needs_confirmation=needs_confirmation,
            elapsed_ms=elapsed_ms,
        )


async def main() -> None:
    mod = _load_exercises_module()
    async with Client(mod.mcp) as client:
        firewall = ContentFirewall(client)

        for url in mod._PAGES:
            verdict = await firewall.call("fetch_page", {"url": url})
            print(
                f"{url}: {len(verdict.hits)} hit(s), "
                f"confirm={verdict.needs_confirmation}"
            )

        print()
        print(f"Firewall processed {len(firewall.log)} calls total.")
        for entry in firewall.log:
            print(" ", entry)


asyncio.run(main())
