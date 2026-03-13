# Current Repo State

這份參考檔集中描述 `merc-fju-3.0` 目前和 area 建置直接相關的 repo 現況。

## area/ 現況

目前 repo 內已恢復的正式/既有區域是：

- `limbo`
- `loyang`
- `beiping`
- `new`
- `newfight`
- `pk_area`
- `free_fight`

另外，`player` 區域不需要寫入 `area/directory.lst`，系統會自動讀取。

## 每區常見結構

- 既有區域通常至少有 `index`、`mob/`、`obj/`、`res/`、`roo/`、`shp/`
- 戰鬥區與部分主城區還可能附帶區域地圖檔；它不一定放在區根目錄，也可能放在 `roo/` 內，視既有區格式而定
- 地圖不要只當成平面格子：`src/act_move.c` 目前支援 `north/east/south/west/up/down/enter/out`，規劃與修復出口時要把它當成立體拓樸
- `mapmd-json` 的內部模型是 graph-native：room = node、exit = edge，而 `#Keyword` / `#Job` / `#Enquire` 是掛在 node 上的互動與導流 metadata
- `mapmd-json` 現在也允許 external exit：若某個出口本來就要接到 spec 外、但 repo 內已存在的既有房號，可在 exit 上標示 `external: true`，讓 generator 保留這個出口，同時略過 same-spec target / reverse-link 驗證
- 不要再把 `mineral/` 視為目前 repo 的既定必備目錄；只有任務真的需要礦脈/採集物時才新增，並同步確認載入格式
- `beiping` 額外有 `map`
- `pk_area/roo` 目前有 `map`、`map2`
- `free_fight/roo` 目前有一個名為 `pk_area` 的地圖檔；名稱雖舊，但內容是在畫 `7001-7044` 的房間布局
- 修改既有區時保留原本地圖檔名與格式；不要因為檔名看起來怪就先改名
- 目前 area 內地圖檔分布並不一致：`limbo` 沒有、`beiping` 在區根目錄、`loyang` 在 `roo/` 下有多張、`free_fight` 則沿用舊名 `pk_area`
- 目前沒有證據顯示這些 area-local 地圖檔一定會被 runtime 直接讀取；它們比較適合視為維護輔助或歷史資料
- `help/map.hlp` 是玩家可見的世界地圖，和每個 AREA 的設計規格檔是不同層次的東西
- 目前沒有通用 MUD map 標準適合直接拿來當 Merc-FJU 的 room source of truth；本 skill 使用的是 Merc-first、Git-friendly 的內部 graph schema
- 若 repo 內存在 `plans/` 與 `area/rebuild_plan.md`，表示這個專案也在使用長期重建工作流；此時除了單次 area 任務外，還要同步遵守追蹤看板與固定 prompt 規則

## plans/ 現況

- `plans/` 是正式長期規劃入口，不是臨時草稿區
- 全局計畫使用 `plans/NNNN-topic-slug.md`
- 單一 area 計畫使用 `plans/area/NNNN-area-slug.md`
- `area/rebuild_plan.md` 是日常追蹤看板，負責 `todo / in_progress / done / blocked / next_action`
- 若使用固定 prompt `繼續實作下一個待建 area`，先讀 `area/rebuild_plan.md` 再決定下一個目標
- 長期重建流程還應使用 `delivery_gate` 與 `next_prompt` 來判斷：現在該先 commit、續做當前 area，還是已可前進下一區

## ref/ 現況

- `ref/Readme.md` 是 `ref/` 的入口索引，先用它判斷該讀世界藍圖、template、spec-first scaffold、生成器，還是模擬系統
- 目前和 `plans/0001-world-map-area-rebuild.md` 對齊的本輪直接使用類別只有兩種：
- 世界藍圖與拓樸
- AREA Scaffold 與 Template
- 目前先不進本輪實作依據的類別有兩種：
- 生成器與編輯器原型
- 模擬與系統原型
- 這些 deferred 類別不是沒價值，而是留到未來要做 map tooling、自動化編輯器、經濟/勢力/NPC 生態/歷史事件系統時再讀；不要在第一輪 area spec 工作就把它們全載進來
- 若任務是世界級 area rebuild，優先從 `ref/Readme.md` 指向的世界藍圖、`world-graph.json` 與題材分布資料開始
- 若任務是像 `loyang_outskirts` 這種新 area spec，讀取順序固定為：
- `ref/Readme.md`
- `area-template-wild_loyang_east.md`
- `sanguo-area-specfirst/` 中相近 `wild_*` 節點
- 必要時才補讀 `sanguo-area-scaffold/`

## scripts/ 現況

- repo 根目錄 `scripts/` 目前可見的腳本只有 `scripts/convert_big5_to_utf8.py`
- 本 skill 另外提供 `scripts/generate_roo_from_map_md.py`，用來把受限結構的 `map.md` 轉成 `.roo` scaffold；它不是自由文字 Markdown compiler
- 這支 script 目前只做一件事：把 `mapmd-json` graph schema 驗證後投影成 `.roo` scaffold；它不是 Mudlet、SQLite 或其他外部 mapper exporter
- external exit 仍會輸出成正式 `.roo #Exit`，只是驗證時不要求目標房間也出現在同一份 spec 內
- 不要假設 `scripts/check-data.py` 或其他舊工具一定存在；驗證步驟應先以 repo 實際檔案為準
- 若任務涉及大量舊資料匯入、回填或外部檔案導入，可用 `convert_big5_to_utf8.py` 協助確認 UTF-8 轉碼

## 舊版資料比對來源

- 若目前 repo 的 `area/`、`data/`、`help/` 或固定房號資料不完整，或你需要確認舊區原本長相，允許回查舊 repo `jakeuj/merc-fju-2.0-utf8`
- 優先把舊 repo 視為「歷史對照來源」，不是直接覆蓋真相；真正要採用哪份資料，仍以目前 3.0 任務目標與現行 repo 狀態決定
- 特別適合用在：
- 補回舊區的 `mob/obj/roo/res/shp`
- 對照舊 VNUM、舊出口、舊出生點、舊交通/懸賞/提示文字
- 確認某個房號、NPC、物件、技能掉落或 help 文案在舊版是否存在
- 若從舊 repo 搬資料回來，必須重新檢查 UTF-8、VNUM 衝突、目錄結構與現行設定是否一致
