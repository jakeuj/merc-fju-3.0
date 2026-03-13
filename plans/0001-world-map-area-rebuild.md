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
- `todo`
- `in_progress`
- `done`
- `blocked`
- `next_action`
- 固定主 prompt

## Fixed Prompt

日後延續工作使用固定主 prompt：

`繼續實作下一個待建 area`

規則：

- 若 `area/rebuild_plan.md` 有 `in_progress`，優先續做該區
- 否則選第一個 `todo` 且無 blocker 的 area

## Candidate Order

依 `area/world_map.md` 目前排序，第一批新 AREA 候選為：

1. `loyang_outskirts`
2. `beiping_outskirts`
3. `jingxiang_road`

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

## Assumptions

- `plans/` 是正式規劃區，不是臨時草稿區
- `area/rebuild_plan.md` 與 `plans/` 分工明確：前者追蹤狀態，後者保存決策完整的計畫
- 未來若有技能或工具專題，可再新增 `plans/skills/`、`plans/tools/`，但目前先只使用 `plans/` 與 `plans/area/`
