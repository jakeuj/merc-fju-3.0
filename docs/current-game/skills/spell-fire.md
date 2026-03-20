---
layout: default
title: Current Game 火系 Skills
---

# Current Game 法術技能 / 火系

這頁是 `docs/current-game/skills.json` 的 `法術技能 / 火系` 可讀版，將舊站鏈路、現行 runtime 與調整維度放在同一頁。

- Skills in this page: `7`
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
| legacy-page:fire | burning hands -> flamestrike -> fireball -> cast fire -> fire elf<br>stone skin -> faerie fire | 7 | legacy_catalog_seeded |

## Skill Cards

## legacy-page:fire

Legacy chain: `burning hands -> flamestrike -> fireball -> cast fire -> fire elf / stone skin -> faerie fire`

### 火焰之掌 / `burning hands`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:fire`
- Legacy prerequisite: `從缺`
- Legacy next: `flamestrike`
- Runtime file: `skill/b/burning_hands.ski`
- Runtime slot: `SLOT_BURNING_HANDS`
- Runtime key: `burning_hands`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `15 / 8`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `伶 人 >= 五十級, max 馬馬虎虎﹗; 刺 客 >= 五十級, max 初窺門徑﹗; 平 民 >= 十級, max 初窺門徑﹗; 郎 中 >= 五十級, max 馬馬虎虎﹗; 武 官 >= 十級, max 初窺門徑﹗; 將 軍 >= 五十級, max 初窺門徑﹗; 天 師 >= 五十級, max 一代宗師﹗; 文 官 >= 十級, max 馬馬虎虎﹗; 道 士 >= 十級, max 出類拔萃﹗; 鑄劍師 >= 五十級, max 登峰造極﹗; 盜 賊 >= 十五級, max 初窺門徑﹗`
- Restrictions: `-`
- Damage model: `code-driven`
- Code path: `src/spell.c:1079`
- Code damage summary: `base ladder: 0; formula: spell_damage(ch, level, TYPE_INT, SPELL_CLASS_ONE); attack mode: ATTACK_RANDOM`
- Damage values: `(not stored in .ski #Damage)`
- Chance / Parry / Innate: `(resolved in code path, not .ski arrays)`
- Legacy page source: `skill/fire.html`
- Notes: Code-driven offensive exception: damage logic currently lives in src/spell.c:1079.

### 三昧真火 / `cast fire`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:fire`
- Legacy prerequisite: `火球術(fireball)`
- Legacy next: `fire elf`
- Runtime file: `skill/c/cast_fire.ski`
- Runtime slot: `SLOT_CAST_FIRE`
- Runtime key: `cast_fire`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `35 / 17`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `天 師 >= 一級, max 一代宗師﹗; 道 士 >= 一級, max 心神領會﹗; 鑄劍師 >= 一級, max 登峰造極﹗`
- Restrictions: `attrs: 智力 >= 二十; skills: 火球術 >= 出類拔萃`
- Damage model: `code-driven`
- Code path: `src/spell.c:405`
- Code damage summary: `formula: spell_damage(ch, level, TYPE_INT, SPELL_CLASS_FOU)`
- Damage values: `(not stored in .ski #Damage)`
- Chance / Parry / Innate: `(resolved in code path, not .ski arrays)`
- Legacy page source: `skill/fire.html`
- Notes: Code-driven offensive exception: damage logic currently lives in src/spell.c:405.

### 精靈之火 / `faerie fire`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:fire`
- Legacy prerequisite: `皮膚石化術(stone skin)`
- Legacy next: `-`
- Runtime file: `skill/f/faerie_fire.ski`
- Runtime slot: `SLOT_FAERIE_FIRE`
- Runtime key: `faerie_fire`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `18 / 24`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `伶 人 >= 五十級, max 一代宗師﹗; 郎 中 >= 五十級, max 登峰造極﹗; 文 官 >= 十五級, max 心神領會﹗`
- Restrictions: `skills: 皮膚石化術 >= 心神領會`
- Damage model: `unresolved`
- Damage audit classification: `needs review`
- Code path: `src/spell.c:2367`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/fire.html`
- Notes: Needs review: damage logic currently lives in src/spell.c:2367.

### 火之精靈 / `fire elf`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:fire`
- Legacy prerequisite: `三昧真火(cast fire)`
- Legacy next: `-`
- Runtime file: `skill/f/fire_elf.ski`
- Runtime slot: `SLOT_FIRE_ELF`
- Runtime key: `fire_elf`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `50 / 25`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `No / No / Yes / No`
- Class limits: `天 師 >= 一級, max 一代宗師﹗`
- Restrictions: `attrs: 智力 >= 二十五; skills: 三昧真火 >= 神乎其技`
- Damage model: `code-driven`
- Code path: `src/ex_spell.c:49`
- Code damage summary: `formula: spell_damage(ch, level, TYPE_INT, SPELL_CLASS_FIV); attack mode: ATTACK_RANDOM`
- Damage values: `(not stored in .ski #Damage)`
- Chance / Parry / Innate: `(resolved in code path, not .ski arrays)`
- Legacy page source: `skill/fire.html`
- Notes: Code-driven offensive exception: damage logic currently lives in src/ex_spell.c:49.

### 火球術 / `fireball`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:fire`
- Legacy prerequisite: `烈焰術(flamestrike)`
- Legacy next: `cast fire`
- Runtime file: `skill/f/fireball.ski`
- Runtime slot: `SLOT_FIREBALL`
- Runtime key: `fireball`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `25 / 14`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `No / No / Yes / No`
- Class limits: `伶 人 >= 五十級, max 心神領會﹗; 郎 中 >= 五十級, max 心神領會﹗; 天 師 >= 五十級, max 一代宗師﹗; 文 官 >= 十級, max 心神領會﹗; 道 士 >= 十級, max 神乎其技﹗; 鑄劍師 >= 五十級, max 登峰造極﹗`
- Restrictions: `attrs: 智力 >= 十五; skills: 烈焰術 >= 心神領會`
- Damage model: `code-driven`
- Code path: `src/spell.c:2230`
- Code damage summary: `formula: spell_damage(ch, level, TYPE_INT, SPELL_CLASS_THR); attack mode: ATTACK_RANDOM`
- Damage values: `(not stored in .ski #Damage)`
- Chance / Parry / Innate: `(resolved in code path, not .ski arrays)`
- Legacy page source: `skill/fire.html`
- Notes: Code-driven offensive exception: damage logic currently lives in src/spell.c:2230.

### 烈焰術 / `flamestrike`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:fire`
- Legacy prerequisite: `火焰之掌(burning hands)`
- Legacy next: `fireball`
- Runtime file: `skill/f/flamestrike.ski`
- Runtime slot: `SLOT_FLAMESTRIKE`
- Runtime key: `flamestrike`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `20 / 12`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `伶 人 >= 五十級, max 心神領會﹗; 郎 中 >= 五十級, max 心神領會﹗; 天 師 >= 五十級, max 一代宗師﹗; 文 官 >= 十級, max 心神領會﹗; 道 士 >= 十級, max 神乎其技﹗; 鑄劍師 >= 五十級, max 登峰造極﹗`
- Restrictions: `attrs: 智力 >= 十; skills: 火焰之掌 >= 初窺門徑`
- Damage model: `code-driven`
- Code path: `src/spell.c:2299`
- Code damage summary: `formula: spell_damage(ch, level, TYPE_INT, SPELL_CLASS_TWO); attack mode: ATTACK_RANDOM`
- Damage values: `(not stored in .ski #Damage)`
- Chance / Parry / Innate: `(resolved in code path, not .ski arrays)`
- Legacy page source: `skill/fire.html`
- Notes: Code-driven offensive exception: damage logic currently lives in src/spell.c:2299.

### 皮膚石化術 / `stone skin`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:fire`
- Legacy prerequisite: `從缺`
- Legacy next: `faerie fire`
- Runtime file: `skill/s/stone_skin.ski`
- Runtime slot: `SLOT_STONE_SKIN`
- Runtime key: `stone_skin`
- Type: `TAR_CHAR_SELF`
- Cost / Wait: `12 / 18`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `伶 人 >= 五十級, max 一代宗師﹗; 郎 中 >= 五十級, max 登峰造極﹗; 文 官 >= 十五級, max 心神領會﹗`
- Restrictions: `-`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/fire.html`

