# World Map-Driven Area Rebuild

## Summary

以 `area/world_map.md` 為世界層參考，建立一套可長期持續、可讓 Agent 安全續跑的 AREA 重建流程。第一個正式新 AREA 以 `loyang_outskirts` 為起點，但這份計畫的目的不只是一個新區，而是先把「全局追蹤 + 單區 spec-first 流程 + 可重複 prompt + 驗證與交付治理」一起定好，讓後續世界能穩定擴張到更多 AREA，而不是每輪重新發明流程。

## Plan Storage Convention

- 長期計畫放在 `plans/`
- 全局計畫命名規則：`plans/NNNN-topic-slug.md`
- 單一 area 計畫命名規則：`plans/area/NNNN-area-slug.md`
- 流水號固定 4 碼，跨分類遞增，不重用

目前已保留的下一個編號：

- `0002`：第一個 area 實作計畫

## Pipeline Architecture

全局 AREA rebuild pipeline 固定分成下列層級：

1. `World Graph`
   - 人工維護世界拓樸、題材分布與 progression
   - 主要入口是 `area/world_map.md`
2. `Area Queue`
   - 由 `area/rebuild_plan.md` 管理 `todo / in_progress / done / blocked`
   - 固定 prompt 只從這裡決定 next actionable area
3. `Area Plan`
   - 由 `plans/area/NNNN-area-slug.md` 固定單區邊界、題材、房號保留與外部連線
4. `Area Spec`
   - 由 `area/<new_area>/map.md` 承接 narrative spec 與 `mapmd-json`
5. `Projection + Implementation`
   - 先由 generator 投影 `.roo`
   - 再補 `mob / obj / res / shp / directory.lst / boundary rooms`
6. `Runtime Validation`
   - 以 build、smoke test、log/debug 檢查證明 area 可載入
7. `Commit / Merge Gate`
   - 只有符合 `delivery_gate` 的 area 才能往下個 milestone 或下一區前進

這個順序是正式流程，不應跳過中間的 queue、plan 或 validation。

## Workflow

- 世界層參考使用 `area/world_map.md`
- 歷史 / 外部世界規劃索引使用 `ref/Readme.md`
- 日常追蹤看板使用 `area/rebuild_plan.md`
- spec-first 區域設計使用 `area/<new_area>/map.md`
- 若需要 `.roo` scaffold，使用 `.agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py`
- 題材與沉浸式設計使用 `.agents/skills/merc-area-builder/references/theme-design-patterns.md`

## Scope Boundary: Quest Data

`data/quest` 與 `data/question` 屬於 current-game runtime content，但預設不屬於 area rebuild 的核心交付物。

預設規則：

- area rebuild 的主軸仍是 world graph、單區 plan、`map.md`、`.roo` 投影、boundary links、`index / mob / obj / res / shp / directory.lst` 與必要驗證。
- 只因為啟動時出現 `系統載入 0 個解謎資料。`，不構成 area rebuild blocker。
- 不得把「補齊 legacy quest system」當成每個新 area 的隱含交付要求，避免整體計畫被舊設計綁回去。

只有在單區 implementation 明確依賴 quest mark 狀態時，才把 `data/quest` 視為該區的附帶交付物。典型條件包括：

- area 的 mobprog 或事件流程有使用 `mpsetquest`、`mpremquest`、`isquest`
- 房間、互動物件或劇情分支必須靠 quest flag 才能開啟、阻擋、轉向或判定完成
- 若不補 `data/quest`，該區 runtime flow 會出現未知 keyword、條件永遠不成立、或 puzzle 無法完成

一旦符合上述條件，單區 plan 與工作回報至少要補：

- quest 依賴是否存在
- 使用到的 quest keyword 清單
- 哪個 mob / room / object / command 會設定、移除或檢查這些 keyword
- 本輪需新增或修改哪些 `data/quest` 條目
- 驗證時如何覆蓋 quest-dependent 路徑

## Recommendation Alignment

本計畫已吸收 `ref/mud-new-area-full-recommendations.md` 的方向，但採「依 repo 現況收斂」的落地方式，而不是直接把建議清單視為已存在的制度。

對齊原則：

- 參考文件提出的六層模型 `世界規劃 / 單區 spec / 生成器 / 驗證器 / smoke test / Git workflow`，在這個 repo 內直接對應到既有 pipeline
- 已經存在的能力，優先明文化成正式 contract，而不是另起一份平行文件重講一次
- 尚未存在的 `templates/`、`schemas/`、`tools/`、`prompts/`，先列入 roadmap；未落地前不得假裝它們已是硬性 gate
- 新增文件或工具時，應優先補現有流程的缺口，避免把 skill reference、`plans/`、`area/rebuild_plan.md` 與新文件做成三套彼此競爭的規則來源

## Capability Matrix

把 `ref/mud-new-area-full-recommendations.md` 映射到目前 repo，能力分層如下：

| Layer | 現行主入口 | 目前狀態 | 下一步缺口 |
| --- | --- | --- | --- |
| 世界規劃層 | `area/world_map.md`、`ref/Readme.md` | 已上線 | 補 world diff 與更明確的題材稽核 |
| 單區 spec 層 | `plans/area/*.md`、`area/<area>/map.md` | 已上線 | 補更固定的 template 與欄位檢查 |
| 生成器層 | `.agents/skills/merc-area-builder/scripts/generate_roo_from_map_md.py` | 已上線 | 仍以 `.roo` 投影為主，尚未包辦整區 bootstrap |
| 驗證器層 | `--validate-only`、`scripts/world_consistency_checker.py` | 部分上線 | 尚缺 plan/schema 驗證、log 摘要與 gate 建議器 |
| 啟動 / smoke test 層 | `make` / `startup.bash` / `log` / `debug` 檢查 | 已上線但偏人工 | 可補 runner 與摘要工具，但不能取代人工判讀成功訊號 |
| Git / PR / Codex workflow 層 | `delivery_gate`、固定 prompt、branch policy | 已上線 | 尚缺 PR template、prompt 套件與半自動 tracker 更新 |

## World Graph Governance

`area/world_map.md` 與其對應的世界拓樸決策屬於 world graph layer。預設規則：

- Agent 不得因為單區實作方便，就自行改寫全局 world graph 或 candidate order
- 若某輪任務真的要改世界拓樸、主鏈 progression、題材分布或大型 world link，應把它視為獨立的 world design task，而不是夾帶在單區 implementation 中
- 單區 plan 只能在既有 world graph 約束下展開；若發現 graph 與實作需求衝突，要先回寫全局計畫或 tracker 說明，再決定是否進入 graph 變更

## Area Unit Of Work

AREA rebuild 的預設工作單位是「一輪任務只處理一個 area milestone」。

規則：

- 固定 prompt 一次只推進一個 area
- 同一輪最多只允許一個 `in_progress` area
- 若當前 area 尚未達到可 commit 或可前進的 gate，不得順手開下一個 area 當平行支線
- 單區任務可分成 spec milestone 與 implementation milestone，但仍算同一個 area unit of work

目的：

- 降低 Agent 同時改多區造成的 world-state 漂移
- 讓 commit、review、smoke test 與問題回溯都能對準單一 area
- 讓 `area/rebuild_plan.md` 真正能當 queue，而不是鬆散記事本

## Area Plan Contract

每個 `plans/area/NNNN-area-slug.md` 至少應固定回答以下欄位，避免單區設計漂離世界層約束：

- `theme`
- `subtheme`
- `reserved_room_block`
- `planned_vnum_range`
- `external_links`
- `delivery_gate`
- `ref_inputs_used`
- `ref_inputs_deferred`
- `theme_basis`
- `compliance_check`

補充規則：

- `external_links` 要明講此區會接到哪些既有 area / room，避免 generator 與 runtime boundary room 各自講各話
- `planned_vnum_range` 代表首段保留區，不等於目前已落地的最後一號
- `delivery_gate` 雖然由 tracker 驅動，但單區 plan 也應保留當前語意與變更理由，方便回讀設計脈絡
- 若這輪只是先做 spec、尚未動 runtime data，也要先把 external links 與 boundary assumptions 寫清楚
- 若單區沒有 quest mark 依賴，不必因為 `data/quest` 目前為空而補 quest 欄位
- 只有當單區 runtime flow 明確依賴 `mpsetquest`、`mpremquest`、`isquest` 時，才需要在單區 plan 額外記錄 quest keyword、觸發來源與驗證方式

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
- `reserved_room_block`
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

另外，單區驗證證據不一定要全部塞進 tracker，但每輪至少要能在單區 plan、commit 訊息或工作回報中回答：

- 本輪用了哪些輸入來源
- 生成了哪些檔案或人工補了哪些 runtime data
- 驗證看了哪個 build / log / debug 結果
- 為何目前可停在這個 `delivery_gate`

## Room VNUM Reservation Policy

新建 area 的 room vnum 預設採「首段從 `xx01` 起跳」策略，目的是讓 spec-first area 在第一版落地後，既保有可讀、可追蹤的擴充空間，也延續 repo 既有 `501`、`9001`、`9101` 這種起號習慣。

規則：

- 新 area 立項時，先在 tracker 與單區 plan 記錄 `reserved_room_block`
- 未來新 area 的第一段 `reserved_room_block` 必須從某個新百位段的 `xx01` 開始
- block 大小依 area 首版規模浮動，但仍需保留 headroom；計算方式為「首版預估房數 + 至少 `8` 格 room headroom」後，往上取到最近的 `10`
- block 的結尾採整十收尾，例如 `9501-9520`、`9601-9630`、`9701-9750`
- 若估算後會跨出同一百位段，直接改用下一個百位段的 `xx01`，不要切成跨百位的保留段
- `planned_vnum_range` 預設應宣告整個首段保留區，而不是只寫到目前已落地的最後一號
- `mapmd-json` 內實際已使用的 room vnum 不必連號，但同一輪新 area 預設應先落在同一個首段保留區內
- extension block 合法，但只在原首段保留區用完後才允許新增，且必須在單區 plan、`map.md` metadata 與 tracker 明確註記
- `area/directory.lst` 的新 area 房號註解應同步反映首段保留區，而不是只反映當前已建立的最後一號
- 目前 `9451/9461/9481/9491` 這類地下鏈切段屬於舊流程遺留；既有 area 保留現狀，但未來新 area 不再沿用同一百位拆給多區的做法

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

配套要求：

- `spec_ready_for_commit` 代表 `map.md`、external links、reserved block 與題材依據已形成穩定里程碑
- `implementation_ready_for_commit` 代表 runtime data 已落地且至少完成一輪必要驗證，但尚未推到「可安全開下一區」
- `validated_ready_to_advance` 代表本區已完成本輪應做的 build / smoke test / log-debug 檢查，且沒有待處理 blocker

## Branch Policy

固定 prompt 不只要遵守 `delivery_gate`，也要遵守 branch gate。

規則：

- 若目前在 `develop` 或 `main`，且下一步是從 `todo` 啟動一個新的 area milestone，預設先切 `codex/<area>-implementation`
- 若目前 area 已經進入 `in_progress`，則在當前工作分支續做，不要同一區中途再切新 branch
- 若只是 merge 後的小型 `docs / tracker / plan` 收尾，可直接留在 `develop`
- 若使用者明講要直接在 `develop` 做，或指定其他 branch 策略，則以使用者指示為準

若採 GitHub review 流程，建議以「一個 area milestone 對應一個 branch / PR」為優先，而不是把多個 area 合併成單一 review 單位；但這是交付建議，不是目前 tracker 的硬性 gate。

目的：

- 避免 `develop` 直接承接長串 area implementation commit
- 讓每個 area milestone 或一小段主題鏈更容易整批 merge
- 讓固定 prompt 在「開始新 area」這一步有一致行為，不必每輪重新口頭提醒

## Runtime Validation Contract

每個 area implementation milestone 至少要回答以下驗證問題：

1. build 是否成功
2. area 是否能被 loader 正常載入
3. 是否出現 `duplicate vnum`、`parse error`、`Load_room`、boundary exit 錯誤或新 warning
4. smoke test 的成功訊號與對應 log 是哪一份
5. `debug/*` 是否出現本輪新增 area 相關的新訊息

規則：

- `spec / plan / tracker only` 任務可停在 `--validate-only`
- 一旦已改到 loadable runtime area data，預設至少要做對應 build 與 smoke test
- 若只是 generator 成功但 boundary room、`area/directory.lst` 或 loader 仍未驗證，不可直接視為 `validated_ready_to_advance`
- 驗證失敗時，先留在當前 area 修正，不要改去做下一區

## Milestone Output Contract

`ref/mud-new-area-full-recommendations.md` 強調「固定產出清單」。在本 repo 內，固定產出不必一次做滿所有文件，但每個 milestone 至少要交付下列內容。

spec milestone 最小產出：

- 單區 plan 已建立或更新，且補齊 `ref_inputs_used / ref_inputs_deferred / theme_basis / compliance_check`
- `area/<area>/map.md` 已形成可讀 spec，並含可驗證的 `mapmd-json`
- `reserved_room_block`、`planned_vnum_range`、`external_links` 已固定到可被後續 implementation 承接
- 至少有一筆可追溯的驗證證據，例如 `--validate-only` 結果或人工檢查紀錄

implementation milestone 最小產出：

- `index / roo / mob / obj / res / shp` 已達到最小可載入集合，或明確註記本輪尚未落地的部分
- `area/directory.lst` 與既有 boundary room 的連動修改已一併納入同一里程碑
- build、smoke test、`log/*`、`debug/*` 的驗證結論可被回讀
- `area/rebuild_plan.md` 與單區 plan 的 `delivery_gate` 已同步到本輪結果

global workflow milestone 最小產出：

- 若這輪調整的是全局流程，而非單一 area，需明講它改進了哪一層 pipeline
- 若這輪吸收 `ref/` 新建議，需判定它是「立即生效的 contract」還是「延後落地的 roadmap item」
- 若新增規則會影響既有 skill reference、tracker 或單區 template，需同時記錄誰是新的 authoritative source

## Commit And Review Unit

全局上以「單一 area milestone」作為 commit 與 review 的最小單位。

規則：

- 同一次 commit / review 盡量只包含一個 area 的主要 spec 或 implementation 變更
- 若同時需要改既有邊界 room、`area/directory.lst` 或 docs，仍視為該 area milestone 的一部分
- 除非是純全局 docs / tracker 收尾，否則不要把兩個不同 area 的主要 runtime 變更混在同一輪

這個規則能讓未來若引入 PR、graph diff 或 CI gate 時，不必重構整個工作方式。

## Fixed Prompt

日後延續工作使用固定主 prompt：

`繼續實作下一個待建 area`

規則：

- 若 `area/rebuild_plan.md` 有 `in_progress`，優先續做該區
- 否則選第一個 `todo` 且無 blocker 的 area
- 這裡的 `next area` 一律解讀為 next actionable area，而不是 candidate queue 的下一個新候選
- 因此只要 `in_progress` 仍存在，就不得切到下一個 `todo`；除非目前區域已轉成 `done`、`blocked` 或 `abandoned`

Agent loop 可視為：

1. 讀 `area/rebuild_plan.md`
2. 取 `in_progress`，否則取第一個可做的 `todo`
3. 讀對應單區 plan
4. 更新或驗證 `map.md`
5. 投影 `.roo` 並補 runtime data
6. 做對應 validation
7. 依結果更新 `delivery_gate`
8. 只有在 gate 允許時才結束當前區或移往下一區

## Candidate Order

依 `area/world_map.md` 目前排序，第一批新 AREA 候選為：

1. `loyang_outskirts`
2. `beiping_outskirts`
3. `jingxiang_road`
4. `wild_longqu_hills`
5. `dng_loyang_sewer`
6. `dng_sewer_depths`
7. `dng_royal_tomb`
8. `sec_catacomb_depths`
9. `sec_rift_below`
10. `sec_rift_core`
11. `sec_rift_deeps`
12. `sec_rift_abyss`
13. `sec_rift_nadir`

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
- `dng_sewer_depths`
  - theme: `詭異民俗風`
  - subtheme: `深層水道`
  - 缺口角色：補洛陽地下水區之下的真正深層水道，讓地下鏈可以從前哨延伸到封印與機關痕跡更重的 deeper section
- `dng_royal_tomb`
  - theme: `探險遺跡`
  - subtheme: `古墓 / 機關`
  - 缺口角色：補深層水道下方的帝王古墓段，讓洛陽地下鏈能從水道系統自然轉入古墓與機關秘境
- `sec_catacomb_depths`
  - theme: `仙俠`
  - subtheme: `地穴 / 靈異`
  - 缺口角色：補帝王古墓底下的靈異地穴與異象核心，讓洛陽地下鏈在古墓之後再延伸出 secret zone
- `sec_rift_below`
  - theme: `仙俠`
  - subtheme: `裂谷 / 異象秘境`
  - 缺口角色：補忘川地穴下方的更深異象裂谷與秘境底層入口，讓洛陽地下鏈在 secret zone 之後還能延伸到更高風險的下層探索帶
- `sec_rift_core`
  - theme: `仙俠`
  - subtheme: `心核 / 裂谷底層`
  - 缺口角色：補異象裂谷沉門下方的裂谷心核與祕境底層核心，讓洛陽地下鏈能在更深層形成一個真正的高風險終點與後續延伸樞紐
- `sec_rift_deeps`
  - theme: `仙俠`
  - subtheme: `裂界 / 深層封印`
  - 缺口角色：補裂谷心核封界下方的更深裂界與深層封印帶，讓洛陽地下鏈在心核之後仍保有更下層的延伸空間
- `sec_rift_abyss`
  - theme: `仙俠`
  - subtheme: `禁底 / 封印底座`
  - 缺口角色：補裂界深層禁底界井下方的實際落地區，讓洛陽地下鏈從「下探預留」轉成可探索的禁底段
- `sec_rift_nadir`
  - theme: `仙俠`
  - subtheme: `禁底 / 裂界禁牢`
  - 缺口角色：補裂界禁底下方的真正禁牢段，讓洛陽地下鏈在禁底之後仍可延伸到封印核心前帶

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
- 全局流程已明確區分 `world graph / queue / area plan / area spec / runtime validation / delivery gate`
- `ref/mud-new-area-full-recommendations.md` 的建議已被收斂成 capability matrix，而不是散落的願望清單
- 缺的文件 / template / schema / tool / prompt 已被整理成 staged roadmap，且不會被誤認為既有硬性 gate
- workflow 文件、template、schema 或 validator 若升級，相關 skill 與 `agents/openai.yaml` 也有明確同步責任，不再讓人機入口漂開
- 後續若導入 PR、graph diff 或 CI，不需要推翻現有 area rebuild 工作方式

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
7. 建立下一個新 AREA 前，先為它選定從 `xx01` 起跳的 `reserved_room_block`，並確認該 block 尚未與現有 `area/`、`src/`、`data/` 中的 room vnum 使用情況衝突

## Systemization Roadmap

`ref/mud-new-area-full-recommendations.md` 的核心價值不是叫 repo 一次長出三十幾個檔，而是提醒我們把 area rebuild 流程逐步系統化。這個 roadmap 把那些建議收斂成「何者先補、何者延後」。

目前這條 roadmap 已由 `plans/0005-area-skill-data-systemization.md` 承接下一步實作，特別把 skill canonical source、per-area content pilot 與 generated read model / runtime audit 分工明確化；本段保留全局脈絡與提升規則，細部落地以 `0005` 為準。

總原則：

- 新文件或工具要補目前 workflow 的實際缺口，不是為了湊齊建議清單
- 既有腳本可延伸時，優先延伸既有腳本，不先複製出功能重疊的新檔名
- 只有當文件或工具已穩定、被反覆使用，才把它升格成正式 gate 或 authoritative source

### Stage 1: Governance And Contracts

先補最直接影響固定 prompt 與單區續跑安全性的文件契約：

- `docs/area-development-handbook.md`
  - 把本計畫、skill reference 與 tracker 共同遵守的 area 開發骨架整理成單一入口
- `docs/area-delivery-gates.md`
  - 把 `spec_in_progress -> validated_ready_to_advance` 的語意獨立寫清楚
- `docs/area-vnum-policy.md`
  - 把 `reserved_room_block`、`planned_vnum_range`、extension block 規則抽成可引用文件
- `docs/area-external-exit-policy.md`
  - 把 external exit、boundary room patch、spec/runtime 同步責任說清楚
- `docs/area-acceptance-checklist.md`
  - 把 implementation ready 與 validated ready 所需證據列成最小 checklist
- `docs/codex-area-workflow.md`
  - 把固定 prompt、branch policy、commit/review unit 與 tracker update 規則整理給 agent 使用

Stage 1 的目標不是取代 `AGENTS.md` 或 skill，而是讓 repo 內有一份對人類協作者也容易回讀的正式入口。

同步要求：

- Stage 1 文件若新增 authoritative rule，需同步檢查 `.agents/skills/merc-area-builder/SKILL.md`
- 若 skill 的使用入口、工作流摘要或預設提示因此改變，需同步更新 `.agents/skills/merc-area-builder/agents/openai.yaml`
- skill 與文件之間若有重複說明，skill 保留最小 workflow 與導覽，細節優先沉到 `references/` 或 repo docs，避免重複維護

### Stage 2: Templates And Schemas

當 Stage 1 規則穩定後，再補模板與 schema，降低單區 plan / spec 格式漂移：

- `templates/area-plan.template.md`
- `templates/map.md.template`
- `templates/area-readme.template.md`
- `templates/new-area-checklist.template.md`
- `schemas/mapmd-json.schema.json`
- `schemas/area-plan.schema.json`

落地原則：

- template 應反映本計畫已固定的欄位，不得自創另一套命名
- `mapmd-json` schema 要對齊 generator 現況，特別是 direction、`external: true`、cluster 與 metadata 欄位
- `area-plan` schema 只驗欄位完整度與基本型別，不應把設計判斷硬編成機械規則

### Stage 3: Validation And Bootstrap Tools

等格式穩定後，再擴充工具層，優先順序如下：

1. 補強既有 validator
   - 優先延伸 `scripts/world_consistency_checker.py`
   - 目標：逐步補強 VNUM、exit、boundary、`directory.lst` 與 area reachability 診斷
2. 補 `mapmd` 專用 validator
   - 可考慮新增 `tools/mapmd_validate.py`
   - 目標：在 generator 前先做更明確的 spec 錯誤摘要
3. 補 vnum allocator
   - 可考慮新增 `tools/area_vnum_allocator.py`
   - 目標：用 repo 現況掃描建議下一段 `reserved_room_block`
4. 補 smoke runner 與 log 摘要
   - 可考慮新增 `tools/area_smoke_test_runner.py`、`tools/log_parse_summary.py`
   - 目標：標準化 `debug/*` 基線、timeout、最新 log 解析與成功訊號回報
5. 補 acceptance / tracker helper
   - 可考慮新增 `tools/area_acceptance_gate.py`、`tools/update_rebuild_tracker.py`
   - 目標：產出 gate 建議，但最後是否前進仍由人工判讀
6. 補 bootstrap / patch 建議器
   - 可考慮新增 `tools/area_scaffold_generator.py`、`tools/area_patch_existing_world.py`
   - 目標：降低新 area 起手與接回既有世界時的人工作業量

這一階段的重點是「輔助」而不是「取代」：新工具應輸出可 review 的建議或摘要，而不是默默寫一堆不可追溯的 area 資料。

目前進度補充：

- `tools/mapmd_validate.py` 已有第一版，可復用現有 generator 驗證並補 metadata 檢查
- `tools/area_vnum_allocator.py` 已有第一版，可掃描 runtime room files 與已記錄保留段後給出 block 建議
- `tools/log_parse_summary.py` 已有第一版，可摘要成功訊號、常見 loader 關鍵字與 `debug/*` 非空檔案
- `tools/area_acceptance_gate.py` 已有第一版，可根據 spec/runtime/log-debug 證據給出保守 gate 建議
- 其餘 Stage 3 工具仍保留在 roadmap，不視為既有硬性 gate

### Stage 4: Prompt, Diff, And CI Packaging

最後才處理比較適合在流程成熟後補齊的包裝層：

- `prompts/new-area-master-prompt.md`
- `prompts/new-area-spec-prompt.md`
- `prompts/new-area-implementation-prompt.md`
- `prompts/new-area-validation-prompt.md`
- `prompts/fix-area-load-error-prompt.md`
- `docs/pr-template-new-area.md`
- `tools/world_graph_diff.py`
- `scripts/validate_area.sh`
- `scripts/validate_world.sh`
- `scripts/ci_validate_new_area.sh`

這些項目適合作為後期標準化產物，但前提是：

- 單區 plan contract 已穩定
- validator 與 smoke test 已有足夠低誤判率
- 團隊真的需要跨多人 / PR / CI 重複使用這些包裝層

## Tooling Promotion Rules

為了避免 roadmap 一邊寫、一邊把半成品誤升成硬規則，新增下列提升條件：

- 文件提升為 authoritative source 前，需先確認不會和 `AGENTS.md`、skill reference、現有 `plans/` 規則衝突
- 工具提升為正式 gate 前，至少要經過多個 area milestone 驗證，且誤判成本低於人工檢查
- 若某個功能已可合理併入現有腳本，例如 `generate_roo_from_map_md.py` 或 `world_consistency_checker.py`，優先擴充原檔，不優先創造同義工具
- world graph diff、CI 與 PR 模板屬於流程成熟後的加速器，不是第一輪 area rebuild 成敗的前置條件

## Assumptions

- `plans/` 是正式規劃區，不是臨時草稿區
- `area/rebuild_plan.md` 與 `plans/` 分工明確：前者追蹤狀態，後者保存決策完整的計畫
- 未來若有技能或工具專題，可再新增 `plans/skills/`、`plans/tools/`，但目前先只使用 `plans/` 與 `plans/area/`
