---
layout: default
title: Current Game 刀 Skills
---

# Current Game 武器技能 / 刀

這頁是 `docs/current-game/skills.json` 的 `武器技能 / 刀` 可讀版，將舊站鏈路、現行 runtime 與調整維度放在同一頁。

- Skills in this page: `10`
- Source JSON: [`skills.json`](../skills.json)
- Registry note: [`skills.md`](../skills.html)
- Index: [`skills-index.md`](../skills-index.html)

## Family Overview

| Family | Legacy Chain | Skills | Audit States |
| --- | --- | --- | --- |
| legacy-page:blade | dream blade -> sea flow blade -> fast blade<br>her blade -> dragon blade -> tiger blade<br>sun blade -> ice blade -> gold blade | 10 | legacy_catalog_seeded |

## Skill Cards

## legacy-page:blade

Legacy chain: `dream blade -> sea flow blade -> fast blade / her blade -> dragon blade -> tiger blade / sun blade -> ice blade -> gold blade`

### 魔刀 / `dragon blade`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:blade`
- Legacy prerequisite: `猛龍刀法(her blade)`
- Legacy next: `tiger blade`
- Runtime file: `skill/d/dragon_blade.ski`
- Runtime slot: `SLOT_DRAGON_BLADE`
- Runtime key: `dragon_blade`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `15 / 14`
- CostType / Weapon / Check: `COST_MOVE / WEAPON_BLADE / check_blade_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `刺 客 >= 一級, max 出神入化﹗; 武 官 >= 一級, max 心神領會﹗; 將 軍 >= 一級, max 一代宗師﹗`
- Restrictions: `attrs: 力量 >= 十五; skills: 猛龍刀法 >= 心神領會`
- Damage values: `[140, 160, 180, 200, 220, 240, 260, 285, 315]`
- Chance values: `[20, 20, 20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/blade.html`

### 相思碎夢刀法 / `dream blade`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:blade`
- Legacy prerequisite: `從缺`
- Legacy next: `sea flow blade`
- Runtime file: `skill/d/dream_blade.ski`
- Runtime slot: `SLOT_DREAM_BLADE`
- Runtime key: `dream_blade`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `25 / 15`
- CostType / Weapon / Check: `COST_MOVE / WEAPON_BLADE / check_blade_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `刺 客 >= 五十級, max 登峰造極﹗; 武 官 >= 三十級, max 出類拔萃﹗; 將 軍 >= 五十級, max 一代宗師﹗`
- Restrictions: `-`
- Damage values: `[95, 115, 135, 155, 175, 195, 215, 240, 270]`
- Chance values: `[20, 20, 20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/blade.html`

### 夢魂七絕 / `dream soul`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:blade`
- Legacy prerequisite: `從缺 職業性別限制﹕女性`
- Legacy next: `-`
- Runtime file: `skill/d/dream_soul.ski`
- Runtime slot: `SLOT_DREAM_SOUL`
- Runtime key: `dream_soul`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `30 / 16`
- CostType / Weapon / Check: `COST_MOVE / WEAPON_BLADE / check_blade_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `刺 客 >= 八十級, max 登峰造極﹗; 將 軍 >= 八十級, max 一代宗師﹗`
- Restrictions: `attrs: 學識 >= 二十五, 體格 >= 三十, 敏捷 >= 三十; skills: 魔刀 >= 出神入化, 花語刀法 >= 登峰造極; classes: 刺 客/將 軍`
- Damage values: `[20, 20, 20, 20, 20, 20, 20, 20]`
- Chance values: `[20, 20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/blade.html`

### 幔羅千葉刀法 / `fast blade`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:blade`
- Legacy prerequisite: `花語刀法(sea flow blade)`
- Legacy next: `-`
- Runtime file: `skill/f/fast_blade.ski`
- Runtime slot: `SLOT_FAST_BLADE`
- Runtime key: `fast_blade`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `30 / 11`
- CostType / Weapon / Check: `COST_MOVE / WEAPON_BLADE / check_blade_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `刺 客 >= 一級, max 神乎其技﹗; 將 軍 >= 一級, max 一代宗師﹗`
- Restrictions: `attrs: 敏捷 >= 二十五, 力量 >= 二十; skills: 花語刀法 >= 登峰造極; classes: 刺 客/將 軍`
- Damage values: `[190, 205, 220, 235, 250, 265, 280, 295, 310, 325, 340, 355, 370, 385, 400, 420, 440, 460, 480, 500, 520, 550]`
- Chance values: `[20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/blade.html`

### 紫金六陽刀法 / `gold blade`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:blade`
- Legacy prerequisite: `傲寒六訣(ice blade)`
- Legacy next: `-`
- Runtime file: `skill/g/gold_blade.ski`
- Runtime slot: `SLOT_GOLD_BLADE`
- Runtime key: `gold_blade`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `15 / 10`
- CostType / Weapon / Check: `COST_MOVE / WEAPON_BLADE / check_blade_attack`
- CanAsk / Teach / Valid / Enable: `No / No / No / Yes`
- Class limits: `將 軍 >= 一級, max 一代宗師﹗; 伶 人 >= -, max -; 刺 客 >= -, max -; 平 民 >= -, max -; 郎 中 >= -, max -; 武 官 >= -, max -; 天 師 >= -, max -; 文 官 >= -, max -; 道 士 >= -, max -; 鑄劍師 >= -, max -; 盜 賊 >= -, max -`
- Restrictions: `attrs: 敏捷 >= 二十五, 力量 >= 三十; skills: 傲寒六訣 >= 登峰造極; classes: 將 軍`
- Damage values: `[20, 20, 20, 20, 20, 20, 20, 20, 20, 20]`
- Chance values: `[10, 10, 10, 10, 10, 10, 10, 10, 10, 10]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/blade.html`

### 猛龍刀法 / `her blade`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:blade`
- Legacy prerequisite: `從缺`
- Legacy next: `dragon blade`
- Runtime file: `skill/h/her_blade.ski`
- Runtime slot: `SLOT_HER_BLADE`
- Runtime key: `her_blade`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `15 / 8`
- CostType / Weapon / Check: `COST_MOVE / WEAPON_BLADE / check_blade_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `刺 客 >= 一級, max 出神入化﹗; 武 官 >= 一級, max 心神領會﹗; 將 軍 >= 一級, max 一代宗師﹗`
- Restrictions: `-`
- Damage values: `[75, 90, 105, 120, 135, 150, 165, 185]`
- Chance values: `[10, 10, 10, 10, 10, 10, 10, 10]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/blade.html`

### 傲寒六訣 / `ice blade`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:blade`
- Legacy prerequisite: `皓日刀法(sun blade)`
- Legacy next: `gold blade`
- Runtime file: `skill/i/iceblade.ski`
- Runtime slot: `SLOT_ICEBLADE`
- Runtime key: `iceblade`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `15 / 10`
- CostType / Weapon / Check: `COST_MOVE / WEAPON_BLADE / check_blade_attack`
- CanAsk / Teach / Valid / Enable: `No / No / No / Yes`
- Class limits: `刺 客 >= 五十級, max 登峰造極﹗; 武 官 >= 十級, max 出類拔萃﹗; 將 軍 >= 五十級, max 一代宗師﹗; 伶 人 >= -, max -; 平 民 >= -, max -; 郎 中 >= -, max -; 天 師 >= -, max -; 文 官 >= -, max -; 道 士 >= -, max -; 鑄劍師 >= -, max -; 盜 賊 >= -, max -`
- Restrictions: `attrs: 力量 >= 二十; skills: 皓日刀法 >= 心神領會`
- Damage values: `[20, 20, 20, 20, 20, 20, 20, 20, 20]`
- Chance values: `[10, 10, 10, 10, 10, 10, 10, 10, 10]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/blade.html`

### 花語刀法 / `sea flow blade`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:blade`
- Legacy prerequisite: `相思碎夢刀法(dream blade)`
- Legacy next: `fast blade`
- Runtime file: `skill/s/seaflow_blade.ski`
- Runtime slot: `SLOT_SEAFLOW_BLADE`
- Runtime key: `seaflow_blade`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `25 / 12`
- CostType / Weapon / Check: `COST_MOVE / WEAPON_BLADE / check_blade_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `刺 客 >= 一級, max 登峰造極﹗; 武 官 >= 一級, max 心神領會﹗; 將 軍 >= 一級, max 一代宗師﹗`
- Restrictions: `attrs: 敏捷 >= 十五, 力量 >= 十五; skills: 相思碎夢刀法 >= 出類拔萃`
- Damage values: `[140, 165, 190, 215, 240, 265, 290, 325]`
- Chance values: `[20, 20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/blade.html`

### 皓日刀法 / `sun blade`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:blade`
- Legacy prerequisite: `從缺`
- Legacy next: `ice blade`
- Runtime file: `skill/s/sun_blade.ski`
- Runtime slot: `SLOT_SUN_BLADE`
- Runtime key: `sun_blade`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `10 / 1`
- CostType / Weapon / Check: `COST_MOVE / WEAPON_BLADE / check_blade_attack`
- CanAsk / Teach / Valid / Enable: `No / No / No / Yes`
- Class limits: `刺 客 >= 五十級, max 登峰造極﹗; 武 官 >= 十級, max 出類拔萃﹗; 將 軍 >= 五十級, max 一代宗師﹗; 伶 人 >= -, max -; 平 民 >= -, max -; 郎 中 >= -, max -; 天 師 >= -, max -; 文 官 >= -, max -; 道 士 >= -, max -; 鑄劍師 >= -, max -; 盜 賊 >= -, max -`
- Restrictions: `-`
- Damage values: `[20, 20, 20, 20, 20, 20]`
- Chance values: `[10, 10, 10, 10, 10, 10]`
- Parry values: `[0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/blade.html`

### 三千古皇刀法 / `tiger blade`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:blade`
- Legacy prerequisite: `魔刀(dragon blade)`
- Legacy next: `-`
- Runtime file: `skill/t/tigerblade.ski`
- Runtime slot: `SLOT_TIGERBLADE`
- Runtime key: `tigerblade`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `30 / 18`
- CostType / Weapon / Check: `COST_MOVE / WEAPON_BLADE / check_blade_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `將 軍 >= 一級, max 一代宗師﹗`
- Restrictions: `attrs: 敏捷 >= 二十, 力量 >= 二十五; skills: 魔刀 >= 登峰造極; classes: 將 軍`
- Damage values: `[240, 270, 300, 330, 360, 400, 440, 480, 520, 580]`
- Chance values: `[20, 20, 20, 20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/blade.html`

