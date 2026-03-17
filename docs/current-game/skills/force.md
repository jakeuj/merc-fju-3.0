---
layout: default
title: Current Game 氣功 Skills
---

# Current Game 武器技能 / 氣功

這頁是 `docs/current-game/skills.json` 的 `武器技能 / 氣功` 可讀版，將舊站鏈路、現行 runtime 與調整維度放在同一頁。

- Skills in this page: `3`
- Source JSON: [`skills.json`](../skills.json)
- Registry note: [`skills.md`](../skills.html)
- Index: [`skills-index.md`](../skills-index.html)

## Family Overview

| Family | Legacy Chain | Skills | Audit States |
| --- | --- | --- | --- |
| legacy-page:energy | universe -> six fire -> fire dragon | 3 | legacy_catalog_seeded |

## Skill Cards

## legacy-page:energy

Legacy chain: `universe -> six fire -> fire dragon`

### 炎龍九式 / `fire dragon`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:energy`
- Legacy prerequisite: `極火六陽(six fire)`
- Legacy next: `-`
- Runtime file: `skill/f/fire_dragon.ski`
- Runtime slot: `SLOT_FIRE_DRAGON`
- Runtime key: `fire_dragon`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `30 / 7`
- CostType / Weapon / Check: `COST_MOVE / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `刺 客 >= 一級, max 一代宗師﹗`
- Restrictions: `skills: 極火六陽 >= 登峰造極; classes: 刺 客`
- Damage values: `[220, 250, 280, 310, 340, 375, 415, 460, 520]`
- Chance values: `[20, 20, 20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/energy.html`

### 極火六陽 / `six fire`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:energy`
- Legacy prerequisite: `先天乾坤功(universe)`
- Legacy next: `fire dragon`
- Runtime file: `skill/s/sixfire.ski`
- Runtime slot: `SLOT_SIXFIRE`
- Runtime key: `sixfire`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `25 / 5`
- CostType / Weapon / Check: `COST_MOVE / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `刺 客 >= 一級, max 一代宗師﹗; 將 軍 >= 一級, max 神乎其技﹗`
- Restrictions: `attrs: 力量 >= 二十, 體格 >= 二十; skills: 先天乾坤功 >= 神乎其技; classes: 刺 客/將 軍`
- Damage values: `[140, 160, 180, 205, 230, 260]`
- Chance values: `[20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/energy.html`

### 先天乾坤功 / `universe`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:energy`
- Legacy prerequisite: `從缺`
- Legacy next: `six fire`
- Runtime file: `skill/u/universe.ski`
- Runtime slot: `SLOT_UNIVERSE`
- Runtime key: `universe`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `20 / 5`
- CostType / Weapon / Check: `COST_MOVE / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `刺 客 >= 一級, max 一代宗師﹗; 武 官 >= 一級, max 出類拔萃﹗; 將 軍 >= 一級, max 登峰造極﹗`
- Restrictions: `attrs: 體格 >= 十`
- Damage values: `[70, 85, 100, 115, 130, 150, 170]`
- Chance values: `[20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/energy.html`

