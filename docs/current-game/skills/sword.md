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
- Damage model: `data-driven`
- Damage values: `[60, 75, 90, 105, 120, 140, 160, 185]`
- Chance values: `[10, 10, 10, 10, 10, 10, 10, 10]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Failenable mean: `116.88`
- Practice-adjusted mean: `player_30=80; player_60=106.24; player_90=138.6; npc_100=116.88`
- Tempo pressure: `player_30=80; player_60=106.24; player_90=138.6; npc_100=116.88`
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
- Damage model: `data-driven`
- Damage values: `[180, 210, 240, 270, 300, 330, 360, 420]`
- Chance values: `[20, 20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Failenable mean: `288.75`
- Practice-adjusted mean: `player_30=220; player_60=272.49; player_90=328.33; npc_100=288.75`
- Tempo pressure: `player_30=20; player_60=24.77; player_90=29.85; npc_100=26.25`
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
- Damage model: `data-driven`
- Damage values: `[200, 225, 250, 280, 315, 355, 400]`
- Chance values: `[10, 10, 10, 10, 10, 10, 10]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Failenable mean: `289.29`
- Practice-adjusted mean: `player_30=227.38; player_60=270.47; player_90=326.33; npc_100=289.29`
- Tempo pressure: `player_30=22.74; player_60=27.05; player_90=32.63; npc_100=28.93`
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
- Damage model: `data-driven`
- Damage values: `[110, 130, 150, 170, 190, 210, 230, 250]`
- Chance values: `[20, 20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Failenable mean: `180`
- Practice-adjusted mean: `player_30=136.66; player_60=171.66; player_90=207.77; npc_100=180`
- Tempo pressure: `player_30=17.08; player_60=21.46; player_90=25.97; npc_100=22.5`
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
- Damage model: `data-driven`
- Damage values: `[95, 115, 135, 155, 175, 200, 225, 250, 275, 305, 340]`
- Chance values: `[20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Failenable mean: `206.36`
- Practice-adjusted mean: `player_30=134.39; player_60=187.42; player_90=249.13; npc_100=206.36`
- Tempo pressure: `player_30=10.34; player_60=14.42; player_90=19.16; npc_100=15.87`
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
- Damage model: `data-driven`
- Damage values: `[110, 130, 150, 170, 190, 215, 240, 265, 295, 330, 370]`
- Chance values: `[20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Failenable mean: `224.09`
- Practice-adjusted mean: `player_30=149.39; player_60=202.42; player_90=266.96; npc_100=224.09`
- Tempo pressure: `player_30=11.49; player_60=15.57; player_90=20.54; npc_100=17.24`
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
- Damage model: `data-driven`
- Damage values: `[60, 75, 90, 105, 120, 135, 150]`
- Chance values: `[10, 10, 10, 10, 10, 10, 10]`
- Parry values: `[2, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Failenable mean: `105`
- Practice-adjusted mean: `player_30=76.43; player_60=100; player_90=123.57; npc_100=105`
- Tempo pressure: `player_30=15.29; player_60=20; player_90=24.71; npc_100=21`
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
- Damage model: `data-driven`
- Damage values: `[155, 175, 195, 215, 235, 260, 290, 325, 360]`
- Chance values: `[10, 10, 10, 10, 10, 10, 10, 10, 10]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Failenable mean: `245.56`
- Practice-adjusted mean: `player_30=185.36; player_60=226.84; player_90=280.05; npc_100=245.56`
- Tempo pressure: `player_30=18.54; player_60=22.68; player_90=28.01; npc_100=24.56`
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
- Damage model: `data-driven`
- Damage values: `[90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255, 270, 290, 310, 335, 360]`
- Chance values: `[10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Failenable mean: `213.82`
- Practice-adjusted mean: `player_30=139.4; player_60=197.35; player_90=257.34; npc_100=213.82`
- Tempo pressure: `player_30=139.4; player_60=197.35; player_90=257.34; npc_100=213.82`
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
- Damage model: `data-driven`
- Damage values: `[55, 70, 85, 100, 115, 130, 145, 165]`
- Chance values: `[10, 10, 10, 10, 10, 10, 10, 10]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Failenable mean: `108.12`
- Practice-adjusted mean: `player_30=75; player_60=101.24; player_90=128.6; npc_100=108.12`
- Tempo pressure: `player_30=75; player_60=101.24; player_90=128.6; npc_100=108.12`
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
- Damage model: `data-driven`
- Damage values: `[170, 195, 220, 245, 275, 310, 350]`
- Chance values: `[10, 10, 10, 10, 10, 10, 10]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Failenable mean: `252.14`
- Practice-adjusted mean: `player_30=197.38; player_60=237.13; player_90=285.15; npc_100=252.14`
- Tempo pressure: `player_30=197.38; player_60=237.13; player_90=285.15; npc_100=252.14`
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
- Damage model: `data-driven`
- Damage values: `[150, 180, 210, 240, 275, 315, 360, 410]`
- Chance values: `[20, 20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Failenable mean: `267.5`
- Practice-adjusted mean: `player_30=190; player_60=244.16; player_90=313.32; npc_100=267.5`
- Tempo pressure: `player_30=13.57; player_60=17.44; player_90=22.38; npc_100=19.11`
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
- Damage model: `data-driven`
- Damage values: `[180, 205, 230, 255, 285, 320, 360, 405, 455]`
- Chance values: `[20, 20, 20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Failenable mean: `299.44`
- Practice-adjusted mean: `player_30=217.96; player_60=272.96; player_90=345.98; npc_100=299.44`
- Tempo pressure: `player_30=15.57; player_60=19.5; player_90=24.71; npc_100=21.39`
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
- CostType / Weapon / Check: `COST_MOVE / WEAPON_SWORD / check_sword_attack`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / Yes`
- Class limits: `伶 人 >= 十級, max 心神領會﹗; 刺 客 >= 十級, max 一代宗師﹗; 平 民 >= 十級, max 初窺門徑﹗; 郎 中 >= 十級, max 心神領會﹗; 武 官 >= 十級, max 神乎其技﹗; 將 軍 >= 十級, max 一代宗師﹗; 天 師 >= 十級, max 出類拔萃﹗; 文 官 >= 十級, max 馬馬虎虎﹗; 道 士 >= 十級, max 馬馬虎虎﹗; 鑄劍師 >= 十級, max 出類拔萃﹗; 盜 賊 >= 十級, max 出類拔萃﹗`
- Restrictions: `-`
- Damage model: `data-driven`
- Damage values: `[70, 200, 85, 100, 115, 130, 145, 160, 175, 190, 205, 225]`
- Chance values: `[20, 30, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '404 150', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Failenable mean: `152`
- Practice-adjusted mean: `player_30=125.35; player_60=124; player_90=166.66; npc_100=152`
- Tempo pressure: `player_30=10.45; player_60=10.33; player_90=13.89; npc_100=12.67`
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
- CostType / Weapon / Check: `COST_MOVE / WEAPON_SWORD / check_sword_attack`
- CanAsk / Teach / Valid / Enable: `No / No / No / Yes`
- Class limits: `刺 客 >= 一級, max 一代宗師﹗; 武 官 >= 一級, max 出神入化﹗; 將 軍 >= 一級, max 登峰造極﹗; 天 師 >= 一級, max 神乎其技﹗; 鑄劍師 >= 一級, max 神乎其技﹗; 盜 賊 >= 一級, max 出神入化﹗; 伶 人 >= -, max -; 平 民 >= -, max -; 郎 中 >= -, max -; 文 官 >= -, max -; 道 士 >= -, max -`
- Restrictions: `skills: 無情劍法 >= 出類拔萃`
- Damage model: `data-driven`
- Damage values: `[115, 135, 155, 175, 195, 220, 245, 275, 310]`
- Chance values: `[10, 10, 10, 10, 10, 10, 10, 10, 10]`
- Parry values: `[0, 0, 0, 0, 0, 0, 0, 0, 0]`
- Innate values: `['0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0', '0 0']`
- Failenable mean: `202.78`
- Practice-adjusted mean: `player_30=145.36; player_60=186.84; player_90=236.1; npc_100=202.78`
- Tempo pressure: `player_30=12.11; player_60=15.57; player_90=19.68; npc_100=16.9`
- Legacy page source: `skill/sword.html`

