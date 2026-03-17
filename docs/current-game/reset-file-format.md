---
layout: default
title: Reset File Format
---

# `.res` 重置檔格式說明

這頁把 `document/reset.txt` 的重點整理成可直接閱讀的 Pages 版本。

## Source Of Truth

- legacy 文件來源：`document/reset.txt`
- 現行 reset 行為仍應回看：
  - `src/db.c`
  - `src/load.c`
  - repo 內已成功載入的 `area/*/res/*.res`

## 檔案位置

```text
area/<area>/res/*.res
```

## 基本格式

`.res` 是逐行命令式格式，常見指令有：

```text
M <mob_vnum> <limit>   <room_vnum>     <comment>
O <obj_vnum> <const>   <room_vnum>     <comment>
P <obj_vnum> <const>   <obj_vnum>      <comment>
G <obj_vnum> <mob_vnum>                <comment>
E <obj_vnum> <mob_vnum> <wear_loc>     <comment>
D <room_vnum> <exit>   <door_state>    <comment>
R <room_vnum> <exit>                   <comment>
A <mob_vnum>                            <comment>
```

## 指令意義

| 指令 | 用途 |
| --- | --- |
| `M` | 生成怪物 |
| `O` | 把物件放進房間 |
| `P` | 把物件放進另一個物件內 |
| `G` | 把物件交給怪物 |
| `E` | 把物件裝備到怪物身上 |
| `D` | 設定門/出口狀態 |
| `R` | 隨機化出口方向 |
| `A` | 讓怪物在 reset 時騎馬 |

## 執行模型

文件與目前 loader 在「結束符號」上有一個重要差異：

- legacy 文件把 `S` 視為 reset 結束行
- 目前 `src/load.c` 的 `load_resets()` 實作是一路讀到 EOF，沒有特判 `S`

因此在目前 repo 實務上，`S` 不應當作必要 terminator；若真的放 literal `S`，反而可能被當成一般命令讀壞。

## 目前 repo 應採用的寫法

- 一行一個 reset 指令
- 使用 `M / O / P / G / E / D / R / A`
- 檔案直接以 EOF 結束
- 不要混入 `#MOB / #OBJ / Room / MaxInArea / MaxInRoom` 這類 block-style 寫法
- 不要再額外放 literal `S`

文件說明 reset 會在：

- 系統啟動時先完整跑一輪
- 之後依區域時間週期重置

對目前工作最重要的理解是：`.res` 是「照順序逐行執行」的，因此資料先後順序很重要。

## 幾個關鍵規則

- `G`、`P`、`E`、`A` 這類命令依賴前面已經建立的怪物或物品。
- `E` 的裝備位置必須合法，例如 `WEAR_WIELD`、`WEAR_HEAD`。
- `D` 只適用於本來就能開關/上鎖的門。
- `R` 可做平面或立體迷宮式亂數出口。

## 常見常數

### 裝備位置

文件列出：

- `WEAR_LIGHT`
- `WEAR_FINGER_L`
- `WEAR_FINGER_R`
- `WEAR_NECK_1`
- `WEAR_NECK_2`
- `WEAR_BODY`
- `WEAR_HEAD`
- `WEAR_LEGS`
- `WEAR_FEET`
- `WEAR_HANDS`
- `WEAR_ARMS`
- `WEAR_SHIELD`
- `WEAR_ABOUT`
- `WEAR_WAIST`
- `WEAR_WRIST_L`
- `WEAR_WRIST_R`
- `WEAR_WIELD`
- `WEAR_HOLD`
- `WEAR_EARRING_L`
- `WEAR_EARRING_R`

### 門狀態

- `DOOR_OPEN`
- `DOOR_CLOSED`
- `DOOR_LOCKED`

## 實務提醒

- reset 問題常常不是語法錯，而是參照到不存在或載入順序不對的 VNUM。
- 商店賣什麼，常常是 `.shp` 類型 + `.res` 給老闆的物品一起決定。
- 新 area 驗證時，`.res` 要和 `mob/obj/roo/shp` 一起看，不要單看單檔。

## 建議搭配閱讀

- [Legacy `document/` 入口](./legacy-documentation.html)
- `document/reset.txt`
- [`.mob` 怪物檔格式說明](./mobile-file-format.html)
- [`.obj` 物品檔格式說明](./object-file-format.html)
- [`.shp` 商店檔格式說明](./shop-file-format.html)
- `src/db.c`
