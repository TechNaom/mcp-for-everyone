"""
Chapter 5 mini project: extend the Chapter 4 bookmarks server with a
static resource and a prompt.

Reuses chapter-04's bookmarks solution rather than duplicating it.
Fill in the TODOs. See solution.py for a reference implementation.
"""

import importlib.util
from pathlib import Path


def _load_chapter_4_module():
    """Load Chapter 4's bookmarks solution by explicit file path.

    Avoids a name collision: this file and Chapter 4's are both named
    solution.py/starter.py, and a plain sys.path + `import solution`
    trick resolves inconsistently depending on how this file is invoked.
    """
    ch4_path = (
        Path(__file__).parents[2]
        / "chapter-04-your-first-mcp-server"
        / "project"
        / "solution.py"
    )
    spec = importlib.util.spec_from_file_location("chapter_04_bookmarks", ch4_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_ch4 = _load_chapter_4_module()
mcp = _ch4.mcp
_load = _ch4._load


# TODO 1: Add a static resource `bookmarks://count` that returns how
# many bookmarks are currently saved, as a plain string like "3 bookmarks".
# Reuse the `_load()` helper already imported above.


# TODO 2: Add a prompt `recommend_reading(topic: str) -> str` that
# returns instruction text asking the model to recommend which saved
# bookmark (by title) is most relevant to the given topic. The prompt
# text itself can't see the actual bookmark list -- that's fine, the
# host is expected to also give the model the bookmark data (e.g. via
# the bookmarks:// resources) alongside this prompt.


if __name__ == "__main__":
    mcp.run(transport="stdio")
