#!/usr/bin/env python3
"""Generate Merc .roo scaffold files from graph-native map.md specs.

This script consumes a constrained subset of Markdown:
- fenced code blocks with info string `mapmd-json`
- each block contains JSON objects describing area metadata, includes, or rooms

The embedded `mapmd-json` block is the canonical machine-readable graph schema.
Current output is a `.roo` projection only. Optional graph metadata such as
`coord`, `cluster`, and `labels` may be parsed and validated, but they are not
emitted into generated `.roo` files.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


VALID_DIRECTIONS = {
    "north": "NORTH",
    "east": "EAST",
    "south": "SOUTH",
    "west": "WEST",
    "up": "UP",
    "down": "DOWN",
    "enter": "ENTER",
    "out": "OUT",
}

REVERSE_DIRECTIONS = {
    "north": "south",
    "east": "west",
    "south": "north",
    "west": "east",
    "up": "down",
    "down": "up",
    "enter": "out",
    "out": "enter",
}

VALID_EXIT_FLAGS = {"IsDoor", "Closed", "Locked", "Pick"}
VALID_POSITIONS = {
    "POS_DEAD",
    "POS_SLEEPING",
    "POS_RESTING",
    "POS_FIGHTING",
    "POS_STANDING",
}

MAP_BLOCK_RE = re.compile(
    r"```mapmd-json\s*\r?\n(.*?)\r?\n```",
    re.DOTALL | re.IGNORECASE,
)

JOB_FUNC_RE = re.compile(r"FUNC_NAME\(\s*([A-Za-z0-9_]+)\s*\)")


@dataclass
class ValidationIssue:
    level: str
    message: str
    source: str = ""


@dataclass
class SpecState:
    area: dict[str, Any] = field(default_factory=dict)
    rooms: dict[int, dict[str, Any]] = field(default_factory=dict)
    issues: list[ValidationIssue] = field(default_factory=list)
    loaded_files: set[Path] = field(default_factory=set)

    def add_issue(self, level: str, message: str, source: Path | str = "") -> None:
        self.issues.append(ValidationIssue(level=level, message=message, source=str(source)))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate .roo scaffold files from structured map.md specs."
    )
    parser.add_argument("map_md", type=Path, help="Path to the master map.md file")
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Directory to emit .roo files into. Defaults to <area>/roo.",
    )
    parser.add_argument(
        "--validate-only",
        action="store_true",
        help="Validate the spec without writing any .roo files.",
    )
    return parser.parse_args()


def load_markdown_spec(path: Path, state: SpecState) -> None:
    path = path.resolve()
    if path in state.loaded_files:
        return
    state.loaded_files.add(path)

    try:
        content = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        state.add_issue("error", f"Include target does not exist: {path}", path)
        return

    blocks = MAP_BLOCK_RE.findall(content)
    if not blocks:
        state.add_issue("error", "No ```mapmd-json blocks found.", path)
        return

    for raw_block in blocks:
        try:
            data = json.loads(raw_block)
        except json.JSONDecodeError as exc:
            state.add_issue("error", f"Invalid JSON block: {exc}", path)
            continue

        if not isinstance(data, dict):
            state.add_issue("error", "Each mapmd-json block must be a JSON object.", path)
            continue

        if "area" in data:
            if not isinstance(data["area"], dict):
                state.add_issue("error", "`area` must be an object.", path)
            else:
                state.area.update(data["area"])

        includes = data.get("includes", [])
        if includes:
            if not isinstance(includes, list) or not all(isinstance(x, str) for x in includes):
                state.add_issue("error", "`includes` must be a list of relative file paths.", path)
            else:
                for include in includes:
                    load_markdown_spec((path.parent / include), state)

        rooms = data.get("rooms", [])
        if rooms:
            if not isinstance(rooms, list):
                state.add_issue("error", "`rooms` must be a list.", path)
            else:
                for room in rooms:
                    register_room(room, path, state)


def register_room(room: Any, source: Path, state: SpecState) -> None:
    if not isinstance(room, dict):
        state.add_issue("error", "Each room entry must be an object.", source)
        return

    vnum = room.get("vnum")
    if not isinstance(vnum, int) or vnum <= 0:
        state.add_issue("error", f"Room has invalid `vnum`: {vnum!r}", source)
        return

    if vnum in state.rooms:
        state.add_issue("error", f"Duplicate room vnum: {vnum}", source)
        return

    state.rooms[vnum] = room


def find_repo_root(start: Path) -> Path | None:
    current = start.resolve()
    for candidate in [current, *current.parents]:
        if (candidate / "src" / "job.c").exists():
            return candidate
    return None


def load_known_jobs(repo_root: Path | None) -> set[str]:
    if not repo_root:
        return set()
    job_c = repo_root / "src" / "job.c"
    try:
        content = job_c.read_text(encoding="utf-8")
    except OSError:
        return set()
    return set(JOB_FUNC_RE.findall(content))


def validate_spec(state: SpecState, known_jobs: set[str]) -> None:
    for vnum, room in state.rooms.items():
        validate_room(vnum, room, state, known_jobs)
    validate_reverse_links(state)


def validate_room(vnum: int, room: dict[str, Any], state: SpecState, known_jobs: set[str]) -> None:
    if not isinstance(room.get("name"), str) or not room["name"].strip():
        state.add_issue("error", f"Room {vnum} is missing `name`.", f"room {vnum}")
    if not isinstance(room.get("description"), str) or not room["description"].strip():
        state.add_issue("error", f"Room {vnum} is missing `description`.", f"room {vnum}")

    sector = room.get("sector_type", "SECT_INSIDE")
    if not isinstance(sector, str) or not sector.strip():
        state.add_issue("error", f"Room {vnum} has invalid `sector_type`.", f"room {vnum}")

    flags = room.get("flags", [])
    if flags and not (
        isinstance(flags, list) and all(isinstance(flag, str) and flag.strip() for flag in flags)
    ):
        state.add_issue("error", f"Room {vnum} has invalid `flags`.", f"room {vnum}")

    owner = room.get("owner")
    if owner is not None and not (
        isinstance(owner, list)
        and len(owner) == 2
        and all(isinstance(x, int) and x >= 0 for x in owner)
    ):
        state.add_issue("error", f"Room {vnum} has invalid `owner`.", f"room {vnum}")

    coord = room.get("coord")
    if coord is not None and not (
        isinstance(coord, list)
        and len(coord) == 3
        and all(isinstance(value, (int, float)) for value in coord)
    ):
        state.add_issue("error", f"Room {vnum} has invalid `coord`.", f"room {vnum}")

    cluster = room.get("cluster")
    if cluster is not None and (not isinstance(cluster, str) or not cluster.strip()):
        state.add_issue("error", f"Room {vnum} has invalid `cluster`.", f"room {vnum}")

    labels = room.get("labels")
    if labels is not None and not (
        isinstance(labels, list)
        and all(isinstance(label, str) and label.strip() for label in labels)
    ):
        state.add_issue("error", f"Room {vnum} has invalid `labels`.", f"room {vnum}")

    exits = room.get("exits", [])
    if exits and not isinstance(exits, list):
        state.add_issue("error", f"Room {vnum} has invalid `exits`.", f"room {vnum}")
    else:
        seen_dirs: set[str] = set()
        for exit_spec in exits:
            if not isinstance(exit_spec, dict):
                state.add_issue("error", f"Room {vnum} has a non-object exit.", f"room {vnum}")
                continue
            direction = str(exit_spec.get("direction", "")).lower()
            target = exit_spec.get("to")
            if direction not in VALID_DIRECTIONS:
                state.add_issue(
                    "error",
                    f"Room {vnum} uses invalid direction `{direction}`.",
                    f"room {vnum}",
                )
                continue
            if direction in seen_dirs:
                state.add_issue(
                    "error",
                    f"Room {vnum} duplicates direction `{direction}`.",
                    f"room {vnum}",
                )
            seen_dirs.add(direction)
            if not isinstance(target, int) or target <= 0:
                state.add_issue(
                    "error",
                    f"Room {vnum} exit `{direction}` has invalid `to` value `{target}`.",
                    f"room {vnum}",
                )
            elif target not in state.rooms:
                state.add_issue(
                    "error",
                    f"Room {vnum} exit `{direction}` targets missing room {target}.",
                    f"room {vnum}",
                )
            exit_flags = exit_spec.get("flags", [])
            if exit_flags and not (
                isinstance(exit_flags, list)
                and all(isinstance(flag, str) and flag in VALID_EXIT_FLAGS for flag in exit_flags)
            ):
                state.add_issue(
                    "error",
                    f"Room {vnum} exit `{direction}` has invalid flags.",
                    f"room {vnum}",
                )

    keywords = room.get("keywords", [])
    if keywords and not isinstance(keywords, list):
        state.add_issue("error", f"Room {vnum} has invalid `keywords`.", f"room {vnum}")
    else:
        for keyword in keywords:
            if not isinstance(keyword, dict):
                state.add_issue("error", f"Room {vnum} has a non-object keyword.", f"room {vnum}")
                continue
            if not isinstance(keyword.get("keyword"), str) or not keyword["keyword"].strip():
                state.add_issue("error", f"Room {vnum} keyword is missing `keyword`.", f"room {vnum}")
            if not isinstance(keyword.get("description"), str) or not keyword["description"].strip():
                state.add_issue(
                    "error", f"Room {vnum} keyword `{keyword.get('keyword', '')}` lacks description.", f"room {vnum}"
                )

    jobs = room.get("jobs", [])
    if jobs and not isinstance(jobs, list):
        state.add_issue("error", f"Room {vnum} has invalid `jobs`.", f"room {vnum}")
    else:
        for job in jobs:
            if not isinstance(job, dict):
                state.add_issue("error", f"Room {vnum} has a non-object job.", f"room {vnum}")
                continue
            keyword = job.get("keyword")
            function = job.get("function")
            position = job.get("position")
            if not isinstance(keyword, str) or not keyword.strip():
                state.add_issue("error", f"Room {vnum} has a job without `keyword`.", f"room {vnum}")
            if not isinstance(function, str) or not function.strip():
                state.add_issue("error", f"Room {vnum} has a job without `function`.", f"room {vnum}")
            elif known_jobs and function not in known_jobs:
                state.add_issue(
                    "error",
                    f"Room {vnum} references unknown job function `{function}`.",
                    f"room {vnum}",
                )
            if not isinstance(position, str) or position not in VALID_POSITIONS:
                state.add_issue(
                    "error",
                    f"Room {vnum} job `{function}` has invalid `position` `{position}`.",
                    f"room {vnum}",
                )

    enquires = room.get("enquires", [])
    if enquires and not isinstance(enquires, list):
        state.add_issue("error", f"Room {vnum} has invalid `enquires`.", f"room {vnum}")
    else:
        for enquire in enquires:
            if isinstance(enquire, str):
                keyword = enquire
            elif isinstance(enquire, dict):
                keyword = enquire.get("keyword", "")
            else:
                state.add_issue("error", f"Room {vnum} has a malformed enquire entry.", f"room {vnum}")
                continue
            if not isinstance(keyword, str) or not keyword.strip():
                state.add_issue("error", f"Room {vnum} has an empty enquire keyword.", f"room {vnum}")


def validate_reverse_links(state: SpecState) -> None:
    for vnum, room in state.rooms.items():
        for exit_spec in room.get("exits", []):
            if not isinstance(exit_spec, dict):
                continue
            direction = str(exit_spec.get("direction", "")).lower()
            target = exit_spec.get("to")
            if direction not in REVERSE_DIRECTIONS or not isinstance(target, int):
                continue
            if exit_spec.get("one_way", False):
                continue
            target_room = state.rooms.get(target)
            if not target_room:
                continue
            expected = REVERSE_DIRECTIONS[direction]
            reverse_exit = next(
                (
                    other
                    for other in target_room.get("exits", [])
                    if isinstance(other, dict)
                    and str(other.get("direction", "")).lower() == expected
                ),
                None,
            )
            if not reverse_exit:
                state.add_issue(
                    "error",
                    f"Room {vnum} exit `{direction}` -> {target} is missing reverse `{expected}`.",
                    f"room {vnum}",
                )
                continue
            if reverse_exit.get("to") != vnum:
                state.add_issue(
                    "error",
                    f"Room {vnum} exit `{direction}` -> {target} conflicts with reverse `{expected}` -> {reverse_exit.get('to')}.",
                    f"room {vnum}",
                )


def validate_area_metadata(state: SpecState) -> None:
    if not state.area:
        return

    name = state.area.get("name")
    title = state.area.get("title")
    if name is not None and (not isinstance(name, str) or not name.strip()):
        state.add_issue("error", "Area has invalid `name`.", "area")
    if title is not None and (not isinstance(title, str) or not title.strip()):
        state.add_issue("error", "Area has invalid `title`.", "area")

    serial = state.area.get("serial")
    if serial is not None and not isinstance(serial, int):
        state.add_issue("error", "Area `serial` must be an integer when present.", "area")

    capital = state.area.get("capital")
    if capital is not None and (not isinstance(capital, str) or not capital.strip()):
        state.add_issue("error", "Area `capital` must be a non-empty string when present.", "area")

    design_notes = state.area.get("design_notes")
    if design_notes is not None and not isinstance(design_notes, str):
        state.add_issue("error", "Area `design_notes` must be a string when present.", "area")


def ensure_tilde(value: str) -> str:
    stripped = value.rstrip()
    if stripped.endswith("~"):
        return stripped
    return f"{stripped}~"


def emit_room(room: dict[str, Any]) -> str:
    lines: list[str] = []
    lines.append(f"Vnum            {room['vnum']}")
    lines.append(f"Name            {ensure_tilde(room['name'])}")
    lines.append("Description")
    lines.append(room["description"].rstrip())
    lines.append("~")
    lines.append(f"SectorType      {room.get('sector_type', 'SECT_INSIDE')}")

    for flag in room.get("flags", []):
        lines.append(f"{flag:<15} Yes")

    owner = room.get("owner")
    if owner:
        lines.append(f"Owner           {owner[0]} {owner[1]}")

    for exit_spec in room.get("exits", []):
        direction = VALID_DIRECTIONS[str(exit_spec["direction"]).lower()]
        lines.append("")
        lines.append("#Exit")
        lines.append(f"Direction       {direction}")
        lines.append(f"ExitVnum        {exit_spec['to']}")
        lines.append(f"ExitDesc        {ensure_tilde(exit_spec.get('exit_desc', ''))}")
        lines.append(f"ExitKeyword     {ensure_tilde(exit_spec.get('exit_keyword', ''))}")
        if "message" in exit_spec:
            lines.append(f"Message         {ensure_tilde(exit_spec.get('message', ''))}")
        lines.append(f"ExitKey         {int(exit_spec.get('exit_key', 0))}")
        for flag in exit_spec.get("flags", []):
            lines.append(f"{flag:<15} Yes")
        lines.append("End")

    for keyword in room.get("keywords", []):
        lines.append("")
        lines.append("#Keyword")
        lines.append(f"Keyword         {ensure_tilde(keyword['keyword'])}")
        lines.append("Description")
        lines.append(keyword["description"].rstrip())
        lines.append("~")
        lines.append("End")

    for job in room.get("jobs", []):
        lines.append("")
        lines.append("#Job")
        lines.append(f"Keyword         {ensure_tilde(job['keyword'])}")
        lines.append(f"Function        {ensure_tilde(job['function'])}")
        lines.append(f"Position        {job['position']}")
        lines.append("End")

    for enquire in room.get("enquires", []):
        keyword = enquire if isinstance(enquire, str) else enquire["keyword"]
        lines.append("")
        lines.append("#Enquire")
        lines.append(f"Keyword         {ensure_tilde(keyword)}")
        lines.append("End")

    lines.append("")
    lines.append("End")
    lines.append("")
    return "\n".join(lines)


def write_rooms(output_dir: Path, rooms: dict[int, dict[str, Any]]) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    for vnum, room in sorted(rooms.items()):
        room_path = output_dir / f"{vnum}.roo"
        room_path.write_text(emit_room(room), encoding="utf-8")


def print_issues(issues: list[ValidationIssue]) -> None:
    for issue in issues:
        prefix = issue.level.upper()
        if issue.source:
            print(f"{prefix}: {issue.source}: {issue.message}", file=sys.stderr)
        else:
            print(f"{prefix}: {issue.message}", file=sys.stderr)


def main() -> int:
    args = parse_args()
    map_md = args.map_md.resolve()
    state = SpecState()

    load_markdown_spec(map_md, state)
    repo_root = find_repo_root(map_md.parent)
    known_jobs = load_known_jobs(repo_root)
    validate_area_metadata(state)
    validate_spec(state, known_jobs)

    errors = [issue for issue in state.issues if issue.level == "error"]
    warnings = [issue for issue in state.issues if issue.level != "error"]
    print_issues(state.issues)

    if errors:
        print(
            f"Validation failed with {len(errors)} error(s) and {len(warnings)} warning(s).",
            file=sys.stderr,
        )
        return 1

    output_dir = args.output_dir or (map_md.parent / "roo")
    if args.validate_only:
        print(
            f"Validation succeeded for {len(state.rooms)} room(s). Output dir would be: {output_dir}"
        )
        return 0

    write_rooms(output_dir, state.rooms)
    print(f"Wrote {len(state.rooms)} room scaffold file(s) to {output_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
