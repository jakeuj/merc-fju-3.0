---
name: merc-area-builder
description: 維護、擴充或搬修 merc-fju-3.0 目前實際存在的區域資料時使用：依 document/README、src/load.c、src/act_move.c 與 area/ 現況處理 limbo、loyang、beiping、new、newfight、pk_area、free_fight 的 index/mob/obj/res/roo/shp 與區域地圖檔結構，將地圖視為包含 north/east/south/west 與 up/down/enter/out 的立體拓樸，並把 #Exit/#Keyword/#Job/#Enquire 視為 room spec 的正式部分；新增 AREA 時先以 map.md 當規格來源，必要時搭配 docs/area-development-handbook.md、templates/、schemas/ 與 tools/mapmd_validate.py、tools/area_vnum_allocator.py、tools/log_parse_summary.py、tools/area_acceptance_gate.py 走 spec-first workflow，也支援以 plans/ 與 area/rebuild_plan.md 維護長期 area 重建流程，更新 area/directory.lst、同步檢查 merc.ini 與固定房號/傳送/提示文字，並在需要世界觀、技能、國家、玩家攻略或交通背景時搭配 docs/3yWebsite/.agents/skills/sango-docs-service/SKILL.md，特別利用 docs/3yWebsite/docs/data/players.json 與 skills.json 做 teacher/service loop、技能來源與新手導流決策。
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

## 資料系統化 v1

目前 repo 另外補上一條 `structured source -> exporter -> legacy runtime files` 的 authoring layer，但它是補強既有 flat-file runtime，不是改 loader：

- skill canonical source：`data/structured/skills/skills.json`
- skill exporter：`scripts/export_structured_skills.py`
- current-game skill read model：`docs/current-game/skills.json`
- per-area content pilot：`area/<area>/content.json`
- area content exporter：`scripts/export_area_content.py`

判讀規則：

- area 拓樸與 world links 仍以 `area/<area>/map.md + mapmd-json` 為主
- `content.json` 在 v1 只負責 `mob / obj / res / shp / area-level balance metadata`
- `skill/*.ski`、`skill/skill.lst`、`area/*/{mob,obj,res,shp}` 仍是 runtime artifact，不是新的設計起點
- `docs/current-game/*.json` 與可讀頁預設當 generated read model，不當 editable source of truth

## 快速開始
1. 先確認任務是要修改既有區域、搬修舊版內容，還是新增區域。
2. 先讀 `area/directory.lst` 與目標區域目錄，理解實際載入順序與檔案結構。
3. 以 `document/README`、`document/mob.txt`、`document/obj.txt`、`document/room.txt`、`document/reset.txt`、`document/shop.txt`、`document/title.txt` 為主要格式依據；若希望直接在 GitHub Pages / `docs/` 路徑閱讀，先看 `docs/current-game/legacy-documentation.md`，再依檔種跳到：
 - `document/README` → `docs/current-game/legacy-readme.md`
 - `document/mob.txt` → `docs/current-game/mobile-file-format.md`
 - `document/obj.txt` → `docs/current-game/object-file-format.md`
 - `document/room.txt` → `docs/current-game/room-file-format.md`
 - `document/reset.txt` → `docs/current-game/reset-file-format.md`
 - `document/shop.txt` → `docs/current-game/shop-file-format.md`
 - `document/title.txt` → `docs/current-game/title-file-format.md`
 - `document/COPYRIGHT` → `docs/current-game/copyright-notice.md`
 若要確認原始 Merc parser / vnum 習慣，再補看 `doc/area-file-format.txt`、`doc/vnum-assignments.txt`、`doc/merc-release-notes.txt`。
 目前專案使用的是拆目錄資料結構，不是原始單檔 `.are`；若回看 `doc/area-file-format.txt` 裡的 `#AREA/#HELPS/#MOBILES/#OBJECTS/#ROOMS/#RESETS/#SHOPS/#SPECIALS`，要把它當概念對照，不要逐段照抄成 3.0 目錄格式。
4. 需要世界觀、技能、國家系統、交通、公告脈絡時，連同 `docs/3yWebsite/.agents/skills/sango-docs-service/SKILL.md` 一起使用，從 `docs/3yWebsite/docs/*.md` 與 `docs/3yWebsite/docs/data/*.json` 取資料。
4.1 若任務是在規劃新 area、補 teacher NPC、重排 world link、補新手導流或設計職業服務節點，優先抽查兩份舊站資料：
 - `docs/3yWebsite/docs/data/players.json`：看玩家攻略實際反覆提到哪些 NPC、升級 loop、轉職與補給動線。
 - `docs/3yWebsite/docs/data/skills.json`：看技能鏈、技能分類、資源消耗、可否教導與舊版命名。
4.2 使用這兩份 JSON 時，預設把它們當「舊站 reference baseline」，不是現行 runtime registry；若本輪真的改了現行可載入資料，另同步 `docs/current-game/*`。
4.1 若這輪會新增、移除、重排或大幅重寫目前實際可載入的 area，除了 runtime / spec 檔，也同步檢查 `docs/current-game/areas.md` 與 `docs/current-game/areas.json` 是否要更新；若只是引用舊站地圖或世界觀，仍不要把 `docs/3yWebsite/` 當現行 area 台帳。
5. 若是新增 AREA，先決定是手寫 `.roo`，還是用 `references/map-spec-template.md` + `scripts/generate_roo_from_map_md.py` 走「spec -> scaffold」流程。
6. 若任務需要參考 repo 內的 `ref/` 世界藍圖、spec-first scaffold、world builder 或題材分布資料，先讀 `ref/Readme.md` 當索引，再挑需要的檔案或子資料夾深入。
7. 若任務屬於長期 area 重建，先讀 `plans/` 與 `area/rebuild_plan.md`；詳細規則見 `references/rebuild-workflow.md`。
7.1 若這輪工作有用 `ref/Readme.md` 來做選讀決策，回寫單區 plan 或追蹤看板時，補上 `ref_inputs_used`、`ref_inputs_deferred`、`theme_basis`、`compliance_check`。
8. 若任務是在建立新區 workflow 或新 area 起手，優先讀 `docs/area-development-handbook.md`，並視需要使用：
- `templates/area-plan.template.md`
- `templates/map.md.template`
- `templates/area-readme.template.md`
- `templates/new-area-checklist.template.md`
- `schemas/mapmd-json.schema.json`
- `schemas/area-plan.schema.json`
- `schemas/skill-registry.schema.json`
- `schemas/area-content.schema.json`
- `data/structured/skills/skills.json`
- `scripts/export_structured_skills.py`
- `scripts/export_area_content.py`
9. 修改完成後，至少做靜態搜尋、編碼檢查與必要的啟動/載入驗證，再回報受影響檔案與風險。
10. 若這輪是 spec / plan / tracker work，先用 `tools/mapmd_validate.py` 驗 `map.md`；若是新 area 規劃房號，優先用 `tools/area_vnum_allocator.py` 估下一段 `reserved_room_block`。
11. 若已做 runtime smoke test，除了人工看 `log/*` 與 `debug/*`，也可用 `tools/log_parse_summary.py` 做摘要；若要快速判讀目前較像 `implementation_ready_for_commit` 還是 `validated_ready_to_advance`，可先用 `tools/area_acceptance_gate.py` 取保守建議。
12. 若要做 area 載入 smoke test，先清空 `debug/*` 內容並建立本輪 `log/*` 觀察基線，再執行測試；若使用 `timeout`，優先給 `45` 到 `60` 秒；測試後用成功訊號、這輪 log 與新產生的 debug 訊息一起判讀。
13. 若這輪有新增 `mob/*.mob` 或 `obj/*.obj`，不要只靠文件猜 parser 會接受什麼：先比對 repo 內已成功載入的同類範例，特別是 `Class` 常數與 `ITEM_FOOD` / `ITEM_DRINK_CON` 的 `Value*` 欄位，測試成功後仍要檢查 `debug/badobject`。若同時新增怪物會 `Enable` 的技能，還要把它視為 loader-risk data change，而不只是 area 純資料。
13.1 新增或修改 `mob/*.mob` 時，先回看 `document/mob.txt` 的 `Name` / `Level` 契約：`Name` 是必填、最短、供指令比對的關鍵名字，預設應維持英文或至少 ASCII-friendly token；中文呈現放在 `ShortDesc` / `Description`，不要把 `Name` 寫成純中文。`Level` 的 legacy 文件仍以 `100` 為平衡上限，但目前 `src/load.c` 的 loader 會擋掉 `<= 0` 或 `> 120`；因此 area rebuild 預設把 `1..100` 視為一般設計帶，`101..120` 只留給明確規劃過的 late-game / endgame 區，且要在單區 plan、tracker 或 area `index` 說明理由。
13.2 若這輪主要是在消化 `document/mob.txt` 或大量搬修 `mob/*.mob`，不要每次整份 legacy 文件重讀到底；按需求分流：
- 基本檔案骨架、區塊順序與 `End/~` 結構，讀 `references/mob-file-layout.md`
- `Vnum/Name/ShortDesc/Level/Enable/AutoEnable/Special` 等主欄位，讀 `references/mob-core-fields.md`
- `#Learn/#Job/Program/Process`，讀 `references/mob-teaching-and-programs.md`
- Act / Effect / Sex / Class / Position 常數，讀 `references/mob-flags-and-constants.md`
14. 新增 `skill/*.ski` 時，至少同步檢查四個登錄點：`src/merc.h` 的 `SLOT_*`、`skill/skill.lst`、`data/symbol.def`、實際的 `skill/<letter>/<name>.ski`。`skill.lst` key、技能 `Name` 與檔名路徑都必須和 repo 內既有技能全域唯一，避免覆蓋舊技能或造成 `Load_skill` 重覆載入。
14.1 若這輪是在調整目前 repo 真正會載入的 skill runtime data，預設先改 `data/structured/skills/skills.json`，再跑 `python -X utf8 scripts/export_structured_skills.py --check`；需要落地時再用 `--write` 回寫 `skill/skill.lst` 與 `skill/*.ski`，不要把 `docs/current-game/skills.json` 當手編來源。
14.2 若這輪是在調整既有 area 的 `mob / obj / res / shp`，而該區已建立 `content.json`，預設先改 `area/<area>/content.json`，再跑 `python -X utf8 scripts/export_area_content.py <area_slug> --check`；目前 v1 pilot 只保證 `area/loyang_outskirts/content.json`。
15. area 設計與純資料實作預設先走快速本機驗證；只有碰到 `src/`、`Makefile*`、`startup*`、`merc.sample.ini`、疑似平台差異，或要替大里程碑做 pre-merge gate 時，才升級到 Ubuntu / Docker 雙平台驗證。若這輪有新增 skill、改 mob `Enable` 鏈，或碰到 loader 相關警告，至少要補實際載入 smoke test，不可只停在靜態比對。
15.1 若這輪有改 `mob/*.mob`，smoke test / log 判讀時主動搜尋 `Load_mobiles﹕怪物 %d 沒有名字。` 與 `Load_mobiles﹕怪物 %d 等級 %d 不合理。` 這兩類訊息；前者通常代表 `Name` 缺失或格式錯，後者代表 `Level` 超出 loader 可接受的 `1..120` 範圍。
16. 若固定 prompt 要從 `todo` 開始一個新的 area milestone，而目前分支是 `develop` 或 `main`，預設先建立 `codex/<area>-implementation` 分支再開始 spec / implementation；除非使用者明講要直接在主分支上做，或這輪只是 merge 後的極小 docs / tracker 收尾。
17. 每輪 area 工作收尾時，主動做一次「經驗回寫判斷」：單區特殊決策回寫到該 area plan / tracker；可重複踩到的 parser、loader、驗證規則回寫到 `skills/references`；屬於全局 workflow 缺口的，再回寫到全局 plan 或 `rebuild-workflow.md`。

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
- 若任務主要是沿既有 handbook / templates / tools 走 workflow，先從 `docs/area-development-handbook.md` 看總覽，再回來這個 skill 補 repo-specific 細節

## 舊站技能與玩家攻略基線

- `docs/3yWebsite/docs/data/skills.json` 目前基線是 `31` 筆：
 - 武器技能 `11`
 - 法術技能 `10`
 - 職業技能 `7`
 - 其他技能 `3`
- `skill/learnlv.html` 對應的「技能熟練度」頁算在 `skills.json` 內，但不是一般技能明細；不要把它當抽取失敗。
- `docs/3yWebsite/docs/data/players.json` 目前基線是 `26` 筆：
 - `bard` `2`
 - `bravo` `8`
 - `general` `7`
 - `mage` `2`
 - `newplayer` `7`
- `players.json` 目前只有 `1` 筆 `.htm` 舊檔：`newhand/players/newplayer/9907151.htm`；規劃或驗證時不要因為副檔名不同就漏看。
- `doctor`、`other`、`smith`、`thief` 目前在舊站只有分類首頁、沒有文章明細；`players.json` 沒有這幾類是正常現象，不代表這些職業不重要。
- 真正要從這兩份 JSON 抽的是「區域耦合訊號」，不是單純做資料展示：
 - `players.json` 用來找出玩家攻略反覆提到的 teacher、補給 NPC、轉職點、巴士/船站、練功斷點與關鍵服務 loop。
 - `skills.json` 用來找出技能鏈、技能名詞、資源消耗、可否教導、職業限制與適合轉成 room/NPC/enquire 的關鍵詞。
- 若打算搬動或刪除攻略裡高頻出現的服務 NPC，例如 `refresh`、`flee`、`mount`、步法/武器教學師父，先確認是否要保留原服務語意、提供替代 NPC，並同步在 plan / tracker 記錄理由。

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
- 若目前沒有 `in_progress` 或 `todo`，而任務是在盤點下一個 area 候選，先用 `players.json` 找「攻略裡最常被當作中繼/訓練/補給節點的城市與路段」，再用 `skills.json` 找出該節點承載的技能/職業服務鏈，避免只按世界地圖外觀選區而忽略玩法耦合
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
- 若任務有新增或修改 `mob/*.mob` / `obj/*.obj`，尤其是 mob `Class` 或特殊 `ItemType`，也要補讀這份檔；其中 `.obj` 可以先從 `docs/current-game/object-file-format.md` 快速定位欄位，再回頭核對 `document/obj.txt` 與 repo 內已成功載入的同類範例，不要只照單一文件猜常數或 `Value*` 欄位
- 若任務核心是 `.mob` 本身的格式搬修，依需求補讀：
  - `references/mob-file-layout.md`
  - `references/mob-core-fields.md`
  - `references/mob-teaching-and-programs.md`
  - `references/mob-flags-and-constants.md`
- 若任務有新增 `skill/*.ski`、替 NPC 換技能、或讓新的 mob `Enable` 指到新技能，先搜尋 repo 內是否已有同名 skill / 同 slot / 同 `skill.lst` key；新增 skill 只是 area data 的一部分，但驗證要求應比一般 `mob/obj` 更高
- NPC 專用且不打算讓玩家學習的技能，預設明確寫 `Valid NO`、`CanAsk NO`、`Teach NO`；但名稱、slot 與 loader 登錄仍要完整，不能因為是 NPC-only 就省略
- 若任務明確是在追「mob 技能偏弱 / 舊技能殘留 / 技能鏈重建」，再補讀 `references/skill-combat-chain-rebuild.md`；這類任務要先區分全域係數、legacy skill 合理保留、與真的需要 runtime 替換的錯位樣本
- 若任務延伸到 `skill/*.ski` 的 `#Damage` 重建，不要只看 `Value` 就決定高低階；至少先一起盤 `Chance`、`Parry`、`Innate`、`Wait`、`Cost`、`CostType`、`Weapon`、`Check`，並回看 `src/fight.c` / `src/skill.c` 的命中、閃避、資源與節奏影響，避免把輕兵、高頻或高暴擊技能一律改成重傷模板

### 4. 同步系統設定
- `merc.ini`、`variable.c`、`job.c`、`bus/ship/bounty` 與 docs 對照點，讀 `references/system-sync-checks.md`
- 若任務碰到交通、新手導流、技能來源、國家系統或官方敘事，這份檔是必要 reference
- 若這輪新增的是目前 repo 真正會載入的技能，而不只是一次性測試檔，優先同步 `docs/current-game/skills.md` / `docs/current-game/skills.json` 或其他 repo 自有紀錄；`docs/3yWebsite/` 預設只拿來參考世界觀、命名與舊技能脈絡，不直接當現行技能台帳
- 若這輪有改到既有 skill runtime 內容，尤其是 `#Damage`、`Cost`、`Wait`、`Teach`、`CanAsk`、`Valid`、`Enable` 這類會進 current-game registry 的欄位，不要只手改 `docs/current-game/skills.json`；先更新 `data/structured/skills/skills.json`、跑 `python -X utf8 scripts/export_structured_skills.py --check` / `--write`，再跑 `python -X utf8 scripts/build_current_game_skill_registry.py` 重建 registry，最後用 `python -X utf8 scripts/generate_current_game_skills_pages.py` 同步分類頁
- 若這輪有改到已建立 `content.json` 的 area runtime content，優先同步 `area/<area>/content.json` 與對應 exporter；若區域還沒有 `content.json`，才維持直接改 `mob / obj / res / shp` 的舊流程
- 若這輪新增或重排的是目前 repo 真正會載入的 area，優先同步 `docs/current-game/areas.md` / `docs/current-game/areas.json`；`docs/3yWebsite/` 的地圖與舊站頁面預設只當背景參考，不直接當現行 area registry
- 若這輪的 area 決策高度依賴舊站技能或玩家攻略，收尾時至少在 plan / tracker 補一句說明：是哪些攻略或技能鏈在支撐這個 world link、teacher 配置或服務節點設計

### 5. 需要世界觀/參考資料時串接 sango-docs-service
- 何時一起用 `sango-docs-service`、優先 docs / JSON 清單與回報要求，讀 `references/docs-service-integration.md`

## 規劃原則

- 詳細規劃原則、VNUM / 題材 / 互動 / 新手流程 / 國家與世界觀一致性，讀 `references/planning-principles.md`

## 驗證
1. 至少檢查 VNUM / 房號引用、`index/res/shp/roo` 對應與地圖出口一致性
2. 若用了 scaffold script，先跑 `--validate-only`
3. 若是 `spec / plan / tracker` 類工作，通常做到 `--validate-only` 即可，不必為了沒有 runtime 變更的任務硬跑雙平台 build
3.1 若想把 `--validate-only` 前置成更清楚的摘要，先跑 `python3 tools/mapmd_validate.py area/<area>/map.md`
4. 若是純 area data work，預設先做本機 build + smoke test；只有在碰到 `src/`、跨平台風險、或 merge 前信心 gate 時再補 Ubuntu / Docker
4.1 若需要替新 area 規劃下一段房號，先跑 `python3 tools/area_vnum_allocator.py --estimated-rooms <N> --headroom <M>`
5. 若牽涉交通、新手、技能、國家或世界觀，對照對應 docs / JSON
6. 若環境允許，做實際載入或 smoke test，並確認成功訊號與 `debug/` / `log/` 沒有新增 area 錯誤；必要時用 `python3 tools/log_parse_summary.py` 與 `python3 tools/area_acceptance_gate.py <area_slug>` 取摘要與 gate 建議
7. 完整驗證清單讀 `references/validation-checklist.md`

## 文件使用建議

- 需要快速導覽 legacy area 手冊時，先看 `docs/current-game/legacy-documentation.md`
- 需要釐清舊版安裝、目錄角色、`index/mob/obj/res/roo/shp` 是怎麼被介紹的，先看 `docs/current-game/legacy-readme.md`
- 需要 `.mob` 欄位與 NPC/teacher/program 骨架時，先看 `docs/current-game/mobile-file-format.md`
- 若要查 skill 內拆分後的 `.mob` 細節，按需求讀：
  - `references/mob-file-layout.md`
  - `references/mob-core-fields.md`
  - `references/mob-teaching-and-programs.md`
  - `references/mob-flags-and-constants.md`
- 需要 `.obj` 欄位與區塊摘要時，先看 `docs/current-game/object-file-format.md`
  注意：area object source 不要混進 runtime/save 風格欄位；目前 loader 吃的是 `Name / ShortDesc / Description / ItemType / Takeable / WearLoc / Value*`，不是 `Keywords / ExtraFlags / WearFlags`
- 需要 `.roo` 欄位、`#Exit/#Keyword/#Job` 與房間旗標摘要時，先看 `docs/current-game/room-file-format.md`
- 需要 `.res` 指令順序、`M/O/P/G/E/D/R/A` 作用時，先看 `docs/current-game/reset-file-format.md`
  注意：現行 `load_resets()` 以 EOF 結束，不要照 legacy 說明額外放 literal `S` terminator
- 需要 `.shp` 商店欄位與 `Keeper/Object/Sential` 關係時，先看 `docs/current-game/shop-file-format.md`
- 需要 area `index` / `Serial` / `Capital` / `Flags` 概念時，先看 `docs/current-game/title-file-format.md`
- 需要看 legacy 授權脈絡與配件限制時，先看 `docs/current-game/copyright-notice.md`
- 需要完整舊文細節、常數表或少見欄位，再回頭看對應的 `document/*.txt`
- 若 Pages 整理頁與 runtime / loader 行為不一致，以 `src/load.c`、`src/merc.h`、`data/symbol.def` 與已成功載入範例為準，並回補 docs

## 參考資料
- `document/README`
- `document/mob.txt`
- `document/obj.txt`
- `document/room.txt`
- `document/reset.txt`
- `document/shop.txt`
- `document/title.txt`
- `document/COPYRIGHT`
- `../../docs/current-game/legacy-documentation.md`
- `../../docs/current-game/legacy-readme.md`
- `../../docs/current-game/mobile-file-format.md`
- `../../docs/current-game/object-file-format.md`
- `../../docs/current-game/room-file-format.md`
- `../../docs/current-game/reset-file-format.md`
- `../../docs/current-game/shop-file-format.md`
- `../../docs/current-game/title-file-format.md`
- `../../docs/current-game/copyright-notice.md`
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
- `references/mob-file-layout.md`
- `references/mob-core-fields.md`
- `references/mob-teaching-and-programs.md`
- `references/mob-flags-and-constants.md`
- `references/skill-combat-chain-rebuild.md`
- `references/system-sync-checks.md`
- `references/docs-service-integration.md`
- `references/planning-principles.md`
- `references/validation-checklist.md`
- `references/rebuild-workflow.md`
- `references/map-spec-template.md`
- `../../docs/area-development-handbook.md`
- `../../docs/area-delivery-gates.md`
- `../../docs/area-vnum-policy.md`
- `../../docs/area-external-exit-policy.md`
- `../../docs/area-acceptance-checklist.md`
- `../../docs/codex-area-workflow.md`
- `../../templates/area-plan.template.md`
- `../../templates/map.md.template`
- `../../templates/area-readme.template.md`
- `../../templates/new-area-checklist.template.md`
- `../../schemas/mapmd-json.schema.json`
- `../../schemas/area-plan.schema.json`
- `../../tools/mapmd_validate.py`
- `../../tools/area_vnum_allocator.py`
- `../../tools/log_parse_summary.py`
- `../../tools/area_acceptance_gate.py`
- `../ref/Readme.md`
- `scripts/generate_roo_from_map_md.py`
- `docs/3yWebsite/.agents/skills/sango-docs-service/SKILL.md`
- 舊版對照：`https://github.com/jakeuj/merc-fju-2.0-utf8`
