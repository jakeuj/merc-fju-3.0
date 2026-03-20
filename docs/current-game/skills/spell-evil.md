---
layout: default
title: Current Game 邪系 Skills
---

# Current Game 法術技能 / 邪系

這頁是 `docs/current-game/skills.json` 的 `法術技能 / 邪系` 可讀版，將舊站鏈路、現行 runtime 與調整維度放在同一頁。

- Skills in this page: `4`
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
| legacy-page:evil | curse -> gate -> evil power -> charm person | 4 | legacy_catalog_seeded |

## Skill Cards

## legacy-page:evil

Legacy chain: `curse -> gate -> evil power -> charm person`

### 迷惑術 / `charm person`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:evil`
- Legacy prerequisite: `邪惡魔力(evil power)`
- Legacy next: `-`
- Runtime file: `skill/c/charm_person.ski`
- Runtime slot: `SLOT_CHARM_PERSON`
- Runtime key: `charm_person`
- Type: `TAR_CHAR_DEFENSIVE`
- Cost / Wait: `120 / 25`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `鑄劍師 >= 六十五級, max 登峰造極﹗`
- Restrictions: `attrs: 學識 >= 二十五; skills: 邪惡魔力 >= 出類拔粹`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/evil.html`

### 詛咒術 / `curse`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:evil`
- Legacy prerequisite: `從缺`
- Legacy next: `gate`
- Runtime file: `skill/c/curse.ski`
- Runtime slot: `SLOT_CURSE`
- Runtime key: `curse`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `20 / 12`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `伶 人 >= 五十級, max 一代宗師﹗; 郎 中 >= 五十級, max 神乎其技﹗; 天 師 >= 五十級, max 神乎其技﹗; 文 官 >= 十級, max 心神領會﹗; 道 士 >= 十級, max 心神領會﹗; 鑄劍師 >= 五十級, max 出神入化﹗`
- Restrictions: `-`
- Damage model: `unresolved`
- Damage audit classification: `needs review`
- Code path: `src/spell.c:1825`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/evil.html`
- Notes: Needs review: damage logic currently lives in src/spell.c:1825.

### 邪惡魔力 / `evil power`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:evil`
- Legacy prerequisite: `魔界之門(gate)`
- Legacy next: `charm person`
- Runtime file: `skill/e/evil_power.ski`
- Runtime slot: `SLOT_EVIL_POWER`
- Runtime key: `evil_power`
- Type: `TAR_CHAR_SELF`
- Cost / Wait: `35 / 20`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `天 師 >= 五十級, max 一代宗師﹗; 道 士 >= 十級, max 出類拔萃﹗; 鑄劍師 >= 五十級, max 登峰造極﹗`
- Restrictions: `skills: 魔界之門 >= 心神領會`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/evil.html`

### 魔界之門 / `gate`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:evil`
- Legacy prerequisite: `詛咒術(curse)`
- Legacy next: `evil power`
- Runtime file: `skill/g/gate.ski`
- Runtime slot: `SLOT_GATE`
- Runtime key: `gate`
- Type: `TAR_STRING`
- Cost / Wait: `55 / 20`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `天 師 >= 五十級, max 神乎其技﹗; 道 士 >= 十級, max 出類拔萃﹗; 鑄劍師 >= 五十級, max 出神入化﹗`
- Restrictions: `skills: 詛咒術 >= 心神領會`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/evil.html`

