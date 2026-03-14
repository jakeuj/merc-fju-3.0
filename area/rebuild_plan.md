# Area Rebuild Tracker

這份檔案是 area 重建的日常追蹤看板，配合 `plans/` 內的正式計畫一起使用。

## Delivery Gate Rules

- 每個 `in_progress` 或 `todo` area 都應標示 `delivery_gate`
- `delivery_gate: spec_ready_for_commit` 或 `implementation_ready_for_commit`
  - 表示本輪應先 commit，不要跳到下一個 area
- `delivery_gate: validated_ready_to_advance`
  - 表示當前 area 已可結束，這時才適合使用固定 prompt 進下一區
- `delivery_gate: spec_in_progress` 或 `implementation_in_progress`
  - 表示仍應續做當前 area
- `delivery_gate: blocked`
  - 表示先解 blocker，不得把「做下一區」當成替代方案

## Smoke Test Hygiene

- 若本輪要做 area 載入或啟動 smoke test，先清空 `debug/*` 內容
- 開始測試前，也要先建立本輪 `log/*` 觀察基線；不一定要整批清空 `log/`，但至少要能明確指出這輪要看的新 log
- 若使用 `timeout` 做 smoke test，優先給 `45` 到 `60` 秒，避免因測試工具過早中止而誤判啟動失敗
- 成功不能只看 process 暫時存活；至少要確認啟動輸出或 log 內有像 `三國歪傳之降龍伏虎開始正常運作` 這類明確成功訊號
- 即使已看到成功訊號，仍要回頭檢查 `debug/*` 是否出現本次新增 area 相關的新錯誤或警告
- 之後也要補看本輪 log 是否有 area 相關 warning / error
- 只有在上述檢查都完成後，才可把 `delivery_gate` 推進到 `implementation_ready_for_commit` 或 `validated_ready_to_advance`

## References

- 全局計畫：`plans/0001-world-map-area-rebuild.md`
- 單區計畫：`plans/area/0002-loyang-outskirts.md`、`plans/area/0003-beiping-outskirts.md`、`plans/area/0004-jingxiang-road.md`
- 世界圖參考：`area/world_map.md`
- ref 索引：`ref/Readme.md`

## Fixed Prompt

日後延續工作使用固定主 prompt：

`繼續實作下一個待建 area`

執行規則：

- 若 `in_progress` 區塊有項目，優先續做該區
- 否則從 `todo` 區塊選第一個沒有 blocker 的 area
- 若當前區塊完成，更新本檔後再移動到下一區
- 這套流程中的 `next area` 指的是 next actionable area，不是 candidate queue 的下一個新名字
- 因此只要仍存在 `in_progress` 項目，就不得跳去下一個 `todo`；除非目前區域已明確標成 `done`、`blocked` 或 `abandoned`
- 若使用者只說「繼續下一個 area / next area」，預設語意仍是「續做目前可執行的 area」，不是直接切換到候選序列的下一個新區
- 每次從 `todo` 推進到 `in_progress`，或完成一輪單區實作後，都要同步檢查對應單區 plan 是否已補上 `ref_inputs_used / ref_inputs_deferred / theme_basis / compliance_check`

## Candidate Queue

1. `jingxiang_road`

## Todo

(目前無待處理 `todo`；先完成 `in_progress` 的 `jingxiang_road`。)

## In Progress

### `jingxiang_road`

- status: `in_progress`
- delivery_gate: `spec_ready_for_commit`
- compliance_check: `compliant with current ref/Readme.md scope`
- plan: `plans/area/0004-jingxiang-road.md`
- parent_region: `future regional chain`
- theme: `江湖風`
- subtheme: `軍旅風`
- world_links: `襄陽`, `新野`, `江夏`, `荊襄大道`
- next_action: 先 commit `jingxiang_road` 的單區 plan + map.md spec 里程碑；commit 後再決定是否進入 implementation（index/mob/obj/res/shp）
- next_prompt: `先 commit 目前 jingxiang_road 的 spec 里程碑；commit 後若要落地 runtime 資產，再續做 jingxiang_road implementation。`
- notes: `plans/area/0004-jingxiang-road.md` 與 `area/jingxiang_road/map.md` 第一版已建立，`mapmd-json` 可通過 scaffold validator


## Done

- `area/world_map.md` 已建立，並整合 `help/map.hlp`、`docs/3yWebsite/docs/maps.md`、`docs/3yWebsite/docs/data/maps.json`、`docs/3yWebsite/map/*.html`
- `plans/0001-world-map-area-rebuild.md` 已建立
- `plans/area/0002-loyang-outskirts.md` 已建立
- `loyang_outskirts` 已完成第一輪整合並進入可前進下一區狀態
- `plans/area/0003-beiping-outskirts.md` 已建立
- `beiping_outskirts` 已完成第一輪整合與 smoke test 驗證，`delivery_gate` 達到 `validated_ready_to_advance`

## Blocked

- none

## Current Recommended Next Step

先 commit 目前 `jingxiang_road` 的 spec 里程碑（plan + map.md）；commit 後再決定是否進 implementation。

語意提醒：

- 目前的 next actionable area 仍是 `jingxiang_road`
- 目前 `delivery_gate` 是 `spec_ready_for_commit`，本輪安全動作是先 commit，不跳下一區
- `beiping_outskirts` 已完成並驗證，可由 `Done` 歷程回查

建議可直接使用的 prompt：

`先 commit 目前 jingxiang_road 的 spec 里程碑；commit 後若要落地 runtime 資產，再續做 jingxiang_road implementation。`
