from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict, deque
from dataclasses import asdict, dataclass, field
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
AREA_ROOT = ROOT / "area"
DIRECTORY_LIST = AREA_ROOT / "directory.lst"

VALID_DIRECTIONS = {
    "north",
    "east",
    "south",
    "west",
    "up",
    "down",
    "enter",
    "out",
}

REVERSE_DIRECTION = {
    "north": "south",
    "east": "west",
    "south": "north",
    "west": "east",
    "up": "down",
    "down": "up",
    "enter": "out",
    "out": "enter",
}

DIRECTORY_RANGE_RE = re.compile(
    r"^\*\s*(?P<name>[A-Za-z0-9_]+)\s+房間\s+(?P<start>\d+)-(?P<end>\d+)"
)

EXCLUDED_AREA_DIRS = {"player"}


@dataclass
class Issue:
    severity: str
    code: str
    message: str
    location: str | None = None


@dataclass
class DirectoryRange:
    name: str
    start: int
    end: int
    line_no: int


@dataclass
class DirectoryEntry:
    name: str
    line_no: int
    declared_range: DirectoryRange | None = None


@dataclass
class RoomExit:
    direction: str | None
    target_vnum: int | None
    line_no: int


@dataclass
class RoomData:
    area_name: str
    path: Path
    file_vnum: int | None
    vnum: int | None
    exits: list[RoomExit] = field(default_factory=list)

    def exit_targets_by_direction(self) -> dict[str, list[int]]:
        targets: dict[str, list[int]] = defaultdict(list)
        for exit_data in self.exits:
            if exit_data.direction and exit_data.target_vnum is not None:
                targets[exit_data.direction].append(exit_data.target_vnum)
        return targets


@dataclass
class AreaData:
    name: str
    path: Path
    directory_entry: DirectoryEntry | None
    index_name: str | None = None
    capital: int | None = None
    rooms: dict[int, RoomData] = field(default_factory=dict)

    def anchor_vnum(self) -> int | None:
        if self.capital and self.capital in self.rooms:
            return self.capital
        if self.rooms:
            return min(self.rooms)
        return None


@dataclass
class Report:
    scanned_areas: int = 0
    scanned_rooms: int = 0
    scanned_exits: int = 0
    errors: list[Issue] = field(default_factory=list)
    warnings: list[Issue] = field(default_factory=list)

    def add(self, severity: str, code: str, message: str, location: str | None = None) -> None:
        issue = Issue(severity=severity, code=code, message=message, location=location)
        if severity == "error":
            self.errors.append(issue)
        else:
            self.warnings.append(issue)

    def to_json(self) -> dict:
        return {
            "summary": {
                "scanned_areas": self.scanned_areas,
                "scanned_rooms": self.scanned_rooms,
                "scanned_exits": self.scanned_exits,
                "errors": len(self.errors),
                "warnings": len(self.warnings),
            },
            "errors": [asdict(issue) for issue in self.errors],
            "warnings": [asdict(issue) for issue in self.warnings],
        }


def relpath(path: Path | None) -> str | None:
    if path is None:
        return None
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def parse_directory_list(path: Path) -> list[DirectoryEntry]:
    entries: list[DirectoryEntry] = []
    pending_range: DirectoryRange | None = None
    for line_no, raw_line in enumerate(read_text(path).splitlines(), start=1):
        stripped = raw_line.strip()
        if not stripped:
            continue
        if stripped.startswith("*"):
            match = DIRECTORY_RANGE_RE.match(stripped)
            if match:
                pending_range = DirectoryRange(
                    name=match.group("name"),
                    start=int(match.group("start")),
                    end=int(match.group("end")),
                    line_no=line_no,
                )
            continue
        entries.append(DirectoryEntry(name=stripped, line_no=line_no, declared_range=pending_range))
        pending_range = None
    return entries


def discover_area_directories(area_root: Path) -> dict[str, Path]:
    directories: dict[str, Path] = {}
    for child in area_root.iterdir():
        if not child.is_dir():
            continue
        if child.name in EXCLUDED_AREA_DIRS:
            continue
        if (child / "index").exists() or (child / "roo").exists():
            directories[child.name] = child
    return directories


def parse_index(path: Path) -> tuple[str | None, int | None]:
    index_name: str | None = None
    capital: int | None = None
    for raw_line in read_text(path).splitlines():
        stripped = raw_line.strip()
        if stripped.startswith("Name"):
            index_name = stripped[len("Name") :].strip().rstrip("~")
        elif stripped.startswith("Capital"):
            capital_text = stripped[len("Capital") :].strip().split()
            if capital_text:
                try:
                    capital = int(capital_text[0])
                except ValueError:
                    capital = None
    return index_name, capital


def parse_room(path: Path, area_name: str) -> RoomData:
    file_vnum: int | None
    try:
        file_vnum = int(path.stem)
    except ValueError:
        file_vnum = None

    room = RoomData(area_name=area_name, path=path, file_vnum=file_vnum, vnum=None)
    in_exit = False
    current_direction: str | None = None
    current_target: int | None = None
    current_line = 0

    for line_no, raw_line in enumerate(read_text(path).splitlines(), start=1):
        stripped = raw_line.strip()
        if not stripped:
            continue
        if stripped == "#Exit":
            in_exit = True
            current_direction = None
            current_target = None
            current_line = line_no
            continue
        if in_exit:
            if stripped == "End":
                room.exits.append(
                    RoomExit(direction=current_direction, target_vnum=current_target, line_no=current_line)
                )
                in_exit = False
                continue
            if stripped.startswith("Direction"):
                current_direction = stripped[len("Direction") :].strip().lower()
                continue
            if stripped.startswith("ExitVnum"):
                value = stripped[len("ExitVnum") :].strip().split()
                if value:
                    try:
                        current_target = int(value[0])
                    except ValueError:
                        current_target = None
                continue
            continue
        if stripped.startswith("Vnum"):
            value = stripped[len("Vnum") :].strip().split()
            if value and room.vnum is None:
                try:
                    room.vnum = int(value[0])
                except ValueError:
                    room.vnum = None
    return room


def bfs(start_nodes: list[int], adjacency: dict[int, set[int]]) -> set[int]:
    visited: set[int] = set()
    queue: deque[int] = deque(start_nodes)
    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        for neighbor in adjacency.get(node, set()):
            if neighbor not in visited:
                queue.append(neighbor)
    return visited


def build_components(nodes: set[int], adjacency: dict[int, set[int]]) -> dict[int, int]:
    component_by_node: dict[int, int] = {}
    next_component_id = 0
    for node in sorted(nodes):
        if node in component_by_node:
            continue
        component_nodes = bfs([node], adjacency)
        for component_node in component_nodes:
            component_by_node[component_node] = next_component_id
        next_component_id += 1
    return component_by_node


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Check merc-fju-3.0 world consistency across area/directory.lst, index files, "
            "room VNUMs, and room exits."
        )
    )
    parser.add_argument(
        "--root-area",
        action="append",
        default=[],
        help=(
            "Area name used as a physical reachability root. May be repeated. "
            "Default: every loadable area with Capital > 0, or the first area listed in "
            "area/directory.lst if no such areas exist."
        ),
    )
    parser.add_argument(
        "--allow-unreachable-area",
        action="append",
        default=[],
        help="Area name to suppress in unreachable-area warnings. May be repeated.",
    )
    parser.add_argument(
        "--skip-unreachable",
        action="store_true",
        help="Skip the physical reachability check for areas.",
    )
    parser.add_argument(
        "--json-report",
        help="Write the full report as JSON to this path.",
    )
    parser.add_argument(
        "--fail-on-warning",
        action="store_true",
        help="Return a non-zero exit code if warnings are found.",
    )
    return parser.parse_args(argv)


def run_checker(args: argparse.Namespace) -> Report:
    report = Report()

    if not DIRECTORY_LIST.exists():
        report.add("error", "missing-directory-list", "Missing area/directory.lst.", relpath(DIRECTORY_LIST))
        return report

    directory_entries = parse_directory_list(DIRECTORY_LIST)
    listed_names = [entry.name for entry in directory_entries]
    discovered_directories = discover_area_directories(AREA_ROOT)

    seen_directory_names: set[str] = set()
    for entry in directory_entries:
        if entry.name in seen_directory_names:
            report.add(
                "error",
                "duplicate-directory-entry",
                f"Duplicate directory.lst entry for area '{entry.name}'.",
                f"{relpath(DIRECTORY_LIST)}:{entry.line_no}",
            )
            continue
        seen_directory_names.add(entry.name)

    extra_directories = sorted(set(discovered_directories) - set(listed_names))
    for area_name in extra_directories:
        report.add(
            "warning",
            "extra-area-directory",
            f"Area directory '{area_name}' is present under area/ but not listed in area/directory.lst.",
            relpath(discovered_directories[area_name]),
        )

    areas: dict[str, AreaData] = {}
    global_rooms: dict[int, RoomData] = {}

    for entry in directory_entries:
        area_path = discovered_directories.get(entry.name)
        if area_path is None:
            report.add(
                "error",
                "missing-area-directory",
                f"Area '{entry.name}' is listed in area/directory.lst but the directory is missing.",
                f"{relpath(DIRECTORY_LIST)}:{entry.line_no}",
            )
            continue

        area = AreaData(name=entry.name, path=area_path, directory_entry=entry)
        areas[area.name] = area

        index_path = area.path / "index"
        roo_dir = area.path / "roo"

        if not index_path.exists():
            report.add("error", "missing-index", f"Area '{area.name}' is missing its index file.", relpath(index_path))
        else:
            area.index_name, area.capital = parse_index(index_path)

        if not roo_dir.exists():
            report.add("error", "missing-roo-dir", f"Area '{area.name}' is missing its roo directory.", relpath(roo_dir))
            continue

        room_paths = sorted(roo_dir.glob("*.roo"), key=lambda item: (not item.stem.isdigit(), item.stem))
        if not room_paths:
            report.add("error", "missing-room-files", f"Area '{area.name}' has no .roo files.", relpath(roo_dir))
            continue

        for room_path in room_paths:
            room = parse_room(room_path, area.name)
            if room.vnum is None:
                report.add(
                    "error",
                    "missing-room-vnum",
                    f"Room file '{room_path.name}' does not define a valid Vnum.",
                    relpath(room_path),
                )
                continue
            if room.file_vnum is None:
                report.add(
                    "warning",
                    "non-numeric-room-filename",
                    f"Room file '{room_path.name}' does not have a numeric filename.",
                    relpath(room_path),
                )
            elif room.file_vnum != room.vnum:
                report.add(
                    "error",
                    "room-filename-vnum-mismatch",
                    f"Room filename '{room_path.name}' does not match its Vnum {room.vnum}.",
                    relpath(room_path),
                )

            if room.vnum in global_rooms:
                other_room = global_rooms[room.vnum]
                report.add(
                    "error",
                    "duplicate-vnum",
                    (
                        f"Duplicate VNUM {room.vnum} found in '{relpath(other_room.path)}' "
                        f"and '{relpath(room.path)}'."
                    ),
                    relpath(room.path),
                )
                continue

            area.rooms[room.vnum] = room
            global_rooms[room.vnum] = room

    report.scanned_areas = len(areas)
    report.scanned_rooms = len(global_rooms)

    for area in areas.values():
        entry = area.directory_entry
        declared_range = entry.declared_range if entry else None
        if declared_range:
            if declared_range.name != area.name:
                report.add(
                    "warning",
                    "directory-comment-name-mismatch",
                    (
                        f"Directory comment names area '{declared_range.name}', "
                        f"but the next entry is '{area.name}'."
                    ),
                    f"{relpath(DIRECTORY_LIST)}:{declared_range.line_no}",
                )
            outside_range = sorted(
                vnum for vnum in area.rooms if not (declared_range.start <= vnum <= declared_range.end)
            )
            if outside_range:
                report.add(
                    "error",
                    "directory-range-mismatch",
                    (
                        f"Area '{area.name}' has room VNUMs outside its directory.lst range "
                        f"{declared_range.start}-{declared_range.end}: {outside_range[:10]}"
                    ),
                    relpath(area.path),
                )
            if area.capital and area.capital not in area.rooms:
                report.add(
                    "error",
                    "capital-room-missing",
                    f"Area '{area.name}' has Capital {area.capital} but no matching room file.",
                    relpath(area.path / "index"),
                )
            if area.capital and not (declared_range.start <= area.capital <= declared_range.end):
                report.add(
                    "warning",
                    "capital-outside-directory-range",
                    (
                        f"Area '{area.name}' has Capital {area.capital}, which is outside the "
                        f"directory.lst range {declared_range.start}-{declared_range.end}."
                    ),
                    relpath(area.path / "index"),
                )
        elif area.capital and area.capital not in area.rooms:
            report.add(
                "error",
                "capital-room-missing",
                f"Area '{area.name}' has Capital {area.capital} but no matching room file.",
                relpath(area.path / "index"),
            )

    directed_adjacency: dict[int, set[int]] = defaultdict(set)
    undirected_adjacency: dict[int, set[int]] = defaultdict(set)

    for room in global_rooms.values():
        exit_targets = room.exit_targets_by_direction()
        report.scanned_exits += len(room.exits)

        for direction, targets in exit_targets.items():
            if len(targets) > 1:
                report.add(
                    "error",
                    "duplicate-exit-direction",
                    (
                        f"Room {room.vnum} in area '{room.area_name}' defines multiple '{direction}' exits: "
                        f"{targets}"
                    ),
                    relpath(room.path),
                )

        for exit_data in room.exits:
            if not exit_data.direction:
                report.add(
                    "error",
                    "missing-exit-direction",
                    f"Room {room.vnum} has an exit block without Direction.",
                    relpath(room.path),
                )
                continue

            if exit_data.direction not in VALID_DIRECTIONS:
                report.add(
                    "error",
                    "invalid-exit-direction",
                    (
                        f"Room {room.vnum} uses invalid direction '{exit_data.direction}'. "
                        f"Expected one of {sorted(VALID_DIRECTIONS)}."
                    ),
                    relpath(room.path),
                )
                continue

            if exit_data.target_vnum is None:
                report.add(
                    "error",
                    "missing-exit-target",
                    f"Room {room.vnum} exit '{exit_data.direction}' has no valid ExitVnum.",
                    relpath(room.path),
                )
                continue

            target_room = global_rooms.get(exit_data.target_vnum)
            if target_room is None:
                report.add(
                    "error",
                    "broken-exit",
                    (
                        f"Room {room.vnum} exit '{exit_data.direction}' points to missing room "
                        f"{exit_data.target_vnum}."
                    ),
                    relpath(room.path),
                )
                continue

            directed_adjacency[room.vnum].add(target_room.vnum)
            undirected_adjacency[room.vnum].add(target_room.vnum)
            undirected_adjacency[target_room.vnum].add(room.vnum)

            reverse_direction = REVERSE_DIRECTION[exit_data.direction]
            reverse_targets = target_room.exit_targets_by_direction().get(reverse_direction, [])
            if not reverse_targets:
                report.add(
                    "warning",
                    "missing-reverse-exit",
                    (
                        f"Room {room.vnum} exit '{exit_data.direction}' reaches {target_room.vnum}, "
                        f"but room {target_room.vnum} has no '{reverse_direction}' exit back."
                    ),
                    relpath(room.path),
                )
            elif room.vnum not in reverse_targets:
                report.add(
                    "warning",
                    "mismatched-reverse-exit",
                    (
                        f"Room {room.vnum} exit '{exit_data.direction}' reaches {target_room.vnum}, "
                        f"but the reverse '{reverse_direction}' exit points to {reverse_targets}."
                    ),
                    relpath(room.path),
                )

    component_by_room = build_components(set(global_rooms), undirected_adjacency)
    for area in areas.values():
        anchor = area.anchor_vnum()
        if anchor is None:
            continue
        anchor_component = component_by_room.get(anchor)
        if anchor_component is None:
            continue

        disconnected = sorted(
            vnum for vnum in area.rooms if component_by_room.get(vnum) != anchor_component
        )
        if not disconnected:
            continue

        orphan_rooms = [vnum for vnum in disconnected if not undirected_adjacency.get(vnum)]
        connected_elsewhere = [vnum for vnum in disconnected if undirected_adjacency.get(vnum)]

        if orphan_rooms:
            report.add(
                "warning",
                "orphan-room",
                (
                    f"Area '{area.name}' has orphan rooms with no room-link connectivity from its anchor "
                    f"{anchor}: {orphan_rooms[:10]}"
                ),
                relpath(area.path),
            )
        if connected_elsewhere:
            report.add(
                "warning",
                "disconnected-room-cluster",
                (
                    f"Area '{area.name}' has rooms not connected to its anchor {anchor}: "
                    f"{connected_elsewhere[:10]}"
                ),
                relpath(area.path),
            )

    if not args.skip_unreachable and areas:
        if args.root_area:
            root_names = args.root_area
        else:
            root_names = [
                area.name
                for area in areas.values()
                if area.capital is not None and area.capital > 0 and area.capital in area.rooms
            ]
            if not root_names and directory_entries:
                root_names = [directory_entries[0].name]
        root_vnums: list[int] = []
        for root_name in root_names:
            area = areas.get(root_name)
            if area is None:
                report.add(
                    "warning",
                    "unknown-root-area",
                    f"Requested root area '{root_name}' is not loadable from area/directory.lst.",
                    relpath(DIRECTORY_LIST),
                )
                continue
            anchor = area.anchor_vnum()
            if anchor is None:
                report.add(
                    "warning",
                    "root-area-without-anchor",
                    f"Requested root area '{root_name}' has no usable anchor room.",
                    relpath(area.path),
                )
                continue
            root_vnums.append(anchor)

        if root_vnums:
            reachable_rooms = bfs(root_vnums, directed_adjacency)
            allowed_unreachable = set(args.allow_unreachable_area)
            for area in areas.values():
                if area.name in allowed_unreachable:
                    continue
                if area.name in root_names:
                    continue
                if area.rooms and any(vnum in reachable_rooms for vnum in area.rooms):
                    continue
                report.add(
                    "warning",
                    "unreachable-area",
                    (
                        f"Area '{area.name}' is not reachable by room exits from root area(s) "
                        f"{root_names}. Teleport/job travel is not modeled by this check."
                    ),
                    relpath(area.path),
                )

    return report


def print_report(report: Report) -> None:
    print(
        "Scanned "
        f"{report.scanned_areas} areas, {report.scanned_rooms} rooms, {report.scanned_exits} exits."
    )
    print(f"Errors: {len(report.errors)}")
    print(f"Warnings: {len(report.warnings)}")

    if report.errors:
        print("\nErrors:")
        for issue in report.errors:
            location = f" ({issue.location})" if issue.location else ""
            print(f"  - [{issue.code}] {issue.message}{location}")

    if report.warnings:
        print("\nWarnings:")
        for issue in report.warnings:
            location = f" ({issue.location})" if issue.location else ""
            print(f"  - [{issue.code}] {issue.message}{location}")

    if not report.errors and not report.warnings:
        print("\nNo consistency issues found.")


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    report = run_checker(args)
    print_report(report)

    if args.json_report:
        output_path = Path(args.json_report)
        output_path.write_text(
            json.dumps(report.to_json(), ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"\nJSON report: {output_path}")

    if report.errors:
        return 1
    if args.fail_on_warning and report.warnings:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
