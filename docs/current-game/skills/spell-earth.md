---
layout: default
title: Current Game 土系 Skills
---

# Current Game 法術技能 / 土系

這頁是 `docs/current-game/skills.json` 的 `法術技能 / 土系` 可讀版，將舊站鏈路、現行 runtime 與調整維度放在同一頁。

- Skills in this page: `6`
- Source JSON: [`skills.json`](../skills.json)
- Registry note: [`skills.md`](../skills.html)
- Index: [`skills-index.md`](../skills-index.html)

## Family Overview

| Family | Legacy Chain | Skills | Audit States |
| --- | --- | --- | --- |
| legacy-page:earth | create food -> detect hidden -> pass door -> fixity<br>flying stone -> earthquake | 6 | legacy_catalog_seeded |

## Skill Cards

## legacy-page:earth

Legacy chain: `create food -> detect hidden -> pass door -> fixity / flying stone -> earthquake`

### 製造食物 / `create food`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:earth`
- Legacy prerequisite: `從缺`
- Legacy next: `detect hidden`
- Runtime file: `skill/c/create_food.ski`
- Runtime slot: `SLOT_CREATE_FOOD`
- Runtime key: `create_food`
- Type: `TAR_IGNORE`
- Cost / Wait: `5 / 12`
- CostType / Weapon / Check: `COST_MANA / - / -`
- CanAsk / Teach / Valid / Enable: `No / No / Yes / No`
- Class limits: `伶 人 >= 一級, max 登峰造極﹗; 郎 中 >= 一級, max 登峰造極﹗; 文 官 >= 一級, max 心神領會﹗`
- Restrictions: `-`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/earth.html`

### 偵測藏匿 / `detect hidden`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:earth`
- Legacy prerequisite: `製造食物(create food)`
- Legacy next: `pass door`
- Runtime file: `skill/d/detect_hidden.ski`
- Runtime slot: `SLOT_DETECT_HIDDEN`
- Runtime key: `detect_hidden`
- Type: `SLOT_DETECT_HIDDEN`
- Cost / Wait: `8 / 20`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `No / No / Yes / No`
- Class limits: `伶 人 >= 一級, max 登峰造極﹗; 郎 中 >= 一級, max 登峰造極﹗; 文 官 >= 一級, max 心神領會﹗`
- Restrictions: `skills: 製造食物 >= 心神領會`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/earth.html`

### 地震術 / `earthquake`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:earth`
- Legacy prerequisite: `飛砂走石術(flying stone)`
- Legacy next: `-`
- Runtime file: `skill/e/earthquake.ski`
- Runtime slot: `SLOT_EARTHQUAKE`
- Runtime key: `earthquake`
- Type: `TAR_IGNORE`
- Cost / Wait: `20 / 15`
- CostType / Weapon / Check: `COST_MANA / - / -`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `伶 人 >= 五十級, max 出類拔萃﹗; 刺 客 >= 五十級, max 出類拔萃﹗; 郎 中 >= 五十級, max 出類拔萃﹗; 武 官 >= 十級, max 馬馬虎虎﹗; 將 軍 >= 五十級, max 出類拔萃﹗; 天 師 >= 五十級, max 一代宗師﹗; 文 官 >= 十級, max 心神領會﹗; 道 士 >= 十級, max 出類拔萃﹗; 鑄劍師 >= 五十級, max 登峰造極﹗; 盜 賊 >= 十級, max 馬馬虎虎﹗`
- Restrictions: `-`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/earth.html`

### 定身術 / `fixity`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:earth`
- Legacy prerequisite: `穿透術(pass door)`
- Legacy next: `-`
- Runtime file: `skill/f/fixity.ski`
- Runtime slot: `SLOT_FIXITY`
- Runtime key: `fixity`
- Type: `TAR_CHAR_SELF`
- Cost / Wait: `12 / 10`
- CostType / Weapon / Check: `COST_MANA / - / -`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `伶 人 >= 一級, max 登峰造極﹗; 郎 中 >= 一級, max 登峰造極﹗`
- Restrictions: `skills: 穿透術 >= 神乎其技`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/earth.html`

### 飛砂走石術 / `flying stone`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:earth`
- Legacy prerequisite: `從缺`
- Legacy next: `earthquake`
- Runtime file: `skill/f/flying_stone.ski`
- Runtime slot: `SLOT_FLYING_STONE`
- Runtime key: `flying_stone`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `15 / 12`
- CostType / Weapon / Check: `COST_MANA / - / -`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `伶 人 >= 五十級, max 出類拔萃﹗; 刺 客 >= 五十級, max 出類拔萃﹗; 郎 中 >= 五十級, max 出類拔萃﹗; 武 官 >= 十級, max 馬馬虎虎﹗; 將 軍 >= 五十級, max 出類拔萃﹗; 天 師 >= 五十級, max 一代宗師﹗; 文 官 >= 十級, max 心神領會﹗; 道 士 >= 十級, max 出類拔萃﹗; 鑄劍師 >= 五十級, max 登峰造極﹗; 盜 賊 >= 十級, max 馬馬虎虎﹗`
- Restrictions: `-`
- Damage model: `code-driven`
- Code path: `src/spell.c:5115`
- Code damage summary: `formula: spell_damage(ch, level, TYPE_INT, SPELL_CLASS_ONE); attack mode: ATTACK_RANDOM`
- Damage values: `(not stored in .ski #Damage)`
- Chance / Parry / Innate: `(resolved in code path, not .ski arrays)`
- Legacy page source: `skill/earth.html`
- Notes: Code-driven offensive exception: damage logic currently lives in src/spell.c:5115.

### 穿透術 / `pass door`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:earth`
- Legacy prerequisite: `偵測藏匿(detect hidden)`
- Legacy next: `fixity`
- Runtime file: `skill/p/pass_door.ski`
- Runtime slot: `SLOT_PASS_DOOR`
- Runtime key: `pass_door`
- Type: `SLOT_PASS_DOOR`
- Cost / Wait: `12 / 22`
- CostType / Weapon / Check: `COST_MANA / - / -`
- CanAsk / Teach / Valid / Enable: `No / No / Yes / No`
- Class limits: `伶 人 >= 一級, max 登峰造極﹗; 郎 中 >= 一級, max 登峰造極﹗; 文 官 >= 一級, max 心神領會﹗`
- Restrictions: `skills: 偵測藏匿 >= 心神領會`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/earth.html`

