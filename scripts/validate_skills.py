#!/usr/bin/env python3
"""Check that every skills/*/SKILL.md has Agent Skills frontmatter.

Required on each file: YAML frontmatter with a non-empty `name` and
`description`. `name` must match the parent directory, except for template
directories whose names start with '_'.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
MAX_NAME = 64
MAX_DESCRIPTION = 1024
NAME_CHARS = set("abcdefghijklmnopqrstuvwxyz0123456789-")
FOLD_MARKERS = {">", ">-", ">+", "|", "|-", "|+"}


def frontmatter_lines(text: str) -> list[str] | str:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return "SKILL.md must start with YAML frontmatter (---)"
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            return lines[1:index]
    return "frontmatter is missing a closing ---"


def parse_frontmatter(lines: list[str]) -> dict[str, str]:
    data: dict[str, str] = {}
    key: str | None = None
    chunks: list[str] = []

    def commit() -> None:
        nonlocal key, chunks
        if key is None:
            return
        value = " ".join(part for part in chunks if part)
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]
        data[key] = value.strip()
        key = None
        chunks = []

    for raw in lines:
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if raw[:1] in {" ", "\t"}:
            if key is not None:
                chunks.append(stripped)
            continue
        commit()
        if ":" not in raw:
            continue
        field, _, value = raw.partition(":")
        key = field.strip()
        value = value.strip()
        chunks = [] if value in FOLD_MARKERS else ([value] if value else [])
    commit()
    return data


def check_name(name: str, directory: str) -> str | None:
    if not name:
        return "frontmatter is missing name"
    if len(name) > MAX_NAME:
        return f"name exceeds {MAX_NAME} characters"
    if any(char not in NAME_CHARS for char in name):
        return "name must be lowercase letters, digits, and hyphens"
    if name.startswith("-") or name.endswith("-") or "--" in name:
        return "name must not start or end with a hyphen or contain '--'"
    if not directory.startswith("_") and name != directory:
        return f"name {name!r} must match the directory name {directory!r}"
    return None


def check_description(description: str) -> str | None:
    if not description or description in FOLD_MARKERS:
        return "frontmatter is missing description"
    if len(description) > MAX_DESCRIPTION:
        return f"description exceeds {MAX_DESCRIPTION} characters"
    if "<" in description or ">" in description:
        return "description must not contain XML tags"
    return None


def main() -> int:
    paths = sorted(SKILLS_DIR.glob("*/SKILL.md"))
    errors: list[str] = []
    if not paths:
        errors.append("no skills/*/SKILL.md files found")

    for path in paths:
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8")
        lines = frontmatter_lines(text)
        if isinstance(lines, str):
            errors.append(f"{rel}: {lines}")
            continue
        fields = parse_frontmatter(lines)
        name_error = check_name(fields.get("name", ""), path.parent.name)
        if name_error:
            errors.append(f"{rel}: {name_error}")
        description_error = check_description(fields.get("description", ""))
        if description_error:
            errors.append(f"{rel}: {description_error}")

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    print(f"ok: {len(paths)} skill file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
