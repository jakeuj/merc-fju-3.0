#!/usr/bin/env python3
"""Summarize Merc startup logs and debug outputs for area validation."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
LOG_ROOT = REPO_ROOT / "log"
DEBUG_ROOT = REPO_ROOT / "debug"
SUCCESS_PATTERNS = [
    re.compile(r"三國歪傳之降龍伏虎開始正常運作"),
]
ERROR_PATTERNS = {
    "load_room": re.compile(r"Load_room", re.IGNORECASE),
    "duplicate": re.compile(r"duplicate", re.IGNORECASE),
    "parse_error": re.compile(r"parse error", re.IGNORECASE),
    "load_mobiles": re.compile(r"load_mobiles", re.IGNORECASE),
    "reset": re.compile(r"reset", re.IGNORECASE),
    "unknown": re.compile(r"unknown", re.IGNORECASE),
    "vnum": re.compile(r"vnum", re.IGNORECASE),
    "open_failure": re.compile(r"(can't open|cannot open|open failed|open error)", re.IGNORECASE),
}


def newest_log_file(log_root: Path) -> Path | None:
    logs = sorted(log_root.glob("*.log"), key=lambda path: path.stat().st_mtime)
    return logs[-1] if logs else None


def summarize_log_file(path: Path) -> dict:
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError as exc:
        return {
            "path": str(path),
            "exists": False,
            "error": str(exc),
            "success": False,
            "matches": {},
            "matched_lines": []
        }

    matched_lines: list[dict[str, str | int]] = []
    matches = {key: 0 for key in ERROR_PATTERNS}
    success = False

    for line_no, line in enumerate(lines, start=1):
        if any(pattern.search(line) for pattern in SUCCESS_PATTERNS):
            success = True
            matched_lines.append({"kind": "success", "line": line_no, "text": line})
        for kind, pattern in ERROR_PATTERNS.items():
            if pattern.search(line):
                matches[kind] += 1
                matched_lines.append({"kind": kind, "line": line_no, "text": line})

    return {
        "path": str(path),
        "exists": True,
        "success": success,
        "matches": matches,
        "matched_lines": matched_lines[:100]
    }


def summarize_debug_dir(debug_root: Path) -> dict:
    files = []
    for debug_file in sorted(debug_root.glob("*")):
        if not debug_file.is_file():
            continue
        try:
            content = debug_file.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            files.append({"path": str(debug_file), "error": str(exc), "non_empty": True})
            continue
        stripped = content.strip()
        files.append(
            {
                "path": str(debug_file),
                "non_empty": bool(stripped),
                "preview": stripped.splitlines()[:5] if stripped else []
            }
        )
    non_empty = [entry for entry in files if entry.get("non_empty")]
    return {"files": files, "non_empty_count": len(non_empty), "non_empty_files": non_empty}


def build_summary(log_file: Path | None, debug_dir: Path) -> dict:
    if log_file is None:
        log_summary = {
            "path": None,
            "exists": False,
            "success": False,
            "matches": {},
            "matched_lines": []
        }
    else:
        log_summary = summarize_log_file(log_file)

    debug_summary = summarize_debug_dir(debug_dir)
    return {
        "log": log_summary,
        "debug": debug_summary
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Summarize Merc startup logs and debug files.")
    parser.add_argument(
        "log_file",
        nargs="?",
        type=Path,
        help="Specific log file to summarize. Defaults to the newest file in log/.",
    )
    parser.add_argument(
        "--debug-dir",
        type=Path,
        default=DEBUG_ROOT,
        help="Debug directory to inspect. Default: ./debug",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print machine-readable JSON output.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    log_file = args.log_file.resolve() if args.log_file else newest_log_file(LOG_ROOT)
    summary = build_summary(log_file, args.debug_dir.resolve())

    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    else:
        log_summary = summary["log"]
        debug_summary = summary["debug"]
        print(f"Log file: {log_summary['path']}")
        print(f"Startup success signal: {'yes' if log_summary['success'] else 'no'}")
        if log_summary["matches"]:
            print("Keyword matches:")
            for kind, count in log_summary["matches"].items():
                if count:
                    print(f"- {kind}: {count}")
        print(f"Non-empty debug files: {debug_summary['non_empty_count']}")
        for entry in debug_summary["non_empty_files"]:
            print(f"- {entry['path']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
