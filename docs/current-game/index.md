---
layout: default
title: Current Game Docs
---

# Current Game Docs

這一區專門記錄目前版本新遊戲的補充文件，和舊版參考站分開維護；目前以技能與 area 兩組現行 runtime 補充台帳為主。

## 目前已有內容

- [技能補充說明](./skills.html)
- [Legacy `document/` 參考手冊入口](./legacy-documentation.html)
- [`document/README` 導讀](./legacy-readme.html)
- [`.mob` 怪物檔格式說明](./mobile-file-format.html)
- [`.obj` 物品檔格式說明](./object-file-format.html)
- [`.roo` 房間檔格式說明](./room-file-format.html)
- [`.res` 重置檔格式說明](./reset-file-format.html)
- [`.shp` 商店檔格式說明](./shop-file-format.html)
- [`index` 區域標題檔格式說明](./title-file-format.html)
- [Legacy 版權宣告](./copyright-notice.html)
- [`.ski` 技能檔格式說明](./skill-file-format.html)
- [`.ski` 進階 Loader Reference](./skill-loader-reference.html)
- [`.ski` 常數查表](./skill-constants.html)
- [`.ski` `pry` 文案對照](./skill-pry-crosswalk.html)
- [技能可讀總覽](./skills-index.html)
- [技能分類子頁](./skills/step.html)
- [技能機器可讀台帳](./skills.json)
- [技能戰鬥鏈審計說明](./skill-combat-audit.html)
- [技能戰鬥鏈審計台帳](./skill-combat-audit.json)
- [Quest / Question 補充說明](./quests.html)
- [Quest / Question 機器可讀台帳](./quests.json)
- [Area 補充說明](./areas.html)
- [Area 機器可讀台帳](./areas.json)

## 文件邊界

- 這裡記錄的是目前 repo 額外補上的現行資料與設計決策。
- 舊版技能脈絡、公告、世界觀語彙與歷史內容，改查 [3y.jakeuj.com](https://3y.jakeuj.com/) 或 repo 內 `docs/3yWebsite/` 鏡像。
- area 世界規劃、重建追蹤與單區 spec 仍以 repo 內的 `area/world_map.md`、`area/rebuild_plan.md`、`plans/area/*.md` 為主；這裡只放 Pages 版補充索引。
- 若未來新增更多現行版本文件，優先放在 `docs/current-game/`，不要直接混寫到舊站鏡像。
- 可讀型技能頁目前由 `scripts/generate_current_game_skills_pages.py` 從 `skills.json` 生成；目前已覆蓋舊站各葉節點分類，後續新增技能資料時優先沿用同一條生成流程。
- `document/*.txt` 這類 legacy authoring reference 若要補進 Pages，優先整理成 `docs/current-game/` 的可讀頁面，再從這裡掛入口。
