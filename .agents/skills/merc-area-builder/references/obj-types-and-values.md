# Object Types And Values

## 何時讀這份
- 你已經知道 `.obj` 主欄位，但不確定 `ItemType`、`Value*`、裝備位置或旗標該怎麼配。
- 你正在處理武器、防具、食物、飲料容器、卷軸、藥水、容器等不同物件型態。

## 搭配閱讀
- `references/obj-file-layout.md`
- `references/obj-core-fields.md`
- `docs/current-game/object-file-format.md`

## `ItemType`

`ItemType` 決定這個物件的玩法身份，也決定 `Value*` 的解讀方式。

常見型態：

- `ITEM_WEAPON`
- `ITEM_ARMOR`
- `ITEM_CONTAINER`
- `ITEM_DRINK_CON`
- `ITEM_FOOD`
- `ITEM_POTION`
- `ITEM_PILL`
- `ITEM_SCROLL`
- `ITEM_WAND`
- `ITEM_STAFF`
- `ITEM_MONEY`
- `ITEM_BOOK`

## `Value*` 的解讀方式

沒有單一通用表可以安全涵蓋所有型態；實務上應這樣做：

1. 先確認 `ItemType`
2. 再找 repo 內已成功載入的同型態 working example
3. 最後回看 `document/obj.txt` 與 `src/load.c`

不要先決定值，再回頭硬套型態。

## 幾個高風險型態

### `ITEM_WEAPON`
- 常和傷害範圍、武器種類常數、裝備位置一起出現。
- 若搬修時忽略武器種類欄位，常會造成玩法表現與命名不一致。

### `ITEM_ARMOR`
- `Armor`、裝備位置、限制條件通常要一起看。

### `ITEM_CONTAINER`
- 內容量、關閉/上鎖特性與 reset 配套常連動。

### `ITEM_DRINK_CON`
- `Value*` 常涉及容量、剩餘量、液體類型與是否被污染。
- 若只照舊文件猜數字，容易出現能載入但玩法很怪的資料。

### `ITEM_FOOD`
- repo 任務裡是高風險欄位之一。
- 不要只抄別區數值；先看已成功載入的食物範例，再對照 loader 行為。

## 旗標與裝備位置

`.obj` 常會同時碰到：

- item extra flags
- wear flags
- `WearLoc`

這三者容易被混成同一件事，但它們語意不同：

- extra flags：描述物件性質
- wear flags：描述可穿戴/可操作方式
- `WearLoc`：實際裝上的位置

## Repo-specific guardrail

- 若這輪有新增或修改 `obj/*.obj`，特別是特殊 `ItemType`，先比對 repo 內已成功載入的同類範例，不要只靠 legacy 常數表猜。
- area source 不要混入 save/runtime 風格的 `Keywords / ExtraFlags / WearFlags` 欄位名。
- `ITEM_FOOD`、`ITEM_DRINK_CON`、武器型態是最常需要先找 working example 的三類。
