---
layout: default
title: Current Game 拳法 Skills
---

# Current Game 武器技能 / 拳法

這頁是 `docs/current-game/skills.json` 的 `武器技能 / 拳法` 可讀版，將舊站鏈路、現行 runtime 與調整維度放在同一頁。

- Skills in this page: `12`
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
| legacy-page:fist | evil fist -> evil king<br>ghost strike -> ghost marial<br>king fist -> sky dragon<br>long fist -> lung shan -> tackle<br>rulai<br>ryo -> hashin | 12 | batch_c_implemented, legacy_catalog_seeded |

## Skill Cards

## legacy-page:fist

Legacy chain: `evil fist -> evil king / ghost strike -> ghost marial / king fist -> sky dragon / long fist -> lung shan -> tackle / rulai / ryo -> hashin`

### 惡霸掌 / `evil fist`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:fist`
- Legacy prerequisite: `從缺`
- Legacy next: `evil king`
- Runtime file: `skill/e/evilfist.ski`
- Runtime slot: `SLOT_EVILFIST`
- Runtime key: `evilfist`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `20 / 10`
- CostType / Weapon / Check: `COST_MOVE / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `刺 客 >= 一級, max 一代宗師﹗; 武 官 >= 一級, max 出類拔萃﹗; 將 軍 >= 一級, max 一代宗師﹗; 盜 賊 >= 一級, max 出類拔萃﹗`
- Restrictions: `-`
- Damage model: `data-driven`
- Damage values: `[70, 85, 100, 115, 130, 155, 190]`
- Chance values: `[10, 10, 10, 10, 10, 10, 10]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Failenable mean: `120.71`
- Practice-adjusted mean: `player_30=86.43; player_60=110; player_90=139.6; npc_100=120.71`
- Tempo pressure: `player_30=8.64; player_60=11; player_90=13.96; npc_100=12.07`
- Legacy page source: `skill/fist.html`

### 邪皇拳 / `evil king`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:fist`
- Legacy prerequisite: `惡霸掌(evil fist)`
- Legacy next: `-`
- Runtime file: `skill/e/evil_king.ski`
- Runtime slot: `SLOT_EVIL_KING`
- Runtime key: `evil_king`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `20 / 8`
- CostType / Weapon / Check: `COST_MOVE / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `刺 客 >= 一級, max 一代宗師﹗; 武 官 >= 一級, max 出類拔萃﹗; 將 軍 >= 一級, max 一代宗師﹗; 盜 賊 >= 一級, max 出類拔萃﹗`
- Restrictions: `attrs: 力量 >= 十五; skills: 惡霸掌 >= 出類拔萃`
- Damage model: `data-driven`
- Damage values: `[125, 145, 165, 185, 205, 230, 260, 300]`
- Chance values: `[10, 10, 10, 10, 10, 10, 10, 10]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Failenable mean: `201.88`
- Practice-adjusted mean: `player_30=151.66; player_60=186.66; player_90=230.27; npc_100=201.88`
- Tempo pressure: `player_30=18.96; player_60=23.33; player_90=28.78; npc_100=25.23`
- Legacy page source: `skill/fist.html`

### 鬼拳 / `ghost marial`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:fist`
- Legacy prerequisite: `玄陰掌(ghost strike)`
- Legacy next: `-`
- Runtime file: `skill/g/ghost_marial.ski`
- Runtime slot: `SLOT_GHOST_MARIAL`
- Runtime key: `ghost_marial`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `20 / 7`
- CostType / Weapon / Check: `COST_MOVE / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `伶 人 >= 一級, max 出類拔萃﹗; 刺 客 >= 一級, max 一代宗師﹗; 郎 中 >= 一級, max 出類拔萃﹗; 將 軍 >= 一級, max 登峰造極﹗; 天 師 >= 一級, max 出類拔萃﹗; 鑄劍師 >= 一級, max 出類拔萃﹗; 盜 賊 >= 一級, max 神乎其技﹗`
- Restrictions: `attrs: 敏捷 >= 十五; skills: 玄陰掌 >= 出類拔萃`
- Damage model: `data-driven`
- Damage values: `[135, 160, 185, 210, 240, 275]`
- Chance values: `[20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Failenable mean: `200.83`
- Practice-adjusted mean: `player_30=157.21; player_60=190.55; player_90=227.96; npc_100=200.83`
- Tempo pressure: `player_30=22.46; player_60=27.22; player_90=32.57; npc_100=28.69`
- Legacy page source: `skill/fist.html`

### 玄陰掌 / `ghost strike`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:fist`
- Legacy prerequisite: `從缺`
- Legacy next: `ghost marial`
- Runtime file: `skill/g/ghoststrike.ski`
- Runtime slot: `SLOT_GHOSTSTRIKE`
- Runtime key: `ghoststrike`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `20 / 10`
- CostType / Weapon / Check: `COST_MOVE / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / Yes / Yes / Yes`
- Class limits: `伶 人 >= 一級, max 出類拔萃﹗; 刺 客 >= 一級, max 一代宗師﹗; 郎 中 >= 一級, max 出類拔萃﹗; 武 官 >= 一級, max 馬馬虎虎﹗; 將 軍 >= 一級, max 登峰造極﹗; 天 師 >= 一級, max 出類拔萃﹗; 文 官 >= 一級, max 馬馬虎虎﹗; 道 士 >= 一級, max 馬馬虎虎﹗; 鑄劍師 >= 一級, max 出類拔萃﹗; 盜 賊 >= 一級, max 登峰造極﹗`
- Restrictions: `-`
- Damage model: `data-driven`
- Damage values: `[75, 95, 115, 135, 155, 180, 210]`
- Chance values: `[20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Failenable mean: `137.86`
- Practice-adjusted mean: `player_30=96.9; player_60=128.33; player_90=162.77; npc_100=137.86`
- Tempo pressure: `player_30=9.69; player_60=12.83; player_90=16.28; npc_100=13.79`
- Legacy page source: `skill/fist.html`

### 秘拳．八神 / `hashin`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:fist`
- Legacy prerequisite: `草薙拳法(ryo)`
- Legacy next: `-`
- Runtime file: `skill/h/hashin.ski`
- Runtime slot: `SLOT_HASHIN`
- Runtime key: `hashin`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `30 / 5`
- CostType / Weapon / Check: `COST_MOVE / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `刺 客 >= 五十級, max 一代宗師﹗; 將 軍 >= 五十級, max 一代宗師﹗`
- Restrictions: `attrs: 力量 >= 二十五; skills: 草薙拳法 >= 出類拔萃; classes: 刺 客/將 軍`
- Damage model: `data-driven`
- Damage values: `[170, 195, 220, 245, 275, 310, 350, 395, 445, 500]`
- Chance values: `[20, 20, 20, 20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Failenable mean: `310.5`
- Practice-adjusted mean: `player_30=211.66; player_60=276.66; player_90=363.88; npc_100=310.5`
- Tempo pressure: `player_30=42.33; player_60=55.33; player_90=72.78; npc_100=62.1`
- Legacy page source: `skill/fist.html`

### 王拳 / `king fist`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:fist`
- Legacy prerequisite: `從缺`
- Legacy next: `sky dragon`
- Runtime file: `skill/k/king_fist.ski`
- Runtime slot: `SLOT_KING_FIST`
- Runtime key: `king_fist`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `19 / 12`
- CostType / Weapon / Check: `COST_MOVE / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `No / No / No / Yes`
- Class limits: `伶 人 >= 一級, max 馬馬虎虎﹗; 刺 客 >= 一級, max 一代宗師﹗; 平 民 >= 一級, max 馬馬虎虎﹗; 郎 中 >= 一級, max 馬馬虎虎﹗; 武 官 >= 一級, max 出類拔萃﹗; 將 軍 >= 一級, max 登峰造極﹗; 天 師 >= 一級, max 馬馬虎虎﹗; 文 官 >= 一級, max 馬馬虎虎﹗; 道 士 >= 一級, max 馬馬虎虎﹗; 鑄劍師 >= 一級, max 馬馬虎虎﹗; 盜 賊 >= 一級, max 出類拔萃﹗`
- Restrictions: `-`
- Damage model: `data-driven`
- Damage values: `[95, 115, 135, 155, 175, 200, 230]`
- Chance values: `[10, 10, 10, 10, 10, 10, 10]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Failenable mean: `157.86`
- Practice-adjusted mean: `player_30=116.9; player_60=148.33; player_90=182.77; npc_100=157.86`
- Tempo pressure: `player_30=9.74; player_60=12.36; player_90=15.23; npc_100=13.16`
- Legacy page source: `skill/fist.html`

### 泰山長拳 / `long fist`

- Audit: `batch_c_implemented`
- Family: `legacy-page:fist`
- Legacy prerequisite: `從缺`
- Legacy next: `lung shan`
- Runtime file: `skill/l/longfist.ski`
- Runtime slot: `SLOT_LONGFIST`
- Runtime key: `longfist`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `10 / 5`
- CostType / Weapon / Check: `COST_MOVE / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / Yes / Yes / Yes`
- Class limits: `伶 人 >= 一級, max 馬馬虎虎﹗; 刺 客 >= 一級, max 一代宗師﹗; 平 民 >= 一級, max 馬馬虎虎﹗; 郎 中 >= 一級, max 馬馬虎虎﹗; 武 官 >= 一級, max 出類拔萃﹗; 將 軍 >= 一級, max 一代宗師﹗; 天 師 >= 一級, max 馬馬虎虎﹗; 文 官 >= 一級, max 馬馬虎虎﹗; 道 士 >= 一級, max 馬馬虎虎﹗; 鑄劍師 >= 一級, max 馬馬虎虎﹗; 盜 賊 >= 一級, max 出類拔萃﹗`
- Restrictions: `-`
- Damage model: `data-driven`
- Damage values: `[45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 135]`
- Chance values: `[20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Failenable mean: `87.78`
- Practice-adjusted mean: `player_30=62.78; player_60=82.96; player_90=103.27; npc_100=87.78`
- Tempo pressure: `player_30=12.56; player_60=16.59; player_90=20.65; npc_100=17.56`
- Legacy page source: `skill/fist.html`

### 瀧山拳法 / `lung shan`

- Audit: `batch_c_implemented`
- Family: `legacy-page:fist`
- Legacy prerequisite: `泰山長拳(long fist)`
- Legacy next: `tackle`
- Runtime file: `skill/l/lungshan.ski`
- Runtime slot: `SLOT_LUNGSHAN`
- Runtime key: `lungshan`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `10 / 5`
- CostType / Weapon / Check: `COST_MOVE / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `刺 客 >= 一級, max 一代宗師﹗; 武 官 >= 一級, max 出類拔萃﹗; 將 軍 >= 一級, max 登峰造極﹗; 盜 賊 >= 一級, max 神乎其技﹗`
- Restrictions: `skills: 泰山長拳 >= 心神領會`
- Damage model: `data-driven`
- Damage values: `[100, 115, 130, 145, 160, 180, 205]`
- Chance values: `[20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Failenable mean: `147.86`
- Practice-adjusted mean: `player_30=116.43; player_60=140; player_90=166.58; npc_100=147.86`
- Tempo pressure: `player_30=23.29; player_60=28; player_90=33.32; npc_100=29.57`
- Legacy page source: `skill/fist.html`

### 如來神掌 / `rulai`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:fist`
- Legacy prerequisite: `從缺`
- Legacy next: `-`
- Runtime file: `skill/r/rulai.ski`
- Runtime slot: `SLOT_RULAI`
- Runtime key: `rulai`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `20 / 10`
- CostType / Weapon / Check: `COST_MOVE / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `No / No / Yes / Yes`
- Class limits: `刺 客 >= 一級, max 一代宗師﹗; 將 軍 >= 一級, max 一代宗師﹗`
- Restrictions: `-`
- Damage model: `data-driven`
- Damage values: `[120, 145, 170, 195, 220, 250, 285, 325, 370]`
- Chance values: `[20, 20, 20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Failenable mean: `231.11`
- Practice-adjusted mean: `player_30=157.96; player_60=209.62; player_90=273.08; npc_100=231.11`
- Tempo pressure: `player_30=15.8; player_60=20.96; player_90=27.31; npc_100=23.11`
- Legacy page source: `skill/fist.html`

### 草薙拳法 / `ryo`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:fist`
- Legacy prerequisite: `從缺`
- Legacy next: `hashin`
- Runtime file: `skill/r/ryo.ski`
- Runtime slot: `SLOT_RYO`
- Runtime key: `ryo`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `20 / 5`
- CostType / Weapon / Check: `COST_MOVE / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `伶 人 >= 一級, max 馬馬虎虎﹗; 刺 客 >= 一級, max 一代宗師﹗; 郎 中 >= 一級, max 馬馬虎虎﹗; 武 官 >= 一級, max 心神領會﹗; 將 軍 >= 一級, max 一代宗師﹗; 天 師 >= 一級, max 馬馬虎虎﹗; 文 官 >= 一級, max 粗通皮毛﹗; 道 士 >= 一級, max 粗通皮毛﹗; 鑄劍師 >= 一級, max 馬馬虎虎﹗; 盜 賊 >= 一級, max 馬馬虎虎﹗`
- Restrictions: `-`
- Damage model: `data-driven`
- Damage values: `[150, 135, 155, 175, 195, 220, 250]`
- Chance values: `[20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Failenable mean: `182.86`
- Practice-adjusted mean: `player_30=136.9; player_60=168.33; player_90=202.77; npc_100=182.86`
- Tempo pressure: `player_30=27.38; player_60=33.67; player_90=40.55; npc_100=36.57`
- Legacy page source: `skill/fist.html`

### 天龍真氣 / `sky dragon force`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:fist`
- Legacy prerequisite: `天龍訣(sky dragon)`
- Legacy next: `-`
- Runtime file: `skill/s/skydragon_force.ski`
- Runtime slot: `SLOT_SKYDRAGON_FORCE`
- Runtime key: `skydragon_force`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `10 / 1`
- CostType / Weapon / Check: `COST_MOVE / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `No / No / No / Yes`
- Class limits: `刺 客 >= 一級, max 一代宗師﹗; 將 軍 >= 一級, max 登峰造極﹗; 盜 賊 >= 一級, max 神乎其技﹗; 伶 人 >= -, max -; 平 民 >= -, max -; 郎 中 >= -, max -; 武 官 >= -, max -; 天 師 >= -, max -; 文 官 >= -, max -; 道 士 >= -, max -; 鑄劍師 >= -, max -`
- Restrictions: `skills: 天龍訣 >= 神乎其技`
- Damage model: `data-driven`
- Damage values: `[220, 270, 330]`
- Chance values: `[10, 10, 10]`
- Parry values: `[0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0']`
- Failenable mean: `273.33`
- Practice-adjusted mean: `player_30=220; player_60=264.4; player_90=301.09; npc_100=273.33`
- Tempo pressure: `player_30=220; player_60=264.4; player_90=301.09; npc_100=273.33`
- Legacy page source: `skill/fist.html`

### 小擒拿手 / `tackle`

- Audit: `batch_c_implemented`
- Family: `legacy-page:fist`
- Legacy prerequisite: `瀧山拳法(lung shan)`
- Legacy next: `-`
- Runtime file: `skill/t/tackle.ski`
- Runtime slot: `SLOT_TACKLE`
- Runtime key: `tackle`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `10 / 5`
- CostType / Weapon / Check: `COST_MOVE / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `刺 客 >= 一級, max 一代宗師﹗; 將 軍 >= 一級, max 登峰造極﹗; 盜 賊 >= 一級, max 神乎其技﹗`
- Restrictions: `skills: 瀧山拳法 >= 神乎其技`
- Damage model: `data-driven`
- Damage values: `[140, 160, 180, 200, 220, 240, 260, 290]`
- Chance values: `[20, 20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Failenable mean: `211.25`
- Practice-adjusted mean: `player_30=166.66; player_60=201.66; player_90=238.33; npc_100=211.25`
- Tempo pressure: `player_30=33.33; player_60=40.33; player_90=47.67; npc_100=42.25`
- Legacy page source: `skill/fist.html`

