---
name: merc-area-builder
description: 維護、擴充或搬修 merc-fju-3.0 目前實際存在的區域資料時使用：依 document/README 與 area/ 現況處理 limbo、loyang、beiping、new、newfight、pk_area、free_fight 的 index/mob/obj/res/roo/shp 結構、更新 area/directory.lst、同步檢查 merc.ini 與固定房號/傳送/提示文字，並在需要世界觀、技能、國家或交通背景時搭配 docs/3yWebsite/.agents/skills/sango-docs-service/SKILL.md 取用 docs 與 JSON 資料。
---

# Merc Area Builder

此技能協助你在目前的 `merc-fju-3.0` 工作區內維護或擴充區域資料。優先依 repo 現況工作，不要沿用「scripts 與 area 已被精簡」那條舊假設。

## 快速開始
1. 先確認任務是要修改既有區域、搬修舊版內容，還是新增區域。
2. 先讀 `area/directory.lst` 與目標區域目錄，理解實際載入順序與檔案結構。
3. 以 `document/README`、`document/mob.txt`、`document/obj.txt`、`document/room.txt`、`document/reset.txt`、`document/shop.txt` 為格式依據，不要憑其他 Merc 變體記憶硬寫。
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
- `res/*.res`：參照 `document/reset.txt`；任何 `M/E/G/O/D` 關聯都要重新核對 VNUM
- `shp/*.shp`：參照 `document/shop.txt`；確認 `Keeper`、販售類型與商品來源一致
- `map`：若目標區有 `map`，先讀原檔再改，不要自行發明格式

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

### 5. 需要世界觀/參考資料時串接 sango-docs-service
- 遇到下列情境時，連同 `docs/3yWebsite/.agents/skills/sango-docs-service/SKILL.md` 一起用：
- 要替區域補世界觀、歷史事件、國家勢力或角色背景
- 要確認技能描述、掉落來源、NPC 對應或玩家指南
- 要比對地圖交通、巴士站、下載資料或公告時間線

優先資料來源：
- 主題總覽：`docs/3yWebsite/docs/index.md`
- 世界與公告：`docs/3yWebsite/docs/system.md`
- 新手/規則/玩家心得：`docs/3yWebsite/docs/newbie.md`
- 技能：`docs/3yWebsite/docs/skills.md` 與 `docs/3yWebsite/docs/data/skills.json`
- 國家系統：`docs/3yWebsite/docs/realm.md` 與 `docs/3yWebsite/docs/data/realm_commands.json`
- 地圖交通：`docs/3yWebsite/docs/maps.md` 與 `docs/3yWebsite/docs/data/maps.json`
- 下載與手冊：`docs/3yWebsite/docs/download.md` 與 `docs/3yWebsite/docs/data/downloads.json`

回答或規劃時，清楚標示資料來自哪個 docs 檔或 JSON，並說明它會影響區域建置流程的哪一步。

## 規劃原則
- 先以現有 VNUM 生態為準，不要直接照搬其他 repo 或舊草案中的千位段假設
- 新增 VNUM 前，先全文搜尋 `area/`、`src/`、`data/` 是否已被使用
- 若只是在既有區內擴房、擴 NPC、擴物件，優先維持該區原本的編號習慣
- 若需要大量搬移舊區，先做 mapping 表，列出舊 VNUM -> 新 VNUM，再開始改檔
- 台詞、地名、勢力名、技能名以目前專案與 docs 參考資料為準，避免混入其他版本設定
- 從 2.0 舊 repo 搬資料時，不要整包照抄；先比對目前 3.0 已存在的 area/data/help/src 耦合，再決定哪些欄位保留、哪些要改寫

## 驗證
1. 先用搜尋工具檢查 VNUM、區名、房號引用是否一致
2. 若有匯入舊資料或懷疑編碼不穩，執行 `python scripts/convert_big5_to_utf8.py` 或等價方式確認檔案可被 UTF-8 正常讀取
3. 檢查 `area/directory.lst`、目標區 `index`、相關 `res/shp/roo` 是否互相對得上
4. 若環境允許，實際啟動遊戲或執行區域 reload，並查看 `debug/`、`log/` 是否出現 `Load_room`、`load_mobiles`、reset 或檔案開啟錯誤
5. 回報時要列出：改了哪些區域檔、哪些系統檔被連動修改、是否引用了 docs 服務資料、以及還沒驗證到的風險

## 參考資料
- `document/README`
- `document/mob.txt`
- `document/obj.txt`
- `document/room.txt`
- `document/reset.txt`
- `document/shop.txt`
- `references/area-build-checklist.md`
- `references/wow-area-example.md`
- `docs/3yWebsite/.agents/skills/sango-docs-service/SKILL.md`
- 舊版對照：`https://github.com/jakeuj/merc-fju-2.0-utf8`
