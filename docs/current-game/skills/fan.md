---
layout: default
title: Current Game 筆扇 Skills
---

# Current Game 武器技能 / 筆扇

這頁是 `docs/current-game/skills.json` 的 `武器技能 / 筆扇` 可讀版，將舊站鏈路、現行 runtime 與調整維度放在同一頁。

- Skills in this page: `9`
- Source JSON: [`skills.json`](../skills.json)
- Registry note: [`skills.md`](../skills.html)
- Index: [`skills-index.md`](../skills-index.html)

## Family Overview

| Family | Legacy Chain | Skills | Audit States |
| --- | --- | --- | --- |
| legacy-page:fan | butterfly fan -> cloud fan -> flower fan<br>ink pen -> bamboo pen -> love poem<br>know pen -> write pen -> eten dragon | 9 | legacy_catalog_seeded |

## Skill Cards

## legacy-page:fan

Legacy chain: `butterfly fan -> cloud fan -> flower fan / ink pen -> bamboo pen -> love poem / know pen -> write pen -> eten dragon`

### 竹林七賢功 / `bamboo pen`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:fan`
- Legacy prerequisite: `潑墨大寫意(ink pen)`
- Legacy next: `love poem`
- Runtime file: `-`
- Runtime slot: `-`
- Runtime key: `-`
- Type: `-`
- Cost / Wait: `- / -`
- CostType / Weapon / Check: `- / - / -`
- CanAsk / Teach / Valid / Enable: `- / - / - / -`
- Class limits: `伶 人 >= 五十級, max 一代宗師﹗; 郎 中 >= 五十級, max 一代宗師﹗; 天 師 >= 五十級, max 登峰造極﹗; 鑄劍師 >= 五十級, max 登峰造極﹗; 刺 客 >= -, max -; 平 民 >= -, max -; 武 官 >= -, max -; 將 軍 >= -, max -; 文 官 >= -, max -; 道 士 >= -, max -; 盜 賊 >= -, max -`
- Restrictions: `skills: 潑墨大寫意 >= 出類拔萃`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/fan.html`
- Notes: No runtime skill file matched yet; legacy requirements still preserved from old-site HTML.

### 舞蝶扇 / `butterfly fan`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:fan`
- Legacy prerequisite: `從缺`
- Legacy next: `cloud fan`
- Runtime file: `-`
- Runtime slot: `-`
- Runtime key: `-`
- Type: `-`
- Cost / Wait: `- / -`
- CostType / Weapon / Check: `- / - / -`
- CanAsk / Teach / Valid / Enable: `- / - / - / -`
- Class limits: `伶 人 >= 一級, max 一代宗師﹗; 郎 中 >= 一級, max 一代宗師﹗; 天 師 >= 一級, max 登峰造極﹗; 文 官 >= 一級, max 出類拔萃﹗; 道 士 >= 一級, max 心神領會﹗; 鑄劍師 >= 一級, max 登峰造極﹗; 刺 客 >= -, max -; 平 民 >= -, max -; 武 官 >= -, max -; 將 軍 >= -, max -; 盜 賊 >= -, max -`
- Restrictions: `-`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/fan.html`
- Notes: No runtime skill file matched yet; legacy requirements still preserved from old-site HTML.

### 夢雲扇 / `cloud fan`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:fan`
- Legacy prerequisite: `舞蝶扇(butterfly fan)`
- Legacy next: `flower fan`
- Runtime file: `-`
- Runtime slot: `-`
- Runtime key: `-`
- Type: `-`
- Cost / Wait: `- / -`
- CostType / Weapon / Check: `- / - / -`
- CanAsk / Teach / Valid / Enable: `- / - / - / -`
- Class limits: `伶 人 >= 五十級, max 一代宗師﹗; 郎 中 >= 五十級, max 一代宗師﹗; 天 師 >= 五十級, max 登峰造極﹗; 鑄劍師 >= 五十級, max 登峰造極﹗; 刺 客 >= -, max -; 平 民 >= -, max -; 武 官 >= -, max -; 將 軍 >= -, max -; 文 官 >= -, max -; 道 士 >= -, max -; 盜 賊 >= -, max -`
- Restrictions: `skills: 舞蝶扇 >= 出類拔萃`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/fan.html`
- Notes: No runtime skill file matched yet; legacy requirements still preserved from old-site HTML.

### 倚天屠龍功 / `eten dragon`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:fan`
- Legacy prerequisite: `臨書點穴(write pen)`
- Legacy next: `-`
- Runtime file: `skill/e/eten.ski`
- Runtime slot: `SLOT_ETEN`
- Runtime key: `eten`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `19 / 10`
- CostType / Weapon / Check: `- / WEAPON_PEN / check_pen_attack`
- CanAsk / Teach / Valid / Enable: `No / No / Yes / Yes`
- Class limits: `伶 人 >= 一級, max 登峰造極﹗; 郎 中 >= 一級, max 一代宗師﹗; 天 師 >= 一級, max 登峰造極﹗; 鑄劍師 >= 一級, max 登峰造極﹗`
- Restrictions: `attrs: 體格 >= 十五, 學識 >= 三十, 智力 >= 二十; skills: 臨書點穴 >= 登峰造極; classes: 伶 人/郎 中/天 師/鑄劍師`
- Damage values: `[20, 20, 20, 20, 20, 20]`
- Chance values: `[10, 10, 10, 10, 10, 10]`
- Parry values: `[0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/fan.html`

### 萬千花顏扇 / `flower fan`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:fan`
- Legacy prerequisite: `夢雲扇(cloud fan)`
- Legacy next: `-`
- Runtime file: `-`
- Runtime slot: `-`
- Runtime key: `-`
- Type: `-`
- Cost / Wait: `- / -`
- CostType / Weapon / Check: `- / - / -`
- CanAsk / Teach / Valid / Enable: `- / - / - / -`
- Class limits: `伶 人 >= 五十級, max 一代宗師﹗; 郎 中 >= 五十級, max 一代宗師﹗; 天 師 >= 五十級, max 登峰造極﹗; 鑄劍師 >= 五十級, max 登峰造極﹗; 刺 客 >= -, max -; 平 民 >= -, max -; 武 官 >= -, max -; 將 軍 >= -, max -; 文 官 >= -, max -; 道 士 >= -, max -; 盜 賊 >= -, max -`
- Restrictions: `attrs: 學識 >= 三十, 智力 >= 二十五; skills: 夢雲扇 >= 出神入化; classes: 伶 人/郎 中/天 師/鑄劍師`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/fan.html`
- Notes: No runtime skill file matched yet; legacy requirements still preserved from old-site HTML.

### 潑墨大寫意 / `ink pen`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:fan`
- Legacy prerequisite: `從缺`
- Legacy next: `bamboo pen`
- Runtime file: `-`
- Runtime slot: `-`
- Runtime key: `-`
- Type: `-`
- Cost / Wait: `- / -`
- CostType / Weapon / Check: `- / - / -`
- CanAsk / Teach / Valid / Enable: `- / - / - / -`
- Class limits: `伶 人 >= 一級, max 一代宗師﹗; 郎 中 >= 一級, max 一代宗師﹗; 天 師 >= 一級, max 登峰造極﹗; 文 官 >= 一級, max 出類拔萃﹗; 道 士 >= 一級, max 心神領會﹗; 鑄劍師 >= 一級, max 登峰造極﹗; 刺 客 >= -, max -; 平 民 >= -, max -; 武 官 >= -, max -; 將 軍 >= -, max -; 盜 賊 >= -, max -`
- Restrictions: `-`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/fan.html`
- Notes: No runtime skill file matched yet; legacy requirements still preserved from old-site HTML.

### 筆之心 / `know pen`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:fan`
- Legacy prerequisite: `從缺`
- Legacy next: `write pen`
- Runtime file: `skill/k/know_pen.ski`
- Runtime slot: `SLOT_KNOW_PEN`
- Runtime key: `know_pen`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `19 / 12`
- CostType / Weapon / Check: `- / WEAPON_PEN / check_pen_attack`
- CanAsk / Teach / Valid / Enable: `Yes / Yes / Yes / Yes`
- Class limits: `伶 人 >= 一級, max 登峰造極﹗; 郎 中 >= 一級, max 登峰造極﹗; 天 師 >= 一級, max 一代宗師﹗; 文 官 >= 一級, max 心神領會﹗; 道 士 >= 一級, max 馬馬虎虎﹗; 鑄劍師 >= 一級, max 登峰造極﹗; 盜 賊 >= 一級, max 馬馬虎虎﹗`
- Restrictions: `-`
- Damage values: `[20, 20, 20, 20]`
- Chance values: `[10, 10, 10, 10]`
- Parry values: `[0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/fan.html`

### 情詩一百篇 / `love poem`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:fan`
- Legacy prerequisite: `竹林七賢功(bamboo pen)`
- Legacy next: `-`
- Runtime file: `-`
- Runtime slot: `-`
- Runtime key: `-`
- Type: `-`
- Cost / Wait: `- / -`
- CostType / Weapon / Check: `- / - / -`
- CanAsk / Teach / Valid / Enable: `- / - / - / -`
- Class limits: `伶 人 >= 五十級, max 一代宗師﹗; 郎 中 >= 五十級, max 一代宗師﹗; 天 師 >= 五十級, max 登峰造極﹗; 鑄劍師 >= 五十級, max 登峰造極﹗; 刺 客 >= -, max -; 平 民 >= -, max -; 武 官 >= -, max -; 將 軍 >= -, max -; 文 官 >= -, max -; 道 士 >= -, max -; 盜 賊 >= -, max -`
- Restrictions: `attrs: 敏捷 >= 二十, 學識 >= 三十, 智力 >= 二十五; skills: 竹林七賢功 >= 出神入化; classes: 伶 人/郎 中/天 師/鑄劍師`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/fan.html`
- Notes: No runtime skill file matched yet; legacy requirements still preserved from old-site HTML.

### 臨書點穴 / `write pen`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:fan`
- Legacy prerequisite: `筆之心(know pen)`
- Legacy next: `eten dragon`
- Runtime file: `skill/w/write_pen.ski`
- Runtime slot: `SLOT_WRITE_PEN`
- Runtime key: `write_pen`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `19 / 12`
- CostType / Weapon / Check: `- / WEAPON_PEN / check_pen_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `伶 人 >= 一級, max 登峰造極﹗; 郎 中 >= 一級, max 登峰造極﹗; 天 師 >= 一級, max 一代宗師﹗; 鑄劍師 >= 一級, max 登峰造極﹗`
- Restrictions: `attrs: 學識 >= 十五; skills: 筆之心 >= 出類拔萃`
- Damage values: `[20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]`
- Chance values: `[20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/fan.html`

