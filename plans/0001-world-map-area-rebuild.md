# World Map-Driven Area Rebuild

## Summary

以 `area/world_map.md` 為世界層參考，建立一套可長期持續的 AREA 重建流程。第一個正式新 AREA 以 `loyang_outskirts` 為起點，但這份計畫的目的不只是一個新區，而是先把「全局追蹤 + 單區 spec-first 流程 + 可重複 prompt」一起定好。

## Plan Storage Convention

- 長期計畫放在 `plans/`
- 全局計畫命名規則：`plans/NNNN-topic-slug.md`
- 單一 area 計畫命名規則：`plans/area/NNNN-area-slug.md`
- 流水號固定 4 碼，跨分類遞增，不重用

目前已保留的下一個編號：

- `0002`：第一個 area 實作計畫

## Workflow

- 世界層參考使用 `area/world_map.md`
- 歷史 / 外部世界規劃索引使用 `ref/Readme.md`
- 日常追蹤看板使用 `area/rebuild_plan.md`
- spec-first 區域設計使用 `area/<new_area>/map.md`
- 若需要 `.roo` scaffold，使用 `.agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py`
- 題材與沉浸式設計使用 `.agents/skills/merc-area-builder/references/theme-design-patterns.md`

## Ref Usage Policy

本輪 area rebuild 對 `ref/` 的使用優先級固定如下。

本輪直接使用：

- 世界藍圖與拓樸
  - `world-graph.json`
  - `三國-MUD-世界設計總藍圖-Architecture-Map.md`
  - `三國-MUD-題材分布表.md`
- AREA scaffold 與 template
  - `area-template-wild_loyang_east.md`
  - `sanguo-area-specfirst/`
  - `sanguo-area-scaffold/`

本輪只作背景索引，不作直接實作依據：

- 生成器與編輯器原型
  - `mud-world-builder/`
  - `mud-ai-map-generator/`
  - `mudlet-map-generator/`
  - `mud-world-map-editor/`
  - `mud-world-map-editor-pro/`
- 模擬與系統原型
  - `mud-ai-faction-strategy-system/`
  - `mud-character-relationship-system/`
  - `mud-economy-system/`
  - `mud-faction-control-system/`
  - `mud-hero-ai-system/`
  - `mud-history-event-system/`
  - `mud-npc-ecosystem-system/`

規則：

- 只有當 area rebuild 明確進入工具化、經濟、勢力或歷史事件模擬階段，才把上述原型納入本輪實作依據
- 在那之前，這些資料夾只保留為未來延伸方向

## Tracking Model

`area/rebuild_plan.md` 應固定包含：

- candidate area 清單
- `theme`
- `subtheme`
- `ref_inputs_used`
- `ref_inputs_deferred`
- `theme_basis`
- `compliance_check`
- `todo`
- `in_progress`
- `done`
- `blocked`
- `next_action`
- `next_prompt`
- `delivery_gate`
- 固定主 prompt

## Ref Compliance Check

為了確保每輪產出沒有偏離 `ref/Readme.md` 定義的本輪參考範圍，每個單區 plan 都要補上：

- `ref_inputs_used`
- `ref_inputs_deferred`
- `theme_basis`
- `compliance_check`

規則：

- `ref_inputs_used` 只列這一輪真正拿來做設計或實作決策的 `ref/` 檔案或資料夾
- `ref_inputs_deferred` 要明講哪些 `ref/` 類別是知道它存在，但刻意不作本輪直接依據
- `theme_basis` 要指出題材判定依據，例如 `題材分布表`、`theme-world-allocation`、單區 template
- `compliance_check` 要直接回答：本區是否仍符合 `ref/Readme.md` 本輪允許來源；若有例外，也要明講原因

## Delivery Gates

每個 area 除了 `todo / in_progress / done / blocked` 之外，還要有更細的交付門檻，用來決定現在應該先 commit，還是可以前進到下一個 area。

建議使用下列 milestone 語意：

- `spec_in_progress`
  - 還在整理 `map.md`、world links、cluster、題材或 room-spec intent
- `spec_ready_for_commit`
  - spec 已形成穩定里程碑，應先 commit，再進下一步
- `implementation_in_progress`
  - 已開始落地 `.roo` / `mob` / `obj` / `res` / `shp` / `directory.lst` / 邊界出口
- `implementation_ready_for_commit`
  - 本輪資料落地已形成穩定里程碑，應先 commit
- `validated_ready_to_advance`
  - 本輪驗證已完成，可結束當前 area，移往下一個候選
- `blocked`
  - 有阻塞，需停在當前 area，不得跳下一區當作替代

決策規則：

- 若 `delivery_gate` 是 `spec_ready_for_commit` 或 `implementation_ready_for_commit`，先 commit，不進下一區
- 若 `delivery_gate` 是 `validated_ready_to_advance`，才可使用 `繼續實作下一個待建 area`
- 若 `delivery_gate` 是任何 `*_in_progress`，表示仍應留在當前 area
- 若 `delivery_gate` 是 `blocked`，先處理 blocker 或明確調整狀態，不能拿「做下一區」當繞路

## Fixed Prompt

日後延續工作使用固定主 prompt：

`繼續實作下一個待建 area`

規則：

- 若 `area/rebuild_plan.md` 有 `in_progress`，優先續做該區
- 否則選第一個 `todo` 且無 blocker 的 area
- 這裡的 `next area` 一律解讀為 next actionable area，而不是 candidate queue 的下一個新候選
- 因此只要 `in_progress` 仍存在，就不得切到下一個 `todo`；除非目前區域已轉成 `done`、`blocked` 或 `abandoned`

## Candidate Order

依 `area/world_map.md` 目前排序，第一批新 AREA 候選為：

1. `loyang_outskirts`
2. `beiping_outskirts`
3. `jingxiang_road`
4. `wild_longqu_hills`
5. `dng_loyang_sewer`

## Theme Allocation

依 `theme-design-patterns.md`，世界級規劃不能只看拓樸，也要看題材分布。第一批候選先固定題材定位：

- `loyang_outskirts`
  - theme: `歷史城市風`
  - subtheme: `軍旅風`
  - 缺口角色：補主城外郊、巡邏線、郊野導流與地下入口過渡
- `beiping_outskirts`
  - theme: `軍旅風`
  - subtheme: `歷史城市風`
  - 缺口角色：補北方邊關、驛站、渡口與邊境緊張感
- `jingxiang_road`
  - theme: `江湖風`
  - subtheme: `軍旅風`
  - 缺口角色：補中長距離官道、流言、伏兵與支線遭遇
- `wild_longqu_hills`
  - theme: `探險遺跡`
  - subtheme: `仙俠風`
  - 缺口角色：補洛陽東郊往外野探索帶的第二段，讓城郊與地下遺跡之間多一層丘陵轉接
- `dng_loyang_sewer`
  - theme: `仙俠風`
  - subtheme: `詭異民俗風`
  - 缺口角色：補洛陽東郊暗井入口之後的地下水路前帶，讓洛陽鏈同時往地表外圈與地下支線延伸

後續新增候選 area 時，必須一併記錄：

- `theme`
- `subtheme`
- 它在六大題材中的缺口價值

## First Implementation Target

第一個正式新 AREA 固定從 `loyang_outskirts` 開始，原因：

- 直接貼著現有 `loyang`
- `world_map.md`、`maps.md`、`maps.json`、`map/loyang.html` 都有依據
- 服務點、交通點與 `#Enquire` 場景完整
- 容易做出道路、外郊、地下入口並存的 3D spec
- 題材上可用 `歷史城市風` 為主、`軍旅風` 為輔，最適合做第一個完整範例
- `ref/Readme.md` 已明確指出 `area-template-wild_loyang_east.md` 與 `sanguo-area-specfirst/` 是最值得優先借鏡的來源

## Acceptance Criteria

- `plans/` 成為正式長期計畫入口
- 後續新增 plan 不需再重新發明命名規則
- 代理能只靠固定主 prompt + `area/rebuild_plan.md` 找到下一步
- `loyang_outskirts` 能作為第一個完整驗證 spec-first 流程的範例

## Proven By First Case

`loyang_outskirts` 已經把第一個正式新 AREA 的工作流跑完到可 commit 的整合里程碑，證明下列流程可行：

- 用 `plans/area/*.md` 固定單區設計意圖
- 用 `area/<new_area>/map.md` 承接人類可讀 spec 與 `mapmd-json`
- 用 generator 投影出第一批 `.roo`
- 再補 `index / mob / obj / res / shp`
- 最後把 area 掛入 `area/directory.lst`、補既有世界邊界出口，並做啟動 smoke test

這次案例也證明兩個全局規則應視為正式流程的一部分：

- `delivery_gate` 不是輔助資訊，而是固定 prompt 能否安全續跑的核心控制欄位
- `mapmd-json` 需要支援 external exit，否則新 AREA 一接到既有主城就會出現 spec 與 runtime 分裂

## Process Updates After Loyang Outskirts

從這次案例回推，全局流程應固定加上以下實務規則：

1. 新 AREA 若要連到既有主城或既有房號，應優先在 `mapmd-json` 明確標示 external exit，再生成 `.roo`
2. 在把新 AREA 掛入 `area/directory.lst` 前，至少要具備：
   - `index`
   - 可通過 validate 的 `map.md`
   - 第一批 `roo`
   - 最小 `mob/obj/res/shp`
2.1 新 AREA 預設 `Capital 0`，除非它被明確指定為出生地 / 首都 / 系統級 home 候選；像城郊、外野、地下入口前哨這類過渡區不應自動進入出生地列表
3. 掛入 `directory.lst` 後，必做一次本機 smoke test，並以最新啟動 log 判定是否成功
4. 若 smoke test 成功，才可把 gate 推進到 `implementation_ready_for_commit`
5. smoke test 前先清空 `debug/*` 內容，並建立本輪 `log/*` 觀察基線；看到成功訊號後，仍要再檢查 `debug/*` 是否有本次新增 area 相關的新 bug / warning
6. 若 smoke test 需要用 `timeout` 控制，時間必須高於正常開機時間；預設優先給 `45` 到 `60` 秒，並在成功後回看本輪 log，避免把測試工具造成的提早中止誤判成 area 載入失敗

## Assumptions

- `plans/` 是正式規劃區，不是臨時草稿區
- `area/rebuild_plan.md` 與 `plans/` 分工明確：前者追蹤狀態，後者保存決策完整的計畫
- 未來若有技能或工具專題，可再新增 `plans/skills/`、`plans/tools/`，但目前先只使用 `plans/` 與 `plans/area/`
