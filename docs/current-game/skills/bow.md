---
layout: default
title: Current Game 弓 Skills
---

# Current Game 武器技能 / 弓

這頁是 `docs/current-game/skills.json` 的 `武器技能 / 弓` 可讀版，將舊站鏈路、現行 runtime 與調整維度放在同一頁。

- Skills in this page: `3`
- Source JSON: [`skills.json`](../skills.json)
- Registry note: [`skills.md`](../skills.html)
- Index: [`skills-index.md`](../skills-index.html)

## Family Overview

| Family | Legacy Chain | Skills | Audit States |
| --- | --- | --- | --- |
| legacy-page:bow | shoot sun -> water cloud blast -> fun wu blast | 3 | legacy_catalog_seeded |

## Skill Cards

## legacy-page:bow

Legacy chain: `shoot sun -> water cloud blast -> fun wu blast`

### 鳳舞箭法 / `fun wu blast`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:bow`
- Legacy prerequisite: `水雲箭法(water cloud blast)`
- Legacy next: `-`
- Runtime file: `skill/f/fun_wu_blast.ski`
- Runtime slot: `SLOT_FUN_WU_BLAST`
- Runtime key: `fun_wu_blast`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `20 / 15`
- CostType / Weapon / Check: `COST_MOVE / WEAPON_BOW / check_bow_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `刺 客 >= 一級, max 神乎其技﹗; 將 軍 >= 一級, max 一代宗師﹗`
- Restrictions: `attrs: 體格 >= 二十五, 敏捷 >= 三十五, 力量 >= 二十五; skills: 水雲箭法 >= 出神入化`
- Damage model: `code-driven`
- Code path: `src/spell.c:5703`
- Code damage summary: `base ladder: 450, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1400; repeat loop: for (tt = 0; tt <= level / 20; tt++); weapon multiplier: WEAPON_BOW value[1..2]; attack mode: ATTACK_RANDOM`
- Damage values: `(not stored in .ski #Damage)`
- Chance / Parry / Innate: `(resolved in code path, not .ski arrays)`
- Legacy page source: `skill/bow.html`
- Notes: Code-driven offensive exception: damage logic currently lives in src/spell.c:5703.

### 射日箭法 / `shoot sun`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:bow`
- Legacy prerequisite: `從缺`
- Legacy next: `water cloud blast`
- Runtime file: `skill/s/shoot_sun.ski`
- Runtime slot: `SLOT_SHOOT_SUN`
- Runtime key: `shoot_sun`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `20 / 10`
- CostType / Weapon / Check: `COST_MOVE / WEAPON_BOW / check_bow_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `刺 客 >= 一級, max 登峰造極﹗; 武 官 >= 一級, max 出類拔萃﹗; 將 軍 >= 一級, max 一代宗師﹗; 鑄劍師 >= 一級, max 出類拔萃﹗; 盜 賊 >= 一級, max 神乎其技﹗`
- Restrictions: `attrs: 敏捷 >= 十`
- Damage model: `data-driven`
- Damage values: `[80, 95, 110, 125, 140, 160, 180]`
- Chance values: `[20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/bow.html`

### 水雲箭法 / `water cloud blast`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:bow`
- Legacy prerequisite: `射日箭法(shoot sun)`
- Legacy next: `fun wu blast`
- Runtime file: `skill/w/water_cloud_blast.ski`
- Runtime slot: `SLOT_WATER_CLOUD_blast`
- Runtime key: `water_cloud_blast`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `20 / 15`
- CostType / Weapon / Check: `COST_MOVE / WEAPON_BOW / check_bow_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `刺 客 >= 一級, max 出神入化﹗; 武 官 >= 一級, max 出類拔萃﹗; 將 軍 >= 一級, max 一代宗師﹗; 鑄劍師 >= 一級, max 出類拔萃﹗; 盜 賊 >= 一級, max 神乎其技﹗`
- Restrictions: `attrs: 敏捷 >= 二十五, 力量 >= 十五; skills: 射日箭法 >= 出類拔萃`
- Damage model: `code-driven`
- Code path: `src/spell.c:5571`
- Code damage summary: `base ladder: 300, 350, 400, 450, 500, 600, 700, 800, 900, 1000; repeat loop: for (tt = 0; tt <= level / 33; tt++); weapon multiplier: WEAPON_BOW value[1..2]; attack mode: ATTACK_RANDOM`
- Damage values: `(not stored in .ski #Damage)`
- Chance / Parry / Innate: `(resolved in code path, not .ski arrays)`
- Legacy page source: `skill/bow.html`
- Notes: Code-driven offensive exception: damage logic currently lives in src/spell.c:5571.

