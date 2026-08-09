"""
Chapter 10 mini project: a tool-output firewall.

Wraps any tool call, scans the result for injection patterns, logs
every call (per the audit-trail interview question), and returns a
verdict the calling host can act on -- allow, or flag-for-confirmation.
Reuses the fetch_page server from the exercises.

Fill in the TODOs. See solution.py for a reference implementation.
"""

import asyncio
import importlib.util
import re
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
    """Wraps tool calls with scanning, logging, and a confirmation verdict."""

    client: "Client"
    log: list[dict] = field(default_factory=list)

    async def call(self, tool_name: str, arguments: dict) -> FirewallVerdict:
        # TODO 1: Call self.client.call_tool(tool_name, arguments), time
        # it, extract the text content, and run it through
        # ch10_exercises.scan_for_injection.

        # TODO 2: Append a log entry (dict) to self.log with at least:
        # tool_name, hit_count, needs_confirmation, elapsed_ms. This is
        # the audit trail -- every call gets logged, not just flagged
        # ones.

        # TODO 3: Return a FirewallVerdict with the results.
        raise NotImplementedError


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


asyncio.run(main())
