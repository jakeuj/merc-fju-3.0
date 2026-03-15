# File Handling Rules

這份參考檔集中說明 area 資料檔、地圖檔與 `mapmd-json` / `.roo` 之間的處理規則。

## 資料檔處理

- `index`：保留既有欄位順序與字串格式；起始房、區域名稱、描述與 `Capital` 要互相對應
- 新增 AREA 時，`Capital` 預設設為 `0`；只有當這個 area 被明確設計成可作出生地、真正首都、或系統級回城 / 國家核心節點時，才應填非零 `Capital`
- 若把 `Capital` 設成非零，先確認它真的應該出現在出生地 / 首都 / home 選單，並且已具備對應服務鏈，不要讓單純的外郊或過渡區誤進出生地清單
- `mob/*.mob`：參照 `document/mob.txt`；確認 `Level`、`Alignment`、旗標、`Process` 是否符合該區用途
- `mob/*.mob` 的 `Class` 不要臆測新常數；先在 repo 內搜尋已成功載入的 mob 範例，沿用 parser 目前真的接受的值，再進 smoke test
- `obj/*.obj`：參照 `document/obj.txt`；若物品要由商店或 reset 產生，確認與 `res`、`shp` 對上
- `obj/*.obj` 若屬於特殊 `ItemType`，不要只照文件猜 `Value` / `Value0..3` 的落點；先在 repo 內搜尋已成功載入的同類物件範例，再決定欄位配置
- `ITEM_LIGHT` 類物件尤其要小心：至少比對是否需要 `WearLoc ITEM_WEAR_LIGHT` 與正確的燈光時間欄位；若只看到 `debug/badobject` 才回修，通常已經太晚
- `ITEM_FOOD` 與 `ITEM_DRINK_CON` 也要先比對 working examples：除了 `ItemType` 本身，還要補齊 parser 需要的 `Value*` 欄位，不要假設留空或沿用通用預設就能過
- `roo/*.roo`：參照 `document/room.txt`；出口要成對檢查，避免只改單向出口
- `roo/` 內若另有地圖檔，也把它視為正式資料的一部分；修房間時先用地圖核對座標關係，再決定哪些出口或描述不合理
- 地圖與出口檢查要包含立體方向：除了 `north/east/south/west`，還要主動檢查 `up/down/enter/out` 是否也和 `src/act_move.c` 的反向關係對得上
- 合法方向 enum 目前只用 `north`、`south`、`east`、`west`、`up`、`down`、`enter`、`out`；文件、template、script 必須維持同一份定義

## 互動 metadata 規則

- `roo/*.roo` 不只要看出口；若房間靠 `#Keyword` 描述暗示玩家輸入特殊動作，例如 `bore hole`、`enter xxx`、`climb xxx`、`push xxx`，就把它視為正式玩法路徑的一部分
- 但要分清楚兩種不同層級：`#Keyword` 只負責 `look/examine` 類描述，不會自動產生新指令；真正的特殊房間互動若不是內建在 `act_move.c` / 其他 `do_*` 指令裡，就必須靠 `#Job` 綁到 `src/job.c` 已註冊的房間 job function
- `#Enquire` 也要視為 room spec 的正式部分；它會被 `do_enquire` 用來做問路與服務查詢，所以只要房間承載訓練、商店、車站、碼頭、銀行、佈告欄等玩家可問路的功能，就應該進 spec
- `labels` 不是 `#Keyword` 的替代品；`labels` 是 graph/editor/export metadata，`keywords` 才是 Merc runtime interaction metadata

## 地圖與 spec-first

- `map`：若目標區有 `map`，先讀原檔再改，不要自行發明格式
- 若地圖檔是平面格狀表示，只把它當作主要平面骨架；任何 `up/down/enter/out` 這類立體或內外層連線，仍要回到 `.roo` 與 `src/act_move.c` 一起核對
- 若是新增 AREA，預設要先寫 `area/<new_area>/map.md`；它是 spec-first 設計檔，優先於任何舊式 area-local 地圖檔
- 若世界層參考已整理在 `area/world_map.md`，先用它決定新 AREA 要接到哪個母城、外郊或 world connector
- 若 `ref/Readme.md` 已提供更細的 area template 或相近節點 scaffold，優先借鏡它們來決定 cluster 命名、房間語氣、題材配置與 world links

## Scaffold generator

- 若想用腳本加速，使用 `references/map-spec-template.md` 提供的受限 Markdown 結構，再交給 `scripts/generate_roo_from_map_md.py` 產生 `.roo` scaffold
- 這個 Python script 的定位是 scaffold generator，不是完整 compiler：它會產生初版 `.roo`、驗證方向/引用/Job，但不會幫你猜缺漏描述、補世界觀或默默創造不存在的 reverse exit
- 若 exit 明確標了 `external: true`，它可以作為「接到既有 area 房號」的合法例外；這正是像 `loyang/556 <-> loyang_outskirts/7501` 這類整合場景需要的行為
- graph schema 可以額外攜帶 `coord`、`cluster`、`labels` 等 metadata，供未來 map/export tooling 使用；目前 `.roo` projection 不會輸出它們

## 長期重建回寫

- 若 area 屬於長期重建看板的一部分，完成一輪實作後要同步回寫 `area/rebuild_plan.md`
- 若本輪已做到可 commit 的安全里程碑，記得把 `delivery_gate` 推到 `spec_ready_for_commit` 或 `implementation_ready_for_commit`

## 進階 parser / 歷史相容

- 若地圖檔與實際 `.roo` 出口不一致，先整理成「地圖預期相鄰關係 -> 實際出口」的對照，再決定要修地圖、修出口，或兩者一起修
- 特別注意像 `area/newfight/roo/1211.roo` 這種房間：`#Keyword hole~` 的描述直接提示玩家用 `bore` 通過裂縫
- 以目前 repo 狀態來看，`bore` 還不是現成可用指令：若需求是讓 `bore hole` 真的可用，就要決定是新增通用 `do_bore`，還是新增 room job 再在對應 `.roo` 裡加 `#Job`
- 若遇到 parser 細節不確定，回看 `doc/area-file-format.txt`
- 若物件 parser 行為和文件不完全一致，優先以 repo 內已成功載入的同類物件為準，再用 `debug/badobject` 驗證這次修改是否乾淨
- 即使啟動 log 已出現成功訊號，只要這輪有改 `obj/*.obj`，仍要回頭檢查 `debug/badobject`；把它當成新 area 物件是否真的過關的正式 gate，不是可有可無的附帶檢查
- 若物件涉及卷軸、藥水、法杖、法器或其他 spell 型效果，補看 `doc/skills-and-spells-guide.txt`
- 進階 NPC 行為或 trigger 語法若不確定，可補看 `doc/mobprogram-guide.txt`
