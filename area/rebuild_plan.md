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

## Room Block Rules

- 新 area 立項時，先記錄 `reserved_room_block`
- 未來新 area 的第一段 `reserved_room_block` 必須從某個 `xx01` 起跳
- `reserved_room_block` 大小依首版 area 規模浮動；用「預估房數 + 至少 `8` 格 headroom」後往上取到最近的 `10`
- `reserved_room_block` 以整十收尾，例如 `9501-9520`、`9601-9630`
- 若 `next_action` 包含建立新 area spec，先確認該 block 未與現有 `area/`、`src/`、`data/` 中已使用的 room vnum 衝突，且不要跨百位切段
- 第一版若只落地部分房間，`planned_vnum_range` 預設仍應反映整個首段保留 block
- 既有 area 後續擴充時，優先使用自己首段保留 block 內的剩餘房號
- 只有原首段保留 block 用完時，才允許新增第二段 extension block
- 若使用 extension block，必須同步記錄在 tracker、單區 plan 與 `map.md` metadata，避免後續維護時看不出房號來源
- `9451/9461/9481/9491` 這類地下鏈切段屬於舊流程遺留，保留現狀；未來新 area 不再沿用同一百位拆多區的做法

## Candidate Queue

1. `sec_rift_deeps`

## Todo

(目前無 `todo` 項目。)

## In Progress

- `sec_rift_deeps`
  - delivery_gate: `implementation_in_progress`
  - parent_region: `loyang underground chain`
  - reserved_room_block: `9701-9720`
  - theme: `仙俠`
  - subtheme: `裂界 / 深層封印`
  - ref_inputs_used: `ref/Readme.md`, `area/world_map.md`, `ref/world-graph.md`, `ref/三國-MUD-題材分布表.md`, `area/sec_rift_core/map.md`
  - ref_inputs_deferred: `ref/sanguo-area-scaffold/`, `mud-world-builder/`, `mud-ai-map-generator/`, `mudlet-map-generator/`, `mud-world-map-editor/`, `mud-world-map-editor-pro/`, 各類經濟/勢力/歷史事件模擬系統
  - theme_basis: `ref/world-graph.md`, `ref/三國-MUD-題材分布表.md`, `area/world_map.md`
  - compliance_check: compliant；本輪僅使用世界圖、題材分布表與既有 `sec_rift_core` spec 脈絡，不把 generator prototype 或模擬系統當成直接 runtime 依據
  - next_action: 以 `area/sec_rift_deeps/map.md` 生成第一批 `roo` 與最小 runtime 資產，並把 `sec_rift_core/9612` 的 down 邊界正式接到 `sec_rift_deeps/9701`
  - notes: `plans/area/0012-sec-rift-deeps.md` 與 `area/sec_rift_deeps/map.md` 第一版已建立；`--validate-only` 已通過；承接 `sec_rift_core/9612` 的 down world link，runtime 仍未掛載


## Done

- `area/world_map.md` 已建立，並整合 `help/map.hlp`、`docs/3yWebsite/docs/maps.md`、`docs/3yWebsite/docs/data/maps.json`、`docs/3yWebsite/map/*.html`
- `plans/0001-world-map-area-rebuild.md` 已建立
- `plans/area/0002-loyang-outskirts.md` 已建立
- `loyang_outskirts` 已完成第一輪整合並進入可前進下一區狀態
- `plans/area/0003-beiping-outskirts.md` 已建立
- `beiping_outskirts` 已完成第一輪整合與 smoke test 驗證，`delivery_gate` 達到 `validated_ready_to_advance`
- `plans/area/0004-jingxiang-road.md` 已建立
- `jingxiang_road` 已完成第一輪 implementation、commit `abd53ac`，並達成可前進下一區狀態
- `plans/area/0005-wild-longqu-hills.md` 已建立
- `wild_longqu_hills` 已完成第一輪 implementation、commit `c6f5c9a`，並達成可前進下一區狀態
- `plans/area/0006-dng-loyang-sewer.md` 已建立
- `dng_loyang_sewer` 已完成第一輪 implementation、commit `efb756e`，並達成可前進下一區狀態
- `plans/area/0007-dng-sewer-depths.md` 已建立
- `dng_sewer_depths` 已完成第一輪 implementation、commit `3717a7d`，並達成可前進下一區狀態
- `plans/area/0008-dng-royal-tomb.md` 已建立
- `dng_royal_tomb` 已完成第一輪 implementation、commit `30e2fa3`，並達成可前進下一區狀態
- `plans/area/0009-sec-catacomb-depths.md` 已建立
- `sec_catacomb_depths` 已完成第一輪 implementation、commit `7d21770`，並達成可前進下一區狀態
- `plans/area/0010-sec-rift-below.md` 已建立
- `sec_rift_below` 已完成第一輪 implementation、commit `3d88215`，並達成可前進下一區狀態
- `plans/area/0011-sec-rift-core.md` 已建立
- `sec_rift_core` 已完成第一輪 implementation、commit `48393ff`，並達成可前進下一區狀態
## Blocked

- none

## Current Recommended Next Step

以 `sec_rift_deeps/map.md` 生成第一批 `roo` 與最小 runtime 資產，延續洛陽地下鏈由 `sec_rift_core/9612` 向下正式接入 `sec_rift_deeps/9701`，並保留 `9712` 的 deeper stub 作為未來裂界禁底延伸點。

語意提醒：

- 目前 `sec_rift_deeps` 已進入 `in_progress`，固定 prompt 下次會優先續做這一區，不會跳往新的候選 area
- `sec_catacomb_depths` 已完成第一輪 implementation 並提交，可由 `Done` 與 `plans/area/0009-sec-catacomb-depths.md` 回查
- `sec_rift_below` 已完成第一輪 implementation 並提交，可由 `Done` 與 `plans/area/0010-sec-rift-below.md` 回查
- `sec_rift_core` 已完成第一輪 implementation 並提交，可由 `Done` 與 `plans/area/0011-sec-rift-core.md` 回查
- 依新 room reservation policy，`sec_rift_below` 已使用 `9501-9520`，`sec_rift_core` 已使用 `9601-9620`；`sec_rift_deeps` 已保留並規劃 `9701-9720`
- 既有地下鏈 `9451/9461/9481/9491` 保留原狀，不在這一輪 retroactive 重編

建議可直接使用的 prompt：

`實作 sec_rift_deeps 的第一批 runtime area，從 map.md 生成 roo、補最小 index/mob/obj/res/shp，並把 sec_rift_core/9612 正式接到 sec_rift_deeps/9701。`
