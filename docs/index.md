---
layout: default
title: Merc FJU 3.0 Docs
---

# Merc FJU 3.0 Current Game

這個 GitHub Pages 站台用來放目前 `merc-fju-3.0` repo 的現行版本文件，作為 `docs/current-game/` 的統一入口，不直接承接舊版官網鏡像內容。

## Current Game

- [AREA 開發手冊](./area-development-handbook.html)
- [AREA Delivery Gates](./area-delivery-gates.html)
- [AREA VNUM Policy](./area-vnum-policy.html)
- [AREA External Exit Policy](./area-external-exit-policy.html)
- [AREA Acceptance Checklist](./area-acceptance-checklist.html)
- [Codex AREA Workflow](./codex-area-workflow.html)
- [AREA / Skill 資料系統化評估](./area-data-systemization-assessment.html)
- [Current Game 首頁](./current-game/)
- [技能補充說明](./current-game/skills.html)
- [Legacy `document/` 參考手冊入口](./current-game/legacy-documentation.html)
- [`document/README` 導讀](./current-game/legacy-readme.html)
- [`.mob` 怪物檔格式說明](./current-game/mobile-file-format.html)
- [`.obj` 物品檔格式說明](./current-game/object-file-format.html)
- [`.roo` 房間檔格式說明](./current-game/room-file-format.html)
- [`.res` 重置檔格式說明](./current-game/reset-file-format.html)
- [`.shp` 商店檔格式說明](./current-game/shop-file-format.html)
- [`index` 區域標題檔格式說明](./current-game/title-file-format.html)
- [Legacy 版權宣告](./current-game/copyright-notice.html)
- [`.ski` 技能檔格式說明](./current-game/skill-file-format.html)
- [`.ski` 進階 Loader Reference](./current-game/skill-loader-reference.html)
- [`.ski` 常數查表](./current-game/skill-constants.html)
- [`.ski` `pry` 文案對照](./current-game/skill-pry-crosswalk.html)
- [技能可讀總覽](./current-game/skills-index.html)
- [技能分類子頁](./current-game/skills/step.html)
- [技能機器可讀台帳](./current-game/skills.json)
- [技能戰鬥鏈審計說明](./current-game/skill-combat-audit.html)
- [Quest / Question 補充說明](./current-game/quests.html)
- [Quest / Question 機器可讀台帳](./current-game/quests.json)
- [Area 補充說明](./current-game/areas.html)
- [Area 機器可讀台帳](./current-game/areas.json)

## Legacy Reference

- 舊版官網已獨立發佈在 [3y.jakeuj.com](https://3y.jakeuj.com/)
- repo 內的 `docs/3yWebsite/` 保留作為開發參考鏡像，不作為這個 Pages 站台的主內容

## Source Of Truth

若是目前版本真正會影響遊戲載入與 NPC 表現的資料，仍以 repo 內 runtime 檔案為準：

- `skill/*.ski`
- `skill/skill.lst`
- `src/merc.h`
- `data/symbol.def`
- `area/*`

Pages 站台中的 `docs/current-game/` 只負責補充說明與開發者索引。
