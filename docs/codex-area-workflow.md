---
layout: default
title: Codex Area Workflow
---

# Codex Area Workflow

這份文件整理 Codex 在本 repo 內執行 area rebuild 任務時的固定工作節奏，重點不是 area 設計本身，而是「每輪先讀什麼、一次做多大、何時停、何時 commit、何時更新 tracker」。

area 設計規則與驗證總覽仍以 [AREA 開發手冊](./area-development-handbook.html) 為主；這份文件偏向 agent 操作守則。

## Before You Touch Files

若任務涉及 existing/new area、maps、`.roo`、world links 或 area planning，先讀：

1. `AGENTS.md`
2. `area/rebuild_plan.md`
3. 對應 `plans/area/NNNN-*.md`
4. 需要時再讀 `plans/0001-world-map-area-rebuild.md`
5. 需要 world / template context 時再讀 `ref/Readme.md`

若是 runtime area work，再補看：

- `area/directory.lst`
- 目標 area 目錄
- `src/load.c`
- `src/act_move.c`

## Fixed Prompt Semantics

固定主 prompt：

`繼續實作下一個待建 area`

這句話在本 workflow 內的正確解讀是：

- 先看 `area/rebuild_plan.md`
- 有 `in_progress` 就續做該區
- 沒有 `in_progress` 才去取第一個可做的 `todo`
- `next area` 是 next actionable area，不是 candidate order 的下一個新名字

## Unit Of Work

預設一次只做一個 area milestone。

允許：

- 同一 area 的 spec 與 runtime 連動修改
- 同一 area 所需的 boundary room、`directory.lst` 與 docs 連動修改

不建議：

- 同一輪同時推進兩個不同 area 的主要 runtime 變更
- 因為卡住一區就順手開下一區

## Branch Rules

若目前在 `develop` 或 `main`，且下一步是從 `todo` 啟動一個新的 area milestone，預設先切 `codex/<area>-implementation`。

例外：

- 若目前 area 已經 `in_progress`，就在當前工作分支續做
- 若只是小型 docs / tracker / plan 收尾，可留在原分支
- 若使用者明講指定 branch 策略，以使用者指示為準

## While Working

每輪至少持續維持三件事：

- 單區 plan 與實作內容不要漂離
- `delivery_gate` 要和實際進度一致
- 本輪決策要能回寫到正確地方，而不是只留在聊天上下文

若用到 `ref/Readme.md` 做選讀決策，記得補：

- `ref_inputs_used`
- `ref_inputs_deferred`
- `theme_basis`
- `compliance_check`

## When To Stop And Ask

預設能自己判斷就自己往前做，但遇到下列情況應停下：

- 世界拓樸要改，但單區 plan 與現有 world graph 明顯衝突
- 決策會影響多個既有 area，且不是單純 boundary patch
- blocker 需要產品 / 世界觀 / 使用者偏好選邊
- 發現工作樹裡有直接衝突的未知修改，無法安全合併

若只是一般 loader / parser / VNUM 問題，應先自行排查，不要太早中斷。

## Commit Rules

commit 與 review 的最小單位，預設是單一 area milestone。

這表示：

- 同一次 commit 盡量只包含一個 area 的主要 spec 或 implementation 變更
- 同 area 所需的邊界房、`directory.lst`、tracker、docs 連動修改可一併納入
- 純全局 docs / workflow 補強可以獨立成 docs commit

若 `delivery_gate` 是：

- `spec_ready_for_commit`
  - 先 commit
- `implementation_ready_for_commit`
  - 先 commit
- `validated_ready_to_advance`
  - 可結束當前區，再交棒下一區

## Validation Rhythm

依任務類型決定驗證成本：

- `spec / plan / tracker only`
  - 通常跑 `--validate-only` 即可
- `area data only`
  - 優先本機 build + smoke test
- 涉及 `src/`、`Makefile*`、`startup*`、`merc.sample.ini` 或平台差異
  - 再升級到更高成本驗證

不要把 docs-only 或 spec-only 任務一律升級成重 build。

## Required Closeout

每輪結束前，至少做：

1. 更新 `area/rebuild_plan.md`
2. 視需要更新單區 plan
3. 視需要更新 `docs/current-game/areas.*`
4. 判斷要不要做經驗回寫
5. 檢查 `delivery_gate` 是否與實際狀態一致

## Relationship To Other Docs

- 流程總覽： [docs/area-development-handbook.md](./area-development-handbook.html)
- gate 定義： [docs/area-delivery-gates.md](./area-delivery-gates.html)
- 驗收清單： [docs/area-acceptance-checklist.md](./area-acceptance-checklist.html)
- 全局規則： `plans/0001-world-map-area-rebuild.md`
