---
layout: default
title: Merc FJU 3.0 Docs
---

# Merc FJU 3.0 Current Game

這個 GitHub Pages 站台用來放目前 `merc-fju-3.0` repo 的現行版本文件，作為 `docs/current-game/` 的統一入口，不直接承接舊版官網鏡像內容。

## Current Game

- [Current Game 首頁](./current-game/)
- [技能補充說明](./current-game/skills.html)
- [技能機器可讀台帳](./current-game/skills.json)
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
