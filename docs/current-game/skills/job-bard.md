---
layout: default
title: Current Game 吟唱系 Skills
---

# Current Game 職業技能 / 吟唱系

這頁是 `docs/current-game/skills.json` 的 `職業技能 / 吟唱系` 可讀版，將舊站鏈路、現行 runtime 與調整維度放在同一頁。

- Skills in this page: `3`
- Source JSON: [`skills.json`](../skills.json)
- Registry note: [`skills.md`](../skills.html)
- Index: [`skills-index.md`](../skills-index.html)

## Family Overview

| Family | Legacy Chain | Skills | Audit States |
| --- | --- | --- | --- |
| legacy-page:bard | judge<br>locate object<br>pry | 3 | legacy_catalog_seeded |

## Skill Cards

## legacy-page:bard

Legacy chain: `judge / locate object / pry`

### 鑑賞技能術 / `judge`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:bard`
- Legacy prerequisite: `從缺`
- Legacy next: `-`
- Runtime file: `skill/j/judge.ski`
- Runtime slot: `SLOT_JUDGE`
- Runtime key: `judge`
- Type: `TAR_STRING`
- Cost / Wait: `22 / 20`
- CostType / Weapon / Check: `- / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `No / Yes / No / No`
- Class limits: `- >= -, max -; - >= -, max -; - >= -, max -`
- Restrictions: `-`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/bard.html`

### 偵測物品 / `locate object`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:bard`
- Legacy prerequisite: `從缺`
- Legacy next: `-`
- Runtime file: `skill/l/locate_object.ski`
- Runtime slot: `SLOT_LOCATE_OBJECT`
- Runtime key: `locate_object`
- Type: `TAR_STRING`
- Cost / Wait: `25 / 20`
- CostType / Weapon / Check: `- / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `- >= -, max -`
- Restrictions: `-`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/bard.html`

### 打聽技能 / `pry`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:bard`
- Legacy prerequisite: `從缺`
- Legacy next: `-`
- Runtime file: `skill/p/pry.ski`
- Runtime slot: `SLOT_PRY`
- Runtime key: `pry`
- Type: `TAR_STRING`
- Cost / Wait: `20 / 18`
- CostType / Weapon / Check: `- / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `No / Yes / No / No`
- Class limits: `- >= -, max -; - >= -, max -; - >= -, max -`
- Restrictions: `-`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/bard.html`

