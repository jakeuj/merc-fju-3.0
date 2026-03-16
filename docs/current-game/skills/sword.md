---
layout: default
title: Current Game 劍 Skills
---

# Current Game 武器技能 / 劍

這頁是 `docs/current-game/skills.json` 的 `武器技能 / 劍` 可讀版，將舊站鏈路、現行 runtime 與調整維度放在同一頁。

- Skills in this page: `15`
- Source JSON: [`skills.json`](../skills.json)
- Registry note: [`skills.md`](../skills.html)
- Index: [`skills-index.md`](../skills-index.html)

## Family Overview

| Family | Legacy Chain | Skills | Audit States |
| --- | --- | --- | --- |
| legacy-page:sword | bad sword -> wumin sword -> noname<br>fu sword -> sky dragon sword -> duansun sword<br>hua sword -> fonxan sword -> dragon sleeve sword<br>shan sword -> shadow kill sword -> six sword<br>two sword -> gsword -> tendo slash | 15 | legacy_catalog_seeded |

## Skill Cards

## legacy-page:sword

Legacy chain: `bad sword -> wumin sword -> noname / fu sword -> sky dragon sword -> duansun sword / hua sword -> fonxan sword -> dragon sleeve sword / shan sword -> shadow kill sword -> six sword / two sword -> gsword -> tendo slash`

### 無情劍法 / `bad sword`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:sword`
- Legacy prerequisite: `從缺`
- Legacy next: `wumin sword`
- Runtime file: `skill/b/badsword.ski`
- Runtime slot: `SLOT_BADSWORD`
- Runtime key: `badsword`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `20 / 1`
- CostType / Weapon / Check: `COST_MOVE / WEAPON_SWORD / check_sword_attack`
- CanAsk / Teach / Valid / Enable: `No / No / No / Yes`
- Class limits: `伶 人 >= 一級, max 馬馬虎虎﹗; 刺 客 >= 一級, max 一代宗師﹗; 平 民 >= 一級, max 馬馬虎虎﹗; 郎 中 >= 一級, max 馬馬虎虎﹗; 武 官 >= 一級, max 神乎其技﹗; 將 軍 >= 一級, max 登峰造極﹗; 天 師 >= 一級, max 出類拔萃﹗; 文 官 >= 一級, max 馬馬虎虎﹗; 道 士 >= 一級, max 馬馬虎虎﹗; 鑄劍師 >= 一級, max 出類拔萃﹗; 盜 賊 >= 一級, max 出類拔萃﹗`
- Restrictions: `-`
- Damage values: `[20, 20, 20, 20, 20, 20, 20, 20]`
- Chance values: `[10, 10, 10, 10, 10, 10, 10, 10]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/sword.html`

### 龍袖劍法 / `dragon sleeve sword`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:sword`
- Legacy prerequisite: `封山劍法(fonxan sword)`
- Legacy next: `-`
- Runtime file: `skill/d/dragonsleeve.ski`
- Runtime slot: `SLOT_DRAGONSLEEVE`
- Runtime key: `dragonsleeve`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `25 / 11`
- CostType / Weapon / Check: `COST_MOVE / WEAPON_SWORD / check_sword_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `刺 客 >= 五十級, max 一代宗師﹗; 將 軍 >= 五十級, max 登峰造極﹗`
- Restrictions: `attrs: 敏捷 >= 十五; skills: 封山劍法 >= 登峰造極; classes: 刺 客/將 軍`
- Damage values: `[180, 210, 240, 270, 300, 330, 360, 420]`
- Chance values: `[20, 20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/sword.html`

### 斷家蝕日劍法 / `duansun sword`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:sword`
- Legacy prerequisite: `雙十旋龍斬(sky dragon sword)`
- Legacy next: `-`
- Runtime file: `skill/d/duansun_sword.ski`
- Runtime slot: `SLOT_DUANSUN_SWORD`
- Runtime key: `duansun_sword`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `15 / 10`
- CostType / Weapon / Check: `COST_MOVE / WEAPON_SWORD / check_sword_attack`
- CanAsk / Teach / Valid / Enable: `No / No / No / Yes`
- Class limits: `刺 客 >= 五十級, max 一代宗師﹗; 將 軍 >= 五十級, max 登峰造極﹗; 伶 人 >= -, max -; 平 民 >= -, max -; 郎 中 >= -, max -; 武 官 >= -, max -; 天 師 >= -, max -; 文 官 >= -, max -; 道 士 >= -, max -; 鑄劍師 >= -, max -; 盜 賊 >= -, max -`
- Restrictions: `attrs: 體格 >= 二十五, 敏捷 >= 三十, 力量 >= 二十五; skills: 雙十旋龍斬 >= 登峰造極; classes: 刺 客/將 軍`
- Damage values: `[20, 20, 20, 20, 20, 20, 20]`
- Chance values: `[10, 10, 10, 10, 10, 10, 10]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/sword.html`

### 封山劍法 / `fonxan sword`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:sword`
- Legacy prerequisite: `華山劍法(hua sword)`
- Legacy next: `dragon sleeve sword`
- Runtime file: `skill/f/fonxansword.ski`
- Runtime slot: `SLOT_FONXANSWORD`
- Runtime key: `fonxansword`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `20 / 8`
- CostType / Weapon / Check: `COST_MOVE / WEAPON_SWORD / check_sword_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `刺 客 >= 一級, max 一代宗師﹗; 武 官 >= 一級, max 出類拔萃﹗; 將 軍 >= 一級, max 一代宗師﹗; 天 師 >= 一級, max 神乎其技﹗; 鑄劍師 >= 一級, max 神乎其技﹗; 盜 賊 >= 一級, max 出神入化﹗`
- Restrictions: `skills: 華山劍法 >= 出類拔萃`
- Damage values: `[110, 130, 150, 170, 190, 210, 230, 250]`
- Chance values: `[20, 20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/sword.html`

### 神龍劍法 / `fu sword`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:sword`
- Legacy prerequisite: `從缺`
- Legacy next: `sky dragon sword`
- Runtime file: `skill/f/fuswords.ski`
- Runtime slot: `SLOT_FUSWORDS`
- Runtime key: `fuswords`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `20 / 13`
- CostType / Weapon / Check: `COST_MOVE / WEAPON_SWORD / check_sword_attack`
- CanAsk / Teach / Valid / Enable: `Yes / Yes / Yes / Yes`
- Class limits: `刺 客 >= 一級, max 一代宗師﹗; 武 官 >= 一級, max 出類拔萃﹗; 將 軍 >= 一級, max 一代宗師﹗`
- Restrictions: `attrs: 體格 >= 十, 力量 >= 十五`
- Damage values: `[20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]`
- Chance values: `[20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/sword.html`

### 無量神劍 / `gsword`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:sword`
- Legacy prerequisite: `兩儀劍法(two sword)`
- Legacy next: `tendo slash`
- Runtime file: `skill/g/gsword.ski`
- Runtime slot: `SLOT_GSWORD`
- Runtime key: `gsword`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `25 / 13`
- CostType / Weapon / Check: `COST_MOVE / WEAPON_SWORD / check_sword_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `刺 客 >= 一級, max 一代宗師﹗; 武 官 >= 一級, max 神乎其技﹗; 將 軍 >= 一級, max 一代宗師﹗; 天 師 >= 一級, max 馬馬虎虎﹗; 鑄劍師 >= 一級, max 馬馬虎虎﹗; 盜 賊 >= 一級, max 出神入化﹗`
- Restrictions: `attrs: 學識 >= 十五; skills: 兩儀劍法 >= 出類拔萃`
- Damage values: `[20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]`
- Chance values: `[20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/sword.html`

### 華山劍法 / `hua sword`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:sword`
- Legacy prerequisite: `從缺`
- Legacy next: `fonxan sword`
- Runtime file: `skill/h/hua_sword.ski`
- Runtime slot: `SLOT_HUA_SWORD`
- Runtime key: `hua_sword`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `10 / 5`
- CostType / Weapon / Check: `COST_MOVE / WEAPON_SWORD / check_sword_attack`
- CanAsk / Teach / Valid / Enable: `Yes / Yes / Yes / Yes`
- Class limits: `伶 人 >= 一級, max 馬馬虎虎﹗; 刺 客 >= 一級, max 一代宗師﹗; 平 民 >= 一級, max 馬馬虎虎﹗; 郎 中 >= 一級, max 馬馬虎虎﹗; 武 官 >= 一級, max 神乎其技﹗; 將 軍 >= 一級, max 一代宗師﹗; 天 師 >= 一級, max 出類拔萃﹗; 文 官 >= 一級, max 馬馬虎虎﹗; 道 士 >= 一級, max 馬馬虎虎﹗; 鑄劍師 >= 一級, max 出類拔萃﹗; 盜 賊 >= 一級, max 出類拔萃﹗`
- Restrictions: `-`
- Damage values: `[60, 75, 90, 105, 120, 135, 150]`
- Chance values: `[10, 10, 10, 10, 10, 10, 10]`
- Parry values: `[2, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/sword.html`

### 無名劍法 / `noname`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:sword`
- Legacy prerequisite: `無名劍(wumin sword)`
- Legacy next: `-`
- Runtime file: `skill/n/noname.ski`
- Runtime slot: `SLOT_NONAME`
- Runtime key: `noname`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `20 / 10`
- CostType / Weapon / Check: `COST_MOVE / WEAPON_SWORD / check_sword_attack`
- CanAsk / Teach / Valid / Enable: `No / No / No / Yes`
- Class limits: `刺 客 >= 五十級, max 一代宗師﹗; 將 軍 >= 五十級, max 出神入化﹗; 伶 人 >= -, max -; 平 民 >= -, max -; 郎 中 >= -, max -; 武 官 >= -, max -; 天 師 >= -, max -; 文 官 >= -, max -; 道 士 >= -, max -; 鑄劍師 >= -, max -; 盜 賊 >= -, max -`
- Restrictions: `attrs: 敏捷 >= 三十五, 力量 >= 二十五; skills: 無名劍 >= 出神入化; classes: 刺 客/將 軍`
- Damage values: `[20, 20, 20, 20, 20, 20, 20, 20, 20]`
- Chance values: `[10, 10, 10, 10, 10, 10, 10, 10, 10]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/sword.html`

### 暗影劍法 / `shadow kill sword`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:sword`
- Legacy prerequisite: `銷魂劍法(shan sword)`
- Legacy next: `six sword`
- Runtime file: `skill/s/shadow_kill.ski`
- Runtime slot: `SLOT_SHADOW_KILL`
- Runtime key: `shadow_kill`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `10 / 1`
- CostType / Weapon / Check: `COST_MOVE / WEAPON_SWORD / check_sword_attack`
- CanAsk / Teach / Valid / Enable: `No / No / No / Yes`
- Class limits: `刺 客 >= 五十級, max 一代宗師﹗; 武 官 >= 十級, max 出神入化﹗; 將 軍 >= 五十級, max 登峰造極﹗; 天 師 >= 五十級, max 神乎其技﹗; 鑄劍師 >= 五十級, max 神乎其技﹗; 盜 賊 >= 十級, max 出神入化﹗; 伶 人 >= -, max -; 平 民 >= -, max -; 郎 中 >= -, max -; 文 官 >= -, max -; 道 士 >= -, max -`
- Restrictions: `skills: 銷魂劍法 >= 出類拔萃`
- Damage values: `[20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]`
- Chance values: `[10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/sword.html`

### 銷魂劍法 / `shan sword`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:sword`
- Legacy prerequisite: `從缺`
- Legacy next: `shadow kill sword`
- Runtime file: `skill/s/shansword.ski`
- Runtime slot: `SLOT_SHANSWORD`
- Runtime key: `shansword`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `10 / 1`
- CostType / Weapon / Check: `COST_MOVE / WEAPON_SWORD / check_sword_attack`
- CanAsk / Teach / Valid / Enable: `No / No / No / Yes`
- Class limits: `伶 人 >= 五十級, max 馬馬虎虎﹗; 刺 客 >= 五十級, max 一代宗師﹗; 平 民 >= 一級, max 馬馬虎虎﹗; 郎 中 >= 五十級, max 馬馬虎虎﹗; 武 官 >= 十級, max 神乎其技﹗; 將 軍 >= 五十級, max 登峰造極﹗; 天 師 >= 五十級, max 出類拔萃﹗; 文 官 >= 十級, max 馬馬虎虎﹗; 道 士 >= 十級, max 馬馬虎虎﹗; 鑄劍師 >= 五十級, max 出類拔萃﹗; 盜 賊 >= 十級, max 出類拔萃﹗`
- Restrictions: `-`
- Damage values: `[20, 20, 20, 20, 20, 20, 20, 20]`
- Chance values: `[10, 10, 10, 10, 10, 10, 10, 10]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/sword.html`

### 六劍訣 / `six sword`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:sword`
- Legacy prerequisite: `暗影劍法(shadow kill sword)`
- Legacy next: `-`
- Runtime file: `skill/s/six_sword.ski`
- Runtime slot: `SLOT_SIX_SWORD`
- Runtime key: `six_sword`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `20 / 1`
- CostType / Weapon / Check: `COST_MOVE / WEAPON_SWORD / check_sword_attack`
- CanAsk / Teach / Valid / Enable: `No / No / No / Yes`
- Class limits: `刺 客 >= 一級, max 一代宗師﹗; 將 軍 >= 一級, max 登峰造極﹗; 伶 人 >= -, max -; 平 民 >= -, max -; 郎 中 >= -, max -; 武 官 >= -, max -; 天 師 >= -, max -; 文 官 >= -, max -; 道 士 >= -, max -; 鑄劍師 >= -, max -; 盜 賊 >= -, max -`
- Restrictions: `attrs: 力量 >= 二十五, 敏捷 >= 三十; skills: 暗影劍法 >= 登峰造極; classes: 刺 客/將 軍`
- Damage values: `[20, 20, 20, 20, 20, 20, 20]`
- Chance values: `[10, 10, 10, 10, 10, 10, 10]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/sword.html`

### 雙十旋龍斬 / `sky dragon sword`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:sword`
- Legacy prerequisite: `神龍劍法(fu sword)`
- Legacy next: `duansun sword`
- Runtime file: `skill/s/skydragon_sword.ski`
- Runtime slot: `SLOT_SKYDRAGON_SWORD`
- Runtime key: `skydragon_sword`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `30 / 14`
- CostType / Weapon / Check: `COST_MOVE / WEAPON_SWORD / check_sword_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `刺 客 >= 一級, max 一代宗師﹗; 將 軍 >= 一級, max 登峰造極﹗`
- Restrictions: `attrs: 體格 >= 二十五, 敏捷 >= 二十五, 力量 >= 二十五; skills: 神龍劍法 >= 神乎其技; classes: 刺 客/將 軍`
- Damage values: `[20, 20, 20, 20, 20, 20, 20, 20]`
- Chance values: `[20, 20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/sword.html`

### 天道九劍 / `tendo slash`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:sword`
- Legacy prerequisite: `無量神劍(gsword)`
- Legacy next: `-`
- Runtime file: `skill/t/tendo_slash.ski`
- Runtime slot: `SLOT_TENDO_SLASH`
- Runtime key: `tendo_slash`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `30 / 14`
- CostType / Weapon / Check: `COST_MOVE / WEAPON_SWORD / check_sword_attack`
- CanAsk / Teach / Valid / Enable: `No / No / Yes / Yes`
- Class limits: `刺 客 >= 一級, max 一代宗師﹗; 將 軍 >= 一級, max 登峰造極﹗`
- Restrictions: `attrs: 敏捷 >= 二十, 學識 >= 二十五; skills: 無量神劍 >= 登峰造極; classes: 刺 客/將 軍`
- Damage values: `[20, 20, 20, 20, 20, 20, 20, 20, 20]`
- Chance values: `[20, 20, 20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/sword.html`

### 兩儀劍法 / `two sword`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:sword`
- Legacy prerequisite: `從缺`
- Legacy next: `gsword`
- Runtime file: `skill/t/twosword.ski`
- Runtime slot: `SLOT_TWOSWORD`
- Runtime key: `twosword`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `20 / 12`
- CostType / Weapon / Check: `- / WEAPON_SWORD / check_sword_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `伶 人 >= 十級, max 心神領會﹗; 刺 客 >= 十級, max 一代宗師﹗; 平 民 >= 十級, max 初窺門徑﹗; 郎 中 >= 十級, max 心神領會﹗; 武 官 >= 十級, max 神乎其技﹗; 將 軍 >= 十級, max 一代宗師﹗; 天 師 >= 十級, max 出類拔萃﹗; 文 官 >= 十級, max 馬馬虎虎﹗; 道 士 >= 十級, max 馬馬虎虎﹗; 鑄劍師 >= 十級, max 出類拔萃﹗; 盜 賊 >= 十級, max 出類拔萃﹗`
- Restrictions: `-`
- Damage values: `[20, 200, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]`
- Chance values: `[20, 30, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '404 150', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/sword.html`

### 無名劍 / `wumin sword`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:sword`
- Legacy prerequisite: `無情劍法(bad sword)`
- Legacy next: `noname`
- Runtime file: `skill/w/wumin_sword.ski`
- Runtime slot: `SLOT_WUMIN_SWORD`
- Runtime key: `wumin_sword`
- Type: `TAR_CHAR_OFFENSIVE`
- Cost / Wait: `20 / 12`
- CostType / Weapon / Check: `- / WEAPON_SWORD / check_sword_attack`
- CanAsk / Teach / Valid / Enable: `No / No / No / Yes`
- Class limits: `刺 客 >= 一級, max 一代宗師﹗; 武 官 >= 一級, max 出神入化﹗; 將 軍 >= 一級, max 登峰造極﹗; 天 師 >= 一級, max 神乎其技﹗; 鑄劍師 >= 一級, max 神乎其技﹗; 盜 賊 >= 一級, max 出神入化﹗; 伶 人 >= -, max -; 平 民 >= -, max -; 郎 中 >= -, max -; 文 官 >= -, max -; 道 士 >= -, max -`
- Restrictions: `skills: 無情劍法 >= 出類拔萃`
- Damage values: `[20, 20, 20, 20, 20, 20, 20, 20, 20]`
- Chance values: `[10, 10, 10, 10, 10, 10, 10, 10, 10]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Legacy page source: `skill/sword.html`

