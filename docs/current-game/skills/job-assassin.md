---
layout: default
title: Current Game 暗殺系 Skills
---

# Current Game 職業技能 / 暗殺系

這頁是 `docs/current-game/skills.json` 的 `職業技能 / 暗殺系` 可讀版，將舊站鏈路、現行 runtime 與調整維度放在同一頁。

- Skills in this page: `3`
- Source JSON: [`skills.json`](../skills.json)
- Registry note: [`skills.md`](../skills.html)
- Index: [`skills-index.md`](../skills-index.html)

## Family Overview

| Family | Legacy Chain | Skills | Audit States |
| --- | --- | --- | --- |
| legacy-page:bravo | bystander fist<br>hate sword<br>iron shield | 3 | legacy_catalog_seeded |

## Skill Cards

## legacy-page:bravo

Legacy chain: `bystander fist / hate sword / iron shield`

### 隔山打牛 / `bystander fist`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:bravo`
- Legacy prerequisite: `從缺`
- Legacy next: `-`
- Runtime file: `skill/b/bystander_fist.ski`
- Runtime slot: `SLOT_BYSTANDER_FIST`
- Runtime key: `bystander_fist`
- Type: `TAR_STRING`
- Cost / Wait: `25 / 30`
- CostType / Weapon / Check: `COST_MOVE / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `刺 客 >= 七十級, max 一代宗師﹗`
- Restrictions: `attrs: 敏捷 >= 三十五`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/bravo.html`

### 劍君十二恨 / `hate sword`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:bravo`
- Legacy prerequisite: `從缺`
- Legacy next: `-`
- Runtime file: `skill/h/hate_sword.ski`
- Runtime slot: `SLOT_HATE_SWORD`
- Runtime key: `hate_sword`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `40 / 9`
- CostType / Weapon / Check: `COST_MOVE / WEAPON_SWORD / check_sword_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `刺 客 >= 八十級, max 一代宗師﹗; 將 軍 >= 八十級, max 登峰造極﹗`
- Restrictions: `attrs: 學識 >= 三十, 敏捷 >= 三十, 力量 >= 三十; skills: 龍袖劍法 >= 粗通皮毛, 天道九劍 >= 馬馬虎虎; classes: 刺 客/將 軍`
- Damage values: `[155, 175, 195, 220, 245, 275, 310, 350, 395, 445, 500, 560]`
- Chance values: `[10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/bravo.html`

### 鐵布衫 / `iron shield`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:bravo`
- Legacy prerequisite: `從缺`
- Legacy next: `-`
- Runtime file: `skill/i/iron_shield.ski`
- Runtime slot: `SLOT_IRON_SHIELD`
- Runtime key: `iron_shield`
- Type: `TAR_CHAR_DEFENSIVE`
- Cost / Wait: `45 / 25`
- CostType / Weapon / Check: `COST_HIT / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `刺 客 >= 七十五級, max 一代宗師﹗`
- Restrictions: `attrs: 敏捷 >= 二十五`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/bravo.html`

