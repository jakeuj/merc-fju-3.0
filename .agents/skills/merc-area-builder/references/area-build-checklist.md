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

## 2. 檔案填寫步驟
1. `index`：確認 `Name`、`Serial`、`Capital`、Description 與實際區域用途一致。
2. `mob/*.mob`：欄位順序遵循 `document/mob.txt`，並核對 `Level`、旗標、`Process`。
3. `obj/*.obj`：依 `document/obj.txt` 填寫，若會由 reset 或商店使用，確保後續 `res` / `shp` 對得上。
4. `roo/*.roo`：依 `document/room.txt` 填寫，每個出口都確認 `ExitVnum` 指向存在房間，且盡量成對。
5. `res/*.res`：依 `document/reset.txt` 重新核對所有 `M/E/G/O/D` 關聯。
6. `shp/*.shp`：依 `document/shop.txt` 設定 `Keeper`、販售類型與價格。
7. `map`：若該區已有 `map`，沿用原格式，不要自行發明新格式。

## 3. 舊 repo 比對檢查
- 只在需要補資料、查歷史設計或確認舊文案時回查 `merc-fju-2.0-utf8`。
- 把舊 repo 視為「對照來源」，不是直接照抄目標。
- 特別檢查：
- 舊 VNUM 是否要沿用、重映射，還是放棄
- 舊出口、舊出生點、舊交通/懸賞/提示文字是否仍符合 3.0 目標
- 舊 `mob/obj/roo/res/shp` 搬回來後是否會和現有 3.0 資料衝突
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

## 5. 編碼與靜態驗證
- 全部檔案維持 UTF-8；若有從舊 repo 匯入或懷疑編碼不穩，執行 `python scripts/convert_big5_to_utf8.py` 或等價方式確認。
- 用搜尋工具檢查：
- VNUM 是否重複
- 區名、舊城名、舊勢力詞是否殘留
- 重要房號是否仍被 `src/`、`data/`、`help/` 引用
- 用 `git diff` / `git status` 確認變更集中在預期檔案。

## 6. 啟動與遊戲內驗證
- 若環境允許，實際啟動遊戲或重載區域。
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
- `references/wow-area-example.md`
- `docs/3yWebsite/.agents/skills/sango-docs-service/SKILL.md`
- `https://github.com/jakeuj/merc-fju-2.0-utf8`
