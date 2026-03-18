# Validation Checklist

這份參考檔集中保存 area 任務的長版驗證清單。

1. 先用搜尋工具檢查 VNUM、區名、房號引用是否一致
2. 若有匯入舊資料或懷疑編碼不穩，執行 `python scripts/convert_big5_to_utf8.py` 或等價方式確認檔案可被 UTF-8 正常讀取
3. 檢查 `area/directory.lst`、目標區 `index`、相關 `res/shp/roo` 是否互相對得上
4. 若目標區有地圖檔，逐格核對地圖上的相鄰房號與 `.roo` 出口是否一致，並確認房間描述是否符合所在方位或區塊用途；若有 `up/down/enter/out`，再回到 `src/act_move.c` 檢查立體反向關係
5. 若這輪是 spec / plan / tracker work，先跑 `python3 tools/mapmd_validate.py area/<area>/map.md`
6. 若使用 `scripts/generate_roo_from_map_md.py`，再跑 `--validate-only`
7. 若牽涉交通或主城導流，再對照 `docs/3yWebsite/docs/maps.md` / `docs/3yWebsite/docs/data/maps.json`
8. 若牽涉新手區、主城服務點或教學導引，再對照 `docs/3yWebsite/docs/newbie.md`
9. 若房間有 `#Keyword` 或描述暗示特殊互動，再逐房檢查玩家實際看到的名詞與動詞是否還能導向正確操作
10. 若房間設計成可被問路找到，再逐房檢查 `#Enquire` 同義詞是否已落地
11. 若房間描述提示的是非內建指令，再確認它的實作位置真的存在：不是 `do_*` 命令，就是 `#Job -> src/job.c` 可解析的 function
12. 若牽涉技能來源、訓練 NPC、秘笈物件或職業導引，再對照 `docs/3yWebsite/docs/skills.md` / `docs/3yWebsite/docs/data/skills.json`；若這輪還新增了目前 repo 的新技能，再補查 `docs/current-game/skills.md` / `docs/current-game/skills.json`
13. 若牽涉國家首都、領地入口、官署、公告板或建國/叛國流程，再對照 `docs/3yWebsite/docs/realm.md` / `docs/3yWebsite/docs/data/realm_commands.json`
14. 若牽涉世界觀敘事、官方公告、元老/神族 NPC 或公開版提示，再對照 `docs/3yWebsite/docs/system.md`、`docs/3yWebsite/docs/data/news.json`、`docs/3yWebsite/docs/data/immortals.json`
15. 若這輪有新增或修改 `mob/*.mob`，先比對 `Class` 是否來自 repo 內已成功載入的常數；不要把文件或直覺猜到的 class name 直接拿去賭 parser 會接受
15.1 若這輪有新增或修改 `mob/*.mob`，確認 `Name` 存在且仍是玩家 / loader 會拿來比對的最短關鍵字；預設使用英文或至少 ASCII-friendly token，不要把 `ShortDesc` 的中文顯示名直接塞進 `Name`
15.2 若這輪有新增或修改 `mob/*.mob`，確認 `Level` 同時符合兩層條件：loader hard gate 仍是 `1..120`，但 world-map-area-rebuild 與新建 area 的 authoring cap 一律是 `1..100`；只要看到 `>100`，預設先回修，不要把它當成可直接帶過的 endgame 例外
16. 若這輪有新增或修改 `obj/*.obj` 的 `ITEM_FOOD` / `ITEM_DRINK_CON`，在啟動前先對照 working examples，確認 `Value*` 欄位已補齊且語意合理
16.1 若這輪有新增或修改 `obj/*.obj`，先做一輪欄位名靜態檢查：area object loader 預期的是 `Name / ShortDesc / Description / ItemType / Takeable / WearLoc / Value*` 這一系欄位；若看到 `Keywords / ExtraFlags / WearFlags` 這類更像 runtime/save serialization 的欄位名，先回修，不要等到 smoke test 才發現
16.2 若這輪有新增或修改 `res/*.res`，先做一輪格式檢查：現行 area reset loader 預期的是單行 `M/O/P/G/E/D/R/A` 指令並以 EOF 結束；若看到 `#MOB / #OBJ / Room / MaxInArea / MaxInRoom` 這類 block 風格，或照舊文件額外放了 literal `S` terminator，先回修，不要等到啟動期才被 `Fread_number` 擋下來
17. 若環境允許，實際啟動遊戲或執行區域 reload；優先讀第一個錯誤，而不是一次猜全部
18. 若有做 smoke test，先清空 `debug/*` 內容，再開始測試，避免把舊 bug 誤當成這次新增 area 的結果
19. 成功與否不能只看 process 是否暫時存活；至少要確認 log 或啟動輸出中出現明確成功訊號
20. 若已有對應 log，可跑 `python3 tools/log_parse_summary.py <logfile>` 幫忙抓成功訊號、關鍵字與 `debug/*` 非空檔案；但最終仍要人工判讀第一個 area/load 錯誤
21. 若這輪有改 `obj/*.obj`，特別是特殊 `ItemType`，額外檢查 `debug/badobject`；不要只看 `debug/bugs`
22. 只要這輪新增或修改過物件，即使已看到成功訊號，`debug/badobject` 仍應視為 release blocker；若有新條目，先回修再宣告 area smoke test 通過
23. 即使已看到成功訊號，仍要回頭檢查 `debug/*`、`log/` 是否出現和本次新增 area 相關的新 bug、warning、`Load_room`、`load_mobiles`、reset 或檔案開啟錯誤
23.1 若這輪有改 `mob/*.mob`，特別掃一次 `Load_mobiles﹕怪物 %d 沒有名字。` 與 `Load_mobiles﹕怪物 %d 等級 %d 不合理。`；這兩種錯誤通常可以直接定位到 `Name` / `Level` 欄位，而不需要先懷疑整個 area 結構
24. 若這輪有改 `mob/*.mob` 的 `AutoEnable` / `Enable`，額外檢查 `debug/failenable`；把它視為怪物技能配置 gate，而不是可以忽略的雜訊
25. 若 `debug/failenable` 出現 `怪物編號 %d 技能 %s 太差/太高`，先沿著第一個 VNUM 回查 `mob/*.mob`，並確認那是 `AutoEnable` 推算極端值，不是玩家 `enable` 數量或 `max_enable` 上限問題
26. 若本輪修法是把 `AutoEnable` 改成固定 `Enable`，回報時要明講這是「固定結果以消除載入警告」而不是「重新平衡整個技能系統」；若反而選擇保留 `AutoEnable`，也要明講你是依什麼理由改技能或 `AttackRatio` / `DodgeRatio`
27. 若要快速取 gate 建議，可跑 `python3 tools/area_acceptance_gate.py <area_slug> [--log-file <logfile>]`；但它只提供保守建議，不取代 tracker 與人工判讀
28. 查看 `debug/`、`log/` 是否出現 `Load_room`、`load_mobiles`、reset 或檔案開啟錯誤；若有 area diagnostics 附帶 area 檔名與行號，優先沿著第一個定位點回修
29. 回報時要列出：改了哪些區域檔、哪些系統檔被連動修改、是否引用了 docs 服務資料、是否動到區域地圖檔、是否使用 Python scaffold 產生 `.roo`、以及還沒驗證到的風險
30. 若任務來自長期重建計畫，也要回報：是否更新 `area/rebuild_plan.md`、下一個推薦 area 是哪個、以及固定 prompt 下次會落到哪份計畫
