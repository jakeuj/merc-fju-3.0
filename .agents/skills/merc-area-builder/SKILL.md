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
6. 若任務屬於長期 area 重建，先讀 `plans/` 與 `area/rebuild_plan.md`；詳細規則見 `references/rebuild-workflow.md`。
7. 修改完成後，至少做靜態搜尋、編碼檢查與必要的啟動/載入驗證，再回報受影響檔案與風險。

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
- 若需要可直接套用的主題模板，讀 `references/theme-design-patterns.md`；它目前提供六大題材：`軍旅風`、`江湖風`、`仙俠風`、`歷史城市風`、`詭異民俗風`、`探險遺跡風`，並附房間語氣、NPC 類型、任務鉤子、物件 / 傳聞模板、`#Keyword` / `#Enquire` 詞庫、混搭規則、世界分區 heuristic 與 `map.md` 建議欄位
- 若任務不是只做單區，而是涉及世界層 area 規劃、題材平均化、州郡 / 主城 / 郊外 / 秘境的風格分工，優先讀 `references/theme-design-patterns.md` 的「世界級題材配置」與「世界分區建議」

## 先看目前專案現況

### area/ 現況
目前 repo 內已恢復的正式/既有區域是：
- `limbo`
- `loyang`
- `beiping`
- `new`
- `newfight`
- `pk_area`
- `free_fight`

另外，`player` 區域不需要寫入 `area/directory.lst`，系統會自動讀取。

### 每區常見結構
- 既有區域通常至少有 `index`、`mob/`、`obj/`、`res/`、`roo/`、`shp/`
- 戰鬥區與部分主城區還可能附帶區域地圖檔；它不一定放在區根目錄，也可能放在 `roo/` 內，視既有區格式而定
- 地圖不要只當成平面格子：`src/act_move.c` 目前支援 `north/east/south/west/up/down/enter/out`，規劃與修復出口時要把它當成立體拓樸
- `mapmd-json` 的內部模型是 graph-native：room = node、exit = edge，而 `#Keyword` / `#Job` / `#Enquire` 是掛在 node 上的互動與導流 metadata
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

### plans/ 現況
- `plans/` 是正式長期規劃入口，不是臨時草稿區
- 全局計畫使用 `plans/NNNN-topic-slug.md`
- 單一 area 計畫使用 `plans/area/NNNN-area-slug.md`
- `area/rebuild_plan.md` 是日常追蹤看板，負責 `todo / in_progress / done / blocked / next_action`
- 若使用固定 prompt `繼續實作下一個待建 area`，先讀 `area/rebuild_plan.md` 再決定下一個目標

### scripts/ 現況
- repo 根目錄 `scripts/` 目前可見的腳本只有 `scripts/convert_big5_to_utf8.py`
- 本 skill 另外提供 `scripts/generate_roo_from_map_md.py`，用來把受限結構的 `map.md` 轉成 `.roo` scaffold；它不是自由文字 Markdown compiler
- 這支 script 目前只做一件事：把 `mapmd-json` graph schema 驗證後投影成 `.roo` scaffold；它不是 Mudlet、SQLite 或其他外部 mapper exporter
- 不要假設 `scripts/check-data.py` 或其他舊工具一定存在；驗證步驟應先以 repo 實際檔案為準
- 若任務涉及大量舊資料匯入、回填或外部檔案導入，可用 `convert_big5_to_utf8.py` 協助確認 UTF-8 轉碼

### 舊版資料比對來源
- 若目前 repo 的 `area/`、`data/`、`help/` 或固定房號資料不完整，或你需要確認舊區原本長相，允許回查舊 repo `jakeuj/merc-fju-2.0-utf8`
- 優先把舊 repo 視為「歷史對照來源」，不是直接覆蓋真相；真正要採用哪份資料，仍以目前 3.0 任務目標與現行 repo 狀態決定
- 特別適合用在：
- 補回舊區的 `mob/obj/roo/res/shp`
- 對照舊 VNUM、舊出口、舊出生點、舊交通/懸賞/提示文字
- 確認某個房號、NPC、物件、技能掉落或 help 文案在舊版是否存在
- 若從舊 repo 搬資料回來，必須重新檢查 UTF-8、VNUM 衝突、目錄結構與現行設定是否一致

## 工作流程

### 1. 盤點目標與耦合
- 先確認是改哪個區：`limbo`、主城（`loyang`、`beiping`）、新手區（`new`、`newfight`）、戰鬥區（`pk_area`、`free_fight`），不同區域耦合不同
- 若任務是長期重建的一部分，先讀 `area/rebuild_plan.md`：
  - 有 `in_progress` 就先續做該區
  - 否則選第一個 `todo` 且無 blocker 的 area
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
- `map.md` 是人類可讀 spec；若要用腳本產生 `.roo`，只能使用其中受限、結構化的機器可讀區塊，不能把自由 prose 直接拿去 compile
- 若是搬修舊版資料，先用搜尋確認舊名稱、舊城名、舊勢力詞是否殘留在 `roo`、`mob`、`obj`、`res`、`shp`、help 或 system data
- 若現行 repo 缺資料或看不出原始設計，回查 `https://github.com/jakeuj/merc-fju-2.0-utf8` 的對應路徑，再把需要的內容 mapping 回 3.0

### 3. 處理資料檔
- `index`：保留既有欄位順序與字串格式；起始房、區域名稱、描述與 `Capital` 要互相對應
- `mob/*.mob`：參照 `document/mob.txt`；確認 `Level`、`Alignment`、旗標、`Process` 是否符合該區用途
- `obj/*.obj`：參照 `document/obj.txt`；若物品要由商店或 reset 產生，確認與 `res`、`shp` 對上
- `roo/*.roo`：參照 `document/room.txt`；出口要成對檢查，避免只改單向出口
- `roo/` 內若另有地圖檔，也把它視為正式資料的一部分；修房間時先用地圖核對座標關係，再決定哪些出口或描述不合理
- 地圖與出口檢查要包含立體方向：除了 `north/east/south/west`，還要主動檢查 `up/down/enter/out` 是否也和 `src/act_move.c` 的反向關係對得上
- 合法方向 enum 目前只用 `north`、`south`、`east`、`west`、`up`、`down`、`enter`、`out`；文件、template、script 必須維持同一份定義
- `roo/*.roo` 不只要看出口；若房間靠 `#Keyword` 描述暗示玩家輸入特殊動作，例如 `bore hole`、`enter xxx`、`climb xxx`、`push xxx`，就把它視為正式玩法路徑的一部分。搬房、改名或改文案時，要一起檢查關鍵字、動詞提示、相鄰房間與相關程式/觸發是否仍對得上
- 但要分清楚兩種不同層級：`#Keyword` 只負責 `look/examine` 類描述，不會自動產生新指令；真正的特殊房間互動若不是內建在 `act_move.c` / 其他 `do_*` 指令裡，就必須靠 `#Job` 綁到 `src/job.c` 已註冊的房間 job function
- `#Enquire` 也要視為 room spec 的正式部分；它會被 `do_enquire` 用來做問路與服務查詢，所以只要房間承載訓練、商店、車站、碼頭、銀行、佈告欄等玩家可問路的功能，就應該進 spec
- `labels` 不是 `#Keyword` 的替代品；`labels` 是 graph/editor/export metadata，`keywords` 才是 Merc runtime interaction metadata
- `res/*.res`：參照 `document/reset.txt`；任何 `M/E/G/O/D` 關聯都要重新核對 VNUM
- `shp/*.shp`：參照 `document/shop.txt`；確認 `Keeper`、販售類型與商品來源一致
- `map`：若目標區有 `map`，先讀原檔再改，不要自行發明格式
- 若地圖檔是平面格狀表示，只把它當作主要平面骨架；任何 `up/down/enter/out` 這類立體或內外層連線，仍要回到 `.roo` 與 `src/act_move.c` 一起核對，不要因為地圖檔沒畫出來就忽略
- 若是新增 AREA，預設要先寫 `area/<new_area>/map.md`；它是 spec-first 設計檔，優先於任何舊式 area-local 地圖檔
- 若世界層參考已整理在 `area/world_map.md`，先用它決定新 AREA 要接到哪個母城、外郊或 world connector
- 若想用腳本加速，使用 `references/map-spec-template.md` 提供的受限 Markdown 結構，再交給 `scripts/generate_roo_from_map_md.py` 產生 `.roo` scaffold
- 這個 Python script 的定位是 scaffold generator，不是完整 compiler：它會產生初版 `.roo`、驗證方向/引用/Job，但不會幫你猜缺漏描述、補世界觀或默默創造不存在的 reverse exit
- graph schema 可以額外攜帶 `coord`、`cluster`、`labels` 等 metadata，供未來 map/export tooling 使用；目前 `.roo` projection 不會輸出它們
- 若 area 屬於長期重建看板的一部分，完成一輪實作後要同步回寫 `area/rebuild_plan.md`：
  - 更新 status
  - 更新 next_action
  - 補上 done 或 blocked
- 若地圖檔與實際 `.roo` 出口不一致，先整理成「地圖預期相鄰關係 -> 實際出口」的對照，再決定要修地圖、修出口，或兩者一起修
- 特別注意像 `area/newfight/roo/1211.roo` 這種房間：`#Keyword hole~` 的描述直接提示玩家用 `bore` 通過裂縫。這類「描述 -> 指令」配對若斷掉，玩家即使看到房間也不一定知道怎麼前進
- 以目前 repo 狀態來看，`bore` 還不是現成可用指令：我沒有找到 `do_bore`，而 `src/job.c` 目前只註冊少數 room job（如 `job_recall_new`、`job_goto_pk_area`）。因此若需求是讓 `bore hole` 真的可用，就要決定是新增通用 `do_bore`，還是新增 room job 再在對應 `.roo` 裡加 `#Job`
- 若遇到 parser 細節不確定，回看 `doc/area-file-format.txt`：字串以 `~` 結尾、數值可用 `|` 組合、空白與多行字串的解析方式都以它為準
- 若在 `mob/obj` 上看到某些傳統 Merc 欄位和本專案行為不完全一致，記得原始 Merc 文件本來就提到部分數值會由系統依 level 或內部規則生成，不是每個欄位都照檔案原值生效
- 若物件涉及卷軸、藥水、法杖、法器或其他 spell 型效果，補看 `doc/skills-and-spells-guide.txt`；原始 Merc 文件提醒 area object 內使用的是 spell slot / area reference，不一定等於系統內部 skill index
- 進階 NPC 行為或 trigger 語法若不確定，可補看 `doc/mobprogram-guide.txt` 理解原始 MOBProgram 概念，再對照本專案現況的 `Process`/腳本風格

### 4. 同步系統設定
- 只要牽涉出生點、recall、新手流程、戰鬥傳送或固定服務點，就要一起檢查：
- `etc/merc.ini`
- `src/merc.ini`
- `src/variable.c`
- `src/job.c`
- `data/bounty.txt`
- `data/bus.txt`
- `data/ship.txt`
- `help/` 內玩家可見提示
- 若區域涉及驛站、渡口、碼頭、首都入口或新手導流，補看 `docs/3yWebsite/docs/maps.md`：把它當交通命名與動線對照表，確認 `Serial` / `Capital`、房間名稱、玩家提示、巴士站名與實際世界線一致
- `maps.md` 明確把地圖視為 `Serial/Capital` 之間的動線來源；若你新增或改寫交通節點，除了 area 檔本身，也要同步核對 `data/bus.txt`、`data/ship.txt`、相關 NPC / `res` 與 help 提示，不要只改單一端
- 若 docs 或 `maps.json` 提到票價、站名、推薦等級或主節點用途，區域內的房間描述、告示、交通 NPC 與 `area` 指令導引也要保持同一套說法
- 若區域涉及新手教學、出生後第一輪探索或練功導流，補看 `docs/3yWebsite/docs/newbie.md`：把它當教學節奏與玩家期望對照表，確認新手區與主城服務點仍支援 `area`、`learn`、`enable`、`group`、`recall`、`score` 等被攻略反覆提到的流程
- `newbie.md` 也反映歷史攻略中依賴的服務 NPC 與互動，例如學習、修裝、補給、救濟金、轉職、官職/國家導引；若你搬動房間、NPC 或傳送點，要一起檢查教學文本、看板與 NPC 對話是否仍說得通
- `newbie.md` 與歷史攻略若提到像 `bore hole`、特定房間關鍵字、地圖捷徑或任務互動詞，也要把它們當成新手導流的一部分，不可只留房間物件或關鍵字卻刪掉玩家能理解的提示
- 若區域涉及技能教師、秘笈掉落、訓練場、職業試煉、法器或技能型獎勵，補看 `docs/3yWebsite/docs/skills.md`：把它當技能命名、來源類型與資源成本對照表，確認 NPC、物件、掉落與文案使用同一套技能名稱與分類
- `skills.md` 也提供「可教導 / 僅領悟 / 秘笈 study / 任務獎勵」這類來源線索；若你移動技能來源，除了 `mob/obj/res/shp`，也要同步檢查 help、任務提示、掉落敘述與相關主城服務 NPC 是否仍合理
- 若區域涉及國家首都、國界、官署、建國/入國導引、國家公告板或國家專屬服務，補看 `docs/3yWebsite/docs/realm.md`：把它當 `realm` 指令、官職權限與 Capital 支援需求對照表，確認房間、NPC、銀行、看板與傳送設定符合國家系統預期
- `realm.md` 也反映 `realm !join`、`!leave`、`!quit`、`!news`、`!read`、`!help`、`!attribution` 這些流程依賴的場景；若你搬動首都、領地入口、國家辦事處或懸賞/罪惡島相關區域，要一起檢查國家導引文字、公告板、銀行需求與 recall 落點是否仍合理
- 若區域涉及世界觀敘事、官方公告脈絡、元老/神族 NPC、授權文字或系統級 help/credit 提示，補看 `docs/3yWebsite/docs/system.md`：把它當故事時間線、官方用語與配件規範對照表，確認 area 描述、公告板、NPC 稱謂與玩家可見提示不會偏離 Merc-FJU 世界線
- `system.md` 也整理公告時間線、Immortal 名冊與版權要求；若你新增官方風格 NPC、歷史事件、傳送試煉、系統公告或公開版說明，要一起檢查 `help fju`、`credit`、相關 help 文案與遊戲內用語是否仍符合規範

### 5. 需要世界觀/參考資料時串接 sango-docs-service
- 遇到下列情境時，連同 `docs/3yWebsite/.agents/skills/sango-docs-service/SKILL.md` 一起用：
- 要替區域補世界觀、歷史事件、國家勢力或角色背景
- 要確認技能描述、掉落來源、NPC 對應或玩家指南
- 要比對地圖交通、巴士站、下載資料或公告時間線
- 要確認新手教學節奏、常用指令導引、規則告示或玩家常見卡點
- 要確認技能命名、熟練度詞彙、資源消耗、秘笈 / study 流程或職業技能來源
- 要確認國家指令流程、官職/權限、首都房間功能、入國/叛國導流或國家公告板
- 要確認故事時間線、系統公告、Immortal/官方 NPC 映射、版權提示或公開版用語

優先資料來源：
- 主題總覽：`docs/3yWebsite/docs/index.md`
- 世界與公告：`docs/3yWebsite/docs/system.md`
- 新手/規則/玩家心得：`docs/3yWebsite/docs/newbie.md`
- 技能：`docs/3yWebsite/docs/skills.md` 與 `docs/3yWebsite/docs/data/skills.json`
- 國家系統：`docs/3yWebsite/docs/realm.md` 與 `docs/3yWebsite/docs/data/realm_commands.json`
- 地圖交通：`docs/3yWebsite/docs/maps.md` 與 `docs/3yWebsite/docs/data/maps.json`
- 下載與手冊：`docs/3yWebsite/docs/download.md` 與 `docs/3yWebsite/docs/data/downloads.json`

回答或規劃時，清楚標示資料來自哪個 docs 檔或 JSON，並說明它會影響區域建置流程的哪一步。
其中 `maps.md` / `maps.json` 不只是背景閱讀：它們可直接用來核對主城與區域節點命名、巴士/船運站點、價格、推薦等級提示與地圖導流，特別適合檢查新手區、主城外圍、驛站與跨區傳送。
其中 `newbie.md` 不只是玩家手冊：它可直接用來核對新手區的教學順序、服務 NPC、常用指令提示、規則告示與升級導流，特別適合檢查 `new`、`newfight`、洛陽周邊與任何出生後第一批會接觸到的房間。
其中 `skills.md` / `skills.json` 不只是技能索引：它們可直接用來核對技能中文/英文名稱、來源類型、熟練度詞彙、資源消耗與 study 相關物件，特別適合檢查訓練 NPC、秘笈掉落、職業試煉與技能獎勵區域。
其中 `realm.md` / `realm_commands.json` 不只是國家介紹：它們可直接用來核對 Capital 房間、國家公告板、銀行門檻、官職權限、入國/離境/叛國流程與國家專屬服務，特別適合檢查主城、國界、官署與國家領地。
其中 `system.md` / `news.json` / `immortals.json` 不只是背景資料：它們可直接用來核對故事時間線、公告順序、Immortal 稱謂、官方 NPC 風格、`help fju` / `credit` 提示與公開版相關文案，特別適合檢查主線敘事、官方公告板與系統服務區。

## 規劃原則
- 先以現有 VNUM 生態為準，不要直接照搬其他 repo 或舊草案中的千位段假設
- 若需要原始 Merc 的 vnum 習慣與限制背景，可參考 `doc/vnum-assignments.txt` 與 `doc/area-file-format.txt`；至少維持「同類型資料不可撞號」這條底線
- 新增 VNUM 前，先全文搜尋 `area/`、`src/`、`data/` 是否已被使用
- 若只是在既有區內擴房、擴 NPC、擴物件，優先維持該區原本的編號習慣
- 若需要大量搬移舊區，先做 mapping 表，列出舊 VNUM -> 新 VNUM，再開始改檔
- 規劃新區或修戰鬥迷宮時，先畫或更新區域地圖檔，再批次檢查每個房間的上下左右出口是否和格位一致；休息室、入口廳、傳送點這類不在主格網內的房間，要用額外節點思考，不要硬塞成主地圖中心
- 若專案使用固定 prompt `繼續實作下一個待建 area`，就把 `area/rebuild_plan.md` 視為下一步選擇器，而不是重新猜測優先順序
- 若區域有樓層、洞口、室內外切換、城門內外、建築入口或其他垂直/內外層結構，先把平面骨架與立體節點分開思考；`up/down/enter/out` 的配對以 `src/act_move.c` 的 `rev_dir[]` 為準，不要自行猜反向方向
- 若區域很大（例如上百個 room），把 `map.md` 當主索引，並拆成 `map-core.md`、`map-floor-2.md`、`map-services.md`、`map-special-routes.md` 之類的子檔；Python scaffold 只接受主檔明確列出的 `includes`
- graph 上預設追求 edge 完整性，所以 reverse exit 會預設要求成對；若 runtime intent 就是單向通道，才用 `one_way` 明確標示這是刻意偏離對稱圖的合法例外
- 台詞、地名、勢力名、技能名以目前專案與 docs 參考資料為準，避免混入其他版本設定
- 可借鏡三國史傳、演義、武俠群像、奇幻三國等題材來增加帶入感，但要先抽取題材母型再落成 repo 內可維護的原生設計，不要讓 area 變成跨 IP 名稱大拼盤
- 若同時在規劃多個 area，主動檢查六大題材分布是否失衡；優先補足缺少的題材類型，而不是讓每個新區都落到同一種風格
- 規劃單一 area 時，也要說清楚它在世界層的 `Theme` / `Subtheme` 與缺口角色，例如「補主城外郊的軍旅風」、「補洛陽周邊的歷史城市風與江湖風過渡帶」
- 從 2.0 舊 repo 搬資料時，不要整包照抄；先比對目前 3.0 已存在的 area/data/help/src 耦合，再決定哪些欄位保留、哪些要改寫
- 若匯入的是更接近原始 Merc 的 reset 寫法，記得 `R` 也是合法 reset 類型，用於亂數出口；不要只認得 `M/E/G/O/D`
- 新手區或主城服務鏈改動時，優先維持 `newbie.md` 中玩家預期仍找得到的核心流程：出生後移動、補給、學習技能、致能、組隊、回城、轉職與國家導引；若必須改路徑，記得同步補新提示
- 房間若依賴 `#Keyword` 提示特殊動詞才能前進或觸發事件，優先維持「玩家看到描述就能推得出指令」這個原則；不要把關鍵字改名、把提示刪掉，或讓描述中的動詞與實際可用指令不一致
- `#Enquire` 不是裝飾資料；它是玩家查服務與找地點的入口。若你在 spec 中把某房間設計成「可問路找到」，就要同步規劃 `.roo` 內的 `#Enquire` 同義詞
- 若要新增這類互動，先確認它屬於哪一種：
- 通用移動/操作：實作或修改 `src/act_move.c` / 其他 `do_*` 指令，並確認命令表已註冊
- 房間特例：在 `src/job.c` / job registry 增加 room job，並在對應 `.roo` 寫 `#Job`
- 不要以為只寫 `#Keyword hole~` 就會自動讓 `bore hole` 可用；`#Keyword` 是提示與檢視描述，不是命令綁定本身
- 同理，不要以為只把某服務寫進房間描述就能被 `enquire` 找到；若玩家要能問路找到它，就要規劃並落地 `#Enquire`
- 技能相關區域改動時，優先維持 `skills.md` 中能被玩家辨識的技能名稱、來源關係與熟練度詞彙；不要在房間、NPC、秘笈、help 與 docs 間混用不同譯名或把「可教導」誤寫成「只能領悟」
- 國家相關區域改動時，優先維持 `realm.md` 中玩家預期的流程與限制：首都要有公告/信件承載點、建國/入國要找得到銀行與官署支援、叛國與離境不要把玩家送回錯誤領地或失去必要導引
- 世界觀或官方敘事相關改動時，優先維持 `system.md` 的時間線、勢力稱呼與官方語氣；不要把新技能開放順序、Immortal 身分、授權提示或 `help fju` / `credit` 類文案寫成與歷史資料衝突

## 驗證
1. 先用搜尋工具檢查 VNUM、區名、房號引用是否一致
2. 若有匯入舊資料或懷疑編碼不穩，執行 `python scripts/convert_big5_to_utf8.py` 或等價方式確認檔案可被 UTF-8 正常讀取
3. 檢查 `area/directory.lst`、目標區 `index`、相關 `res/shp/roo` 是否互相對得上
4. 若目標區有地圖檔，逐格核對地圖上的相鄰房號與 `.roo` 出口是否一致，並確認房間描述是否符合所在方位或區塊用途；若有 `up/down/enter/out`，再回到 `src/act_move.c` 檢查立體反向關係
5. 若使用 `scripts/generate_roo_from_map_md.py`，先跑 `--validate-only`，確認房號、方向、reverse exit、Job function 與受限 Markdown 結構都合法，再決定是否輸出 `.roo`
6. 若牽涉交通或主城導流，再對照 `docs/3yWebsite/docs/maps.md` / `docs/3yWebsite/docs/data/maps.json`，確認站名、票價、主節點用途、`Serial` / `Capital` 與玩家可見提示一致
7. 若牽涉新手區、主城服務點或教學導引，再對照 `docs/3yWebsite/docs/newbie.md`，確認玩家進場後仍能靠 room/NPC/告示走完基本流程，不會卡在缺 NPC、缺提示、缺指令說明
8. 若房間有 `#Keyword` 或描述暗示特殊互動，再逐房檢查玩家實際看到的名詞與動詞是否還能導向正確操作，例如 `hole -> bore hole` 這類提示不能只剩關鍵字、不剩可理解的引導
9. 若房間設計成可被問路找到，再逐房檢查 `#Enquire` 同義詞是否已落地，不要讓 spec 有服務節點、遊戲中卻問不到
10. 若房間描述提示的是非內建指令，再確認它的實作位置真的存在：不是 `do_*` 命令，就是 `#Job -> src/job.c` 可解析的 function；不要讓 area 文案先行、程式端卻沒有入口
11. 若牽涉技能來源、訓練 NPC、秘笈物件或職業導引，再對照 `docs/3yWebsite/docs/skills.md` / `docs/3yWebsite/docs/data/skills.json`，確認技能名稱、來源類型、熟練度詞彙、study / 領悟提示與區域內實作一致
12. 若牽涉國家首都、領地入口、官署、公告板或建國/叛國流程，再對照 `docs/3yWebsite/docs/realm.md` / `docs/3yWebsite/docs/data/realm_commands.json`，確認 `Capital`、公告/信件載體、銀行條件、官職導引與 recall/離境邏輯一致
13. 若牽涉世界觀敘事、官方公告、元老/神族 NPC 或公開版提示，再對照 `docs/3yWebsite/docs/system.md`、`docs/3yWebsite/docs/data/news.json`、`docs/3yWebsite/docs/data/immortals.json`，確認歷史事件、官方稱呼、公告文案與 `help fju` / `credit` 相關提示一致
14. 若環境允許，實際啟動遊戲或執行區域 reload；`doc/merc-release-notes.txt` 也提醒 Merc 本身的開機流程就是很好的 area syntax checker，所以要優先讀第一個錯誤，而不是一次猜全部
15. 查看 `debug/`、`log/` 是否出現 `Load_room`、`load_mobiles`、reset 或檔案開啟錯誤
   原始 Merc 文件也提到 area diagnostics 常會附帶 area 檔名與行號；若有這種訊息，優先沿著第一個定位點回修
16. 回報時要列出：改了哪些區域檔、哪些系統檔被連動修改、是否引用了 docs 服務資料、是否動到區域地圖檔、是否使用 Python scaffold 產生 `.roo`、以及還沒驗證到的風險
17. 若任務來自長期重建計畫，也要回報：是否更新 `area/rebuild_plan.md`、下一個推薦 area 是哪個、以及固定 prompt 下次會落到哪份計畫

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
- `references/rebuild-workflow.md`
- `references/map-spec-template.md`
- `scripts/generate_roo_from_map_md.py`
- `docs/3yWebsite/.agents/skills/sango-docs-service/SKILL.md`
- 舊版對照：`https://github.com/jakeuj/merc-fju-2.0-utf8`
