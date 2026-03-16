---
name: merc-local-ops
description: 操作目前工作區內 merc-fju-3.0 的本機建置、設定、Docker smoke test 與啟停排錯時使用：依 README、AGENTS.md、src/Makefile、src/Makefile.lin、src/startup、src/startup.bash、src/merc.sample.ini / src/merc.ini 與 log/debug 實際狀態，協助在 Windows+WSL(Ubuntu) 與 Mac+Docker(Ubuntu) 兩條主要開發路徑上編譯 merc、檢查模板 ini 與本機生成 ini、確認 log/player/mail/debug/vote 等目錄可寫、處理 shutdown.txt、CLion / IDE shell 設定錯誤、用 zsh 執行 bash 腳本導致的 `BASH_SOURCE` 類錯誤，以及把 toolchain / shell / 容器問題和 world-data 載入錯誤分開。
---

# Merc Local Ops

此技能用來處理 `merc-fju-3.0` 目前 repo 內真實存在的本機操作流程，並以兩條主要開發環境為中心：
- `Windows + WSL (Ubuntu)`：在 WSL 內建置與啟動，必要時由 PowerShell / IDE 橋接進去。
- `macOS + Docker (Ubuntu)`：以 Docker 內的 Ubuntu 做 Linux build / smoke test，macOS 宿主機主要負責工作樹與容器調度。

先以 `README.md`、`AGENTS.md`、`src/startup`、`src/startup.bash`、`startup-wsl.ps1`、`src/merc.sample.ini`、`src/merc.ini`、`etc/`、`log/`、`debug/` 為準，不要沿用不存在的 `start-merc.sh` 或 `scripts/bootstrap.sh` 假設。

## 快速開始
1. 先判斷目前要走哪條主路徑：`Windows + WSL (Ubuntu)` 還是 `macOS + Docker (Ubuntu)`。
2. 若目標是建置，先確認真正持有 `make` / `gcc` 的地方是 WSL 還是 Docker 容器，不要把宿主 shell 誤當成執行面。
3. 若目標是啟動，先確認 `src/merc` 已編好、`src/merc.sample.ini` / 本機生成的 `src/merc.ini` 路徑正確、runtime 目錄可寫，再決定要直接跑 `startup.bash` 還是先做 Ubuntu smoke test。
4. 若啟動失敗，先判斷是 toolchain / shell / 容器問題、設定路徑問題、目錄不可寫、`shutdown.txt` 殘留，還是遊戲資料載入錯誤。
5. 需要指令與排錯順序時，再讀 `references/local-ops-cheatsheet.md`。

## 先看目前 repo 現況
- 目前 repo 根目錄沒有 `start-merc.sh`、`start-merc.ps1`、`start-merc.cmd`
- `scripts/` 目前可見腳本只有 `scripts/convert_big5_to_utf8.py`
- 實際存在的啟動入口是 `src/startup`
- 另外現在已有可在 WSL / bash 直接使用的 `src/startup.bash`
- repo 根目錄另外有 `startup-wsl.ps1`，供 Windows PowerShell / CLion 轉進 WSL 後呼叫 `src/startup.bash`
- tracked 的 ini 模板現在是 `src/merc.sample.ini`
- `src/startup` 與 `src/startup.bash` 都會以 `src/merc.sample.ini` 為模板產生本機用 `src/merc.ini`，並自動把 `HOME DIRECTORY` 指到目前 repo 根目錄
- `startup-wsl.ps1` 應以 `$PSScriptRoot` 推導 repo 根目錄，再透過 `wslpath` 換算成 WSL 路徑；避免把 `H:\...` 或 `/mnt/h/...` 寫死進 repo
- `src/merc` 本體若不帶參數，會先看環境變數 `merc`，否則 fallback 到內建預設 `merc.ini`
- 版本控制內可直接檢視的主要模板設定檔是 `src/merc.sample.ini`
- `etc/` 目前有多個 runtime / 半動態檔，但工作樹內沒有 `etc/merc.ini`
- 在這個工作區的常見現況下，Windows 端常只有 `powershell` / `wsl.exe`，真正可用的 `make`、`gcc` 在 WSL 內；要先探測，不要直接判定「無法編譯」
- `src/startup` 是 `csh` 腳本；在 WSL / Ubuntu 裡不一定有 `csh` 或 `tcsh`
- `src/startup.bash` 是 Bash 腳本，依賴 `BASH_SOURCE[0]` 推導腳本位置；若被 `zsh startup.bash` 或 CLion 的 zsh shell runner 執行，會因 `BASH_SOURCE[0]: parameter not set` 類錯誤直接失敗
- `Windows + WSL (Ubuntu)` 若看到 `/usr/bin/env: 'bash\r': No such file or directory`，優先判斷是 `src/startup.bash` 被存成 `CRLF`，讓 shebang 變成 `#!/usr/bin/env bash\r`
- 這類 shebang 行尾錯誤可先用 `Format-Hex src/startup.bash | Select-Object -First 3`，或在 WSL 內 `head -n 1 ./startup.bash | od -An -t x1` 確認第一行結尾是否為 `0D 0A`
- 若 repo 需要長期避免這類問題，優先在 `.gitattributes` 明確固定 `*.sh`、`*.bash` 與 `src/startup` 為 `LF`
- `src/Makefile.lin` 現在已補上和主 `Makefile` 一致的 `LIBS` 判斷：Ubuntu build path 會帶 `-lcrypt`，Darwin 則不帶
- 在 macOS 上若要驗證 Ubuntu 行為，優先用 Docker 掛載工作樹到 Ubuntu 容器，再跑 `Makefile.lin` 與 `startup.bash` smoke test
- 目前 repo 已驗證可同時通過 `make -C src clean && make -C src merc` 與 `make -C src -f Makefile.lin clean && make -C src -f Makefile.lin merc`，兩邊都應維持 warning-free；任一邊重新出現 warning 都應先視為 regression
- 生成後的 `src/merc.ini` 才是 `./merc` 無參數時真正會吃到的本機設定；模板 `src/merc.sample.ini` 不應直接拿來當跨機器共用實機設定
- 若 `src/merc.sample.ini` 被修正或替換，既有的 `src/merc.ini` 不會自動刷新；必要時要刪掉舊的 `src/merc.ini` 再重新跑 `startup` / `startup.bash`
- `src/merc.sample.ini` 若看起來被截斷、缺少後半段設定或 `Ticket Set` 之類關鍵項目，會直接造成啟動期誤判；先把模板完整性查清楚，不要只盯著 binary
- `mail/`、`debug/`、`vote/`、`board/`、`data/`、`etc/` 常已存在，但 `log/`、`player/` 可能需要在本機先建立
- 某些 runtime 檔雖然看起來像執行期產物，卻是 tracked 檔；目前至少要留意 `debug/error`、`etc/net.log`、`etc/stock`
- 對這類「已被 git 追蹤、但本機常被執行期改寫」的檔案，優先建議使用本機 `git update-index --skip-worktree`，不要修改 repo 的 `.gitignore`
- 目前這個 repo 常見適合本地 `skip-worktree` 的 tracked runtime 檔包含 `debug/badfile`、`debug/badobject`、`debug/bugs`、`debug/chat.log`、`debug/error`、`debug/failenable`、`debug/failexit`、`debug/failload`、`debug/failpass`、`debug/suicide.log`、`debug/suspect`、`debug/xnames.log`、`etc/net.log`、`etc/stock`、`etc/database`、`etc/address`、`mail/.mud`、`vote/.mud`、`board/.mud`
- 對 `src/shutdown.txt` 這類未追蹤且只想本機忽略的檔案，優先放進 `.git/info/exclude`，避免把個人偏好寫進 repo
- 目前這個 repo 常見適合本地 `.git/info/exclude` 的未追蹤 runtime 產物包含 `/src/merc.ini`、`/src/shutdown.txt`、`/log/*.log`、`/player/*`

## 工作流程

### 1. 建置
- `macOS` 宿主機原生 build 基準：`make -C src clean && make -C src merc`
- `Windows + WSL (Ubuntu)`：先從 PowerShell 探測 `wsl.exe` 與 WSL 內的工具鏈，再在 WSL 內執行 `cd src && make clean && make`
- `macOS + Docker (Ubuntu)`：優先在 Ubuntu 容器內執行 `make -C src -f Makefile.lin clean && make -C src -f Makefile.lin merc`
- 若任務只是 area plan、tracker、`map.md` spec，或純 area data 且沒有碰 `src/`，預設不要把 Docker / Ubuntu build 當每一步的固定成本；先做本機快速驗證，必要時再升級
- 若任務和 warning、toolchain parity、跨平台回歸有關，預設要同時驗證 macOS 原生與 Ubuntu build；不要只驗單邊
- 若目前 shell 是 PowerShell，先檢查：
- `Get-Command make, gcc, wsl -ErrorAction SilentlyContinue`
- 若 PowerShell 沒有 `make`，但 `wsl.exe` 存在，接著檢查：
- `wsl.exe bash -lc 'cd /mnt/<drive>/<path>/src && command -v make && command -v gcc'`
- 若 WSL 內有工具鏈，優先把建置命令改成在 WSL 執行，而不是停在「PowerShell 找不到 make」
- Windows 路徑轉 WSL 路徑時，像 `H:\repos\merc-fju-3.0` 應轉成 `/mnt/h/repos/merc-fju-3.0`
- 若要在 macOS 上重現 Ubuntu 問題，優先用 Docker 啟 Ubuntu 容器，不要拿宿主機的 Darwin build 當 Linux 結果
- 若 `Makefile.lin` 報 `crypt` 解析失敗，先檢查當前工作樹是否包含 `LIBS` / `$(LIBS)` 修正，不要先去安裝額外套件
- 適合升級到 Ubuntu / Docker 的常見時機：有改 `src/`、`Makefile*`、`startup*`、`merc.sample.ini`、看到平台相依錯誤，或準備把一整段 area milestone merge 回主線前做較高信心驗證

### 2. 設定
- 先檢查 `src/merc.sample.ini`
- 需要部署說明時，可補充 README 提到的 `etc/merc.ini` 用途，但要明講目前 repo 工作樹內不含該檔
- 先確認至少這些欄位：
- `NAME`
- `MUD PORT`
- `HOME DIRECTORY`
- 各種 `* DIRECTORY`
- 若啟動訊息出現 `generate_ticket: 沒有中獎的資料.`，先回頭檢查 ini 內是否真的有 `Ticket Set = ...`，因為這組資料是從 ini 建立，不是另外讀某個 ticket 檔
- 若路徑和目前工作區不一致，優先建議直接修正設定，而不是發明額外 wrapper
- `Windows + WSL (Ubuntu)` 下，`HOME DIRECTORY` 應對到 WSL 路徑，例如 `/mnt/h/...`
- `macOS + Docker (Ubuntu)` 下，若是容器 smoke test，`HOME DIRECTORY` 應對到容器內掛載路徑，例如 `/workspace/merc-fju-3.0`
- 若只是 smoke test，可接受先由 `merc.sample.ini` 產生本機 `merc.ini` 或臨時 `merc.test.ini` 指到目前 workspace，再用它啟動；回報時要明講這是測試用設定，不是永久修正

### 3. 啟動與停止
- 啟動流程以 `src/startup` 為主
- 若目前環境沒有 `csh` / `tcsh`，優先改用 `src/startup.bash`
- 若使用者是在 Windows IDE 內啟動，優先考慮 repo 根目錄的 `startup-wsl.ps1`
- 若使用者是在 CLion 或其他 IDE 內直接跑 `src/startup.bash`，明確提醒 interpreter 要設成 `bash`，不要設成 `zsh`；若 IDE 只是在 terminal 內手動執行，也要用 `bash ./startup.bash` 或直接 `./startup.bash`
- 若使用者是在 macOS 上驗證 Ubuntu，可在 Docker 容器內用 `timeout 45s` 到 `60s` 跑 `cd src && ./startup.bash`
- `src/startup` 與 `src/startup.bash` 的預設流程都應優先視為「自動產生本機 ini 並啟動」
- `startup-wsl.ps1` 應只負責橋接 PowerShell 與 WSL，不要複製 bash 啟動邏輯
- 做 smoke test 或 area 載入驗證前，先清空 `debug/` 內既有檔案內容，並先建立本輪 `log/` 觀察基線（例如記下最新 log 檔名，或清空這輪要看的單一 log）；否則測試後很難分辨哪些是本次執行的新訊號、哪些只是歷史殘留
- 先確認 `csh` / `tcsh` 是否存在；若沒有，直接指出 `startup` 目前不可直接執行，不要假裝它是通的
- `startup` 會：
- 在 `src/` 內移除 `shutdown.txt`
- 於 `../log/` 找下一個可用的 `<number>.log`
- 執行 `../src/merc merc.ini`
- 若看到 `shutdown.txt` 則結束 loop
- 回答時清楚區分：
- 「如何從 `src/startup` 啟動」
- 「何時改用 `src/startup.bash`」
- 「`merc` 本體是否存在」
- 「退出是因為腳本流程，還是因為遊戲載入失敗」
- 若建置是在 WSL 內完成，也優先假設啟動要在同一個 WSL 環境內做，再檢查 `HOME DIRECTORY` 與 runtime 目錄是否仍對應到 WSL 可見路徑
- 若建置是在 Docker Ubuntu 內完成，也優先在同一個容器 / 同一條容器掛載路徑裡做 smoke test，避免主機與容器看到不同路徑
- 若 `startup` 因缺少 `csh` 無法執行，但 `merc` binary 本體可跑，允許先用 `./merc <temp-ini>` 做 smoke test，把 shell 問題和遊戲載入問題拆開
- 若直接執行 `./merc`，要記得它預設仍會讀 `merc.ini`；因此本機跨機器流程應先確保 `startup` / `startup.bash` 已生成正確的本機 `merc.ini`
- 若使用 `startup-wsl.ps1`，確認 `wsl.exe` 與 WSL 內的 `wslpath` 可用，再讓它轉呼叫 `src/startup.bash`
- 若 `startup-wsl.ps1` 本身正常，但 WSL 一進 `startup.bash` 就報 `bash\r`，先修腳本行尾，不要誤判成 `wsl.exe` 或 PowerShell 橋接壞掉
- 若剛修過 `src/merc.sample.ini`，啟動前先刪掉舊的 `src/merc.ini`，避免用到先前生成的壞設定；重新生成後再檢查 `HOME DIRECTORY`
- 若執行目的是 world-data / loader 驗證，但預設 `MUD PORT` 已被占用，可複製 `src/merc.ini` 成臨時 `src/merc.test.ini`，把 `MUD PORT` 與相鄰服務 port 改成未占用值，再直接跑 `./merc merc.test.ini`；這能把 bind 問題和資料載入問題拆開
- 若用 `timeout` 做 smoke test，時間要明顯高於正常開機時間；預設優先用 `45` 到 `60` 秒，避免因測試工具太早殺行程而誤看到「系統不正常終止」
- 成功訊號至少要記錄像 `三國歪傳之降龍伏虎開始正常運作` 這種明確啟動完成字樣；不要只因為程式暫時沒退出就視為成功
- 若 `log/*.log` 已出現「開始正常運作」，但尾端接著出現「系統不正常終止」，先確認是否只是 smoke test 的 `timeout` 主動中止；這和啟動失敗是兩件事
- 即使已看到成功訊號，仍要回頭檢查 `debug/*` 是否留下和本次修改、尤其是新增 area 相關的錯誤或警告

### 4. 目錄可寫性與 runtime
- 啟動前常要檢查：
- `log/`
- `player/`
- `mail/`
- `debug/`
- `vote/`
- 必要時也檢查 `board/`、`etc/`、`data/`
- 若 `log/` 或 `player/` 根本不存在，先把它視為需要建立的 runtime 目錄，不要只回報「不可寫」
- 若是 Codex Cloud setup / maintenance script，建立 runtime 目錄可直接用 `mkdir -p log player mail debug vote`
- 啟動或 smoke test 後，若 `git status` 出現 `debug/error`、`etc/net.log`、`etc/stock` 之類 tracked runtime 檔變動，要先判斷那是測試副作用還是任務本身的一部分
- 若不可寫，先指出哪個目錄是 blocker，再給最小修復步驟
- 不要預設這一定是 WSL ACL 問題；先以目前實際 OS / 檔案權限為準
- 讀 log 時優先看本輪新產生的 `log/*.log`，或你在測前先建立基線後鎖定的那份 log，確認是否已出現「開始正常運作」或資料載入總結；`debug/bugs` 常會混著舊錯誤，不能單看最後幾筆就判定目前仍失敗
- 若本輪測試前已先清空 `debug/*`，那麼測試後新增的 `debug/bugs`、`debug/error`、`debug/failenable` 等內容就應優先視為本次執行的新結果，必須逐一判斷是否和本次 area 改動有關
- `debug/failenable` 不是玩家 `enable` 數量不足，也不是 `max_enable` 上限告警；它是怪物載入 `AutoEnable` 時，`src/load.c -> get_adeptation()` 算出的熟練度極端值警告
- 若 `debug/failenable` 出現 `怪物編號 %d 技能 %s 太差/太高`，先把它歸類成 `mob/*.mob` 的 area data 問題：檢查對應怪物的 `AutoEnable`、`AttackRatio`、`DodgeRatio`、Level 與技能型態，再決定要改成固定 `Enable`，或改技能 / 係數；不要誤往玩家 `enable` 指令或本機 shell 問題排查
- 若只是要做短期止血、或對象是服務型 / 非戰鬥核心 NPC，固定 `Enable` 仍是最小修復；但若對象是守衛、禁軍、高手、盜賊這類戰鬥核心 NPC，應升級成 area / docs 層面的技能定位調整，不要把 `Enable 100` 當長期答案
- 若 log 或終端出現 `Load_skill﹕技能名稱 XXX 重覆`，優先檢查三件事：是否覆蓋了既有 `skill/<letter>/*.ski`、`skill/skill.lst` 是否重複 key、不同 skill 檔的 `Name` 是否撞名；這通常是 skill 登錄或檔名衝突，不是 build / shell 問題
- 若 log 或終端出現 `Fread_number: 讀取檔案已定義字串 SLOT_... 錯誤`，優先檢查新 `SLOT_*` 是否只加在 `src/merc.h`，卻漏了 `data/symbol.def`；這是 loader 常數表不同步，不是 area parser 壞掉

### 5. 排錯分流
- **編譯錯誤**：處理 `src/*.c`、`include/*.h`、`Makefile*`
- **設定錯誤**：處理 `src/merc.sample.ini`、本機生成的 `src/merc.ini` 與 `HOME DIRECTORY` / 目錄路徑
- **模板與生成檔不同步**：處理 `src/merc.sample.ini` 已修正但 `src/merc.ini` 仍是舊內容，需要刪掉重生
- **啟動腳本問題**：處理 `src/startup`、`shutdown.txt`、`merc` 是否存在
- **Shell / 工具鏈錯置**：處理 PowerShell 沒有 `make`、WSL 有工具鏈、路徑轉換、`wsl.exe` 可否進入工作區
- **Shell 類型錯置**：處理把 Bash 腳本交給 `zsh` / IDE 預設 shell 執行，導致 `BASH_SOURCE`、陣列展開、`set -eu` 等 Bash-only 行為出錯
- **Docker / Ubuntu 路徑錯置**：處理 macOS 宿主機路徑、容器掛載路徑、`HOME DIRECTORY`、容器內 runtime 目錄
- **Shell 相依缺件**：處理 `startup` 依賴 `csh` / `tcsh`、WSL 只有 `bash` 時的 fallback
- **Runtime 目錄缺漏**：處理 `log/`、`player/` 尚未建立但 binary 本身其實可啟動
- **Tracked runtime 汙染**：處理測試後被碰到的 `debug/error`、`etc/net.log`、`etc/stock` 等 tracked 檔，避免誤 commit
- **本機 runtime 靜音**：處理如何在不改遠端 repo 規則的前提下，用 `skip-worktree` 或 `.git/info/exclude` 降低本機反覆出現的 runtime 噪音
- **資料載入錯誤**：看 `log/*.log`、`debug/`，並把問題轉交到 area / world-data 修復，不要繼續當作純本機 ops 問題

## 回答規則
- 先給最短可執行命令，再補一句用途或風險
- 明確指出命令應在哪個目錄執行
- 若 repo 內沒有使用者提到的 launcher 或腳本，直接說不存在，再改用現有入口回答
- 若 PowerShell 找不到 `make`，先檢查 WSL 是否可用與 repo 是否可從 `/mnt/<drive>/...` 存取；只有在 WSL 也沒有工具鏈時，才回報缺少編譯環境
- 若使用者提到 `make -C src -f Makefile.lin` 與 `crypt` 解析失敗，直接指出這是舊 Linux Makefile 連結步驟缺少 `-lcrypt`，目前 repo 應改用已修正的 `src/Makefile.lin`
- 若使用者明講是 `Mac+Docker(Ubuntu)`，優先把 Linux 驗證放進 Docker 裡，不要把 Darwin build 結果誤當 Ubuntu 結果
- 若使用者問「還有沒有 warning」或要做 warning cleanup，預設答案基準應同時包含 macOS 原生與 Ubuntu build；目前 repo 目標是兩邊都 warning-free
- 若 `startup` 存在但 shell 相依缺件，明確說「入口存在，但目前環境缺少 `csh` / `tcsh`，因此不能直接用它」
- 若使用者貼出 `/bin/zsh .../src/startup.bash` 或 `BASH_SOURCE[0]: parameter not set`，先直接指出這是「用錯 shell」而不是 repo 腳本本身壞掉；最短修正是改成 `cd src && ./startup.bash` 或 `/bin/bash src/startup.bash`
- 若要做 smoke test，可先建立缺少的 runtime 目錄並用臨時 ini 驗證 binary 是否能進到資料載入階段
- 若啟動測試碰到 tracked runtime 檔，但那些變動不是本次交付物，回報時要明講並在結束前清回乾淨
- 若使用者希望長期降低本機 runtime 噪音：
- 對 tracked 檔用 `git update-index --skip-worktree <path>`
- 對未追蹤但只想本機忽略的檔案用 `.git/info/exclude`
- 套用後可用 `git ls-files -v | grep '^S '`，或 PowerShell 的 `git ls-files -v | Select-String '^S '` 驗證哪些 tracked 檔已被本地靜音
- 不要把這類個人本機靜音需求直接寫進 repo `.gitignore`，除非它對整個團隊都合理
- 若 `debug/bugs` 只剩舊錯誤，但最新 `log/*.log` 已出現「開始正常運作」，要明講 `debug/bugs` 是歷史噪音，不代表這次啟動仍失敗
- 但若測試前已先清空 `debug/*`，就不能再把測試後的 debug 訊息當成歷史噪音略過；必須回頭判斷它們是否是這次新增 area / reset / room / mob / obj 帶出的新問題
- 若 log 已顯示 `Load_room`、重複 VNUM、mob/obj/reset parse error，立即切換成資料層錯誤描述
- 若使用者只是要查狀態或看 log，不要一開始就建議修改腳本

## 參考資料
- `README.md`
- `src/startup`
- `src/merc.sample.ini`
- `src/merc.ini`
- `references/local-ops-cheatsheet.md`
