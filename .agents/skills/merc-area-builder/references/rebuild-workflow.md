# Rebuild Workflow

這份參考檔說明 `plans/`、`area/rebuild_plan.md` 與固定 prompt 的配合方式。

## Purpose

- 支援長期、分多輪完成的 AREA 重建
- 讓代理可以用固定 prompt 持續接續工作
- 把 roadmap 與日常待辦拆開管理

## File Roles

- `docs/area-development-handbook.md`
  - workflow 的正式人類可讀入口
  - 先整理 source-of-truth、七層 pipeline、驗證層級與 companion docs
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

## Workflow Docs And Tooling

- 若任務是在建立新 area workflow、起草新 plan、或幫別人接手這套流程，先讀 `docs/area-development-handbook.md`
- 需要更細的流程切片時，再按需讀：
  - `docs/area-delivery-gates.md`
  - `docs/area-vnum-policy.md`
  - `docs/area-external-exit-policy.md`
  - `docs/area-acceptance-checklist.md`
  - `docs/codex-area-workflow.md`
- 新 area 起手時，可直接用：
  - `templates/area-plan.template.md`
  - `templates/map.md.template`
  - `templates/area-readme.template.md`
  - `templates/new-area-checklist.template.md`
- 現有 workflow 輔助工具：
  - `tools/mapmd_validate.py`
  - `tools/area_vnum_allocator.py`
  - `tools/log_parse_summary.py`
  - `tools/area_acceptance_gate.py`

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

## Level Band Governance

- area rebuild 的正式平衡上限是 `1..100`；不要把 loader 的 `1..120` 容忍範圍誤當成新建 area 的 authoring 空間
- `95..100` 視為 plateau endgame band；若未來還要向下延伸新的 endgame layer，應靠 encounter 結構、資源壓力、抗性與路線壓迫加強，而不是讓怪物等級超過 `100`
- 單區 plan 的 `level_range`、`map.md` 的 `LevelRange`、`mapmd-json.area.level_range` 必須一致
- 若 area 已有 runtime `mob/*.mob` 或 `content.json`，應再和實際怪物等級、`balance_metadata.planned_level_range` 對齊

## Branch Gate Rules

固定 prompt 除了要看 `delivery_gate`，也要看目前所在 branch 是否適合承接新的 area milestone。

決策規則：

1. 若目前在 `develop` 或 `main`，且這次要從 `todo` 啟動一個新的 area milestone，預設先建立 `codex/<area>-implementation` 分支，再開始 spec / implementation
2. 若目前 area 已經是 `in_progress`，則優先留在當前工作分支續做，不要為了同一區中途再切新 branch
3. 若這輪只是 merge 後的小型 `docs / tracker / plan` 收尾，可留在 `develop`
4. 若使用者明講「直接在 develop 做」或指定其他 branch 策略，依使用者指示覆蓋預設規則

目的：

- 避免固定 prompt 在 `develop` 上直接累積一長串新 area 實作 commit
- 讓每一段 area milestone 更容易整批 merge / review / rollback
- 把「是否該先切分支」制度化，而不是靠當輪臨時記憶

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

## Historical External References

若 `world_map`、`ref/`、`players.json`、`skills.json` 仍不足以回答歷史 rebuild-era 的 area 優先序、等級帶、城市規模或技能重設節奏，可以補充使用外部歷史資料，例如：

- `references/rebuildnote-2011-progress.md`
- `references/community-leveling-baseline.md`

使用規則：

1. 這類資料只當 supplemental historical evidence，不得覆蓋 repo 內既有 source of truth
2. 若真的採用，單區 plan / tracker 的 `ref_inputs_used` 要記精確 URL 與日期
3. 若有查但刻意不採用，也可寫進 `ref_inputs_deferred` 或 `compliance_check`
4. 特別適合拿來回答：
   - 這個城市 historically 可能做到多大
   - 這個 level band 是否曾有 rebuild-era 先例
   - 是否值得先投資 generator / scaffold 再擴寫大城
   - 技能數值調整應該一次定版，還是分批實測
5. 若外部來源是玩家社群的 leveling 文，而不是 admin / rebuild note，預設只把它當 `level_range` 與玩家體感順序的 sanity check，不當成世界主線權威

## Update Rules

每次完成一輪 area 工作後，都要同步回寫 `area/rebuild_plan.md`：

- 更新 status
- 更新 next_action
- 更新 next_prompt
- 更新 delivery_gate
- 將完成項移到 `done`，或把問題移到 `blocked`
- 補上下一個推薦 area 或下一個推薦 prompt

此外，收尾時要額外做一次「經驗回寫判斷」，避免同類問題反覆重踩：

- 若問題只屬於當前 area 的 world link、題材決策、reserved block、deferred item 或特殊 blocker，回寫單區 plan 與 tracker
- 若問題屬於 repo 現實中的 parser / loader / data-format / smoke-test 規則，而且未來同類 area 高機率再遇到，回寫到對應的 `skills/references`
- 若問題暴露的是固定 prompt、branch 策略、delivery gate、驗證節奏等全局流程缺口，回寫到全局 plan 或本檔
- 若只是一次性的 typo、局部內容修稿或不具可重用性的偶發失誤，可不必擴寫成長期規則

## Integration Checklist For A New Area

當一個新 AREA 從 spec 要走到真正可載入時，建議固定照下面順序：

1. 完成 `plans/area/NNNN-*.md`
2. 完成 `area/<new_area>/map.md`
3. 先跑 `tools/mapmd_validate.py` 做摘要驗證
   - 這一步除了房號 / world link / cluster，也應確認 `LevelRange`、`mapmd-json.area.level_range`、runtime mob level 與 `content.json` 的 `planned_level_range` 沒有 drift
4. 再用 generator `--validate-only`
5. 產生第一批 `.roo`
6. 補 `index`
7. 補最小 `mob / obj / res / shp`
8. 若要接到既有主城或既有房號，先在 `mapmd-json` 標示 external exit
9. 再把邊界出口同步改到既有 area 的 `.roo`
10. 掛入 `area/directory.lst`
11. 先清空 `debug/*` 內容
12. 先建立本輪 `log/*` 觀察基線，例如記下最新 log 檔名，或清空這輪要看的單一 log
13. 做本機 smoke test；若使用 `timeout`，優先給 `45` 到 `60` 秒
14. 用 `tools/log_parse_summary.py` 摘要成功訊號與 `debug/*`
15. 視需要用 `tools/area_acceptance_gate.py` 取保守 gate 建議
16. 確認啟動輸出或本輪 log 中有像 `三國歪傳之降龍伏虎開始正常運作` 這類成功訊號
17. 再回頭檢查 `debug/*` 是否留下和本次新增 area 相關的新錯誤或警告，並補看本輪 log 是否有 area warning / error
18. smoke test 成功後，把 `delivery_gate` 推到 `implementation_ready_for_commit` 或更高狀態

## Notes From The First Real Case

`loyang_outskirts` 是這套流程的第一個正式驗證案例，實際踩出的規則如下：

- external exit 是必要需求，不是可有可無的 enhancement
- `.res` parser 可能比文件更保守，遇到 parse error 時優先比對 repo 內既有成功範例
- `debug/bugs` 可能殘留舊錯誤；啟動是否成功要以最新啟動輸出和 log 內是否出現「開始正常運作」為準
- 若測試前有先清空 `debug/*`，那麼測試後的 `debug/*` 訊息就應視為本輪新增訊號，不能再用「歷史殘留」理由忽略
- `log/*` 不一定要整批清空，但至少要先建立本輪觀察基線，避免把舊 log 和這輪結果混在一起
- 若 `timeout` 太短，常會在人已經看到成功訊號後仍留下「系統不正常終止」這種測試噪音；timeout 應高於正常開機時間

## Recommended Reporting

若任務來自這套長期流程，回報時應多補三件事：

- 目前 area 狀態是否已更新到追蹤看板
- 下一個推薦 area 是哪個
- 固定 prompt 下次會接到哪份單區計畫
