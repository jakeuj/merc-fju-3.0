---
layout: default
title: Area Delivery Gates
---

# Area Delivery Gates

這份文件把 AREA rebuild workflow 的 `delivery_gate` 語意獨立整理，避免 agent 或人類協作者在單區尚未完成時誤跳到下一區。

總覽仍以 [AREA 開發手冊](./area-development-handbook.html) 與 `plans/0001-world-map-area-rebuild.md` 為準；這份文件只負責 gate 定義、決策規則與最小證據要求。

## Gate Values

固定使用下列值：

- `spec_in_progress`
- `spec_ready_for_commit`
- `implementation_in_progress`
- `implementation_ready_for_commit`
- `validated_ready_to_advance`
- `blocked`

不要自創同義值，例如 `spec_done`、`ready`、`pending_commit`。

## Gate Definitions

### `spec_in_progress`

表示目前仍在整理下列任一項：

- `plans/area/*.md`
- `area/<area>/map.md`
- 題材與 cluster 設計
- `reserved_room_block`
- `planned_vnum_range`
- `external_links`

這個狀態下不得宣告該區可進入下一區。

### `spec_ready_for_commit`

表示 spec 已形成穩定里程碑，通常至少具備：

- 單區 plan 已可回讀
- `map.md` 與 `mapmd-json` 已可驗證
- `external_links` 與 boundary assumptions 已明確
- ref metadata 已補齊

這個狀態的下一步是先 commit，而不是直接開始另一個 area。

### `implementation_in_progress`

表示已開始落地 runtime data，例如：

- `.roo`
- `index`
- `mob / obj / res / shp`
- `area/directory.lst`
- 既有 boundary room patch

這個狀態下仍屬於同一個 area milestone，應續做當前 area。

### `implementation_ready_for_commit`

表示本輪 runtime data 已形成穩定里程碑，通常至少具備：

- 新 area 自身資料已達到最小可載入集合
- boundary room 與 `area/directory.lst` 同步完成
- 已完成本輪必要驗證
- 無待處理 blocker

這個狀態的下一步仍然是先 commit。

### `validated_ready_to_advance`

表示當前 area 已完成本輪應做的驗證，且可以安全交棒到下一個 actionable area。

通常至少包含：

- 對應 build 結果
- smoke test 成功訊號
- `log/*` 與 `debug/*` 已檢查
- tracker 與單區 plan 已回寫

只有這個狀態才適合配合固定 prompt 前進下一區。

### `blocked`

表示目前有 blocker，無法安全推進。

常見 blocker：

- `Load_room` / parse error / duplicate vnum
- boundary link 未定案
- VNUM 衝突未解
- 需要使用者或世界層決策才能繼續

這個狀態下不得把「改做下一區」當成替代方案。

## Decision Matrix

看到 gate 時，預設行為如下：

- `spec_in_progress`
  - 續做當前 area 的 spec
- `spec_ready_for_commit`
  - 先 commit 當前里程碑
- `implementation_in_progress`
  - 續做當前 area 的 runtime 落地與驗證
- `implementation_ready_for_commit`
  - 先 commit 當前里程碑
- `validated_ready_to_advance`
  - 才可前進下一個 actionable area
- `blocked`
  - 先解 blocker 或把阻塞條件寫清楚

## Minimum Evidence By Gate

### Spec Gates

`spec_in_progress` 到 `spec_ready_for_commit` 至少要能回答：

- 這區要接到哪裡
- 保留哪段房號
- 主題與 subtheme 是什麼
- `mapmd-json` 是否已可通過 `--validate-only`
- 這輪用了哪些 `ref/` 輸入

### Implementation Gates

`implementation_in_progress` 到 `implementation_ready_for_commit` 至少要能回答：

- 哪些 runtime 檔已落地
- 既有 boundary room 是否已同步
- `area/directory.lst` 是否已同步
- 驗證用了哪個 build / smoke test / log / debug

### Advance Gate

`validated_ready_to_advance` 除了 implementation evidence 外，還應加上：

- 本輪沒有待處理 blocker
- tracker 已更新到可交棒狀態
- 下次固定 prompt 會落到哪一區可被說明

## Tracker Rules

`area/rebuild_plan.md` 中每個 `todo` 或 `in_progress` area 都應標示 `delivery_gate`。

同步規則：

- 當前工作完成一輪後，更新 `delivery_gate`
- 若 gate 從 `*_in_progress` 進到 `*_ready_for_commit`，不要同時把 area 偷偷移到下一區
- 若 area 已達 `validated_ready_to_advance`，再由 tracker 決定下一個 actionable area
- 若遇到 blocker，將原因寫進 tracker 與單區 plan，而不是只在 commit 訊息或聊天中提到

## Forbidden Moves

下列行為視為違反 gate discipline：

- `spec_ready_for_commit` 還沒 commit 就直接切到下一區
- `implementation_ready_for_commit` 還沒 commit 就開另一個 area
- `blocked` 狀態下改做下一區當替代方案
- generator 成功但未驗 loader / boundary / `directory.lst` 就宣告 `validated_ready_to_advance`
- tracker 還寫 `in_progress`，卻口頭把下一區當作現在的 target

## Relationship To Other Docs

- 流程總覽： [docs/area-development-handbook.md](./area-development-handbook.html)
- 全局規則： `plans/0001-world-map-area-rebuild.md`
- 日常狀態： `area/rebuild_plan.md`
- Agent 執行節奏： [docs/codex-area-workflow.md](./codex-area-workflow.html)
