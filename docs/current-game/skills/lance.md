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

## Legacy Damage Policy

- Balance goal: `hybrid runtime-first`
- Formula policy: `piecewise linear default`
- Primary metrics: `failenable_mean / practice_adjusted_mean(30, 60, 90, npc_100) / tempo_pressure`
- Player tier model: `level_equals_practice_tier`
- Separate tracks: `TAR_CHAR_OFFENSIVE -> offensive ladder; TAR_DODGE -> dodge ladder`
- Non-linear exceptions: `disallowed unless explicitly documented in combat_tuning_profile`

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
- Damage model: `data-driven`
- Damage values: `[170, 195, 220, 245, 270, 300, 335, 375, 420]`
- Chance values: `[10, 10, 10, 10, 10, 10, 10, 10, 10]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Failenable mean: `281.11`
- Practice-adjusted mean: `player_30=207.95; player_60=259.61; player_90=323.07; npc_100=281.11`
- Tempo pressure: `player_30=12.23; player_60=15.27; player_90=19; npc_100=16.54`
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
- Damage model: `data-driven`
- Damage values: `[90, 110, 130, 150, 170, 195, 220]`
- Chance values: `[20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Failenable mean: `152.14`
- Practice-adjusted mean: `player_30=111.9; player_60=143.33; player_90=177.3; npc_100=152.14`
- Tempo pressure: `player_30=7.99; player_60=10.24; player_90=12.66; npc_100=10.87`
- Legacy page source: `skill/lance.html`

