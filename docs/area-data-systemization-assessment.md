---
layout: default
title: Area Data Systemization Assessment
---

# Area Data Systemization Assessment

這份文件記錄目前 `plans/0001-world-map-area-rebuild.md` 的完成度評估，以及「是否改成資料庫方式管理 area / skill / balance 資料」的結論。

## Executive Summary

- 若看 `plans/0001-world-map-area-rebuild.md` 的核心目標，也就是讓 area rebuild 可以穩定續跑、可追蹤、可驗證，完成度約 `85%` 到 `90%`
- 若看整份計畫後段的 systemization roadmap，包含 template、schema、validation tooling、prompt/CI packaging 全部做滿，完成度約 `70%` 到 `75%`
- 目前最值得做的是「資料結構化」，但不建議直接把資料庫當成 runtime 與 Git workflow 的 primary source of truth
- 建議採用 `structured files -> generator/export -> legacy runtime files` 的模式，而不是直接 `database -> runtime`

## Completion Assessment For `plans/0001-world-map-area-rebuild.md`

### 已明確落地的部分

- 世界圖、tracker、單區 plan、`map.md` / `mapmd-json`、generator、runtime 驗證與 `delivery_gate` 已形成正式工作流
- `area/rebuild_plan.md` 已實際作為 next actionable area 的唯一日常追蹤入口
- 多個單區 milestone 已完成，流程已被反覆驗證，不是只靠第一個 sample case
- Stage 1 類型的人類可讀治理文件目前已存在：
  - `docs/area-development-handbook.md`
  - `docs/area-delivery-gates.md`
  - `docs/area-vnum-policy.md`
  - `docs/area-external-exit-policy.md`
  - `docs/area-acceptance-checklist.md`
  - `docs/codex-area-workflow.md`
- Stage 3 已有多個可用工具：
  - `tools/mapmd_validate.py`
  - `tools/area_vnum_allocator.py`
  - `tools/log_parse_summary.py`
  - `tools/area_acceptance_gate.py`

### 尚未完全做滿的部分

- Stage 2 的 template / schema 仍未完整成套落地
- Stage 3 仍缺較完整的 bootstrap / patch 建議器與更強的 world consistency 診斷
- Stage 4 的 prompt packaging、diff tooling、CI scripts 與 review packaging 尚未完成
- 技能、怪物、道具、商店與 reset 的「可批次調整資料模型」仍偏分散，尚未形成統一的結構化 source layer

## Current Runtime Reality

目前 repo 的現行 runtime source of truth 仍是 flat files，不是 database。

### Area

- `area/directory.lst`
- `area/<area>/index`
- `area/<area>/roo/*`
- `area/<area>/mob/*`
- `area/<area>/obj/*`
- `area/<area>/res/*`
- `area/<area>/shp/*`
- loader 主要在 `src/load.c` 與 `src/file.c`

### Skill

- `skill/skill.lst`
- `skill/<letter>/<name>.ski`
- runtime skill schema 對應 `src/load.c` 的 `load_skill()`
- 相關結構與常數在 `src/merc.h`、`data/symbol.def`
- 現行可回讀文件見：
  - `docs/current-game/skill-file-format.md`
  - `docs/current-game/skill-loader-reference.md`
  - `docs/current-game/skills.json`

這代表：如果直接改成 DB-first，真正要動到的不只是 authoring tooling，而是整個 loader contract 與 repo 的 review / diff 方式。

## Assessment: Should We Move To Database Management?

結論：**不建議目前直接改成資料庫作為 primary source of truth，但非常建議導入結構化中介資料層。**

### 為什麼不建議直接 DB-first

- 現有 runtime 明確吃 flat files，改 DB-first 代表要重寫 loader 或建立一條新的 boot contract
- area / skill 內容高度依賴 Git diff、review 與人眼比對，database 對這件事通常更差
- 單區 area rebuild 現在已經建立一套 `map.md -> roo -> runtime validation` 的穩定流程，直接換核心資料源風險高
- 若把 SQLite 或其他 DB 檔直接進 Git，merge conflict、review 可讀性與可追溯性通常都會變差

### 為什麼仍然要做資料結構化

- 技能平衡、怪物 tier、掉寶池、商店、teacher、reset 配置，本質上都很適合用結構化資料管理
- 結構化資料比較容易做：
  - 批次生成
  - 跨 area 一致性檢查
  - 平衡審計與報表
  - 大範圍數值調整
  - 程式化 export 到 legacy runtime files
- repo 其實已經部分走在這條路上：
  - `area/<area>/map.md` 內嵌 `mapmd-json`
  - `scripts/build_current_game_skill_registry.py`
  - `docs/current-game/skills.json`
  - `docs/current-game/areas.json`

## Recommended Direction

建議用三層模型，而不是直接把 DB 變成 loader input：

1. `Human-editable structured source`
   - Git-friendly 的 Markdown / JSON / YAML
   - 作為 area / skill / balance 的 canonical authoring layer
2. `Generator / exporter`
   - 把結構化資料投影成 runtime 需要的 flat files
3. `Legacy runtime files`
   - 維持 `area/*`、`skill/*.ski` 等目前 loader 真正吃的格式

### 對 area 的建議

- 空間拓樸與 world links 繼續以 `map.md + mapmd-json` 為主
- 另外新增 per-area 的結構化 content layer，負責：
  - mob roster
  - item/drop pool
  - shop inventory
  - reset / spawn group
  - area-level balance metadata
- 由工具生成 `mob / obj / res / shp` 草稿，保留人工 review 與微調空間

### 對 skill 的建議

- 優先做 skill 的 canonical structured registry
- 把 `.ski` 中與平衡、可教導性、資源消耗、職業限制、slot、weapon、damage profile 有關的欄位抽成明確 schema
- 再由 generator 產出 `.ski`
- 把平衡審計、crosswalk、family/category 分析直接建立在 structured registry 上

### 對資料庫的建議定位

如果未來真的要用 DB，建議把它放在以下角色，而不是當第一步：

- analysis cache
- 查詢 / dashboard backend
- build artifact
- 匯入 structured files 後的中間索引層

換句話說，較合理的順序是：

`structured files first -> export pipeline -> optional database later`

不是：

`database first -> 強迫 runtime / Git / review 全部改制`

## Expected Benefits Of The Recommended Approach

若採結構化 source layer，而不是直接 DB-first，仍可得到主要收益：

- 批次生成 area 房間周邊資料更快
- 批次生成怪物、物品、商店與 reset 更一致
- 技能平衡與跨區域 balance 調整更容易
- 可以逐步導入，不必一次重寫 loader
- 保留目前 flat-file runtime 的穩定性與相容性
- 對 Git diff、review 與回溯更友善

## Suggested Next Priorities

若要開始做 systemization，建議優先順序如下：

1. 先整理 skill 的 structured registry 與 `.ski` generator
2. 再整理 per-area content schema，覆蓋 mob / obj / shp / res
3. 補 balance audit / consistency report
4. 最後再評估是否需要 SQLite 或其他 DB 當分析層

原因：

- 技能平衡通常最容易受益於批次化與表格化
- area 拓樸目前已有 `mapmd-json`，比 skill 更不急著改核心表示法
- 等 structured source 與 generator 穩定後，再決定要不要加 DB，風險最低
