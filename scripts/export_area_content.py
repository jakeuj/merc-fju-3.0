from __future__ import annotations

import argparse
from pathlib import Path

from structured_runtime_files import ROOT, diff_paths, read_json, render_res_file, render_simple_kv_file, write_text


def load_area_content(area_slug: str) -> dict:
    return read_json(ROOT / "area" / area_slug / "content.json")


def validate_area_content(area_slug: str, data: dict) -> list[str]:
    errors: list[str] = []
    if data.get("area_slug") != area_slug:
        errors.append(f"content.json area_slug mismatch: expected {area_slug}, got {data.get('area_slug')}")

    seen_paths: set[str] = set()
    for section in ("mob_files", "obj_files", "shp_files"):
        for item in data.get(section, []):
            rel = item.get("relative_path")
            if not rel:
                errors.append(f"{section}: missing relative_path")
                continue
            if rel in seen_paths:
                errors.append(f"Duplicate managed path: {rel}")
            seen_paths.add(rel)

    for item in data.get("res_files", []):
        rel = item.get("relative_path")
        if not rel:
            errors.append("res_files: missing relative_path")
            continue
        if rel in seen_paths:
            errors.append(f"Duplicate managed path: {rel}")
        seen_paths.add(rel)

    return errors


def expected_area_outputs(data: dict) -> dict[str, str]:
    outputs: dict[str, str] = {}
    for section in ("mob_files", "obj_files", "shp_files"):
        for item in data.get(section, []):
            outputs[item["relative_path"]] = render_simple_kv_file(item)
    for item in data.get("res_files", []):
        outputs[item["relative_path"]] = render_res_file(item)
    return outputs


def actual_area_paths(area_slug: str) -> list[Path]:
    area_root = ROOT / "area" / area_slug
    paths: list[Path] = []
    for child in ("mob", "obj", "res", "shp"):
        paths.extend(sorted((area_root / child).glob("*.*")))
    return paths


def run_check(area_slug: str, data: dict) -> int:
    errors = validate_area_content(area_slug, data)
    expected = expected_area_outputs(data)
    missing, extra, changed = diff_paths(expected, actual_area_paths(area_slug))
    if errors or missing or extra or changed:
        for error in errors:
            print(f"ERROR {error}")
        for path in missing:
            print(f"ERROR Missing runtime artifact: {path}")
        for path in extra:
            print(f"ERROR Unmanaged runtime artifact: {path}")
        for path in changed:
            print(f"ERROR Drift detected: {path}")
        return 1
    print(f"area content check passed for {area_slug}")
    return 0


def run_write(area_slug: str, data: dict) -> int:
    errors = validate_area_content(area_slug, data)
    if errors:
        for error in errors:
            print(f"ERROR {error}")
        return 1
    for relative_path, text in expected_area_outputs(data).items():
        write_text(ROOT / relative_path, text)
        print(f"wrote {relative_path}")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Export canonical per-area content JSON to legacy runtime files.")
    parser.add_argument("area_slug", help="Target area slug, for example loyang_outskirts")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="Validate source JSON and compare rendered output to runtime files.")
    mode.add_argument("--write", action="store_true", help="Write rendered area content files from structured JSON.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    data = load_area_content(args.area_slug)
    if args.check:
        raise SystemExit(run_check(args.area_slug, data))
    raise SystemExit(run_write(args.area_slug, data))


if __name__ == "__main__":
    main()
