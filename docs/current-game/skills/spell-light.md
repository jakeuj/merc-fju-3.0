---
layout: default
title: Current Game 光系 Skills
---

# Current Game 法術技能 / 光系

這頁是 `docs/current-game/skills.json` 的 `法術技能 / 光系` 可讀版，將舊站鏈路、現行 runtime 與調整維度放在同一頁。

- Skills in this page: `7`
- Source JSON: [`skills.json`](../skills.json)
- Registry note: [`skills.md`](../skills.html)
- Index: [`skills-index.md`](../skills-index.html)

## Family Overview

| Family | Legacy Chain | Skills | Audit States |
| --- | --- | --- | --- |
| legacy-page:light | colour spray<br>detect mask<br>make light -> infravision -> teleport -> detect invis -> summon | 7 | legacy_catalog_seeded |

## Skill Cards

## legacy-page:light

Legacy chain: `colour spray / detect mask / make light -> infravision -> teleport -> detect invis -> summon`

### 七彩霓虹 / `colour spray`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:light`
- Legacy prerequisite: `從缺`
- Legacy next: `-`
- Runtime file: `skill/c/colour_spray.ski`
- Runtime slot: `SLOT_COLOUR_SPRAY`
- Runtime key: `colour_spray`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `15 / 12`
- CostType / Weapon / Check: `COST_MANA / - / -`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `伶 人 >= 五十級, max 出類拔萃﹗; 刺 客 >= 五十級, max 出類拔萃﹗; 郎 中 >= 五十級, max 出類拔萃﹗; 武 官 >= 十級, max 馬馬虎虎﹗; 將 軍 >= 五十級, max 出類拔萃﹗; 天 師 >= 五十級, max 一代宗師﹗; 文 官 >= 十級, max 心神領會﹗; 道 士 >= 十級, max 出類拔萃﹗; 鑄劍師 >= 五十級, max 登峰造極﹗; 盜 賊 >= 十級, max 馬馬虎虎﹗`
- Restrictions: `-`
- Damage model: `code-driven`
- Code path: `src/spell.c:1419`
- Code damage summary: `formula: spell_damage(ch, level, TYPE_INT, SPELL_CLASS_ONE); attack mode: ATTACK_RANDOM`
- Damage values: `(not stored in .ski #Damage)`
- Chance / Parry / Innate: `(resolved in code path, not .ski arrays)`
- Legacy page source: `skill/light.html`
- Notes: Code-driven offensive exception: damage logic currently lives in src/spell.c:1419.

### 偵測隱形 / `detect invis`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:light`
- Legacy prerequisite: `隨機傳送(teleport)`
- Legacy next: `summon`
- Runtime file: `skill/d/detect_invis.ski`
- Runtime slot: `SLOT_DETECT_INVIS`
- Runtime key: `detect_invis`
- Type: `TAR_CHAR_SELF`
- Cost / Wait: `40 / 22`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `No / No / Yes / No`
- Class limits: `伶 人 >= 一級, max 一代宗師﹗; 郎 中 >= 一級, max 神乎其技﹗`
- Restrictions: `attrs: 學識 >= 二十; skills: 隨機傳送 >= 出類拔萃`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/light.html`

### 偵測易容 / `detect mask`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:light`
- Legacy prerequisite: `從缺`
- Legacy next: `-`
- Runtime file: `skill/d/detect_mask.ski`
- Runtime slot: `SLOT_DETECT_MASK`
- Runtime key: `detect_mask`
- Type: `TAR_CHAR_SELF`
- Cost / Wait: `40 / 22`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `No / No / Yes / No`
- Class limits: `伶 人 >= 一級, max 一代宗師﹗; 郎 中 >= 一級, max 神乎其技﹗; 文 官 >= 三十級, max 心神領會﹗`
- Restrictions: `attrs: 學識 >= 十五`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/light.html`

### 夜視術 / `infravision`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:light`
- Legacy prerequisite: `千丈光芒(make light)`
- Legacy next: `teleport`
- Runtime file: `skill/i/infravision.ski`
- Runtime slot: `SLOT_INFRAVISION`
- Runtime key: `infravision`
- Type: `TAR_CHAR_DEFENSIVE`
- Cost / Wait: `20 / 18`
- CostType / Weapon / Check: `COST_MANA / - / -`
- CanAsk / Teach / Valid / Enable: `No / No / Yes / No`
- Class limits: `伶 人 >= 一級, max 一代宗師﹗; 郎 中 >= 一級, max 神乎其技﹗; 文 官 >= 一級, max 心神領會﹗`
- Restrictions: `skills: 千丈光芒 >= 心神領會`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/light.html`

### 千丈光芒 / `make light`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:light`
- Legacy prerequisite: `從缺`
- Legacy next: `infravision`
- Runtime file: `skill/m/make_light.ski`
- Runtime slot: `SLOT_MAKE_LIGHT`
- Runtime key: `make_light`
- Type: `TAR_IGNORE`
- Cost / Wait: `15 / 10`
- CostType / Weapon / Check: `COST_MANA / - / -`
- CanAsk / Teach / Valid / Enable: `No / No / Yes / No`
- Class limits: `伶 人 >= 一級, max 一代宗師﹗; 郎 中 >= 一級, max 神乎其技﹗; 文 官 >= 一級, max 心神領會﹗`
- Restrictions: `-`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/light.html`

### 招喚術 / `summon`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:light`
- Legacy prerequisite: `偵測隱形(detect invis)`
- Legacy next: `-`
- Runtime file: `skill/s/summon.ski`
- Runtime slot: `SLOT_SUMMON`
- Runtime key: `summon`
- Type: `TAR_STRING`
- Cost / Wait: `50 / 30`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `No / No / Yes / No`
- Class limits: `伶 人 >= 一級, max 一代宗師﹗`
- Restrictions: `attrs: 學識 >= 二十五; skills: 偵測隱形 >= 出類拔萃`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/light.html`

### 隨機傳送 / `teleport`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:light`
- Legacy prerequisite: `夜視術(infravision)`
- Legacy next: `detect invis`
- Runtime file: `skill/t/teleport.ski`
- Runtime slot: `SLOT_TELEPORT`
- Runtime key: `teleport`
- Type: `TAR_CHAR_SELF`
- Cost / Wait: `35 / 20`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `No / No / Yes / No`
- Class limits: `伶 人 >= 一級, max 一代宗師﹗; 郎 中 >= 一級, max 神乎其技﹗`
- Restrictions: `attrs: 學識 >= 十五; skills: 夜視術 >= 出類拔萃`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/light.html`

