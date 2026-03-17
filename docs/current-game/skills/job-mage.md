---
layout: default
title: Current Game 法師系 Skills
---

# Current Game 職業技能 / 法師系

這頁是 `docs/current-game/skills.json` 的 `職業技能 / 法師系` 可讀版，將舊站鏈路、現行 runtime 與調整維度放在同一頁。

- Skills in this page: `6`
- Source JSON: [`skills.json`](../skills.json)
- Registry note: [`skills.md`](../skills.html)
- Index: [`skills-index.md`](../skills-index.html)

## Family Overview

| Family | Legacy Chain | Skills | Audit States |
| --- | --- | --- | --- |
| legacy-page:mage | abstract<br>dark hell -> seven key numen<br>meditation<br>restore staff<br>six god | 6 | legacy_catalog_seeded |

## Skill Cards

## legacy-page:mage

Legacy chain: `abstract / dark hell -> seven key numen / meditation / restore staff / six god`

### 煉妖術 / `abstract`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:mage`
- Legacy prerequisite: `從缺`
- Legacy next: `-`
- Runtime file: `skill/a/abstract.ski`
- Runtime slot: `SLOT_ABSTRACT`
- Runtime key: `abstract`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `50 / 10`
- CostType / Weapon / Check: `COST_MANA / - / -`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `天 師 >= 五十級, max 一代宗師﹗; 道 士 >= 三十級, max 心神領會﹗; 鑄劍師 >= 五十級, max 登峰造極﹗; - >= -, max -`
- Restrictions: `attrs: 智力 >= 三十五`
- Damage model: `code-driven`
- Code path: `src/spell.c:5358`
- Code damage summary: `Direct damage path confirmed in source, but no compact summary was extracted.`
- Damage values: `(not stored in .ski #Damage)`
- Chance / Parry / Innate: `(resolved in code path, not .ski arrays)`
- Legacy page source: `skill/mage.html`
- Notes: Code-driven offensive exception: damage logic currently lives in src/spell.c:5358.

### 死黑核爆裂地獄 / `dark hell`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:mage`
- Legacy prerequisite: `從缺`
- Legacy next: `seven key numen`
- Runtime file: `skill/d/dark_hell.ski`
- Runtime slot: `SLOT_DARK_HELL`
- Runtime key: `dark_hell`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `100 / 30`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `天 師 >= 六十級, max 一代宗師﹗`
- Restrictions: `attrs: 學識 >= 二十五, 智力 >= 二十五; skills: 狂奔雷電 >= 登峰造極, 火之精靈 >= 出神入化`
- Damage model: `code-driven`
- Code path: `src/spell.c:5426`
- Code damage summary: `formula: spell_damage(ch, level, TYPE_INT, SPELL_CLASS_MAG); attack mode: ATTACK_RANDOM`
- Damage values: `(not stored in .ski #Damage)`
- Chance / Parry / Innate: `(resolved in code path, not .ski arrays)`
- Legacy page source: `skill/mage.html`
- Notes: Code-driven offensive exception: damage logic currently lives in src/spell.c:5426.

### 打禪七 / `meditation`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:mage`
- Legacy prerequisite: `從缺`
- Legacy next: `-`
- Runtime file: `skill/m/meditation.ski`
- Runtime slot: `SLOT_MEDITATION`
- Runtime key: `meditation`
- Type: `TAR_MEDITATION`
- Cost / Wait: `1 / 1`
- CostType / Weapon / Check: `COST_MANA / - / -`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `天 師 >= 五十級, max 一代宗師﹗; 道 士 >= 十級, max 心神領會﹗; 鑄劍師 >= 五十級, max 登峰造極﹗`
- Restrictions: `attrs: 智力 >= 二十, 學識 >= 十五`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/mage.html`

### 補充法杖 / `restore staff`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:mage`
- Legacy prerequisite: `從缺`
- Legacy next: `-`
- Runtime file: `skill/r/restore_staff.ski`
- Runtime slot: `SLOT_RESTORE_STAFF`
- Runtime key: `restore_staff`
- Type: `TAR_OBJ_INV`
- Cost / Wait: `40 / 25`
- CostType / Weapon / Check: `COST_MANA / - / -`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `伶 人 >= 一級, max 一代宗師﹗; 郎 中 >= 一級, max 出神入化﹗; 天 師 >= 一級, max 一代宗師﹗; 文 官 >= 一級, max 出類拔萃﹗; 道 士 >= 一級, max 出類拔萃﹗; 鑄劍師 >= 一級, max 出神入化﹗`
- Restrictions: `-`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/mage.html`

### 七鑰守護神 / `seven key numen`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:mage`
- Legacy prerequisite: `死黑核爆裂地獄(dark hell)`
- Legacy next: `-`
- Runtime file: `skill/s/seven_key_numen.ski`
- Runtime slot: `SLOT_SEVEN_KEY_NUMEN`
- Runtime key: `seven_key_numen`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `300 / 45`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `No / No / Yes / No`
- Class limits: `天 師 >= 九十級, max 一代宗師﹗`
- Restrictions: `attrs: 智力 >= 四十; skills: 死黑核爆裂地獄 >= 神乎其技`
- Damage model: `code-driven`
- Code path: `src/spell.c:4161`
- Code damage summary: `formula: spell_damage(ch, level, TYPE_INT, SPELL_CLASS_MAG); attack mode: ATTACK_RANDOM`
- Damage values: `(not stored in .ski #Damage)`
- Chance / Parry / Innate: `(resolved in code path, not .ski arrays)`
- Legacy page source: `skill/mage.html`
- Notes: Code-driven offensive exception: damage logic currently lives in src/spell.c:4161.

### 六神訣 / `six god`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:mage`
- Legacy prerequisite: `從缺`
- Legacy next: `-`
- Runtime file: `skill/s/six_god.ski`
- Runtime slot: `SLOT_SIX_GOD`
- Runtime key: `six_god`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `130 / 20`
- CostType / Weapon / Check: `COST_MANA / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `天 師 >= 六十級, max 一代宗師﹗; 鑄劍師 >= 八十級, max 神乎其技﹗`
- Restrictions: `attrs: 學識 >= 二十五`
- Damage model: `code-driven`
- Code path: `src/spell.c:5484`
- Code damage summary: `formula: spell_damage(ch, level, TYPE_WIS, SPELL_CLASS_FIV); attack mode: ATTACK_RANDOM`
- Damage values: `(not stored in .ski #Damage)`
- Chance / Parry / Innate: `(resolved in code path, not .ski arrays)`
- Legacy page source: `skill/mage.html`
- Notes: Code-driven offensive exception: damage logic currently lives in src/spell.c:5484.

