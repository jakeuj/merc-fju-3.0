from __future__ import annotations

import argparse
import sys
from pathlib import Path

from structured_runtime_files import (
    ROOT,
    bool_from_yes_no,
    diff_paths,
    extract_skill_runtime_contract,
    first_top_level_field,
    load_check_allowlist,
    load_symbol_allowlists,
    read_json,
    render_skill_file,
    render_skill_lst,
    skill_lst_entries,
    trim_tilde,
    write_text,
)


STRUCTURED_SKILLS_JSON = ROOT / "data/structured/skills/skills.json"


def load_structured_skills() -> dict:
    return read_json(STRUCTURED_SKILLS_JSON)


def validate_structured_skills(data: dict) -> list[str]:
    errors: list[str] = []
    allowlists = load_symbol_allowlists()
    valid_checks = load_check_allowlist()
    seen_names: set[str] = set()
    seen_runtime_paths: set[str] = set()
    seen_lst_keys: set[str] = set()
    skill_index = {skill["english_name"]: skill for skill in data.get("skills", [])}

    for skill in data.get("skills", []):
        name = skill.get("english_name")
        if not name:
            errors.append("Skill entry missing english_name.")
            continue
        if name in seen_names:
            errors.append(f"Duplicate english_name: {name}")
        seen_names.add(name)

        contract = skill.get("runtime_contract") or {}
        runtime_path = contract.get("skill_file")
        slot_symbol = contract.get("slot_symbol")
        lst_key = contract.get("skill_lst_key")

        if not runtime_path:
            errors.append(f"{name}: missing runtime_contract.skill_file")
        elif runtime_path in seen_runtime_paths:
            errors.append(f"Duplicate runtime target path: {runtime_path}")
        else:
            seen_runtime_paths.add(runtime_path)

        if not slot_symbol:
            errors.append(f"{name}: missing slot_symbol")
        if not lst_key:
            errors.append(f"{name}: missing skill_lst_key")
        elif lst_key in seen_lst_keys:
            errors.append(f"Duplicate skill_lst key in runtime_contract: {lst_key}")
        else:
            seen_lst_keys.add(lst_key)

        type_value = contract.get("type")
        if type_value and type_value not in allowlists["type"]:
            errors.append(f"{name}: illegal Type {type_value}")

        cost_type = contract.get("cost_type")
        if cost_type and cost_type not in allowlists["cost_type"]:
            errors.append(f"{name}: illegal CostType {cost_type}")

        weapon = contract.get("weapon")
        if weapon and weapon not in allowlists["weapon"]:
            errors.append(f"{name}: illegal Weapon {weapon}")

        check = contract.get("check")
        if check and check not in valid_checks:
            errors.append(f"{name}: illegal Check {check}")

        document = skill.get("document") or []
        doc_name = trim_tilde(first_top_level_field(document, "Name"))

        if doc_name and doc_name != name:
            errors.append(f"{name}: document Name mismatch ({doc_name})")

    skill_lst_doc = data.get("skill_lst") or {}
    lst_entries = skill_lst_entries(skill_lst_doc)
    lst_seen: set[str] = set()
    for entry in lst_entries:
        key = entry["key"]
        if key in lst_seen:
            errors.append(f"Duplicate skill.lst key: {key}")
        lst_seen.add(key)
        skill = next((item for item in data.get("skills", []) if (item.get("runtime_contract") or {}).get("skill_lst_key") == key), None)
        if skill is None:
            errors.append(f"skill.lst entry {key} has no matching skill definition")
            continue
        expected = skill.get("runtime_contract") or {}
        contract = extract_skill_runtime_contract(
            {
                "relative_path": expected.get("skill_file"),
                "document": skill.get("document") or [],
            },
            entry,
        )
        for field_name in ("skill_lst_key", "slot_number", "slot_symbol", "skill_file", "type", "cost_type", "weapon", "check"):
            if expected.get(field_name) != contract.get(field_name):
                errors.append(
                    f"{skill['english_name']}: runtime_contract.{field_name} mismatch "
                    f"(expected {expected.get(field_name)!r}, got {contract.get(field_name)!r})"
                )

    entry_keys = {entry["key"] for entry in lst_entries}
    for skill in data.get("skills", []):
        contract = skill.get("runtime_contract") or {}
        if contract.get("skill_lst_key") not in entry_keys:
            errors.append(f"{skill['english_name']}: missing skill.lst entry")

    return errors


def expected_skill_outputs(data: dict) -> dict[str, str]:
    outputs = {
        "skill/skill.lst": render_skill_lst(data["skill_lst"]),
    }
    for skill in data["skills"]:
        contract = skill["runtime_contract"]
        outputs[contract["skill_file"]] = render_skill_file(skill)
    return outputs


def run_check(data: dict) -> int:
    errors = validate_structured_skills(data)
    expected = expected_skill_outputs(data)
    actual_paths = [ROOT / "skill/skill.lst", *sorted((ROOT / "skill").rglob("*.ski"))]
    missing, extra, changed = diff_paths(expected, actual_paths)

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

    print(f"structured skill check passed for {len(data['skills'])} skills")
    return 0


def run_write(data: dict) -> int:
    errors = validate_structured_skills(data)
    if errors:
        for error in errors:
            print(f"ERROR {error}")
        return 1

    outputs = expected_skill_outputs(data)
    for relative_path, text in outputs.items():
        write_text(ROOT / relative_path, text)
        print(f"wrote {relative_path}")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Export canonical structured skill JSON to legacy runtime files.")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="Validate source JSON and compare rendered output to runtime files.")
    mode.add_argument("--write", action="store_true", help="Write rendered skill runtime files from structured JSON.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    data = load_structured_skills()
    if args.check:
        raise SystemExit(run_check(data))
    raise SystemExit(run_write(data))


if __name__ == "__main__":
    main()
