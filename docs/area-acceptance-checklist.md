---
layout: default
title: Area Acceptance Checklist
---

# Area Acceptance Checklist

這份文件整理新 AREA 在不同里程碑下的最小驗收清單，目標是讓 `implementation_ready_for_commit` 與 `validated_ready_to_advance` 有一致的判準。

總覽仍以 [AREA 開發手冊](./area-development-handbook.html) 與 [Area Delivery Gates](./area-delivery-gates.html) 為準；這份文件專注在 checklist。

## Spec Milestone Checklist

當一個 area 要從 `spec_in_progress` 進到 `spec_ready_for_commit`，至少確認：

- 對應 `plans/area/NNNN-*.md` 已存在且可回讀
- `theme`、`subtheme`、`reserved_room_block`、`planned_vnum_range`、`external_links` 已寫明
- `ref_inputs_used`、`ref_inputs_deferred`、`theme_basis`、`compliance_check` 已補齊
- `area/<area>/map.md` 已存在
- `mapmd-json` 可通過 `--validate-only`
- 若有 planned world link 或 external exit，語意已分清楚

## Implementation Milestone Checklist

當一個 area 要從 `implementation_in_progress` 進到 `implementation_ready_for_commit`，至少確認：

- 已產生第一批 `.roo`
- `index` 已存在且核心欄位正確
- 最小 `mob / obj / res / shp` 已落地，或明確標示本輪刻意 deferred 的部分
- 若有 `mob/*.mob`，`Name` 已維持必填、command-facing 的英文或 ASCII-friendly 關鍵字，而不是純中文顯示名
- 若有 `mob/*.mob`，`Level` 已同時符合 loader hard gate `1..120` 與新建 area authoring cap `<=100`；若有 `>100`，預設仍視為未完成修正
- 若有 external exit，既有 boundary room 已同步 patch
- 若 area 已可載入，`area/directory.lst` 已同步
- 新 area 預設 `Capital 0` 的判斷沒有被誤改

## Runtime Validation Checklist

只要這輪已改到 loadable runtime area data，至少確認：

- VNUM 與 boundary links 已檢查
- `index / mob / obj / res / shp / roo` 一致性已檢查
- `area/directory.lst` 順序已檢查
- 已做對應 build
- 已做 smoke test
- 已找到明確成功訊號
- 已檢查本輪 `log/*`
- 已檢查本輪 `debug/*`

## Debug And Loader Checklist

若本輪做了 runtime area work，額外確認：

- `debug/*` 已在測試前清空或 baseline
- `Load_room`、parse error、duplicate vnum、reset 錯誤皆已排除
- 若本輪有改 `mob/*.mob`，已排除 `Load_mobiles﹕怪物 %d 沒有名字。` 與 `Load_mobiles﹕怪物 %d 等級 %d 不合理。`
- 若本輪有改 `obj/*.obj`，已檢查 `debug/badobject`
- 若本輪有改 `mob/*.mob` 的 `AutoEnable` / `Enable`，已檢查 `debug/failenable`
- 若有新的 area-related warning / error，未修完前不宣告通過

## Docs And Tracker Checklist

在宣告里程碑完成前，至少確認：

- `area/rebuild_plan.md` 已更新 status、`next_action`、`next_prompt`、`delivery_gate`
- 單區 plan 已回寫本輪重要決策
- 若 runtime area registry 真正變動，已更新 `docs/current-game/areas.md` 與 `docs/current-game/areas.json`
- 若本輪踩出新的可重用規則，已決定要回寫到單區 plan、tracker、skill reference 或全局 plan

## Ready-For-Commit Checklist

要推進到 `spec_ready_for_commit` 或 `implementation_ready_for_commit` 前，再做一次簡短自查：

- 這輪產出是否能被下一個人直接接手
- 還有沒有未寫回文件的隱性假設
- commit 是否能維持單一 area milestone 為單位
- 若現在切到下一區，是否會讓當前 area 變成難以回溯的半完成狀態

只要其中一項答案偏向「會」，就不應急著宣告 ready。

## Ready-To-Advance Checklist

只有同時滿足下列條件，才適合標成 `validated_ready_to_advance`：

- 本輪該做的 spec 與 runtime 變更都已完成
- 驗證證據完整
- tracker 已回寫
- 沒有 blocker
- 下次固定 prompt 進入下一區時，不會因為本區遺漏而被迫回頭補洞

## Relationship To Other Docs

- 流程總覽： [docs/area-development-handbook.md](./area-development-handbook.html)
- gate 語意： [docs/area-delivery-gates.md](./area-delivery-gates.html)
- agent 節奏： [docs/codex-area-workflow.md](./codex-area-workflow.html)
