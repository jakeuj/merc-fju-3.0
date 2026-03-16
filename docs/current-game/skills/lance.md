---
layout: default
title: Current Game 槍 Skills
---

# Current Game 武器技能 / 槍

這頁是 `docs/current-game/skills.json` 的 `武器技能 / 槍` 可讀版，將舊站鏈路、現行 runtime 與調整維度放在同一頁。

- Skills in this page: `2`
- Source JSON: [`skills.json`](../skills.json)
- Registry note: [`skills.md`](../skills.html)
- Index: [`skills-index.md`](../skills-index.html)

## Family Overview

| Family | Legacy Chain | Skills | Audit States |
| --- | --- | --- | --- |
| legacy-page:lance | young gun -> eight gun | 2 | legacy_catalog_seeded |

## Skill Cards

## legacy-page:lance

Legacy chain: `young gun -> eight gun`

### 密傳˙八極槍 / `eight gun`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:lance`
- Legacy prerequisite: `楊家槍法(young gun)`
- Legacy next: `-`
- Runtime file: `skill/e/eight_gun.ski`
- Runtime slot: `SLOT_EIGHT_GUN`
- Runtime key: `eight_gun`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `30 / 17`
- CostType / Weapon / Check: `COST_MOVE / WEAPON_SPEAR / check_spear_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `刺 客 >= 五十級, max 神乎其技﹗; 將 軍 >= 五十級, max 一代宗師﹗`
- Restrictions: `attrs: 力量 >= 二十; skills: 楊家槍法 >= 神乎其技; classes: 刺 客/將 軍`
- Damage values: `[20, 20, 20, 20, 20, 20, 20, 20, 20]`
- Chance values: `[10, 10, 10, 10, 10, 10, 10, 10, 10]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/lance.html`

### 楊家槍法 / `young gun`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:lance`
- Legacy prerequisite: `從缺`
- Legacy next: `eight gun`
- Runtime file: `skill/y/younggun.ski`
- Runtime slot: `SLOT_YOUNGGUN`
- Runtime key: `younggun`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `20 / 14`
- CostType / Weapon / Check: `COST_MOVE / WEAPON_SPEAR / check_spear_attack`
- CanAsk / Teach / Valid / Enable: `No / No / Yes / Yes`
- Class limits: `刺 客 >= 二十級, max 神乎其技﹗; 武 官 >= 二十級, max 出類拔萃﹗; 將 軍 >= 二十級, max 一代宗師﹗`
- Restrictions: `-`
- Damage values: `[20, 20, 20, 20, 20, 20, 20]`
- Chance values: `[20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/lance.html`

