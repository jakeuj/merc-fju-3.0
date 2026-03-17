---
layout: default
title: Current Game 聖系 Skills
---

# Current Game 法術技能 / 聖系

這頁是 `docs/current-game/skills.json` 的 `法術技能 / 聖系` 可讀版，將舊站鏈路、現行 runtime 與調整維度放在同一頁。

- Skills in this page: `11`
- Source JSON: [`skills.json`](../skills.json)
- Registry note: [`skills.md`](../skills.html)
- Index: [`skills-index.md`](../skills-index.html)

## Family Overview

| Family | Legacy Chain | Skills | Audit States |
| --- | --- | --- | --- |
| legacy-page:holy | bless -> giant strength -> protection -> heal -> sanctuary<br>detect evil -> dispel evil -> remove curse -> harm -> power word | 11 | legacy_catalog_seeded |

## Skill Cards

## legacy-page:holy

Legacy chain: `bless -> giant strength -> protection -> heal -> sanctuary / detect evil -> dispel evil -> remove curse -> harm -> power word`

### 群仙祝福 / `bless`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:holy`
- Legacy prerequisite: `從缺`
- Legacy next: `giant strength`
- Runtime file: `skill/c/cast_bless.ski`
- Runtime slot: `SLOT_CAST_BLESS`
- Runtime key: `cast_bless`
- Type: `TAR_CHAR_DEFENSIVE`
- Cost / Wait: `15 / 10`
- CostType / Weapon / Check: `COST_MANA / - / -`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `-`
- Restrictions: `-`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/holy.html`

### 偵測邪惡 / `detect evil`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:holy`
- Legacy prerequisite: `從缺`
- Legacy next: `dispel evil`
- Runtime file: `skill/d/detect_evil.ski`
- Runtime slot: `SLOT_DETECT_EVIL`
- Runtime key: `detect_evil`
- Type: `SLOT_DETECT_EVIL`
- Cost / Wait: `5 / 12`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `伶 人 >= 一級, max 一代宗師﹗; 刺 客 >= 一級, max 馬馬虎虎﹗; 平 民 >= 一級, max 馬馬虎虎﹗; 郎 中 >= 一級, max 出神入化﹗; 武 官 >= 一級, max 馬馬虎虎﹗; 將 軍 >= 一級, max 馬馬虎虎﹗; 天 師 >= 一級, max 心神領會﹗; 文 官 >= 一級, max 出類拔萃﹗; 道 士 >= 一級, max 心神領會﹗; 鑄劍師 >= 一級, max 心神領會﹗; 盜 賊 >= 一級, max 馬馬虎虎﹗`
- Restrictions: `-`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/holy.html`

### 破除邪惡 / `dispel evil`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:holy`
- Legacy prerequisite: `偵測邪惡(detect evil)`
- Legacy next: `remove curse`
- Runtime file: `skill/d/dispel_evil.ski`
- Runtime slot: `SLOT_DISPEL_EVIL`
- Runtime key: `dispel_evil`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `15 / 12`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `伶 人 >= 一級, max 一代宗師﹗; 郎 中 >= 一級, max 出神入化﹗; 文 官 >= 一級, max 出類拔萃﹗`
- Restrictions: `skills: 偵測邪惡 >= 心神領會`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/holy.html`

### 巨人之力 / `giant strength`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:holy`
- Legacy prerequisite: `群仙祝福(bless)`
- Legacy next: `protection`
- Runtime file: `skill/g/giant_strength.ski`
- Runtime slot: `SLOT_GIANT_STRENGTH`
- Runtime key: `giant_strength`
- Type: `TAR_CHAR_DEFENSIVE`
- Cost / Wait: `20 / 15`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `伶 人 >= 一級, max 一代宗師﹗; 郎 中 >= 一級, max 出神入化﹗; 文 官 >= 一級, max 心神領會﹗`
- Restrictions: `skills: 群仙祝福 >= 心神領會`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/holy.html`

### 傷害術 / `harm`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:holy`
- Legacy prerequisite: `移除詛咒術(remove curse)`
- Legacy next: `power word`
- Runtime file: `skill/h/harm.ski`
- Runtime slot: `SLOT_HARM`
- Runtime key: `harm`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `35 / 15`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `伶 人 >= 一級, max 一代宗師﹗; 郎 中 >= 一級, max 出神入化﹗`
- Restrictions: `skills: 移除詛咒術 >= 神乎其技`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/holy.html`

### 恢復術 / `heal`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:holy`
- Legacy prerequisite: `「靈神訣」(protection)`
- Legacy next: `sanctuary`
- Runtime file: `skill/h/heal.ski`
- Runtime slot: `SLOT_HEAL`
- Runtime key: `heal`
- Type: `TAR_CHAR_DEFENSIVE`
- Cost / Wait: `50 / 20`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `伶 人 >= 一級, max 出神入化﹗; 郎 中 >= 一級, max 一代宗師﹗`
- Restrictions: `skills: 「靈神訣」 >= 出類拔萃`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/holy.html`

### 聖言 / `power word`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:holy`
- Legacy prerequisite: `傷害術(harm)`
- Legacy next: `-`
- Runtime file: `skill/p/power_word.ski`
- Runtime slot: `SLOT_POWER_WORD`
- Runtime key: `power_word`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `50 / 25`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `No / No / Yes / No`
- Class limits: `伶 人 >= 七十五級, max 一代宗師﹗`
- Restrictions: `attrs: 學識 >= 二十; skills: 傷害術 >= 出類拔萃`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/holy.html`

### 「靈神訣」 / `protection`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:holy`
- Legacy prerequisite: `巨人之力(giant strength)`
- Legacy next: `heal`
- Runtime file: `skill/p/protection.ski`
- Runtime slot: `SLOT_PROTECTION`
- Runtime key: `protection`
- Type: `SLOT_PROTECTION`
- Cost / Wait: `25 / 20`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `伶 人 >= 一級, max 一代宗師﹗; 郎 中 >= 一級, max 出神入化﹗`
- Restrictions: `skills: 巨人之力 >= 出類拔萃`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/holy.html`

### 妙手回春 / `remeday`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:holy`
- Legacy prerequisite: `治療藥物中毒(cure overdose)`
- Legacy next: `-`
- Runtime file: `skill/r/remeday.ski`
- Runtime slot: `SLOT_REMEDAY`
- Runtime key: `remeday`
- Type: `TAR_CHAR_DEFENSIVE`
- Cost / Wait: `200 / 60`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `伶 人 >= 一級, max 出類拔萃﹗; 郎 中 >= 一級, max 一代宗師﹗`
- Restrictions: `attrs: 學識 >= 二十五; skills: 治療藥物中毒 >= 神乎其技`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/holy.html`

### 移除詛咒術 / `remove curse`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:holy`
- Legacy prerequisite: `破除邪惡(dispel evil)`
- Legacy next: `harm`
- Runtime file: `skill/r/remove_curse.ski`
- Runtime slot: `SLOT_REMOVE_CURSE`
- Runtime key: `remove_curse`
- Type: `TAR_CHAR_DEFENSIVE`
- Cost / Wait: `20 / 15`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `伶 人 >= 一級, max 一代宗師﹗; 郎 中 >= 一級, max 出神入化﹗; 文 官 >= 一級, max 出類拔萃﹗`
- Restrictions: `skills: 破除邪惡 >= 心神領會`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/holy.html`

### 聖光術 / `sanctuary`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:holy`
- Legacy prerequisite: `恢復術(heal)`
- Legacy next: `-`
- Runtime file: `skill/s/sanctuary.ski`
- Runtime slot: `SLOT_SANCTUARY`
- Runtime key: `sanctuary`
- Type: `SLOT_SANCTUARY`
- Cost / Wait: `75 / 30`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `No / No / Yes / No`
- Class limits: `伶 人 >= 一級, max 一代宗師﹗; 郎 中 >= 一級, max 出神入化﹗`
- Restrictions: `skills: 恢復術 >= 出神入化`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/holy.html`

