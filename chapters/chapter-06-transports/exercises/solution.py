"""Chapter 6 exercises — reference solution: run the notes server over
Streamable HTTP, both session-based (default) and stateless.

Usage:
    python solution.py              # session-based (default), port 8767
    python solution.py --stateless  # stateless_http=True, port 8768
"""

import importlib.util
import sys
from pathlib import Path


def _load_chapter_4_module():
    ch4_path = (
        Path(__file__).parents[2]
        / "chapter-04-your-first-mcp-server"
        / "exercises"
        / "solution.py"
    )
    spec = importlib.util.spec_from_file_location("chapter_04_notes", ch4_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


mcp = _load_chapter_4_module().mcp


if __name__ == "__main__":
    if "--stateless" in sys.argv:
        mcp.run(
            transport="streamable-http",
            host="127.0.0.1",
            port=8768,
            stateless_http=True,
        )
    else:
        mcp.run(transport="streamable-http", host="127.0.0.1", port=8767)
