from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_JSON = ROOT / "docs/current-game/skills.json"
INDEX_MD = ROOT / "docs/current-game/skills-index.md"
SKILLS_DIR = ROOT / "docs/current-game/skills"

LEAF_PAGE_MAP = {
    ("武器技能", "劍"): "sword.md",
    ("武器技能", "刀"): "blade.md",
    ("武器技能", "弓"): "bow.md",
    ("武器技能", "槍"): "lance.md",
    ("武器技能", "棍"): "staff.md",
    ("武器技能", "斧"): "axe.md",
    ("武器技能", "鞭"): "whip.md",
    ("武器技能", "筆扇"): "fan.md",
    ("武器技能", "短兵"): "short.md",
    ("武器技能", "拳法"): "fist.md",
    ("武器技能", "氣功"): "force.md",
    ("法術技能", "火系"): "spell-fire.md",
    ("法術技能", "風系"): "spell-wind.md",
    ("法術技能", "光系"): "spell-light.md",
    ("法術技能", "聖系"): "spell-holy.md",
    ("法術技能", "雷系"): "spell-thunder.md",
    ("法術技能", "水系"): "spell-water.md",
    ("法術技能", "土系"): "spell-earth.md",
    ("法術技能", "暗系"): "spell-dark.md",
    ("法術技能", "邪系"): "spell-evil.md",
    ("法術技能", "毒系"): "spell-poison.md",
    ("職業技能", "格鬥系"): "job-fighter.md",
    ("職業技能", "暗殺系"): "job-assassin.md",
    ("職業技能", "法師系"): "job-mage.md",
    ("職業技能", "鑄造系"): "job-smith.md",
    ("職業技能", "吟唱系"): "job-bard.md",
    ("職業技能", "醫療系"): "job-healer.md",
    ("職業技能", "盜賊系"): "job-thief.md",
    ("其他技能", "步法"): "step.md",
    ("其他技能", "技能"): "misc.md",
    ("其他技能", "技能熟練度"): "proficiency.md",
}


def load_skills() -> dict:
    return json.loads(SKILLS_JSON.read_text(encoding="utf-8"))


def ensure_dirs() -> None:
    SKILLS_DIR.mkdir(parents=True, exist_ok=True)


def nav_of(skill: dict) -> dict:
    return skill.get("legacy_navigation") or {}


def bool_text(value: object) -> str:
    if value is True:
        return "Yes"
    if value is False:
        return "No"
    return "-"


def md_table(headers: list[str], rows: list[list[str]]) -> str:
    out = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    out.extend("| " + " | ".join(row) + " |" for row in rows)
    return "\n".join(out)


def family_chain(skills: list[dict]) -> str:
    roots = [s for s in skills if (s.get("legacy_reference") or {}).get("chain_root")]
    if not roots:
        roots = sorted(skills, key=lambda s: s["english_name"])
    chains = []
    for root in sorted(roots, key=lambda s: s["english_name"]):
        chain = [root["english_name"]]
        seen = {root["english_name"]}
        current = root
        while True:
            next_names = (current.get("legacy_reference") or {}).get("next") or []
            next_name = next((name for name in next_names if name not in seen), None)
            if not next_name:
                break
            chain.append(next_name)
            seen.add(next_name)
            current = next((item for item in skills if item["english_name"] == next_name), None)
            if current is None:
                break
        chains.append(" -> ".join(chain))
    return "<br>".join(chains)


def page_path_for(group: str, leaf: str) -> str | None:
    filename = LEAF_PAGE_MAP.get((group, leaf))
    if not filename:
        return None
    return f"./skills/{filename[:-3]}.html"


def page_file_for(group: str, leaf: str) -> Path | None:
    filename = LEAF_PAGE_MAP.get((group, leaf))
    if not filename:
        return None
    return SKILLS_DIR / filename


def class_limit_summary(class_limits: list[dict]) -> str:
    if not class_limits:
        return "-"
    parts = []
    for item in class_limits:
        job = item.get("job") or "-"
        level = item.get("min_level") or "-"
        prof = item.get("max_proficiency") or "-"
        parts.append(f"{job} >= {level}, max {prof}")
    return "; ".join(parts)


def restriction_summary(restrictions: dict) -> str:
    if not restrictions:
        return "-"
    parts = []
    attrs = restrictions.get("attribute_limits") or []
    prereqs = restrictions.get("skill_prerequisites") or []
    class_reqs = restrictions.get("class_requirements") or []
    if attrs:
        parts.append(
            "attrs: " + ", ".join(f"{item.get('attribute')} >= {item.get('minimum')}" for item in attrs)
        )
    if prereqs:
        parts.append(
            "skills: " + ", ".join(f"{item.get('skill')} >= {item.get('minimum')}" for item in prereqs)
        )
    if class_reqs:
        parts.append(
            "classes: " + ", ".join("/".join(item.get("allowed_classes") or []) for item in class_reqs)
        )
    return "; ".join(parts) if parts else "-"


def write_index(data: dict) -> None:
    skills = data["skills"]
    by_leaf: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for skill in skills:
        nav = nav_of(skill)
        if nav.get("group") and nav.get("leaf"):
            by_leaf[(nav["group"], nav["leaf"])].append(skill)

    lines = [
        "---",
        "layout: default",
        "title: Current Game Skills Index",
        "---",
        "",
        "# Current Game Skills Index",
        "",
        "這頁提供 GitHub Pages 可直接瀏覽的技能總覽，資料源來自 `docs/current-game/skills.json`。",
        "",
        "這些子頁由 `scripts/generate_current_game_skills_pages.py` 從同一份 registry 靜態生成。",
        "",
    ]

    for group, leaves in data["legacy_site_navigation"]["groups"].items():
        rows = []
        for leaf in leaves:
            leaf_skills = sorted(by_leaf.get((group, leaf), []), key=lambda item: item["english_name"])
            examples = ", ".join(item["english_name"] for item in leaf_skills[:3]) or "-"
            page = page_path_for(group, leaf)
            page_text = f"[Open]({page})" if page else "Not generated yet"
            rows.append([leaf, str(len(leaf_skills)), examples, page_text])
        lines.extend(
            [
                f"## {group}",
                "",
                md_table(["Leaf", "Skills", "Examples", "Readable Page"], rows),
                "",
            ]
        )

    INDEX_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def skill_section(skill: dict) -> str:
    runtime = skill.get("runtime") or {}
    combat = skill.get("combat_dimensions") or {}
    legacy_ref = skill.get("legacy_reference") or {}
    legacy_catalog = skill.get("legacy_catalog") or {}
    legacy_requirements = skill.get("legacy_requirements") or {}
    restrictions = legacy_requirements.get("restrictions") or {}
    lines = [
        f"### {skill['chinese_name']} / `{skill['english_name']}`",
        "",
        f"- Audit: `{(skill.get('status') or {}).get('audit_state', '-')}`",
        f"- Family: `{skill.get('family', '-')}`",
        f"- Legacy prerequisite: `{legacy_ref.get('prerequisite') or '-'}`",
        f"- Legacy next: `{', '.join(legacy_ref.get('next') or []) or '-'}`",
        f"- Runtime file: `{runtime.get('skill_file') or '-'}`",
        f"- Runtime slot: `{runtime.get('slot_symbol') or '-'}`",
        f"- Runtime key: `{runtime.get('skill_lst_key') or '-'}`",
        f"- Type: `{runtime.get('type') or '-'}`",
        f"- Cost / Wait: `{runtime.get('cost') if runtime.get('cost') is not None else '-'} / {runtime.get('wait') if runtime.get('wait') is not None else '-'}`",
        f"- CostType / Weapon / Check: `{runtime.get('cost_type') or '-'} / {runtime.get('weapon') or '-'} / {runtime.get('check') or '-'}`",
        f"- CanAsk / Teach / Valid / Enable: `{bool_text(runtime.get('canask'))} / {bool_text(runtime.get('teach'))} / {bool_text(runtime.get('valid'))} / {bool_text(runtime.get('enable'))}`",
        f"- Class limits: `{class_limit_summary(legacy_requirements.get('class_limits') or [])}`",
        f"- Restrictions: `{restriction_summary(restrictions)}`",
    ]
    damage_source = combat.get("damage_source")
    if damage_source == "code-driven":
        lines.extend(
            [
                "- Damage model: `code-driven`",
                f"- Code path: `{combat.get('code_path') or '-'}`",
                f"- Code damage summary: `{combat.get('code_damage_summary') or '-'}`",
                "- Damage values: `(not stored in .ski #Damage)`",
                "- Chance / Parry / Innate: `(resolved in code path, not .ski arrays)`",
            ]
        )
    elif damage_source == "unresolved" and not combat.get("damage_values"):
        lines.extend(
            [
                "- Damage model: `unresolved`",
                f"- Damage audit classification: `{combat.get('damage_gap_classification') or 'needs review'}`",
                f"- Code path: `{combat.get('code_path') or '-'}`",
                f"- Damage values: `{combat.get('damage_values') or []}`",
                f"- Chance values: `{combat.get('chance_values') or []}`",
                f"- Parry values: `{combat.get('parry_values') or []}`",
                f"- Innate values: `{combat.get('innate_values') or []}`",
            ]
        )
    elif combat.get("damage_values"):
        lines.extend(
            [
                "- Damage model: `data-driven`",
                f"- Damage values: `{combat.get('damage_values') or []}`",
                f"- Chance values: `{combat.get('chance_values') or []}`",
                f"- Parry values: `{combat.get('parry_values') or []}`",
                f"- Innate values: `{combat.get('innate_values') or []}`",
            ]
        )
    else:
        lines.extend(
            [
                f"- Damage values: `{combat.get('damage_values') or []}`",
                f"- Chance values: `{combat.get('chance_values') or []}`",
                f"- Parry values: `{combat.get('parry_values') or []}`",
                f"- Innate values: `{combat.get('innate_values') or []}`",
            ]
        )
    if legacy_catalog:
        lines.append(f"- Legacy page source: `{legacy_catalog.get('path') or '-'}`")
    notes = combat.get("notes") or []
    if notes:
        lines.append(f"- Notes: {'; '.join(notes)}")
    lines.append("")
    return "\n".join(lines)


def write_leaf_page(data: dict, group: str, leaf: str) -> None:
    target = page_file_for(group, leaf)
    if target is None:
        return

    leaf_skills = [
        skill
        for skill in data["skills"]
        if nav_of(skill).get("group") == group and nav_of(skill).get("leaf") == leaf
    ]
    leaf_skills.sort(key=lambda item: (item.get("family") or "", item["english_name"]))
    by_family: dict[str, list[dict]] = defaultdict(list)
    for skill in leaf_skills:
        by_family[skill.get("family") or "unknown"].append(skill)

    family_rows = []
    for family, items in sorted(by_family.items()):
        family_rows.append(
            [
                family,
                family_chain(items),
                str(len(items)),
                ", ".join(sorted({(item.get("status") or {}).get("audit_state", "-") for item in items})),
            ]
        )

    lines = [
        "---",
        "layout: default",
        f"title: Current Game {leaf} Skills",
        "---",
        "",
        f"# Current Game {group} / {leaf}",
        "",
        f"這頁是 `docs/current-game/skills.json` 的 `{group} / {leaf}` 可讀版，將舊站鏈路、現行 runtime 與調整維度放在同一頁。",
        "",
        f"- Skills in this page: `{len(leaf_skills)}`",
        "- Source JSON: [`skills.json`](../skills.json)",
        "- Registry note: [`skills.md`](../skills.html)",
        "- Index: [`skills-index.md`](../skills-index.html)",
        "",
        "## Family Overview",
        "",
        md_table(["Family", "Legacy Chain", "Skills", "Audit States"], family_rows),
        "",
        "## Skill Cards",
        "",
    ]

    for family, items in sorted(by_family.items()):
        lines.append(f"## {family}")
        lines.append("")
        lines.append(f"Legacy chain: `{family_chain(items).replace('<br>', ' / ')}`")
        lines.append("")
        for skill in sorted(items, key=lambda item: item["english_name"]):
            lines.append(skill_section(skill))

    target.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ensure_dirs()
    data = load_skills()
    write_index(data)
    for group, leaves in data["legacy_site_navigation"]["groups"].items():
        for leaf in leaves:
            write_leaf_page(data, group, leaf)


if __name__ == "__main__":
    main()
