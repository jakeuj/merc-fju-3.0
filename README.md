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

## 編譯

```bash
# 一般 Linux
cd src
make clean && make

# FreeBSD
cp Makefile.bsd Makefile
cd src
make clean && make
```

編譯完成後，`src/` 目錄下會產生可執行檔 `merc`。

## 設定

編輯 `etc/merc.ini`，至少設定以下三項：

```ini
NAME            <你的遊戲名稱>
MUD PORT        <連線埠號>
HOME DIRECTORY  <遊戲實際路徑>
```

## 啟動

```bash
cd src
./startup &
```

第一個連線的玩家將成為超級管理者（Implementor）。

若遇問題，請查閱 `log/` 或 `debug/` 目錄中的錯誤訊息。

## 版權

本版本基於 **Merc 2.2**，版權需遵守 `doc/license.doc` 及 `doc/license.txt` 的 Diku/Merc 授權條款。

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
