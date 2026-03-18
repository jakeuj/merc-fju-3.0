from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIELD_WIDTH = 16
SKILL_ENTRY_PATTERN = re.compile(
    r"^(?P<key>\S+)"
    r"(?P<between_key_and_star>\s+)\*"
    r"(?P<between_star_and_label>\s+)"
    r"(?P<label>技能(?:號碼|編號))"
    r"(?P<between_label_and_number>\s+)"
    r"(?P<number>\d+)"
    r"(?P<between_number_and_slot>\s+)"
    r"(?P<slot>SLOT_\S+)"
    r"(?P<trailing>.*)$"
)
SCALAR_LINE_PATTERN = re.compile(r"^(?P<key>\S+)(?:\s{2,}|\t+)(?P<value>.*)$")
SYMBOL_PATTERN = re.compile(r"\b(?P<symbol>(?:TAR|COST|WEAPON)_[A-Z0-9_]+)\b")
CHECK_PATTERN = re.compile(r"\b(check_[A-Za-z0-9_]+)\b")
RESET_ARG_TOKEN = re.compile(r"^-?\d+$|^[A-Z_]+$|^[a-z_]+$")
BLOCK_FIELD_KEYS = {"description", "help", "message"}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def parse_scalar_line(line: str) -> tuple[str, str] | None:
    match = SCALAR_LINE_PATTERN.match(line)
    if not match:
        return None
    return match.group("key"), match.group("value")


def normalize_key(key: str) -> str:
    return key.strip().lower()


def render_scalar_field(key: str, value: str) -> str:
    return f"{key:<{FIELD_WIDTH}}{value}"


def parse_document_nodes(lines: list[str], start: int = 0, *, allow_sections: bool = False) -> tuple[list[dict], int]:
    nodes: list[dict] = []
    index = start
    while index < len(lines):
        line = lines[index]
        if line == "End":
            return nodes, index + 1
        if line == "":
            nodes.append({"kind": "blank"})
            index += 1
            continue
        if line.lstrip().startswith("*"):
            nodes.append({"kind": "raw", "text": line})
            index += 1
            continue
        if allow_sections and line.startswith("#"):
            section_name = line[1:].strip()
            section_nodes, index = parse_document_nodes(lines, index + 1, allow_sections=False)
            nodes.append({"kind": "section", "name": section_name, "entries": section_nodes})
            continue
        scalar = parse_scalar_line(line)
        if scalar:
            key, value = scalar
            if value == "" and normalize_key(key) in BLOCK_FIELD_KEYS:
                block_node, index = parse_block_field(lines, index, key)
                nodes.append(block_node)
                continue
            nodes.append({"kind": "field", "key": key, "value": value})
            index += 1
            continue

        key = line.strip()
        block_node, index = parse_block_field(lines, index, key)
        nodes.append(block_node)
    raise ValueError("Document is missing terminal 'End'")


def parse_block_field(lines: list[str], index: int, key: str) -> tuple[dict, int]:
    block_lines: list[str] = []
    terminator_style = "line"
    index += 1
    while index < len(lines):
        current = lines[index]
        if current == "~":
            terminator_style = "line"
            break
        if current.endswith("~"):
            block_lines.append(current[:-1])
            terminator_style = "inline"
            break
        block_lines.append(current)
        index += 1
    if index >= len(lines):
        raise ValueError(f"Unterminated block field '{key}'")
    return {"kind": "block_field", "key": key, "lines": block_lines, "terminator_style": terminator_style}, index + 1


def render_document_nodes(nodes: list[dict]) -> list[str]:
    lines: list[str] = []
    for node in nodes:
        kind = node["kind"]
        if kind == "blank":
            lines.append("")
        elif kind == "field":
            lines.append(render_scalar_field(node["key"], node["value"]))
        elif kind == "raw":
            lines.append(node["text"])
        elif kind == "block_field":
            lines.append(node["key"])
            block_lines = list(node["lines"])
            if node.get("terminator_style") == "inline":
                if block_lines:
                    block_lines[-1] = block_lines[-1] + "~"
                else:
                    block_lines.append("~")
                lines.extend(block_lines)
            else:
                lines.extend(block_lines)
                lines.append("~")
        elif kind == "section":
            lines.append(f"#{node['name']}")
            lines.extend(render_document_nodes(node["entries"]))
            lines.append("End")
        else:
            raise ValueError(f"Unsupported node kind: {kind}")
    return lines


def parse_skill_file(path: Path) -> dict:
    lines = read_text(path).splitlines()
    nodes, index = parse_document_nodes(lines, allow_sections=True)
    if index != len(lines):
        trailing = lines[index:]
        if any(line != "" for line in trailing):
            raise ValueError(f"Unexpected trailing content in {path}")
    return {
        "relative_path": str(path.relative_to(ROOT)).replace("\\", "/"),
        "document": nodes,
    }


def render_skill_file(skill: dict) -> str:
    lines = render_document_nodes(skill["document"])
    lines.append("End")
    return "\n".join(lines) + "\n"


def parse_skill_lst(path: Path) -> dict:
    nodes: list[dict] = []
    for line in read_text(path).splitlines():
        if line == "":
            nodes.append({"kind": "blank"})
            continue
        match = SKILL_ENTRY_PATTERN.match(line)
        if match:
            nodes.append(
                {
                    "kind": "entry",
                    "key": match.group("key"),
                    "number": int(match.group("number")),
                    "slot_symbol": match.group("slot"),
                    "format": {
                        "between_key_and_star": match.group("between_key_and_star"),
                        "between_star_and_label": match.group("between_star_and_label"),
                        "label": match.group("label"),
                        "between_label_and_number": match.group("between_label_and_number"),
                        "between_number_and_slot": match.group("between_number_and_slot"),
                        "trailing": match.group("trailing"),
                    },
                }
            )
        else:
            nodes.append({"kind": "raw", "text": line})
    return {
        "relative_path": str(path.relative_to(ROOT)).replace("\\", "/"),
        "nodes": nodes,
    }


def render_skill_lst(document: dict) -> str:
    lines: list[str] = []
    for node in document["nodes"]:
        kind = node["kind"]
        if kind == "blank":
            lines.append("")
        elif kind == "raw":
            lines.append(node["text"])
        elif kind == "entry":
            fmt = node["format"]
            lines.append(
                f"{node['key']}"
                f"{fmt['between_key_and_star']}*"
                f"{fmt['between_star_and_label']}{fmt['label']}"
                f"{fmt['between_label_and_number']}{node['number']}"
                f"{fmt['between_number_and_slot']}{node['slot_symbol']}"
                f"{fmt['trailing']}"
            )
        else:
            raise ValueError(f"Unsupported skill.lst node kind: {kind}")
    return "\n".join(lines) + "\n"


def skill_lst_entries(document: dict) -> list[dict]:
    return [node for node in document["nodes"] if node["kind"] == "entry"]


def top_level_field_map(nodes: list[dict]) -> dict[str, str]:
    fields: dict[str, str] = {}
    for node in nodes:
        if node["kind"] != "field":
            continue
        key = normalize_key(node["key"])
        if key not in fields:
            fields[key] = node["value"]
    return fields


def first_top_level_field(nodes: list[dict], key: str) -> str | None:
    wanted = normalize_key(key)
    for node in nodes:
        if node["kind"] == "field" and normalize_key(node["key"]) == wanted:
            return node["value"]
    return None


def parse_simple_kv_file(path: Path) -> dict:
    lines = read_text(path).splitlines()
    nodes, index = parse_document_nodes(lines, allow_sections=False)
    if index != len(lines):
        trailing = lines[index:]
        if any(line != "" for line in trailing):
            raise ValueError(f"Unexpected trailing content in {path}")
    return {
        "relative_path": str(path.relative_to(ROOT)).replace("\\", "/"),
        "document": nodes,
    }


def render_simple_kv_file(document: dict) -> str:
    lines = render_document_nodes(document["document"])
    lines.append("End")
    return "\n".join(lines) + "\n"


def parse_reset_line(line: str) -> dict:
    stripped = line.strip()
    if not stripped:
        return {"kind": "blank"}
    parts = stripped.split()
    opcode = parts[0]
    arguments: list[str] = []
    comment_tokens: list[str] = []
    for token in parts[1:]:
        if not comment_tokens and RESET_ARG_TOKEN.match(token):
            arguments.append(token)
        else:
            comment_tokens.append(token)
    return {
        "kind": "reset",
        "opcode": opcode,
        "arguments": arguments,
        "comment": " ".join(comment_tokens),
    }


def parse_res_file(path: Path) -> dict:
    nodes = [parse_reset_line(line) for line in read_text(path).splitlines()]
    return {
        "relative_path": str(path.relative_to(ROOT)).replace("\\", "/"),
        "nodes": nodes,
    }


def render_res_file(document: dict) -> str:
    lines: list[str] = []
    for node in document["nodes"]:
        if node["kind"] == "blank":
            lines.append("")
            continue
        text = " ".join([node["opcode"], *node.get("arguments", []), node.get("comment", "")]).rstrip()
        lines.append(text)
    return "\n".join(lines) + "\n"


def extract_skill_runtime_contract(skill: dict, skill_lst_entry: dict) -> dict:
    nodes = skill["document"]
    fields = top_level_field_map(nodes)
    return {
        "skill_lst_key": skill_lst_entry["key"],
        "slot_number": skill_lst_entry["number"],
        "slot_symbol": skill_lst_entry["slot_symbol"],
        "skill_file": skill["relative_path"],
        "function": trim_tilde(fields.get("function")),
        "type": trim_tilde(fields.get("type")),
        "cost_type": trim_tilde(fields.get("costtype")),
        "cost": to_int(fields.get("cost")),
        "wait": to_int(fields.get("wait")),
        "weapon": trim_tilde(fields.get("weapon")),
        "check": trim_tilde(fields.get("check")),
        "canask": bool_from_yes_no(fields.get("canask")),
        "teach": bool_from_yes_no(fields.get("teach")),
        "valid": bool_from_yes_no(fields.get("valid")),
        "enable": bool_from_yes_no(fields.get("enable")),
    }


def trim_tilde(value: str | None) -> str | None:
    if value is None:
        return None
    return value.rstrip("~").strip()


def to_int(value: str | None) -> int | None:
    if value is None:
        return None
    value = value.strip()
    if not value or not re.fullmatch(r"-?\d+", value):
        return None
    return int(value)


def bool_from_yes_no(value: str | None) -> bool | None:
    if value is None:
        return None
    normalized = trim_tilde(value)
    if normalized == "YES":
        return True
    if normalized == "NO":
        return False
    return None


def load_symbol_allowlists() -> dict[str, set[str]]:
    allowlists = {
        "type": set(),
        "cost_type": set(),
        "weapon": set(),
    }
    text = read_text(ROOT / "data/symbol.def")
    for symbol in SYMBOL_PATTERN.findall(text):
        if symbol.startswith("TAR_"):
            allowlists["type"].add(symbol)
        elif symbol.startswith("COST_"):
            allowlists["cost_type"].add(symbol)
        elif symbol.startswith("WEAPON_"):
            allowlists["weapon"].add(symbol)
    return allowlists


def load_check_allowlist() -> set[str]:
    checks: set[str] = set()
    for path in (ROOT / "src").glob("*.c"):
        checks.update(CHECK_PATTERN.findall(read_text(path)))
    return checks


def diff_paths(expected: dict[str, str], actual_paths: list[Path]) -> tuple[list[str], list[str], list[str]]:
    actual = {str(path.relative_to(ROOT)).replace("\\", "/"): read_text(path) for path in actual_paths}
    missing = sorted(path for path in expected if path not in actual)
    extra = sorted(path for path in actual if path not in expected)
    changed = sorted(path for path, text in expected.items() if actual.get(path) is not None and actual[path] != text)
    return missing, extra, changed


def read_json(path: Path) -> dict:
    return json.loads(read_text(path))
