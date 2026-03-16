---
layout: default
title: Current Game Step Skills
---

# Current Game Step Skills

這頁是 `docs/current-game/skills.json` 的 `步法` 可讀版，優先把舊站步法鏈與目前 runtime 狀態放在同一頁。

- Skills in this page: `15`
- Source JSON: [`skills.json`](../skills.json)
- Registry note: [`skills.md`](../skills.html)

## Family Overview

| Family | Legacy Chain | Skills | Audit States |
| --- | --- | --- | --- |
| legacy-step-cloud | cloud steps -> gdragon steps -> mirage steps | 3 | batch_b_prechecked, legacy_unreviewed |
| legacy-step-cloud-ghost | cloud ghost -> wind color steps | 2 | legacy_unreviewed |
| legacy-step-nine | nine steps -> color steps | 2 | legacy_unreviewed |
| legacy-step-shade | shade steps -> wind steps | 2 | legacy_unreviewed |
| legacy-step-sleev | sleev steps -> sky steps | 2 | batch_b_prechecked, legacy_unreviewed |
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
- Damage values: `[20, 20, 20, 20, 20, 20, 20]`
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
- Damage values: `[20, 20, 20, 20, 20, 20, 20]`
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
- Damage values: `[20, 20, 20, 20, 20, 20]`
- Chance values: `[20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/step.html`

### 風雲袖步 / `sleev steps`

- Audit: `legacy_unreviewed`
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
- Damage values: `[20, 20, 20, 20]`
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
- Damage values: `[20, 20, 20, 20, 20, 20]`
- Chance values: `[10, 10, 10, 10, 10, 10]`
- Parry values: `[0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/step.html`

