# Rebuild Workflow

這份參考檔說明 `plans/`、`area/rebuild_plan.md` 與固定 prompt 的配合方式。

## Purpose

- 支援長期、分多輪完成的 AREA 重建
- 讓代理可以用固定 prompt 持續接續工作
- 把 roadmap 與日常待辦拆開管理

## File Roles

- `plans/NNNN-topic-slug.md`
  - 全局計畫
  - 保存長期策略、候選排序、總體規則
- `plans/area/NNNN-area-slug.md`
  - 單一 area 的實作計畫
  - 保存該區的 spec、world links、分群、驗證目標
- `area/rebuild_plan.md`
  - 日常追蹤看板
  - 保存 `todo / in_progress / done / blocked / next_action`
- `area/world_map.md`
  - 世界層規劃依據
  - 幫助決定新 area 應該接在哪個母城或世界節點

## Naming Rules

- 全局計畫：`plans/NNNN-topic-slug.md`
- 單區計畫：`plans/area/NNNN-area-slug.md`
- `NNNN` 固定 4 碼
- 編號跨分類遞增，不重用

## Fixed Prompt

固定主 prompt：

`繼續實作下一個待建 area`

使用規則：

1. 先讀 `area/rebuild_plan.md`
2. 若有 `in_progress`，優先續做
3. 否則選第一個 `todo` 且無 blocker 的 area
4. 再讀對應的 `plans/area/NNNN-*.md`
5. 若需要世界層脈絡，再讀 `area/world_map.md`

## Update Rules

每次完成一輪 area 工作後，都要同步回寫 `area/rebuild_plan.md`：

- 更新 status
- 更新 next_action
- 將完成項移到 `done`，或把問題移到 `blocked`
- 補上下一個推薦 area 或下一個推薦 prompt

## Recommended Reporting

若任務來自這套長期流程，回報時應多補三件事：

- 目前 area 狀態是否已更新到追蹤看板
- 下一個推薦 area 是哪個
- 固定 prompt 下次會接到哪份單區計畫
