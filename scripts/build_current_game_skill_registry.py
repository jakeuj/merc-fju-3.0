from __future__ import annotations

import json
import re
from collections import defaultdict
from html import unescape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEGACY_SKILLS_JSON = ROOT / "docs/3yWebsite/docs/data/skills.json"
LEGACY_SKILL_DIR = ROOT / "docs/3yWebsite/skill"
CURRENT_SKILLS_JSON = ROOT / "docs/current-game/skills.json"


NPC_RUNTIME_SKILLS = {
    "military blade": {
        "chinese_name": "鎮軍刀法",
        "family": "npc-military",
        "intended_roles": ["城市守衛", "城門守衛", "禁軍護衛"],
    },
    "military steps": {
        "chinese_name": "鎮軍步",
        "family": "npc-military",
        "intended_roles": ["城市守軍", "騎卒", "低中階軍職 NPC"],
    },
    "imperial sword": {
        "chinese_name": "禁城御劍",
        "family": "npc-imperial",
        "intended_roles": ["殿前護衛", "御前護衛", "皇宮禁衛軍高階樣本"],
    },
    "imperial steps": {
        "chinese_name": "龍驤御步",
        "family": "npc-imperial",
        "intended_roles": ["殿前護衛", "御前護衛"],
    },
    "night blade": {
        "chinese_name": "夜梟奪命刀",
        "family": "npc-night",
        "intended_roles": ["盜賊", "浪人", "大盜類 NPC"],
    },
    "shadowtrace steps": {
        "chinese_name": "流影換形步",
        "family": "npc-night",
        "intended_roles": ["盜賊", "浪人", "大盜類 NPC"],
    },
    "cavalry lance": {
        "chinese_name": "驍騎槍式",
        "family": "npc-military",
        "intended_roles": ["騎兵", "持槍軍職 NPC"],
    },
}


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_existing_registry() -> dict[str, dict]:
    if not CURRENT_SKILLS_JSON.exists():
        return {}
    data = read_json(CURRENT_SKILLS_JSON)
    return {item["english_name"]: item for item in data.get("skills", []) if item.get("english_name")}


def load_skill_lst() -> dict[str, str]:
    out: dict[str, str] = {}
    pattern = re.compile(r"^(\S+)\s+\*\s+技能(?:號碼|編號)\s+\d+\s+(SLOT_\S+)$")
    for line in (ROOT / "skill/skill.lst").read_text(encoding="utf-8", errors="ignore").splitlines():
        m = pattern.match(line.strip())
        if m:
            out[m.group(1)] = m.group(2)
    return out


def parse_runtime_skills(skill_lst: dict[str, str]) -> dict[str, dict]:
    runtime_by_name: dict[str, dict] = {}
    for ski in (ROOT / "skill").rglob("*.ski"):
        lines = ski.read_text(encoding="utf-8", errors="ignore").splitlines()
        runtime_name = next((line.split(None, 1)[1].rstrip("~").strip() for line in lines if line.startswith("Name")), None)
        if not runtime_name:
            continue

        def get(prefix: str) -> str | None:
            for line in lines:
                if line.startswith(prefix):
                    return line[len(prefix) :].strip().rstrip("~")
            return None

        damage_values: list[int] = []
        chance_values: list[int] = []
        parry_values: list[int] = []
        innate_values: list[str] = []
        for line in lines:
            if line.startswith("Value"):
                try:
                    damage_values.append(int(line.split()[-1]))
                except Exception:
                    pass
            elif line.startswith("Chance"):
                try:
                    chance_values.append(int(line.split()[-1]))
                except Exception:
                    pass
            elif line.startswith("Parry"):
                try:
                    parry_values.append(int(line.split()[-1]))
                except Exception:
                    pass
            elif line.startswith("Innate") and not re.match(r"^Innate\s+(YES|NO)\s*$", line):
                innate_values.append(" ".join(line.split()[1:]))

        stem = ski.stem

        def to_int(value: str | None) -> int | None:
            return int(value) if value and value.isdigit() else None

        runtime = {
            "exists": True,
            "skill_file": str(ski.relative_to(ROOT)).replace("\\", "/"),
            "skill_lst_key": stem if stem in skill_lst else None,
            "slot_symbol": get("Slot            ") or skill_lst.get(stem),
            "type": get("Type            "),
            "cost": to_int(get("Cost            ")),
            "cost_type": get("Costtype        "),
            "wait": to_int(get("Wait            ")),
            "weapon": get("Weapon          "),
            "check": get("Check           "),
            "associate": get("Associate       "),
            "canask": {"YES": True, "NO": False}.get(get("CanAsk          ")),
            "teach": {"YES": True, "NO": False}.get(get("Teach           ")),
            "valid": {"YES": True, "NO": False}.get(get("Valid           ")),
            "enable": {"YES": True, "NO": False}.get(get("Enable          ")),
        }
        combat = {
            "damage_values": damage_values,
            "chance_values": chance_values,
            "parry_values": parry_values,
            "innate_values": innate_values,
            "wait": runtime["wait"],
            "cost": runtime["cost"],
            "cost_type": runtime["cost_type"],
            "weapon": runtime["weapon"],
            "check": runtime["check"],
            "prepared_for_adjustment": True,
            "notes": [],
        }
        runtime["combat_dimensions"] = combat
        runtime_by_name[runtime_name] = runtime
    return runtime_by_name


def html_to_text(fragment: str) -> str:
    text = fragment
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.I)
    text = re.sub(r"</p>", "\n", text, flags=re.I)
    text = re.sub(r"<[^>]+>", "", text)
    text = unescape(text)
    text = text.replace("\r", "")
    text = re.sub(r"\n{2,}", "\n", text)
    return text.strip()


FIELD_LABELS = [
    "英文名稱",
    "中文名稱",
    "攻擊武器",
    "互相教導",
    "技能功能",
    "技能分類",
    "浪費數值",
    "領悟技能",
    "領悟機率",
    "預備功夫",
    "職業限制",
    "限 制",
    "教 導",
]


def normalize_inline(text: str | None) -> str | None:
    if text is None:
        return None
    return re.sub(r"\s+", " ", text).strip()


def parse_page_leaf(html: str, fallback: str) -> str:
    m = re.search(r"<b>([^<]+)</b>", html, flags=re.I)
    return html_to_text(m.group(1)) if m else fallback


def parse_labeled_sections(text: str) -> dict[str, str]:
    matches = list(re.finditer(r"(英文名稱|中文名稱|攻擊武器|互相教導|技能功能|技能分類|浪費數值|領悟技能|領悟機率|預備功夫|職業限制|限 制|教 導)﹕", text))
    out: dict[str, str] = {}
    for i, match in enumerate(matches):
        label = match.group(1)
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        out[label] = text[start:end].strip()
    return out


def clean_lines(block: str | None) -> list[str]:
    if not block:
        return []
    return [line.strip() for line in block.splitlines() if line.strip()]


def parse_class_limits(lines: list[str]) -> list[dict]:
    out = []
    for line in lines:
        if "不能學習" in line:
            job = line.split("不能學習", 1)[0].strip()
            out.append({"job": job, "learnable": False, "raw": line})
            continue
        m = re.match(r"(.+?)則等級最低要\s*(.+?)才能學習﹐熟練度最高可以到(.+)", line)
        if m:
            out.append(
                {
                    "job": m.group(1).strip(),
                    "min_level": m.group(2).strip(),
                    "max_proficiency": m.group(3).strip(),
                    "learnable": True,
                    "raw": line,
                }
            )
        else:
            out.append({"raw": line})
    return out


def parse_restrictions(lines: list[str]) -> dict:
    result = {
        "attribute_limits": [],
        "skill_prerequisites": [],
        "class_requirements": [],
        "raw_lines": lines,
    }
    for line in lines:
        stripped = re.sub(r"^[一二三四五六七八九十]+、", "", line).strip()
        if "本技能沒有任何限制" in stripped:
            result["no_extra_limits"] = True
            continue
        m_attr = re.match(r"本技能限制(.+?)不能低於(.+?)。?$", stripped)
        if m_attr and not m_attr.group(1).startswith("技能") and m_attr.group(1) != "職業限制為 (":
            result["attribute_limits"].append({"attribute": m_attr.group(1).strip(), "minimum": m_attr.group(2).strip(), "raw": stripped})
            continue
        m_skill = re.match(r"本技能限制技能(.+?)熟練度不能低於為(.+?)。?$", stripped)
        if m_skill:
            result["skill_prerequisites"].append({"skill": m_skill.group(1).strip(), "minimum": m_skill.group(2).strip(), "raw": stripped})
            continue
        m_class = re.match(r"本技能限制職業限制為\s*(.+)$", stripped)
        if m_class:
            classes = re.findall(r"\(([^()]+)\)", m_class.group(1))
            result["class_requirements"].append({"allowed_classes": classes, "raw": stripped})
            continue
    return result


def parse_teachers(lines: list[str]) -> list[dict]:
    out = []
    for line in lines:
        stripped = re.sub(r"^[一二三四五六七八九十]+、", "", line).strip()
        if "對不起﹐這種技能沒有人教導" in stripped:
            out.append({"available": False, "raw": stripped})
            continue
        m = re.match(r"(.+?)的(.+?)\(([^()]+)\)有教導(.+?)﹐(.+?)﹐費用\s*(.+?)。?$", stripped)
        if m:
            out.append(
                {
                    "location": m.group(1).strip(),
                    "teacher_name": m.group(2).strip(),
                    "teacher_id": m.group(3).strip(),
                    "teaches": m.group(4).strip(),
                    "attitude": m.group(5).strip(),
                    "cost": m.group(6).strip(),
                    "available": True,
                    "raw": stripped,
                }
            )
        else:
            out.append({"raw": stripped})
    return out


def parse_html_page(page: Path) -> list[dict]:
    html = page.read_text(encoding="utf-8", errors="ignore")
    if page.name in {"index.html"}:
        return []
    leaf = parse_page_leaf(html, page.stem)
    page_path = f"docs/3yWebsite/skill/{page.name}"
    blocks = re.findall(r'<a name="\d+"></a>(.*?)(?:<a href="#top">|</table>\s*</td>\s*</tr>)', html, flags=re.S | re.I)
    entries = []
    for block in blocks:
        text = html_to_text(block)
        fields = parse_labeled_sections(text)
        english_name = normalize_inline(fields.get("英文名稱"))
        chinese_name = normalize_inline(fields.get("中文名稱"))
        if not english_name or not chinese_name:
            continue
        legacy_catalog = {
            "path": f"skill/{page.name}",
            "category": None,
            "英文名稱": english_name,
            "中文名稱": chinese_name,
            "攻擊武器": normalize_inline(fields.get("攻擊武器")),
            "互相教導": normalize_inline(fields.get("互相教導")),
            "技能功能": normalize_inline(fields.get("技能功能")),
            "技能分類": normalize_inline(fields.get("技能分類")),
            "浪費數值": normalize_inline(fields.get("浪費數值")),
            "領悟技能": normalize_inline(fields.get("領悟技能")),
            "領悟機率": normalize_inline(fields.get("領悟機率")),
            "預備功夫": normalize_inline(fields.get("預備功夫")),
        }
        class_lines = clean_lines(fields.get("職業限制"))
        restriction_lines = clean_lines(fields.get("限 制"))
        teaching_lines = clean_lines(fields.get("教 導"))
        entries.append(
            {
                "english_name": english_name,
                "chinese_name": chinese_name,
                "page_path": page_path,
                "leaf": leaf,
                "legacy_catalog": legacy_catalog,
                "legacy_requirements": {
                    "class_limits": parse_class_limits(class_lines),
                    "restrictions": parse_restrictions(restriction_lines),
                    "teaching_sources": parse_teachers(teaching_lines),
                },
            }
        )
    return entries


def navigation_group_for_page(path: str) -> str:
    mapping = {
        "skill/axe.html": "武器技能",
        "skill/blade.html": "武器技能",
        "skill/bow.html": "武器技能",
        "skill/lance.html": "武器技能",
        "skill/stick.html": "武器技能",
        "skill/whip.html": "武器技能",
        "skill/fan.html": "武器技能",
        "skill/dagger.html": "武器技能",
        "skill/fist.html": "武器技能",
        "skill/sword.html": "武器技能",
        "skill/energy.html": "武器技能",
        "skill/fire.html": "法術技能",
        "skill/wind.html": "法術技能",
        "skill/light.html": "法術技能",
        "skill/holy.html": "法術技能",
        "skill/thunder.html": "法術技能",
        "skill/water.html": "法術技能",
        "skill/earth.html": "法術技能",
        "skill/dark.html": "法術技能",
        "skill/evil.html": "法術技能",
        "skill/poison.html": "法術技能",
        "skill/general.html": "職業技能",
        "skill/bravo.html": "職業技能",
        "skill/mage.html": "職業技能",
        "skill/smith.html": "職業技能",
        "skill/bard.html": "職業技能",
        "skill/doctor.html": "職業技能",
        "skill/thief.html": "職業技能",
        "skill/step.html": "其他技能",
        "skill/skill.html": "其他技能",
        "skill/learnlv.html": "其他技能",
    }
    return mapping[path]


def normalize_leaf(group: str, leaf: str, legacy_catalog: dict | None) -> str:
    if group == "法術技能" and leaf == "雷電系":
        return "雷系"
    if group == "其他技能" and (legacy_catalog or {}).get("display_name") == "技能的熟練度共分十二個等級":
        return "技能熟練度"
    return leaf


def parse_parenthetical_names(text: str | None) -> list[str]:
    if not text or text == "從缺":
        return []
    return re.findall(r"\(([^()]+)\)", text)


def category_group_for_entry(legacy_catalog: dict | None, page_group: str | None, custom_name: str) -> str:
    if custom_name in NPC_RUNTIME_SKILLS:
        return "current-runtime"
    if legacy_catalog and legacy_catalog.get("display_name"):
        return legacy_catalog.get("category") or "其他技能"
    if legacy_catalog and legacy_catalog.get("category"):
        return legacy_catalog["category"]
    return page_group or "current-runtime"


def infer_family(path: str, english_name: str, leaf: str) -> str:
    stem = Path(path).stem
    if path == "skill/step.html":
        if english_name in {"cloud steps", "gdragon steps", "mirage steps"}:
            return "legacy-step-cloud"
        if english_name in {"sleev steps", "sky steps"}:
            return "legacy-step-sleev"
        if english_name in {"nine steps", "color steps"}:
            return "legacy-step-nine"
        if english_name in {"cloud ghost", "wind color steps"}:
            return "legacy-step-cloud-ghost"
        if english_name in {"shade steps", "wind steps"}:
            return "legacy-step-shade"
        return "legacy-step-standalone"
    return f"legacy-page:{stem}"


def build_status(existing: dict[str, dict], name: str, player_facing: bool, npc_only: bool) -> dict:
    status = dict(existing.get(name, {}).get("status", {}))
    status["player_facing"] = player_facing
    status["npc_only"] = npc_only
    status.setdefault("audit_state", "runtime_active" if npc_only else "legacy_catalog_seeded")
    return status


def dedupe_notes(notes: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for note in notes:
        if not note or note in seen:
            continue
        seen.add(note)
        out.append(note)
    return out


def build_registry() -> dict:
    existing = load_existing_registry()
    legacy_rows = read_json(LEGACY_SKILLS_JSON)
    legacy_by_name = {row.get("英文名稱") or row.get("display_name"): row for row in legacy_rows}
    skill_lst = load_skill_lst()
    runtime_by_name = parse_runtime_skills(skill_lst)

    html_entries = {}
    leaf_map: dict[str, tuple[str, str]] = {}
    for page in sorted(LEGACY_SKILL_DIR.glob("*.html")):
        if page.name == "index.html":
            continue
        entries = parse_html_page(page)
        for entry in entries:
            name = entry["english_name"]
            html_entries[name] = entry
            group = navigation_group_for_page(entry["legacy_catalog"]["path"])
            leaf = normalize_leaf(group, entry["leaf"], entry["legacy_catalog"])
            leaf_map[name] = (group, leaf)

    legacy_site_navigation = {
        "source": "docs/3yWebsite/skill/index.html and per-page category layout",
        "groups": {
            "武器技能": ["劍", "刀", "弓", "槍", "棍", "斧", "鞭", "筆扇", "短兵", "拳法", "氣功"],
            "法術技能": ["火系", "風系", "光系", "聖系", "雷系", "水系", "土系", "暗系", "邪系", "毒系"],
            "職業技能": ["格鬥系", "暗殺系", "法師系", "鑄造系", "吟唱系", "醫療系", "盜賊系"],
            "其他技能": ["步法", "技能", "技能熟練度"],
        },
        "normalization_notes": [
            "Old-site docs/data/skills.json may flatten page-level navigation into broad category values only.",
            "雷電系 is normalized into 雷系 for navigation parity with the old-site category menu.",
            "技能熟練度 is kept as a navigation leaf even though it is informational rather than a runtime skill.",
        ],
    }

    all_names = set(legacy_by_name) | set(html_entries) | set(NPC_RUNTIME_SKILLS) | set(runtime_by_name)
    skills = []
    for name in sorted(all_names):
        if name is None:
            continue
        legacy_row = legacy_by_name.get(name)
        html_entry = html_entries.get(name)
        runtime = runtime_by_name.get(name, {"exists": False})
        custom = NPC_RUNTIME_SKILLS.get(name)

        legacy_catalog = None
        if legacy_row:
            legacy_catalog = dict(legacy_row)
        elif html_entry:
            legacy_catalog = dict(html_entry["legacy_catalog"])

        if html_entry:
            page_path = html_entry["legacy_catalog"]["path"]
            page_group, leaf = leaf_map[name]
            legacy_requirements = html_entry["legacy_requirements"]
        elif legacy_catalog:
            page_path = legacy_catalog.get("path")
            page_group = navigation_group_for_page(page_path)
            leaf = normalize_leaf(page_group, legacy_catalog.get("技能分類") or legacy_catalog.get("display_name") or page_group, legacy_catalog)
            legacy_requirements = {
                "class_limits": [],
                "restrictions": {
                    "attribute_limits": [],
                    "skill_prerequisites": [],
                    "class_requirements": [],
                    "raw_lines": [],
                },
                "teaching_sources": [],
            }
        else:
            page_path = None
            page_group = None
            leaf = None
            legacy_requirements = {
                "class_limits": [],
                "restrictions": {
                    "attribute_limits": [],
                    "skill_prerequisites": [],
                    "class_requirements": [],
                    "raw_lines": [],
                },
                "teaching_sources": [],
            }

        prereq = (legacy_catalog or {}).get("預備功夫")
        upgrade = (legacy_catalog or {}).get("領悟技能")
        legacy_reference = {
            "page": f"docs/3yWebsite/{page_path}" if page_path else None,
            "data_path": "docs/3yWebsite/docs/data/skills.json" if legacy_row else (f"docs/3yWebsite/{page_path}" if page_path else None),
            "chain_root": prereq in (None, "", "從缺"),
            "previous": parse_parenthetical_names(prereq),
            "next": parse_parenthetical_names(upgrade),
            "prerequisite": prereq,
            "upgrade_target": upgrade,
            "upgrade_chance": (legacy_catalog or {}).get("領悟機率"),
        }

        if not legacy_catalog and name == "技能的熟練度共分十二個等級":
            legacy_reference["chain_root"] = True

        family = custom["family"] if custom else infer_family(page_path or f"custom/{name}", name, leaf or "")
        category_group = category_group_for_entry(legacy_catalog, page_group, name)
        chinese_name = (legacy_catalog or {}).get("中文名稱") or custom and custom["chinese_name"] or name
        player_facing = name not in NPC_RUNTIME_SKILLS and name != "技能的熟練度共分十二個等級"
        npc_only = name in NPC_RUNTIME_SKILLS
        existing_combat = dict(existing.get(name, {}).get("combat_dimensions", {}))
        combat = dict(existing_combat)
        combat.update(runtime.get("combat_dimensions", {
            "damage_values": [],
            "chance_values": [],
            "parry_values": [],
            "innate_values": [],
            "wait": runtime.get("wait"),
            "cost": runtime.get("cost"),
            "cost_type": runtime.get("cost_type"),
            "weapon": runtime.get("weapon"),
            "check": runtime.get("check"),
            "prepared_for_adjustment": bool(runtime.get("exists")),
            "notes": [],
        }))
        if existing_combat.get("notes"):
            combat["notes"] = dedupe_notes(list(existing_combat["notes"]))
        if not runtime.get("exists"):
            combat.setdefault("prepared_for_adjustment", False)
        if legacy_requirements["restrictions"]["raw_lines"] and not combat.get("notes"):
            combat["notes"] = []
        if not runtime.get("exists"):
            combat["notes"] = dedupe_notes(
                combat.get("notes", [])
                + ["No runtime skill file matched yet; legacy requirements still preserved from old-site HTML."]
            )

        item = {
            "english_name": name,
            "chinese_name": chinese_name,
            "category_group": category_group,
            "legacy_navigation": {"group": page_group, "leaf": leaf, "page_path": page_path} if page_group and leaf and page_path else None,
            "legacy_catalog": legacy_catalog,
            "legacy_reference": legacy_reference,
            "legacy_requirements": legacy_requirements,
            "family": family,
            "runtime": runtime,
            "combat_dimensions": combat,
            "status": build_status(existing, name, player_facing, npc_only),
        }
        if custom:
            item["intended_roles"] = custom["intended_roles"]
        skills.append(item)

    return {
        "registry_version": 4,
        "scope": "Integrated current-game skill registry for merc-fju-3.0. It combines old-site catalog data, full old-site skill HTML extraction, runtime presence, and skill-combat audit fields without replacing runtime source files.",
        "coverage": {
            "seeded_families": [
                "all entries from docs/3yWebsite/docs/data/skills.json",
                "all entries extracted from docs/3yWebsite/skill/*.html",
                "2026-03 npc-only runtime additions",
            ],
            "planned_expansion": [
                "per-skill mob usage cross-links",
                "post-adjustment before/after combat audit snapshots",
                "generated readable pages for more skill leaves",
            ],
        },
        "source_layers": {
            "legacy_html": ["docs/3yWebsite/skill/*.html"],
            "legacy_json": ["docs/3yWebsite/docs/data/skills.json", "docs/3yWebsite/docs/data/players.json"],
            "legacy_guides": ["docs/3yWebsite/newhand/newbies/index.html"],
            "runtime": ["skill/*.ski", "skill/skill.lst", "src/merc.h", "data/symbol.def"],
        },
        "legacy_site_navigation": legacy_site_navigation,
        "combat_dimension_schema": {
            "purpose": "Keep one audit-ready place for current skill templates, legacy requirements, and future tuning deltas.",
            "fields": ["damage_values", "chance_values", "parry_values", "innate_values", "wait", "cost", "cost_type", "weapon", "check"],
            "usage_notes": [
                "Do not tune by damage_values alone; read chance/parry/innate/wait/cost/weapon/check together.",
                "Use legacy_requirements to preserve old-site class, attribute, and prerequisite constraints even before runtime reconciliation is complete.",
                "When a batch changes a skill, append batch-specific notes rather than overwriting historical context.",
            ],
        },
        "notes": [
            "This file is an integrated working registry, not the runtime source of truth.",
            "Old-site HTML is the preferred source for descendant skills and requirement details when docs/3yWebsite/docs/data/skills.json flattens a page into one root row.",
            "docs/3yWebsite/newhand/newbies/index.html is used as a starter-play reference for early learnable skills, beginner enable expectations, and class progression context.",
            "combat_dimensions is intended to hold both current runtime values and future tuning metadata.",
        ],
        "skills": skills,
    }


def main() -> None:
    registry = build_registry()
    CURRENT_SKILLS_JSON.write_text(json.dumps(registry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {CURRENT_SKILLS_JSON}")
    print(f"skills {len(registry['skills'])}")


if __name__ == "__main__":
    main()
