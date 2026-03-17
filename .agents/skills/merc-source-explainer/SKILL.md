---
name: merc-source-explainer
description: 解說目前工作區內 merc-fju-3.0 的 Merc MUD 原始碼、設定檔與資料目錄時使用：追程式流程、回答 src/*.c 與 include/*.h 的責任、說明 merc.ini 與 area/angel/command/skill/social/data/help 等檔案如何被載入、協助定位 bug 或功能修改入口，並在需要建置/啟動脈絡時依 README、src/startup、src/startup.bash 的實際狀態回答，包括說明 legacy csh launcher、bash launcher 與 IDE shell 設定差異。
---

# Merc Source Explainer

此技能用來解說 `merc-fju-3.0` 目前實際存在的原始碼與資料樹。先以 repo 真實檔案為準，不要沿用舊版 2.0、WSL wrapper、或已不存在腳本的假設。

## 快速開始
1. 先確認問題屬於哪一類：程式流程、設定檔、資料格式、建置啟動、或 bug 追查。
2. 先讀 `README.md` 與 `references/overview.md`，建立目前 3.0 repo 的總覽。
3. 若題目和 `.ski`、`pry` 技能說明、`SLOT_* / EFFECT_* / ATTACK_*`、或技能學習限制有關，優先看：
   - `docs/current-game/skill-file-format.md`
   - `docs/current-game/skill-loader-reference.md`
   - `docs/current-game/skill-constants.md`
   - `docs/current-game/skill-pry-crosswalk.md`
4. 需要講程式邏輯時，直接開對應的 `src/*.c`、`include/*.h`、`src/merc.sample.ini` / `src/merc.ini`、`document/*.txt`，不要只憑記憶回答；若只是先找 legacy 文件入口，可先看 `docs/current-game/legacy-documentation.md`。
5. 如果文件與程式不一致，以 `src/*.c`、`src/merc.h`、runtime data 檔為準，並明確指出哪個說明頁需要回補。
6. 回答時優先把「入口檔案」「呼叫鏈」「對應資料檔」一起講清楚，讓使用者知道下一步該去哪裡改。
7. 如果問題其實是區域建置或管理員指令，改用更專門的技能，例如 `merc-area-builder` 或 `mud-command-handbook`。

## 先看目前 repo 現況
- 核心程式碼在 `src/`，包含 `merc.ini`、`startup`、`Makefile` 與大量 `*.c`
- 目前 repo 根目錄沒有 `start-merc.sh`、`start-merc.ps1`、`start-merc.cmd`、`scripts/bootstrap.sh` 這類 wrapper；講啟動流程時應以 `README.md` 與 `src/startup` 為準
- `src/startup` 是 legacy `csh` launcher，`src/startup.bash` 則是目前給 bash 環境使用的入口；若使用者貼的是 `/bin/zsh .../startup.bash` 或 `BASH_SOURCE[0]: parameter not set`，要先指出是 shell 不相容，不要誤判成 MUD 載入失敗
- `docs/` 目前主要是 `docs/3yWebsite/` 文件站，不要引用不存在的 `docs/DATA_LAYOUT.md` 或 `docs/RUNTIME_RESET.md`
- `docs/current-game/` 現在已有 hand-maintained 的 `.ski` / `pry` 文件頁，也開始承接 `document/` 的 Pages 化入口；可當作技能資料格式、玩家文案對照與 legacy 手冊導覽的第一層入口，但涉及 runtime 爭議時仍要回頭查 `src/load.c`、`src/act_info.c`、`src/merc.h`
- `scripts/` 目前可見腳本只有 `scripts/convert_big5_to_utf8.py`
- `etc/` 目前存在多個 runtime / 半動態檔案，但工作樹裡沒有 `etc/merc.ini`；設定解說應先看 `src/merc.sample.ini` 與本機生成的 `src/merc.ini`，再說明部署時可能會複製到 `etc/`

## 回答流程

### 1. 先分類問題
- **建置/啟動**：看 `README.md`、`src/Makefile*`、`src/startup`
- **設定檔**：看 `src/merc.sample.ini`、本機生成的 `src/merc.ini`，必要時再比對 `etc/` 與 `src/ini.c`
- **資料載入**：看 `src/db.c`、`src/load.c`、`src/reload.c` 以及 `document/*.txt`
- **技能格式 / 學習說明 / pry 文案**：先看 `docs/current-game/skill-*.md`，再交叉驗證 `src/act_info.c`、`src/load.c`、`src/bit.c`、`src/class.c`、`src/function.c`
- **遊戲邏輯**：依主題追 `src/act_*.c`、`fight.c`、`magic.c`、`skill.c`、`job.c`、`variable.c`
- **檔案儲存/玩家資料**：看 `src/file.c`、`src/save.c`、`src/ini.c` 與 `player/`, `mail/`, `board/`, `data/`, `etc/`

### 2. 用實際檔案建立答案
- 先指出功能入口檔
- 再指出相關設定或資料檔
- 若邏輯分散，給出最短可理解的呼叫鏈
- 若使用者想改功能，明確指出優先修改點與可能連動檔案

### 3. 遇到資料格式問題時回到文件
- 房間、NPC、物件、reset、商店格式優先看：
- `docs/current-game/legacy-documentation.md`
- `docs/current-game/object-file-format.md`（物品格式時優先）
- `document/room.txt`
- `document/mob.txt`
- `document/obj.txt`
- `document/reset.txt`
- `document/shop.txt`
- 技能檔 / `pry` 對照優先看：
- `docs/current-game/skill-file-format.md`
- `docs/current-game/skill-loader-reference.md`
- `docs/current-game/skill-constants.md`
- `docs/current-game/skill-pry-crosswalk.md`

## 常見解說主題

### 建置與啟動
- 目前 README 記載的標準流程是 `cd src` 後執行 `make clean && make`
- FreeBSD 需先把 `Makefile.bsd` 複製成 `Makefile`
- 啟動方式要分清楚：`src/startup` 是 legacy `csh`，`src/startup.bash` 是目前 bash-friendly 入口；回答時不要把兩者混成同一種 shell 條件
- `src/startup.bash` 內使用 `BASH_SOURCE[0]`，所以若被 `zsh` 執行會在很前面就失敗；這類問題要先歸類成 shell / IDE interpreter 問題，而不是遊戲 binary 或 world-data 問題
- 若使用者問 `merc` 不帶參數會吃哪個 ini，應直接追 `src/comm.c` 的 `main()`：它會先看命令列參數，再看環境變數 `merc`，最後 fallback 到 `INI_FILE`
- 若使用者問「為什麼開不起來」，先分清楚是編譯失敗、啟動腳本問題，還是區域/資料載入錯誤

### 設定檔
- `src/merc.sample.ini` 是目前 repo 內可直接讀到的主要設定模板；本機執行時常會先由啟動腳本生成 `src/merc.ini`
- `src/merc.sample.ini` 修好之後，不代表現有 `src/merc.ini` 會跟著更新；若要解釋「明明模板修了但啟動還是舊行為」，要把生成檔不同步一起講出來
- `src/merc.h` 目前把 `INI_FILE` 定義成 `merc.ini`
- 重點欄位通常包含：
- `MUD PORT`
- `NAME`
- `HOME DIRECTORY`
- 各種 `* DIRECTORY`
- `Help Extension` / `Social Extension` / `Skill Extension`
- `Player Angel`、`Attack Value`、`Skill Value` 等遊戲開關
- 若使用者問某欄位由誰使用，進一步追 `src/ini.c` 與實際讀取該值的模組
- 若使用者問 `generate_ticket: 沒有中獎的資料.` 是哪裡來的，應追 `src/db.c -> generate_ticket()` 與 `src/ini.c` 的 `Ticket Set` 解析；`order_list` 是從 ini 建立，不是額外 ticket 檔案

### 原始碼模組分工
- `act_*.c`：玩家指令與互動
- `db.c`, `load.c`, `reload.c`：資料載入、重載、啟動期初始化
- `fight.c`, `magic.c`, `skill.c`, `spell.c`：戰鬥、法術、技能
- `job.c`, `variable.c`, `system.c`：系統規則、固定流程、全域變數/常數
- `file.c`, `save.c`, `ini.c`：設定與檔案 I/O
- `angel.c`, `bus.c`, `ship.c`, `bounty.c`：具體系統模組與對應資料檔

### 指令與房間互動入口
- 一般玩家指令先看 `interp.c`，它會先在命令表中找對應的 `do_*` 函式
- 移動與常見動作通常落在 `act_move.c`、`act_obj.c`、`act_info.c` 等檔案，例如 `do_enter` 在 `act_move.c`
- `interp.c` 不只派送一般指令；若房間、房內 NPC、房內物件載入了 `job`，也會依 `keyword` 把玩家輸入轉到對應 job function
- `job.c` 是 room / mob / object job function 的註冊表入口；如果某個互動不是現成 `do_*` 指令，也不是已註冊 job，那就算 area 文案寫了提示，玩家仍然不能真的執行
- 以目前 repo 狀態來看，`bore` 是典型例子：`area/newfight/roo/1211.roo` 的 `#Keyword hole~` 會提示玩家輸入 `bore`，但目前找不到 `do_bore`，而 `job.c` 也只註冊少數 job，因此不能把這類文案直接當成「功能已存在」

### 資料目錄與程式的對應
- `area/`：世界區域資料
- `angel/`：守護神資料
- `command/`：指令定義
- `skill/`：技能資料
- `social/`：社交指令
- `help/`, `greeting/`, `joke/`：玩家可見文字
- `data/`, `board/`, `etc/`：系統資料與部分 runtime / 半動態資料
- `player/`, `mail/`, `log/`, `debug/`, `vote/`：執行後會變動的資料

### `.ski` / `pry` 問題的最短路徑
- 先用 `docs/current-game/skill-file-format.md` 找欄位
- 再用 `docs/current-game/skill-loader-reference.md` 確認 loader / function whitelist
- 需要常數時看 `docs/current-game/skill-constants.md`
- 需要把玩家文案對回 `.ski` 時看 `docs/current-game/skill-pry-crosswalk.md`
- 若文件與 runtime 不一致：
- `pry` 輸出優先追 `src/act_info.c -> do_pry()`
- 熟練稱號優先追 `src/bit.c -> adeptation_name()`
- 職業中文名優先追 `src/class.c -> class_name()`
- skill parser 與結構優先追 `src/load.c`、`src/merc.h`

### Bug 追查
- 不要一開始就猜答案；先找第一個報錯點
- 若是編譯錯誤，先看 `src/` 的對應 `.c/.h`
- 若是啟動期錯誤，先看 `log/`、`debug/`，再回頭找載入該資料的程式碼
- 若是資料錯誤，先找是哪個 parser 讀它，再核對 `document/*.txt` 格式
- 若是功能行為不符預期，從使用者看到的指令或效果回推到 `act_*.c`、`interp.c`、系統模組
- 若是「房間文字明明提示可以做某動作，但指令不能用」，優先分辨它是：
- 內建命令缺失：去找 `do_*` 是否存在、是否註冊到命令表
- room job 缺失：去找 `.roo/.mob/.obj` 是否有 `#Job`，以及 `src/job.c` 是否有對應 function

## 回答原則
- 保持繁體中文，必要時保留英文函式名、結構名、檔名
- 優先提供可追溯的檔案路徑與修改入口，不只做抽象解釋
- 明確區分「repo 目前存在的事實」和「我根據原始碼推測的行為」
- 若問題牽涉目前 repo 沒有的腳本或文件，直接指出不存在，並改以現有入口回答

## 參考資料
- `README.md`
- `references/overview.md`
- `src/merc.ini`
- `src/startup`
- `docs/current-game/skill-file-format.md`
- `docs/current-game/skill-loader-reference.md`
- `docs/current-game/skill-constants.md`
- `docs/current-game/skill-pry-crosswalk.md`
- `docs/current-game/legacy-documentation.md`
- `docs/current-game/object-file-format.md`
- `document/mob.txt`
- `document/obj.txt`
- `document/room.txt`
- `document/reset.txt`
- `document/shop.txt`
