---
layout: default
title: Current Game 毒系 Skills
---

# Current Game 法術技能 / 毒系

這頁是 `docs/current-game/skills.json` 的 `法術技能 / 毒系` 可讀版，將舊站鏈路、現行 runtime 與調整維度放在同一頁。

- Skills in this page: `6`
- Source JSON: [`skills.json`](../skills.json)
- Registry note: [`skills.md`](../skills.html)
- Index: [`skills-index.md`](../skills-index.html)

## Family Overview

| Family | Legacy Chain | Skills | Audit States |
| --- | --- | --- | --- |
| legacy-page:poison | acid blast -> blindness -> sleep -> poison<br>detect poison -> weaken | 6 | legacy_catalog_seeded |

## Skill Cards

## legacy-page:poison

Legacy chain: `acid blast -> blindness -> sleep -> poison / detect poison -> weaken`

### 酸液術 / `acid blast`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:poison`
- Legacy prerequisite: `從缺`
- Legacy next: `blindness`
- Runtime file: `skill/a/acid_blast.ski`
- Runtime slot: `SLOT_ACID_BLAST`
- Runtime key: `acid_blast`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `20 / 12`
- CostType / Weapon / Check: `COST_MANA / - / -`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `伶 人 >= 五十級, max 出類拔萃﹗; 郎 中 >= 五十級, max 出類拔萃﹗; 天 師 >= 五十級, max 一代宗師﹗; 文 官 >= 三十級, max 馬馬虎虎﹗; 道 士 >= 三十級, max 心神領會﹗; 鑄劍師 >= 五十級, max 登峰造極﹗`
- Restrictions: `-`
- Damage model: `code-driven`
- Code path: `src/spell.c:993`
- Code damage summary: `formula: spell_damage(ch, level, TYPE_INT, SPELL_CLASS_ONE); attack mode: ATTACK_RANDOM`
- Damage values: `(not stored in .ski #Damage)`
- Chance / Parry / Innate: `(resolved in code path, not .ski arrays)`
- Legacy page source: `skill/poison.html`
- Notes: Code-driven offensive exception: damage logic currently lives in src/spell.c:993.

### 眼盲術 / `blindness`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:poison`
- Legacy prerequisite: `酸液術(acid blast)`
- Legacy next: `sleep`
- Runtime file: `skill/b/blindness.ski`
- Runtime slot: `SLOT_BLINDNESS`
- Runtime key: `blindness`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `25 / 12`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `伶 人 >= 五十級, max 神乎其技﹗; 郎 中 >= 五十級, max 神乎其技﹗; 天 師 >= 五十級, max 出神入化﹗; 鑄劍師 >= 五十級, max 一代宗師﹗`
- Restrictions: `skills: 酸液術 >= 心神領會`
- Damage model: `unresolved`
- Damage audit classification: `needs review`
- Code path: `src/spell.c:1024`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/poison.html`
- Notes: Needs review: damage logic currently lives in src/spell.c:1024.

### 偵測毒物 / `detect poison`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:poison`
- Legacy prerequisite: `從缺`
- Legacy next: `weaken`
- Runtime file: `skill/d/detect_poison.ski`
- Runtime slot: `SLOT_DETECT_POISON`
- Runtime key: `detect_poison`
- Type: `TAR_OBJ_INV`
- Cost / Wait: `15 / 12`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `伶 人 >= 五十級, max 一代宗師﹗; 郎 中 >= 五十級, max 出神入化﹗; 文 官 >= 十級, max 出類拔萃﹗`
- Restrictions: `-`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/poison.html`

### 毒殺術 / `poison`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:poison`
- Legacy prerequisite: `睡眠術(sleep)`
- Legacy next: `-`
- Runtime file: `skill/p/poison.ski`
- Runtime slot: `SLOT_POISON`
- Runtime key: `poison`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `30 / 20`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `鑄劍師 >= 五十級, max 登峰造極﹗`
- Restrictions: `skills: 睡眠術 >= 出類拔萃`
- Damage model: `unresolved`
- Damage audit classification: `needs review`
- Code path: `src/spell.c:3195`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/poison.html`
- Notes: Needs review: damage logic currently lives in src/spell.c:3195.

### 睡眠術 / `sleep`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:poison`
- Legacy prerequisite: `眼盲術(blindness)`
- Legacy next: `poison`
- Runtime file: `skill/s/sleep.ski`
- Runtime slot: `SLOT_SLEEP`
- Runtime key: `sleep`
- Type: `TAR_CHAR_DEFENSIVE`
- Cost / Wait: `25 / 12`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `天 師 >= 五十級, max 登峰造極﹗; 鑄劍師 >= 五十級, max 一代宗師﹗`
- Restrictions: `skills: 眼盲術 >= 出類拔萃`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/poison.html`

### 虛弱術 / `weaken`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:poison`
- Legacy prerequisite: `偵測毒物(detect poison)`
- Legacy next: `-`
- Runtime file: `skill/w/weaken.ski`
- Runtime slot: `SLOT_WEAKEN`
- Runtime key: `weaken`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `20 / 15`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `伶 人 >= 五十級, max 一代宗師﹗; 郎 中 >= 五十級, max 出神入化﹗; 文 官 >= 十級, max 出類拔萃﹗`
- Restrictions: `attrs: 敏捷 >= 十; skills: 偵測毒物 >= 心神領會`
- Damage model: `unresolved`
- Damage audit classification: `needs review`
- Code path: `src/spell.c:3731`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/poison.html`
- Notes: Needs review: damage logic currently lives in src/spell.c:3731.

