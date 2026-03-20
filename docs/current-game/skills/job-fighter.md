---
layout: default
title: Current Game 格鬥系 Skills
---

# Current Game 職業技能 / 格鬥系

這頁是 `docs/current-game/skills.json` 的 `職業技能 / 格鬥系` 可讀版，將舊站鏈路、現行 runtime 與調整維度放在同一頁。

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
| legacy-page:general | dragon phoenix<br>gold shield | 2 | legacy_catalog_seeded |

## Skill Cards

## legacy-page:general

Legacy chain: `dragon phoenix / gold shield`

### 斬龍破鳳刀 / `dragon phoenix`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:general`
- Legacy prerequisite: `從缺`
- Legacy next: `-`
- Runtime file: `skill/d/dragon_phoe.ski`
- Runtime slot: `SLOT_DRAGON_PHOE`
- Runtime key: `dragon_phoe`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `40 / 10`
- CostType / Weapon / Check: `COST_MOVE / WEAPON_BLADE / check_blade_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `刺 客 >= 八十級, max 出神入化﹗; 將 軍 >= 八十級, max 一代宗師﹗`
- Restrictions: `attrs: 敏捷 >= 二十五, 力量 >= 三十; skills: 幔羅千葉刀法 >= 粗通皮毛, 魔刀 >= 出神入化; classes: 刺 客/將 軍`
- Damage model: `data-driven`
- Damage values: `[180, 210, 240, 270, 305, 345, 390, 440, 500]`
- Chance values: `[20, 20, 20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Failenable mean: `320`
- Practice-adjusted mean: `player_30=225.55; player_60=290.73; player_90=374; npc_100=320`
- Tempo pressure: `player_30=22.55; player_60=29.07; player_90=37.4; npc_100=32`
- Legacy page source: `skill/general.html`

### 金鐘罩 / `gold shield`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:general`
- Legacy prerequisite: `從缺`
- Legacy next: `-`
- Runtime file: `skill/g/gold_shield.ski`
- Runtime slot: `SLOT_GOLD_SHIELD`
- Runtime key: `gold_shield`
- Type: `TAR_CHAR_DEFENSIVE`
- Cost / Wait: `50 / 25`
- CostType / Weapon / Check: `COST_HIT / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `將 軍 >= 七十五級, max 一代宗師﹗`
- Restrictions: `attrs: 體格 >= 二十五`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/general.html`

