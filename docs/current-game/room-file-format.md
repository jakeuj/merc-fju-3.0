---
layout: default
title: Room File Format
---

# `.roo` 房間檔格式說明

這頁整理 `document/room.txt` 的主要內容，方便在 GitHub Pages 上快速查 `.roo` 欄位與區塊。

## Source Of Truth

- legacy 文件來源：`document/room.txt`
- 現行 room loader / movement 行為以這些檔案為準：
  - `src/load.c`
  - `src/act_move.c`
  - `src/merc.h`
  - repo 內已成功載入的 `area/*/roo/*.roo`

## 檔案位置

```text
area/<area>/roo/*.roo
```

## 基本格式

```text
Vnum            <number>
Name            <string>~
Description
<multiline text>
~
SectorType      <number or symbol>
<room flags>    Yes

#Exit
Direction       <number or symbol>
ExitVnum        <number>
ExitDesc        <string>~
ExitKeyword     <string>~
Message         <string>~
ExitKey         <number>
<exit flags>    Yes
End

#Keyword
Keyword         <string>~
Description
<multiline text>
~
End

#Job
Keyword         <string>~
Function        <string>~
Position        <number or symbol>
End

End
```

## 主要欄位

| 欄位 | 用途 |
| --- | --- |
| `Vnum` | 房間號碼 |
| `Name` | 房間名稱 |
| `Description` | 進房時看到的完整描述 |
| `SectorType` | 地形類型 |
| 房間旗標 | 定義房間性質，例如安全區、銀行、不可戰鬥 |

## `SectorType`

文件列出的常見地形有：

- `SECT_INSIDE`
- `SECT_CITY`
- `SECT_FIELD`
- `SECT_FOREST`
- `SECT_HILLS`
- `SECT_MOUNTAIN`
- `WATER_SWIM`
- `WATER_NOSWIM`
- `SECT_AIR`
- `SECT_DESERT`

這些值同時影響移動消耗。

## 房間旗標

`document/room.txt` 列出常見旗標，例如：

- `Dark`
- `NoMob`
- `Indoors`
- `Private`
- `Safe`
- `ForeverLight`
- `NoRecall`
- `DepositMoney`
- `StoreRoom`
- `NoFight`
- `NoQuit`
- `Club`
- `Memorize`
- `Stock`
- `NoWhere`
- `Sail`
- `Fane`
- `Killer`
- `Standard`

這些旗標決定玩家在房間裡可做的事與系統功能。

## `#Exit`

出口區塊常見欄位：

- `Direction`
- `ExitVnum`
- `ExitDesc`
- `ExitKeyword`
- `Message`
- `ExitKey`
- 出口旗標

這是 `.roo` 最關鍵的結構之一。雖然舊文件用傳統出口概念說明，但目前 repo 實作還要一起看 `src/act_move.c` 與現況 area 範例。

## `#Keyword`

房內可 `look <keyword>` 的額外描述。

## `#Job`

讓房間可依關鍵字呼叫 `job.c` 內函式；這對解謎、互動牆面、交通節點都很重要。

## 實務提醒

- 房間拓樸不要只靠文件猜，先比對目標 area 現存 `roo/` 與 `map.md`。
- 若 prose spec 與 runtime `.roo` 不一致，spec-first area 應以 `mapmd-json` 與規劃檔為準，再投影到 `.roo`。
- 若房間提示某個特殊動作可用，不代表功能一定存在；要再查 `#Job` 或 `do_*`。

## 建議搭配閱讀

- [Legacy `document/` 入口](./legacy-documentation.html)
- `document/room.txt`
- `src/load.c`
- `src/act_move.c`
- `area/*/map.md`
- repo 內既有 `area/*/roo/*.roo`
