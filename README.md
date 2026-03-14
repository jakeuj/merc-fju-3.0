# 輔大三國歪傳之降龍伏虎 (Merc-FJU 3.0 Rewrite)

> 📢 **2026-03-13 更新**：本 repo `merc-fju-3.0` 為 [jakeuj/merc-fju-2.0-utf8](https://github.com/jakeuj/merc-fju-2.0-utf8)
> 的 Rewrite（重寫）；2.0 會持續保留作為歷史參照，而 3.0 會在 Apple Silicon、Docker
> 與現代 Linux/macOS 環境上延伸既有改造並統整程式碼/資料。

> Merc-FJU 3.0 以 **Merc 2.2** 為核心，沿用 2.0 僅保留的 UTF-8 轉檔成果，
> 並在此乾淨基礎上重新整理 Docker 工具鏈、啟動腳本、程式碼與區域資料。
> 想了解最初的 UTF-8 轉換，請前往 2.0 repo；此 README 只留下 3.0 的入口，詳細操作請閱讀下方連結。

## 目錄結構

| 目錄 | 說明 |
|------|------|
| `src/` | C 語言原始程式碼 |
| `area/` | 遊戲區域資料 |
| `angel/` | 守護神設定資料 |
| `command/` | 指令資料 |
| `data/` | 系統資料 |
| `document/` | 本版參考手冊 |
| `doc/` | 原始 Merc 參考文件 |
| `include/` | 職業、地形等設定 |
| `etc/` | 雜項設定（含 `merc.ini`） |
| `greeting/` | 進站畫面 |
| `help/` | 線上求助檔案 |
| `skill/` | 技能資料檔案 |
| `social/` | 社交指令 |
| `board/` | 版面設定與資料 |
| `joke/` | 笑話集 |
| `player/` | 玩家存檔（執行時產生） |
| `mail/` | 玩家信件（執行時產生） |
| `log/` | 記錄檔（執行時產生） |
| `debug/` | 錯誤回報（執行時產生） |
| `vote/` | 投票資料 |

## 系統需求

- **OS**：Linux（核心 2.0.30 以上）或 FreeBSD
- **記憶體**：建議 32 MB 以上（執行需約 12 MB）
- **工具**：`gcc`（≥ 2.7.2.2）、`make`、`tar`、`zip`
- **函式庫**：`crypt` library（一般 Linux 內附）
- `/proc` 虛擬檔案系統支援（不需 root 權限）

## 開發環境

目前 README 主要針對兩種實際開發路徑：

- `Windows + WSL (Ubuntu)`：日常編譯與本機啟動主路徑
- `macOS + Docker (Ubuntu)`：用 Ubuntu 容器驗證 Linux build / warning / smoke test

若要確認 Linux 相容性，請以 Ubuntu 結果為準；不要把 macOS 原生 build 視為 Ubuntu 也一定乾淨。

目前 repo 也已驗證：
- `make -C src clean && make -C src merc` 在 macOS 原生路徑應可 warning-free 編譯
- `make -C src -f Makefile.lin clean && make -C src -f Makefile.lin merc` 在 Ubuntu 路徑應可 warning-free 編譯

若任一邊重新出現 warning，請優先視為 regression，並同步檢查另一邊是否也受影響。

## 編譯

```bash
# Windows + WSL (Ubuntu) / 一般 Linux
cd src
make clean && make

# macOS 原生驗證
make -C src clean && make -C src merc

# FreeBSD
cp Makefile.bsd Makefile
cd src
make clean && make
```

編譯完成後，`src/` 目錄下會產生可執行檔 `merc`。

若要在 `macOS + Docker (Ubuntu)` 驗證 Linux build，建議改用：

```bash
docker run --rm -v "$PWD":/workspace/merc-fju-3.0 -w /workspace/merc-fju-3.0 \
  ubuntu:24.04 bash -lc '
    apt-get update &&
    apt-get install -y build-essential perl &&
    mkdir -p log player mail debug vote &&
    make -C src -f Makefile.lin clean &&
    make -C src -f Makefile.lin merc
  '
```

若是在明確的 Linux / Ubuntu 容器內，建議改用：

```bash
make -C src -f Makefile.lin clean && make -C src -f Makefile.lin merc
```

原因是雲端容器通常走 Linux build path，而 `src/Makefile.lin` 現在已補上和主 `Makefile` 一致的 `LIBS` 判斷：非 Darwin 平台會自動連結 `-lcrypt`。若你在舊工作樹看到 `crypt` unresolved，先更新到包含此修正的版本，不要先假設缺少系統套件。

若這次任務是清 warning 或確認 cross-platform parity，建議至少跑兩條驗證：
- macOS 原生：`make -C src clean && make -C src merc`
- Ubuntu / Docker：`make -C src -f Makefile.lin clean && make -C src -f Makefile.lin merc`

## 設定

版控中的 ini 模板目前放在 `src/merc.sample.ini`。本機開發 / 測試時，建議不要直接手改 tracked 模板，而是讓啟動腳本自動產生本機用的 `src/merc.ini`。

若要手動檢查模板內容，至少留意以下三項：

```ini
NAME            <你的遊戲名稱>
MUD PORT        <連線埠號>
HOME DIRECTORY  <遊戲實際路徑>
```

若是部署到正式環境，再視需要將本機生成的 `merc.ini` 或等價設定配置到 `etc/merc.ini`。

環境對應重點：

- `Windows + WSL (Ubuntu)`：`HOME DIRECTORY` 應對到 WSL 路徑，例如 `/mnt/h/...`
- `macOS + Docker (Ubuntu)`：若在容器內測試，`HOME DIRECTORY` 應對到容器掛載路徑，例如 `/workspace/merc-fju-3.0`

## 啟動

```bash
# 推薦：Windows + WSL (Ubuntu) / 一般 bash 環境
cd src
./startup.bash &

# 保留：legacy csh 版本
cd src
./startup &
```

`startup.bash` 是目前建議的本機開發入口；它會從 `src/merc.sample.ini` 自動產生 `src/merc.ini`，並把 `HOME DIRECTORY` 改成目前 repo 根目錄。  
`startup` 仍保留作為 legacy `csh` 啟動腳本，供舊流程與相容用途使用。

若是在 Windows + WSL 環境下想從 IDE 直接啟動，可使用 repo 根目錄的 `startup-wsl.ps1`。該腳本會依自己的所在位置動態換算 WSL 路徑，再轉呼叫 `src/startup.bash`，不需要在腳本內寫死每台機器的 repo 路徑。

若是在 `macOS + Docker (Ubuntu)` 驗證 Linux 啟動，可在容器內做 smoke test：

```bash
docker run --rm -v "$PWD":/workspace/merc-fju-3.0 -w /workspace/merc-fju-3.0 \
  ubuntu:24.04 bash -lc '
    apt-get update &&
    apt-get install -y build-essential perl &&
    mkdir -p log player mail debug vote &&
    make -C src -f Makefile.lin merc &&
    rm -f debug/* &&
    timeout 60s bash -lc "cd src && ./startup.bash"
  '
```

驗證成功時，請在最新 `log/*.log` 尋找：
- `三國歪傳之降龍伏虎開始正常運作.`

即使看到成功訊號，仍要檢查 `debug/*` 是否有新產生的 warning / error。

第一個連線的玩家將成為超級管理者（Implementor）。

若遇問題，請查閱 `log/` 或 `debug/` 目錄中的錯誤訊息。

## 版權

本版本基於 **Merc 2.2**，版權需遵守 `doc/diku-license.doc` 及 `doc/merc-license-terms.txt` 的 Diku/Merc 授權條款。

本地修改版（三國歪傳製作群）版權說明請見 [document/COPYRIGHT](document/COPYRIGHT)，重點摘要：

- 限制範圍目錄：`src/`、`area/`、`angel/`、`data/`、`greeting/`、`social/`、`document/`、`etc/`、`help/`、`edit/`
- 可自由修改與再發行，**不得涉及商業行為**
- 公開架設須保留 Diku、Merc 及「三國歪傳之降龍伏虎」字樣
- 公開架設區域不得含有釋放版本區域（limbo 除外）
- 詳細規定請閱讀 [document/COPYRIGHT](document/COPYRIGHT)

## 原始製作群

| 姓名 | 學校／所系 | Email |
|------|-----------|-------|
| 蘇家興 | 輔仁大學化學研究所 86 期 | paul@mud.ch.fju.edu.tw |
| 周昀瑾 | 輔仁大學生物研究所 86 期 | lc@mud.ch.fju.edu.tw |
| 黃欣偉 | 輔仁大學化學研究所 85 期 | robinl@mud.ch.fju.edu.tw |
| 高智亮 | 師範大學化學研究所 85 期 | lumo@mud.ch.fju.edu.tw |
| 徐國財 | 輔仁大學化學研究所 84 期 | ene@mud.ch.fju.edu.tw |

## 翻新測試人

| 姓名 | 學校／所系 | Email |
|------|-----------|-------|
| 朱立恆 | 輔仁大學資管學系 95 期 | 495742481@m365.fju.edu.tw |

> 感謝原團隊與社群貢獻；若需完整歷史說明、原始說明書或轉檔腳本，
> 請查閱 `document/` 目錄（保留所有舊版 README／授權）以及 `convert_big5_to_utf8.py`。

## UTF-8 轉換說明

本 fork 使用 [convert_big5_to_utf8.py](scripts/convert_big5_to_utf8.py) 將原始 Big5/CP950 編碼的大量（近三千個）文字檔批次轉換為 UTF-8，以利現代工具鏈與版本控制使用。轉換腳本會：

- 依序嘗試 `utf-8`、`utf-8-sig`、`big5hkscs`、`cp950` 等常見編碼來解碼來源檔案，並記錄實際來源編碼。
- 僅在需要時重新寫入 UTF-8，若原檔已是 UTF-8 則自動跳過，並在輸出摘要顯示各類統計。
- 保留 ANSI 色碼/控制符，另針對個別檔案（如 `area/new/roo/458.roo`）在轉換前修正不合法位元組。

執行完成後再跑一次腳本即可驗證整個 repo（排除 `.DS_Store` 等二進位檔）均可成功以 UTF-8 解碼。
