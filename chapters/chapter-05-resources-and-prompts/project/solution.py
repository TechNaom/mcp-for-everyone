"""Chapter 5 mini project — reference solution."""

import importlib.util
from pathlib import Path


def _load_chapter_4_module():
    """Load Chapter 4's bookmarks solution under a unique module name.

    A plain `sys.path.insert` + `import solution` breaks depending on how
    this file itself is invoked (both files are named solution.py) --
    running `python solution.py` directly happens to work because of
    Python's automatic sys.path[0] handling, but `python -c "import
    solution"` or a test runner importing this file by name resolves the
    import back to *this* file instead of Chapter 4's, causing a
    circular self-import. Loading by explicit file path sidesteps the
    name collision entirely, regardless of invocation method.
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


@mcp.resource("bookmarks://count")
def bookmark_count() -> str:
    """Static resource: how many bookmarks are currently saved."""
    data = _load()
    return f"{len(data)} bookmarks"


@mcp.prompt()
def recommend_reading(topic: str) -> str:
    """Ask the model to recommend a saved bookmark relevant to a topic."""
    return (
        f"Given the saved bookmarks available to you, recommend the single "
        f"most relevant one for someone interested in '{topic}', and explain "
        f"why in one sentence."
    )


if __name__ == "__main__":
    mcp.run(transport="stdio")
