---
layout: default
title: Current Game 盜賊系 Skills
---

# Current Game 職業技能 / 盜賊系

這頁是 `docs/current-game/skills.json` 的 `職業技能 / 盜賊系` 可讀版，將舊站鏈路、現行 runtime 與調整維度放在同一頁。

- Skills in this page: `10`
- Source JSON: [`skills.json`](../skills.json)
- Registry note: [`skills.md`](../skills.html)
- Index: [`skills-index.md`](../skills-index.html)

## Family Overview

| Family | Legacy Chain | Skills | Audit States |
| --- | --- | --- | --- |
| legacy-page:thief | cook<br>hide -> backstab<br>mask<br>venom -> pick -> sneak -> dormancy -> peek -> steal | 10 | legacy_catalog_seeded |

## Skill Cards

## legacy-page:thief

Legacy chain: `cook / hide -> backstab / mask / venom -> pick -> sneak -> dormancy -> peek -> steal`

### 背刺 / `backstab`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:thief`
- Legacy prerequisite: `隱藏術(hide)`
- Legacy next: `-`
- Runtime file: `skill/b/backstab.ski`
- Runtime slot: `SLOT_BACKSTAB`
- Runtime key: `backstab`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `20 / 12`
- CostType / Weapon / Check: `- / - / check_dagger_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `盜 賊 >= 六十五級, max 一代宗師﹗; 伶 人 >= -, max -; 刺 客 >= -, max -; 平 民 >= -, max -; 郎 中 >= -, max -; 武 官 >= -, max -; 將 軍 >= -, max -; 天 師 >= -, max -; 文 官 >= -, max -; 道 士 >= -, max -; 鑄劍師 >= -, max -`
- Restrictions: `attrs: 敏捷 >= 三十; skills: 隱藏術 >= 出神入化`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/thief.html`

### 料理術 / `cook`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:thief`
- Legacy prerequisite: `從缺`
- Legacy next: `-`
- Runtime file: `skill/c/cook.ski`
- Runtime slot: `SLOT_COOK`
- Runtime key: `cook`
- Type: `TAR_OBJ_ROOM`
- Cost / Wait: `12 / 24`
- CostType / Weapon / Check: `- / - / check_unrigid_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `- >= -, max -; - >= -, max -; 盜 賊 >= 十五級, max 一代宗師﹗; 伶 人 >= -, max -; 刺 客 >= -, max -; 郎 中 >= -, max -; 武 官 >= -, max -; 將 軍 >= -, max -; 天 師 >= -, max -; 文 官 >= -, max -; 道 士 >= -, max -; 鑄劍師 >= -, max -`
- Restrictions: `attrs: 學識 >= 五`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/thief.html`

### 龜息大法 / `dormancy`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:thief`
- Legacy prerequisite: `潛行術(sneak)`
- Legacy next: `peek`
- Runtime file: `skill/d/dormancy.ski`
- Runtime slot: `SLOT_DORMANCY`
- Runtime key: `dormancy`
- Type: `TAR_MEDITATION`
- Cost / Wait: `1 / 1`
- CostType / Weapon / Check: `- / - / -`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `盜  賊 >= 十級, max 一代宗師﹗; 伶  人 >= -, max -; 刺  客 >= -, max -; 平  民 >= -, max -; 郎  中 >= -, max -; 武  官 >= -, max -; 將  軍 >= -, max -; 天  師 >= -, max -; 文  官 >= -, max -; 道  士 >= -, max -; 鑄劍師 >= -, max -; - >= -, max -; - >= -, max -; - >= -, max -; - >= -, max -; - >= -, max -; - >= -, max -; - >= -, max -; - >= -, max -`
- Restrictions: `-`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/thief.html`

### 隱藏術 / `hide`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:thief`
- Legacy prerequisite: `從缺`
- Legacy next: `backstab`
- Runtime file: `skill/h/hide.ski`
- Runtime slot: `SLOT_HIDE`
- Runtime key: `hide`
- Type: `TAR_CHAR_SELF`
- Cost / Wait: `20 / 12`
- CostType / Weapon / Check: `- / - / -`
- CanAsk / Teach / Valid / Enable: `No / No / No / No`
- Class limits: `盜 賊 >= 五十級, max 一代宗師﹗; 伶 人 >= -, max -; 刺 客 >= -, max -; 平 民 >= -, max -; 郎 中 >= -, max -; 武 官 >= -, max -; 將 軍 >= -, max -; 天 師 >= -, max -; 文 官 >= -, max -; 道 士 >= -, max -; 鑄劍師 >= -, max -`
- Restrictions: `attrs: 敏捷 >= 二十五`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/thief.html`

### 易容術 / `mask`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:thief`
- Legacy prerequisite: `從缺`
- Legacy next: `-`
- Runtime file: `skill/m/mask.ski`
- Runtime slot: `SLOT_MASK`
- Runtime key: `mask`
- Type: `TAR_CHAR_SELF`
- Cost / Wait: `100 / 12`
- CostType / Weapon / Check: `- / - / -`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `- >= -, max -; - >= -, max -; 伶 人 >= -, max -; 刺 客 >= -, max -; 平 民 >= -, max -; 郎 中 >= -, max -; 武 官 >= -, max -; 將 軍 >= -, max -; 天 師 >= -, max -; 文 官 >= -, max -; 道 士 >= -, max -; 鑄劍師 >= -, max -`
- Restrictions: `-`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/thief.html`

### 偷窺術 / `peek`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:thief`
- Legacy prerequisite: `龜息大法(dormancy)`
- Legacy next: `steal`
- Runtime file: `-`
- Runtime slot: `-`
- Runtime key: `-`
- Type: `-`
- Cost / Wait: `- / -`
- CostType / Weapon / Check: `- / - / -`
- CanAsk / Teach / Valid / Enable: `- / - / - / -`
- Class limits: `盜  賊 >= 十五級, max 一代宗師﹗; 伶  人 >= -, max -; 刺  客 >= -, max -; 平  民 >= -, max -; 郎  中 >= -, max -; 武  官 >= -, max -; 將  軍 >= -, max -; 天  師 >= -, max -; 文  官 >= -, max -; 道  士 >= -, max -; 鑄劍師 >= -, max -; - >= -, max -; - >= -, max -; - >= -, max -; - >= -, max -; - >= -, max -; - >= -, max -`
- Restrictions: `-`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/thief.html`
- Notes: No runtime skill file matched yet; legacy requirements still preserved from old-site HTML.

### 開鎖 / `pick`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:thief`
- Legacy prerequisite: `抹毒(venom)`
- Legacy next: `sneak`
- Runtime file: `skill/p/pick.ski`
- Runtime slot: `SLOT_PICK`
- Runtime key: `pick`
- Type: `TAR_ARGUMENT`
- Cost / Wait: `20 / 20`
- CostType / Weapon / Check: `- / - / -`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `盜  賊 >= 一級, max 一代宗師﹗; 伶  人 >= -, max -; 刺  客 >= -, max -; 平  民 >= -, max -; 郎  中 >= -, max -; 武  官 >= -, max -; 將  軍 >= -, max -; 天  師 >= -, max -; 文  官 >= -, max -; 道  士 >= -, max -; 鑄劍師 >= -, max -; - >= -, max -; - >= -, max -; - >= -, max -; - >= -, max -; - >= -, max -`
- Restrictions: `-`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/thief.html`

### 潛行術 / `sneak`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:thief`
- Legacy prerequisite: `開鎖(pick)`
- Legacy next: `dormancy`
- Runtime file: `skill/s/sneak.ski`
- Runtime slot: `SLOT_SNEAK`
- Runtime key: `sneak`
- Type: `TAR_CHAR_SELF`
- Cost / Wait: `20 / 12`
- CostType / Weapon / Check: `- / - / -`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `盜  賊 >= 一級, max 一代宗師﹗; 伶  人 >= -, max -; 刺  客 >= -, max -; 平  民 >= -, max -; 郎  中 >= -, max -; 武  官 >= -, max -; 將  軍 >= -, max -; 天  師 >= -, max -; 文  官 >= -, max -; 道  士 >= -, max -; 鑄劍師 >= -, max -; - >= -, max -; - >= -, max -; - >= -, max -; - >= -, max -; - >= -, max -`
- Restrictions: `-`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/thief.html`

### 偷竊 / `steal`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:thief`
- Legacy prerequisite: `偷窺術(peek)`
- Legacy next: `-`
- Runtime file: `skill/s/steal.ski`
- Runtime slot: `SLOT_STEAL`
- Runtime key: `steal`
- Type: `TAR_ARGUMENT`
- Cost / Wait: `20 / 20`
- CostType / Weapon / Check: `- / - / -`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `- >= -, max -; - >= -, max -; 伶 人 >= -, max -; 刺 客 >= -, max -; 平 民 >= -, max -; 郎 中 >= -, max -; 武 官 >= -, max -; 將 軍 >= -, max -; 天 師 >= -, max -; 文 官 >= -, max -; 道 士 >= -, max -; 鑄劍師 >= -, max -`
- Restrictions: `attrs: 敏捷 >= 三十五; skills: 偷窺術 >= 登峰造極`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/thief.html`

### 抹毒 / `venom`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:thief`
- Legacy prerequisite: `從缺`
- Legacy next: `pick`
- Runtime file: `skill/v/venom.ski`
- Runtime slot: `SLOT_VENOM`
- Runtime key: `venom`
- Type: `TAR_OBJ_INV`
- Cost / Wait: `10 / 10`
- CostType / Weapon / Check: `- / - / -`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `伶  人 >= 一級, max 出神入化﹗; 刺  客 >= 一級, max 出神入化﹗; 郎  中 >= 一級, max 出神入化﹗; 武  官 >= 一級, max 出神入化﹗; 將  軍 >= 一級, max 出神入化﹗; 天  師 >= 一級, max 出神入化﹗; 文  官 >= 一級, max 出神入化﹗; 道  士 >= 一級, max 出神入化﹗; 鑄劍師 >= 一級, max 出神入化﹗; 盜  賊 >= 一級, max 一代宗師﹗; 平  民 >= -, max -; - >= -, max -; - >= -, max -; - >= -, max -; - >= -, max -`
- Restrictions: `-`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/thief.html`

