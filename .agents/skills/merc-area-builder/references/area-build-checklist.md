# Merc 區域建立檢查清單

## 0. 前置規劃
- 確認這次是修改既有區域、搬修舊版資料，還是新增區域。
- 先讀 `area/directory.lst`，確認目前實際載入的區域與順序。
- 決定目標 `area/<slug>`，並先檢查 `area/` 是否已有同名目錄。
- 規劃 VNUM 前，先搜尋 `area/`、`src/`、`data/` 是否已使用相同房號/物件/NPC 編號。
- 若目前 repo 缺少舊區內容、固定房號來源或歷史文案，回查舊 repo `https://github.com/jakeuj/merc-fju-2.0-utf8` 當歷史對照來源。

## 1. 建立目錄與登錄
| 項目 | 動作 |
| --- | --- |
| `area/<slug>/` | 依需求建立或整理 `index`, `mob/`, `obj/`, `roo/`, `res/`, `shp/`；只有真的需要時才新增 `mineral/`。 |
| `area/directory.lst` | 新增正式區時加入 `<slug>`，並保持載入順序正確；既有區搬修時確認名稱與目錄一致。 |
| 現有模板 | 優先參考 `area/loyang`、`area/beiping`、`area/new`、`area/newfight`、`area/pk_area`、`area/free_fight` 的實際格式。 |

備註：
若回看 `doc/area-file-format.txt`，記得那是原始 Merc 的單檔 `.are` 結構；在本專案裡要把它當成概念映射，不是逐段照抄。

## 2. 檔案填寫步驟
1. `index`：確認 `Name`、`Serial`、`Capital`、Description 與實際區域用途一致。
2. `mob/*.mob`：欄位順序遵循 `document/mob.txt`，並核對 `Level`、旗標、`Process`。
3. `obj/*.obj`：依 `document/obj.txt` 填寫，若會由 reset 或商店使用，確保後續 `res` / `shp` 對得上。
4. `roo/*.roo`：依 `document/room.txt` 填寫，每個出口都確認 `ExitVnum` 指向存在房間，且盡量成對。
5. `res/*.res`：依 `document/reset.txt` 重新核對所有 `M/E/G/O/D` 關聯。
6. `shp/*.shp`：依 `document/shop.txt` 設定 `Keeper`、販售類型與價格。
7. `map`：若該區已有 `map`，沿用原格式，不要自行發明新格式。
8. 若 parser 細節不確定，回看 `doc/area-file-format.txt`：字串 `~` 結尾、數值 `|` 組合、空白與多行字串解析都以它為準。
9. 若要理解複雜 NPC trigger / 腳本概念，可補看 `doc/mobprogram-guide.txt` 再對照本專案現況。
10. 若物件帶 spell 效果，補看 `doc/skills-and-spells-guide.txt`；area object 引用的 spell slot / area value 不一定等於系統內部 skill index。

## 3. 舊 repo 比對檢查
- 只在需要補資料、查歷史設計或確認舊文案時回查 `merc-fju-2.0-utf8`。
- 把舊 repo 視為「對照來源」，不是直接照抄目標。
- 特別檢查：
- 舊 VNUM 是否要沿用、重映射，還是放棄
- 舊出口、舊出生點、舊交通/懸賞/提示文字是否仍符合 3.0 目標
- 舊 `mob/obj/roo/res/shp` 搬回來後是否會和現有 3.0 資料衝突
- 舊 reset 若含 `R` 類型亂數出口，不要誤判成異常；先對照 `doc/area-file-format.txt` 與 `doc/security-features.txt`
- 從舊 repo 複製回來的文字檔，重新確認 UTF-8、路徑、區名、勢力名與現行世界設定

## 4. 系統連動檢查
- 只要牽涉出生點、recall、新手流程、戰鬥區或固定服務點，就檢查：
- `src/merc.ini`
- `src/variable.c`
- `src/job.c`
- `data/bounty.txt`
- `data/bus.txt`
- `data/ship.txt`
- `help/` 內玩家可見提示
- 若任務也需要世界觀、技能、國家或交通背景，連同 `docs/3yWebsite/.agents/skills/sango-docs-service/SKILL.md` 一起使用。
- 若有驛站、渡口、碼頭、主城入口或跨區導流，對照 `docs/3yWebsite/docs/maps.md` / `docs/3yWebsite/docs/data/maps.json`，確認站名、票價、主節點用途、`Serial` / `Capital` 與 room/help/NPC 提示一致。
- 若 docs 提到推薦等級或地圖節點用途，區域內的房間描述、告示與 `area` 指令導引也要用同一套命名與分級邏輯。
- 若有出生後導流、新手教學房、訓練場、轉職或國家導引，對照 `docs/3yWebsite/docs/newbie.md`，確認 `area`、`learn`、`enable`、`group`、`recall`、`score` 等關鍵流程仍有 room/NPC/看板支撐。
- 若搬動新手服務 NPC、補給點、修裝、救濟金、轉職或官署位置，要同步修正新手提示與玩家第一輪探索路線，避免攻略文字與現況斷線。
- 若有技能教師、秘笈掉落、訓練場、法器或職業任務，對照 `docs/3yWebsite/docs/skills.md` / `docs/3yWebsite/docs/data/skills.json`，確認技能名稱、來源類型、熟練度詞彙、資源消耗與區域內 NPC/物件/掉落一致。
- 若技能需 `study`、領悟、預備功夫或特殊資源消耗，房間提示、NPC 對話、物件說明與 help 文字要反映同一套規則，不要只在其中一處更新。
- 若有國家首都、領地入口、官署、公告板、建國/入國/離境流程，對照 `docs/3yWebsite/docs/realm.md` / `docs/3yWebsite/docs/data/realm_commands.json`，確認 `Capital`、銀行、官職導引、新聞/信件載體與國家專屬服務都有落點。
- 若牽涉叛國、懸賞、罪惡島或國土 recall，確認 `realm !quit` / `!leave` 類流程的懲罰與離境邏輯不會和房間傳送、出生點、國界提示互相衝突。
- 若有世界觀主線、官方公告板、元老/神族 NPC、試煉傳送或公開版提示，對照 `docs/3yWebsite/docs/system.md` / `docs/3yWebsite/docs/data/news.json` / `docs/3yWebsite/docs/data/immortals.json`，確認敘事、公告順序、官方稱謂與玩家可見文案一致。
- 若區域或 help 涉及 `help fju`、`credit`、授權說明或官方製作群彩蛋，確認文字沒有違反 `system.md` / `announce` 轉錄出的版權要求，也不要誤刪應保留的提示。

## 5. 編碼與靜態驗證
- 全部檔案維持 UTF-8；若有從舊 repo 匯入或懷疑編碼不穩，執行 `python scripts/convert_big5_to_utf8.py` 或等價方式確認。
- 用搜尋工具檢查：
- VNUM 是否重複
- 區名、舊城名、舊勢力詞是否殘留
- 重要房號是否仍被 `src/`、`data/`、`help/` 引用
- 若編號規劃拿不準，可補看 `doc/vnum-assignments.txt` 與 `doc/area-file-format.txt` 的原始 Merc 背景，但實際採用仍以目前 3.0 世界資料為準。
- 若區域有交通節點，再核對 `docs/3yWebsite/docs/maps.md` 是否仍和 `data/bus.txt` / `data/ship.txt`、區域內提示文字、驛站 NPC 配置對得上。
- 若區域有新手導引或服務鏈，再核對 `docs/3yWebsite/docs/newbie.md` 提到的指令、NPC 類型、推薦練功流與告示文字是否仍找得到落點。
- 若區域有技能來源或秘笈物件，再核對 `docs/3yWebsite/docs/skills.md` 是否仍和 `mob/obj/res/shp`、掉落提示、訓練 NPC 與相關 help 文案對得上。
- 若區域有國家流程或 Capital 功能，再核對 `docs/3yWebsite/docs/realm.md` 是否仍和 `Capital`、board/note 類物件、銀行/官署服務點、國家提示與 recall 設定對得上。
- 若區域有官方敘事、公告或 Immortal/元老 NPC，再核對 `docs/3yWebsite/docs/system.md` 是否仍和新聞時間線、NPC 稱謂、help/credit 文案與公告板內容對得上。
- 用 `git diff` / `git status` 確認變更集中在預期檔案。

## 6. 啟動與遊戲內驗證
- 若環境允許，實際啟動遊戲或重載區域。
- 把 Merc 開機流程當成 syntax checker：優先讀第一個 area/load 錯誤，不要一次猜整串連鎖問題。
- 若錯誤訊息附 area 檔名或行號，先沿著第一個定位點修，不要跳著改。
- 檢查 `log/`、`debug/` 是否出現：
- `Load_room`
- `load_mobiles`
- reset / parse error
- 檔案開啟失敗
- 若 log 已出現資料載入錯誤，優先修 area/data 問題，不要誤判成純啟動器問題。

## 7. 延伸參考
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
- `references/historical-large-city-example.md`
- `docs/3yWebsite/.agents/skills/sango-docs-service/SKILL.md`
- `https://github.com/jakeuj/merc-fju-2.0-utf8`
