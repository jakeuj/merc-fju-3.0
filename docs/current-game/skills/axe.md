---
layout: default
title: Current Game 斧 Skills
---

# Current Game 武器技能 / 斧

這頁是 `docs/current-game/skills.json` 的 `武器技能 / 斧` 可讀版，將舊站鏈路、現行 runtime 與調整維度放在同一頁。

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
| legacy-page:axe | ghost axe -> tiger axe | 2 | legacy_catalog_seeded |

## Skill Cards

## legacy-page:axe

Legacy chain: `ghost axe -> tiger axe`

### 神盤鬼斧六絕式 / `ghost axe`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:axe`
- Legacy prerequisite: `從缺`
- Legacy next: `tiger axe`
- Runtime file: `skill/g/ghost_axe.ski`
- Runtime slot: `SLOT_GHOST_AXE`
- Runtime key: `ghost_axe`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `30 / 15`
- CostType / Weapon / Check: `COST_MOVE / WEAPON_AXE / check_axe_attack`
- CanAsk / Teach / Valid / Enable: `Yes / Yes / Yes / Yes`
- Class limits: `伶 人 >= 一級, max 馬馬虎虎﹗; 刺 客 >= 一級, max 神乎其技﹗; 平 民 >= 一級, max 馬馬虎虎﹗; 郎 中 >= 一級, max 馬馬虎虎﹗; 武 官 >= 一級, max 出類拔萃﹗; 將 軍 >= 一級, max 一代宗師﹗; 天 師 >= 一級, max 馬馬虎虎﹗; 文 官 >= 一級, max 馬馬虎虎﹗; 道 士 >= 一級, max 馬馬虎虎﹗; 鑄劍師 >= 一級, max 馬馬虎虎﹗; 盜 賊 >= 一級, max 馬馬虎虎﹗`
- Restrictions: `-`
- Damage model: `data-driven`
- Damage values: `[95, 115, 135, 155, 180, 210]`
- Chance values: `[20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Failenable mean: `148.33`
- Practice-adjusted mean: `player_30=112.77; player_60=139.44; player_90=170.18; npc_100=148.33`
- Tempo pressure: `player_30=7.52; player_60=9.3; player_90=11.35; npc_100=9.89`
- Legacy page source: `skill/axe.html`

### 霸虎戰訣 / `tiger axe`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:axe`
- Legacy prerequisite: `神盤鬼斧六絕式(ghost axe)`
- Legacy next: `-`
- Runtime file: `skill/t/tiger_axe.ski`
- Runtime slot: `SLOT_TIGER_AXE`
- Runtime key: `tiger_axe`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `35 / 18`
- CostType / Weapon / Check: `COST_MOVE / WEAPON_AXE / check_axe_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `刺 客 >= 一級, max 神乎其技﹗; 將 軍 >= 一級, max 一代宗師﹗`
- Restrictions: `attrs: 力量 >= 三十; skills: 神盤鬼斧六絕式 >= 神乎其技; classes: 刺 客/將 軍`
- Damage model: `data-driven`
- Damage values: `[180, 205, 230, 255, 280, 305, 335, 365, 400, 440, 485, 540, 600]`
- Chance values: `[20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Failenable mean: `355.38`
- Practice-adjusted mean: `player_30=240.89; player_60=317.3; player_90=418.58; npc_100=355.38`
- Tempo pressure: `player_30=13.38; player_60=17.63; player_90=23.25; npc_100=19.74`
- Legacy page source: `skill/axe.html`

