#!/usr/bin/env python3
"""Validate Merc-FJU map.md specs and summarize mapmd-json state.

This tool reuses the existing scaffold generator's parser/validator so it stays
aligned with the current repo contract, then adds a small amount of stricter
metadata checking around reserved room blocks and cluster references.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
GENERATOR_PATH = (
    REPO_ROOT / ".agents" / "skills" / "merc-area-builder" / "scripts" / "generate_roo_from_map_md.py"
)
VALID_DIRECTIONS = {"north", "east", "south", "west", "up", "down", "enter", "out"}


def load_generator_module():
    spec = importlib.util.spec_from_file_location("generate_roo_from_map_md", GENERATOR_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load generator module from {GENERATOR_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)  # type: ignore[assignment]
    return module


def parse_range(value: Any) -> tuple[int, int] | None:
    if not isinstance(value, str) or "-" not in value:
        return None
    left, right = value.split("-", 1)
    if not left.isdigit() or not right.isdigit():
        return None
    start = int(left)
    end = int(right)
    if start <= 0 or end < start:
        return None
    return start, end


def add_issue(state: Any, level: str, message: str, source: str = "metadata") -> None:
    state.add_issue(level, message, source)


def validate_metadata_contract(state: Any) -> None:
    area = state.area or {}
    if not area:
        add_issue(state, "error", "Missing `area` metadata object.", "area")
        return

    planned_range = parse_range(area.get("planned_vnum_range"))
    if planned_range is None:
        add_issue(
            state,
            "error",
            "Area `planned_vnum_range` is missing or invalid; expected `NNNN-NNNN`.",
            "area",
        )

    reserved_block = parse_range(area.get("reserved_room_block"))
    if reserved_block is None:
        add_issue(
            state,
            "warning" if planned_range is not None else "error",
            "Area `reserved_room_block` is missing or invalid; expected `NNNN-NNNN`.",
            "area",
        )

    theme = area.get("theme")
    if not isinstance(theme, dict):
        add_issue(state, "error", "Area `theme` must be an object.", "area")
    else:
        primary = theme.get("primary")
        secondary = theme.get("secondary")
        if not isinstance(primary, str) or not primary.strip():
            add_issue(state, "error", "Area theme is missing `primary`.", "area")
        if not isinstance(secondary, str) or not secondary.strip():
            add_issue(state, "error", "Area theme is missing `secondary`.", "area")

    cluster_defs = area.get("clusters", [])
    cluster_ids: set[str] = set()
    if cluster_defs is not None:
        if not isinstance(cluster_defs, list):
            add_issue(state, "error", "Area `clusters` must be a list when present.", "area")
        else:
            for cluster in cluster_defs:
                if not isinstance(cluster, dict):
                    add_issue(state, "error", "Each cluster must be an object.", "area")
                    continue
                cluster_id = cluster.get("id")
                if not isinstance(cluster_id, str) or not cluster_id.strip():
                    add_issue(state, "error", "Each cluster must have a non-empty `id`.", "area")
                    continue
                if cluster_id in cluster_ids:
                    add_issue(state, "error", f"Duplicate cluster id `{cluster_id}`.", "area")
                    continue
                cluster_ids.add(cluster_id)

    world_links = area.get("world_links", [])
    if world_links is not None:
        if not isinstance(world_links, list):
            add_issue(state, "error", "Area `world_links` must be a list when present.", "area")
        else:
            for idx, link in enumerate(world_links):
                source = f"area.world_links[{idx}]"
                if not isinstance(link, dict):
                    add_issue(state, "error", "Each world link must be an object.", source)
                    continue
                direction = str(link.get("direction", "")).lower()
                if direction not in VALID_DIRECTIONS:
                    add_issue(state, "error", f"Invalid world link direction `{direction}`.", source)
                source_vnum = link.get("source_vnum")
                if not isinstance(source_vnum, int) or source_vnum not in state.rooms:
                    add_issue(
                        state,
                        "error",
                        "World link `source_vnum` must point to a room defined in this spec.",
                        source,
                    )

    active_range = reserved_block or planned_range
    if active_range is not None:
        start, end = active_range
        for vnum, room in sorted(state.rooms.items()):
            if not (start <= vnum <= end):
                add_issue(
                    state,
                    "warning",
                    f"Room {vnum} falls outside the active reservation range {start}-{end}.",
                    f"room {vnum}",
                )
            cluster = room.get("cluster")
            if cluster_ids and cluster is not None and cluster not in cluster_ids:
                add_issue(
                    state,
                    "warning",
                    f"Room {vnum} references undefined cluster `{cluster}`.",
                    f"room {vnum}",
                )


def summarize(state: Any) -> dict[str, Any]:
    errors = [issue for issue in state.issues if issue.level == "error"]
    warnings = [issue for issue in state.issues if issue.level != "error"]
    return {
        "area_name": state.area.get("name"),
        "area_title": state.area.get("title"),
        "room_count": len(state.rooms),
        "loaded_files": sorted(str(path) for path in state.loaded_files),
        "error_count": len(errors),
        "warning_count": len(warnings),
        "issues": [
            {"level": issue.level, "source": issue.source, "message": issue.message}
            for issue in state.issues
        ],
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate map.md / mapmd-json specs with repo-aware rules."
    )
    parser.add_argument("map_md", type=Path, help="Path to the master area map.md")
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print a machine-readable JSON summary instead of human-readable text.",
    )
    parser.add_argument(
        "--fail-on-warning",
        action="store_true",
        help="Return non-zero when warnings are present.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    module = load_generator_module()

    map_md = args.map_md.resolve()
    state = module.SpecState()
    module.load_markdown_spec(map_md, state)
    repo_root = module.find_repo_root(map_md.parent)
    known_jobs = module.load_known_jobs(repo_root)
    module.validate_area_metadata(state)
    module.validate_spec(state, known_jobs)
    validate_metadata_contract(state)

    summary = summarize(state)

    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    else:
        module.print_issues(state.issues)
        print(
            f"Validated {summary['room_count']} room(s) across {len(summary['loaded_files'])} file(s)."
        )
        print(
            f"Area: {summary['area_name'] or '<unknown>'} / {summary['area_title'] or '<unknown>'}"
        )
        print(
            f"Result: {summary['error_count']} error(s), {summary['warning_count']} warning(s)."
        )

    if summary["error_count"]:
        return 1
    if args.fail_on_warning and summary["warning_count"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
