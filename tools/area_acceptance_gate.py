#!/usr/bin/env python3
"""Recommend a delivery gate for an area based on current evidence."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
TOOLS_ROOT = REPO_ROOT / "tools"


def run_json_command(command: list[str]) -> tuple[int, dict]:
    result = subprocess.run(command, capture_output=True, text=True, cwd=REPO_ROOT)
    payload = {}
    if result.stdout.strip():
        payload = json.loads(result.stdout)
    return result.returncode, payload


def directory_entry_exists(area_slug: str) -> bool:
    directory_list = REPO_ROOT / "area" / "directory.lst"
    if not directory_list.exists():
        return False
    for line in directory_list.read_text(encoding="utf-8", errors="replace").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("*"):
            continue
        if stripped.split()[0] == area_slug:
            return True
    return False


def runtime_shape(area_dir: Path) -> dict[str, object]:
    expected_dirs = ["mob", "obj", "res", "roo", "shp"]
    existing_dirs = {name: (area_dir / name).is_dir() for name in expected_dirs}
    roo_files = sorted((area_dir / "roo").glob("*.roo")) if existing_dirs["roo"] else []
    return {
        "area_dir_exists": area_dir.is_dir(),
        "index_exists": (area_dir / "index").is_file(),
        "existing_dirs": existing_dirs,
        "roo_count": len(roo_files),
        "has_runtime_shape": (area_dir / "index").is_file() and len(roo_files) > 0
    }


def recommend_gate(spec_ok: bool, runtime: dict[str, object], log_summary: dict | None) -> tuple[str, list[str]]:
    reasons: list[str] = []
    if not spec_ok:
        reasons.append("spec validation still has errors")
        return "blocked", reasons

    if not runtime["has_runtime_shape"]:
        reasons.append("spec is valid but runtime asset shape is not complete yet")
        return "spec_ready_for_commit", reasons

    reasons.append("runtime asset shape exists")

    if log_summary is None:
        reasons.append("no log/debug evidence supplied; cannot recommend advance gate")
        return "implementation_ready_for_commit", reasons

    log_info = log_summary["log"]
    debug_info = log_summary["debug"]
    error_like = sum(log_info.get("matches", {}).values())
    if error_like:
        reasons.append("log contains loader-style keywords that need review")
        return "blocked", reasons
    if debug_info.get("non_empty_count", 0):
        reasons.append("debug directory has non-empty files that need manual review")
        return "implementation_ready_for_commit", reasons
    if not log_info.get("success", False):
        reasons.append("no startup success signal found in log")
        return "implementation_ready_for_commit", reasons

    reasons.append("startup success signal found and no log/debug blockers detected")
    return "validated_ready_to_advance", reasons


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Recommend a delivery gate for an area.")
    parser.add_argument("area_slug", help="Area slug, e.g. loyang_outskirts")
    parser.add_argument(
        "--map-md",
        type=Path,
        help="Override path to map.md. Defaults to area/<slug>/map.md",
    )
    parser.add_argument(
        "--log-file",
        type=Path,
        help="Optional startup log file to combine with the gate recommendation.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print machine-readable JSON output.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    area_slug = args.area_slug
    area_dir = REPO_ROOT / "area" / area_slug
    map_md = args.map_md.resolve() if args.map_md else (area_dir / "map.md")

    spec_returncode, spec_summary = run_json_command(
        [sys.executable, str(TOOLS_ROOT / "mapmd_validate.py"), str(map_md), "--json"]
    )
    runtime_summary = runtime_shape(area_dir)
    runtime_summary["directory_entry_exists"] = directory_entry_exists(area_slug)

    log_summary = None
    if args.log_file:
        _, log_summary = run_json_command(
            [sys.executable, str(TOOLS_ROOT / "log_parse_summary.py"), str(args.log_file.resolve()), "--json"]
        )

    recommended_gate, reasons = recommend_gate(spec_returncode == 0, runtime_summary, log_summary)

    result = {
        "area_slug": area_slug,
        "map_md": str(map_md),
        "recommended_gate": recommended_gate,
        "reasons": reasons,
        "spec_summary": spec_summary,
        "runtime_summary": runtime_summary,
        "log_summary": log_summary
    }

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Area: {area_slug}")
        print(f"Recommended gate: {recommended_gate}")
        print("Reasons:")
        for reason in reasons:
            print(f"- {reason}")
        print("")
        print(f"Spec errors: {spec_summary.get('error_count', 'n/a')}")
        print(f"Spec warnings: {spec_summary.get('warning_count', 'n/a')}")
        print(f"Has runtime shape: {runtime_summary['has_runtime_shape']}")
        print(f"Directory entry exists: {runtime_summary['directory_entry_exists']}")
        if log_summary is not None:
            print(f"Startup success signal: {log_summary['log']['success']}")
            print(f"Non-empty debug files: {log_summary['debug']['non_empty_count']}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
