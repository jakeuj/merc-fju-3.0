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

## Mob Authoring Guardrails

- `mob/*.mob` 的 `Name` 是必填欄位，也是玩家與 loader 拿來比對的最短關鍵名字；預設維持英文或至少 ASCII-friendly token，中文顯示名放在 `ShortDesc` / `Description`
- `mob/*.mob` 的 `Level` 要分清楚兩層規則：
  - legacy `document/mob.txt`：把 `100` 視為平衡上的傳統上限
  - current loader：接受 `1..120`，會把 `<= 0` 或 `> 120` 視為 `Load_mobiles` blocker
- tracker 的 area rebuild authoring policy 一律把 `1..100` 當交付上限；不要因為 loader 接受 `120`，就把 `101..120` 延續成新建 area 的通用做法
- 若在新建或最近重建的 area 內看到 `>100`，預設視為 drift，先修回 `<=100` 再前進 milestone
- 若本輪 smoke test 出現 `Load_mobiles﹕怪物 %d 沒有名字。` 或 `Load_mobiles﹕怪物 %d 等級 %d 不合理。`，先留在當前 area 修正 `Name` / `Level`，不要跳下一區
- `95..100` 是晚期 plateau endgame band；未來若還要往更深層擴寫，預設應靠 encounter 結構、資源壓力、抗性或路線壓迫加強，而不是把怪物等級推到 `101+`

## Level Range Alignment

- 單區 plan 的 `level_range`、`area/<area>/map.md` 的 `LevelRange` 與 `mapmd-json.area.level_range` 必須一致
- 若 area 已建立 `content.json`，`balance_metadata.planned_level_range` 也應與同一組數值對齊
- 若 runtime `mob/*.mob` 已存在，實際怪物等級至少要落在宣告的 `level_range` 內；若不一致，先修 spec 或 runtime 再前進 milestone

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
- 歷史重建補充：`https://3yrebuildnote.blogspot.com/2013/04/blog-post.html`
- 玩家 leveling baseline：`https://disp.cc/b/mud_3y/2mUG`

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
- 若 `players.json / skills.json` 仍無法說明 historical rebuild-era 的 level band、城市規模或區域優先序，可補讀 `https://3yrebuildnote.blogspot.com/2013/04/blog-post.html`，但只能當補充脈絡，不得覆蓋 `world_map`、`ref/` 與 current repo state。
- 若要校對玩家實際感知的練功帶，可補讀 `https://disp.cc/b/mud_3y/2mUG`；這類社群資料只用來做 `level_range` sanity check，不直接決定 queue。
- 若這輪是因為 docs dataset 才決定某個新候選區、world link 或服務節點配置，記得在單區 plan / tracker 補上：
  - `ref_inputs_used`
  - `ref_inputs_deferred`
  - `theme_basis`
  - `compliance_check`
- `docs/3yWebsite` 仍視為 reference-only 舊站鏡像；若未來真的改動現行 runtime 的 area / skill registry，要另同步 `docs/current-game/*`。

## Queue Variety Gate

- 當 `candidate queue`、`todo`、`in_progress` 全為空時，禁止把「最新完成 area 的預留 `world link`」直接視為 next actionable area
- 新的 next actionable area 必須先一起盤點：
  - `area/world_map.md`
  - `ref/sanguo-progression-map.md`
  - `ref/三國-MUD-題材分布表.md`
  - `docs/3yWebsite/docs/data/players.json`
  - `docs/3yWebsite/docs/data/skills.json`
- active queue 預設要交錯配置 `City / Wild / Dungeon / Fort` 等不同 family，不得連續安排三個同 family area
- 若新候選區只能回答「更深、更暗、更滿級」，但補不出新的玩家 loop、交通價值或題材差異，不得放進 `todo`
- `sec_rift_spirit_core_*` 晚期鏈在 `sec_rift_spirit_core_gehennal` 暫停；未來若要恢復，必須先建立獨立的 endgame world-design 任務

## Fixed Prompt

日後延續工作使用固定主 prompt：

`繼續實作下一個待建 area`

執行規則：

- 若 `in_progress` 區塊有項目，優先續做該區
- 否則從 `todo` 區塊選第一個沒有 blocker 的 area
- 若 `candidate queue`、`todo`、`in_progress` 全為空，先重建 queue 與 `todo`
- 若當前區塊完成，更新本檔後再移動到下一區
- 這套流程中的 `next area` 指的是 next actionable area，不是 candidate queue 的下一個新名字
- 因此只要仍存在 `in_progress` 項目，就不得跳去下一個 `todo`；除非目前區域已明確標成 `done`、`blocked` 或 `abandoned`
- 若使用者只說「繼續下一個 area / next area」，預設語意仍是「續做目前可執行的 area」，不是直接切換到候選序列的下一個新區
- 每次從 `todo` 推進到 `in_progress`，或完成一輪單區實作後，都要同步檢查對應單區 plan 是否已補上 `ref_inputs_used / ref_inputs_deferred / theme_basis / compliance_check`
- 若 queue 為空，不得把最新完成 area 的 `down` / 預留 world link 直接當成下一區；必須先回到 `world_map + progression + players/skills` 盤點

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

- `city_chenliu`
  - area_family: `City`
  - reserved_room_block: `13801-13830`
  - level_range: `15-26`
  - theme: `歷史城市`
  - subtheme: `中原樞紐城 / 軍旅與江湖中繼`
  - ref_inputs_used:
    - `area/world_map.md`
    - `ref/sanguo-progression-map.md`
    - `ref/三國-MUD-題材分布表.md`
    - `docs/3yWebsite/map/chenliu.html`
    - `docs/3yWebsite/docs/data/players.json`
    - `docs/3yWebsite/docs/data/skills.json`
    - `https://3yrebuildnote.blogspot.com/2013/04/blog-post.html`
    - `https://disp.cc/b/mud_3y/2mUG`
    - `ref/mud-area-templates/city_loyang.md`
    - `ref/sanguo-area-specfirst/area/city_chenliu/map.md`
  - ref_inputs_deferred:
    - `mud-world-builder/`
    - `mud-ai-map-generator/`
    - `mudlet-map-generator/`
    - `mud-world-map-editor/`
    - `mud-world-map-editor-pro/`
    - 各類經濟/勢力/歷史事件模擬系統
    - `sec_rift_spirit_core_*` 晚期鏈模板
  - theme_basis:
    - `sanguo-progression-map` 的 Lv15 主線城市槽位
    - `題材分布表` 的歷史城市主節點
    - 陳留舊站地圖的服務節點密度
    - `players.json / skills.json` 提供的師父、補給與旅行 loop
    - 歷史重建筆記顯示陳留曾先以大型 `roo` 與基本設施 NPC 為重建起點，支持本區先做 service backbone、後續再擴房
    - 玩家 leveling 文把陳留列在 `Lv15-21`，支持本區作為 midgame 低段主線城市的強度帶
  - compliance_check:
    - compliant；本區是主世界 queue reset 的第一個正式 `todo`，明確從晚期 spirit-core 深井鏈切回三國城市節奏
- `wild_puyang_forest`
  - area_family: `Wild`
  - reserved_room_block: `13901-13930`
  - level_range: `20-30`
  - theme: `探險`
  - subtheme: `中原林野 / 官渡前哨外圍`
  - ref_inputs_used:
    - `area/world_map.md`
    - `ref/sanguo-progression-map.md`
    - `ref/三國-MUD-題材分布表.md`
    - `ref/sanguo-area-specfirst/area/road_puyang/map.md`
    - `ref/sanguo-area-specfirst/area/city_puyang/map.md`
  - ref_inputs_deferred:
    - `docs/3yWebsite/docs/data/players.json`
    - `docs/3yWebsite/docs/data/skills.json`
    - 各類原型工具與模擬系統
  - theme_basis:
    - `city_chenliu` 之後的野外承接帶
    - 濮陽與官渡之間需要戰前探索型練功區
  - compliance_check:
    - compliant；與前一個 `City` 形成題材切換，不沿用深井鏈
- `dng_guandu_battlefield`
  - area_family: `Dungeon`
  - reserved_room_block: `14001-14030`
  - level_range: `24-34`
  - theme: `軍旅`
  - subtheme: `古戰場 / 官渡鏖兵`
  - ref_inputs_used:
    - `area/world_map.md`
    - `ref/sanguo-progression-map.md`
    - `ref/三國-MUD-題材分布表.md`
    - `ref/mud-area-templates/dng_royal_tomb.md`
  - ref_inputs_deferred:
    - `docs/3yWebsite/docs/data/players.json`
    - `docs/3yWebsite/docs/data/skills.json`
    - 各類原型工具與模擬系統
  - theme_basis:
    - progression 主線的官渡戰場位置
    - 題材從林野轉向戰地 dungeon
  - compliance_check:
    - compliant；提供戰場型 dungeon，而不是再做一個地下深井
- `fort_hulao`
  - area_family: `Fort`
  - reserved_room_block: `14101-14120`
  - level_range: `28-36`
  - theme: `軍旅`
  - subtheme: `東都門戶 / 虎牢雄關`
  - ref_inputs_used:
    - `area/world_map.md`
    - `ref/sanguo-progression-map.md`
    - `ref/mud-area-templates/fort_hulao.md`
    - `ref/sanguo-area-specfirst/area/fort_hulao/map.md`
  - ref_inputs_deferred:
    - `docs/3yWebsite/docs/data/players.json`
    - `docs/3yWebsite/docs/data/skills.json`
    - 各類原型工具與模擬系統
  - theme_basis:
    - `world_map` 的戰略 choke point
    - 模板成熟度高，適合作為 queue reset 後的高辨識度軍事關卡
  - compliance_check:
    - compliant；屬於明確三國關隘，不是抽象 endgame 秘境
- `city_xiangyang`
  - area_family: `City`
  - reserved_room_block: `14201-14230`
  - level_range: `35-45`
  - theme: `歷史城市`
  - subtheme: `荊州門戶 / 軍旅樞紐`
  - ref_inputs_used:
    - `area/world_map.md`
    - `ref/sanguo-progression-map.md`
    - `ref/三國-MUD-題材分布表.md`
    - `ref/sanguo-area-specfirst/area/city_xiangyang/map.md`
  - ref_inputs_deferred:
    - `docs/3yWebsite/map/shanyan.html`
    - `docs/3yWebsite/docs/data/players.json`
    - `docs/3yWebsite/docs/data/skills.json`
    - 各類原型工具與模擬系統
  - theme_basis:
    - 主線往荊州推進的城市樞紐
    - 與 `fort_hulao` 形成軍事關卡後的城市回補節奏
  - compliance_check:
    - compliant；維持 `City -> Wild/Dungeon/Fort -> City` 節奏
- `wild_jiangxia_river`
  - area_family: `Wild`
  - reserved_room_block: `14301-14330`
  - level_range: `40-50`
  - theme: `探險`
  - subtheme: `江夏水道 / 水軍河岸`
  - ref_inputs_used:
    - `area/world_map.md`
    - `ref/sanguo-progression-map.md`
    - `ref/三國-MUD-題材分布表.md`
    - `ref/sanguo-area-specfirst/area/city_jiangxia/map.md`
  - ref_inputs_deferred:
    - `docs/3yWebsite/docs/data/players.json`
    - `docs/3yWebsite/docs/data/skills.json`
    - 各類原型工具與模擬系統
  - theme_basis:
    - 由襄陽往江夏延伸的水路野外
    - 以河道、水軍與交通風險提供主線後段變化
  - compliance_check:
    - compliant；以水域野外收束第一輪重排 queue，不延續 spirit-core 尾鏈

## Todo

(目前無 `todo` 項目。)

## In Progress

- `dng_guandu_battlefield`
  - plan: `plans/area/0055-dng-guandu-battlefield.md`
  - delivery_gate: `implementation_ready_for_commit`
  - current_status:
    - 已建立最小 loadable runtime scaffold：`index / mob / obj / res / shp / roo`
    - 已將 `13912 <-> 14001` 落成 `wild_puyang_forest` 與 `dng_guandu_battlefield` 的雙向 runtime boundary
    - `tools/mapmd_validate.py`、generator `--validate-only`、generator write 均已通過
    - WSL Linux build 與 startup smoke test 已通過；成功 log 為 `log/1020.log`
    - `debug/badobject` 為空，`debug/error` 只有 timeout 強制關機紀錄
  - next_action:
    - 先 commit `dng_guandu_battlefield` 的 implementation milestone
    - commit 後把 `dng_guandu_battlefield` 移到 done
    - 接著開始 `fort_hulao` 的 spec milestone


## Done

- `2026-03-20` `dng_guandu_battlefield` 已完成第一輪 runtime implementation 待 commit，已完成 WSL Linux build 與 startup smoke test，下一步是提交 implementation milestone 後前進 `fort_hulao`
- `2026-03-20` `wild_puyang_forest` 已完成第一輪 runtime implementation、commit `a9c7398`，完成 WSL Linux build 與 startup smoke test，並達成可前進下一區狀態
- `2026-03-20` `city_chenliu` 已完成第一輪 runtime implementation、commit `e6756ff`，完成 WSL Linux build 與 startup smoke test，並達成可前進下一區狀態

- `2026-03-20` 已正式凍結 `sec_rift_spirit_core_*` 晚期尾鏈的自動續寫流程，active queue 改回 `City / Wild / Dungeon / Fort` 交錯的三國主線節奏，並把 `city_chenliu` 設為下一個正式 `todo`
- `2026-03-19` 已完成晚期 `sec_rift_*` 鏈的 `82-100` plateau 重壓縮，對齊 `plans/area/*`、`map.md`、`mapmd-json` 與 runtime `mob/*.mob`，並補上 `tools/mapmd_validate.py` 的 `level_range` / runtime / `content.json` guardrail
- `area/world_map.md` 已建立，並整合 `help/map.hlp`、`docs/3yWebsite/docs/maps.md`、`docs/3yWebsite/docs/data/maps.json`、`docs/3yWebsite/map/*.html`
- `docs/current-game/areas.md` 與 `docs/current-game/areas.json` 已建立，整理目前 loadable runtime area registry 與重建鏈摘要
- `plans/0005-area-skill-data-systemization.md` 已完成 v1，建立 structured skill source、`loyang_outskirts` area content pilot 與 exporter-based runtime round-trip 流程
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
- `plans/area/0023-sec-rift-sealed-core-heart.md` 已建立
- `sec_rift_sealed_core_heart` 已完成第一輪 implementation、commit `da76474`，完成本機 Linux build 與 smoke test，並達成可前進下一區狀態
- `plans/area/0024-sec-rift-core-spirit-nadir.md` 已建立
- `sec_rift_core_spirit_nadir` 已完成第一輪 implementation、commit `1c77c8b`，完成本機 Linux build 與 smoke test，並達成可前進下一區狀態
- `plans/area/0025-sec-rift-core-spirit-abyss.md` 已建立
- `sec_rift_core_spirit_abyss` 已完成第一輪 implementation、commit `677db5b`，完成本機 Linux build 與 smoke test，並達成可前進下一區狀態
- `plans/area/0026-sec-rift-spirit-core-hollow.md` 已建立
- `sec_rift_spirit_core_hollow` 已完成第一輪 implementation、commit `813fb02`，完成本機 Linux build 與 smoke test，並達成可前進下一區狀態
- `plans/area/0027-sec-rift-spirit-core-void.md` 已建立
- `sec_rift_spirit_core_void` 已完成第一輪 implementation、commit `8179a01`，完成本機 Linux build 與 smoke test，並達成可前進下一區狀態
- `plans/area/0028-sec-rift-spirit-core-vacuum.md` 已建立
- `sec_rift_spirit_core_vacuum` 已完成第一輪 implementation、commit `9e670ee`，完成 WSL Linux build 與 smoke test，並達成可前進下一區狀態
- `plans/area/0029-sec-rift-spirit-core-null.md` 已建立
- `sec_rift_spirit_core_null` 已完成第一輪 implementation、commit `fb42780`，完成 WSL Linux build 與 smoke test，並達成可前進下一區狀態
- `plans/area/0030-sec-rift-spirit-core-zero.md` 已建立
- `sec_rift_spirit_core_zero` 已完成 spec 建立與 validate-only 驗證，並進入下一段 implementation milestone 準備
- `sec_rift_spirit_core_zero` 已完成 runtime implementation、commit `cc9bd99`，並完成 WSL build 與 smoke test 驗證
- `plans/area/0031-sec-rift-spirit-core-blank.md` 已建立
- `sec_rift_spirit_core_blank` 已完成 runtime implementation、commit `ae1f268`，並完成 WSL build 與 smoke test 驗證
- `plans/area/0032-sec-rift-spirit-core-white.md` 已建立
- `sec_rift_spirit_core_white` 已完成 runtime implementation，完成 WSL build 與 smoke test 驗證
- `plans/area/0033-sec-rift-spirit-core-plain.md` 已建立
- `sec_rift_spirit_core_plain` 已完成 runtime implementation，完成 WSL build 與 smoke test 驗證
- `plans/area/0034-sec-rift-spirit-core-faint.md` 已建立
- `sec_rift_spirit_core_faint` 已完成 runtime implementation，完成 WSL build 與 smoke test 驗證
- `plans/area/0035-sec-rift-spirit-core-trace.md` 已建立
- `sec_rift_spirit_core_trace` 已完成 runtime implementation，完成本機 build 與 smoke test 驗證，並達成可前進下一區狀態
- `plans/area/0036-sec-rift-spirit-core-mote.md` 已建立
- `sec_rift_spirit_core_mote` 已完成 runtime implementation，完成本機 build 與 smoke test 驗證，並達成可前進下一區狀態
- `plans/area/0037-sec-rift-spirit-core-grain.md` 已建立
- `sec_rift_spirit_core_grain` 已完成 runtime implementation，完成本機 build 與 smoke test 驗證，並達成可前進下一區狀態
- `plans/area/0038-sec-rift-spirit-core-last.md` 已建立
- `sec_rift_spirit_core_last` 已完成 runtime implementation，完成本機 build 與 smoke test 驗證，並達成可前進下一區狀態
- `plans/area/0039-sec-rift-spirit-core-final.md` 已建立
- `sec_rift_spirit_core_final` 已完成 runtime implementation，完成本機 build 與 smoke test 驗證，並達成可前進下一區狀態
- `plans/area/0040-sec-rift-spirit-core-terminal.md` 已建立
- `sec_rift_spirit_core_terminal` 已完成 runtime implementation，完成本機 build 與 smoke test 驗證，並達成可前進下一區狀態
- `plans/area/0041-sec-rift-spirit-core-extinct.md` 已建立
- `sec_rift_spirit_core_extinct` 已完成 runtime implementation，完成本機 build 與 smoke test 驗證，並達成可前進下一區狀態
- `plans/area/0042-sec-rift-spirit-core-silent.md` 已建立
- `sec_rift_spirit_core_silent` 已完成 runtime implementation，完成本機 build 與 smoke test 驗證，並達成可前進下一區狀態
- `plans/area/0043-sec-rift-spirit-core-dim.md` 已建立
- `sec_rift_spirit_core_dim` 已完成 runtime implementation，完成本機 build 與 smoke test 驗證，並達成可前進下一區狀態
- `plans/area/0044-sec-rift-spirit-core-gloam.md` 已建立
- `sec_rift_spirit_core_gloam` 已完成 runtime implementation，完成本機 build 與 smoke test 驗證，並達成可前進下一區狀態
- `plans/area/0045-sec-rift-spirit-core-umbral.md` 已建立
- `sec_rift_spirit_core_umbral` 已完成 runtime implementation，完成本機 build 與 smoke test 驗證，並達成可前進下一區狀態
- `plans/area/0046-sec-rift-spirit-core-nether.md` 已建立
- `sec_rift_spirit_core_nether` 已完成 runtime implementation，完成本機 build 與 smoke test 驗證，並達成可前進下一區狀態
- `plans/area/0047-sec-rift-spirit-core-stygian.md` 已建立
- `sec_rift_spirit_core_stygian` 已完成 runtime implementation，完成本機 build 與 smoke test 驗證，並達成可前進下一區狀態
- `plans/area/0048-sec-rift-spirit-core-chthonic.md` 已建立
- `sec_rift_spirit_core_chthonic` 已完成 runtime implementation，完成本機 build 與 smoke test 驗證，並達成可前進下一區狀態
- `plans/area/0049-sec-rift-spirit-core-abysmal.md` 已建立
- `sec_rift_spirit_core_abysmal` 已完成 runtime implementation，完成本機 build 與 smoke test 驗證，並達成可前進下一區狀態
- `plans/area/0050-sec-rift-spirit-core-tartarean.md` 已建立
- `sec_rift_spirit_core_tartarean` 已完成 runtime implementation，完成本機 build 與 smoke test 驗證，並達成可前進下一區狀態
- `plans/area/0051-sec-rift-spirit-core-infernal.md` 已建立
- `sec_rift_spirit_core_infernal` 已完成 runtime implementation，完成本機 build 與 smoke test 驗證，並達成可前進下一區狀態
- `plans/area/0052-sec-rift-spirit-core-gehennal.md` 已建立
- `sec_rift_spirit_core_gehennal` 已完成 runtime implementation，完成本機 build 與 smoke test 驗證，並達成可前進下一區狀態
## Blocked

- none

## Current Recommended Next Step

`dng_guandu_battlefield` 已進入 `implementation_ready_for_commit`。下一步應先 commit 目前的 runtime milestone；commit 後把它移到 done，並開始 `fort_hulao` 的 spec milestone。

## Next Action

- commit `dng_guandu_battlefield` 的 implementation milestone
- commit 後開始 `fort_hulao`：
  - 建立單區 plan
  - 建立 `area/fort_hulao/map.md`
  - 跑 `tools/mapmd_validate.py` 與 generator `--validate-only`

## Next Prompt

`先 commit 目前 dng_guandu_battlefield 的 implementation milestone；commit 後把它標記為 done，再開始 fort_hulao 的 spec milestone。`
