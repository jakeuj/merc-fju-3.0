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
- 成功不能只看 process 暫時存活；至少要確認啟動輸出或 log 內有像 `三國歪傳之降龍伏虎開始正常運作` 這類明確成功訊號
- 即使已看到成功訊號，仍要回頭檢查 `debug/*` 是否出現本次新增 area 相關的新錯誤或警告
- 只有在上述三點都完成後，才可把 `delivery_gate` 推進到 `implementation_ready_for_commit` 或 `validated_ready_to_advance`

## References

- 全局計畫：`plans/0001-world-map-area-rebuild.md`
- 單區計畫：`plans/area/0002-loyang-outskirts.md`
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

## Candidate Queue

1. `loyang_outskirts`
2. `beiping_outskirts`
3. `jingxiang_road`

## Todo

### `beiping_outskirts`

- status: `todo`
- delivery_gate: `spec_in_progress`
- plan: `not created yet`
- parent_region: `beiping`
- theme: `軍旅風`
- subtheme: `歷史城市風`
- world_links: `北平郊區`, `易京`, `白狼山`
- next_action: 在 `loyang_outskirts` 穩定後建立單區計畫檔
- next_prompt: `在 loyang_outskirts 完成並可前進後，建立 beiping_outskirts 的單區計畫與 map.md spec 草案。`
- notes: 北方交通與邊關混合型候選

### `jingxiang_road`

- status: `todo`
- delivery_gate: `spec_in_progress`
- plan: `not created yet`
- parent_region: `future regional chain`
- theme: `江湖風`
- subtheme: `軍旅風`
- world_links: `襄陽`, `新野`, `江夏`, `荊襄大道`
- next_action: 等 `loyang_outskirts` 與 `beiping_outskirts` 後再評估
- next_prompt: `在 loyang_outskirts 與 beiping_outskirts 完成後，建立 jingxiang_road 的單區計畫與 map.md spec 草案。`
- notes: docs 依據足夠，但 repo 內尚未有直接母城 area，成本較高

## In Progress

### `loyang_outskirts`

- status: `in_progress`
- delivery_gate: `implementation_ready_for_commit`
- plan: `plans/area/0002-loyang-outskirts.md`
- parent_region: `loyang`
- theme: `歷史城市風`
- subtheme: `軍旅風`
- world_links: `洛陽東郊`, `龍渠丘陵`, `洛陽地下水區入口`
- next_action: 先 commit 目前 `loyang_outskirts` 的整合里程碑；commit 後再決定是否補龍渠丘陵 / 地下水區的後續 world link 或將狀態推進到 `validated_ready_to_advance`
- next_prompt: `先 commit 目前 loyang_outskirts 的整合里程碑；commit 後若仍需後續世界連接，續做 loyang_outskirts，否則再繼續實作下一個待建 area。`
- notes: `area/loyang_outskirts` 已具備 `index`、`mob`、`obj`、`res`、`roo`、`shp` 最小集合，並已成功掛入 `area/directory.lst`；`556 <-> 7501` 邊界出口已落地，WSL smoke test 也已進到「開始正常運作」

## Done

- `area/world_map.md` 已建立，並整合 `help/map.hlp`、`docs/3yWebsite/docs/maps.md`、`docs/3yWebsite/docs/data/maps.json`、`docs/3yWebsite/map/*.html`
- `plans/0001-world-map-area-rebuild.md` 已建立
- `plans/area/0002-loyang-outskirts.md` 已建立

## Blocked

- none

## Current Recommended Next Step

先 commit 目前 `loyang_outskirts` 的整合里程碑，再決定是否續做後續 world link，或把它推進到可前往下一區的狀態。

語意提醒：

- 目前的 next actionable area 仍是 `loyang_outskirts`
- 只有當 `loyang_outskirts` 被移到 `Done`、`Blocked` 或明確標示 `Abandoned` 之後，`beiping_outskirts` 才會成為下一個 area
- 目前 `delivery_gate` 已進到 `implementation_ready_for_commit`，表示這一輪的安全動作是先 commit 當前里程碑，再決定是否續做或切下一區

建議可直接使用的 prompt：

`先 commit 目前 loyang_outskirts 的整合里程碑；commit 後若仍需後續世界連接，續做 loyang_outskirts，否則再繼續實作下一個待建 area。`
