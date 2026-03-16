---
layout: default
title: Current Game 拳法 Skills
---

# Current Game 武器技能 / 拳法

這頁是 `docs/current-game/skills.json` 的 `武器技能 / 拳法` 可讀版，將舊站鏈路、現行 runtime 與調整維度放在同一頁。

- Skills in this page: `12`
- Source JSON: [`skills.json`](../skills.json)
- Registry note: [`skills.md`](../skills.html)
- Index: [`skills-index.md`](../skills-index.html)

## Family Overview

| Family | Legacy Chain | Skills | Audit States |
| --- | --- | --- | --- |
| legacy-page:fist | evil fist -> evil king<br>ghost strike -> ghost marial<br>king fist -> sky dragon<br>long fist -> lung shan -> tackle<br>rulai<br>ryo -> hashin | 12 | legacy_catalog_seeded |

## Skill Cards

## legacy-page:fist

Legacy chain: `evil fist -> evil king / ghost strike -> ghost marial / king fist -> sky dragon / long fist -> lung shan -> tackle / rulai / ryo -> hashin`

### 惡霸掌 / `evil fist`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:fist`
- Legacy prerequisite: `從缺`
- Legacy next: `evil king`
- Runtime file: `skill/e/evilfist.ski`
- Runtime slot: `SLOT_EVILFIST`
- Runtime key: `evilfist`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `20 / 10`
- CostType / Weapon / Check: `COST_MOVE / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `刺 客 >= 一級, max 一代宗師﹗; 武 官 >= 一級, max 出類拔萃﹗; 將 軍 >= 一級, max 一代宗師﹗; 盜 賊 >= 一級, max 出類拔萃﹗`
- Restrictions: `-`
- Damage values: `[20, 20, 20, 20, 20, 20, 20]`
- Chance values: `[10, 10, 10, 10, 10, 10, 10]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/fist.html`

### 邪皇拳 / `evil king`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:fist`
- Legacy prerequisite: `惡霸掌(evil fist)`
- Legacy next: `-`
- Runtime file: `skill/e/evil_king.ski`
- Runtime slot: `SLOT_EVIL_KING`
- Runtime key: `evil_king`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `20 / 8`
- CostType / Weapon / Check: `COST_MOVE / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `刺 客 >= 一級, max 一代宗師﹗; 武 官 >= 一級, max 出類拔萃﹗; 將 軍 >= 一級, max 一代宗師﹗; 盜 賊 >= 一級, max 出類拔萃﹗`
- Restrictions: `attrs: 力量 >= 十五; skills: 惡霸掌 >= 出類拔萃`
- Damage values: `[20, 20, 20, 20, 20, 20, 20, 20]`
- Chance values: `[10, 10, 10, 10, 10, 10, 10, 10]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/fist.html`

### 鬼拳 / `ghost marial`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:fist`
- Legacy prerequisite: `玄陰掌(ghost strike)`
- Legacy next: `-`
- Runtime file: `skill/g/ghost_marial.ski`
- Runtime slot: `SLOT_GHOST_MARIAL`
- Runtime key: `ghost_marial`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `20 / 7`
- CostType / Weapon / Check: `- / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `伶 人 >= 一級, max 出類拔萃﹗; 刺 客 >= 一級, max 一代宗師﹗; 郎 中 >= 一級, max 出類拔萃﹗; 將 軍 >= 一級, max 登峰造極﹗; 天 師 >= 一級, max 出類拔萃﹗; 鑄劍師 >= 一級, max 出類拔萃﹗; 盜 賊 >= 一級, max 神乎其技﹗`
- Restrictions: `attrs: 敏捷 >= 十五; skills: 玄陰掌 >= 出類拔萃`
- Damage values: `[20, 20, 20, 20, 20, 20]`
- Chance values: `[20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/fist.html`

### 玄陰掌 / `ghost strike`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:fist`
- Legacy prerequisite: `從缺`
- Legacy next: `ghost marial`
- Runtime file: `skill/g/ghoststrike.ski`
- Runtime slot: `SLOT_GHOSTSTRIKE`
- Runtime key: `ghoststrike`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `20 / 10`
- CostType / Weapon / Check: `COST_MOVE / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / Yes / Yes / Yes`
- Class limits: `伶 人 >= 一級, max 出類拔萃﹗; 刺 客 >= 一級, max 一代宗師﹗; 郎 中 >= 一級, max 出類拔萃﹗; 武 官 >= 一級, max 馬馬虎虎﹗; 將 軍 >= 一級, max 登峰造極﹗; 天 師 >= 一級, max 出類拔萃﹗; 文 官 >= 一級, max 馬馬虎虎﹗; 道 士 >= 一級, max 馬馬虎虎﹗; 鑄劍師 >= 一級, max 出類拔萃﹗; 盜 賊 >= 一級, max 登峰造極﹗`
- Restrictions: `-`
- Damage values: `[20, 20, 20, 20, 20, 20, 20]`
- Chance values: `[20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/fist.html`

### 秘拳．八神 / `hashin`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:fist`
- Legacy prerequisite: `草薙拳法(ryo)`
- Legacy next: `-`
- Runtime file: `skill/h/hashin.ski`
- Runtime slot: `SLOT_HASHIN`
- Runtime key: `hashin`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `30 / 5`
- CostType / Weapon / Check: `COST_MOVE / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `刺 客 >= 五十級, max 一代宗師﹗; 將 軍 >= 五十級, max 一代宗師﹗`
- Restrictions: `attrs: 力量 >= 二十五; skills: 草薙拳法 >= 出類拔萃; classes: 刺 客/將 軍`
- Damage values: `[20, 20, 20, 20, 20, 20, 20, 20, 20, 20]`
- Chance values: `[20, 20, 20, 20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/fist.html`

### 王拳 / `king fist`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:fist`
- Legacy prerequisite: `從缺`
- Legacy next: `sky dragon`
- Runtime file: `skill/k/king_fist.ski`
- Runtime slot: `SLOT_KING_FIST`
- Runtime key: `king_fist`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `19 / 12`
- CostType / Weapon / Check: `- / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `No / No / No / Yes`
- Class limits: `伶 人 >= 一級, max 馬馬虎虎﹗; 刺 客 >= 一級, max 一代宗師﹗; 平 民 >= 一級, max 馬馬虎虎﹗; 郎 中 >= 一級, max 馬馬虎虎﹗; 武 官 >= 一級, max 出類拔萃﹗; 將 軍 >= 一級, max 登峰造極﹗; 天 師 >= 一級, max 馬馬虎虎﹗; 文 官 >= 一級, max 馬馬虎虎﹗; 道 士 >= 一級, max 馬馬虎虎﹗; 鑄劍師 >= 一級, max 馬馬虎虎﹗; 盜 賊 >= 一級, max 出類拔萃﹗`
- Restrictions: `-`
- Damage values: `[20, 20, 20, 20, 20, 20, 20]`
- Chance values: `[10, 10, 10, 10, 10, 10, 10]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/fist.html`

### 泰山長拳 / `long fist`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:fist`
- Legacy prerequisite: `從缺`
- Legacy next: `lung shan`
- Runtime file: `skill/l/longfist.ski`
- Runtime slot: `SLOT_LONGFIST`
- Runtime key: `longfist`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `10 / 5`
- CostType / Weapon / Check: `COST_MOVE / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / Yes / Yes / Yes`
- Class limits: `伶 人 >= 一級, max 馬馬虎虎﹗; 刺 客 >= 一級, max 一代宗師﹗; 平 民 >= 一級, max 馬馬虎虎﹗; 郎 中 >= 一級, max 馬馬虎虎﹗; 武 官 >= 一級, max 出類拔萃﹗; 將 軍 >= 一級, max 一代宗師﹗; 天 師 >= 一級, max 馬馬虎虎﹗; 文 官 >= 一級, max 馬馬虎虎﹗; 道 士 >= 一級, max 馬馬虎虎﹗; 鑄劍師 >= 一級, max 馬馬虎虎﹗; 盜 賊 >= 一級, max 出類拔萃﹗`
- Restrictions: `-`
- Damage values: `[20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]`
- Chance values: `[20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/fist.html`

### 瀧山拳法 / `lung shan`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:fist`
- Legacy prerequisite: `泰山長拳(long fist)`
- Legacy next: `tackle`
- Runtime file: `skill/l/lungshan.ski`
- Runtime slot: `SLOT_LUNGSHAN`
- Runtime key: `lungshan`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `10 / 5`
- CostType / Weapon / Check: `COST_MOVE / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `刺 客 >= 一級, max 一代宗師﹗; 武 官 >= 一級, max 出類拔萃﹗; 將 軍 >= 一級, max 登峰造極﹗; 盜 賊 >= 一級, max 神乎其技﹗`
- Restrictions: `skills: 泰山長拳 >= 心神領會`
- Damage values: `[20, 20, 20, 20, 20, 20, 20]`
- Chance values: `[20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/fist.html`

### 如來神掌 / `rulai`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:fist`
- Legacy prerequisite: `從缺`
- Legacy next: `-`
- Runtime file: `skill/r/rulai.ski`
- Runtime slot: `SLOT_RULAI`
- Runtime key: `rulai`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `20 / 10`
- CostType / Weapon / Check: `COST_MOVE / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `No / No / Yes / Yes`
- Class limits: `刺 客 >= 一級, max 一代宗師﹗; 將 軍 >= 一級, max 一代宗師﹗`
- Restrictions: `-`
- Damage values: `[20, 20, 20, 20, 20, 20, 20, 20, 20]`
- Chance values: `[20, 20, 20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/fist.html`

### 草薙拳法 / `ryo`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:fist`
- Legacy prerequisite: `從缺`
- Legacy next: `hashin`
- Runtime file: `skill/r/ryo.ski`
- Runtime slot: `SLOT_RYO`
- Runtime key: `ryo`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `20 / 5`
- CostType / Weapon / Check: `COST_MOVE / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `伶 人 >= 一級, max 馬馬虎虎﹗; 刺 客 >= 一級, max 一代宗師﹗; 郎 中 >= 一級, max 馬馬虎虎﹗; 武 官 >= 一級, max 心神領會﹗; 將 軍 >= 一級, max 一代宗師﹗; 天 師 >= 一級, max 馬馬虎虎﹗; 文 官 >= 一級, max 粗通皮毛﹗; 道 士 >= 一級, max 粗通皮毛﹗; 鑄劍師 >= 一級, max 馬馬虎虎﹗; 盜 賊 >= 一級, max 馬馬虎虎﹗`
- Restrictions: `-`
- Damage values: `[150, 20, 20, 20, 20, 20, 20]`
- Chance values: `[20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/fist.html`

### 天龍真氣 / `sky dragon force`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:fist`
- Legacy prerequisite: `天龍訣(sky dragon)`
- Legacy next: `-`
- Runtime file: `skill/s/skydragon_force.ski`
- Runtime slot: `SLOT_SKYDRAGON_FORCE`
- Runtime key: `skydragon_force`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `10 / 1`
- CostType / Weapon / Check: `COST_MOVE / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `No / No / No / Yes`
- Class limits: `刺 客 >= 一級, max 一代宗師﹗; 將 軍 >= 一級, max 登峰造極﹗; 盜 賊 >= 一級, max 神乎其技﹗; 伶 人 >= -, max -; 平 民 >= -, max -; 郎 中 >= -, max -; 武 官 >= -, max -; 天 師 >= -, max -; 文 官 >= -, max -; 道 士 >= -, max -; 鑄劍師 >= -, max -`
- Restrictions: `skills: 天龍訣 >= 神乎其技`
- Damage values: `[20, 20, 20]`
- Chance values: `[10, 10, 10]`
- Parry values: `[0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0']`
- Legacy page source: `skill/fist.html`

### 小擒拿手 / `tackle`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:fist`
- Legacy prerequisite: `瀧山拳法(lung shan)`
- Legacy next: `-`
- Runtime file: `skill/t/tackle.ski`
- Runtime slot: `SLOT_TACKLE`
- Runtime key: `tackle`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `10 / 5`
- CostType / Weapon / Check: `COST_MOVE / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `刺 客 >= 一級, max 一代宗師﹗; 將 軍 >= 一級, max 登峰造極﹗; 盜 賊 >= 一級, max 神乎其技﹗`
- Restrictions: `skills: 瀧山拳法 >= 神乎其技`
- Damage values: `[20, 20, 20, 20, 20, 20, 20, 20]`
- Chance values: `[20, 20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/fist.html`

