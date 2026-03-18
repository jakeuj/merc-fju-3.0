# Shop File Layout

## 何時讀這份
- 你正在建立或修補 `area/<area>/shp/*.shp`。
- 你要確認 `Keeper`、`Object`、`Sential`、營業時間與商店類型。

## 搭配閱讀
- `references/reset-file-layout.md`
- `docs/current-game/shop-file-format.md`
- 對應 area 的 `mob/*.mob`、`obj/*.obj`、`res/*.res`

## 檔案位置

```text
area/<area>/shp/*.shp
```

通常一個 `.shp` 檔代表一間商店。

## 基本骨架

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

## 主欄位

### `Type`
- 商店類型。
- 以 repo working examples 和 loader 接受值為準。

### `Keeper`
- 店主怪物 VNUM。
- 必須真的存在，且該怪物不能已經掛了別的 shop 結構。

### `Object`
- 商店允許販售的物件類型或類別，不是完整實際庫存。

### `Horse`
- 馬房販售清單。

### `Mercenary`
- 傭兵販售清單。

### `OpenHour` / `CloseHour`
- 營業時間。

### `SellProfit` / `BuyProfit`
- 買入與賣出的價格比例。

### `Sential`
- 店主駐點房間。
- 若店主會亂走，通常要重新檢查這個設定是否合理。

## 實際賣什麼不是只看 `.shp`

真正會賣什麼，常常還要一起看：

- `.res` 是否把物件 `G` 給店長
- `.obj` 的類型與價格是否合理
- `.mob` 的店主是否真的存在且扮演商店角色

## Repo-specific guardrail

- legacy 文件前段範例曾寫 `SHOP_COPER`，但附註常數表與 current docs 走 `SHOP_HOPER`；遇到這種差異時，以 current loader 和 repo working examples 為準。
- `Keeper` / `Object` / `Sential` 必須一起對得上，否則 loader 雖可能載入，但玩法會明顯錯位。
