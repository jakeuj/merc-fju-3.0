---
layout: default
title: Current Game 雷系 Skills
---

# Current Game 法術技能 / 雷系

這頁是 `docs/current-game/skills.json` 的 `法術技能 / 雷系` 可讀版，將舊站鏈路、現行 runtime 與調整維度放在同一頁。

- Skills in this page: `6`
- Source JSON: [`skills.json`](../skills.json)
- Registry note: [`skills.md`](../skills.html)
- Index: [`skills-index.md`](../skills-index.html)

## Family Overview

| Family | Legacy Chain | Skills | Audit States |
| --- | --- | --- | --- |
| legacy-page:thunder | control weather -> haste<br>shocking grasp -> lightning bolt -> call lightning -> cast lightning | 6 | legacy_catalog_seeded |

## Skill Cards

## legacy-page:thunder

Legacy chain: `control weather -> haste / shocking grasp -> lightning bolt -> call lightning -> cast lightning`

### 呼叫天雷 / `call lightning`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:thunder`
- Legacy prerequisite: `小雷球(lightning bolt)`
- Legacy next: `cast lightning`
- Runtime file: `skill/c/call_lightning.ski`
- Runtime slot: `SLOT_CALL_LIGHTNING`
- Runtime key: `call_lightning`
- Type: `TAR_IGNORE`
- Cost / Wait: `22 / 15`
- CostType / Weapon / Check: `- / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `天 師 >= 三十五級, max 一代宗師﹗; 道 士 >= 三十五級, max 出類拔萃﹗; 鑄劍師 >= 三十五級, max 一代宗師﹗`
- Restrictions: `attrs: 智力 >= 十五; skills: 小雷球 >= 心神領會`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/thunder.html`

### 狂奔雷電 / `cast lightning`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:thunder`
- Legacy prerequisite: `呼叫天雷(call lightning)`
- Legacy next: `-`
- Runtime file: `skill/c/cast_lightning.ski`
- Runtime slot: `SLOT_CAST_LIGHTNING`
- Runtime key: `cast_lightning`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `28 / 20`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `天 師 >= 五十級, max 一代宗師﹗; 鑄劍師 >= 五十級, max 登峰造極﹗`
- Restrictions: `attrs: 智力 >= 二十; skills: 呼叫天雷 >= 出類拔萃`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/thunder.html`

### 控制天氣術 / `control weather`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:thunder`
- Legacy prerequisite: `從缺`
- Legacy next: `haste`
- Runtime file: `skill/c/control_weather.ski`
- Runtime slot: `SLOT_CONTROL_WEATHER`
- Runtime key: `control_weather`
- Type: `TAR_STRING`
- Cost / Wait: `25 / 12`
- CostType / Weapon / Check: `- / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `伶 人 >= 五十級, max 一代宗師﹗; 郎 中 >= 五十級, max 出類拔萃﹗; 天 師 >= 五十級, max 出類拔萃﹗; 文 官 >= 十級, max 心神領會﹗; 道 士 >= 十級, max 心神領會﹗; 鑄劍師 >= 五十級, max 出類拔萃﹗`
- Restrictions: `attrs: 智力 >= 五`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/thunder.html`

### 迅捷 / `haste`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:thunder`
- Legacy prerequisite: `控制天氣術(control weather)`
- Legacy next: `-`
- Runtime file: `skill/h/haste.ski`
- Runtime slot: `SLOT_HASTE`
- Runtime key: `haste`
- Type: `TAR_CHAR_DEFENSIVE`
- Cost / Wait: `40 / 25`
- CostType / Weapon / Check: `- / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `伶 人 >= 一級, max 一代宗師﹗; 郎 中 >= 一級, max 出神入化﹗`
- Restrictions: `attrs: 學識 >= 二十; skills: 控制天氣術 >= 心神領會`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/thunder.html`

### 小雷球 / `lightning bolt`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:thunder`
- Legacy prerequisite: `輕度電擊術(shocking grasp)`
- Legacy next: `call lightning`
- Runtime file: `skill/l/lightning_bolt.ski`
- Runtime slot: `SLOT_LIGHTNING_BOLT`
- Runtime key: `lightning_bolt`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `20 / 12`
- CostType / Weapon / Check: `- / - / -`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `伶 人 >= 五十級, max 馬馬虎虎﹗; 郎 中 >= 五十級, max 馬馬虎虎﹗; 天 師 >= 五十級, max 一代宗師﹗; 文 官 >= 十級, max 馬馬虎虎﹗; 道 士 >= 十級, max 出類拔萃﹗; 鑄劍師 >= 五十級, max 登峰造極﹗`
- Restrictions: `attrs: 智力 >= 十; skills: 輕度電擊術 >= 馬馬虎虎`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/thunder.html`

### 輕度電擊術 / `shocking grasp`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:thunder`
- Legacy prerequisite: `從缺`
- Legacy next: `lightning bolt`
- Runtime file: `skill/s/shocking_grasp.ski`
- Runtime slot: `SLOT_SHOCKING_GRASP`
- Runtime key: `shocking_grasp`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `15 / 8`
- CostType / Weapon / Check: `- / - / -`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `伶 人 >= 五十級, max 馬馬虎虎﹗; 刺 客 >= 五十級, max 初窺門徑﹗; 平 民 >= 十級, max 初窺門徑﹗; 郎 中 >= 五十級, max 馬馬虎虎﹗; 武 官 >= 十級, max 初窺門徑﹗; 將 軍 >= 五十級, max 初窺門徑﹗; 天 師 >= 五十級, max 一代宗師﹗; 文 官 >= 十級, max 馬馬虎虎﹗; 道 士 >= 十級, max 出類拔萃﹗; 鑄劍師 >= 五十級, max 登峰造極﹗; 盜 賊 >= 十五級, max 初窺門徑﹗`
- Restrictions: `attrs: 智力 >= 五`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/thunder.html`

