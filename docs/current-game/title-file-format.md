---
layout: default
title: Area Index File Format
---

# `index` 區域標題檔格式說明

這頁整理 `document/title.txt` 的內容。舊文件把區域根目錄中的 `index` 檔稱為「標題檔案」。

## Source Of Truth

- legacy 文件來源：`document/title.txt`
- 現行 area metadata 與載入行為請再交叉比對：
  - `src/load.c`
  - repo 內既有 `area/*/index`
  - `area/directory.lst`

## 檔案位置

對每個 area 來說，區域根目錄中的 `index` 就是這份 metadata：

```text
area/<area>/index
```

## 基本格式

```text
Echo          <symbol or number>
Editor        <string>~
Name          <string>~
Flags         <symbol or number>
Upper         <symbol or number>
Lower         <symbol or number>
Fog           <number>
Serial        <number>
Capital       <number>
Description
<multiline text>
~

End
```

## 主要欄位

| 欄位 | 用途 |
| --- | --- |
| `Echo` | 區域是否對一般玩家顯現 |
| `Editor` | 區域編輯者 |
| `Name` | 區域名稱 |
| `Flags` | 區域旗標 |
| `Upper` / `Lower` | 建議等級範圍 |
| `Fog` | 迷霧機率 |
| `Serial` | 區域序號 |
| `Capital` | 出生城房號 |
| `Description` | `area help` 補充說明 |

## 常見常數

### `Echo`

- `NO_ECHO`
- `WILL_ECHO`

### 等級

- `LEVEL_GOD`
- `LEVEL_SUP`
- `LEVEL_DEI`
- `LEVEL_ANG`
- `LEVEL_HER`
- `LEVEL_IMM`
- `LEVEL_PC`

### 區域旗標

- `SECTION_FLY`
- `SECTION_SWIM`
- `SECTION_NEWHAND`

## 文件中的重點說明

- `Editor` 與 `Name` 一定要有。
- `Upper` / `Lower` 表示建議逛區等級。
- `Capital` 若非 0，會把該區視為新玩家可選的出生城。
- `Description` 會用在 area help 類型的輔助說明。

## 對 area 規劃最有用的部分

- `Serial` 把房號區間和區域識別綁在一起。
- `Capital` 直接影響出生地與 recall。
- `Flags` 讓整個區域可套用統一屬性，例如新手區。

## 建議搭配閱讀

- [Legacy `document/` 入口](./legacy-documentation.html)
- `document/title.txt`
- `area/directory.lst`
- repo 內既有 `area/*/index`
