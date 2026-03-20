---
layout: default
title: Current Game 技能熟練度 Skills
---

# Current Game 其他技能 / 技能熟練度

這頁是 `docs/current-game/skills.json` 的 `其他技能 / 技能熟練度` 可讀版，將舊站鏈路、現行 runtime 與調整維度放在同一頁。

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
| legacy-page:learnlv | 技能的熟練度共分十二個等級 | 1 | legacy_reference_only |

## Skill Cards

## legacy-page:learnlv

Legacy chain: `技能的熟練度共分十二個等級`

### 技能的熟練度共分十二個等級 / `技能的熟練度共分十二個等級`

- Audit: `legacy_reference_only`
- Family: `legacy-page:learnlv`
- Legacy prerequisite: `-`
- Legacy next: `-`
- Runtime file: `-`
- Runtime slot: `-`
- Runtime key: `-`
- Type: `-`
- Cost / Wait: `- / -`
- CostType / Weapon / Check: `- / - / -`
- CanAsk / Teach / Valid / Enable: `- / - / - / -`
- Class limits: `-`
- Restrictions: `-`
- Damage values: `[]`
- Chance values: `[]`
- Parry values: `[]`
- Innate values: `[]`
- Legacy page source: `skill/learnlv.html`
- Notes: No runtime skill file matched yet; legacy requirements still preserved from old-site HTML.

