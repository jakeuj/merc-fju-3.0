from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_JSON = ROOT / "docs/current-game/skills.json"
INDEX_MD = ROOT / "docs/current-game/skills-index.md"
STEP_MD = ROOT / "docs/current-game/skills/step.md"


def load_skills() -> dict:
    return json.loads(SKILLS_JSON.read_text(encoding="utf-8"))


def ensure_dirs() -> None:
    STEP_MD.parent.mkdir(parents=True, exist_ok=True)


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


def write_index(data: dict) -> None:
    skills = data["skills"]
    by_leaf: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for skill in skills:
        nav = nav_of(skill)
        if nav.get("group") and nav.get("leaf"):
            by_leaf[(nav["group"], nav["leaf"])].append(skill)

    page_map = {
        ("其他技能", "步法"): "./skills/step.html",
    }

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
        "目前先提供分類總覽與 `步法` 子頁；其他葉節點可依同一份 JSON 再擴充生成。",
        "",
    ]

    for group, leaves in data["legacy_site_navigation"]["groups"].items():
        rows = []
        for leaf in leaves:
            leaf_skills = sorted(
                by_leaf.get((group, leaf), []),
                key=lambda item: item["english_name"],
            )
            examples = ", ".join(item["english_name"] for item in leaf_skills[:3]) or "-"
            page = page_map.get((group, leaf))
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
        f"- Damage values: `{combat.get('damage_values') or []}`",
        f"- Chance values: `{combat.get('chance_values') or []}`",
        f"- Parry values: `{combat.get('parry_values') or []}`",
        f"- Innate values: `{combat.get('innate_values') or []}`",
    ]
    if legacy_catalog:
        lines.append(f"- Legacy page source: `{legacy_catalog.get('path') or '-'}`")
    notes = combat.get("notes") or []
    if notes:
        lines.append(f"- Notes: {'; '.join(notes)}")
    lines.append("")
    return "\n".join(lines)


def write_step_page(data: dict) -> None:
    step_skills = [
        skill for skill in data["skills"] if (nav_of(skill).get("leaf") == "步法")
    ]
    step_skills.sort(key=lambda item: (item.get("family") or "", item["english_name"]))
    by_family: dict[str, list[dict]] = defaultdict(list)
    for skill in step_skills:
        by_family[skill.get("family") or "unknown"].append(skill)

    family_rows = []
    for family, items in sorted(by_family.items()):
        family_rows.append(
            [
                family,
                family_chain(items),
                str(len(items)),
                ", ".join(
                    sorted(
                        {
                            (item.get("status") or {}).get("audit_state", "-")
                            for item in items
                        }
                    )
                ),
            ]
        )

    lines = [
        "---",
        "layout: default",
        "title: Current Game Step Skills",
        "---",
        "",
        "# Current Game Step Skills",
        "",
        "這頁是 `docs/current-game/skills.json` 的 `步法` 可讀版，優先把舊站步法鏈與目前 runtime 狀態放在同一頁。",
        "",
        f"- Skills in this page: `{len(step_skills)}`",
        f"- Source JSON: [`skills.json`](../skills.json)",
        f"- Registry note: [`skills.md`](../skills.html)",
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

    STEP_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ensure_dirs()
    data = load_skills()
    write_index(data)
    write_step_page(data)


if __name__ == "__main__":
    main()
