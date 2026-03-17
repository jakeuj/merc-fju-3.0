#!/usr/bin/env python3
"""Suggest the next reserved_room_block for a new area.

This tool scans current runtime room files plus reserved blocks recorded in
spec/planning files, then recommends the next `xx01-xxNN` block using the repo's
headroom policy.
"""

from __future__ import annotations

import argparse
import json
import math
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


REPO_ROOT = Path(__file__).resolve().parents[1]
AREA_ROOT = REPO_ROOT / "area"
PLANS_AREA_ROOT = REPO_ROOT / "plans" / "area"
BLOCK_PATTERNS = [
    re.compile(r'"reserved_room_block"\s*:\s*"(?P<start>\d+)-(?P<end>\d+)"'),
    re.compile(r'"planned_vnum_range"\s*:\s*"(?P<start>\d+)-(?P<end>\d+)"'),
    re.compile(r"reserved_room_block\s*:\s*`?(?P<start>\d+)-(?P<end>\d+)`?", re.IGNORECASE),
    re.compile(r"planned_vnum_range\s*:\s*`?(?P<start>\d+)-(?P<end>\d+)`?", re.IGNORECASE),
    re.compile(r"ReservedRoomBlock\s*:\s*`?(?P<start>\d+)-(?P<end>\d+)`?"),
]
ROOM_FILE_RE = re.compile(r"^(?P<vnum>\d+)\.roo$")


@dataclass(frozen=True)
class BlockRecord:
    start: int
    end: int
    source: str
    kind: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Suggest the next reserved_room_block for a new Merc-FJU area."
    )
    parser.add_argument(
        "--estimated-rooms",
        type=int,
        default=12,
        help="Estimated room count for the first version of the new area. Default: 12.",
    )
    parser.add_argument(
        "--headroom",
        type=int,
        default=8,
        help="Extra room headroom to reserve before rounding. Default: 8.",
    )
    parser.add_argument(
        "--start-hundred",
        type=int,
        help="Optional explicit hundred-band base, e.g. 10000 to start searching from 10001.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print machine-readable JSON output.",
    )
    return parser.parse_args()


def collect_runtime_room_records() -> list[BlockRecord]:
    records: list[BlockRecord] = []
    for room_file in AREA_ROOT.glob("*/roo/*.roo"):
        match = ROOM_FILE_RE.match(room_file.name)
        if not match:
            continue
        vnum = int(match.group("vnum"))
        records.append(
            BlockRecord(start=vnum, end=vnum, source=str(room_file.relative_to(REPO_ROOT)), kind="room")
        )
    return records


def collect_reserved_block_records(paths: Iterable[Path], kind: str) -> list[BlockRecord]:
    records: list[BlockRecord] = []
    for path in paths:
        try:
            content = path.read_text(encoding="utf-8")
        except OSError:
            continue
        seen: set[tuple[int, int]] = set()
        for pattern in BLOCK_PATTERNS:
            for match in pattern.finditer(content):
                start = int(match.group("start"))
                end = int(match.group("end"))
                if end < start:
                    continue
                key = (start, end)
                if key in seen:
                    continue
                seen.add(key)
                records.append(
                    BlockRecord(
                        start=start,
                        end=end,
                        source=str(path.relative_to(REPO_ROOT)),
                        kind=kind,
                    )
                )
    return records


def compute_block_size(estimated_rooms: int, headroom: int) -> int:
    if estimated_rooms <= 0:
        raise ValueError("--estimated-rooms must be positive.")
    if headroom < 0:
        raise ValueError("--headroom cannot be negative.")
    return int(math.ceil((estimated_rooms + headroom) / 10.0) * 10)


def block_overlaps(candidate_start: int, candidate_end: int, occupied: list[BlockRecord]) -> bool:
    return any(not (candidate_end < record.start or candidate_start > record.end) for record in occupied)


def pick_start_hundred(occupied: list[BlockRecord], explicit: int | None) -> int:
    if explicit is not None:
        if explicit < 0 or explicit % 100 != 0:
            raise ValueError("--start-hundred must be a non-negative multiple of 100.")
        return explicit

    if not occupied:
        return 0

    max_end = max(record.end for record in occupied)
    return (max_end // 100 + 1) * 100


def recommend_block(occupied: list[BlockRecord], block_size: int, start_hundred: int) -> tuple[int, int]:
    if block_size <= 0:
        raise ValueError("Computed block size must be positive.")
    if block_size > 99:
        raise ValueError("Computed block size exceeds a single hundred-band.")

    hundred = start_hundred
    while True:
        candidate_start = hundred + 1
        candidate_end = candidate_start + block_size - 1
        if candidate_end >= hundred + 100:
            hundred += 100
            continue
        if not block_overlaps(candidate_start, candidate_end, occupied):
            return candidate_start, candidate_end
        hundred += 100


def main() -> int:
    args = parse_args()
    block_size = compute_block_size(args.estimated_rooms, args.headroom)

    occupied = []
    occupied.extend(collect_runtime_room_records())
    occupied.extend(collect_reserved_block_records(AREA_ROOT.glob("*/map.md"), kind="map-md"))
    occupied.extend(collect_reserved_block_records(PLANS_AREA_ROOT.glob("*.md"), kind="plan"))
    occupied.sort(key=lambda record: (record.start, record.end, record.kind, record.source))

    start_hundred = pick_start_hundred(occupied, args.start_hundred)
    recommended_start, recommended_end = recommend_block(occupied, block_size, start_hundred)

    result = {
      "estimated_rooms": args.estimated_rooms,
      "headroom": args.headroom,
      "block_size": block_size,
      "recommended_block": f"{recommended_start}-{recommended_end}",
      "recommended_start": recommended_start,
      "recommended_end": recommended_end,
      "scan_summary": {
        "runtime_room_files": sum(1 for record in occupied if record.kind == "room"),
        "map_md_blocks": sum(1 for record in occupied if record.kind == "map-md"),
        "plan_blocks": sum(1 for record in occupied if record.kind == "plan")
      },
      "sample_conflicts": [
        {
          "kind": record.kind,
          "range": f"{record.start}-{record.end}",
          "source": record.source
        }
        for record in occupied[-10:]
      ]
    }

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Estimated rooms: {args.estimated_rooms}")
        print(f"Headroom: {args.headroom}")
        print(f"Computed block size: {block_size}")
        print(f"Recommended reserved_room_block: {recommended_start}-{recommended_end}")
        print("")
        print("Recent occupied ranges considered:")
        for record in occupied[-10:]:
            print(f"- [{record.kind}] {record.start}-{record.end} ({record.source})")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
