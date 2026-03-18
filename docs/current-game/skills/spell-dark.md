---
layout: default
title: Current Game 暗系 Skills
---

# Current Game 法術技能 / 暗系

這頁是 `docs/current-game/skills.json` 的 `法術技能 / 暗系` 可讀版，將舊站鏈路、現行 runtime 與調整維度放在同一頁。

- Skills in this page: `7`
- Source JSON: [`skills.json`](../skills.json)
- Registry note: [`skills.md`](../skills.html)
- Index: [`skills-index.md`](../skills-index.html)

## Family Overview

| Family | Legacy Chain | Skills | Audit States |
| --- | --- | --- | --- |
| legacy-page:dark | cause light -> cause serious -> slow -> cause critical<br>ventriloquate -> invis -> mass invis | 7 | legacy_catalog_seeded |

## Skill Cards

## legacy-page:dark

Legacy chain: `cause light -> cause serious -> slow -> cause critical / ventriloquate -> invis -> mass invis`

### 極度傷害 / `cause critical`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:dark`
- Legacy prerequisite: `遲滯術(slow)`
- Legacy next: `-`
- Runtime file: `skill/c/cause_critical.ski`
- Runtime slot: `SLOT_CAUSE_CRITICAL`
- Runtime key: `cause_critical`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `25 / 20`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `天 師 >= 五十級, max 一代宗師﹗; 鑄劍師 >= 五十級, max 登峰造極﹗`
- Restrictions: `skills: 遲滯術 >= 出類拔萃`
- Damage model: `code-driven`
- Code path: `src/spell.c:1194`
- Code damage summary: `formula: spell_damage(ch, level, TYPE_INT, SPELL_CLASS_FOU); attack mode: ATTACK_RANDOM`
- Damage values: `(not stored in .ski #Damage)`
- Chance / Parry / Innate: `(resolved in code path, not .ski arrays)`
- Legacy page source: `skill/dark.html`
- Notes: Code-driven offensive exception: damage logic currently lives in src/spell.c:1194.

### 輕度傷害 / `cause light`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:dark`
- Legacy prerequisite: `從缺`
- Legacy next: `cause serious`
- Runtime file: `skill/c/cause_light.ski`
- Runtime slot: `SLOT_CAUSE_LIGHT`
- Runtime key: `cause_light`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `15 / 12`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `伶 人 >= 五十級, max 出類拔萃﹗; 郎 中 >= 五十級, max 出類拔萃﹗; 天 師 >= 五十級, max 一代宗師﹗; 文 官 >= 十級, max 心神領會﹗; 道 士 >= 十級, max 神乎其技﹗; 鑄劍師 >= 五十級, max 登峰造極﹗`
- Restrictions: `-`
- Damage model: `code-driven`
- Code path: `src/spell.c:1167`
- Code damage summary: `formula: spell_damage(ch, level, TYPE_INT, SPELL_CLASS_ONE); attack mode: ATTACK_RANDOM`
- Damage values: `(not stored in .ski #Damage)`
- Chance / Parry / Innate: `(resolved in code path, not .ski arrays)`
- Legacy page source: `skill/dark.html`
- Notes: Code-driven offensive exception: damage logic currently lives in src/spell.c:1167.

### 中度傷害 / `cause serious`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:dark`
- Legacy prerequisite: `輕度傷害(cause light)`
- Legacy next: `slow`
- Runtime file: `skill/c/cause_serious.ski`
- Runtime slot: `SLOT_CAUSE_SERIOUS`
- Runtime key: `cause_serious`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `20 / 15`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `伶 人 >= 五十級, max 出類拔萃﹗; 郎 中 >= 五十級, max 出類拔萃﹗; 天 師 >= 五十級, max 一代宗師﹗; 文 官 >= 十級, max 心神領會﹗; 道 士 >= 十級, max 神乎其技﹗; 鑄劍師 >= 五十級, max 登峰造極﹗`
- Restrictions: `skills: 輕度傷害 >= 心神領會`
- Damage model: `code-driven`
- Code path: `src/spell.c:1222`
- Code damage summary: `formula: spell_damage(ch, level, TYPE_INT, SPELL_CLASS_TWO); attack mode: ATTACK_RANDOM`
- Damage values: `(not stored in .ski #Damage)`
- Chance / Parry / Innate: `(resolved in code path, not .ski arrays)`
- Legacy page source: `skill/dark.html`
- Notes: Code-driven offensive exception: damage logic currently lives in src/spell.c:1222.

### 隱形術 / `invis`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:dark`
- Legacy prerequisite: `腹語術(ventriloquate)`
- Legacy next: `mass invis`
- Runtime file: `skill/i/invis.ski`
- Runtime slot: `SLOT_INVIS`
- Runtime key: `invis`
- Type: `TAR_CHAR_DEFENSIVE`
- Cost / Wait: `15 / 18`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `伶 人 >= 五十級, max 一代宗師﹗; 郎 中 >= 五十級, max 出神入化﹗; 文 官 >= 十五級, max 心神領會﹗`
- Restrictions: `attrs: 智力 >= 十; skills: 腹語術 >= 心神領會`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/dark.html`

### 全體隱形 / `mass invis`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:dark`
- Legacy prerequisite: `隱形術(invis)`
- Legacy next: `-`
- Runtime file: `skill/m/mass_invis.ski`
- Runtime slot: `SLOT_MASS_INVIS`
- Runtime key: `mass_invis`
- Type: `TAR_IGNORE`
- Cost / Wait: `20 / 24`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `伶 人 >= 五十級, max 一代宗師﹗; 郎 中 >= 五十級, max 出神入化﹗`
- Restrictions: `attrs: 智力 >= 十五; skills: 隱形術 >= 出類拔萃`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/dark.html`

### 遲滯術 / `slow`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:dark`
- Legacy prerequisite: `中度傷害(cause serious)`
- Legacy next: `cause critical`
- Runtime file: `skill/s/slow.ski`
- Runtime slot: `SLOT_SLOW`
- Runtime key: `slow`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `25 / 20`
- CostType / Weapon / Check: `COST_MANA / - / -`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `伶 人 >= 五十級, max 出類拔萃﹗; 郎 中 >= 五十級, max 出類拔萃﹗; 天 師 >= 五十級, max 一代宗師﹗; 文 官 >= 十級, max 心神領會﹗; 道 士 >= 十級, max 神乎其技﹗; 鑄劍師 >= 五十級, max 登峰造極﹗`
- Restrictions: `skills: 中度傷害 >= 心神領會`
- Damage model: `unresolved`
- Damage audit classification: `needs review`
- Code path: `src/spell.c:5140`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/dark.html`
- Notes: Needs review: damage logic currently lives in src/spell.c:5140.

### 腹語術 / `ventriloquate`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:dark`
- Legacy prerequisite: `從缺`
- Legacy next: `invis`
- Runtime file: `skill/v/ventriloquate.ski`
- Runtime slot: `SLOT_VENTRILOQUATE`
- Runtime key: `ventriloquate`
- Type: `TAR_STRING`
- Cost / Wait: `5 / 12`
- CostType / Weapon / Check: `COST_MANA / - / -`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `伶 人 >= 五十級, max 一代宗師﹗; 郎 中 >= 五十級, max 出神入化﹗; 將 軍 >= 五十級, max 心神領會﹗; 天 師 >= 五十級, max 心神領會﹗; 文 官 >= 十五級, max 出類拔萃﹗; 道 士 >= 十五級, max 心神領會﹗; 鑄劍師 >= 五十級, max 心神領會﹗`
- Restrictions: `-`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/dark.html`

