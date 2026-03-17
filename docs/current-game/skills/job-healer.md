---
layout: default
title: Current Game 醫療系 Skills
---

# Current Game 職業技能 / 醫療系

這頁是 `docs/current-game/skills.json` 的 `職業技能 / 醫療系` 可讀版，將舊站鏈路、現行 runtime 與調整維度放在同一頁。

- Skills in this page: `4`
- Source JSON: [`skills.json`](../skills.json)
- Registry note: [`skills.md`](../skills.html)
- Index: [`skills-index.md`](../skills-index.html)

## Family Overview

| Family | Legacy Chain | Skills | Audit States |
| --- | --- | --- | --- |
| legacy-page:doctor | anti physique<br>cure overdose -> remeday<br>deva shield<br>physique | 4 | legacy_catalog_seeded |

## Skill Cards

## legacy-page:doctor

Legacy chain: `anti physique / cure overdose -> remeday / deva shield / physique`

### 經脈逆行 / `anti physique`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:doctor`
- Legacy prerequisite: `從缺`
- Legacy next: `-`
- Runtime file: `skill/a/anti_physique.ski`
- Runtime slot: `SLOT_ANTI_PHYSIQUE`
- Runtime key: `anti_physique`
- Type: `TAR_MEDITATION`
- Cost / Wait: `1 / 1`
- CostType / Weapon / Check: `COST_MANA / - / -`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `刺 客 >= 五十級, max 出神入化﹗; 武 官 >= 十級, max 馬馬虎虎﹗; 將 軍 >= 五十級, max 一代宗師﹗`
- Restrictions: `attrs: 體格 >= 二十, 敏捷 >= 十五, 學識 >= 十五`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/doctor.html`

### 治療藥物中毒 / `cure overdose`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:doctor`
- Legacy prerequisite: `從缺`
- Legacy next: `remeday`
- Runtime file: `skill/c/cure_overdose.ski`
- Runtime slot: `SLOT_CURE_OVERDOSE`
- Runtime key: `cure_overdose`
- Type: `TAR_CHAR_DEFENSIVE`
- Cost / Wait: `10 / 12`
- CostType / Weapon / Check: `COST_MANA / - / -`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `伶 人 >= 一級, max 神乎其技﹗; 郎 中 >= 一級, max 登峰造極﹗; 文 官 >= 一級, max 出類拔萃﹗`
- Restrictions: `attrs: 學識 >= 十`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/doctor.html`

### 金剛護體 / `deva shield`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:doctor`
- Legacy prerequisite: `從缺`
- Legacy next: `-`
- Runtime file: `skill/d/deva_shield.ski`
- Runtime slot: `SLOT_DEVA_SHIELD`
- Runtime key: `deva_shield`
- Type: `TAR_CHAR_DEFENSIVE`
- Cost / Wait: `70 / 25`
- CostType / Weapon / Check: `COST_MOVE / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `伶 人 >= 七十五級, max 出神入化﹗; 郎 中 >= 七十五級, max 一代宗師﹗; 鑄劍師 >= 七十五級, max 出神入化﹗`
- Restrictions: `attrs: 智力 >= 二十五, 學識 >= 二十五`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/doctor.html`

### 易筋經 / `physique`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:doctor`
- Legacy prerequisite: `從缺`
- Legacy next: `-`
- Runtime file: `skill/p/physique.ski`
- Runtime slot: `SLOT_PHYSIQUE`
- Runtime key: `physique`
- Type: `TAR_MEDITATION`
- Cost / Wait: `1 / 1`
- CostType / Weapon / Check: `COST_MANA / - / -`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `伶 人 >= 五十級, max 出類拔萃﹗; 郎 中 >= 五十級, max 出類拔萃﹗; 文 官 >= 十級, max 馬馬虎虎﹗`
- Restrictions: `attrs: 體格 >= 十五, 敏捷 >= 二十, 學識 >= 十五`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/doctor.html`

