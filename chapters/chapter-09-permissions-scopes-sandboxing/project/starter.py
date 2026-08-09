"""
Chapter 9 mini project: a permission audit tool.

Scans a server module's source for tool functions and reports which
ones have no @require_scope check -- catching exactly the "forgot the
decorator" regression from this chapter's practice bank, automatically,
without needing to manually review every tool by hand.

Fill in the TODOs. See solution.py for a reference implementation.
"""

import importlib.util
from pathlib import Path


def load_module_from_path(path: Path, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def audit_scopes(module, tool_names: list[str]) -> list[str]:
    """Return the names of tools (from `tool_names`) whose function in
    `module` has no `_required_scope` attribute -- i.e., no scope check."""
    # TODO 1: For each name in tool_names, look it up on `module` with
    # getattr. If the attribute is missing OR the found function has no
    # `_required_scope` attribute, add the name to the returned list.
    return []


def print_report(unscoped: list[str]) -> None:
    # TODO 2: Print a clear report. If `unscoped` is empty, print
    # something reassuring ("All N tools have scope checks."). If not
    # empty, print each unscoped tool name as a warning, and make the
    # output visually distinct enough that it wouldn't be missed in CI
    # log output (e.g., a clear "FAIL" marker).
    pass


if __name__ == "__main__":
    ch9_exercises = load_module_from_path(
        Path(__file__).parents[1] / "exercises" / "solution.py", "ch9_exercises"
    )
    tool_names = ["save_note", "list_notes", "delete_note"]

    # TODO 3 (production-gear): Call audit_scopes and print_report. Then
    # deliberately test the audit tool itself: temporarily comment out
    # the @require_scope decorator on one tool in a COPY of the
    # exercises solution (don't modify the original), re-run the audit,
    # and confirm it catches the missing check.

    unscoped = audit_scopes(ch9_exercises, tool_names)
    print_report(unscoped)
