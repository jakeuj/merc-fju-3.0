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

## Quest Boundary

- `data/quest` / `data/question` 預設不屬於 area rebuild 的核心交付物。
- 啟動時若看到 `系統載入 0 個解謎資料。`，在沒有單區 quest 依賴證據前，不視為 tracker blocker。
- 只有當當前 area 的 runtime flow 明確使用 `mpsetquest`、`mpremquest`、`isquest`，或某段 puzzle / branch 必須依賴 quest flag 才能成立時，才把 quest data 納入該區 scope。
- 一旦納入，單區 plan / tracker 至少要補：
  - quest keyword 清單
  - 觸發來源
  - `data/quest` 需新增或修改的條目
  - quest-dependent 驗證路徑
- 若當前 area 沒有 quest mark 依賴，應優先維持 spec-first area workflow，不要為了補 legacy quest system 而擴張本輪 scope。

## References

- 全局計畫：`plans/0001-world-map-area-rebuild.md`
- 單區計畫：`plans/area/0002-loyang-outskirts.md`、`plans/area/0003-beiping-outskirts.md`、`plans/area/0004-jingxiang-road.md`、`plans/area/0019-sec-rift-core-below-deeps.md`、`plans/area/0020-sec-rift-core-vein-abyss.md`
- 世界圖參考：`area/world_map.md`
- ref 索引：`ref/Readme.md`
- 舊站 docs 參考：`docs/3yWebsite/docs/index.md`
- 舊站玩家攻略資料：`docs/3yWebsite/docs/data/players.json`
- 舊站技能資料：`docs/3yWebsite/docs/data/skills.json`

## Docs Dataset Guidance

- 當前 tracker 沒有 `in_progress`、也沒有 `todo` 時，若要盤點下一個 area candidate，先用 `docs/3yWebsite/docs/data/players.json` 與 `docs/3yWebsite/docs/data/skills.json` 補玩法耦合脈絡，再決定候選區。
- `skills.json` 目前基線是 `31` 筆，分類應為：
  - 武器技能 `11`
  - 法術技能 `10`
  - 職業技能 `7`
  - 其他技能 `3`
- `players.json` 目前基線是 `26` 筆，分類應為：
  - `bard` `2`
  - `bravo` `8`
  - `general` `7`
  - `mage` `2`
  - `newplayer` `7`
- `players.json` 內有 `1` 筆 `.htm` 舊檔（`newhand/players/newplayer/9907151.htm`）；盤點來源時不要漏掉。
- 使用方式：
  - 先從 `players.json` 找出玩家攻略高頻提到的 teacher、轉職點、巴士/船站、醫補與練功 loop。
  - 再從 `skills.json` 核對這些節點承接哪些技能鏈、資源消耗與職業服務。
  - 最後才把候選 area 放進 `candidate queue` 或 `todo`。
- 若這輪是因為 docs dataset 才決定某個新候選區、world link 或服務節點配置，記得在單區 plan / tracker 補上：
  - `ref_inputs_used`
  - `ref_inputs_deferred`
  - `theme_basis`
  - `compliance_check`
- `docs/3yWebsite` 仍視為 reference-only 舊站鏡像；若未來真的改動現行 runtime 的 area / skill registry，要另同步 `docs/current-game/*`。

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

- `sec_rift_sealed_core_heart`
  - reserved_room_block: `10801-10820`
  - theme: `仙俠`
  - subtheme: `封心核心 / 心脈主井`

## Todo

(目前無 `todo` 項目。)

## In Progress

- `sec_rift_sealed_core_heart`
  - plan: `plans/area/0023-sec-rift-sealed-core-heart.md`
  - spec: `area/sec_rift_sealed_core_heart/map.md`
  - reserved_room_block: `10801-10820`
  - theme: `仙俠`
  - subtheme: `封心核心 / 心脈主井`
  - ref_inputs_used:
    - `ref/Readme.md`
    - `area/sec_rift_sealed_core_basin/map.md`
    - `ref/world-graph.md`
    - `ref/三國-MUD-題材分布表.md`
  - ref_inputs_deferred:
    - `docs/3yWebsite/docs/data/players.json`（repo 目前不存在，僅保留追蹤需求）
    - `docs/3yWebsite/docs/data/skills.json`（repo 目前不存在，僅保留追蹤需求）
    - `ref/sanguo-area-scaffold/`
    - `mud-world-builder/`
    - `mud-ai-map-generator/`
    - `mudlet-map-generator/`
    - `mud-world-map-editor/`
    - `mud-world-map-editor-pro/`
    - 各類經濟/勢力/歷史事件模擬系統
  - theme_basis:
    - `area/sec_rift_sealed_core_basin/map.md`
    - `ref/world-graph.md`
    - `ref/三國-MUD-題材分布表.md`
  - compliance_check: `compliant；依既有地下鏈向下 world link 先建立下一段 spec-first 里程碑，維持 ref/Readme.md 容許的規劃範圍`
  - delivery_gate: `implementation_in_progress`


## Done

- `area/world_map.md` 已建立，並整合 `help/map.hlp`、`docs/3yWebsite/docs/maps.md`、`docs/3yWebsite/docs/data/maps.json`、`docs/3yWebsite/map/*.html`
- `docs/current-game/areas.md` 與 `docs/current-game/areas.json` 已建立，整理目前 loadable runtime area registry 與重建鏈摘要
- `docs/CNAME` 已設定 `sango.jakeuj.com`，讓 current-game GitHub Pages 可掛上專用網域
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
- `plans/area/0012-sec-rift-deeps.md` 已建立
- `sec_rift_deeps` 已完成第一輪 implementation，完成本機 build 與 smoke test，並達成可前進下一區狀態
- `plans/area/0013-sec-rift-abyss.md` 已建立
- `sec_rift_abyss` 已完成第一輪 implementation，完成本機 Linux build，並達成可前進下一區狀態
- `plans/area/0014-sec-rift-nadir.md` 已建立
- `sec_rift_nadir` 已完成第一輪 implementation，完成本機 Linux build，並達成可前進下一區狀態
- `plans/area/0015-sec-rift-prison-core.md` 已建立
- `sec_rift_prison_core` 已完成第一輪 implementation，完成本機 build 與 smoke test，並達成可前進下一區狀態
- `plans/area/0016-sec-rift-underseal-dais.md` 已建立
- `sec_rift_underseal_dais` 已完成第一輪 implementation，完成本機 Linux build，並達成可前進下一區狀態
- `plans/area/0017-sec-rift-true-core.md` 已建立
- `sec_rift_true_core` 已完成第一輪 implementation，完成本機 Linux build，並達成可前進下一區狀態
- `plans/area/0018-sec-rift-core-below.md` 已建立
- `sec_rift_core_below` 已完成第一輪 implementation，完成本機 Linux build，並達成可前進下一區狀態
- `plans/area/0019-sec-rift-core-below-deeps.md` 已建立
- `sec_rift_core_below_deeps` 已完成第一輪 implementation，完成本機 Linux build，並達成可前進下一區狀態
- `plans/area/0020-sec-rift-core-vein-abyss.md` 已建立
- `sec_rift_core_vein_abyss` 已完成第一輪 implementation、commit `f4fe735`，完成 WSL Linux build 與 smoke test，並達成可前進下一區狀態
- `plans/area/0021-sec-rift-underseal-basin.md` 已建立
- `sec_rift_underseal_basin` 已完成第一輪 implementation、commit `344459d`，完成本機 Linux build 與 smoke test，並達成可前進下一區狀態
- `plans/area/0022-sec-rift-sealed-core-basin.md` 已建立
- `sec_rift_sealed_core_basin` 已完成第一輪 implementation、commit `2fb0a07`，完成本機 Linux build 與 smoke test，並達成可前進下一區狀態
## Blocked

- none

## Current Recommended Next Step

目前新的 next actionable area 仍是 `sec_rift_sealed_core_heart`；spec milestone 已提交，本輪最合適的下一步是開始第一輪 runtime implementation。

下一輪建議動作：

1. 以 `map.md` 生成 `roo/10801-10812` 第一版並補最小 runtime 資產
2. 一併修改 `area/sec_rift_sealed_core_basin/roo/10712.roo` 與 `area/directory.lst`
3. 跑 build、smoke test、`log/*` 與 `debug/*` 驗證
4. 再將 `delivery_gate` 推到 `implementation_ready_for_commit` 或更高狀態

（註：目前 repo 無 `docs/3yWebsite/docs/data/players.json` 與 `skills.json`，下一輪若要做 docs-assisted pass，需先補回 dataset 或改用現存資料來源。）

語意提醒：

- 目前已有 `in_progress` 項目 `sec_rift_sealed_core_heart`，再次使用固定 prompt 時應優先續做此區，不得跳到其他候選
- `sec_rift_core_below` 已完成第一輪 implementation 並提交，可由 `Done` 與 `plans/area/0018-sec-rift-core-below.md` 回查
- `sec_rift_core_below_deeps` 已完成第一輪 implementation 並提交，可由 `Done` 與 `plans/area/0019-sec-rift-core-below-deeps.md` 回查
- 依新 room reservation policy，`sec_rift_below` 已使用 `9501-9520`，`sec_rift_core` 已使用 `9601-9620`，`sec_rift_deeps` 已完成 `9701-9712` 第一版落地，`sec_rift_prison_core` 已完成 `10001-10012` 第一版落地，`sec_rift_underseal_dais` 已完成 `10101-10112` 第一版落地，`sec_rift_true_core` 已完成 `10201-10212` 第一版落地，`sec_rift_core_below` 已完成 `10301-10312` 第一版落地，`sec_rift_core_below_deeps` 已完成 `10401-10412` 第一版落地，`sec_rift_core_vein_abyss` 已完成 `10501-10512` 第一版落地，`sec_rift_underseal_basin` 已完成 `10601-10612` 第一版落地，並保留 `10601-10620` 作為首段 block
- 既有地下鏈 `9451/9461/9481/9491` 保留原狀，不在這一輪 retroactive 重編


建議可直接使用的 prompt：

`續做 sec_rift_sealed_core_heart：開始第一輪 runtime implementation，完成後再做 smoke test。`
