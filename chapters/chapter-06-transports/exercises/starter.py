"""
Chapter 6 exercises: run the notes server over Streamable HTTP and
observe the stateless_http gotcha yourself.

Fill in the TODOs. This file runs the SERVER. Use a second terminal (or
solution_client.py) to actually call it, since mcp.run() blocks.
"""

import importlib.util
from pathlib import Path


def _load_chapter_4_module():
    """Load Chapter 4's notes-server solution by explicit file path
    (avoids a solution.py/solution.py name collision)."""
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
    # TODO 1: Run this server over Streamable HTTP, host="127.0.0.1",
    # port=8767, WITHOUT setting stateless_http (use the SDK default).

    # TODO 2: Once TODO 1 works, add a second `if` branch (e.g. behind a
    # sys.argv check like `--stateless`) that instead runs with
    # stateless_http=True on port 8768, so you can compare both.
    pass
