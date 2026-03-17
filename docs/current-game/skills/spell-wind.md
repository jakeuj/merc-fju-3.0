---
layout: default
title: Current Game 風系 Skills
---

# Current Game 法術技能 / 風系

這頁是 `docs/current-game/skills.json` 的 `法術技能 / 風系` 可讀版，將舊站鏈路、現行 runtime 與調整維度放在同一頁。

- Skills in this page: `10`
- Source JSON: [`skills.json`](../skills.json)
- Registry note: [`skills.md`](../skills.html)
- Index: [`skills-index.md`](../skills-index.html)

## Family Overview

| Family | Legacy Chain | Skills | Audit States |
| --- | --- | --- | --- |
| legacy-page:wind | armor -> faerie fog -> shield<br>magic missile -> wind blade -> vacuum wind<br>refresh -> wakeup -> fly dance -> super refresh | 10 | legacy_catalog_seeded |

## Skill Cards

## legacy-page:wind

Legacy chain: `armor -> faerie fog -> shield / magic missile -> wind blade -> vacuum wind / refresh -> wakeup -> fly dance -> super refresh`

### 天神守護 / `armor`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:wind`
- Legacy prerequisite: `從缺`
- Legacy next: `faerie fog`
- Runtime file: `skill/c/cast_armor.ski`
- Runtime slot: `SLOT_CAST_ARMOR`
- Runtime key: `cast_armor`
- Type: `TAR_CHAR_DEFENSIVE`
- Cost / Wait: `12 / 15`
- CostType / Weapon / Check: `COST_MANA / - / -`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `伶 人 >= 一級, max 一代宗師﹗; 郎 中 >= 一級, max 出神入化﹗; 文 官 >= 一級, max 心神領會﹗`
- Restrictions: `-`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/wind.html`

### 精靈之霧 / `faerie fog`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:wind`
- Legacy prerequisite: `天神守護(armor)`
- Legacy next: `shield`
- Runtime file: `skill/f/faerie_fog.ski`
- Runtime slot: `SLOT_FAERIE_FOG`
- Runtime key: `faerie_fog`
- Type: `TAR_IGNORE`
- Cost / Wait: `15 / 18`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `No / No / Yes / No`
- Class limits: `伶 人 >= 一級, max 一代宗師﹗; 郎 中 >= 一級, max 出神入化﹗`
- Restrictions: `skills: 天神守護 >= 心神領會`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/wind.html`

### 飛翔術 / `fly dance`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:wind`
- Legacy prerequisite: `微風喚醒術(wakeup)`
- Legacy next: `super refresh`
- Runtime file: `skill/f/fly.ski`
- Runtime slot: `SLOT_FLY`
- Runtime key: `fly`
- Type: `SLOT_FLY`
- Cost / Wait: `15 / 20`
- CostType / Weapon / Check: `COST_MANA / - / -`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `伶 人 >= 十五級, max 出神入化﹗; 郎 中 >= 十五級, max 一代宗師﹗; 文 官 >= 十五級, max 出類拔萃﹗`
- Restrictions: `skills: 微風喚醒術 >= 心神領會`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/wind.html`

### 魔法飛彈 / `magic missile`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:wind`
- Legacy prerequisite: `從缺`
- Legacy next: `wind blade`
- Runtime file: `skill/m/magic_missile.ski`
- Runtime slot: `SLOT_MAGIC_MISSILE`
- Runtime key: `magic_missile`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `15 / 12`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `伶 人 >= 五十級, max 出類拔萃﹗; 刺 客 >= 五十級, max 出類拔萃﹗; 郎 中 >= 五十級, max 出類拔萃﹗; 武 官 >= 十級, max 馬馬虎虎﹗; 將 軍 >= 五十級, max 出類拔萃﹗; 天 師 >= 五十級, max 一代宗師﹗; 文 官 >= 十級, max 心神領會﹗; 道 士 >= 十級, max 出類拔萃﹗; 鑄劍師 >= 五十級, max 登峰造極﹗; 盜 賊 >= 十級, max 馬馬虎虎﹗`
- Restrictions: `attrs: 智力 >= 五`
- Damage model: `code-driven`
- Code path: `src/spell.c:2982`
- Code damage summary: `formula: spell_damage(ch, level, TYPE_INT, SPELL_CLASS_ONE); attack mode: ATTACK_RANDOM`
- Damage values: `(not stored in .ski #Damage)`
- Chance / Parry / Innate: `(resolved in code path, not .ski arrays)`
- Legacy page source: `skill/wind.html`
- Notes: Code-driven offensive exception: damage logic currently lives in src/spell.c:2982.

### 體力恢復術 / `refresh`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:wind`
- Legacy prerequisite: `從缺`
- Legacy next: `wakeup`
- Runtime file: `skill/r/refresh.ski`
- Runtime slot: `SLOT_REFRESH`
- Runtime key: `refresh`
- Type: `TAR_CHAR_DEFENSIVE`
- Cost / Wait: `12 / 18`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `伶 人 >= 十五級, max 出神入化﹗; 刺 客 >= 十五級, max 出類拔萃﹗; 郎 中 >= 十五級, max 一代宗師﹗; 武 官 >= 十五級, max 心神領會﹗; 將 軍 >= 十五級, max 出類拔萃﹗; 天 師 >= 十五級, max 神乎其技﹗; 文 官 >= 十五級, max 心神領會﹗; 道 士 >= 十五級, max 心神領會﹗; 鑄劍師 >= 十五級, max 神乎其技﹗; 盜 賊 >= 十五級, max 心神領會﹗`
- Restrictions: `-`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/wind.html`

### 護盾術 / `shield`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:wind`
- Legacy prerequisite: `精靈之霧(faerie fog)`
- Legacy next: `-`
- Runtime file: `skill/s/shield.ski`
- Runtime slot: `SLOT_SHIELD`
- Runtime key: `shield`
- Type: `TAR_CHAR_DEFENSIVE`
- Cost / Wait: `25 / 25`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `伶 人 >= 一級, max 一代宗師﹗; 郎 中 >= 一級, max 出神入化﹗`
- Restrictions: `attrs: 智力 >= 二十; skills: 精靈之霧 >= 出類拔萃`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/wind.html`

### 強力體力恢復術 / `super refresh`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:wind`
- Legacy prerequisite: `飛翔術(fly dance)`
- Legacy next: `-`
- Runtime file: `skill/s/super_refresh.ski`
- Runtime slot: `SLOT_SUPER_REFRESH`
- Runtime key: `super_refresh`
- Type: `TAR_CHAR_DEFENSIVE`
- Cost / Wait: `20 / 15`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `郎 中 >= 七十五級, max 一代宗師﹗`
- Restrictions: `attrs: 智力 >= 二十五; skills: 飛翔術 >= 出神入化`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/wind.html`

### 真空之風 / `vacuum wind`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:wind`
- Legacy prerequisite: `風之刃(wind blade)`
- Legacy next: `-`
- Runtime file: `skill/v/vacuum_wind.ski`
- Runtime slot: `SLOT_VACUUM_WIND`
- Runtime key: `vacuum_wind`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `30 / 15`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `天 師 >= 五十級, max 一代宗師﹗; 道 士 >= 十級, max 出類拔萃﹗; 鑄劍師 >= 五十級, max 登峰造極﹗`
- Restrictions: `attrs: 智力 >= 十五; skills: 風之刃 >= 心神領會`
- Damage model: `code-driven`
- Code path: `src/spell.c:3035`
- Code damage summary: `formula: spell_damage(ch, level, TYPE_INT, SPELL_CLASS_THR); attack mode: ATTACK_RANDOM`
- Damage values: `(not stored in .ski #Damage)`
- Chance / Parry / Innate: `(resolved in code path, not .ski arrays)`
- Legacy page source: `skill/wind.html`
- Notes: Code-driven offensive exception: damage logic currently lives in src/spell.c:3035.

### 微風喚醒術 / `wakeup`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:wind`
- Legacy prerequisite: `體力恢復術(refresh)`
- Legacy next: `fly dance`
- Runtime file: `skill/w/wakeup.ski`
- Runtime slot: `SLOT_WAKEUP`
- Runtime key: `wakeup`
- Type: `TAR_CHAR_DEFENSIVE`
- Cost / Wait: `12 / 20`
- CostType / Weapon / Check: `COST_MANA / - / -`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `伶 人 >= 十五級, max 出神入化﹗; 郎 中 >= 十五級, max 一代宗師﹗; 文 官 >= 十五級, max 心神領會﹗`
- Restrictions: `skills: 體力恢復術 >= 心神領會`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/wind.html`

### 風之刃 / `wind blade`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:wind`
- Legacy prerequisite: `魔法飛彈(magic missile)`
- Legacy next: `vacuum wind`
- Runtime file: `skill/w/wind_blade.ski`
- Runtime slot: `SLOT_WIND_BLADE`
- Runtime key: `wind_blade`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `15 / 15`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `伶 人 >= 五十級, max 出類拔萃﹗; 郎 中 >= 五十級, max 出類拔萃﹗; 天 師 >= 五十級, max 一代宗師﹗; 文 官 >= 十級, max 心神領會﹗; 道 士 >= 十級, max 出類拔萃﹗; 鑄劍師 >= 五十級, max 登峰造極﹗`
- Restrictions: `attrs: 智力 >= 十; skills: 魔法飛彈 >= 心神領會`
- Damage model: `code-driven`
- Code path: `src/spell.c:3007`
- Code damage summary: `formula: spell_damage(ch, level, TYPE_INT, SPELL_CLASS_TWO); attack mode: ATTACK_RANDOM`
- Damage values: `(not stored in .ski #Damage)`
- Chance / Parry / Innate: `(resolved in code path, not .ski arrays)`
- Legacy page source: `skill/wind.html`
- Notes: Code-driven offensive exception: damage logic currently lives in src/spell.c:3007.

