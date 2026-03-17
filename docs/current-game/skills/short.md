---
layout: default
title: Current Game 短兵 Skills
---

# Current Game 武器技能 / 短兵

這頁是 `docs/current-game/skills.json` 的 `武器技能 / 短兵` 可讀版，將舊站鏈路、現行 runtime 與調整維度放在同一頁。

- Skills in this page: `4`
- Source JSON: [`skills.json`](../skills.json)
- Registry note: [`skills.md`](../skills.html)
- Index: [`skills-index.md`](../skills-index.html)

## Family Overview

| Family | Legacy Chain | Skills | Audit States |
| --- | --- | --- | --- |
| legacy-page:dagger | be needle -> seven dagger<br>dragon dagger -> rain throwing | 4 | legacy_catalog_seeded |

## Skill Cards

## legacy-page:dagger

Legacy chain: `be needle -> seven dagger / dragon dagger -> rain throwing`

### 碧血十二針 / `be needle`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:dagger`
- Legacy prerequisite: `從缺`
- Legacy next: `seven dagger`
- Runtime file: `skill/b/be_needle.ski`
- Runtime slot: `SLOT_BE_NEEDLE`
- Runtime key: `be_needle`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `20 / 2`
- CostType / Weapon / Check: `COST_MOVE / WEAPON_DAGGER / check_dagger_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `伶 人 >= 五十級, max 神乎其技﹗; 刺 客 >= 五十級, max 神乎其技﹗; 郎 中 >= 五十級, max 一代宗師﹗; 武 官 >= 二十五級, max 初窺門徑﹗; 將 軍 >= 五十級, max 出類拔萃﹗; 天 師 >= 五十級, max 出類拔萃﹗; 文 官 >= 二十五級, max 初窺門徑﹗; 道 士 >= 二十五級, max 初窺門徑﹗; 鑄劍師 >= 五十級, max 出類拔萃﹗; 盜 賊 >= 二十五級, max 登峰造極﹗`
- Restrictions: `-`
- Damage values: `[55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 110, 120]`
- Chance values: `[10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/dagger.html`

### 盤龍匕法 / `dragon dagger`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:dagger`
- Legacy prerequisite: `從缺`
- Legacy next: `rain throwing`
- Runtime file: `skill/d/dragon_dagger.ski`
- Runtime slot: `SLOT_DRAGON_DAGGER`
- Runtime key: `dragon_dagger`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `15 / 10`
- CostType / Weapon / Check: `COST_MOVE / WEAPON_DAGGER / check_dagger_attack`
- CanAsk / Teach / Valid / Enable: `No / No / No / Yes`
- Class limits: `伶 人 >= 五十級, max 出神入化﹗; 郎 中 >= 五十級, max 登峰造極﹗; 文 官 >= 十級, max 初窺門徑﹗; 盜 賊 >= 十級, max 一代宗師﹗; 刺 客 >= -, max -; 平 民 >= -, max -; 武 官 >= -, max -; 將 軍 >= -, max -; 天 師 >= -, max -; 道 士 >= -, max -; 鑄劍師 >= -, max -`
- Restrictions: `-`
- Damage values: `[105, 125, 145, 165, 190]`
- Chance values: `[10, 10, 10, 10, 10]`
- Parry values: `[0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/dagger.html`

### 霸雨螫魂 / `rain throwing`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:dagger`
- Legacy prerequisite: `盤龍匕法(dragon dagger)`
- Legacy next: `-`
- Runtime file: `skill/r/rain_throwing.ski`
- Runtime slot: `SLOT_RAIN_THROWING`
- Runtime key: `rain_throwing`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `10 / 1`
- CostType / Weapon / Check: `COST_MOVE / WEAPON_DAGGER / check_dagger_attack`
- CanAsk / Teach / Valid / Enable: `No / No / No / Yes`
- Class limits: `伶 人 >= 五十級, max 出神入化﹗; 郎 中 >= 五十級, max 登峰造極﹗; 盜 賊 >= 五十級, max 一代宗師﹗; 刺 客 >= -, max -; 平 民 >= -, max -; 武 官 >= -, max -; 將 軍 >= -, max -; 天 師 >= -, max -; 文 官 >= -, max -; 道 士 >= -, max -; 鑄劍師 >= -, max -`
- Restrictions: `attrs: 敏捷 >= 二十五; skills: 盤龍匕法 >= 出類拔萃`
- Damage values: `[135, 155, 175, 195, 220, 250]`
- Chance values: `[10, 20, 20, 10, 10, 10]`
- Parry values: `[0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/dagger.html`

### 七奇炙針訣 / `seven dagger`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:dagger`
- Legacy prerequisite: `碧血十二針(be needle)`
- Legacy next: `-`
- Runtime file: `skill/s/seven_dagger.ski`
- Runtime slot: `SLOT_SEVEN_DAGGER`
- Runtime key: `seven_dagger`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `20 / 3`
- CostType / Weapon / Check: `COST_MOVE / WEAPON_DAGGER / check_dagger_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `伶 人 >= 一級, max 神乎其技﹗; 郎 中 >= 一級, max 神乎其技﹗; 天 師 >= 一級, max 神乎其技﹗; 鑄劍師 >= 一級, max 神乎其技﹗; 盜 賊 >= 一級, max 一代宗師﹗`
- Restrictions: `attrs: 敏捷 >= 十五; skills: 碧血十二針 >= 出類拔萃`
- Damage values: `[90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 195, 210, 230]`
- Chance values: `[20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/dagger.html`

