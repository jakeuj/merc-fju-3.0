---
name: merc-area-builder
description: 維護、擴充或搬修 merc-fju-3.0 目前實際存在的區域資料時使用：依 document/README、src/load.c、src/act_move.c 與 area/ 現況處理 limbo、loyang、beiping、new、newfight、pk_area、free_fight 的 index/mob/obj/res/roo/shp 與區域地圖檔結構，將地圖視為包含 north/east/south/west 與 up/down/enter/out 的立體拓樸，並把 #Exit/#Keyword/#Job/#Enquire 視為 room spec 的正式部分；新增 AREA 時先以 map.md 當規格來源，必要時再用 Python scaffold 產生初版 .roo，也支援以 plans/ 與 area/rebuild_plan.md 維護長期 area 重建流程，更新 area/directory.lst、同步檢查 merc.ini 與固定房號/傳送/提示文字，並在需要世界觀、技能、國家或交通背景時搭配 docs/3yWebsite/.agents/skills/sango-docs-service/SKILL.md 取用 docs 與 JSON 資料。
---

# Merc Area Builder

此技能協助你在目前的 `merc-fju-3.0` 工作區內維護或擴充區域資料。優先依 repo 現況工作，不要沿用「scripts 與 area 已被精簡」那條舊假設。

## 三層架構

目前的 `map.md` 設計採三層：

- Authoring layer：`map.md` 內的人類可讀 prose 與嵌入的 `mapmd-json`
- Internal model layer：`mapmd-json` 是 canonical machine-readable graph schema
- Projection layer：目前只有 `.roo`

`map.md` is the design document, while the embedded `mapmd-json` block is the canonical machine-readable graph schema used by generators.

source of truth 要分兩種：

- 人類設計語意的 source of truth = `map.md`
- 機器生成的 canonical source of truth = `mapmd-json`

因此若 prose 和 `mapmd-json` 衝突，generator 一律以 `mapmd-json` 為準，並要求回頭修正 spec，不要讓兩套敘述長期分裂。

## 快速開始
1. 先確認任務是要修改既有區域、搬修舊版內容，還是新增區域。
2. 先讀 `area/directory.lst` 與目標區域目錄，理解實際載入順序與檔案結構。
3. 以 `document/README`、`document/mob.txt`、`document/obj.txt`、`document/room.txt`、`document/reset.txt`、`document/shop.txt` 為主要格式依據；若要確認原始 Merc parser / vnum 習慣，再補看 `doc/area-file-format.txt`、`doc/vnum-assignments.txt`、`doc/merc-release-notes.txt`。
 目前專案使用的是拆目錄資料結構，不是原始單檔 `.are`；若回看 `doc/area-file-format.txt` 裡的 `#AREA/#HELPS/#MOBILES/#OBJECTS/#ROOMS/#RESETS/#SHOPS/#SPECIALS`，要把它當概念對照，不要逐段照抄成 3.0 目錄格式。
4. 需要世界觀、技能、國家系統、交通、公告脈絡時，連同 `docs/3yWebsite/.agents/skills/sango-docs-service/SKILL.md` 一起使用，從 `docs/3yWebsite/docs/*.md` 與 `docs/3yWebsite/docs/data/*.json` 取資料。
5. 若是新增 AREA，先決定是手寫 `.roo`，還是用 `references/map-spec-template.md` + `scripts/generate_roo_from_map_md.py` 走「spec -> scaffold」流程。
6. 若任務需要參考 repo 內的 `ref/` 世界藍圖、spec-first scaffold、world builder 或題材分布資料，先讀 `ref/Readme.md` 當索引，再挑需要的檔案或子資料夾深入。
7. 若任務屬於長期 area 重建，先讀 `plans/` 與 `area/rebuild_plan.md`；詳細規則見 `references/rebuild-workflow.md`。
7.1 若這輪工作有用 `ref/Readme.md` 來做選讀決策，回寫單區 plan 或追蹤看板時，補上 `ref_inputs_used`、`ref_inputs_deferred`、`theme_basis`、`compliance_check`。
8. 修改完成後，至少做靜態搜尋、編碼檢查與必要的啟動/載入驗證，再回報受影響檔案與風險。
9. 若要做 area 載入 smoke test，先清空 `debug/*` 內容並建立本輪 `log/*` 觀察基線，再執行測試；若使用 `timeout`，優先給 `45` 到 `60` 秒；測試後用成功訊號、這輪 log 與新產生的 debug 訊息一起判讀。
10. 若這輪有新增 `mob/*.mob` 或 `obj/*.obj`，不要只靠文件猜 parser 會接受什麼：先比對 repo 內已成功載入的同類範例，特別是 `Class` 常數與 `ITEM_FOOD` / `ITEM_DRINK_CON` 的 `Value*` 欄位，測試成功後仍要檢查 `debug/badobject`。
11. area 設計與純資料實作預設先走快速本機驗證；只有碰到 `src/`、`Makefile*`、`startup*`、`merc.sample.ini`、疑似平台差異，或要替大里程碑做 pre-merge gate 時，才升級到 Ubuntu / Docker 雙平台驗證。
12. 若固定 prompt 要從 `todo` 開始一個新的 area milestone，而目前分支是 `develop` 或 `main`，預設先建立 `codex/<area>-implementation` 分支再開始 spec / implementation；除非使用者明講要直接在主分支上做，或這輪只是 merge 後的極小 docs / tracker 收尾。
13. 每輪 area 工作收尾時，主動做一次「經驗回寫判斷」：單區特殊決策回寫到該 area plan / tracker；可重複踩到的 parser、loader、驗證規則回寫到 `skills/references`；屬於全局 workflow 缺口的，再回寫到全局 plan 或 `rebuild-workflow.md`。

## 主題靈感與沉浸式設計

- 在生成新 AREA、補寫房間描述、NPC、任務、技能、道具、裝備或互動事件時，可以主動借鏡下列題材的敘事節奏、場景意象與玩法結構：
- 歷史 / 演義系：`三國志`、`三國演義`
- 武俠 / 奇幻系：`幻想三國志`、`金庸群俠傳` 與其他相近的華語武俠 RPG 氛圍
- 借鏡的重點是「題材母型」與「玩家感受」：城郊軍營、關隘哨站、江湖門派、奇人異士、失傳秘笈、護送任務、名將傳聞、山寨伏兵、水路暗道、地脈異象等
- 優先把這些靈感轉譯成符合 Merc-FJU 世界的原生內容：房間敘述節奏、地名風格、NPC 身分、支線鉤子、掉落邏輯、技能來源、裝備典故與服務節點
- 若靈感來自受著作權保護的特定作品，預設做「改寫後的致敬／變體」，不要直接整包照抄專有角色名、逐句台詞、完整門派設定或劇情橋段；除非目前 repo / docs 已明確把該名稱視為專案既有 canon
- 若靈感來自歷史人物或《三國演義》這類公共領域題材，仍要優先對齊本專案既有世界線、國家、城市、技能與 help 用語，不要只因典故好用就破壞現有設定一致性
- 在 spec prose 中，不只描述地圖拓樸，也主動寫出「這個節點想讓玩家感受到什麼」：例如軍鎮壓力、郊野詭譎、江湖祕聞、邊關肅殺、地下水道潮濕危險
- 在 room/NPC/quest 設計上，優先讓玩家從文字就能推得出玩法：誰可問路、誰像師父、哪裡像埋伏點、哪個物件可能可檢視、哪句傳聞暗示支線
- 技能、武功、道具與裝備命名可帶有古風、兵法、江湖或異聞色彩，但要避免和既有 `skills.md` / help / docs 的名稱體系衝突；若要新增來源，需同步規劃 teacher、study 物件、掉落或任務導引
- 若一個區域明顯採用某種主題語彙（例如軍旅、俠客、山寨、妖異水脈），就讓房間描述、NPC 口吻、物件命名、遭遇事件與 `#Enquire` 詞彙維持同一語氣，不要風格跳躍
- 若需要題材資料支撐世界觀、地理、國家、技能或玩家導流，優先仍以 `docs/3yWebsite` 與 repo 既有內容為主，再把外部作品當作 flavor inspiration，而不是新的 source of truth
- 若需要可直接套用的主題模板，先讀 `references/theme-design-patterns.md` 這份索引，再按需分流：
- 世界級題材分布與州郡 / 主城 / 郊外 / 秘境配置，讀 `references/theme-world-allocation.md`
- `歷史城市風` / `軍旅風`，讀 `references/theme-patterns-civic-military.md`
- `江湖風` / `仙俠風`，讀 `references/theme-patterns-jianghu-mystic.md`
- `詭異民俗風` / `探險遺跡風`，讀 `references/theme-patterns-folklore-ruins.md`

## 先看目前專案現況

- area / plans / ref / scripts / 舊版對照的 repo 現況，讀 `references/current-repo-state.md`
- 若任務主要是新增 area 或重建既有 area，這份檔案是最值得先補讀的 context reference

## 工作流程

### 1. 盤點目標與耦合
- 先確認是改哪個區：`limbo`、主城（`loyang`、`beiping`）、新手區（`new`、`newfight`）、戰鬥區（`pk_area`、`free_fight`），不同區域耦合不同
- 若任務是長期重建的一部分，先讀 `area/rebuild_plan.md`：
- 有 `in_progress` 就先續做該區
- 否則選第一個 `todo` 且無 blocker 的 area
- 這裡的 `next area` 一律指 next actionable area，不是 candidate queue 的下一個新候選；只要 `in_progress` 還在，就不得自行跳到下一個 `todo`
- 再讀該區的 `delivery_gate`：
- `spec_ready_for_commit` / `implementation_ready_for_commit`：先 commit，不進下一區
- `validated_ready_to_advance`：才可進下一個 `todo`
- `spec_in_progress` / `implementation_in_progress`：續做當前 area
- `blocked`：先處理 blocker
- 對應的決策完整計畫再回到 `plans/` 內的全局或單區 plan
- 先查 `area/directory.lst` 的順序與註解，避免把物件或房間引用到尚未載入的區域
- 先看 `src/act_move.c` 裡目前可用的方向與反向配對；現行實作至少有 `north/east/south/west/up/down/enter/out`，不要假設出口只會是平面四向
- 先看 `src/load.c`，確認 `.roo` 的正式 schema：頂層區塊至少有 `#Exit`、`#Keyword`、`#Job`、`#Enquire`
- 把 `mapmd-json` 當作 canonical machine-readable graph schema 來想，不要把 `.roo` 反過來當設計源頭
- 先檢查目標區是否已有地圖檔（例如 `map`、`map2` 或 `roo/` 內的格狀檔）；若有，先把它當作房間拓樸的事實來源，再回頭查各 `.roo` 出口與描述
- 若牽涉固定房號、出生地、交通、懸賞、教學流程，主動搜尋 `src/`、`etc/`、`data/`、`help/` 是否也要一起改

### 2. 先用現有區域當模板
- 優先比對 `area/loyang`、`area/beiping`、`area/new` 等現存區域，而不是依賴過往已被移除又後來復原前的假設
- 若是新增區域，先建立 `area/<new_area>/map.md` 當設計規格，再從最接近的既有區域複製結構與格式，逐步落地成 `roo` / `mob` / `obj` / `res` / `shp`
- 若是按重建計畫新增 area，先同時讀：
  - `plans/0001-*.md` 這類全局 plan
  - `plans/area/NNNN-*.md` 這類單區 plan
  - `area/world_map.md`
- 若 repo 內存在 `ref/Readme.md`，先用它決定還要不要補讀世界藍圖、題材分布表、單區 template 或 spec-first scaffold 範例
- 若這輪確實是用 `ref/Readme.md` 在做選讀決策，完成後不要只回報「有參考 ref」；要明確回寫：
  - `ref_inputs_used`
  - `ref_inputs_deferred`
  - `theme_basis`
  - `compliance_check`
- `map.md` 是人類可讀 spec；若要用腳本產生 `.roo`，只能使用其中受限、結構化的機器可讀區塊，不能把自由 prose 直接拿去 compile
- 若是搬修舊版資料，先用搜尋確認舊名稱、舊城名、舊勢力詞是否殘留在 `roo`、`mob`、`obj`、`res`、`shp`、help 或 system data
- 若現行 repo 缺資料或看不出原始設計，回查 `https://github.com/jakeuj/merc-fju-2.0-utf8` 的對應路徑，再把需要的內容 mapping 回 3.0

### 3. 處理資料檔
- `index/mob/obj/roo/res/shp/map`、`#Keyword/#Job/#Enquire`、`external: true` 與 scaffold generator 的細則，讀 `references/file-handling-rules.md`
- 若任務重點是修出口、整合新 area、補 `#Enquire`、比對地圖檔或確認 `.roo` schema，這份檔要補讀
- 若任務有新增或修改 `mob/*.mob` / `obj/*.obj`，尤其是 mob `Class` 或特殊 `ItemType`，也要補讀這份檔；不要只照文件猜常數或 `Value*` 欄位，先比對 repo 內已成功載入的同類範例

### 4. 同步系統設定
- `merc.ini`、`variable.c`、`job.c`、`bus/ship/bounty` 與 docs 對照點，讀 `references/system-sync-checks.md`
- 若任務碰到交通、新手導流、技能來源、國家系統或官方敘事，這份檔是必要 reference

### 5. 需要世界觀/參考資料時串接 sango-docs-service
- 何時一起用 `sango-docs-service`、優先 docs / JSON 清單與回報要求，讀 `references/docs-service-integration.md`

## 規劃原則

- 詳細規劃原則、VNUM / 題材 / 互動 / 新手流程 / 國家與世界觀一致性，讀 `references/planning-principles.md`

## 驗證
1. 至少檢查 VNUM / 房號引用、`index/res/shp/roo` 對應與地圖出口一致性
2. 若用了 scaffold script，先跑 `--validate-only`
3. 若是 `spec / plan / tracker` 類工作，通常做到 `--validate-only` 即可，不必為了沒有 runtime 變更的任務硬跑雙平台 build
4. 若是純 area data work，預設先做本機 build + smoke test；只有在碰到 `src/`、跨平台風險、或 merge 前信心 gate 時再補 Ubuntu / Docker
5. 若牽涉交通、新手、技能、國家或世界觀，對照對應 docs / JSON
6. 若環境允許，做實際載入或 smoke test，並確認成功訊號與 `debug/` / `log/` 沒有新增 area 錯誤
7. 完整驗證清單讀 `references/validation-checklist.md`

## 參考資料
- `document/README`
- `document/mob.txt`
- `document/obj.txt`
- `document/room.txt`
- `document/reset.txt`
- `document/shop.txt`
- `doc/area-file-format.txt`
- `doc/vnum-assignments.txt`
- `doc/merc-release-notes.txt`
- `doc/mobprogram-guide.txt`
- `doc/security-features.txt`
- `doc/skills-and-spells-guide.txt`
- `references/area-build-checklist.md`
- `references/historical-large-city-example.md`
- `references/theme-design-patterns.md`
- `references/theme-world-allocation.md`
- `references/theme-patterns-civic-military.md`
- `references/theme-patterns-jianghu-mystic.md`
- `references/theme-patterns-folklore-ruins.md`
- `references/current-repo-state.md`
- `references/file-handling-rules.md`
- `references/system-sync-checks.md`
- `references/docs-service-integration.md`
- `references/planning-principles.md`
- `references/validation-checklist.md`
- `references/rebuild-workflow.md`
- `references/map-spec-template.md`
- `../ref/Readme.md`
- `scripts/generate_roo_from_map_md.py`
- `docs/3yWebsite/.agents/skills/sango-docs-service/SKILL.md`
- 舊版對照：`https://github.com/jakeuj/merc-fju-2.0-utf8`
