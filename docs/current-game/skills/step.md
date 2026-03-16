---
layout: default
title: Current Game 步法 Skills
---

# Current Game 其他技能 / 步法

這頁是 `docs/current-game/skills.json` 的 `其他技能 / 步法` 可讀版，將舊站鏈路、現行 runtime 與調整維度放在同一頁。

- Skills in this page: `15`
- Source JSON: [`skills.json`](../skills.json)
- Registry note: [`skills.md`](../skills.html)
- Index: [`skills-index.md`](../skills-index.html)

## Family Overview

| Family | Legacy Chain | Skills | Audit States |
| --- | --- | --- | --- |
| legacy-step-cloud | cloud steps -> gdragon steps -> mirage steps | 3 | batch_b_prechecked, legacy_unreviewed |
| legacy-step-cloud-ghost | cloud ghost -> wind color steps | 2 | legacy_unreviewed |
| legacy-step-nine | nine steps -> color steps | 2 | legacy_unreviewed |
| legacy-step-shade | shade steps -> wind steps | 2 | legacy_unreviewed |
| legacy-step-sleev | sleev steps -> sky steps | 2 | batch_b_prechecked |
| legacy-step-standalone | eight steps<br>free steps<br>hundred steps<br>night steps | 4 | legacy_unreviewed |

## Skill Cards

## legacy-step-cloud

Legacy chain: `cloud steps -> gdragon steps -> mirage steps`

### 翦雲步 / `cloud steps`

- Audit: `batch_b_prechecked`
- Family: `legacy-step-cloud`
- Legacy prerequisite: `從缺`
- Legacy next: `gdragon steps`
- Runtime file: `skill/c/cloud_steps.ski`
- Runtime slot: `SLOT_CLOUD_STEPS`
- Runtime key: `cloud_steps`
- Type: `TAR_DODGE`
- Cost / Wait: `5 / 1`
- CostType / Weapon / Check: `COST_MOVE / - / -`
- CanAsk / Teach / Valid / Enable: `Yes / Yes / Yes / Yes`
- Class limits: `伶 人 >= 一級, max 心神領會﹗; 刺 客 >= 一級, max 登峰造極﹗; 平 民 >= 一級, max 馬馬虎虎﹗; 郎 中 >= 一級, max 心神領會﹗; 武 官 >= 一級, max 出類拔萃﹗; 將 軍 >= 一級, max 登峰造極﹗; 天 師 >= 一級, max 出類拔萃﹗; 文 官 >= 一級, max 馬馬虎虎﹗; 道 士 >= 一級, max 心神領會﹗; 鑄劍師 >= 一級, max 出類拔萃﹗; 盜 賊 >= 一級, max 一代宗師﹗`
- Restrictions: `-`
- Damage values: `[35, 45, 55, 65, 75, 85, 95]`
- Chance values: `[10, 10, 10, 10, 10, 10, 10]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/step.html`

### 青玄身法 / `gdragon steps`

- Audit: `batch_b_prechecked`
- Family: `legacy-step-cloud`
- Legacy prerequisite: `翦雲步(cloud steps)`
- Legacy next: `mirage steps`
- Runtime file: `skill/g/gdragon_steps.ski`
- Runtime slot: `SLOT_GDRAGON_STEPS`
- Runtime key: `gdragon_steps`
- Type: `TAR_DODGE`
- Cost / Wait: `15 / 10`
- CostType / Weapon / Check: `COST_MOVE / - / -`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `刺 客 >= 五十級, max 登峰造極﹗; 武 官 >= 三十級, max 出類拔萃﹗; 將 軍 >= 五十級, max 登峰造極﹗; 天 師 >= 五十級, max 出類拔萃﹗; 鑄劍師 >= 五十級, max 出類拔萃﹗; 盜 賊 >= 三十級, max 出神入化﹗`
- Restrictions: `skills: 翦雲步 >= 出類拔萃`
- Damage values: `[80, 95, 110, 125, 140, 155, 170]`
- Chance values: `[20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/step.html`

### 離影迷蹤步 / `mirage steps`

- Audit: `legacy_unreviewed`
- Family: `legacy-step-cloud`
- Legacy prerequisite: `青玄身法(gdragon steps)`
- Legacy next: `-`
- Runtime file: `skill/m/mirage_steps.ski`
- Runtime slot: `SLOT_MIRAGE_STEPS`
- Runtime key: `mirage_steps`
- Type: `TAR_DODGE`
- Cost / Wait: `15 / 10`
- CostType / Weapon / Check: `COST_MOVE / - / -`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `刺 客 >= 五十級, max 一代宗師﹗; 將 軍 >= 五十級, max 登峰造極﹗`
- Restrictions: `attrs: 敏捷 >= 十五; skills: 青玄身法 >= 登峰造極; classes: 刺 客/將 軍`
- Damage values: `[20, 20, 20, 20, 20, 20, 20]`
- Chance values: `[10, 10, 10, 10, 10, 10, 10]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/step.html`

## legacy-step-cloud-ghost

Legacy chain: `cloud ghost -> wind color steps`

### 雲蹤魅影 / `cloud ghost`

- Audit: `legacy_unreviewed`
- Family: `legacy-step-cloud-ghost`
- Legacy prerequisite: `從缺`
- Legacy next: `wind color steps`
- Runtime file: `skill/c/cloud_ghost.ski`
- Runtime slot: `SLOT_CLOUD_GHOST`
- Runtime key: `cloud_ghost`
- Type: `TAR_DODGE`
- Cost / Wait: `15 / 10`
- CostType / Weapon / Check: `COST_MOVE / - / -`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `伶 人 >= 一級, max 一代宗師﹗; 郎 中 >= 一級, max 一代宗師﹗; 天 師 >= 一級, max 一代宗師﹗; 文 官 >= 一級, max 出類拔萃﹗; 道 士 >= 一級, max 出類拔萃﹗; 鑄劍師 >= 一級, max 一代宗師﹗`
- Restrictions: `-`
- Damage values: `[20, 20, 20, 20, 20, 20]`
- Chance values: `[10, 10, 10, 10, 10, 10]`
- Parry values: `[0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/step.html`

### 破風彩雲步 / `wind color steps`

- Audit: `legacy_unreviewed`
- Family: `legacy-step-cloud-ghost`
- Legacy prerequisite: `雲蹤魅影(cloud ghost)`
- Legacy next: `-`
- Runtime file: `skill/w/windcolor_steps.ski`
- Runtime slot: `SLOT_WINDCOLOR_STEPS`
- Runtime key: `windcolor_steps`
- Type: `TAR_DODGE`
- Cost / Wait: `15 / 10`
- CostType / Weapon / Check: `COST_MOVE / - / -`
- CanAsk / Teach / Valid / Enable: `No / No / Yes / Yes`
- Class limits: `伶 人 >= 一級, max 登峰造極﹗; 郎 中 >= 一級, max 登峰造極﹗; 天 師 >= 一級, max 登峰造極﹗; 文 官 >= 一級, max 出類拔萃﹗; 道 士 >= 一級, max 出類拔萃﹗; 鑄劍師 >= 一級, max 一代宗師﹗`
- Restrictions: `attrs: 學識 >= 二十; skills: 雲蹤魅影 >= 出類拔萃`
- Damage values: `[20, 20, 20, 20, 20, 20]`
- Chance values: `[20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/step.html`

## legacy-step-nine

Legacy chain: `nine steps -> color steps`

### 七彩幻步 / `color steps`

- Audit: `legacy_unreviewed`
- Family: `legacy-step-nine`
- Legacy prerequisite: `九天靈影步(nine steps)`
- Legacy next: `-`
- Runtime file: `skill/c/color_steps.ski`
- Runtime slot: `SLOT_COLOR_STEPS`
- Runtime key: `color_steps`
- Type: `TAR_DODGE`
- Cost / Wait: `10 / 5`
- CostType / Weapon / Check: `COST_MOVE / - / -`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `天 師 >= 一級, max 登峰造極﹗; 鑄劍師 >= 一級, max 登峰造極﹗`
- Restrictions: `attrs: 敏捷 >= 十五; skills: 九天靈影步 >= 出類拔萃; classes: 天 師/鑄劍師`
- Damage values: `[20, 20, 20, 20, 20, 20, 20]`
- Chance values: `[10, 10, 10, 10, 10, 10, 10]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/step.html`

### 九天靈影步 / `nine steps`

- Audit: `legacy_unreviewed`
- Family: `legacy-step-nine`
- Legacy prerequisite: `從缺`
- Legacy next: `color steps`
- Runtime file: `skill/n/nine_step.ski`
- Runtime slot: `SLOT_NINE_STEP`
- Runtime key: `nine_step`
- Type: `TAR_DODGE`
- Cost / Wait: `5 / 1`
- CostType / Weapon / Check: `COST_MOVE / - / -`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `天 師 >= 一級, max 出神入化﹗; 道 士 >= 一級, max 心神領會﹗; 鑄劍師 >= 一級, max 登峰造極﹗`
- Restrictions: `-`
- Damage values: `[20, 20, 20, 100, 20, 20, 20, 20, 20]`
- Chance values: `[10, 10, 10, 10, 10, 10, 10, 10]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/step.html`

## legacy-step-shade

Legacy chain: `shade steps -> wind steps`

### 換星步 / `shade steps`

- Audit: `legacy_unreviewed`
- Family: `legacy-step-shade`
- Legacy prerequisite: `從缺`
- Legacy next: `wind steps`
- Runtime file: `skill/s/shade_steps.ski`
- Runtime slot: `SLOT_SHADE_STEPS`
- Runtime key: `shade_steps`
- Type: `TAR_DODGE`
- Cost / Wait: `15 / 10`
- CostType / Weapon / Check: `COST_MOVE / - / -`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `伶 人 >= 一級, max 心神領會﹗; 刺 客 >= 一級, max 心神領會﹗; 郎 中 >= 一級, max 心神領會﹗; 武 官 >= 一級, max 馬馬虎虎﹗; 將 軍 >= 一級, max 心神領會﹗; 天 師 >= 一級, max 心神領會﹗; 文 官 >= 一級, max 馬馬虎虎﹗; 道 士 >= 一級, max 馬馬虎虎﹗; 鑄劍師 >= 一級, max 心神領會﹗; 盜 賊 >= 一級, max 登峰造極﹗`
- Restrictions: `-`
- Damage values: `[20, 20, 20, 20, 20, 20, 20]`
- Chance values: `[20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/step.html`

### 風影藏 / `wind steps`

- Audit: `legacy_unreviewed`
- Family: `legacy-step-shade`
- Legacy prerequisite: `換星步(shade steps)`
- Legacy next: `-`
- Runtime file: `skill/w/wind_steps.ski`
- Runtime slot: `SLOT_WIND_STEPS`
- Runtime key: `wind_steps`
- Type: `TAR_DODGE`
- Cost / Wait: `15 / 10`
- CostType / Weapon / Check: `COST_MOVE / - / -`
- CanAsk / Teach / Valid / Enable: `No / No / Yes / Yes`
- Class limits: `盜 賊 >= 一級, max 一代宗師﹗`
- Restrictions: `attrs: 敏捷 >= 二十; skills: 換星步 >= 出類拔萃; classes: 盜 賊`
- Damage values: `[20, 20, 20, 20, 20, 20, 20, 20]`
- Chance values: `[20, 20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/step.html`

## legacy-step-sleev

Legacy chain: `sleev steps -> sky steps`

### 俠客天雲身法 / `sky steps`

- Audit: `batch_b_prechecked`
- Family: `legacy-step-sleev`
- Legacy prerequisite: `風雲袖步(sleev steps)`
- Legacy next: `-`
- Runtime file: `skill/s/sky_steps.ski`
- Runtime slot: `SLOT_SKY_STEPS`
- Runtime key: `sky_steps`
- Type: `TAR_DODGE`
- Cost / Wait: `10 / 10`
- CostType / Weapon / Check: `COST_MOVE / - / -`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `刺 客 >= 一級, max 一代宗師﹗; 將 軍 >= 一級, max 神乎其技﹗`
- Restrictions: `attrs: 力量 >= 二十, 敏捷 >= 二十五; skills: 風雲袖步 >= 出類拔萃; classes: 刺 客/將 軍`
- Damage values: `[95, 115, 135, 155, 175, 195]`
- Chance values: `[20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/step.html`

### 風雲袖步 / `sleev steps`

- Audit: `batch_b_prechecked`
- Family: `legacy-step-sleev`
- Legacy prerequisite: `從缺`
- Legacy next: `sky steps`
- Runtime file: `skill/s/sleev_steps.ski`
- Runtime slot: `SLOT_SLEEV_STEPS`
- Runtime key: `sleev_steps`
- Type: `TAR_DODGE`
- Cost / Wait: `10 / 10`
- CostType / Weapon / Check: `COST_MOVE / - / -`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `伶 人 >= 一級, max 馬馬虎虎﹗; 刺 客 >= 一級, max 登峰造極﹗; 郎 中 >= 一級, max 馬馬虎虎﹗; 武 官 >= 一級, max 馬馬虎虎﹗; 將 軍 >= 一級, max 登峰造極﹗; 天 師 >= 一級, max 心神領會﹗; 文 官 >= 一級, max 粗通皮毛﹗; 道 士 >= 一級, max 初窺門徑﹗; 鑄劍師 >= 一級, max 心神領會﹗; 盜 賊 >= 一級, max 心神領會﹗`
- Restrictions: `-`
- Damage values: `[60, 80, 100, 120]`
- Chance values: `[20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/step.html`

## legacy-step-standalone

Legacy chain: `eight steps / free steps / hundred steps / night steps`

### 醉八仙 / `eight steps`

- Audit: `legacy_unreviewed`
- Family: `legacy-step-standalone`
- Legacy prerequisite: `從缺`
- Legacy next: `-`
- Runtime file: `skill/e/eight_steps.ski`
- Runtime slot: `SLOT_EIGHT_STEPS`
- Runtime key: `eight_steps`
- Type: `TAR_DODGE`
- Cost / Wait: `20 / 1`
- CostType / Weapon / Check: `COST_MOVE / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `No / No / No / Yes`
- Class limits: `伶 人 >= 五十級, max 一代宗師﹗; 郎 中 >= 五十級, max 一代宗師﹗; 天 師 >= 五十級, max 一代宗師﹗; 鑄劍師 >= 五十級, max 一代宗師﹗; 刺 客 >= -, max -; 平 民 >= -, max -; 武 官 >= -, max -; 將 軍 >= -, max -; 文 官 >= -, max -; 道 士 >= -, max -; 盜 賊 >= -, max -`
- Restrictions: `attrs: 敏捷 >= 二十, 學識 >= 二十三, 智力 >= 二十五; classes: 伶 人/郎 中/天 師/鑄劍師`
- Damage values: `[20, 20, 20, 20, 20, 20, 20, 20]`
- Chance values: `[10, 10, 10, 10, 10, 10, 10, 10]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/step.html`

### 逍遙遊 / `free steps`

- Audit: `legacy_unreviewed`
- Family: `legacy-step-standalone`
- Legacy prerequisite: `從缺`
- Legacy next: `-`
- Runtime file: `skill/f/free_steps.ski`
- Runtime slot: `SLOT_FREE_STEPS`
- Runtime key: `free_steps`
- Type: `TAR_DODGE`
- Cost / Wait: `10 / 10`
- CostType / Weapon / Check: `COST_MOVE / - / -`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `刺 客 >= 八十級, max 一代宗師﹗; 郎 中 >= 八十級, max 出神入化﹗`
- Restrictions: `attrs: 力量 >= 二十五, 敏捷 >= 三十; classes: 刺 客/平 民/武 官`
- Damage values: `[20, 20, 20, 20, 20, 20, 20, 20, 20]`
- Chance values: `[20, 20, 20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/step.html`

### 百幻身法 / `hundred steps`

- Audit: `legacy_unreviewed`
- Family: `legacy-step-standalone`
- Legacy prerequisite: `從缺`
- Legacy next: `-`
- Runtime file: `skill/h/hundred_steps.ski`
- Runtime slot: `SLOT_HUNDRED_STEPS`
- Runtime key: `hundred_steps`
- Type: `TAR_DODGE`
- Cost / Wait: `15 / 10`
- CostType / Weapon / Check: `COST_MOVE / - / -`
- CanAsk / Teach / Valid / Enable: `No / No / No / Yes`
- Class limits: `伶 人 >= 八十級, max 一代宗師﹗; 郎 中 >= 八十級, max 一代宗師﹗; 刺 客 >= -, max -; 平 民 >= -, max -; 武 官 >= -, max -; 將 軍 >= -, max -; 天 師 >= -, max -; 文 官 >= -, max -; 道 士 >= -, max -; 鑄劍師 >= -, max -; 盜 賊 >= -, max -`
- Restrictions: `attrs: 敏捷 >= 二十五, 學識 >= 三十, 智力 >= 三十; skills: 百鬼夜行步 >= 出神入化; classes: 伶 人/郎 中`
- Damage values: `[20, 20, 20, 20, 20, 20, 20, 20]`
- Chance values: `[10, 10, 10, 10, 10, 10, 10, 10]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/step.html`

### 百鬼夜行步 / `night steps`

- Audit: `legacy_unreviewed`
- Family: `legacy-step-standalone`
- Legacy prerequisite: `從缺`
- Legacy next: `-`
- Runtime file: `skill/n/night_steps.ski`
- Runtime slot: `SLOT_NIGHT_STEPS`
- Runtime key: `night_steps`
- Type: `TAR_DODGE`
- Cost / Wait: `15 / 10`
- CostType / Weapon / Check: `COST_MOVE / - / -`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `伶 人 >= 七十級, max 一代宗師﹗; 郎 中 >= 七十級, max 一代宗師﹗; 天 師 >= 七十級, max 登峰造極﹗; 鑄劍師 >= 七十級, max 登峰造極﹗`
- Restrictions: `attrs: 敏捷 >= 二十五, 學識 >= 三十, 智力 >= 三十; classes: 伶 人/郎 中/天 師/鑄劍師`
- Damage values: `[20, 20, 20, 20, 20, 20]`
- Chance values: `[10, 10, 10, 10, 10, 10]`
- Parry values: `[0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/step.html`

