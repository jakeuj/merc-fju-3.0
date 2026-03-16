---
layout: default
title: Current Game 棍 Skills
---

# Current Game 武器技能 / 棍

這頁是 `docs/current-game/skills.json` 的 `武器技能 / 棍` 可讀版，將舊站鏈路、現行 runtime 與調整維度放在同一頁。

- Skills in this page: `2`
- Source JSON: [`skills.json`](../skills.json)
- Registry note: [`skills.md`](../skills.html)
- Index: [`skills-index.md`](../skills-index.html)

## Family Overview

| Family | Legacy Chain | Skills | Audit States |
| --- | --- | --- | --- |
| legacy-page:stick | monkey stick -> day stick | 2 | legacy_catalog_seeded |

## Skill Cards

## legacy-page:stick

Legacy chain: `monkey stick -> day stick`

### 日晃棍法 / `day stick`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:stick`
- Legacy prerequisite: `猴棍(monkey stick)`
- Legacy next: `-`
- Runtime file: `skill/d/daystick.ski`
- Runtime slot: `SLOT_DAYSTICK`
- Runtime key: `daystick`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `30 / 14`
- CostType / Weapon / Check: `COST_MOVE / WEAPON_CLUB / check_club_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `刺 客 >= 一級, max 一代宗師﹗; 武 官 >= 一級, max 粗通皮毛﹗; 將 軍 >= 一級, max 一代宗師﹗`
- Restrictions: `attrs: 敏捷 >= 十; skills: 猴棍 >= 出類拔萃`
- Damage values: `[20, 20, 20, 20, 20]`
- Chance values: `[20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/stick.html`

### 猴棍 / `monkey stick`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:stick`
- Legacy prerequisite: `從缺`
- Legacy next: `day stick`
- Runtime file: `skill/m/monkey_stick.ski`
- Runtime slot: `SLOT_MONKEY_STICK`
- Runtime key: `monkey_stick`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `30 / 17`
- CostType / Weapon / Check: `COST_MOVE / WEAPON_CLUB / check_club_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `伶 人 >= 一級, max 初窺門徑﹗; 刺 客 >= 一級, max 一代宗師﹗; 平 民 >= 一級, max 初窺門徑﹗; 郎 中 >= 一級, max 初窺門徑﹗; 武 官 >= 一級, max 出類拔萃﹗; 將 軍 >= 一級, max 一代宗師﹗; 天 師 >= 一級, max 初窺門徑﹗; 文 官 >= 一級, max 初窺門徑﹗; 道 士 >= 一級, max 初窺門徑﹗; 鑄劍師 >= 一級, max 初窺門徑﹗; 盜 賊 >= 一級, max 心神領會﹗`
- Restrictions: `-`
- Damage values: `[20, 20, 20, 20, 20]`
- Chance values: `[10, 10, 10, 10, 10]`
- Parry values: `[0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/stick.html`

