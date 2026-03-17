---
layout: default
title: Legacy Document References
---

# Legacy `document/` 參考手冊

這一頁把 repo 根目錄 `document/` 內的舊式參考手冊整理進 GitHub Pages，方便直接在站上查閱，不必再回到 raw text 檔案。

## 定位

- `document/` 是 Merc-FJU 舊版 area/data 撰寫手冊。
- 這批文件屬於 legacy authoring reference，不是目前 runtime 的唯一 source of truth。
- 真正會決定 loader 行為與常數接受範圍的，仍然是 `src/load.c`、`src/act_move.c`、`src/merc.h`、`data/symbol.def` 與 repo 內已成功載入的資料檔。

## 目前已轉成 Pages 可讀頁面

- [`document/README` 導讀](./legacy-readme.html)
- [`.mob` 怪物檔格式說明](./mobile-file-format.html)
- [`.obj` 物品檔格式說明](./object-file-format.html)
- [`.roo` 房間檔格式說明](./room-file-format.html)
- [`.res` 重置檔格式說明](./reset-file-format.html)
- [`.shp` 商店檔格式說明](./shop-file-format.html)
- [`index` 區域標題檔格式說明](./title-file-format.html)
- [Legacy 版權宣告](./copyright-notice.html)

## `document/` 原始手冊索引

| 原始檔案 | 用途 | 建議放在哪條閱讀路徑 |
| --- | --- | --- |
| `document/README` | 舊版安裝與 area 目錄概念總覽 | 先讀這份建立背景 |
| `document/mob.txt` | `.mob` 怪物檔格式 | area / NPC data work |
| `document/obj.txt` | `.obj` 物品檔格式 | 物件、掉落、商店、道具互動 |
| `document/reset.txt` | `.res` 重置格式 | reset / spawn / 掉落鏈 |
| `document/room.txt` | `.roo` 房間格式 | 房間、出口、關鍵字、互動 |
| `document/shop.txt` | `.shp` 商店格式 | 商店 NPC 與買賣設定 |
| `document/title.txt` | 舊版 title 相關資料 | 歷史參考 |
| `document/COPYRIGHT` | 授權與釋出聲明 | 法務與來源追溯 |

## 轉換完成狀態

| 原始檔案 | Pages 狀態 | 對應頁面 |
| --- | --- | --- |
| `document/README` | 已轉換 | [`legacy-readme.html`](./legacy-readme.html) |
| `document/mob.txt` | 已轉換 | [`mobile-file-format.html`](./mobile-file-format.html) |
| `document/obj.txt` | 已轉換 | [`object-file-format.html`](./object-file-format.html) |
| `document/reset.txt` | 已轉換 | [`reset-file-format.html`](./reset-file-format.html) |
| `document/room.txt` | 已轉換 | [`room-file-format.html`](./room-file-format.html) |
| `document/shop.txt` | 已轉換 | [`shop-file-format.html`](./shop-file-format.html) |
| `document/title.txt` | 已轉換 | [`title-file-format.html`](./title-file-format.html) |
| `document/COPYRIGHT` | 已轉換 | [`copyright-notice.html`](./copyright-notice.html) |

## 閱讀建議

1. 若你是在補現行 docs，先從 `document/README` 理解這批文件原本要解釋的目錄結構。
2. 若你是在做 area data，優先看對應檔種的手冊，再回頭用目前 repo 的實際範例交叉比對。
3. 若文字說明與目前 loader 行為不一致，以現行程式與可成功載入資料為準，並把差異補記到 `docs/current-game/`。

## 後續擴充方向

這批頁面先完成第一版 Pages 化；後續若要補強，最值得追加的是：

- `.mob` / `.roo` / `.res` / `.shp` 的 runtime loader 差異註記
- 與 repo 內成功載入範例的對照
- `document/title.txt` 和現行 `area/*/index` 差異說明
