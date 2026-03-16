---
layout: default
title: Current Game 鑄造系 Skills
---

# Current Game 職業技能 / 鑄造系

這頁是 `docs/current-game/skills.json` 的 `職業技能 / 鑄造系` 可讀版，將舊站鏈路、現行 runtime 與調整維度放在同一頁。

- Skills in this page: `6`
- Source JSON: [`skills.json`](../skills.json)
- Registry note: [`skills.md`](../skills.html)
- Index: [`skills-index.md`](../skills-index.html)

## Family Overview

| Family | Legacy Chain | Skills | Audit States |
| --- | --- | --- | --- |
| legacy-page:smith | enchant weapon -> identify -> make sword<br>mint<br>repair -> develop | 6 | legacy_catalog_seeded |

## Skill Cards

## legacy-page:smith

Legacy chain: `enchant weapon -> identify -> make sword / mint / repair -> develop`

### 強化武器 / `develop`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:smith`
- Legacy prerequisite: `修理術(repair)`
- Legacy next: `-`
- Runtime file: `skill/d/develop.ski`
- Runtime slot: `SLOT_DEVELOP`
- Runtime key: `develop`
- Type: `TAR_OBJ_INV`
- Cost / Wait: `50 / 25`
- CostType / Weapon / Check: `- / - / -`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `鑄劍師 >= 一級, max 一代宗師﹗`
- Restrictions: `attrs: 力量 >= 十五, 學識 >= 二十`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/smith.html`

### 加強武器威力 / `enchant weapon`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:smith`
- Legacy prerequisite: `從缺`
- Legacy next: `identify`
- Runtime file: `skill/e/enchant_weapon.ski`
- Runtime slot: `SLOT_ENCHANT_WEAPON`
- Runtime key: `enchant_weapon`
- Type: `TAR_OBJ_INV`
- Cost / Wait: `50 / 24`
- CostType / Weapon / Check: `- / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `天 師 >= 一級, max 馬馬虎虎﹗; 道 士 >= 一級, max 初窺門徑﹗; 鑄劍師 >= 一級, max 一代宗師﹗`
- Restrictions: `-`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/smith.html`

### 鑑定術 / `identify`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:smith`
- Legacy prerequisite: `加強武器威力(enchant weapon)`
- Legacy next: `make sword`
- Runtime file: `skill/i/identify.ski`
- Runtime slot: `SLOT_IDENTIFY`
- Runtime key: `identify`
- Type: `TAR_OBJ_INV`
- Cost / Wait: `15 / 24`
- CostType / Weapon / Check: `- / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `鑄劍師 >= 一級, max 一代宗師﹗`
- Restrictions: `attrs: 智力 >= 十五; skills: 加強武器威力 >= 心神領會`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/smith.html`

### 魔法劍 / `make sword`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:smith`
- Legacy prerequisite: `鑑定術(identify)`
- Legacy next: `-`
- Runtime file: `skill/m/make_sword.ski`
- Runtime slot: `SLOT_MAKE_SWORD`
- Runtime key: `make_sword`
- Type: `TAR_CHAR_DEFENSIVE`
- Cost / Wait: `100 / 10`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `鑄劍師 >= 一級, max 一代宗師﹗`
- Restrictions: `attrs: 智力 >= 二十五; skills: 鑑定術 >= 出神入化`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/smith.html`

### 鑄造術 / `mint`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:smith`
- Legacy prerequisite: `從缺`
- Legacy next: `-`
- Runtime file: `skill/m/mint.ski`
- Runtime slot: `SLOT_MINT`
- Runtime key: `mint`
- Type: `TAR_OBJ_INV`
- Cost / Wait: `30 / 24`
- CostType / Weapon / Check: `- / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `鑄劍師 >= 一級, max 一代宗師﹗`
- Restrictions: `attrs: 力量 >= 十, 學識 >= 八`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/smith.html`

### 修理術 / `repair`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:smith`
- Legacy prerequisite: `從缺`
- Legacy next: `develop`
- Runtime file: `skill/r/repair.ski`
- Runtime slot: `SLOT_REPAIR`
- Runtime key: `repair`
- Type: `TAR_OBJ_INV`
- Cost / Wait: `30 / 24`
- CostType / Weapon / Check: `- / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `鑄劍師 >= 一級, max 一代宗師﹗`
- Restrictions: `attrs: 力量 >= 十, 學識 >= 十`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/smith.html`

