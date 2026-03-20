---
layout: default
title: Current Game 技能 Skills
---

# Current Game 其他技能 / 技能

這頁是 `docs/current-game/skills.json` 的 `其他技能 / 技能` 可讀版，將舊站鏈路、現行 runtime 與調整維度放在同一頁。

- Skills in this page: `1`
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
| legacy-page:skill | mount | 1 | legacy_catalog_seeded |

## Skill Cards

## legacy-page:skill

Legacy chain: `mount`

### 騎術 / `mount`

- Audit: `legacy_catalog_seeded`
- Family: `legacy-page:skill`
- Legacy prerequisite: `從缺`
- Legacy next: `-`
- Runtime file: `skill/m/mount.ski`
- Runtime slot: `SLOT_MOUNT`
- Runtime key: `mount`
- Type: `TAR_MOUNT`
- Cost / Wait: `15 / 10`
- CostType / Weapon / Check: `COST_MOVE / - / -`
- CanAsk / Teach / Valid / Enable: `Yes / No / Yes / No`
- Class limits: `伶 人 >= 一級, max 一代宗師﹗; 刺 客 >= 一級, max 一代宗師﹗; 平 民 >= 一級, max 一代宗師﹗; 郎 中 >= 一級, max 一代宗師﹗; 武 官 >= 一級, max 一代宗師﹗; 將 軍 >= 一級, max 一代宗師﹗; 天 師 >= 一級, max 一代宗師﹗; 文 官 >= 一級, max 一代宗師﹗; 道 士 >= 一級, max 一代宗師﹗; 鑄劍師 >= 一級, max 一代宗師﹗; 盜 賊 >= 一級, max 一代宗師﹗`
- Restrictions: `-`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/skill.html`

