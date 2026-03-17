---
layout: default
title: Shop File Format
---

# `.shp` 商店檔格式說明

這頁整理 `document/shop.txt` 的主要欄位與使用方式。

## Source Of Truth

- legacy 文件來源：`document/shop.txt`
- 現行商店行為仍應交叉比對：
  - `src/load.c`
  - `src/job.c`
  - repo 內既有 `area/*/shp/*.shp`
  - 對應的 `mob/*.mob` 與 `res/*.res`

## 檔案位置

```text
area/<area>/shp/*.shp
```

一個 `.shp` 通常代表一間商店。

## 基本格式

```text
Type            <number or symbol>
Keeper          <mob_vnum>

Object          <v1> <v2> <v3> <v4> <v5>
Horse           <v1> <v2> <v3> <v4> <v5>
Mercenary       <v1> <v2> <v3> <v4> <v5>
OpenHour        <number>
CloseHour       <number>
SellProfit      <number>
BuyProfit       <number>
Sential         <room_vnum>

End
```

## 主要欄位

| 欄位 | 用途 |
| --- | --- |
| `Type` | 商店類型 |
| `Keeper` | 店長怪物 VNUM |
| `Object` | 商店可賣的種類或類別 |
| `Horse` | 馬房販售清單 |
| `Mercenary` | 傭兵販售清單 |
| `OpenHour` / `CloseHour` | 營業時間 |
| `SellProfit` | 向玩家買入的價格比例 |
| `BuyProfit` | 賣給玩家的價格比例 |
| `Sential` | 老闆駐點房間 |

## `Type` 常見類型

- `SHOP_STORE`
- `SHOP_SMITH`
- `SHOP_HOPER`
- `SHOP_MERCENARY`

文件內前段範例把馬房拼成 `SHOP_COPER`，附註常數表則寫 `SHOP_HOPER`；這正是 legacy 文件與現行常數可能有落差的例子，實作時要以 loader 與現存範例為準。

## `Object` 在做什麼

這裡設定的是「商店允許交易哪些類型」，不是實際已經放到老闆身上的商品清單。

真正會賣什麼，仍要另外在 `.res` 裡把物件 `G` 給店長。

## 文件特別提醒的重點

- `Keeper` 對應的怪物必須存在，而且要比商店資料更早被系統認得。
- 一間商店最多列五個 `Object` / `Horse` / `Mercenary` 項目。
- 24 小時商店可設：

```text
OpenHour        0
CloseHour       23
```

- 若店長會亂走，又同時設定 `Sential`，畫面行為會很怪。

## 和其他資料檔的關係

`.shp` 不能獨立理解，通常至少要一起看：

- `mob/*.mob`
  - 老闆 NPC 是否會移動、是否為商店角色
- `res/*.res`
  - 老闆身上實際拿了哪些商品
- `obj/*.obj`
  - 商品類型與售價是否合理

## 建議搭配閱讀

- [Legacy `document/` 入口](./legacy-documentation.html)
- `document/shop.txt`
- [`.mob` 怪物檔格式說明](./mobile-file-format.html)
- [`.obj` 物品檔格式說明](./object-file-format.html)
- [`.res` 重置檔格式說明](./reset-file-format.html)
