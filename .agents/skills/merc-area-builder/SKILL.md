---
name: merc-area-builder
description: 維護、擴充或搬修 merc-fju-3.0 目前實際存在的區域資料時使用：依 document/README 與 area/ 現況處理 limbo、loyang、beiping、new、newfight、pk_area、free_fight 的 index/mob/obj/res/roo/shp 結構、更新 area/directory.lst、同步檢查 merc.ini 與固定房號/傳送/提示文字，並在需要世界觀、技能、國家或交通背景時搭配 docs/3yWebsite/.agents/skills/sango-docs-service/SKILL.md 取用 docs 與 JSON 資料。
---

# Merc Area Builder

此技能協助你在目前的 `merc-fju-3.0` 工作區內維護或擴充區域資料。優先依 repo 現況工作，不要沿用「scripts 與 area 已被精簡」那條舊假設。

## 快速開始
1. 先確認任務是要修改既有區域、搬修舊版內容，還是新增區域。
2. 先讀 `area/directory.lst` 與目標區域目錄，理解實際載入順序與檔案結構。
3. 以 `document/README`、`document/mob.txt`、`document/obj.txt`、`document/room.txt`、`document/reset.txt`、`document/shop.txt` 為主要格式依據；若要確認原始 Merc parser / vnum 習慣，再補看 `doc/area-file-format.txt`、`doc/vnum-assignments.txt`、`doc/merc-release-notes.txt`。
 目前專案使用的是拆目錄資料結構，不是原始單檔 `.are`；若回看 `doc/area-file-format.txt` 裡的 `#AREA/#HELPS/#MOBILES/#OBJECTS/#ROOMS/#RESETS/#SHOPS/#SPECIALS`，要把它當概念對照，不要逐段照抄成 3.0 目錄格式。
4. 需要世界觀、技能、國家系統、交通、公告脈絡時，連同 `docs/3yWebsite/.agents/skills/sango-docs-service/SKILL.md` 一起使用，從 `docs/3yWebsite/docs/*.md` 與 `docs/3yWebsite/docs/data/*.json` 取資料。
5. 修改完成後，至少做靜態搜尋、編碼檢查與必要的啟動/載入驗證，再回報受影響檔案與風險。

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
- 不要再把 `mineral/` 視為目前 repo 的既定必備目錄；只有任務真的需要礦脈/採集物時才新增，並同步確認載入格式
- `beiping` 額外有 `map`，修改時保留既有格式與用途

### scripts/ 現況
- `scripts/` 目前可見的腳本只有 `scripts/convert_big5_to_utf8.py`
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
- 先查 `area/directory.lst` 的順序與註解，避免把物件或房間引用到尚未載入的區域
- 若牽涉固定房號、出生地、交通、懸賞、教學流程，主動搜尋 `src/`、`etc/`、`data/`、`help/` 是否也要一起改

### 2. 先用現有區域當模板
- 優先比對 `area/loyang`、`area/beiping`、`area/new` 等現存區域，而不是依賴過往已被移除又後來復原前的假設
- 若是新增區域，先從最接近的既有區域複製結構與格式，再逐步替換名稱、VNUM、描述與 reset
- 若是搬修舊版資料，先用搜尋確認舊名稱、舊城名、舊勢力詞是否殘留在 `roo`、`mob`、`obj`、`res`、`shp`、help 或 system data
- 若現行 repo 缺資料或看不出原始設計，回查 `https://github.com/jakeuj/merc-fju-2.0-utf8` 的對應路徑，再把需要的內容 mapping 回 3.0

### 3. 處理資料檔
- `index`：保留既有欄位順序與字串格式；起始房、區域名稱、描述與 `Capital` 要互相對應
- `mob/*.mob`：參照 `document/mob.txt`；確認 `Level`、`Alignment`、旗標、`Process` 是否符合該區用途
- `obj/*.obj`：參照 `document/obj.txt`；若物品要由商店或 reset 產生，確認與 `res`、`shp` 對上
- `roo/*.roo`：參照 `document/room.txt`；出口要成對檢查，避免只改單向出口
- `roo/*.roo` 不只要看出口；若房間靠 `#Keyword` 描述暗示玩家輸入特殊動作，例如 `bore hole`、`enter xxx`、`climb xxx`、`push xxx`，就把它視為正式玩法路徑的一部分。搬房、改名或改文案時，要一起檢查關鍵字、動詞提示、相鄰房間與相關程式/觸發是否仍對得上
- 但要分清楚兩種不同層級：`#Keyword` 只負責 `look/examine` 類描述，不會自動產生新指令；真正的特殊房間互動若不是內建在 `act_move.c` / 其他 `do_*` 指令裡，就必須靠 `#Job` 綁到 `src/job.c` 已註冊的房間 job function
- `res/*.res`：參照 `document/reset.txt`；任何 `M/E/G/O/D` 關聯都要重新核對 VNUM
- `shp/*.shp`：參照 `document/shop.txt`；確認 `Keeper`、販售類型與商品來源一致
- `map`：若目標區有 `map`，先讀原檔再改，不要自行發明格式
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
- 台詞、地名、勢力名、技能名以目前專案與 docs 參考資料為準，避免混入其他版本設定
- 從 2.0 舊 repo 搬資料時，不要整包照抄；先比對目前 3.0 已存在的 area/data/help/src 耦合，再決定哪些欄位保留、哪些要改寫
- 若匯入的是更接近原始 Merc 的 reset 寫法，記得 `R` 也是合法 reset 類型，用於亂數出口；不要只認得 `M/E/G/O/D`
- 新手區或主城服務鏈改動時，優先維持 `newbie.md` 中玩家預期仍找得到的核心流程：出生後移動、補給、學習技能、致能、組隊、回城、轉職與國家導引；若必須改路徑，記得同步補新提示
- 房間若依賴 `#Keyword` 提示特殊動詞才能前進或觸發事件，優先維持「玩家看到描述就能推得出指令」這個原則；不要把關鍵字改名、把提示刪掉，或讓描述中的動詞與實際可用指令不一致
- 若要新增這類互動，先確認它屬於哪一種：
- 通用移動/操作：實作或修改 `src/act_move.c` / 其他 `do_*` 指令，並確認命令表已註冊
- 房間特例：在 `src/job.c` / job registry 增加 room job，並在對應 `.roo` 寫 `#Job`
- 不要以為只寫 `#Keyword hole~` 就會自動讓 `bore hole` 可用；`#Keyword` 是提示與檢視描述，不是命令綁定本身
- 技能相關區域改動時，優先維持 `skills.md` 中能被玩家辨識的技能名稱、來源關係與熟練度詞彙；不要在房間、NPC、秘笈、help 與 docs 間混用不同譯名或把「可教導」誤寫成「只能領悟」
- 國家相關區域改動時，優先維持 `realm.md` 中玩家預期的流程與限制：首都要有公告/信件承載點、建國/入國要找得到銀行與官署支援、叛國與離境不要把玩家送回錯誤領地或失去必要導引
- 世界觀或官方敘事相關改動時，優先維持 `system.md` 的時間線、勢力稱呼與官方語氣；不要把新技能開放順序、Immortal 身分、授權提示或 `help fju` / `credit` 類文案寫成與歷史資料衝突

## 驗證
1. 先用搜尋工具檢查 VNUM、區名、房號引用是否一致
2. 若有匯入舊資料或懷疑編碼不穩，執行 `python scripts/convert_big5_to_utf8.py` 或等價方式確認檔案可被 UTF-8 正常讀取
3. 檢查 `area/directory.lst`、目標區 `index`、相關 `res/shp/roo` 是否互相對得上
4. 若牽涉交通或主城導流，再對照 `docs/3yWebsite/docs/maps.md` / `docs/3yWebsite/docs/data/maps.json`，確認站名、票價、主節點用途、`Serial` / `Capital` 與玩家可見提示一致
5. 若牽涉新手區、主城服務點或教學導引，再對照 `docs/3yWebsite/docs/newbie.md`，確認玩家進場後仍能靠 room/NPC/告示走完基本流程，不會卡在缺 NPC、缺提示、缺指令說明
6. 若房間有 `#Keyword` 或描述暗示特殊互動，再逐房檢查玩家實際看到的名詞與動詞是否還能導向正確操作，例如 `hole -> bore hole` 這類提示不能只剩關鍵字、不剩可理解的引導
7. 若房間描述提示的是非內建指令，再確認它的實作位置真的存在：不是 `do_*` 命令，就是 `#Job -> src/job.c` 可解析的 function；不要讓 area 文案先行、程式端卻沒有入口
8. 若牽涉技能來源、訓練 NPC、秘笈物件或職業導引，再對照 `docs/3yWebsite/docs/skills.md` / `docs/3yWebsite/docs/data/skills.json`，確認技能名稱、來源類型、熟練度詞彙、study / 領悟提示與區域內實作一致
9. 若牽涉國家首都、領地入口、官署、公告板或建國/叛國流程，再對照 `docs/3yWebsite/docs/realm.md` / `docs/3yWebsite/docs/data/realm_commands.json`，確認 `Capital`、公告/信件載體、銀行條件、官職導引與 recall/離境邏輯一致
10. 若牽涉世界觀敘事、官方公告、元老/神族 NPC 或公開版提示，再對照 `docs/3yWebsite/docs/system.md`、`docs/3yWebsite/docs/data/news.json`、`docs/3yWebsite/docs/data/immortals.json`，確認歷史事件、官方稱呼、公告文案與 `help fju` / `credit` 相關提示一致
11. 若環境允許，實際啟動遊戲或執行區域 reload；`doc/merc-release-notes.txt` 也提醒 Merc 本身的開機流程就是很好的 area syntax checker，所以要優先讀第一個錯誤，而不是一次猜全部
12. 查看 `debug/`、`log/` 是否出現 `Load_room`、`load_mobiles`、reset 或檔案開啟錯誤
   原始 Merc 文件也提到 area diagnostics 常會附帶 area 檔名與行號；若有這種訊息，優先沿著第一個定位點回修
13. 回報時要列出：改了哪些區域檔、哪些系統檔被連動修改、是否引用了 docs 服務資料、以及還沒驗證到的風險

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
- `docs/3yWebsite/.agents/skills/sango-docs-service/SKILL.md`
- 舊版對照：`https://github.com/jakeuj/merc-fju-2.0-utf8`
