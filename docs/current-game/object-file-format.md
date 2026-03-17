---
layout: default
title: Object File Format
---

# `.obj` 物品檔格式說明

這頁把 `document/obj.txt` 整理成 GitHub Pages 可直接查閱的版本，供目前 repo 的 area / object data work 使用。

## Source Of Truth

這份說明的主要依據與邊界如下：

- legacy 文件來源：`document/obj.txt`
- loader 與常數仍以現行 repo 為準：
  - `src/load.c`
  - `src/merc.h`
  - `data/symbol.def`
  - repo 內已成功載入的 `area/*/obj/*.obj`

若這頁和 runtime 行為不同，優先相信現行 loader，並回頭修正文檔。

## 檔案位置

所有 area 物品檔放在：

```text
area/<area>/obj/*.obj
```

每個 `.obj` 檔代表一個物品定義；整個 area 的物品集合由這些檔案組成。

## 基本格式

```text
#OBJECT
Vnum            <number>
Name            <string>~
ShortDesc       <string>~
LongDesc        <string>~
Description
<multiline text>
~
Unit            <string>~
ItemType        <number or symbol>
<extra flags>   Yes
<wear flags>    Yes
WearLoc         <number or symbol>
Level           <number>
Value           <up to 15 values>
Weight          <number>
Cost            <number>
Exp             <number>
Armor           <number>
Disappear       <number or symbol>

#Affect
...
End

#Extra
...
End

#Job
...
End

#Restrict
...
End

#Message
...
End

End
```

## 最小必填欄位

以 `document/obj.txt` 的描述來看，實務上最少要先把這幾個欄位寫完整：

| 欄位 | 用途 |
| --- | --- |
| `Vnum` | 物品虛擬編號，area 內物件不可重複 |
| `Name` | 英文關鍵名，玩家指令與系統辨識會用到 |
| `ShortDesc` | 物品短描述，顯示於持有/裝備列表 |
| `Description` | 物品出現在房間時的敘述 |
| `ItemType` | 物品類型，決定 `Value*` 的解讀方式 |

其他像 `Unit`、`WearLoc`、`Weight`、`Cost`、`Level` 則有機會依類型或預設值省略，但建議不要只靠預設值撐所有資料。

## 範例

```text
#OBJECT
Vnum            300
Name            sword~
ShortDesc       黑鐵劍(sword)~
Description
一把由黑鐵打造的長劍(sword)。
~
Unit            把~
ItemType        ITEM_WEAPON
Glow            Yes
Hum             Yes
Takeable        Yes
WearLoc         ITEM_WEAR_HANDS
Level           1
Value           10 20 0 WEAPON_SWORD
Weight          20
Exp             150
Cost            1000

#Affect
Location        APPLY_STR
Modifier        1
End

#Extra
Keyword         head~
Description
看看它的劍頭就知道死在它手下的人不少吧﹗
~
End

#Restrict
Type            RES_SKILL
Value           SLOT_NONAME
ViceValue       30
End

End
```

## 主要欄位

| 欄位 | 說明 |
| --- | --- |
| `Vnum` | 物品號碼。文件建議和 area 房號對照，方便維護。 |
| `Name` | 最短英文名，建議保留英文，便於指令辨識。 |
| `ShortDesc` | 中文短描述，最好包含 `Name` 的英文關鍵字。 |
| `LongDesc` | 舊文件註記目前未必有實際用途，可視需要補。 |
| `Description` | 房間中可見的完整描述；內容從下一行開始，到 `~` 結束。 |
| `Unit` | 物品單位，例如「把」「個」「件」。 |
| `ItemType` | 物品型態，可寫數值或字串常數；建議寫常數。 |
| `WearLoc` | 裝備位置，可省略；未裝備型物件通常為 0。 |
| `Level` | 物品等級，文件預設值為 `1`。 |
| `Weight` | 重量，文件預設值為 `1`。 |
| `Cost` | 價值，文件說明預設約為等級乘十。 |
| `Armor` | 裝備強度，主要給防具用。 |
| `Exp` | 升級經驗，只對武器/防具有意義。 |
| `Disappear` | 丟棄後是否消失，常數為 `YES` / `NO`。 |

## `ItemType` 常見類型

| 常數 | 說明 |
| --- | --- |
| `ITEM_WEAPON` | 武器 |
| `ITEM_ARMOR` | 防具 |
| `ITEM_POTION` | 藥水 |
| `ITEM_PILL` | 藥丸 |
| `ITEM_SCROLL` | 卷軸 |
| `ITEM_WAND` | 法杖 |
| `ITEM_STAFF` | 法器 |
| `ITEM_CONTAINER` | 容器 |
| `ITEM_DRINK_CON` | 裝水容器 |
| `ITEM_FOOD` | 食物 |
| `ITEM_MONEY` | 金錢 |
| `ITEM_BOOK` | 秘笈 |
| `ITEM_ARROW` | 箭 |
| `ITEM_BACKBAG` | 弓箭袋 |

`document/obj.txt` 還列出完整的 `ITEM_*` 常數表；若要新增較少見類型，建議對照 `data/symbol.def` 與現存範例一起確認。

## 額外旗標與穿戴旗標

文件把物品旗標分成兩種：

1. 額外旗標，例如 `Glow Yes`、`Magic Yes`、`NoDrop Yes`
2. 穿戴旗標，目前文件明確列出的是 `Takeable Yes`

常見額外旗標包含：

- `Glow`
- `Hum`
- `Evil`
- `Invis`
- `Magic`
- `NoDrop`
- `Bless`
- `NoRemove`
- `Inventory`
- `NoSave`
- `Contraband`
- `Loadable`

這些旗標可組合使用。文件特別提醒像 `NoDrop`、`NoRemove`、`Contraband` 這類限制型旗標不要濫加。

## `WearLoc` 常見位置

| 常數 | 說明 |
| --- | --- |
| `ITEM_WEAR_FINGER` | 手指 |
| `ITEM_WEAR_NECK` | 頸部 |
| `ITEM_WEAR_BODY` | 身上 |
| `ITEM_WEAR_HEAD` | 頭部 |
| `ITEM_WEAR_LEGS` | 腿部 |
| `ITEM_WEAR_FEET` | 腳部 |
| `ITEM_WEAR_HANDS` | 手部 |
| `ITEM_WEAR_ARMS` | 手臂 |
| `ITEM_WEAR_SHIELD` | 盾牌 |
| `ITEM_WEAR_ABOUT` | 背上 |
| `ITEM_WEAR_WAIST` | 腰部 |
| `ITEM_WEAR_WRIST` | 手腕 |
| `ITEM_WIELD` | 裝備為武器 |
| `ITEM_HOLD` | 握持 |
| `ITEM_WEAR_EARRING` | 耳朵 |
| `ITEM_WEAR_BACK` | 背袋 |
| `ITEM_WEAR_LIGHT` | 照明 |

## `Value` / `Value0..Value14`

`Value` 是物品真正的參數區。文件允許兩種寫法：

- 單行：`Value <v0> <v1> ...`
- 分欄：`Value0` 到 `Value14`

不同 `ItemType` 會用到不同欄位。

### 武器 `ITEM_WEAPON`

| 欄位 | 意義 |
| --- | --- |
| `Value1` | 最小傷害，`-1` 表示交給系統 |
| `Value2` | 最大傷害，`-1` 表示交給系統 |
| `Value3` | 武器種類，例如 `WEAPON_SWORD` |

### 防具 `ITEM_ARMOR`

| 欄位 | 意義 |
| --- | --- |
| `Value0` | 防護等級，`-1` 表示交給系統 |

### 容器 `ITEM_CONTAINER`

| 欄位 | 意義 |
| --- | --- |
| `Value1` | 可放重量 |
| `Value2` | 容器狀態，像 `CON_CAN_OPEN`、`CON_CLOSE`、`CON_LOCKED` |
| `Value3` | 鑰匙號碼 |

### 裝水容器 `ITEM_DRINK_CON`

| 欄位 | 意義 |
| --- | --- |
| `Value1` | 容量上限 |
| `Value2` | 目前容量 |
| `Value3` | 液體種類，例如 `LIQ_WATER` |
| `Value4` | 非 0 表示有毒 |

### 食物 `ITEM_FOOD`

| 欄位 | 意義 |
| --- | --- |
| `Value0` | 有效期限；`-1` 表示不消失 |
| `Value1` | 份量 / 次數 |
| `Value2` | 每口消耗量與飽足感 |
| `Value3` | 非 0 表示有毒 |
| `Value4` | 吃完後產生的物品 VNUM |

### 消耗品

`ITEM_SCROLL`、`ITEM_POTION`、`ITEM_PILL` 共用類似欄位：

| 欄位 | 意義 |
| --- | --- |
| `Value1` | 影響數值 |
| `Value2` | 影響類別，例如補血、補法、補體、鑑定 |

### 其他類型

`document/obj.txt` 對 `ITEM_LIGHT`、`ITEM_WAND`、`ITEM_STAFF`、`ITEM_MONEY` 等也有欄位說明；若這輪真的要做這些類型，建議直接回看原始 `document/obj.txt` 與現存範例一起對。

## 區塊欄位

### `#Affect`

用來改變角色屬性或衍生數值，常見欄位：

- `Location`
- `Modifier` 或 `Value`
- `End`

`Location` 可用 `APPLY_STR`、`APPLY_DEX`、`APPLY_INT`、`APPLY_CON`、`APPLY_HITROLL`、`APPLY_DAMROLL` 等常數。

### `#Extra`

讓玩家可對物件做額外 `look <keyword>`：

- `Keyword`
- `Description`
- `End`

這很適合書頁、器物刻字、封印紋路、道具說明牌這類互動。

### `#Job`

讓物件可觸發 `job.c` 內定義的特殊函式：

- `Keyword`
- `Function`
- `Position`
- `End`

### `#Restrict`

控制裝備或使用限制：

- `Type`
- `Skill`
- `Value`
- `ViceValue`
- `End`

文件列出的 `Type` 包含能力、職業、性別、信任值、技能熟練度等限制。

### `#Message`

自訂在 `eat`、`wear`、`drop`、`study` 等動作時顯示的訊息：

- `Type`
- `String`
- `Self`
- `Others`
- `End`

這區也支援 `$n`、`$p`、`$C`、`$0` 這類替換碼與顏色控制碼。

## 文件中的幾個實務提醒

- 關鍵字不一定要照文件順序排列。
- 但若有 `#Affect`、`#Extra`、`#Job`、`#Restrict`、`#Message`，要先定義 `Vnum`，否則 loader 可能出錯。
- 文件明確建議盡量使用字串常數，不要硬寫數字。
- 若新增 `mob/*.mob` 或 `obj/*.obj`，不要只照文件猜 parser，還要對照 repo 內已成功載入的同類型範例。

## 建議搭配閱讀

- [Legacy `document/` 入口](./legacy-documentation.html)
- `document/obj.txt`
- `document/room.txt`
- `document/reset.txt`
- `src/load.c`
- `data/symbol.def`

## 後續可補的方向

如果要把這頁補完整，下一步最值得加的是：

- 完整 `ITEM_*` / `WEAPON_*` / `APPLY_*` 常數查表
- `#Message` 的所有 `ACT_WHEN_*` 事件表
- 目前 repo 實際可載入 `.obj` 範例對照
- 與 loader 差異的「現況修正註記」
