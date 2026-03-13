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
  - 保存 `todo / in_progress / done / blocked / next_action / next_prompt / delivery_gate`
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

語意規則：

- 這個 workflow 內的 `next area` 是 next actionable area，不是 candidate queue 的下一個新名稱
- 只要 `in_progress` 還存在，就不得切到下一個 `todo`
- 只有目前區域已明確轉成 `done`、`blocked` 或 `abandoned`，才可以往候選序列的下一區前進

## Delivery Gate Rules

`area/rebuild_plan.md` 應額外用 `delivery_gate` 告訴代理：現在該 commit、該續做，還是可前往下一區。

建議 gate：

- `spec_in_progress`
- `spec_ready_for_commit`
- `implementation_in_progress`
- `implementation_ready_for_commit`
- `validated_ready_to_advance`
- `blocked`

決策規則：

1. 若 gate 是 `spec_ready_for_commit` 或 `implementation_ready_for_commit`，先 commit
2. 若 gate 是 `validated_ready_to_advance`，才可進下一個 area
3. 若 gate 是任何 `*_in_progress`，就續做當前 area
4. 若 gate 是 `blocked`，先解 blocker

## Ref Compliance Check

若這輪 area 工作是透過 `ref/Readme.md` 來選擇 template、world blueprint 或 scaffold，則單區 plan 應補上：

- `ref_inputs_used`
- `ref_inputs_deferred`
- `theme_basis`
- `compliance_check`

目的：

- 明確標示這一輪真正採用的 `ref/` 依據
- 明確標示哪些 generator / editor prototype 或模擬系統是刻意 deferred
- 確保下一輪接手時，不會把超出本輪範圍的 `ref/` 原型誤當成正式依據

## Update Rules

每次完成一輪 area 工作後，都要同步回寫 `area/rebuild_plan.md`：

- 更新 status
- 更新 next_action
- 更新 next_prompt
- 更新 delivery_gate
- 將完成項移到 `done`，或把問題移到 `blocked`
- 補上下一個推薦 area 或下一個推薦 prompt

## Integration Checklist For A New Area

當一個新 AREA 從 spec 要走到真正可載入時，建議固定照下面順序：

1. 完成 `plans/area/NNNN-*.md`
2. 完成 `area/<new_area>/map.md`
3. 用 generator `--validate-only`
4. 產生第一批 `.roo`
5. 補 `index`
6. 補最小 `mob / obj / res / shp`
7. 若要接到既有主城或既有房號，先在 `mapmd-json` 標示 external exit
8. 再把邊界出口同步改到既有 area 的 `.roo`
9. 掛入 `area/directory.lst`
10. 先清空 `debug/*` 內容
11. 做本機 smoke test
12. 確認 log 或啟動輸出中有像 `三國歪傳之降龍伏虎開始正常運作` 這類成功訊號
13. 再回頭檢查 `debug/*` 是否留下和本次新增 area 相關的新錯誤或警告
14. smoke test 成功後，把 `delivery_gate` 推到 `implementation_ready_for_commit`

## Notes From The First Real Case

`loyang_outskirts` 是這套流程的第一個正式驗證案例，實際踩出的規則如下：

- external exit 是必要需求，不是可有可無的 enhancement
- `.res` parser 可能比文件更保守，遇到 parse error 時優先比對 repo 內既有成功範例
- `debug/bugs` 可能殘留舊錯誤；啟動是否成功要以最新啟動輸出和 log 內是否出現「開始正常運作」為準
- 若測試前有先清空 `debug/*`，那麼測試後的 `debug/*` 訊息就應視為本輪新增訊號，不能再用「歷史殘留」理由忽略

## Recommended Reporting

若任務來自這套長期流程，回報時應多補三件事：

- 目前 area 狀態是否已更新到追蹤看板
- 下一個推薦 area 是哪個
- 固定 prompt 下次會接到哪份單區計畫
