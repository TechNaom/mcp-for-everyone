"""Chapter 9 mini project — reference solution: a permission audit tool."""

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
    unscoped = []
    for name in tool_names:
        fn = getattr(module, name, None)
        if fn is None or not hasattr(fn, "_required_scope"):
            unscoped.append(name)
    return unscoped


def print_report(unscoped: list[str]) -> None:
    if not unscoped:
        print("PASS: all tools have scope checks.")
        return
    print(f"FAIL: {len(unscoped)} tool(s) with NO scope check:")
    for name in unscoped:
        print(f"  - {name}")


if __name__ == "__main__":
    ch9_exercises = load_module_from_path(
        Path(__file__).parents[1] / "exercises" / "solution.py", "ch9_exercises"
    )
    tool_names = ["save_note", "list_notes", "delete_note"]

    unscoped = audit_scopes(ch9_exercises, tool_names)
    print_report(unscoped)

    # Prove the audit tool actually catches a missing check: define a
    # fake "forgot the decorator" tool inline and confirm it's flagged.
    def unscoped_tool() -> str:
        return "dangerous"

    class FakeModule:
        save_note = ch9_exercises.save_note
        list_notes = ch9_exercises.list_notes
        delete_note = unscoped_tool  # simulating a missing decorator

    print()
    print("Re-running against a module with a deliberately missing check:")
    print_report(audit_scopes(FakeModule, tool_names))
