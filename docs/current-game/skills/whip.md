---
layout: default
title: Current Game 鞭 Skills
---

# Current Game 武器技能 / 鞭

這頁是 `docs/current-game/skills.json` 的 `武器技能 / 鞭` 可讀版，將舊站鏈路、現行 runtime 與調整維度放在同一頁。

- Skills in this page: `2`
- Source JSON: [`skills.json`](../skills.json)
- Registry note: [`skills.md`](../skills.html)
- Index: [`skills-index.md`](../skills-index.html)

## Family Overview

| Family | Legacy Chain | Skills | Audit States |
| --- | --- | --- | --- |
| legacy-page:whip | gwhip -> ming snake | 2 | legacy_catalog_seeded |

## Skill Cards

## legacy-page:whip

Legacy chain: `gwhip -> ming snake`

### 紫龍鞭法 / `gwhip`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:whip`
- Legacy prerequisite: `從缺`
- Legacy next: `ming snake`
- Runtime file: `skill/g/gwhip.ski`
- Runtime slot: `SLOT_GWHIP`
- Runtime key: `gwhip`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `15 / 10`
- CostType / Weapon / Check: `COST_MOVE / WEAPON_WHIP / check_whip_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `伶 人 >= 一級, max 馬馬虎虎﹗; 刺 客 >= 一級, max 一代宗師﹗; 平 民 >= 一級, max 初窺門徑﹗; 郎 中 >= 一級, max 馬馬虎虎﹗; 武 官 >= 一級, max 出類拔萃﹗; 將 軍 >= 一級, max 登峰造極﹗; 天 師 >= 一級, max 心神領會﹗; 文 官 >= 一級, max 初窺門徑﹗; 道 士 >= 一級, max 馬馬虎虎﹗; 鑄劍師 >= 一級, max 心神領會﹗; 盜 賊 >= 一級, max 出神入化﹗`
- Restrictions: `-`
- Damage values: `[85, 100, 115, 130, 145, 160, 180, 200, 220, 245, 270]`
- Chance values: `[20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/whip.html`

### 冥蛇鞭法 / `ming snake`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:whip`
- Legacy prerequisite: `紫龍鞭法(gwhip)`
- Legacy next: `-`
- Runtime file: `skill/m/ming_snake.ski`
- Runtime slot: `SLOT_MING_SNAKE`
- Runtime key: `ming_snake`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `15 / 10`
- CostType / Weapon / Check: `COST_MOVE / WEAPON_WHIP / check_whip_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `刺 客 >= 一級, max 登峰造極﹗; 武 官 >= 一級, max 馬馬虎虎﹗; 將 軍 >= 一級, max 登峰造極﹗; 盜 賊 >= 一級, max 神乎其技﹗`
- Restrictions: `skills: 紫龍鞭法 >= 出類拔萃`
- Damage values: `[120, 140, 160, 180, 205, 230, 260, 295]`
- Chance values: `[10, 10, 10, 10, 10, 10, 10, 10]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/whip.html`

