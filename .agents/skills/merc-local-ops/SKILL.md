---
name: merc-local-ops
description: 操作目前工作區內 merc-fju-3.0 的本機建置、設定與啟停排錯時使用：依 README、src/Makefile、src/startup、src/merc.ini 與 log/debug 實際狀態，協助編譯 merc、檢查 etc 或 src 的 merc.ini、確認 log/player/mail/debug/vote 等目錄可寫、處理 shutdown.txt 與啟動失敗，並把資料載入錯誤和純環境問題分開。
---

# Merc Local Ops

此技能用來處理 `merc-fju-3.0` 目前 repo 內真實存在的本機操作流程。先以 `README.md`、`src/startup`、`src/merc.ini`、`etc/`、`log/`、`debug/` 為準，不要沿用不存在的 `start-merc.sh`、Windows wrapper 或 `scripts/bootstrap.sh` 假設。

## 快速開始
1. 先確認使用者是在 Linux / BSD shell，還是在 Windows 上只是查看 repo。
2. 若目標是建置，先依 `README.md` 走 `cd src && make clean && make`。
3. 若目標是啟動，先確認 `src/merc` 已編好、`src/merc.ini` 或部署用 `etc/merc.ini` 路徑正確、runtime 目錄可寫，然後以 `src/startup` 為中心回答。
4. 若啟動失敗，先判斷是編譯問題、設定路徑問題、目錄不可寫、`shutdown.txt` 殘留，還是遊戲資料載入錯誤。
5. 需要指令與排錯順序時，再讀 `references/local-ops-cheatsheet.md`。

## 先看目前 repo 現況
- 目前 repo 根目錄沒有 `start-merc.sh`、`start-merc.ps1`、`start-merc.cmd`
- `scripts/` 目前可見腳本只有 `scripts/convert_big5_to_utf8.py`
- 實際存在的啟動入口是 `src/startup`
- 版本控制內可直接檢視的主要設定檔是 `src/merc.ini`
- `etc/` 目前有多個 runtime / 半動態檔，但工作樹內沒有 `etc/merc.ini`

## 工作流程

### 1. 建置
- 依 `README.md` 指示，標準流程是：
- `cd src`
- `make clean && make`
- FreeBSD 先把 `Makefile.bsd` 複製成 `Makefile`
- 若編譯失敗，先處理 `src/` 內的錯誤，不要先懷疑 runtime 或區域資料

### 2. 設定
- 先檢查 `src/merc.ini`
- 需要部署說明時，可補充 README 提到的 `etc/merc.ini` 用途，但要明講目前 repo 工作樹內不含該檔
- 先確認至少這些欄位：
- `NAME`
- `MUD PORT`
- `HOME DIRECTORY`
- 各種 `* DIRECTORY`
- 若路徑和目前工作區不一致，優先建議直接修正設定，而不是發明額外 wrapper

### 3. 啟動與停止
- 啟動流程以 `src/startup` 為主
- `startup` 會：
- 在 `src/` 內移除 `shutdown.txt`
- 於 `../log/` 找下一個可用的 `<number>.log`
- 執行 `../src/merc merc.ini`
- 若看到 `shutdown.txt` 則結束 loop
- 回答時清楚區分：
- 「如何從 `src/startup` 啟動」
- 「`merc` 本體是否存在」
- 「退出是因為腳本流程，還是因為遊戲載入失敗」

### 4. 目錄可寫性與 runtime
- 啟動前常要檢查：
- `log/`
- `player/`
- `mail/`
- `debug/`
- `vote/`
- 必要時也檢查 `board/`、`etc/`、`data/`
- 若不可寫，先指出哪個目錄是 blocker，再給最小修復步驟
- 不要預設這一定是 WSL ACL 問題；先以目前實際 OS / 檔案權限為準

### 5. 排錯分流
- **編譯錯誤**：處理 `src/*.c`、`include/*.h`、`Makefile*`
- **設定錯誤**：處理 `src/merc.ini` 與 `HOME DIRECTORY` / 目錄路徑
- **啟動腳本問題**：處理 `src/startup`、`shutdown.txt`、`merc` 是否存在
- **資料載入錯誤**：看 `log/*.log`、`debug/`，並把問題轉交到 area / world-data 修復，不要繼續當作純本機 ops 問題

## 回答規則
- 先給最短可執行命令，再補一句用途或風險
- 明確指出命令應在哪個目錄執行
- 若 repo 內沒有使用者提到的 launcher 或腳本，直接說不存在，再改用現有入口回答
- 若 log 已顯示 `Load_room`、重複 VNUM、mob/obj/reset parse error，立即切換成資料層錯誤描述
- 若使用者只是要查狀態或看 log，不要一開始就建議修改腳本

## 參考資料
- `README.md`
- `src/startup`
- `src/merc.ini`
- `references/local-ops-cheatsheet.md`
